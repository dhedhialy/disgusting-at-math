(function () {
  var PREFIX = "dmath:";
  var STRUGGLE_MS = 20 * 60 * 1000;
  var DAY = 24 * 60 * 60 * 1000;

  function read(key, fallback) {
    try {
      var raw = localStorage.getItem(PREFIX + key);
      if (raw == null) return fallback;
      return JSON.parse(raw);
    } catch (err) {
      return fallback;
    }
  }

  function write(key, value) {
    localStorage.setItem(PREFIX + key, JSON.stringify(value));
  }

  function checked(slug, stage) {
    return !!read("p:" + slug + ":" + stage, false);
  }

  function setChecked(slug, stage, value) {
    write("p:" + slug + ":" + stage, !!value);
  }

  function topicList() {
    return window.CURRICULUM || [];
  }

  function stages() {
    return window.STAGES || [];
  }

  function score(slug) {
    var n = 0;
    stages().forEach(function (s) {
      if (checked(slug, s.id)) n += 1;
    });
    return n;
  }

  function totalSlots() {
    return topicList().length * stages().length;
  }

  function totalChecked() {
    var n = 0;
    topicList().forEach(function (t) { n += score(t.slug); });
    return n;
  }

  function percent() {
    var slots = totalSlots();
    if (!slots) return 0;
    return Math.round((100 * totalChecked()) / slots);
  }

  function currentSlug() {
    var list = topicList().filter(function (t) { return t.group === "core"; });
    for (var i = 0; i < list.length; i++) {
      if (!checked(list[i].slug, "gate")) return list[i].slug;
    }
    return list.length ? list[list.length - 1].slug : "";
  }

  function bindChecks() {
    document.querySelectorAll("input[data-stage]").forEach(function (box) {
      var slug = box.getAttribute("data-slug");
      var stage = box.getAttribute("data-stage");
      box.checked = checked(slug, stage);
      if (box.getAttribute("data-bound")) return;
      box.setAttribute("data-bound", "1");
      box.addEventListener("change", function () {
        setChecked(slug, stage, box.checked);
        paint();
      });
    });
  }

  function paint() {
    document.querySelectorAll("input[data-stage]").forEach(function (box) {
      box.checked = checked(box.getAttribute("data-slug"), box.getAttribute("data-stage"));
    });
    var pct = percent();
    document.querySelectorAll("[data-overall]").forEach(function (el) {
      el.textContent = pct + "%";
    });
    document.querySelectorAll("[data-overall-bar]").forEach(function (el) {
      el.style.width = pct + "%";
    });
    var here = currentSlug();
    document.querySelectorAll("[data-here-label]").forEach(function (el) {
      var topic = topicList().filter(function (t) { return t.slug === here; })[0];
      el.textContent = topic ? topic.title : "Start at AP Precalculus";
    });
    document.querySelectorAll("[data-topic-score]").forEach(function (el) {
      var slug = el.getAttribute("data-topic-score");
      var n = score(slug);
      var m = stages().length;
      el.textContent = n + "/" + m;
      var row = el.closest("li");
      if (row) row.classList.toggle("here", slug === here);
      var bar = row && row.querySelector("[data-topic-bar]");
      if (bar) bar.style.width = Math.round((100 * n) / m) + "%";
    });
    paintDue();
    paintClocks();
    paintAttacks();
  }

  function startStamp(id) {
    return read("t:" + id, 0);
  }

  function paintClocks() {
    var now = Date.now();
    document.querySelectorAll("[data-clock]").forEach(function (el) {
      var id = el.getAttribute("data-clock");
      var start = startStamp(id);
      var btn = document.querySelector('[data-solution="' + id + '"]');
      if (!start) {
        el.textContent = "Timer not started. Twenty minutes of real work before a solution.";
        if (btn) btn.disabled = true;
        return;
      }
      var left = STRUGGLE_MS - (now - start);
      if (left <= 0) {
        el.textContent = "Twenty minutes are up. Reveal only if the writeup is actually written.";
        if (btn) btn.disabled = false;
      } else {
        var m = Math.floor(left / 60000);
        var s = Math.floor((left % 60000) / 1000);
        el.textContent = "Keep working. Solution locked for " + m + ":" + (s < 10 ? "0" : "") + s + ".";
        if (btn) btn.disabled = true;
      }
    });
  }

  function bindTimers() {
    document.querySelectorAll("[data-start]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var id = btn.getAttribute("data-start");
        if (!startStamp(id)) write("t:" + id, Date.now());
        paintClocks();
      });
    });
    document.querySelectorAll("[data-solution]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var id = btn.getAttribute("data-solution");
        var start = startStamp(id);
        if (!start || Date.now() - start < STRUGGLE_MS) return;
        var panel = document.getElementById("sol-" + id);
        if (panel) panel.hidden = !panel.hidden;
        btn.textContent = panel && panel.hidden ? "Reveal solution" : "Hide solution";
      });
    });
    document.querySelectorAll("[data-show-proof]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var panel = document.getElementById(btn.getAttribute("data-show-proof"));
        if (!panel) return;
        panel.hidden = !panel.hidden;
        btn.textContent = panel.hidden ? "I wrote a proof. Reveal." : "Hide proof";
      });
    });
  }

  function reviewState(id) {
    return read("r:" + id, { next: [] });
  }

  function bindReviews() {
    document.querySelectorAll("[data-log-review]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var id = btn.getAttribute("data-log-review");
        var state = reviewState(id);
        var now = Date.now();
        if (!state.next.length) {
          state.next = [now + DAY, now + 7 * DAY, now + 30 * DAY];
        } else {
          state.next = state.next.filter(function (t) { return t > now + 1000; });
        }
        write("r:" + id, state);
        paintDue();
      });
    });
  }

  function paintDue() {
    var box = document.getElementById("due-list");
    if (!box) return;
    var now = Date.now();
    var items = [];
    document.querySelectorAll("[data-bank-id]").forEach(function (el) {
      var id = el.getAttribute("data-bank-id");
      var state = reviewState(id);
      var due = (state.next || []).filter(function (t) { return t <= now; });
      if (due.length) {
        items.push("<li>" + el.getAttribute("data-bank-label") + " — due</li>");
      }
    });
    box.innerHTML = items.length ? items.join("") : "<li>Nothing due. Log a writeup to schedule 1 / 7 / 30 days.</li>";
  }

  function bindTransfer() {
    var exp = document.getElementById("export-progress");
    var imp = document.getElementById("import-progress");
    var file = document.getElementById("import-file");
    if (exp) {
      exp.addEventListener("click", function () {
        var dump = {};
        for (var i = 0; i < localStorage.length; i++) {
          var k = localStorage.key(i);
          if (k && k.indexOf(PREFIX) === 0) dump[k] = localStorage.getItem(k);
        }
        var blob = new Blob([JSON.stringify(dump, null, 2)], { type: "application/json" });
        var a = document.createElement("a");
        a.href = URL.createObjectURL(blob);
        a.download = "disgusting-at-math-progress.json";
        a.click();
      });
    }
    if (imp && file) {
      imp.addEventListener("click", function () { file.click(); });
      file.addEventListener("change", function () {
        var f = file.files && file.files[0];
        if (!f) return;
        var reader = new FileReader();
        reader.onload = function () {
          var data = JSON.parse(String(reader.result));
          Object.keys(data).forEach(function (k) {
            if (k.indexOf(PREFIX) === 0) localStorage.setItem(k, data[k]);
          });
          restoreGrades();
          paint();
        };
        reader.readAsText(f);
      });
    }
  }

  function bindFilters() {
    var topic = document.getElementById("filter-topic");
    var tier = document.getElementById("filter-tier");
    var q = document.getElementById("filter-q");
    if (!topic && !tier && !q) return;
    function apply() {
      var tv = topic ? topic.value : "all";
      var hv = tier ? tier.value : "all";
      var query = q ? q.value.trim().toLowerCase() : "";
      document.querySelectorAll("#resource-table tbody tr").forEach(function (row) {
        var okT = tv === "all" || row.getAttribute("data-topic") === tv;
        var okH = hv === "all" || row.getAttribute("data-tier") === hv;
        var okQ = !query || row.textContent.toLowerCase().indexOf(query) !== -1;
        row.hidden = !(okT && okH && okQ);
      });
    }
    [topic, tier, q].forEach(function (el) {
      if (!el) return;
      el.addEventListener("input", apply);
      el.addEventListener("change", apply);
    });
  }

  function fold(s) {
    var t = String(s || "").toLowerCase();
    t = t.replace(/[−–—]/g, "-");
    t = t.replace(/[’']/g, "");
    t = t.replace(/\\dfrac/g, "\\frac");
    t = t.replace(/\\frac\s*\{([^{}]+)\}\s*\{([^{}]+)\}/g, "($1)/($2)");
    t = t.replace(/\\sqrt\s*\{([^{}]+)\}/g, "sqrt($1)");
    t = t.replace(/√\s*\{([^{}]+)\}/g, "sqrt($1)");
    t = t.replace(/√\s*\(?([a-z0-9+\-]+)\)?/g, "sqrt($1)");
    t = t.replace(/\^\{([^{}]+)\}/g, "^($1)");
    t = t.replace(/\^\(([^()]+)\)/g, "^$1");
    t = t.replace(/π/g, "pi");
    t = t.replace(/θ/g, "theta");
    t = t.replace(/λ/g, "lambda");
    t = t.replace(/ω/g, "omega");
    t = t.replace(/ε/g, "epsilon");
    t = t.replace(/α/g, "alpha");
    t = t.replace(/≥/g, ">=");
    t = t.replace(/≤/g, "<=");
    t = t.replace(/\\(sin|cos|tan|log|ln|exp|pi|theta|lambda|omega|epsilon|alpha|infty|sin)/g, "$1");
    t = t.replace(/\\/g, "");
    t = t.replace(/[{}]/g, "");
    t = t.replace(/_/g, "");
    t = t.replace(/\s+/g, "");
    t = t.replace(/\*/g, "");
    return t;
  }

  function has(hay, needle) {
    var n = fold(needle);
    var h = fold(hay);
    if (!n) return false;
    if (/^-?\d+(\.\d+)?$/.test(n)) {
      var esc = n.replace(".", "\\.");
      return new RegExp("(^|[^0-9.^])" + esc + "([^0-9.]|$)").test(h);
    }
    if (/^[a-z]{1,3}$/.test(n) && /^[a-z]{1,3}$/.test(String(needle || "").toLowerCase().trim())) {
      return new RegExp("(^|[^a-z])" + n + "([^a-z]|$)").test(String(hay || "").toLowerCase());
    }
    return h.indexOf(n) !== -1;
  }

  function gradeById(id) {
    var list = window.GRADES || [];
    for (var i = 0; i < list.length; i++) {
      if (list[i].id === id) return list[i];
    }
    return null;
  }

  function draft(id) {
    return read("a:" + id, { work: "", answer: "", workOk: false, answerOk: false, missing: [] });
  }

  function workMissing(work, answer, need) {
    var missing = [];
    var text = String(work || "").trim();
    if (text.length < 80) missing.push("write the argument, not only the answer");
    if (text && fold(text) === fold(answer)) missing.push("put the argument in the work box and the conclusion on the answer line");
    (need || []).forEach(function (req) {
      var ok = (req.any || []).some(function (alt) { return has(text, alt); });
      if (!ok) missing.push(req.hint);
    });
    return missing;
  }

  function answerOk(answer, parts) {
    return (parts || []).every(function (alts) {
      return alts.some(function (alt) { return has(answer, alt); });
    });
  }

  function paintVerdict(id) {
    var el = document.querySelector('[data-verdict="' + id + '"]');
    if (!el) return;
    var d = draft(id);
    el.classList.remove("ok");
    if (!d.work && !d.answer) {
      el.textContent = "";
      return;
    }
    if (!d.judged) {
      el.textContent = "Saved in this browser. Not checked yet.";
      return;
    }
    if (d.workOk && d.answerOk) {
      el.classList.add("ok");
      el.textContent = "Counted. The work checks and the answer checks.";
      return;
    }
    var bits = [];
    if (d.workOk) bits.push("Work checks.");
    else if (d.missing && d.missing.length) bits.push("Work still open: " + d.missing.join("; ") + ".");
    else if (d.work || d.answer) bits.push("Work not checked yet.");
    if (d.answerOk) bits.push("Answer checks.");
    else if (d.answer) bits.push("Answer does not check.");
    else bits.push("Answer is empty.");
    el.textContent = bits.join(" ");
  }

  function paintAttacks() {
    var list = window.GRADES || [];
    var n = 0;
    list.forEach(function (g) {
      var d = draft(g.id);
      if (d.workOk && d.answerOk) n += 1;
    });
    var label = n + "/" + list.length;
    document.querySelectorAll("[data-attack-score]").forEach(function (el) {
      el.textContent = label;
    });
    var box = document.getElementById("attack-log");
    if (!box) return;
    var titles = {};
    topicList().forEach(function (t) { titles[t.slug] = t.title; });
    box.innerHTML = list.map(function (g) {
      var d = draft(g.id);
      var status = "not started";
      if (d.workOk && d.answerOk) status = "work checked, answer checked";
      else if (d.work || d.answer) {
        status = (d.workOk ? "work checked" : "work not checked") + ", " +
          (d.answerOk ? "answer checked" : "answer not checked");
      }
      var title = titles[g.slug] || g.slug;
      return "<li><a href=\"topics/" + g.slug + ".html#attack\">" + title + " · Attack " + g.n +
        "</a> — " + status + "</li>";
    }).join("");
  }

  function checkGrade(id) {
    var spec = gradeById(id);
    var form = document.querySelector('[data-grade="' + id + '"]');
    if (!spec || !form) return;
    var workEl = form.querySelector("[data-work]");
    var ansEl = form.querySelector("[data-answer]");
    var work = workEl ? workEl.value : "";
    var answer = ansEl ? ansEl.value : "";
    var missing = workMissing(work, answer, spec.need);
    var okA = answerOk(answer, spec.parts);
    write("a:" + id, {
      work: work,
      answer: answer,
      workOk: missing.length === 0,
      answerOk: okA,
      missing: missing,
      judged: true,
      at: Date.now()
    });
    paintVerdict(id);
    paintAttacks();
  }

  function restoreGrades() {
    document.querySelectorAll("[data-grade]").forEach(function (form) {
      var id = form.getAttribute("data-grade");
      var d = draft(id);
      var workEl = form.querySelector("[data-work]");
      var ansEl = form.querySelector("[data-answer]");
      if (workEl) workEl.value = d.work || "";
      if (ansEl) ansEl.value = d.answer || "";
      paintVerdict(id);
    });
    paintAttacks();
  }

  function bindGrades() {
    document.querySelectorAll("[data-grade]").forEach(function (form) {
      if (form.getAttribute("data-bound")) return;
      form.setAttribute("data-bound", "1");
      var id = form.getAttribute("data-grade");
      var workEl = form.querySelector("[data-work]");
      var ansEl = form.querySelector("[data-answer]");
      function persist() {
        var work = workEl ? workEl.value : "";
        var answer = ansEl ? ansEl.value : "";
        var cur = draft(id);
        if (work === (cur.work || "") && answer === (cur.answer || "")) return;
        write("a:" + id, {
          work: work,
          answer: answer,
          workOk: false,
          answerOk: false,
          missing: [],
          judged: false,
          at: Date.now()
        });
        paintVerdict(id);
        paintAttacks();
      }
      if (workEl) workEl.addEventListener("input", persist);
      if (ansEl) ansEl.addEventListener("input", persist);
      form.addEventListener("submit", function (ev) { ev.preventDefault(); checkGrade(id); });
    });
    restoreGrades();
    document.querySelectorAll("[data-check]").forEach(function (btn) {
      if (btn.getAttribute("data-bound")) return;
      btn.setAttribute("data-bound", "1");
      btn.addEventListener("click", function () { checkGrade(btn.getAttribute("data-check")); });
    });
  }

  function fileWarning() {
    var el = document.getElementById("file-warning");
    if (!el) return;
    if (location.protocol === "file:") {
      el.hidden = false;
    }
  }

  document.addEventListener("DOMContentLoaded", function () {
    bindChecks();
    bindTimers();
    bindReviews();
    bindTransfer();
    bindFilters();
    bindGrades();
    fileWarning();
    paint();
    setInterval(paintClocks, 1000);
  });
})();
