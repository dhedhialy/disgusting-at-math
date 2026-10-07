from bits import R, frame

ANA = {
    "slug": "real-analysis",
    "short": "Real analysis",
    "title": "Real Analysis",
    "track": "Math",
    "needs": ["calc-1", "proof-logic"],
    "what": """
<p>Real analysis is the repair job on calculus. Every limit, derivative, and integral you have used is given hypotheses and a proof, and the places the proof fails become the famous counterexamples: a continuous nowhere-differentiable function, a sequence of continuous functions whose limit is discontinuous, a derivative that is not integrable in the Riemann sense on a fat set. The spine is the completeness of the real line, sequential compactness, uniform continuity on compact intervals, the Riemann integral, and uniform convergence.</p>
<p>Rudin’s Principles of Mathematical Analysis is the ceiling. The third-edition ISBN catalogued for it is 978-0-07-054235-8. It is paid, and its exercises are qualifying-exam material. You should not open Rudin as the first book. Jiří Lebl’s Basic Analysis is free, careful, and enough to learn the subject. Abbott’s Understanding Analysis, ISBN 978-1-4939-2711-1, is the paid book people love because the motivation is written in English; use it if you buy one. Pugh, ISBN 978-3-319-17770-0, is the other paid route, with harder exercises. MIT 18.100 is the course with problem sets.</p>
<p>ε–δ is not a style. It is the definition. If you translate it into a picture and then stop writing inequalities, you have not done the proof.</p>
""",
    "attack": [
        {
            "q": "<p>Let \\(S=\\{x\\in\\mathbb{R}:x^2<2\\}\\). Using completeness, prove that \\(\\alpha=\\sup S\\) satisfies \\(\\alpha^2=2\\).</p>",
            "a": "<p>\\(S\\) is nonempty and bounded above, so \\(\\alpha\\) exists. If \\(\\alpha^2<2\\), a small enough positive increment stays in \\(S\\), contradicting the least-upper-bound property. If \\(\\alpha^2>2\\), a slightly smaller number is still an upper bound. The only remaining possibility is \\(\\alpha^2=2\\). Write the increments explicitly: if \\(\\alpha^2<2\\), choose \\(h>0\\) with \\(h<1\\) and \\(h<(2-\\alpha^2)/(2\\alpha+1)\\).</p>",
        },
        {
            "q": "<p>Prove that a convergent sequence is Cauchy.</p>",
            "a": "<p>If \\(a_n\\to L\\), take \\(\\varepsilon/2\\). Past \\(N\\), both \\(a_n\\) and \\(a_m\\) are within \\(\\varepsilon/2\\) of \\(L\\), so they are within \\(\\varepsilon\\) of each other by the triangle inequality.</p>",
        },
        {
            "q": "<p>Show that \\(f(x)=1/x\\) on \\((0,1]\\) is continuous but not uniformly continuous.</p>",
            "a": "<p>Continuity at each \\(c\\in(0,1]\\) is the usual reciprocal estimate. Not uniform: take \\(x_n=1/n\\), \\(y_n=1/(n+1)\\). The gaps go to 0 while \\(|f(x_n)-f(y_n)|=1\\). So no single \\(\\delta\\) serves \\(\\varepsilon=1/2\\).</p>",
        },
    ],
    "core": [
        {
            "name": "Completeness",
            "statement": "Every nonempty subset of \\(\\mathbb{R}\\) that is bounded above has a least upper bound. Equivalent forms: every Cauchy sequence converges; every monotone bounded sequence converges; nested closed intervals have nonempty intersection.",
            "proof": "<p>From the least-upper-bound property to monotone convergence: the supremum of the set of terms is the limit. Cauchy completeness from monotone convergence uses a subsequence of dyadic windows. You should write one direction in full and know the names of the others.</p>",
        },
        {
            "name": "Continuity",
            "statement": "Continuity at a point is the ε–δ definition. On a compact set, a continuous real function is uniformly continuous, bounded, and attains its max and min. The intermediate value theorem holds on an interval.",
            "proof": "<p>Uniform continuity on \\([a,b]\\): if it failed, sequences with gaps going to 0 and values separated by a fixed ε would have a convergent subsequence by Bolzano–Weierstrass, and continuity at the limit point would be contradicted. The extreme value theorem is the same compactness plus the fact that the image of an interval is an interval.</p>",
        },
        {
            "name": "Differentiation",
            "statement": "Differentiability implies continuity. The mean value theorem holds. There exist functions continuous everywhere and differentiable nowhere; you should know that Weierstrass built one, and be able to state what that forbids you from claiming.",
            "proof": "<p>Differentiability implies continuity because the difference \\(f(x)-f(a)=f'(a)(x-a)+o(x-a)\\) goes to 0. The mean value theorem is the one you already proved in calculus, now with hypotheses you do not skip. The nowhere-differentiable example is a uniform limit of a series of jagged continuous functions; read one construction in Lebl or Abbott and rewrite the estimate.</p>",
        },
        {
            "name": "Riemann integral",
            "statement": "A bounded function on \\([a,b]\\) is Riemann integrable if and only if for every \\(\\varepsilon>0\\) there is a partition whose upper and lower sums differ by less than \\(\\varepsilon\\). Continuous functions are integrable. A function with finitely many discontinuities is integrable. The fundamental theorem needs continuity of \\(f\\), or integrability of \\(f\\) plus continuity of \\(F\\) in the other direction, and you should state which form you mean.",
            "proof": "<p>Uniform continuity gives a partition where the oscillation on every subinterval is small, hence upper minus lower is small. Finite discontinuities are isolated in small intervals whose total length makes their contribution less than ε.</p>",
        },
        {
            "name": "Uniform convergence",
            "statement": "A uniform limit of continuous functions is continuous. The Weierstrass M-test gives uniform convergence of a series. Power series converge uniformly on compact subsets of the open interval of convergence, so they may be integrated and differentiated termwise there.",
            "proof": "<p>The ε/3 argument: choose one function in the sequence within ε/3 of the limit everywhere, then use its continuity. The M-test compares with a convergent numerical series. Termwise integration of power series follows from uniform convergence on a smaller closed interval.</p>",
        },
    ],
    "tiers": {
        "0": [R(
            "Tao, books page for Analysis I",
            "https://terrytao.wordpress.com/books/analysis-i/",
            "Read once, do not study from this. It is a prospectus for a construction of the reals. It tells you the subject is about building the line, not about computing more integrals.",
        )],
        "1": [R(
            "Jiří Lebl, Basic Analysis, and MIT 18.100A",
            "https://www.jirka.org/ra/realanal.pdf",
            "Free, current, and written as a course. The HTML home is https://www.jirka.org/ra/ . MIT 18.100A supplies another problem-set culture: https://ocw.mit.edu/courses/18-100a-real-analysis-fall-2020/ . Abbott, ISBN 978-1-4939-2711-1, is the paid book to buy if Lebl’s tone is too dry.",
        )],
        "2": [R(
            "18.100B and Pugh’s exercises",
            "https://ocw.mit.edu/courses/18-100b-real-analysis-spring-2025/",
            "18.100B is the harder MIT track. Pugh, Real Mathematical Analysis, ISBN 978-3-319-17770-0, is paid and is the exercise upgrade. Do the 18.100 sets either way.",
        )],
        "3": [R(
            "Rudin, Principles of Mathematical Analysis, ISBN 978-0-07-054235-8",
            "https://ocw.mit.edu/courses/18-100b-real-analysis-spring-2025/",
            "Baby Rudin is paid and is the qualifying-exam ceiling. No free legal PDF was verified. The link is 18.100B, the public problem set at that altitude. Work Rudin’s Chapter 1–8 exercises if you own the book. Do not read the solutions collections first.",
        )],
    },
    "hardest": [
        {
            "label": "Lebl, the exercises on completeness, uniform continuity, and uniform convergence",
            "url": "https://www.jirka.org/ra/realanal.pdf",
            "why": "They are written to be done. The hard ones are the counterexamples, which punish a missing quantifier.",
        },
        {
            "label": "MIT 18.100A problem sets",
            "url": "https://ocw.mit.edu/courses/18-100a-real-analysis-fall-2020/",
            "why": "A real course’s idea of a week of work, not a highlight.",
        },
        {
            "label": "MIT 18.100B",
            "url": "https://ocw.mit.edu/courses/18-100b-real-analysis-spring-2025/",
            "why": "The harder track. Use it when 18.100A feels like translation rather than struggle.",
        },
        {
            "label": "Rudin, Chapters 1–8, the exercises",
            "url": "https://www.jirka.org/ra/",
            "why": "Rudin is paid and unlinked as a file. This link is Lebl’s site, where you should be before you spend money. Rudin’s exercises are hard because the hints are absent and the theorems are stated at full strength.",
        },
        {
            "label": "Construct \\(\\sqrt{2}\\) from the least-upper-bound property, timed, blank page",
            "url": "https://www.jirka.org/ra/realanal.pdf",
            "why": "If this takes more than a clean page, completeness is still a word.",
        },
    ],
    "gate": "<p>Pass: written proofs, from memory, of: Cauchy sequences converge in \\(\\mathbb{R}\\) (one direction, named), uniform continuity of a continuous function on \\([a,b]\\), and the ε/3 proof that a uniform limit of continuous functions is continuous. Plus ten Lebl exercises you got wrong on the first attempt, rewritten. Fail if any proof swaps the order of quantifiers.</p>",
    "svg": frame(
        '<path d="M60 220 C 140 210, 180 120, 240 140 S 340 240, 400 160 520 80, 580 120" fill="none" stroke="#fff" stroke-width="1.5"/>'
        '<path d="M60 190 C 140 180, 180 90, 240 110 S 340 210, 400 130 520 50, 580 90" fill="none" stroke="rgba(255,255,255,0.45)"/>'
        '<path d="M60 250 C 140 240, 180 150, 240 170 S 340 270, 400 190 520 110, 580 150" fill="none" stroke="rgba(255,255,255,0.45)"/>'
        '<text x="70" y="80" fill="#bbb" font-size="13" font-family="Georgia, serif">ε tube</text>',
        label="An epsilon tube around a function",
    ),
    "caption": "Uniform continuity is one δ for the whole interval. Pointwise continuity is a δ that depends on the point.",
    "batches": [
        {"name": "The line", "items": [
            "Prove the archimedean property from the least-upper-bound property.",
            "Construct \\(\\sqrt{2}\\) as a supremum.",
            "Prove every monotone bounded sequence converges.",
            "Show that a set of reals with an upper bound has a least upper bound, by naming the axiom you use. Do not prove the axiom.",
            "Give a bounded set of rationals with no rational least upper bound.",
        ]},
        {"name": "Sequences", "items": [
            "Prove convergent implies Cauchy.",
            "Prove a Cauchy sequence is bounded.",
            "Bolzano–Weierstrass: every bounded sequence has a convergent subsequence. Write it.",
            "Give a sequence with two distinct limit points.",
            "Show \\((-1)^n\\) does not converge, from the definition.",
        ]},
        {"name": "Continuity and derivatives", "items": [
            "ε–δ proof that \\(x^2\\) is continuous at 3.",
            "Prove \\(1/x\\) is not uniformly continuous on \\((0,1]\\).",
            "Prove the intermediate value theorem.",
            "Prove the mean value theorem from Rolle, with hypotheses.",
            "Show differentiability implies continuity.",
        ]},
        {"name": "Integral and series of functions", "items": [
            "Prove a continuous function on \\([a,b]\\) is Riemann integrable.",
            "Give a function that is discontinuous at one point and still integrable.",
            "Prove the ε/3 argument for uniform limits.",
            "State the M-test and use it on \\(\\sum x^n/n^2\\) on \\([-1,1]\\).",
            "Show that term-by-term integration of a power series is valid inside the radius.",
        ]},
        {"name": "Ceiling", "items": [
            "Ten hard Lebl exercises, rewritten after you were stuck.",
            "One 18.100 problem set, chosen from the middle of the course.",
            "Rudin Chapter 2 exercises if you own it; otherwise the compactness section of Lebl, all of it.",
            "Blank-page proof of Bolzano–Weierstrass.",
            "A counterexample to interchanging limit and integral, written with the functions explicit.",
        ]},
    ],
    "bank": [
        "\\(\\sqrt{2}\\) as a supremum.",
        "Convergent implies Cauchy.",
        "\\(1/x\\) not uniformly continuous on \\((0,1]\\).",
        "Bolzano–Weierstrass.",
        "Intermediate value theorem.",
        "Continuous on a compact interval implies integrable.",
        "ε/3 for uniform limits.",
        "M-test on \\(\\sum x^n/n^2\\).",
        "Differentiable implies continuous.",
        "One counterexample you had to rebuild twice.",
    ],
    "oral": "State completeness, prove that continuous functions on compact intervals are uniformly continuous, and explain uniform versus pointwise convergence with an example. No notes.",
}

TOPO = {
    "slug": "topology",
    "short": "Topology",
    "title": "Topology",
    "track": "Math",
    "needs": ["proof-logic", "real-analysis"],
    "what": """
<p>Point-set topology is what remains of analysis when you delete the metric and keep the language of nearness. An open set is no longer a union of balls; it is a member of a declared collection closed under arbitrary unions and finite intersections. Continuity becomes “the preimage of an open set is open.” Compactness becomes “every open cover has a finite subcover,” which on \\(\\mathbb{R}^n\\) with the standard topology is the Heine–Borel theorem you already used without naming. Connectedness, separation axioms, and countability axioms are the other switches. The fundamental group is the first algebraic invariant: loops up to continuous deformation.</p>
<p>Munkres, Topology, 2nd edition, ISBN 978-0-13-181629-9, is the main text and it is paid. The supplementary exercises are the ceiling. MIT 18.901 from fall 2004 posts problem sets keyed to those sections; that page is your plan. Topology Without Tears is the free book if you need a gentler parallel text. π-Base is a database of spaces and counterexamples, useful after you have a definition, useless as a first reading. Learn Anything’s topology page is mostly journalism and applied-topology ads. The Quanta piece below is the one preview worth the slot. The Munkres solution repository is a check you run after your writeup, not a teacher.</p>
<p>A space is a list of open sets plus the theorems you can prove from that list. If you cannot produce a counterexample when a hypothesis is dropped, you do not know the theorem.</p>
""",
    "attack": [
        {
            "q": "<p>In \\(\\mathbb{R}\\) with the standard topology, which of \\((0,1)\\) and \\([0,1]\\) is compact? Give a cover that kills the one that fails.</p>",
            "a": "<p>\\([0,1]\\) is compact by Heine–Borel. \\((0,1)\\) is not: the cover \\(\\{(1/n, 1): n\\ge 2\\}\\) has no finite subcover, because any finite subcollection has a largest \\(n\\) and then misses points near 0.</p>",
        },
        {
            "q": "<p>Is \\(\\mathbb{Q}\\), with the subspace topology from \\(\\mathbb{R}\\), connected?</p>",
            "a": "<p>No. \\(\\mathbb{Q}\\cap(-\\infty,\\sqrt{2})\\) and \\(\\mathbb{Q}\\cap(\\sqrt{2},\\infty)\\) are nonempty, disjoint, open in \\(\\mathbb{Q}\\), and cover \\(\\mathbb{Q}\\).</p>",
        },
        {
            "q": "<p>Prove that the continuous image of a connected space is connected.</p>",
            "a": "<p>If the image split into two nonempty sets open in the image, their preimages would split the domain into two nonempty sets open in the domain. So a connected domain cannot map onto a disconnected space.</p>",
        },
    ],
    "core": [
        {
            "name": "Spaces and bases",
            "statement": "A topology on \\(X\\) is a collection of subsets containing \\(\\emptyset\\) and \\(X\\), closed under arbitrary unions and finite intersections. A basis generates a topology by taking arbitrary unions. The subspace, product, and quotient topologies are defined by the coarsest or finest topology making the relevant maps continuous, and you should be able to write each one with open sets.",
            "proof": "<p>These are definitions. The lemma you must prove: a basis satisfies the intersection condition, and the unions form a topology. Product topology: basic open sets are products of opens with all but finitely many factors equal to the whole space, in the case of arbitrary products; for two spaces it is products of opens.</p>",
        },
        {
            "name": "Continuity and separation",
            "statement": "\\(f\\) is continuous if and only if preimages of opens are open. Hausdorff: distinct points have disjoint neighborhoods. Metric spaces are Hausdorff. Compact subsets of Hausdorff spaces are closed.",
            "proof": "<p>The preimage criterion matches the metric ε–δ definition when the topology comes from a metric, because balls form a basis. Hausdorff plus compact implies closed: separate a point outside from every point inside, take a finite subcover of the inside, and intersect the corresponding outside neighborhoods.</p>",
        },
        {
            "name": "Connectedness and compactness",
            "statement": "Connected means the space is not the union of two nonempty disjoint opens. Path-connected implies connected. Compact means every open cover has a finite subcover. Continuous images preserve both. A closed subset of a compact space is compact. In \\(\\mathbb{R}^n\\), compact iff closed and bounded.",
            "proof": "<p>Preservation under continuous maps is the preimage argument from the attack. Closed subsets of compact sets: add the complement to a cover and throw it away after taking a finite subcover. Heine–Borel is the one hard theorem; prove it for \\([a,b]\\) by the least-upper-bound argument, then for boxes, then for closed bounded sets by sitting inside a box.</p>",
        },
        {
            "name": "Countability and metric spaces",
            "statement": "First countable: countable local bases. Second countable: countable basis for the whole topology. Second countable implies separable and Lindelöf. A metric space is first countable. Urysohn’s metrization theorem: a second-countable regular Hausdorff space is metrizable. You must be able to state it and know why each hypothesis is there, even if the proof is a project.",
            "proof": "<p>Metric first countability: balls of radius \\(1/n\\). Second countability implies separable by picking a point from each basis element. Counterexamples (an uncountable discrete space, the Sorgenfrey line’s square) are the content of the exercises in Munkres. Build two of them.</p>",
        },
        {
            "name": "Fundamental group",
            "statement": "Loops based at \\(x_0\\), modulo path homotopy, form a group \\(\\pi_1(X,x_0)\\). A continuous map induces a homomorphism. \\(\\pi_1(S^1)\\cong\\mathbb{Z}\\). A covering map induces an injection on fundamental groups. Simply connected means path-connected and trivial fundamental group.",
            "proof": "<p>The group operation is concatenation of paths; homotopy of paths supplies the inverse and associativity up to homotopy. The isomorphism \\(\\pi_1(S^1)\\cong\\mathbb{Z}\\) is the winding-number argument via the covering \\(\\mathbb{R}\\to S^1\\). Write that lifting argument once, slowly.</p>",
        },
    ],
    "tiers": {
        "0": [R(
            "Quanta, Topology 101",
            "https://www.quantamagazine.org/topology-101-how-mathematicians-study-holes-20210126/",
            "Read once, do not study from this. It is journalism about holes. It is also the only Learn Anything topology link that is a genuine preview rather than a paper or a tool. Then leave it.",
        )],
        "1": [R(
            "Munkres, Topology, 2nd edition, ISBN 978-0-13-181629-9, read beside Topology Without Tears",
            "https://www.topologywithouttears.net/",
            "Munkres is paid and is the main text; the ISBN is the catalogued 2nd edition. Topology Without Tears is the free parallel book when a Munkres paragraph is too compressed. Use both. Do not replace Munkres’s exercises with the free book’s.",
        )],
        "2": [R(
            "MIT 18.901, Fall 2004, assignments",
            "https://ocw.mit.edu/courses/18-901-introduction-to-topology-fall-2004/pages/assignments/",
            "The problem plan, with section and exercise numbers aimed at Munkres. Do these in order. The course page is https://ocw.mit.edu/courses/18-901-introduction-to-topology-fall-2004/ .",
        )],
        "3": [R(
            "Munkres supplementary exercises, checked only after your writeup",
            "https://github.com/9beach/munkres-topology-solutions",
            "The repository is a solution check, not a text. Open it after the 20-minute timer and a complete writeup, one exercise at a time. π-Base is the counterexample catalog when you need a space: https://topology.pi-base.org/ .",
        )],
    },
    "hardest": [
        {
            "label": "MIT 18.901 assignments",
            "url": "https://ocw.mit.edu/courses/18-901-introduction-to-topology-fall-2004/pages/assignments/",
            "why": "They name the Munkres exercises. That removes the excuse of not knowing what “hard enough” means.",
        },
        {
            "label": "Munkres, supplementary exercises at the ends of chapters",
            "url": "https://ocw.mit.edu/courses/18-901-introduction-to-topology-fall-2004/",
            "why": "These are the ceiling inside the book. They combine definitions you were allowed to keep separate.",
        },
        {
            "label": "π-Base, find a space that is connected but not path-connected",
            "url": "https://topology.pi-base.org/",
            "why": "You may look up the name only after you have tried to build the topologist’s sine curve yourself.",
        },
        {
            "label": "Prove π₁(S¹) is isomorphic to ℤ",
            "url": "https://www.topologywithouttears.net/",
            "why": "The lifting argument is the first proof in the subject that feels like a real machine. The free book will not do this at Munkres’s depth; use Munkres and this link only if you are still building the point-set foundation.",
        },
        {
            "label": "9beach, one supplementary exercise, after your own writeup",
            "url": "https://github.com/9beach/munkres-topology-solutions",
            "why": "The hardness is the writeup. The repository is the audit.",
        },
    ],
    "gate": "<p>Pass: the 18.901 assignment list, completed in order through compactness and the fundamental group, with written solutions. You must also prove, from memory, that a continuous image of a compact space is compact, and sketch why π₁(S¹) is ℤ. Fail if “open set” still means “blob” rather than “member of the topology.”</p>",
    "svg": frame(
        '<circle cx="200" cy="180" r="70" fill="none" stroke="#fff"/>'
        '<circle cx="420" cy="180" r="70" fill="none" stroke="#fff"/>'
        '<path d="M200 110 A70 70 0 0 1 200 250" fill="none" stroke="#fff" stroke-width="1.5"/>'
        '<text x="160" y="90" fill="#bbb" font-size="13" font-family="Georgia, serif">open</text>'
        '<text x="400" y="90" fill="#bbb" font-size="13" font-family="Georgia, serif">open</text>'
        '<text x="300" y="40" fill="#bbb" font-size="13" font-family="Georgia, serif">a cover with no finite subcover</text>',
        label="Two open sets in a cover",
    ),
    "caption": "Compactness is about covers, not about being closed and bounded, until you prove Heine–Borel.",
    "batches": [
        {"name": "Definitions", "items": [
            "Write the subspace topology and prove a set is open in the subspace iff it is the intersection of the subspace with an open set of the big space.",
            "Prove that a composition of continuous maps is continuous, from preimages.",
            "Show that an infinite set with the finite-complement topology is not Hausdorff.",
            "Describe the product topology on \\(\\mathbb{R}\\times\\mathbb{R}\\) and check it matches the metric topology.",
            "Give a quotient of \\([0,1]\\) that is homeomorphic to the circle. Say what you glue.",
        ]},
        {"name": "Connectedness", "items": [
            "Prove the continuous image of a connected space is connected.",
            "Show \\(\\mathbb{Q}\\) is totally disconnected in the sense that its only connected subsets are singletons. Prove at least that it is disconnected.",
            "Path-connected implies connected. Give the name of a standard counterexample to the converse and then build it.",
            "Prove that a union of connected sets with a point in common is connected.",
            "Is the punctured plane connected? Path-connected? Prove it.",
        ]},
        {"name": "Compactness", "items": [
            "The cover of \\((0,1)\\) with no finite subcover.",
            "Prove a closed subset of a compact space is compact.",
            "Prove a compact subset of a Hausdorff space is closed.",
            "Heine–Borel for \\([0,1]\\).",
            "Prove a continuous real function on a compact space attains its maximum.",
        ]},
        {"name": "Countability and metric", "items": [
            "Show a metric space is first countable.",
            "Show second countable implies separable.",
            "State Urysohn’s metrization theorem and point to a hypothesis whose failure you can illustrate.",
            "Prove that a compact metric space is complete and totally bounded, or state precisely which direction you can prove today.",
            "Use π-Base only after you have named the property you are hunting.",
        ]},
        {"name": "Fundamental group", "items": [
            "Define path homotopy and prove concatenation is well-defined on classes.",
            "Compute \\(\\pi_1\\) of a convex set in \\(\\mathbb{R}^n\\).",
            "State the induced homomorphism and prove functoriality for a composition.",
            "Sketch the proof that \\(\\pi_1(S^1)\\cong\\mathbb{Z}\\).",
            "Do the next unfinished 18.901 assignment.",
        ]},
    ],
    "bank": [
        "Cover of \\((0,1)\\) with no finite subcover.",
        "\\(\\mathbb{Q}\\) disconnected.",
        "Continuous image of a connected space.",
        "Closed subset of a compact space.",
        "Compact in a Hausdorff space is closed.",
        "Heine–Borel on \\([0,1]\\).",
        "Product topology versus the metric topology on \\(\\mathbb{R}^2\\).",
        "Metric spaces are first countable.",
        "\\(\\pi_1\\) of a convex set.",
        "Winding number sketch for the circle.",
    ],
    "oral": "Define a topology, define compactness, prove that continuous images of compact spaces are compact, and say what the fundamental group measures. Blank page.",
}

# Electives are shorter in spirit but still full pages.
def elective(slug, short, title, needs, what, attack, core, tiers, hardest, gate, svg, caption, batches, bank, oral):
    return dict(slug=slug, short=short, title=title, track="Math", needs=needs, what=what,
                attack=attack, core=core, tiers=tiers, hardest=hardest, gate=gate, svg=svg,
                caption=caption, batches=batches, bank=bank, oral=oral)
