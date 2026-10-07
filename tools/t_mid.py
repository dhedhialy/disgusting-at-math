from bits import R, frame

PROOF = {
    "slug": "proof-logic",
    "short": "Proof and logic",
    "title": "Proof and Logic",
    "track": "Math",
    "needs": ["precalc-hardening"],
    "what": """
<p>A proof is a finite piece of writing in which every sentence is either a definition, a hypothesis, or a consequence of earlier sentences by a rule you could name. Logic and set theory are the grammar of those sentences: connectives, quantifiers, membership, functions, relations. Induction is the one extra rule that talks about the natural numbers. Cardinality is the first place the grammar says something your intuition will reject, and that is why it is on this page.</p>
<p>You are not collecting logical symbols for their own sake. You are learning to block the three moves that produce fake mathematics: proving the converse instead of the statement, hiding a quantifier, and using an example as a proof of a universal claim. Enderton’s book is the ceiling for the logic itself. You do not need it to start analysis. You need Hammack’s chapters cold, including the calculus chapter, because ε–δ will otherwise feel like a new religion instead of a definition.</p>
<p>Write proofs as paragraphs. A stack of arrows with no verbs is not a proof. If you cannot read it aloud to someone who has not seen the problem, it is not finished.</p>
""",
    "attack": [
        {
            "q": "<p>Prove that there is no rational number whose square is 2. Paragraph form.</p>",
            "a": "<p>Suppose \\(p/q\\) is in lowest terms and \\((p/q)^2=2\\). Then \\(p^2=2q^2\\), so \\(p\\) is even, say \\(p=2k\\). Then \\(4k^2=2q^2\\), so \\(q^2=2k^2\\) and \\(q\\) is even. Both even contradicts lowest terms. Hence no such rational exists.</p>",
        },
        {
            "q": "<p>Prove by induction that \\(1+2+\\cdots+n=n(n+1)/2\\) for every positive integer \\(n\\).</p>",
            "a": "<p>Base \\(n=1\\): both sides equal 1. If the formula holds for \\(n=k\\), then the sum through \\(k+1\\) is \\(k(k+1)/2+(k+1)=(k+1)(k/2+1)=(k+1)(k+2)/2\\). By induction it holds for all positive integers.</p>",
        },
        {
            "q": "<p>Give an injective function \\(\\mathbb{N}\\to\\mathbb{N}\\) that is not surjective. Say what this forbids you from concluding about “size.”</p>",
            "a": "<p>\\(f(n)=n+1\\), with \\(\\mathbb{N}=\\{0,1,2,\\ldots\\}\\) or \\(\\{1,2,\\ldots\\}\\), either works. It misses 0 or 1. For infinite sets, injection does not imply surjection, so you cannot treat “into a proper subset” as a proof that a set is smaller in the finite sense. Cardinality needs a bijection, or a pair of injections and Cantor–Bernstein.</p>",
        },
    ],
    "core": [
        {
            "name": "Quantifiers",
            "statement": "A statement \\(\\forall x\\in S,\\, P(x)\\) is false exactly when one counterexample exists. A statement \\(\\exists x\\in S,\\, P(x)\\) is proved by exhibiting one element and checking \\(P\\). Negation swaps the quantifiers and negates the predicate.",
            "proof": "<p>This is the meaning of the symbols, not a theorem. The skill is mechanical: the negation of \\(\\forall\\varepsilon>0\\,\\exists\\delta>0\\,\\ldots\\) is \\(\\exists\\varepsilon>0\\,\\forall\\delta>0\\,\\ldots\\) with the inner inequality flipped. Write three examples until it is boring.</p>",
        },
        {
            "name": "Sets, functions, relations",
            "statement": "\\(A\\subseteq B\\) means every element of \\(A\\) is in \\(B\\). \\(A=B\\) means both inclusions. A relation is a set of ordered pairs. It is an equivalence relation when it is reflexive, symmetric, and transitive, and then the equivalence classes partition the set. A function is injective, surjective, or bijective in the usual senses.",
            "proof": "<p>To prove inclusion, take an arbitrary element and chase membership. To prove two sets equal, write both inclusions. The partition claim: reflexivity puts each element in its own class; symmetry and transitivity make overlap of classes imply equality.</p>",
        },
        {
            "name": "Proof patterns",
            "statement": "Direct proof assumes the hypothesis and reaches the conclusion. Contrapositive proves \\(\\neg Q\\Rightarrow\\neg P\\) instead of \\(P\\Rightarrow Q\\). Contradiction assumes the negation of the claim and derives a false sentence. Existence may be constructive or not. Uniqueness is a separate sentence: any two objects satisfying the property are equal.",
            "proof": "<p>The contrapositive is equivalent to the implication because both fail only in the case \\(P\\) true and \\(Q\\) false. Contradiction is the observation that if \\(\\neg C\\) implies a falsehood, then \\(\\neg C\\) is false. These are schemas. A proof still has to contain the content of the problem.</p>",
        },
        {
            "name": "Induction",
            "statement": "If \\(P(1)\\) holds and \\(P(k)\\) implies \\(P(k+1)\\) for every \\(k\\ge 1\\), then \\(P(n)\\) holds for every positive integer \\(n\\). Strong induction allows the inductive step to use all earlier cases. The well-ordering principle (every nonempty subset of the positive integers has a least element) is equivalent.",
            "proof": "<p>If some positive integer failed, the set of failures would have a least element \\(m\\). Then \\(m\\ne 1\\), and \\(m-1\\) would satisfy \\(P\\), hence so would \\(m\\), a contradiction. That argument uses well-ordering. Going the other way is the usual least-element proof written as induction.</p>",
        },
        {
            "name": "Cardinality",
            "statement": "Two sets have the same cardinality when a bijection exists between them. \\(\\mathbb{N}\\), \\(\\mathbb{Z}\\), and \\(\\mathbb{Q}\\) are countable. \\(\\mathbb{R}\\) is not: Cantor’s diagonal argument. If there are injections both ways between two sets, there is a bijection (Cantor–Bernstein).",
            "proof": "<p>Countability of \\(\\mathbb{Q}\\) is the zigzag through fractions in lowest terms. Diagonalization: any list of real numbers in \\((0,1)\\) misses the number whose \\(n\\)th digit differs from the \\(n\\)th digit of the \\(n\\)th listed number. Cantor–Bernstein can be quoted once you have used it; the proof is a chain argument you should read in Hammack and then rewrite.</p>",
        },
    ],
    "tiers": {
        "0": [R(
            "Hammack, Book of Proof, the landing page",
            "https://richardhammack.github.io/BookOfProof/",
            "Read once, do not study from this. Read the description and the table of contents so you see that counting, induction, relations, and a chapter of ε–δ are all in one book. Then close the page and open the PDF.",
        )],
        "1": [R(
            "Richard Hammack, Book of Proof, 3rd edition, revision 3.4 (5 February 2025), ISBN 978-0-9894721-2-8",
            "https://richardhammack.github.io/BookOfProof/Main.pdf",
            "Free legal PDF, Creative Commons, AIM open textbook. This replaces Velleman as the working text because you can start tonight. Velleman, How to Prove It,  ISBN 978-1-108-43953-4, is the paid book to buy if you want a second, slightly stricter pass. The ISBN was confirmed against the Open Library catalog; a stable publisher page was not.",
        )],
        "2": [R(
            "Hammack, every exercise in Chapters 1–14, written",
            "https://richardhammack.github.io/BookOfProof/Main.pdf",
            "The book is the problem set. Do not use the solution section until a writeup exists. Munkres’s Chapter 1 exercises are the harder set-theory drill once Hammack feels short; the book is paid, ISBN 978-0-13-181629-9 for the 2nd edition catalog entry, and the topology page sends you there properly.",
        )],
        "3": [R(
            "Kedlaya, The Putnam Archive",
            "https://kskedlaya.org/putnam-archive/",
            "The public ceiling for timed proof-writing. Enderton, A Mathematical Introduction to Logic, ISBN 978-0-12-238452-3, is the paid logic ceiling; no free copy was verified, so it is named and not linked.",
        )],
    },
    "hardest": [
        {
            "label": "Hammack, Chapter 13, the ε–δ and sequence exercises",
            "url": "https://richardhammack.github.io/BookOfProof/Main.pdf",
            "why": "This is the first time a proof has an alternating quantifier you cannot bluff.",
        },
        {
            "label": "Hammack, Chapter 14, Cantor–Bernstein and uncountability",
            "url": "https://richardhammack.github.io/BookOfProof/Main.pdf",
            "why": "You will want to say “obviously bigger.” The exercises refuse that sentence.",
        },
        {
            "label": "Putnam 1987 problems",
            "url": "https://kskedlaya.org/putnam-archive/1987.pdf",
            "why": "Several early problems are pure reasoning. Treat A1 and B1 as proof exams, not as calculus.",
        },
        {
            "label": "Putnam 2008 problems",
            "url": "https://kskedlaya.org/putnam-archive/2008.pdf",
            "why": "A modern paper. The A1/B1 layer is the right ceiling before you have had analysis.",
        },
        {
            "label": "Kedlaya’s Putnam archive, the whole index",
            "url": "https://kskedlaya.org/putnam-archive/",
            "why": "When you need another paper, take it from here. Solutions on that site are for after your writeup.",
        },
    ],
    "gate": "<p>Pass: twenty proofs from Hammack, at least two from each of direct proof, contrapositive, contradiction, induction, relations, and cardinality, written in paragraphs and read aloud. Plus the irrationality of \\(\\sqrt{2}\\) and one diagonal argument, from memory, on a blank page. Fail if any proof uses an example as a universal claim.</p>",
    "svg": frame(
        '<ellipse cx="250" cy="180" rx="120" ry="80" fill="none" stroke="#fff"/>'
        '<ellipse cx="390" cy="180" rx="120" ry="80" fill="none" stroke="#fff"/>'
        '<text x="175" y="175" fill="#fff" font-size="16" font-family="Georgia, serif">A</text>'
        '<text x="430" y="175" fill="#fff" font-size="16" font-family="Georgia, serif">B</text>'
        '<text x="300" y="175" fill="#bbb" font-size="14" font-family="Georgia, serif">A∩B</text>',
        label="Two sets and their intersection",
    ),
    "caption": "To prove equality of sets, prove both inclusions. The picture is not the proof.",
    "batches": [
        {"name": "Grammar", "items": [
            "Negate: for every \\(\\varepsilon>0\\) there exists \\(\\delta>0\\) such that if \\(0<|x-a|<\\delta\\) then \\(|f(x)-L|<\\varepsilon\\).",
            "Negate: there exists a real \\(M\\) such that for every positive integer \\(n\\), \\(|a_n|\\le M\\).",
            "Which of “if \\(n^2\\) is even then \\(n\\) is even” and its converse is true? Prove the true one.",
            "Disprove: every positive integer is a sum of three squares. One counterexample, named as a counterexample.",
            "Translate “the set of even integers is closed under addition” into symbols, then prove it.",
        ]},
        {"name": "Sets and functions", "items": [
            "Prove \\(A\\cap(B\\cup C)=(A\\cap B)\\cup(A\\cap C)\\) by two inclusions.",
            "Prove that a composition of injections is injective.",
            "Find a surjection \\(\\mathbb{N}\\to\\mathbb{Z}\\) and write the rule.",
            "Show that congruence modulo \\(n\\) is an equivalence relation. Describe the classes.",
            "Prove that if \\(f:A\\to B\\) is bijective then \\(f^{-1}\\) is a function.",
        ]},
        {"name": "Induction", "items": [
            "Prove \\(1+2+\\cdots+n=n(n+1)/2\\).",
            "Prove \\(2^n>n\\) for every positive integer \\(n\\).",
            "Prove that \\(3\\) divides \\(n^3-n\\).",
            "Prove the formula for the sum of a geometric series by induction.",
            "Use strong induction to prove that every integer \\(n\\ge 2\\) has a prime factor.",
        ]},
        {"name": "Cardinality and structure", "items": [
            "Prove \\(\\sqrt{2}\\) is irrational.",
            "Prove \\(\\mathbb{Z}\\) is countable by writing an explicit bijection with \\(\\mathbb{N}\\).",
            "Write Cantor’s diagonal argument for \\((0,1)\\).",
            "Show that a countable union of finite sets need not be finite, and that a countable union of countable sets is countable if you allow a choice of listings.",
            "Prove uniqueness of the additive identity in a set equipped with an associative operation, from the axioms, in five lines.",
        ]},
        {"name": "Ceiling", "items": [
            "All of Hammack Chapter 13, written, before any solution is opened.",
            "All of Hammack Chapter 14.",
            "Putnam 1987 A1 and B1, full writeups, then the rest of the paper as far as you can.",
            "Putnam 2008 A1 and B1.",
            "One proof from this page, chosen at random by a friend, delivered orally.",
        ]},
    ],
    "bank": [
        "Irrationality of \\(\\sqrt{2}\\).",
        "Sum \\(1+\\cdots+n\\) by induction.",
        "Injection \\(\\mathbb{N}\\to\\mathbb{N}\\) that misses a point.",
        "Negation of the ε–δ definition.",
        "Distributive law for sets, both inclusions.",
        "Composition of injections.",
        "Congruence modulo \\(n\\).",
        "Every \\(n\\ge 2\\) has a prime factor.",
        "Diagonal argument.",
        "Putnam 1987 A1.",
    ],
    "oral": "Define injection and surjection, prove the sum formula by induction, and explain why a single example cannot prove a universal statement. Blank page.",
}

CALC = {
    "slug": "calc-1",
    "short": "Calculus",
    "title": "Single-Variable Calculus",
    "track": "Math",
    "needs": ["proof-logic"],
    "what": """
<p>Single-variable calculus is the study of limits, and of the two constructions that limits make rigorous: instantaneous rate of change, and accumulated change. The derivative is a limit of difference quotients. The integral is a limit of sums. The fundamental theorem says these are inverse operations when the hypotheses hold. Everything else in a first course is a consequence or a technique: mean value theorem, L’Hôpital, sequences, series, Taylor polynomials with a remainder you can estimate.</p>
<p>Stewart is the book most colleges assign. It is paid, and I am not pinning an edition because I could not verify one cleanly. You do not need it. APEX Calculus is free, complete, and enough for computational control; MIT 18.01 supplies the problem sets and the exams with solutions. Spivak is the ceiling, not the first book: its exercises are where a correct computation stops being the standard and a proof becomes the standard. Demidovich is the computational grind, thousands of problems, and it is on the Internet Archive legally as a library scan.</p>
<p>Learn Anything’s calculus page exists and is a junk drawer. The two links from it worth keeping are Thompson’s Calculus Made Easy, which is a preview and not a course, and Keisler’s infinitesimal calculus, which is a legitimate alternate foundation. They are not better than 18.01 plus a problem book if your goal is to be able to sit an exam.</p>
""",
    "attack": [
        {
            "q": "<p>Using only \\(f'(a)=\\lim_{h\\to 0}(f(a+h)-f(a))/h\\), prove that the derivative of \\(x^3\\) is \\(3x^2\\).</p>",
            "a": "<p>\\(((x+h)^3-x^3)/h=(3x^2 h+3xh^2+h^3)/h=3x^2+3xh+h^2\\), which tends to \\(3x^2\\) as \\(h\\to 0\\).</p>",
        },
        {
            "q": "<p>A particle has position \\(s(t)=t^3-6t^2+9t\\) for \\(t\\ge 0\\). On which interval is it moving in the negative direction?</p>",
            "a": "<p>\\(s'(t)=3t^2-12t+9=3(t-1)(t-3)\\). The velocity is negative when the quadratic is negative, which is between the roots: \\(t\\in(1,3)\\).</p>",
        },
        {
            "q": "<p>From the definition, why is the derivative of a constant function equal to 0?</p>",
            "a": "<p>If \\(f(x)=c\\), the difference quotient is \\((c-c)/h=0\\) for every \\(h\\ne 0\\), so the limit is 0.</p>",
        },
    ],
    "core": [
        {
            "name": "Limit and continuity",
            "statement": "\\(\\lim_{x\\to a}f(x)=L\\) means: for every \\(\\varepsilon>0\\) there exists \\(\\delta>0\\) such that \\(0<|x-a|<\\delta\\) implies \\(|f(x)-L|<\\varepsilon\\). \\(f\\) is continuous at \\(a\\) when the limit equals \\(f(a)\\).",
            "proof": "<p>This is a definition. The work is using it. Sum and product rules for limits follow by algebraic estimates and the triangle inequality; write the product rule once, in ε–δ, before you trust it.</p>",
        },
        {
            "name": "Derivative",
            "statement": "\\(f'(a)\\) is the limit of \\((f(a+h)-f(a))/h\\) when it exists. Product, quotient, and chain rules hold when the pieces are differentiable. If \\(f\\) has a local extremum at an interior point and \\(f'\\) exists there, then \\(f'=0\\).",
            "proof": "<p>The product rule is the usual add-and-subtract of \\(f(a+h)g(a)\\). Fermat’s interior extremum theorem: the difference quotient cannot approach a positive number and a negative number at once, because the function lies on one side of its value.</p>",
        },
        {
            "name": "Mean value theorem",
            "statement": "If \\(f\\) is continuous on \\([a,b]\\) and differentiable on \\((a,b)\\), then some \\(c\\) in \\((a,b)\\) has \\(f'(c)=(f(b)-f(a))/(b-a)\\). Consequence: if \\(f'=0\\) everywhere on an interval then \\(f\\) is constant.",
            "proof": "<p>Reduce to Rolle by subtracting the chord. Rolle: a continuous function on a compact interval attains its max and min; if it is not constant an interior extremum exists, and there the derivative vanishes. The constant-function corollary is immediate.</p>",
        },
        {
            "name": "Fundamental theorem",
            "statement": "If \\(f\\) is continuous on \\([a,b]\\) and \\(F(x)=\\int_a^x f\\), then \\(F'=f\\). If \\(G'=f\\), then \\(\\int_a^b f=G(b)-G(a)\\).",
            "proof": "<p>The difference quotient of \\(F\\) is the average of \\(f\\) over a short interval, which approaches \\(f(x)\\) by continuity. The second form is the mean value theorem applied to \\(F-G\\), whose derivative is zero.</p>",
        },
        {
            "name": "Sequences and series",
            "statement": "A series \\(\\sum a_n\\) converges when its partial sums converge. Absolute convergence implies convergence. The ratio test, the comparison test, and the alternating series test are the working tests. A power series has a radius of convergence. Taylor’s theorem supplies a remainder, Lagrange form \\(f^{(n+1)}(c)(x-a)^{n+1}/(n+1)!\\) under the usual hypotheses.",
            "proof": "<p>Absolute convergence uses comparison with the series of absolute values and completeness of \\(\\mathbb{R}\\), which you may treat carefully now or again in analysis. The ratio test compares with a geometric series. Taylor with Lagrange remainder is repeated integration by parts or repeated application of the mean value theorem; write one of those once.</p>",
        },
    ],
    "tiers": {
        "0": [R(
            "3Blue1Brown, Essence of Calculus",
            "https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr",
            "Watch once, do not study from this. It shows what a derivative is buying you. It does not make you able to compute one under pressure.",
        )],
        "1": [R(
            "APEX Calculus, together with MIT 18.01SC",
            "https://www.apexcalculus.com/",
            "APEX is free and complete; the download page is https://www.apexcalculus.com/downloads . MIT 18.01SC is the lecture, problem set, and exam spine: https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/ . Stewart is the usual paid textbook; no edition is pinned here. APEX plus 18.01 is the better working pair because the exams are public.",
        )],
        "2": [R(
            "Demidovich, Problems in Mathematical Analysis (Mir, 1970)",
            "https://archive.org/details/DemidovichEtAlProblemsInMathematicalAnalysisMir1970",
            "About three thousand problems, ordered by technique. Apostol, Calculus, Volume 1, ISBN 978-0-471-00005-1, is the paid proof-flavored alternate. Do Demidovich for speed and Apostol when you want the theorem proved before the drill.",
            paid=False,
        )],
        "3": [R(
            "Spivak, Calculus, ISBN 978-0-914098-91-1, and Putnam analysis problems",
            "https://kskedlaya.org/putnam-archive/2024.pdf",
            "Spivak is paid; the ISBN is the catalogued one for his Calculus. Its end-of-chapter problems are the English-language ceiling for a first course. The 2024 Putnam paper is one concrete ceiling exam; pick the problems that are limits, inequalities, or series. Keisler’s free infinitesimal book is a side door, not this ceiling: https://people.math.wisc.edu/~hkeisler/calc.html",
        )],
    },
    "hardest": [
        {
            "label": "MIT 18.01SC exams",
            "url": "https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/",
            "why": "Timed, graded, and solved. You find out whether you can start, not whether you can recognize a worked example.",
        },
        {
            "label": "Demidovich, the later problems in the chapters on limits, series, and integrals",
            "url": "https://archive.org/details/DemidovichEtAlProblemsInMathematicalAnalysisMir1970",
            "why": "The early items are drill. The late items in each section are where a standard method needs an estimate.",
        },
        {
            "label": "Spivak, the chapters on limits, the fundamental theorem, and infinite series",
            "url": "https://www.apexcalculus.com/",
            "why": "Spivak has no verified free copy, so this link is the free book you already own and the instruction is: buy or borrow Spivak and do those chapters’ problems. They are hard because they ask for proofs of facts the other books use.",
        },
        {
            "label": "Putnam 2024",
            "url": "https://kskedlaya.org/putnam-archive/2024.pdf",
            "why": "A full modern paper. Mine it for analytic problems. Most of the paper is not calculus, and that is information.",
        },
        {
            "label": "Putnam 1987",
            "url": "https://kskedlaya.org/putnam-archive/1987.pdf",
            "why": "Older papers hide less machinery. If you cannot start A1, the issue is writing, not content.",
        },
    ],
    "gate": "<p>Pass: one full MIT 18.01 exam, closed book, in the allotted time, score at the level of the published solutions on every problem you claim, plus five Spivak problems from three different chapters, written as proofs. Fail if the Taylor remainder is a formula you cannot derive.</p>",
    "svg": frame(
        '<path d="M60 260 Q 200 240, 300 160 T 580 80" fill="none" stroke="#fff" stroke-width="1.5"/>'
        '<line x1="180" y1="250" x2="420" y2="110" stroke="rgba(255,255,255,0.75)"/>'
        '<line x1="300" y1="160" x2="460" y2="70" stroke="#fff"/>'
        '<circle cx="300" cy="160" r="4" fill="#fff"/>'
        '<text x="470" y="68" fill="#bbb" font-size="13" font-family="Georgia, serif">tangent</text>'
        '<text x="400" y="140" fill="#bbb" font-size="13" font-family="Georgia, serif">secant</text>',
        label="A secant approaching a tangent",
    ),
    "caption": "The derivative is the limit of those secant slopes, when the limit exists.",
    "batches": [
        {"name": "Limits", "items": [
            "Compute \\(\\lim_{x\\to 0}(\\sqrt{1+x}-1)/x\\) by algebra.",
            "Prove that \\(\\lim_{x\\to 0}x\\sin(1/x)=0\\) with the squeeze theorem.",
            "Give an example where the left- and right-hand limits exist and differ.",
            "From the ε–δ definition, prove \\(\\lim_{x\\to 2}(3x+1)=7\\).",
            "Show that \\(\\lim_{x\\to 0}\\sin x/x=1\\) is the fact you are using whenever you differentiate sine. If you cannot prove it yet, write precisely which inequality you are missing.",
        ]},
        {"name": "Derivatives", "items": [
            "Differentiate \\(x^3\\), \\(\\sin x\\), and \\(e^x\\) from the definition or from a named theorem you have proved.",
            "State and prove the product rule.",
            "Find and classify critical points of \\(x^3-6x^2+9x\\).",
            "A rectangle of perimeter 20 has maximum area when it is a square. Prove it.",
            "State L’Hôpital’s rule with hypotheses. Give a limit where the hypotheses fail and the rule would give nonsense.",
        ]},
        {"name": "Integrals", "items": [
            "Compute \\(\\int_0^1 x^2\\,dx\\) from the definition with a regular partition, then again by the fundamental theorem.",
            "Prove the second form of the fundamental theorem from the first, as sketched in the core list.",
            "Integrate by parts: \\(\\int x e^x\\,dx\\).",
            "Compute the area between \\(y=x\\) and \\(y=x^2\\) on \\([0,1]\\).",
            "Improper integral \\(\\int_1^\\infty x^{-2}\\,dx\\). Say why \\(\\int_1^\\infty x^{-1}\\,dx\\) diverges.",
        ]},
        {"name": "Series", "items": [
            "Does \\(\\sum 1/n^2\\) converge? Which test, and why does the same test not apply to the harmonic series?",
            "Radius of convergence of \\(\\sum x^n/n\\) and of \\(\\sum n! x^n\\).",
            "Write the degree-3 Taylor polynomial of \\(e^x\\) at 0 and the Lagrange remainder bound on \\([-1,1]\\).",
            "Alternating harmonic series: converge? absolutely?",
            "Give a series that converges but not absolutely.",
        ]},
        {"name": "Ceiling", "items": [
            "One 18.01 exam, timed.",
            "Twenty Demidovich problems from three chapters, the later numbers.",
            "Five Spivak problems, written as proofs.",
            "Three Putnam problems of an analytic kind, from Kedlaya’s archive.",
            "Derive the mean value theorem from Rolle’s theorem without notes.",
        ]},
    ],
    "bank": [
        "Derivative of \\(x^3\\) from the definition.",
        "Where \\(s(t)=t^3-6t^2+9t\\) has negative velocity.",
        "ε–δ proof that \\(3x+1\\to 7\\) as \\(x\\to 2\\).",
        "Product rule.",
        "Mean value theorem from Rolle.",
        "Fundamental theorem, both forms.",
        "\\(\\int_1^\\infty x^{-1}\\,dx\\) diverges.",
        "Radius of \\(\\sum x^n/n\\).",
        "Taylor remainder for \\(e^x\\) on \\([-1,1]\\).",
        "One 18.01 exam problem you got wrong the first time.",
    ],
    "oral": "Define the derivative, prove the product rule, state the fundamental theorem, and explain what a radius of convergence means. No notes.",
}
