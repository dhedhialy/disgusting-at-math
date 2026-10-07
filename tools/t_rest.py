from bits import R, frame

ABS = {
    "slug": "abstract-algebra",
    "short": "Abstract algebra",
    "title": "Abstract Algebra",
    "track": "Math",
    "needs": ["proof-logic", "linear-algebra"],
    "what": """
<p>Abstract algebra studies sets with operations that obey a short list of axioms, and the maps that preserve those operations. Groups capture symmetry. Rings capture arithmetic. Fields capture the setting in which linear algebra was happening all along. The payoff in a first serious course is the isomorphism theorems, the classification of finitely generated abelian groups, the Sylow theorems, and, if you go the distance, the Galois correspondence between field extensions and groups of automorphisms.</p>
<p>You already know linear maps are homomorphisms of additive groups that also respect scalar multiplication. This page removes the scalars and asks what is left. The work is examples: symmetric groups, cyclic groups, matrix groups, polynomial rings, and finite fields. A definition you cannot illustrate with two nonisomorphic examples is a definition you will misquote.</p>
<p>Judson’s Abstract Algebra: Theory and Applications is free, updated, and has enough exercises to be the whole course. Dummit and Foote is the paid encyclopedia; no edition was verified, so it is not given an ISBN here. Use it as a reference after Judson, not as a place to hide from exercises.</p>
""",
    "attack": [
        {"q": "<p>Is the set of nonzero reals under multiplication a group? What is the identity, and what is the inverse of \\(-2\\)?</p>",
         "a": "<p>Yes. The identity is \\(1\\). The inverse of \\(-2\\) is \\(-1/2\\), because their product is 1. Closure, associativity, identity, and inverses all hold. Zero is excluded because it has no multiplicative inverse.</p>"},
        {"q": "<p>List the elements of \\(S_3\\) and find a subgroup of order 2 and a subgroup of order 3.</p>",
         "a": "<p>\\(S_3\\) has six permutations of \\(\\{1,2,3\\}\\). A subgroup of order 2 is \\(\\{e,(12)\\}\\). A subgroup of order 3 is the alternating group \\(A_3=\\{e,(123),(132)\\}\\), which is cyclic.</p>"},
        {"q": "<p>Prove that the identity element of a group is unique.</p>",
         "a": "<p>If \\(e\\) and \\(f\\) are both identities, then \\(e=ef=f\\).</p>"},
    ],
    "core": [
        {"name": "Groups", "statement": "A group is a set with an associative binary operation, an identity, and inverses. A subgroup is a subset that is a group under the same operation. The order of an element is the size of the cyclic subgroup it generates. Lagrange: the order of a subgroup divides the order of a finite group.",
         "proof": "<p>Lagrange is a counting argument: the left cosets of a subgroup partition the group and all have the same size, namely the order of the subgroup.</p>"},
        {"name": "Homomorphisms", "statement": "A homomorphism preserves the operation. Its kernel is a normal subgroup, and its image is a subgroup. The first isomorphism theorem: \\(G/\\ker\\varphi\\cong\\operatorname{im}\\varphi\\).",
         "proof": "<p>The kernel is the preimage of the identity. Cosets of the kernel are the fibers of the homomorphism. The induced map on cosets is a bijection onto the image and preserves the operation.</p>"},
        {"name": "Quotients and Sylow", "statement": "If \\(N\\) is normal in \\(G\\), the set of cosets \\(G/N\\) is a group. A finite group of order \\(p^k m\\) with \\(p\\) not dividing \\(m\\) has a subgroup of order \\(p^k\\), and the number of them is congruent to 1 mod \\(p\\) and divides \\(m\\).",
         "proof": "<p>The quotient operation is well-defined exactly because \\(N\\) is normal: \\(aN\\cdot bN=abN\\) does not depend on representatives. The Sylow theorems are proved by letting the group act on the set of subsets of size \\(p^k\\), or on its Sylow subgroups by conjugation. Write the congruence \\(n_p\\equiv 1\\pmod p\\) from the class equation after you have seen one proof; do not memorize it as a spell.</p>"},
        {"name": "Rings and fields", "statement": "A commutative ring with identity has an ideal theory. Quotients by ideals are rings. A field is a commutative ring in which every nonzero element is invertible. \\(F[x]\\) over a field is a Euclidean domain, hence a principal ideal domain, hence a unique factorization domain.",
         "proof": "<p>The division algorithm in \\(F[x]\\) is polynomial long division. Principal ideals follow by taking a polynomial of least degree in a nonzero ideal. Unique factorization follows from the usual Euclidean-domain argument.</p>"},
        {"name": "Galois, stated", "statement": "A finite Galois extension \\(K/F\\) has automorphism group \\(G\\) with \\(|G|=[K:F]\\), and intermediate fields correspond bijectively to subgroups of \\(G\\), order-reversing. The splitting field of a separable polynomial is Galois.",
         "proof": "<p>This is the fundamental theorem of Galois theory. A first course often reaches it at the end. You should be able to compute the Galois group of \\(x^2-2\\) over \\(\\mathbb{Q}\\) and of a cyclotomic extension of small degree before you claim the correspondence. The proof uses the theorem of the primitive element and linear independence of characters.</p>"},
    ],
    "tiers": {
        "0": [R("Judson, the book’s front page", "https://judsonbooks.org/abstract-algebra-theory-and-applications/",
                "Read once, do not study from this. See that the book runs from groups through Galois theory and that a free PDF exists. Then download the PDF and work there.")],
        "1": [R("Judson, Abstract Algebra: Theory and Applications, 2025/2026 edition PDF",
                "https://judsonbooks.org/aata-files/aata-20260811.pdf",
                "Free. The HTML edition is https://judsonbooks.org/aata-files/aata-html/aata.html . Paperback ISBN 978-1-944325-21-3 is the 2026 print edition named on the author’s page. This is the main text because it is complete, exercised, and legal.")],
        "2": [R("Judson’s harder exercises, all of them, plus the Sage checks he includes",
                "https://judsonbooks.org/aata-files/aata-html/aata.html",
                "The exercises are the problem set. Dummit and Foote is the paid source of extra problems; no edition was verified.")],
        "3": [R("Putnam problems on groups, rings, and polynomials",
                "https://kskedlaya.org/putnam-archive/",
                "Borisov’s sorted list points at the algebra problems: https://people.math.binghamton.edu/borisov/Putnam/SelectedProblemList.pdf . Qualifying exams in algebra are the real ceiling; a public one you can start now is a Putnam algebra problem you cannot start in five minutes.")],
    },
    "hardest": [
        {"label": "Judson, the Sylow exercises", "url": "https://judsonbooks.org/aata-files/aata-20260811.pdf",
         "why": "Counting subgroups is where Lagrange stops being enough."},
        {"label": "Judson, Galois correspondence computations", "url": "https://judsonbooks.org/aata-files/aata-html/aata.html",
         "why": "A small extension you compute by hand teaches more than a paragraph about solvability."},
        {"label": "Borisov, algebra section", "url": "https://people.math.binghamton.edu/borisov/Putnam/SelectedProblemList.pdf",
         "why": "Putnam algebra problems are short and do not announce which theorem they want."},
        {"label": "Putnam 2008", "url": "https://kskedlaya.org/putnam-archive/2008.pdf",
         "why": "Use it as a timed paper after the Sylow chapter."},
        {"label": "Classify groups of order pq for distinct primes, with hypotheses written", "url": "https://judsonbooks.org/aata-files/aata-20260811.pdf",
         "why": "The proof is a Sylow counting argument. If you only remember the conclusion, you do not have it."},
    ],
    "gate": "<p>Pass: written proofs of Lagrange, the first isomorphism theorem, and one Sylow counting argument for a specific order, plus a complete computation of the Galois group of \\(x^3-2\\) over \\(\\mathbb{Q}\\) or a written admission of exactly which lemma you are missing. Fail if “normal” means “invariant” without a sentence about conjugates or kernels.</p>",
    "svg": frame(
        '<rect x="70" y="140" width="140" height="70" fill="none" stroke="#fff"/>'
        '<rect x="400" y="140" width="140" height="70" fill="none" stroke="#fff"/>'
        '<line x1="210" y1="175" x2="400" y2="175" stroke="#fff" marker-end=""/>'
        '<polygon points="390,168 400,175 390,182" fill="#fff"/>'
        '<text x="90" y="180" fill="#fff" font-size="16" font-family="Georgia, serif">G</text>'
        '<text x="430" y="180" fill="#fff" font-size="16" font-family="Georgia, serif">G/N</text>'
        '<text x="270" y="160" fill="#bbb" font-size="14" font-family="Georgia, serif">quotient</text>',
        label="A group mapping onto a quotient"),
    "caption": "The first isomorphism theorem says every homomorphism is a quotient onto its image.",
    "batches": [
        {"name": "Groups", "items": [
            "Prove the identity is unique and inverses are unique.",
            "Prove that \\(S_3\\) is nonabelian.",
            "List subgroups of \\(\\mathbb{Z}/6\\mathbb{Z}\\).",
            "Prove Lagrange for a subgroup of a finite group.",
            "Show \\(A_3\\) is cyclic.",
        ]},
        {"name": "Homomorphisms", "items": [
            "Kernel of the sign homomorphism \\(S_n\\to\\{\\pm 1\\}\\).",
            "Prove the first isomorphism theorem.",
            "Show that a cyclic group of order \\(n\\) is isomorphic to \\(\\mathbb{Z}/n\\mathbb{Z}\\).",
            "Prove the center of a group is a normal subgroup.",
            "Give two groups of order 4 that are not isomorphic.",
        ]},
        {"name": "Sylow and quotients", "items": [
            "How many elements of order 2 are in \\(S_3\\)?",
            "Prove there is a normal subgroup of order 7 in a group of order 14, or decide it carefully with Sylow.",
            "State all three Sylow theorems.",
            "Show \\(\\mathbb{Z}\\) is not isomorphic to \\(\\mathbb{Q}\\) as groups under addition.",
            "Compute the conjugacy classes of \\(S_3\\).",
        ]},
        {"name": "Rings", "items": [
            "Prove \\(F[x]\\) is a Euclidean domain when \\(F\\) is a field.",
            "Factor \\(x^2+1\\) over \\(\\mathbb{R}\\) and over \\(\\mathbb{C}\\).",
            "Show \\(\\mathbb{Z}/n\\mathbb{Z}\\) is a field iff \\(n\\) is prime.",
            "Ideals of \\(\\mathbb{Z}\\).",
            "A ring homomorphism from a field is injective or zero. Prove it.",
        ]},
        {"name": "Ceiling", "items": [
            "Galois group of \\(x^2-2\\) over \\(\\mathbb{Q}\\).",
            "As far as you can get on \\(x^3-2\\).",
            "Five Borisov algebra problems.",
            "One Putnam paper’s algebra problems, timed for the ones you attempt.",
            "Oral proof of the first isomorphism theorem.",
        ]},
    ],
    "bank": [
        "Identity in a group is unique.",
        "Subgroups of \\(S_3\\).",
        "Lagrange.",
        "First isomorphism theorem.",
        "Two groups of order 4.",
        "\\(\\mathbb{Z}/n\\mathbb{Z}\\) is a field iff \\(n\\) is prime.",
        "\\(F[x]\\) is a Euclidean domain.",
        "Sylow statement for \\(n_p\\).",
        "Galois group of \\(x^2-2\\).",
        "Center is normal.",
    ],
    "oral": "Define a group, prove Lagrange, and state the first isomorphism theorem with the kernel in the sentence. No notes.",
}

CX = {
    "slug": "complex-analysis",
    "short": "Complex analysis",
    "title": "Complex Analysis",
    "track": "Math",
    "needs": ["calc-3", "real-analysis"],
    "what": """
<p>Complex analysis is calculus for functions \\(\\mathbb{C}\\to\\mathbb{C}\\) that are complex-differentiable on an open set. That single hypothesis is absurdly strong. It implies the function is analytic, that its integral over a triangle vanishes, that Cauchy's integral formula recovers the function from its values on a circle, and that a bounded entire function is constant. Residues then turn real integrals into contour bookkeeping. You are not learning a new computational trick. You are learning why holomorphicity is a rigidity condition.</p>
<p>MIT 18.04 is a full course with notes and problem sets, and it is the working text because a standard book such as Ahlfors or Conway is paid and no free legal scan was verified. Stein and Shakarchi, and Needham’s Visual Complex Analysis, are paid and unnamed by ISBN here for the same reason. Use 18.04’s problem sets as the book. The proofs you must own are Cauchy's theorem for a disk, the integral formula, and the residue theorem at the level of a simple pole.</p>
<p>A formal power series you cannot connect to an integral is not yet complex analysis.</p>
""",
    "attack": [
        {"q": "<p>Write the Cauchy–Riemann equations for \\(f=u+iv\\), and check them for \\(f(z)=z^2\\).</p>",
         "a": "<p>\\(u_x=v_y\\) and \\(u_y=-v_x\\). For \\(z^2=(x+iy)^2=x^2-y^2+2ixy\\), one has \\(u_x=2x=v_y\\) and \\(u_y=-2y=-v_x\\).</p>"},
        {"q": "<p>Compute \\(\\int_{|z|=1} dz/z\\), counterclockwise.</p>",
         "a": "<p>Parametrize \\(z=e^{i\\theta}\\), \\(dz=ie^{i\\theta}d\\theta\\), \\(\\theta\\) from 0 to \\(2\\pi\\). The integral is \\(\\int_0^{2\\pi} i\\,d\\theta=2\\pi i\\).</p>"},
        {"q": "<p>Why does Cauchy–Riemann for \\(f(z)=\\bar z\\) fail?</p>",
         "a": "<p>\\(u=x\\), \\(v=-y\\). Then \\(u_x=1\\) and \\(v_y=-1\\), so \\(u_x\\ne v_y\\). Conjugation is not holomorphic anywhere.</p>"},
    ],
    "core": [
        {"name": "Holomorphic", "statement": "\\(f\\) is holomorphic at \\(z_0\\) when \\(\\lim_{h\\to 0}(f(z_0+h)-f(z_0))/h\\) exists in \\(\\mathbb{C}\\). On an open set this is equivalent, given continuous partials, to the Cauchy–Riemann equations.",
         "proof": "<p>Approach along real and imaginary directions to get Cauchy–Riemann. The converse, with continuous partials, writes the real differential and matches it to multiplication by a complex number.</p>"},
        {"name": "Cauchy", "statement": "If \\(f\\) is holomorphic inside and on a triangle, the integral over the boundary is 0. Cauchy's integral formula: \\(f(a)=\\frac{1}{2\\pi i}\\int_\\gamma f(z)/(z-a)\\,dz\\) for \\(a\\) inside a suitable closed curve.",
         "proof": "<p>Goursat’s proof for a triangle subdivides and uses a uniform estimate on the difference quotient. The integral formula reduces to the integral of \\(1/(z-a)\\) by writing \\(f(z)=f(a)+(f(z)-f(a))\\) and showing the second term integrates to 0.</p>"},
        {"name": "Consequences", "statement": "Holomorphic functions are analytic. Liouville: a bounded entire function is constant. The identity theorem: if two holomorphic functions on a connected open set agree on a set with a limit point, they agree everywhere.",
         "proof": "<p>Expand via Cauchy's formula as a power series. Liouville: Cauchy's estimates force every Taylor coefficient past the constant term to vanish when the function is bounded. The identity theorem uses isolation of zeros of a non identically zero holomorphic function.</p>"},
        {"name": "Residues", "statement": "The residue at an isolated singularity is the coefficient of \\(1/(z-a)\\) in the Laurent series, and the integral over a small circle is \\(2\\pi i\\) times that coefficient. A simple pole of \\(p/q\\) at a simple zero of \\(q\\) has residue \\(p(a)/q'(a)\\).",
         "proof": "<p>Laurent coefficients are Cauchy integrals. Only the \\(1/(z-a)\\) term survives integration over a circle. The simple-pole formula is the limit \\((z-a)p(z)/q(z)\\) as \\(z\\to a\\), which is \\(p(a)/q'(a)\\) by differentiability of \\(q\\).</p>"},
        {"name": "Real integrals", "statement": "A standard real integral of a rational function of sine and cosine, or a rational function with enough decay, can be read off from residues of a related complex function, provided you justify the vanishing of the integral on the closing arc.",
         "proof": "<p>The justification is an estimate: length of the arc times the maximum of the modulus. Write one such estimate, for a semicircle and a function with degree of the denominator at least two more than the numerator, before you use a table.</p>"},
    ],
    "tiers": {
        "0": [R("MIT 18.04 course page, the overview only",
                "https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/",
                "Read once, do not study from this. Read the overview so you see the destination is contour integrals and residues. The same site is the course; the preview is one pass over the description, then you start the problem sets as Tier 1.")],
        "1": [R("MIT 18.04 notes and problem sets",
                "https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/",
                "This is the main text. Ahlfors and Conway are the paid classics; editions were not verified, so they are not cited with fake ISBNs.")],
        "2": [R("18.04 exams and the harder problem sets",
                "https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/",
                "Do every set. The hardness is justifying arcs and branch cuts, not the residue arithmetic.")],
        "3": [R("Putnam problems that are complex analysis in disguise, via Kedlaya",
                "https://kskedlaya.org/putnam-archive/",
                "Qualifying exams in complex analysis are the real ceiling. Until you have a public quals PDF you have personally verified, the Putnam archive plus a complete 18.04 exam is the honest public ceiling.")],
    },
    "hardest": [
        {"label": "18.04 problem sets on Cauchy's theorem", "url": "https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/",
         "why": "You have to say where the function is holomorphic, not just compute."},
        {"label": "18.04 exams", "url": "https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/",
         "why": "Branch cuts and estimates show up without a section header."},
        {"label": "Compute a real improper integral by residues, with the arc estimate written", "url": "https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/",
         "why": "The estimate is the part everyone skips and the part the grader wants."},
        {"label": "Prove Liouville from Cauchy's estimates", "url": "https://kskedlaya.org/putnam-archive/2008.pdf",
         "why": "A short proof you should own. The Putnam link is a timed paper to attempt the same week, not the proof itself."},
        {"label": "Identity theorem, with the zeros-are-isolated lemma", "url": "https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/",
         "why": "This is the rigidity. Without the lemma the theorem is a slogan."},
    ],
    "gate": "<p>Pass: a timed 18.04 exam, plus written proofs of Cauchy's integral formula for a circle and of Liouville’s theorem. Fail if a residue computation has no sentence about the contour.</p>",
    "svg": frame(
        '<circle cx="320" cy="180" r="100" fill="none" stroke="#fff" stroke-width="1.5"/>'
        '<circle cx="320" cy="180" r="4" fill="#fff"/>'
        '<path d="M420 180 A100 100 0 0 0 320 80" fill="none" stroke="#fff"/>'
        '<polygon points="330,78 320,70 318,88" fill="#fff"/>'
        '<text x="330" y="176" fill="#bbb" font-size="14" font-family="Georgia, serif">a</text>',
        label="A circle contour around a point"),
    "caption": "Cauchy's formula rebuilds f(a) from the values on the circle.",
    "batches": [
        {"name": "Differentiability", "items": ["Cauchy–Riemann for \\(z^2\\) and for \\(\\bar z\\).", "Prove that a holomorphic function with zero derivative is locally constant, on a disk.", "Show \\(e^z\\) is entire.", "Find where \\(|z|^2\\) is complex differentiable.", "Express \\(f'(z)\\) in terms of \\(u_x\\) and \\(v_x\\)."]},
        {"name": "Integrals", "items": ["\\(\\int_{|z|=1} dz/z\\).", "\\(\\int_{|z|=2} dz/(z-1)\\).", "State Goursat’s theorem.", "Prove the integral of an exact derivative \\(F'\\) over a closed curve is zero when \\(F\\) is entire.", "Estimate \\(|\\int_\\gamma f|\\le \\mathrm{length}(\\gamma)\\cdot\\max|f|\\)."]},
        {"name": "Consequences", "items": ["Derive the Taylor series of \\(1/(1-z)\\) on the unit disk.", "Prove Liouville.", "Prove the fundamental theorem of algebra from Liouville.", "State the identity theorem.", "Give two different holomorphic functions that agree on \\(\\{1/n\\}\\). Explain why this does not contradict the identity theorem."]},
        {"name": "Residues", "items": ["Residue of \\(1/(z^2+1)\\) at \\(i\\).", "Simple-pole formula, proved.", "A semicircle estimate for \\(1/(z^2+1)\\).", "Compute \\(\\int_{-\\infty}^{\\infty} dx/(x^2+1)\\) by residues.", "A function with an essential singularity: \\(e^{1/z}\\). Name one Laurent coefficient."]},
        {"name": "Ceiling", "items": ["One 18.04 exam.", "Liouville from memory.", "One branch-cut problem from the course.", "Fundamental theorem of algebra via Liouville.", "Oral statement of Cauchy's formula."]},
    ],
    "bank": ["Cauchy–Riemann for \\(z^2\\).", "\\(\\int dz/z\\) on the unit circle.", "\\(\\bar z\\) is nowhere holomorphic.", "Liouville.", "Fundamental theorem of algebra via Liouville.", "Residue of \\(1/(z^2+1)\\) at \\(i\\).", "Real integral of \\(1/(x^2+1)\\).", "Identity theorem’s hypothesis.", "Arc estimate.", "One missed 18.04 problem."],
    "oral": "State Cauchy–Riemann, compute the unit-circle integral of \\(1/z\\), and state Liouville. No notes.",
}

MEA = {
    "slug": "measure-theory",
    "short": "Measure theory",
    "title": "Measure Theory",
    "track": "Math",
    "needs": ["real-analysis"],
    "what": """
<p>Measure theory replaces the Riemann integral, which cannot handle a pointwise limit of functions without an extra uniform-convergence hypothesis you often do not have. A measure assigns sizes to a σ-algebra of sets. Lebesgue measure on \\(\\mathbb{R}\\) extends length. The integral is built from simple functions up, and the convergence theorems — monotone convergence, Fatou, dominated convergence — are the reason the subject exists. \\(L^p\\) spaces are complete. That completeness is what makes Fourier analysis and probability sit on the same foundation.</p>
<p>Sheldon Axler’s Measure, Integration & Real Analysis is free from the author and is the main text. Rudin’s Real and Complex Analysis is the paid ceiling; no ISBN was verified for that specific title in this pass, so none is printed. Folland is the other standard paid book, same situation. You do not need either to learn the convergence theorems. You need to prove them.</p>
<p>A set of measure zero is not a set you can ignore inside a definition. It is a set you can ignore inside a statement that has already been proved to depend only on almost-everywhere behavior.</p>
""",
    "attack": [
        {"q": "<p>Show that any countable subset of \\(\\mathbb{R}\\) has Lebesgue outer measure zero.</p>",
         "a": "<p>Enumerate the set as \\(x_n\\). Cover \\(x_n\\) by an interval of length \\(\\varepsilon/2^n\\). The total length is \\(\\varepsilon\\). Outer measure is the infimum of such covers, so it is 0.</p>"},
        {"q": "<p>Why is the pointwise limit of the functions \\(f_n=n\\mathbf{1}_{(0,1/n)}\\) on \\([0,1]\\) not something the Riemann integral handles gracefully? Compute the integrals and the limit.</p>",
         "a": "<p>Each \\(f_n\\) integrates to 1. The pointwise limit is 0 everywhere (at 0 the functions are 0 if you define them that way, and for \\(x>0\\) eventually \\(1/n<x\\)). So the limit of the integrals is 1 and the integral of the limit is 0. There is no dominating integrable function that is independent of \\(n\\) and finite a.e. in a way that saves dominated convergence; the spikes escape every integrable dominant. This is why you need a hypothesis.</p>"},
        {"q": "<p>State dominated convergence in one sentence, including the dominant.</p>",
         "a": "<p>If \\(|f_n|\\le g\\) almost everywhere, \\(g\\) integrable, and \\(f_n\\to f\\) almost everywhere, then \\(f\\) is integrable and the integrals converge to the integral of \\(f\\).</p>"},
    ],
    "core": [
        {"name": "Measures", "statement": "A σ-algebra is closed under complements and countable unions. A measure is a countably additive \\([0,\\infty]\\)-valued function on it, with \\(\\mu(\\emptyset)=0\\). Lebesgue measure is the completion of the restriction of outer measure to the Carathéodory-measurable sets, and it extends length on intervals.",
         "proof": "<p>Countable additivity for disjoint intervals is a standard estimate. Carathéodory’s criterion produces a σ-algebra on which outer measure is a measure. Completion adds subsets of null sets.</p>"},
        {"name": "Integral", "statement": "The integral of a nonnegative simple function is the obvious sum. For a nonnegative measurable function it is the supremum of integrals of simple functions underneath. For a general measurable function it is the difference of the positive and negative parts, when at least one is finite.",
         "proof": "<p>Well-definedness of the simple-function integral uses a common refinement of the level sets. Monotone convergence is then used to prove linearity for nonnegative functions. Write that once.</p>"},
        {"name": "Convergence theorems", "statement": "Monotone convergence: if \\(0\\le f_n\\uparrow f\\) then the integrals rise to the integral of \\(f\\). Fatou: the integral of the liminf is at most the liminf of the integrals. Dominated convergence is the statement in the attack.",
         "proof": "<p>Monotone convergence is the technical heart; Fatou is monotone convergence applied to the infima from each index onward; dominated convergence is Fatou applied to \\(g+f_n\\) and \\(g-f_n\\).</p>"},
        {"name": "Fubini", "statement": "For σ-finite measures, the integral of a nonnegative measurable function on a product equals the iterated integrals in either order. For integrable functions of either sign, the same holds, and almost every slice is integrable.",
         "proof": "<p>Prove it for indicators of measurable rectangles, then for simple functions, then by monotone convergence. The signed case uses integrability to justify the difference.</p>"},
        {"name": "L^p", "statement": "\\(L^p\\) is the space of measurable functions with \\(\\int |f|^p<\\infty\\), modulo almost-everywhere equality. It is a Banach space for \\(1\\le p\\le\\infty\\). Hölder’s inequality is the tool that makes the dual of \\(L^p\\) look like \\(L^q\\).",
         "proof": "<p>Completeness is: a fast Cauchy sequence has a subsequence with \\(\\|f_{n_{k+1}}-f_{n_k}\\|<2^{-k}\\), the telescoping series converges absolutely almost everywhere by monotone convergence, and the limit is the \\(L^p\\) limit. Hölder is Young’s inequality integrated.</p>"},
    ],
    "tiers": {
        "0": [R("Axler, the measure-theory book site", "https://measure.axler.net/",
                "Read once, do not study from this. Confirm the PDF is the free book and see the table of contents. Then work in the PDF.")],
        "1": [R("Axler, Measure, Integration & Real Analysis", "https://measure.axler.net/MIRA.pdf",
                "Free legal PDF from the author. This is the main text. It goes from measure through functional analysis at a level you can actually finish.")],
        "2": [R("Axler’s exercises on the convergence theorems and L^p", "https://measure.axler.net/MIRA.pdf",
                "The book is the problem set. Do not skip the “prove that this hypothesis is necessary” exercises.")],
        "3": [R("A qualifying-exam style reconstruction of dominated convergence", "https://measure.axler.net/MIRA.pdf",
                "Rudin’s Real and Complex Analysis and Folland are the paid ceilings; ISBNs were not verified, so they are not numbered here. The public ceiling is: write the three convergence theorems and a counterexample for each missing hypothesis, from memory.")],
    },
    "hardest": [
        {"label": "Axler, monotone convergence and the exercises after it", "url": "https://measure.axler.net/MIRA.pdf",
         "why": "Every later theorem is this one with a costume."},
        {"label": "A counterexample to interchanging limit and integral", "url": "https://measure.axler.net/MIRA.pdf",
         "why": "The spikes \\(n\\mathbf{1}_{(0,1/n)}\\) are the prototype. You need two more, including one where Fatou is strict."},
        {"label": "Prove L^p is complete", "url": "https://measure.axler.net/MIRA.pdf",
         "why": "The subsequence trick is the one you will reuse for the rest of your life."},
        {"label": "Fubini for a nonnegative function, written", "url": "https://measure.axler.net/",
         "why": "People apply Fubini to signed functions they have not shown to be integrable. The proof tells you why the hypothesis is there."},
        {"label": "State Hölder and use it to prove the dual pairing of L^p and L^q is well-defined", "url": "https://measure.axler.net/MIRA.pdf",
         "why": "This is the door to functional analysis. A slogan does not open it."},
    ],
    "gate": "<p>Pass: from memory, the proofs of monotone convergence’s consequences (Fatou and dominated convergence, assuming monotone convergence) and the construction of a non-integrable pointwise limit of integrable functions. Plus the completeness of \\(L^1\\). Fail if “almost everywhere” is not in the statements.</p>",
    "svg": frame(
        '<line x1="40" y1="280" x2="600" y2="280" stroke="#fff"/>'
        '<rect x="80" y="200" width="30" height="80" fill="none" stroke="#fff"/>'
        '<rect x="140" y="120" width="20" height="160" fill="none" stroke="#fff"/>'
        '<rect x="200" y="60" width="12" height="220" fill="none" stroke="#fff"/>'
        '<rect x="260" y="20" width="8" height="260" fill="none" stroke="#fff"/>'
        '<text x="300" y="80" fill="#bbb" font-size="13" font-family="Georgia, serif">taller, thinner</text>',
        label="Spikes of constant integral and increasing height"),
    "caption": "The integrals stay 1. The pointwise limit is 0. Dominated convergence needs a dominant.",
    "batches": [
        {"name": "Measure", "items": ["Outer measure of a countable set.", "Prove countable subadditivity of outer measure.", "Show a single point has measure zero.", "Why is the Vitali set nonmeasurable? Outline, including where choice is used.", "Intervals are measurable. Say which theorem you are quoting."]},
        {"name": "Functions", "items": ["A function is measurable iff preimages of intervals \\((-\\infty,a)\\) are measurable. Prove one direction.", "Pointwise limits of measurable functions are measurable.", "Simple-function approximation of a nonnegative measurable function.", "Integral of a simple function, well-defined.", "\\(\\int n 1_{(0,1/n)}=1\\)."]},
        {"name": "Theorems", "items": ["State monotone convergence.", "Deduce Fatou.", "Deduce dominated convergence.", "Give a case where Fatou is strict.", "Give a case where there is no integrable dominant."]},
        {"name": "Product and L^p", "items": ["Fubini’s hypothesis for signed functions.", "Hölder for sums, then for integrals.", "Prove L^1 completeness with the subsequence trick.", "\\(\\|f\\|_\\infty\\) as an essential supremum. Give a function where the essential supremum is smaller than every bound you would guess from pointwise values on the rationals... or explain why that cannot happen for a continuous function.", "Minkowski’s inequality, stated."]},
        {"name": "Ceiling", "items": ["All three convergence theorems, memory.", "Completeness of L^p.", "One counterexample page, three examples.", "Fubini outline.", "Oral definition of the integral."]},
    ],
    "bank": ["Countable sets have measure zero.", "The escaping spike.", "Dominated convergence, full statement.", "Fatou from monotone convergence.", "Measurable functions are closed under pointwise limits.", "L^1 completeness.", "Hölder.", "Fubini’s σ-finite hypothesis.", "Vitali set, where choice enters.", "Essential supremum."],
    "oral": "Define a measure, state dominated convergence with the dominant, and explain the spike counterexample. No notes.",
}

PDE = {
    "slug": "pde",
    "short": "PDEs",
    "title": "Partial Differential Equations",
    "track": "Math",
    "needs": ["ode", "calc-3"],
    "what": """
<p>Partial differential equations ask for functions of several variables whose partial derivatives satisfy a relation. The introductory trinity is the Laplace equation, the heat equation, and the wave equation. They are the models of equilibrium, diffusion, and propagation. Separation of variables turns them into Sturm–Liouville problems you already met in ordinary differential equations. Energy estimates and maximum principles are the tools that survive after separation of variables stops working, which is almost immediately on a domain that is not a rectangle.</p>
<p>MIT 18.152 is a real introduction with assignments, and it is the course to work. Strauss’s Partial Differential Equations is the standard paid book; no edition was verified. Evans is the graduate ceiling and is paid, same situation. You are not ready for Evans until maximum principles and energy methods are boring. Fourier series from the ODE page are a prerequisite you must actually be able to use, not a topic you once saw.</p>
<p>A formal series that does not satisfy the boundary conditions is not a solution. Write the conditions first.</p>
""",
    "attack": [
        {"q": "<p>Solve \\(u_t=u_{xx}\\) for \\(0<x<\\pi\\), \\(t>0\\), with \\(u(0,t)=u(\\pi,t)=0\\) and \\(u(x,0)=\\sin x\\).</p>",
         "a": "<p>Separate: \\(X''+\\lambda X=0\\), \\(X(0)=X(\\pi)=0\\), so \\(\\lambda=n^2\\), \\(X=\\sin nx\\). Time part \\(T'= -n^2 T\\). The initial condition is already a single mode, so \\(u(x,t)=e^{-t}\\sin x\\).</p>"},
        {"q": "<p>For the wave equation \\(u_{tt}=c^2 u_{xx}\\) on the line, state d’Alembert’s formula and the domain of dependence of a point \\((x,t)\\).</p>",
         "a": "<p>\\(u(x,t)=\\frac{1}{2}(f(x+ct)+f(x-ct))+\\frac{1}{2c}\\int_{x-ct}^{x+ct} g\\), for initial position \\(f\\) and velocity \\(g\\). The value at \\((x,t)\\) depends only on the initial data in \\([x-ct,x+ct]\\).</p>"},
        {"q": "<p>Why does a maximum principle for the heat equation say a hot spot in the interior cannot appear later if it was not on the boundary or in the initial data?</p>",
         "a": "<p>For the heat equation on a bounded interval, the maximum of a solution on a closed time-space rectangle is attained on the parabolic boundary: the initial segment and the lateral sides. An interior maximum at a positive time would force, by the equation and the second-derivative test, a contradiction unless the solution is constant. So a new interior hot spot cannot be born.</p>"},
    ],
    "core": [
        {"name": "Classification", "statement": "A second-order linear equation \\(au_{xx}+2bu_{xy}+cu_{yy}+\\cdots=0\\) is elliptic, parabolic, or hyperbolic according to the sign of \\(b^2-ac\\), the same discriminant as a conic. Laplace, heat, and wave are the models.",
         "proof": "<p>A linear change of variables diagonalizes the principal symbol. The sign of the discriminant is invariant and decides whether you get a sum of squares, a heat-type degeneracy, or a difference of squares.</p>"},
        {"name": "Separation", "statement": "On a rectangle or an interval, product solutions \\(X(x)T(t)\\) reduce the PDE to ODEs. The spatial operator with the boundary conditions produces an orthogonal basis of eigenfunctions. The initial condition becomes a coefficient problem.",
         "proof": "<p>Plug in, divide, and equate a function of \\(x\\) to a function of \\(t\\). Orthogonality of sines on \\([0,\\pi]\\) is a calculus computation. Completeness of the basis is a theorem you may quote from Fourier analysis after you have used the coefficients correctly.</p>"},
        {"name": "Wave equation", "statement": "d’Alembert’s formula solves the one-dimensional wave equation on the line. Finite propagation speed is the domain of dependence. Reflections come from the method of images when the boundary condition is Dirichlet or Neumann on a half-line.",
         "proof": "<p>Factor \\(\\partial_{tt}-c^2\\partial_{xx}=(\\partial_t-c\\partial_x)(\\partial_t+c\\partial_x)\\) and change to characteristic coordinates \\(\\xi=x+ct\\), \\(\\eta=x-ct\\). The general solution is \\(F(\\xi)+G(\\eta)\\). Match initial conditions to get the formula.</p>"},
        {"name": "Maximum principle", "statement": "A harmonic function on a bounded domain attains its maximum and minimum on the boundary. A consequence is uniqueness for the Dirichlet problem.",
         "proof": "<p>If the Laplacian is positive, a maximum cannot occur at an interior point because the Hessian would have negative trace. For harmonic functions, apply that to \\(u+\\varepsilon|x|^2\\) and let \\(\\varepsilon\\to 0\\). Uniqueness: the difference of two solutions is zero on the boundary and harmonic, hence zero.</p>"},
        {"name": "Energy", "statement": "For the wave equation with suitable boundary conditions, the sum of kinetic and potential energy is constant. That identity gives uniqueness of the initial-boundary-value problem.",
         "proof": "<p>Multiply the equation by \\(u_t\\) and integrate by parts. The boundary terms vanish because of the boundary condition. What remains is the derivative of the energy.</p>"},
    ],
    "tiers": {
        "0": [R("MIT 18.152, the course description",
                "https://ocw.mit.edu/courses/18-152-introduction-to-partial-differential-equations-fall-2011/",
                "Read once, do not study from this. See that the course is Laplace, heat, and wave, not a catalogue of tricks. Then use the assignments as the work.")],
        "1": [R("MIT 18.152 assignments and notes",
                "https://ocw.mit.edu/courses/18-152-introduction-to-partial-differential-equations-fall-2011/",
                "The main text. Strauss is the usual paid book; no edition was verified.")],
        "2": [R("18.152 problem sets, every one",
                "https://ocw.mit.edu/courses/18-152-introduction-to-partial-differential-equations-fall-2011/",
                "Separation, maximum principles, and energy estimates are all in the sets. Do them in order.")],
        "3": [R("Evans is the graduate ceiling; the public ceiling is a full 18.152 exam plus d’Alembert from memory",
                "https://ocw.mit.edu/courses/18-152-introduction-to-partial-differential-equations-fall-2011/",
                "Evans is paid and unnumbered here. Do not start it until the maximum principle proof is yours.")],
    },
    "hardest": [
        {"label": "18.152 assignments on separation of variables", "url": "https://ocw.mit.edu/courses/18-152-introduction-to-partial-differential-equations-fall-2011/",
         "why": "The eigenvalue problem includes the boundary conditions. Forget them and the series is wrong."},
        {"label": "A maximum-principle proof for harmonic functions", "url": "https://ocw.mit.edu/courses/18-152-introduction-to-partial-differential-equations-fall-2011/",
         "why": "The ε|x|² trick is short and easy to garble."},
        {"label": "d’Alembert from the factored operator", "url": "https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/",
         "why": "You should derive it, not memorize it. The 18.03 link is the ODE course that prepared the characteristics."},
        {"label": "Energy conservation for the wave equation", "url": "https://ocw.mit.edu/courses/18-152-introduction-to-partial-differential-equations-fall-2011/",
         "why": "Integration by parts with boundary terms is the whole proof. The idea is one line."},
        {"label": "Uniqueness for the Dirichlet problem on a bounded domain", "url": "https://ocw.mit.edu/courses/18-152-introduction-to-partial-differential-equations-fall-2011/",
         "why": "It is the maximum principle applied to a difference. Say so in a proof, not in a phrase."},
    ],
    "gate": "<p>Pass: solve the heat equation on an interval for a general sine series initial condition, derive d’Alembert’s formula, and prove uniqueness for the Dirichlet problem via the maximum principle. Written. Fail if the series ignores the boundary conditions.</p>",
    "svg": frame(
        '<path d="M40 220 Q 120 80, 200 220 T 360 220 T 520 220 T 600 180" fill="none" stroke="#fff"/>'
        '<path d="M40 240 Q 120 140, 200 240 T 360 240 T 520 240 T 600 210" fill="none" stroke="rgba(255,255,255,0.55)"/>'
        '<text x="70" y="70" fill="#bbb" font-size="13" font-family="Georgia, serif">later, smaller</text>',
        label="A heat profile flattening"),
    "caption": "Heat flattens. The maximum does not grow.",
    "batches": [
        {"name": "Models", "items": ["Classify Laplace, heat, and wave by the discriminant.", "Derive the heat equation from a flux proportional to the gradient, in one sentence of conservation.", "Write the Laplacian in polar coordinates. You may look up the formula only after you have started the chain rule.", "Boundary conditions: Dirichlet versus Neumann, in words.", "An initial condition is not a boundary condition. Say where each lives."]},
        {"name": "Separation", "items": ["The sine series for the attack problem.", "Heat equation with \\(u(x,0)=\\sin x+\\frac13\\sin 3x\\).", "Wave equation on \\((0,\\pi)\\) with zero ends and initial velocity 0, initial position \\(\\sin 2x\\).", "Show that \\(X''+\\lambda X=0\\) with \\(X(0)=X(\\pi)=0\\) has a nonzero solution only when \\(\\lambda=n^2\\) for a positive integer \\(n\\).", "Coefficients of a square wave via inner products."]},
        {"name": "Characteristics", "items": ["Solve \\(u_t+cu_x=0\\) by characteristics.", "Derive d’Alembert.", "Domain of dependence.", "Method of images for the half-line, Dirichlet, one example.", "Finite propagation: a change in the initial data outside \\([x-ct,x+ct]\\) does not affect \\(u(x,t)\\)."]},
        {"name": "Principles", "items": ["Maximum principle for harmonic functions, proof.", "Uniqueness for Dirichlet.", "Energy for the wave equation.", "Uniqueness from energy.", "A formal series that fails the boundary condition, and the repair."]},
        {"name": "Ceiling", "items": ["One 18.152 assignment done cold.", "d’Alembert from memory.", "Maximum principle from memory.", "A heat-equation series with two modes.", "Oral classification of the three equations."]},
    ],
    "bank": ["Heat equation, initial sine.", "d’Alembert.", "Domain of dependence.", "Maximum principle.", "Dirichlet uniqueness.", "Energy identity.", "Classification by discriminant.", "Sine series coefficients.", "Transport equation \\(u_t+cu_x=0\\).", "A series that violated the boundary condition."],
    "oral": "Classify the three second-order equations, solve the heat equation for a sine initial condition, and state the maximum principle. No notes.",
}

NUM = {
    "slug": "number-theory",
    "short": "Number theory",
    "title": "Number Theory",
    "track": "Math",
    "needs": ["proof-logic"],
    "what": """
<p>Elementary number theory is the arithmetic of the integers: divisibility, primes, congruences, and the multiplicative group of units modulo \\(n\\). The theorems you use forever are Euclid’s lemma, the Euclidean algorithm, the Chinese remainder theorem, Fermat’s little theorem, and the existence of primitive roots modulo primes. Quadratic reciprocity is the first theorem that feels deeper than the definitions. Analytic number theory, which counts primes, is a later life. This page stops at reciprocity and at the contest problems that use only this machinery.</p>
<p>William Stein’s Elementary Number Theory is a free PDF and it is the working book. Ireland and Rosen is the paid next book; no edition was verified. Contest number theory at the AIME and early Putnam level is the ceiling that matches this page. Algebraic number theory waits until the abstract-algebra page is real.</p>
<p>If you cannot compute a modular inverse by hand, you do not know the Euclidean algorithm, regardless of how many theorems you can name.</p>
""",
    "attack": [
        {"q": "<p>Prove there are infinitely many primes.</p>",
         "a": "<p>If \\(p_1,\\ldots,p_k\\) were all the primes, then \\(N=p_1\\cdots p_k+1\\) would have a prime factor, and that factor could not be any \\(p_i\\), because \\(N\\) leaves remainder 1 on division by each \\(p_i\\).</p>"},
        {"q": "<p>Solve \\(3x\\equiv 1\\pmod{10}\\).</p>",
         "a": "<p>The inverse of 3 mod 10 is 7, because \\(21\\equiv 1\\). So \\(x\\equiv 7\\pmod{10}\\).</p>"},
        {"q": "<p>State Fermat’s little theorem and use it to compute \\(2^{10}\\mod 11\\).</p>",
         "a": "<p>If \\(p\\) is prime and \\(p\\nmid a\\), then \\(a^{p-1}\\equiv 1\\pmod p\\). Here \\(2^{10}\\equiv 1\\pmod{11}\\).</p>"},
    ],
    "core": [
        {"name": "Divisibility", "statement": "The Euclidean algorithm computes \\(\\gcd\\). Bézout: \\(\\gcd(a,b)=ax+by\\) for some integers \\(x,y\\). Euclid’s lemma: if a prime divides a product, it divides a factor. Unique factorization follows.",
         "proof": "<p>The algorithm produces a descending sequence of remainders and the gcd is preserved at each step. Back-substitution gives Bézout. Euclid’s lemma is Bézout applied to a prime that shares no factor with one of the terms.</p>"},
        {"name": "Congruences", "statement": "\\(ax\\equiv b\\pmod n\\) has a solution iff \\(\\gcd(a,n)\\) divides \\(b\\), and then there are exactly that many solutions modulo \\(n\\). The Chinese remainder theorem: if the moduli are coprime in pairs, the system has a unique solution modulo the product.",
         "proof": "<p>Solvability is Bézout. The Chinese remainder theorem for two moduli is an explicit Bézout combination; the general case is induction.</p>"},
        {"name": "Units", "statement": "\\((\\mathbb{Z}/n\\mathbb{Z})^\\times\\) is a group of order \\(\\varphi(n)\\). Euler’s theorem: \\(a^{\\varphi(n)}\\equiv 1\\pmod n\\) when \\(\\gcd(a,n)=1\\). Fermat is the prime case. For an odd prime \\(p\\), the multiplicative group mod \\(p\\) is cyclic.",
         "proof": "<p>Euler is Lagrange applied to the unit group. Cyclicity modulo a prime is proved by counting elements of each order using the factorization of \\(x^{d}-1\\), or by quoting the structure theorem for finite subgroups of the multiplicative group of a field.</p>"},
        {"name": "Quadratic residues", "statement": "The Legendre symbol \\(\\left(\\frac{a}{p}\\right\\)\\) is 1, −1, or 0 according as \\(a\\) is a quadratic residue, a nonresidue, or 0 mod an odd prime \\(p\\). Euler’s criterion and the law of quadratic reciprocity compute it.",
         "proof": "<p>Euler’s criterion is \\(a^{(p-1)/2}\\equiv\\left(\\frac{a}{p}\\right)\\pmod p\\), from the cyclic group. Reciprocity is a real theorem; learn one proof, Gauss’s lemma being the most elementary, and be able to use the statement even while the proof is still fragile.</p>"},
        {"name": "Diophantine samples", "statement": "Linear Diophantine equations are Bézout. The equation \\(x^2+y^2=z^2\\) is solved by rational points on the circle, or by the standard parametrization. Fermat’s theorem on sums of two squares characterizes primes that are sums of two squares as 2 and those congruent to 1 mod 4.",
         "proof": "<p>The parametrization of Pythagorean triples comes from the slope of the line through \\((-1,0)\\) on the unit circle. The sum-of-two-squares theorem uses the fact that −1 is a square mod \\(p\\) exactly when \\(p=2\\) or \\(p\\equiv 1\\pmod 4\\), which is a Legendre-symbol computation, plus a descent.</p>"},
    ],
    "tiers": {
        "0": [R("Stein, Elementary Number Theory, the PDF’s table of contents",
                "https://wstein.org/ent/ent.pdf",
                "Read once, do not study from this. Skim the contents so you see the path from gcd to reciprocity. Then start at chapter 1 and do the exercises.")],
        "1": [R("William Stein, Elementary Number Theory: Primes, Congruences, and Secrets",
                "https://wstein.org/ent/ent.pdf",
                "Free PDF. This is the main text. It includes computation, which keeps the theorems honest.")],
        "2": [R("AIME number theory and Stein’s exercises",
                "https://artofproblemsolving.com/wiki/index.php/AIME_Problems_and_Solutions",
                "AIME is the right hard-problem layer. Stein’s later exercises are the other half.")],
        "3": [R("Putnam number theory via Borisov and Kedlaya",
                "https://people.math.binghamton.edu/borisov/Putnam/SelectedProblemList.pdf",
                "The sorted list plus the archive https://kskedlaya.org/putnam-archive/ . Ireland and Rosen is the paid graduate-leaning book; no edition was verified.")],
    },
    "hardest": [
        {"label": "AIME number theory, problems 10–15", "url": "https://artofproblemsolving.com/wiki/index.php/AIME_Problems_and_Solutions",
         "why": "Modular arithmetic under a requirement that the answer is a three-digit integer."},
        {"label": "Borisov, number theory section", "url": "https://people.math.binghamton.edu/borisov/Putnam/SelectedProblemList.pdf",
         "why": "Putnam number theory is olympiad number theory with less time and cleaner writing demanded."},
        {"label": "Quadratic reciprocity computations in Stein", "url": "https://wstein.org/ent/ent.pdf",
         "why": "The symbol is easy to mis-multiply. The exercises catch that."},
        {"label": "Prove the multiplicative group mod p is cyclic, as far as you can", "url": "https://wstein.org/ent/ent.pdf",
         "why": "This is the structural theorem of the page. A citation is not a proof."},
        {"label": "Infinitely many primes congruent to 3 mod 4", "url": "https://wstein.org/ent/ent.pdf",
         "why": "Euclid’s proof with one extra idea. If you cannot find the idea, you do not yet own congruences."},
    ],
    "gate": "<p>Pass: Euclidean algorithm and inverse, from memory; proof of infinitely many primes; proof of Euler’s theorem from Lagrange; five AIME number-theory problems numbered 10 or higher. Fail if quadratic reciprocity is a formula you cannot evaluate on a small prime.</p>",
    "svg": frame(
        '<line x1="40" y1="180" x2="600" y2="180" stroke="#fff"/>'
        + "".join(
            f'<line x1="{40+i*28}" y1="172" x2="{40+i*28}" y2="188" stroke="#fff"/>'
            for i in range(20)
        )
        + '<circle cx="40" cy="180" r="5" fill="#000" stroke="#fff"/>'
        + '<circle cx="96" cy="180" r="5" fill="#fff"/>'
        + '<circle cx="152" cy="180" r="5" fill="#fff"/>'
        + '<circle cx="208" cy="180" r="5" fill="#fff"/>'
        + '<text x="80" y="150" fill="#bbb" font-size="13" font-family="Georgia, serif">primes</text>',
        label="A number line with a few primes marked"),
    "caption": "The Euclidean algorithm is the whole elementary theory in one loop.",
    "batches": [
        {"name": "Arithmetic", "items": ["Euclidean algorithm for 252 and 198.", "Bézout coefficients for that pair.", "Prove Euclid’s lemma.", "Infinitely many primes.", "Infinitely many primes congruent to 3 mod 4."]},
        {"name": "Congruences", "items": ["Solve \\(3x\\equiv 1\\pmod{10}\\).", "Solve the system \\(x\\equiv 2\\pmod 3\\), \\(x\\equiv 3\\pmod 5\\).", "State the Chinese remainder theorem.", "Compute \\(\\varphi(100)\\).", "Euler: last two digits of \\(3^{40}\\), or say why you need a sharper tool."]},
        {"name": "Structure", "items": ["Fermat mod 11 on \\(2^{10}\\).", "Find a primitive root mod 7.", "Prove Euler from Lagrange.", "Show \\((\\mathbb{Z}/8\\mathbb{Z})^\\times\\) is not cyclic.", "Order of 2 mod 13."]},
        {"name": "Residues", "items": ["Legendre symbol \\((2/7)\\) by listing.", "Euler’s criterion for that symbol.", "One reciprocity computation Stein assigns.", "Which primes are sums of two squares? State the theorem.", "A Pythagorean triple that is not a multiple of 3-4-5, generated by the parametrization."]},
        {"name": "Ceiling", "items": ["Five AIME number-theory problems, number ≥ 10.", "Three Borisov problems.", "Primitive root existence, outline.", "Infinitely many primes 3 mod 4, memory.", "Oral Euclidean algorithm."]},
    ],
    "bank": ["Infinitely many primes.", "Inverse of 3 mod 10.", "Fermat mod 11.", "Chinese remainder, two moduli.", "\\(\\varphi(100)\\).", "Primitive root mod 7.", "Units mod 8 are not cyclic.", "Euclid’s lemma.", "Primes 3 mod 4, infinitely many.", "One AIME #12 on congruences."],
    "oral": "Prove there are infinitely many primes, compute a modular inverse with the Euclidean algorithm, and state Fermat’s little theorem. No notes.",
}

COM = {
    "slug": "combinatorics",
    "short": "Combinatorics",
    "title": "Combinatorics",
    "track": "Math",
    "needs": ["proof-logic"],
    "what": """
<p>Combinatorics on this page means counting, bijections, generating functions, and the first graph-theoretic facts you need in order to not be helpless on an olympiad or a Putnam A1. The binomial theorem, inclusion–exclusion, pigeonhole, and recurrence relations are the whole elementary theory. Ordinary generating functions turn linear recurrences into algebra. A graph is a set of vertices and edges; trees, bipartite graphs, and the handshake lemma are the part you must be able to prove in a paragraph.</p>
<p>Lehman, Leighton, and Meyer’s Mathematics for Computer Science is free and contains a serious counting and graph section. It is the working text. Wilf’s generatingfunctionology is the right specialized book; the Penn URL that used to host it did not return a stable copy in this check, so it is not linked. Use the generating-function chapters of the MIT notes instead. AIME and Putnam counting problems are the ceiling.</p>
<p>A counting argument that does not say what is being counted, and in what order, is a guess with binomial coefficients glued on.</p>
""",
    "attack": [
        {"q": "<p>How many ways can you choose 2 elements from a set of \\(n\\)? Derive the formula, do not quote it.</p>",
         "a": "<p>There are \\(n(n-1)\\) ordered pairs of distinct elements, and each unordered pair was counted twice, so \\(\\binom{n}{2}=n(n-1)/2\\).</p>"},
        {"q": "<p>Prove the handshake lemma: the sum of degrees in a graph is twice the number of edges.</p>",
         "a": "<p>Count the set of pairs \\((v,e)\\) with \\(v\\) incident to \\(e\\) in two ways. Summing degrees counts each edge twice, once at each end.</p>"},
        {"q": "<p>Use inclusion–exclusion to count the integers from 1 to 100 that are divisible by 2 or 3 or 5.</p>",
         "a": "<p>\\(\\lfloor 100/2\\rfloor+\\lfloor 100/3\\rfloor+\\lfloor 100/5\\rfloor-\\lfloor 100/6\\rfloor-\\lfloor 100/10\\rfloor-\\lfloor 100/15\\rfloor+\\lfloor 100/30\\rfloor=50+33+20-16-10-6+3=74\\).</p>"},
    ],
    "core": [
        {"name": "Binomial theorem", "statement": "\\((x+y)^n=\\sum_{k=0}^n\\binom{n}{k}x^{n-k}y^k\\). Pascal’s recurrence \\(\\binom{n}{k}=\\binom{n-1}{k}+\\binom{n-1}{k-1}\\) has a bijective proof.",
         "proof": "<p>The binomial theorem is the distributive law: each term picks \\(x\\) or \\(y\\) from each factor. Pascal: a \\(k\\)-subset of an \\(n\\)-set either contains a distinguished element or it does not.</p>"},
        {"name": "Inclusion–exclusion and pigeonhole", "statement": "The size of a union is the alternating sum of the sizes of intersections. If more than \\(kn\\) pigeons sit in \\(n\\) holes, some hole has at least \\(k+1\\) pigeons.",
         "proof": "<p>Inclusion–exclusion is induction on the number of sets, or an indicator-function identity: \\(\\prod(1-1_{A_i})\\) expands to the alternating sum. Pigeonhole is the contrapositive of “\\(k\\) per hole gives at most \\(kn\\).”</p>"},
        {"name": "Recurrences and generating functions", "statement": "The ordinary generating function of a sequence turns a linear recurrence into a rational function. The Fibonacci generating function is \\(x/(1-x-x^2)\\). Partial fractions extract coefficients.",
         "proof": "<p>Multiply the recurrence by \\(x^n\\) and sum. The initial conditions fix the numerator. Partial fractions and the geometric series give the Binet-style closed form if you want it; the generating function is already the answer for many problems.</p>"},
        {"name": "Graphs", "statement": "Handshake lemma. A tree on \\(n\\) vertices has \\(n-1\\) edges and is connected and acyclic; any two of those properties imply the third, among the usual list. A graph is bipartite if and only if it has no odd cycle.",
         "proof": "<p>A tree has a leaf; delete it and induct to get \\(n-1\\) edges. Bipartite: color by distance from a vertex on each component; an odd cycle makes the color inconsistent. Conversely an odd cycle cannot be 2-colored.</p>"},
        {"name": "Double counting", "statement": "If you count a set of pairs in two ways, you get an identity. This is the source of the handshake lemma, of \\(\\sum k\\binom{n}{k}=n2^{n-1}\\), and of most olympiad counting proofs that look like magic.",
         "proof": "<p>The identity \\(\\sum k\\binom{n}{k}=n2^{n-1}\\) counts pairs \\((x,S)\\) with \\(x\\in S\\subseteq\\{1,\\ldots,n\\}\\): choose the distinguished element first, or choose the set and then the element.</p>"},
    ],
    "tiers": {
        "0": [R("Lehman, Leighton, Meyer, the contents page of the PDF",
                "https://courses.csail.mit.edu/6.042/spring18/mcs.pdf",
                "Read once, do not study from this. Find the counting and graph chapters. Then work those chapters and skip the rest until you want it.")],
        "1": [R("Mathematics for Computer Science, Lehman, Leighton, Meyer",
                "https://courses.csail.mit.edu/6.042/spring18/mcs.pdf",
                "Free. The counting, induction, and graph chapters are the main text. Better than a paid combinatorics survey you will not finish, because the problems are inline and the book is complete.")],
        "2": [R("AIME counting problems",
                "https://artofproblemsolving.com/wiki/index.php/AIME_Problems_and_Solutions",
                "The hard-problem layer. Filter by combinatorics using the AoPS index or Po-Shen Loh: https://live.poshenloh.com/")],
        "3": [R("Putnam combinatorics, Borisov’s list",
                "https://people.math.binghamton.edu/borisov/Putnam/SelectedProblemList.pdf",
                "The ceiling at this level. Generatingfunctionology is the right extra book if you find a legal copy you can verify yourself; a stable free URL was not confirmed here.")],
    },
    "hardest": [
        {"label": "AIME counting, problems 10–15", "url": "https://artofproblemsolving.com/wiki/index.php/AIME_Problems_and_Solutions",
         "why": "Overcounting is the entire difficulty. The arithmetic is nothing."},
        {"label": "Po-Shen Loh, combinatorics at the top rating", "url": "https://live.poshenloh.com/",
         "why": "Sorted, so you cannot hide in algebra."},
        {"label": "Borisov, combinatorics", "url": "https://people.math.binghamton.edu/borisov/Putnam/SelectedProblemList.pdf",
         "why": "Putnam counting problems are proofs, not three-digit answers."},
        {"label": "Handshake lemma and the tree theorem, blank page", "url": "https://courses.csail.mit.edu/6.042/spring18/mcs.pdf",
         "why": "If these are not instant, the later problems will be folklore you cannot use."},
        {"label": "Fibonacci generating function, derived", "url": "https://courses.csail.mit.edu/6.042/spring18/mcs.pdf",
         "why": "One derivation teaches the method. A memorized Binet formula does not."},
    ],
    "gate": "<p>Pass: handshake lemma, binomial theorem, and inclusion–exclusion for three sets, from memory, plus five AIME counting problems numbered 8 or higher and two Putnam combinatorics problems with full proofs. Fail if a count does not name the set being counted.</p>",
    "svg": frame(
        '<circle cx="160" cy="180" r="8" fill="#fff"/>'
        '<circle cx="320" cy="80" r="8" fill="#fff"/>'
        '<circle cx="320" cy="280" r="8" fill="#fff"/>'
        '<circle cx="480" cy="180" r="8" fill="#fff"/>'
        '<line x1="160" y1="180" x2="320" y2="80" stroke="#fff"/>'
        '<line x1="160" y1="180" x2="320" y2="280" stroke="#fff"/>'
        '<line x1="320" y1="80" x2="480" y2="180" stroke="#fff"/>'
        '<line x1="320" y1="280" x2="480" y2="180" stroke="#fff"/>',
        label="A tree on four vertices"),
    "caption": "Four vertices, three edges, connected, no cycle. Any two of those force the third, in the usual theorem.",
    "batches": [
        {"name": "Counts", "items": ["Derive \\(\\binom{n}{2}\\).", "Pascal’s identity, bijectively.", "Binomial theorem for \\(n=3\\), expanded by hand, then the general proof.", "How many subsets does an \\(n\\)-set have? Two proofs.", "\\(\\sum k\\binom{n}{k}=n2^{n-1}\\), by double counting."]},
        {"name": "Inclusion and pigeons", "items": ["Integers from 1 to 100 divisible by 2, 3, or 5.", "Derangements of 3 items, by inclusion–exclusion.", "Pigeonhole: among 5 integers, two have the same remainder mod 4.", "Five points in a square of side 1; two are at most \\(\\sqrt{2}/2\\) apart. Prove it.", "State inclusion–exclusion for three sets from memory."]},
        {"name": "Recurrences", "items": ["Fibonacci recurrence, first ten terms, and the generating function.", "Number of binary strings of length \\(n\\) with no two consecutive 1s. Find the recurrence.", "Solve \\(a_n=3a_{n-1}\\), \\(a_0=2\\).", "A linear recurrence of order 2, characteristic polynomial, one example.", "Partial fractions of \\(x/(1-x-x^2)\\), as far as you are willing to go."]},
        {"name": "Graphs", "items": ["Handshake lemma.", "A tree has \\(n-1\\) edges.", "Prove bipartite iff no odd cycle.", "Draw a connected graph with exactly one cycle and count its edges.", "Euler’s formula \\(V-E+F=2\\) for a connected plane graph, proved by induction or clearly cited as not yet proved."]},
        {"name": "Ceiling", "items": ["Five AIME counting problems.", "Two Putnam combinatorics proofs.", "Generating function of the no-consecutive-1s strings.", "Oral handshake lemma.", "One double-counting identity you invent and then prove."]},
    ],
    "bank": ["\\(\\binom{n}{2}\\) derived.", "Handshake lemma.", "Inclusion–exclusion, 2, 3, 5 up to 100.", "Pascal’s identity.", "Fibonacci generating function.", "No two consecutive ones.", "Bipartite iff no odd cycle.", "Tree edge count.", "\\(\\sum k\\binom{n}{k}\\).", "One Putnam counting problem."],
    "oral": "Derive the binomial coefficient, prove the handshake lemma, and state inclusion–exclusion for three sets. No notes.",
}

ELECTIVES = [ABS, CX, MEA, PDE, NUM, COM]
