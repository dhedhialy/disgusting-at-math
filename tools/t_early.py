from bits import R, frame

AP = {
    "slug": "ap-precalc",
    "short": "AP Precalculus",
    "title": "AP Precalculus",
    "track": "Math",
    "needs": [],
    "what": """
<p>AP Precalculus is the last course in which a wrong algebraic move can still look like a small slip. After this, every later subject assumes you can rewrite an expression without changing its domain, read a graph as a set of pairs, and keep a parameter straight. The College Board course is a checklist of that fluency: polynomial and rational functions, exponential and logarithmic functions, trigonometric and polar functions, and functions involving parameters, vectors, and matrices at a light level. Passing the exam is not the target. The target is that none of those manipulations ever becomes the thing you are thinking about while you are trying to think about a proof or a derivative.</p>
<p>The hard part at this level is not a new theorem. It is domain, extraneous roots, and the difference between an identity and an equation that happens to hold at two points. A competition problem will hide a restriction inside a substitution. If you cannot say, out loud, what values were legal before you squared both sides, you are not done with this page.</p>
<p>You already sit in this course. Treat the class as a lower bound. The pages after this one will not reteach factoring, the unit circle, or logarithm rules. If one of those still costs you time, it is still this topic.</p>
""",
    "attack": [
        {
            "q": "<p>Solve \\(\\sqrt{x+3}+\\sqrt{x-1}=4\\). State the domain before you move anything, and prove there is only one real solution.</p>",
            "a": "<p>Domain: \\(x\\ge 1\\). Set \\(a=\\sqrt{x+3}\\), \\(b=\\sqrt{x-1}\\), so \\(a+b=4\\) and \\(a^2-b^2=4\\). Then \\((a-b)(a+b)=4\\), hence \\(a-b=1\\). Solving the linear pair gives \\(a=5/2\\), \\(b=3/2\\), so \\(x=1+(3/2)^2=13/4\\). The sum of two increasing square roots is strictly increasing on \\([1,\\infty)\\), so the solution is unique. Check: \\(\\sqrt{25/4}+\\sqrt{9/4}=5/2+3/2=4\\).</p>",
        },
        {
            "q": "<p>The polynomial \\(x^3-6x^2+11x-6\\) has three integer roots. Find them. Then say, in one sentence, why the rational root theorem means you did not miss a rational root.</p>",
            "a": "<p>Possible rational roots are the factors of 6: \\(\\pm 1,2,3,6\\). Evaluate: \\(p(1)=0\\), \\(p(2)=0\\), \\(p(3)=0\\). So \\(p(x)=(x-1)(x-2)(x-3)\\). Any rational root, written in lowest terms \\(p/q\\), must have \\(p\\) dividing the constant term and \\(q\\) dividing the leading coefficient. Here the leading coefficient is 1, so every rational root is an integer divisor of 6, and those were all tested.</p>",
        },
        {
            "q": "<p>Find the equation of the circle through \\((0,0)\\), \\((4,0)\\), and \\((0,2)\\).</p>",
            "a": "<p>Write \\(x^2+y^2+Dx+Ey+F=0\\). The origin forces \\(F=0\\). The point \\((4,0)\\) forces \\(16+4D=0\\), so \\(D=-4\\). The point \\((0,2)\\) forces \\(4+2E=0\\), so \\(E=-2\\). The circle is \\(x^2+y^2-4x-2y=0\\), center \\((2,1)\\), radius \\(\\sqrt{5}\\).</p>",
        },
    ],
    "core": [
        {
            "name": "Function",
            "statement": "A function \\(f:D\\to C\\) assigns to each \\(x\\in D\\) exactly one value \\(f(x)\\in C\\). The graph is the set of pairs. \\(f\\) is invertible precisely when it is one-to-one, and then \\((f^{-1}\\circ f)(x)=x\\) on the domain.",
            "proof": "<p>If \\(f(a)=f(b)\\) implies \\(a=b\\), each value in the image has one preimage, so the inverse relation is a function. The two composition identities are the definition of that inverse. If some value is hit twice, the inverse relation fails to be single-valued.</p>",
        },
        {
            "name": "Polynomials",
            "statement": "If \\(p\\) is a polynomial and \\(p(a)=0\\), then \\(x-a\\) divides \\(p(x)\\). A nonconstant polynomial of degree \\(n\\) has at most \\(n\\) roots unless it is identically zero. For \\(p(x)=a_n x^n+\\cdots+a_0\\) with integer coefficients, any rational root in lowest terms \\(r/s\\) has \\(r\\mid a_0\\) and \\(s\\mid a_n\\).",
            "proof": "<p>Divide by \\(x-a\\): \\(p(x)=(x-a)q(x)+r\\) with \\(r\\) constant, and \\(p(a)=r\\). The root bound is induction on degree after one linear factor is peeled off. The rational root theorem follows by clearing denominators and using that a prime dividing \\(s\\) cannot divide \\(r\\), hence cannot divide \\(a_0\\) after the equation is arranged; the symmetric argument handles \\(r\\) and \\(a_n\\).</p>",
        },
        {
            "name": "Exponentials and logarithms",
            "statement": "For \\(b>0\\), \\(b\\ne 1\\), and positive \\(x,y\\): \\(\\log_b(xy)=\\log_b x+\\log_b y\\), \\(\\log_b(x^k)=k\\log_b x\\), and \\(\\log_b x=\\ln x/\\ln b\\). The exponential \\(b^x\\) is the inverse of \\(\\log_b\\).",
            "proof": "<p>These are the exponent laws rewritten in inverse language. If \\(x=b^u\\) and \\(y=b^v\\), then \\(xy=b^{u+v}\\), which is the addition rule. Change of base is \\(\\ln x=\\ln(b^{\\log_b x})=\\log_b x\\cdot\\ln b\\).</p>",
        },
        {
            "name": "Unit circle",
            "statement": "On the circle \\(x^2+y^2=1\\), the point at angle \\(\\theta\\) from the positive \\(x\\)-axis is \\((\\cos\\theta,\\sin\\theta)\\). Thus \\(\\cos^2\\theta+\\sin^2\\theta=1\\). Addition: \\(\\sin(\\alpha+\\beta)=\\sin\\alpha\\cos\\beta+\\cos\\alpha\\sin\\beta\\) and \\(\\cos(\\alpha+\\beta)=\\cos\\alpha\\cos\\beta-\\sin\\alpha\\sin\\beta\\).",
            "proof": "<p>The identity is the circle equation at that point. One clean derivation of addition uses Euler’s formula \\(e^{i\\theta}=\\cos\\theta+i\\sin\\theta\\) and multiplies; a purely geometric derivation uses the distance formula between points at angles \\(\\alpha\\) and \\(-\\beta\\) on the unit circle and expands. Either is acceptable if you can reproduce it from a blank page.</p>",
        },
        {
            "name": "Triangles and sequences",
            "statement": "In a triangle, \\(a/\\sin A=b/\\sin B=2R\\) and \\(c^2=a^2+b^2-2ab\\cos C\\). An arithmetic sequence has constant difference; a geometric sequence has constant ratio. The partial sum of a finite geometric series with ratio \\(r\\ne 1\\) is \\(a(1-r^{n})/(1-r)\\).",
            "proof": "<p>Drop an altitude to prove the area formula \\(\\tfrac12 ab\\sin C\\), then equate two expressions for the area to get the law of sines; the law of cosines is the Pythagorean theorem applied to the two right triangles formed by an altitude. The geometric sum is the usual multiplication by \\(1-r\\).</p>",
        },
    ],
    "tiers": {
        "0": [R(
            "Khan Academy, AP Precalculus",
            "https://www.khanacademy.org/math/ap-precalculus",
            "Watch once, do not study from this. It is the official unit map, useful for seeing the shape of the course, and a bad place to spend your evenings.",
        )],
        "1": [R(
            "Stitz and Zeager, Precalculus, version 4−ε (15 January 2024)",
            "https://stitz-zeager.com/Precalculus4.pdf",
            "Free legal PDF from the authors. This is the book you work. OpenStax Precalculus 2e is the alternate if you want a second explanation of the same material: https://openstax.org/details/books/precalculus-2e",
        )],
        "2": [R(
            "Art of Problem Solving, Precalculus",
            "https://artofproblemsolving.com/store/book/precalculus",
            "The competition-flavored textbook. Paid. Use it after Stitz and Zeager, not instead of it. Alcumus at a hard rating is the daily drill: https://artofproblemsolving.com/alcumus",
            paid=True,
        )],
        "3": [R(
            "Po-Shen Loh, live contest index, and the AMC 12 / AIME archives",
            "https://live.poshenloh.com/",
            "Real MAA problems, sorted by concept, with difficulty ratings. The AoPS indexes, opened and checked in a browser, are https://artofproblemsolving.com/wiki/index.php/AMC_12_Problems_and_Solutions and https://artofproblemsolving.com/wiki/index.php/AIME_Problems_and_Solutions . Learn Anything has no precalculus page.",
        )],
    },
    "hardest": [
        {
            "label": "AMC 12, problems 21–25, any recent year, via Po-Shen Loh or the AoPS AMC 12 index",
            "url": "https://artofproblemsolving.com/wiki/index.php/AMC_12_Problems_and_Solutions",
            "why": "The last five are where a routine identity stops being enough and you have to invent a substitution or a counting model.",
        },
        {
            "label": "2023 AMC 12A Problem 21",
            "url": "https://artofproblemsolving.com/wiki/index.php/2023_AMC_12A_Problems/Problem_21",
            "why": "Graph distance on the icosahedron. The algebra is nothing; the hardness is organizing symmetry so you do not triple-count.",
        },
        {
            "label": "AIME I and II, problems 10–15, filtered to algebra, functions, and trigonometry",
            "url": "https://artofproblemsolving.com/wiki/index.php/AIME_Problems_and_Solutions",
            "why": "Integer answers punish a dropped domain or a sign error you would have survived on a homework sheet.",
        },
        {
            "label": "Po-Shen Loh, hardest band, topics: logarithms, polynomials, trigonometry",
            "url": "https://live.poshenloh.com/",
            "why": "Same MAA problems, already sorted, so you cannot pretend you are practicing logs while hiding in easy geometry.",
        },
        {
            "label": "Sharygin, Problems in Plane Geometry (Mir, 1988), the analytic-geometry slice",
            "url": "https://archive.org/details/SharyginProblemsInPlaneGeometryScienceForEveryone",
            "why": "Coordinate bashes that still require a geometric idea. Use this only for the coordinate and locus problems, not as a Euclidean detour.",
        },
    ],
    "gate": "<p>Pass: five consecutive AMC 12 problems numbered 21 through 25, chosen from five different years, all on functions, algebra, or trigonometry, solved cold. Full written solutions. No calculator unless the contest allowed one. Fail if any solution uses a step you cannot justify, including a squared equation whose extra roots you did not throw out.</p>",
    "svg": frame(
        '<circle cx="320" cy="190" r="110" fill="none" stroke="#fff" stroke-width="1.5"/>'
        '<line x1="320" y1="190" x2="430" y2="190" stroke="#fff"/>'
        '<line x1="320" y1="190" x2="375" y2="95" stroke="#fff"/>'
        '<line x1="430" y1="190" x2="375" y2="95" stroke="rgba(255,255,255,0.7)"/>'
        '<path d="M360 190 A40 40 0 0 0 345 158" fill="none" stroke="#fff"/>'
        '<text x="368" y="178" fill="#fff" font-size="14" font-family="Georgia, serif">θ</text>'
        '<text x="400" y="150" fill="#fff" font-size="14" font-family="Georgia, serif">1</text>'
        '<text x="300" y="220" fill="#bbb" font-size="13" font-family="Georgia, serif">cos θ</text>'
        '<text x="250" y="140" fill="#bbb" font-size="13" font-family="Georgia, serif">sin θ</text>',
        label="Unit circle with a reference triangle",
    ),
    "caption": "The unit circle is a definition, not a mnemonic. Cosine and sine are coordinates.",
    "batches": [
        {"name": "Cleanups", "items": [
            "State the domain of \\(\\log_2(x^2-1)\\) and of \\(\\sqrt{4-x}+\\sqrt{x+1}\\).",
            "Solve \\(2^{x}+2^{x+1}+2^{x+2}=7\\cdot 2^{x}\\) and explain the cancellation.",
            "Expand \\(\\sin(2\\theta)\\) and \\(\\cos(2\\theta)\\) from the addition formulas. Do not quote them from memory first.",
            "Find the inverse of \\(f(x)=(2x-1)/(x+3)\\) and its domain.",
            "Sum \\(3+6+12+\\cdots+3\\cdot 2^{7}\\).",
        ]},
        {"name": "Restrictions", "items": [
            "Solve \\(\\sqrt{x+5}=x-1\\) and list every extraneous root you created.",
            "Solve \\(\\log_2(x-1)+\\log_2(x+1)=3\\).",
            "For which \\(k\\) does \\(x^2-2x+k=0\\) have two distinct real roots? Draw the condition.",
            "A rational function has vertical asymptotes \\(x=1\\) and \\(x=-2\\) and a horizontal asymptote \\(y=2\\). Write one such function and one that fails the horizontal condition.",
            "Prove that \\(\\log_b a\\cdot\\log_a b=1\\) for legal bases and arguments.",
        ]},
        {"name": "Graphs as sets", "items": [
            "Sketch \\(y=2\\sin(x-\\pi/3)+1\\) by listing the transformations in the order you apply them.",
            "How many solutions does \\(\\sin x=x/10\\) have? Argue from graphs, no calculator.",
            "Find the range of \\(f(x)=(x^2+1)/(x^2+2)\\).",
            "Parameterize the line through \\((1,2)\\) and \\((4,-1)\\). Where does it meet the circle \\(x^2+y^2=1\\)?",
            "Show that \\(x+1/x\\ge 2\\) for \\(x>0\\), with equality only at \\(x=1\\).",
        ]},
        {"name": "Contest shape", "items": [
            "Find all real \\(x\\) with \\(x^2+x+1\\) dividing \\(x^3-1\\), and factor the quotient.",
            "Solve \\(\\sin\\theta+\\cos\\theta=1\\) exactly, on \\([0,2\\pi)\\).",
            "The polynomial \\(x^4+4\\) factors over the reals. Find the factorization.",
            "A geometric sequence of positive terms has second term 6 and fourth term 24. Find the first term. How many answers?",
            "From Po-Shen Loh, do five problems rated in the top band under polynomials or logs. Write them up.",
        ]},
        {"name": "Ceiling", "items": [
            "Five AMC 12 problems numbered 15–25, mixed years, written in full.",
            "Three AIME problems numbered 8–15 on algebra or trig.",
            "Ten Sharygin problems that are solved by coordinates, not by a pure Euclidean theorem you have not proved.",
            "Rebuild the unit-circle addition formula without looking.",
            "One Alcumus session at the hardest available setting, topic of your weakest function family. Keep the written work, not the score.",
        ]},
    ],
    "bank": [
        "\\(\\sqrt{x+3}+\\sqrt{x-1}=4\\), with the uniqueness argument.",
        "Rational roots of \\(x^3-6x^2+11x-6\\), and the theorem that closed the search.",
        "Circle through \\((0,0)\\), \\((4,0)\\), \\((0,2)\\).",
        "Domain of \\(\\log_2(x^2-1)\\).",
        "\\(\\sin\\theta+\\cos\\theta=1\\) on one full turn.",
        "Factor \\(x^4+4\\) over the reals.",
        "Range of \\((x^2+1)/(x^2+2)\\).",
        "2023 AMC 12A #21, written, not watched.",
        "One AIME #12 on logs or trig, from the archive.",
        "Law of cosines derived from an altitude, not quoted.",
    ],
    "oral": "From a blank page, define a function, state the rational root theorem, derive \\(\\sin^2+\\cos^2=1\\) from the circle, and solve one logarithm equation while naming the domain out loud.",
}

HARD = {
    "slug": "precalc-hardening",
    "short": "Precalc, hard",
    "title": "Precalculus, competition-hard",
    "track": "Math",
    "needs": ["ap-precalc"],
    "what": """
<p>This page is the same functions, trigonometry, and analytic geometry, pushed until the standard method is not enough. Competition precalculus adds complex numbers as a working tool, polynomials as objects with structure rather than expressions to factor, functional equations, inequalities with equality cases, and trigonometry used as algebra on the circle. The College Board will not ask most of this. Later analysis and olympiad calculus will assume you already paid for it.</p>
<p>The failure mode is collecting tricks. A trick that you cannot derive is a fact you will misapply the first time the problem is rotated. Every identity on this page has to be something you can rebuild: De Moivre from multiplication of complex numbers, AM-GM from a square, the factor theorem from division. Gelfand’s short books were written exactly in this spirit. The free scans of them are access-restricted on the Internet Archive, so they are not linked here as downloads. Use the sources below, which are open.</p>
<p>When a problem splits into cases, write the cases down before you compute. Most lost points at this level are a case that was never named.</p>
""",
    "attack": [
        {
            "q": "<p>Solve \\(\\log_2 x+\\log_x 2=5/2\\).</p>",
            "a": "<p>Let \\(t=\\log_2 x\\), so \\(t\\ne 0\\) and \\(x>0\\), \\(x\\ne 1\\). Then \\(t+1/t=5/2\\). Multiply by \\(2t\\): \\(2t^2-5t+2=0\\), \\((2t-1)(t-2)=0\\). So \\(t=1/2\\) or \\(t=2\\), hence \\(x=\\sqrt{2}\\) or \\(x=4\\). Both check.</p>",
        },
        {
            "q": "<p>How many real roots does \\(x^5-5x+1=0\\) have? Do not approximate them. Count them.</p>",
            "a": "<p>\\(f'(x)=5x^4-5=5(x^4-1)\\), so the only real critical points are \\(x=\\pm 1\\). \\(f(-1)=5>0\\) is a local max and \\(f(1)=-3<0\\) is a local min, because \\(f''\\) or the first-derivative sign chart says so: \\(f'\\) is negative on \\((-1,1)\\) and positive outside. \\(f(-2)<0\\), \\(f(2)>0\\). So there is one root in \\((-\\infty,-1)\\), one in \\((-1,1)\\), and one in \\((1,\\infty)\\). Three real roots, and therefore two nonreal complex roots.</p>",
        },
        {
            "q": "<p>Prove that for positive \\(a,b\\), \\((a+b)/2\\ge\\sqrt{ab}\\), and characterize equality.</p>",
            "a": "<p>\\((\\sqrt{a}-\\sqrt{b})^2\\ge 0\\) expands to \\(a+b\\ge 2\\sqrt{ab}\\). Equality holds exactly when \\(\\sqrt{a}=\\sqrt{b}\\), that is \\(a=b\\).</p>",
        },
    ],
    "core": [
        {
            "name": "Complex arithmetic",
            "statement": "\\(i^2=-1\\). In polar form, \\(re^{i\\theta}\\cdot \\rho e^{i\\phi}=r\\rho e^{i(\\theta+\\phi)}\\). De Moivre: \\((\\cos\\theta+i\\sin\\theta)^n=\\cos(n\\theta)+i\\sin(n\\theta)\\). Nonreal roots of real polynomials come in conjugate pairs.",
            "proof": "<p>Multiplication adds angles because that is how \\(e^{i\\theta}=\\cos\\theta+i\\sin\\theta\\) multiplies, or by expanding the sine and cosine addition formulas inductively. The conjugate-root theorem is the observation that conjugating \\(p(z)=0\\) with real coefficients yields \\(p(\\bar z)=0\\).</p>",
        },
        {
            "name": "Polynomial structure",
            "statement": "Over \\(\\mathbb{C}\\), a degree-\\(n\\) polynomial has exactly \\(n\\) roots, counted with multiplicity. If the coefficients are real and \\(a+bi\\) is a root, so is \\(a-bi\\). A symmetric polynomial in the roots can be written in the elementary symmetric sums, which are the coefficients up to sign.",
            "proof": "<p>The existence half is the fundamental theorem of algebra; you are not asked to prove it here, only to use the counting consequence after unique factorization in \\(\\mathbb{C}[x]\\), which you may take as known once the theorem is stated. Vieta is equating coefficients in \\(a_n\\prod(x-r_i)\\).</p>",
        },
        {
            "name": "Inequalities",
            "statement": "AM-GM for \\(n\\) positive numbers, Cauchy–Schwarz in the form \\((a_1^2+\\cdots+a_n^2)(b_1^2+\\cdots+b_n^2)\\ge(a_1b_1+\\cdots+a_nb_n)^2\\), and the trivial bound from squares: a sum of squares is nonnegative.",
            "proof": "<p>The \\(n=2\\) AM-GM is the attack above. Cauchy–Schwarz is the discriminant of \\(\\sum(a_i t-b_i)^2\\ge 0\\) being nonpositive, or the expansion of \\(\\sum_{i<j}(a_ib_j-a_jb_i)^2\\ge 0\\).</p>",
        },
        {
            "name": "Trigonometric form",
            "statement": "The linear combination \\(a\\cos\\theta+b\\sin\\theta\\) equals \\(R\\cos(\\theta-\\alpha)\\) with \\(R=\\sqrt{a^2+b^2}\\) and \\(\\cos\\alpha=a/R\\), \\(\\sin\\alpha=b/R\\). Product-to-sum identities are the addition formulas solved for products.",
            "proof": "<p>Divide by \\(R\\) and match the addition formula for cosine. Product-to-sum is the sum and difference of \\(\\cos(\\alpha+\\beta)\\) and \\(\\cos(\\alpha-\\beta)\\), rearranged.</p>",
        },
        {
            "name": "Conics",
            "statement": "A conic is a curve \\(Ax^2+Bxy+Cy^2+Dx+Ey+F=0\\). After rotation to kill the \\(xy\\) term and translation to complete the square, the type is ellipse, parabola, or hyperbola according to the discriminant \\(B^2-4AC\\).",
            "proof": "<p>The rotation by an angle satisfying \\(\\cot 2\\theta=(A-C)/B\\) removes \\(xy\\). Completing the square is algebra. The discriminant is invariant under rotation, which is why it classifies the conic before you compute the angle.</p>",
        },
    ],
    "tiers": {
        "0": [R(
            "Paul’s Online Math Notes, Algebra",
            "https://tutorial.math.lamar.edu/Classes/Alg/Alg.aspx",
            "Read once, do not study from this. Skim the section list so you can see which algebra moves you still hesitate on. Then close it and go to the book.",
        )],
        "1": [R(
            "Stitz and Zeager, the complex, trig, and conic chapters you rushed",
            "https://stitz-zeager.com/Precalculus4.pdf",
            "Same free book as the previous page. The hardening is in which exercises you choose: every proof-style exercise, every complex-number section, every inequality.",
        )],
        "2": [R(
            "AoPS Precalculus, plus Alcumus on hard",
            "https://artofproblemsolving.com/store/book/precalculus",
            "Paid textbook aimed at contests. Paired with Alcumus: https://artofproblemsolving.com/alcumus . Better than another college precalculus book because the problems are the point.",
            paid=True,
        )],
        "3": [R(
            "AIME problems and Sharygin’s plane geometry",
            "https://artofproblemsolving.com/wiki/index.php/AIME_Problems_and_Solutions",
            "AIME is the ceiling for precalculus technique. Sharygin, for the coordinate slice only: https://archive.org/details/SharyginProblemsInPlaneGeometryScienceForEveryone . Gelfand’s problem books are the right spirit; legal free downloads were not verified, so they are not linked.",
        )],
    },
    "hardest": [
        {
            "label": "AIME problems 10–15 on complex numbers, trigonometry, polynomials, and inequalities",
            "url": "https://artofproblemsolving.com/wiki/index.php/AIME_Problems_and_Solutions",
            "why": "The answer is an integer from 000 to 999, which means a structural idea, not a decimal hunt.",
        },
        {
            "label": "Po-Shen Loh, top difficulty, complex numbers and trig",
            "url": "https://live.poshenloh.com/",
            "why": "You can filter to the concept and stop pretending a random AMC #8 is practice.",
        },
        {
            "label": "AMC 12 #21–25, several years, complex or trig tags",
            "url": "https://artofproblemsolving.com/wiki/index.php/AMC_12_Problems_and_Solutions",
            "why": "Timed pressure on identities you were supposed to have made automatic.",
        },
        {
            "label": "Sharygin, coordinate and locus problems",
            "url": "https://archive.org/details/SharyginProblemsInPlaneGeometryScienceForEveryone",
            "why": "The diagram lies. The algebra tells the truth only if you chose coordinates that respect the symmetry.",
        },
        {
            "label": "Alcumus, hardest setting, precalculus topics",
            "url": "https://artofproblemsolving.com/alcumus",
            "why": "The generator will keep serving the topic you miss. That is the opposite of a highlight reel.",
        },
    ],
    "gate": "<p>Pass: eight AIME problems, numbered 8 or higher, from at least four different years, covering at least three of complex numbers, trigonometry, polynomials, and inequalities. Full writeups. You may use the contest’s answer format as a checksum only after the solution is written. Fail if you needed a solution video to find the idea.</p>",
    "svg": frame(
        '<line x1="40" y1="180" x2="600" y2="180" stroke="#fff"/>'
        '<line x1="320" y1="30" x2="320" y2="330" stroke="#fff"/>'
        '<path d="M80 250 C 180 280, 240 40, 320 180 S 480 80, 580 140" fill="none" stroke="#fff" stroke-width="1.5"/>'
        '<circle cx="168" cy="214" r="4" fill="#fff"/>'
        '<circle cx="320" cy="180" r="4" fill="#fff"/>'
        '<circle cx="470" cy="128" r="4" fill="#fff"/>'
        '<text x="150" y="206" fill="#bbb" font-size="13" font-family="Georgia, serif">local max</text>'
        '<text x="430" y="118" fill="#bbb" font-size="13" font-family="Georgia, serif">local min</text>',
        label="A quintic crossing the axis three times",
    ),
    "caption": "Critical points tell you how many times a polynomial can cross the axis. They do not find the roots.",
    "batches": [
        {"name": "Complex", "items": [
            "Write \\((1+i)^{10}\\) in the form \\(a+bi\\) using polar form.",
            "Find all cube roots of \\(8i\\).",
            "Show that if \\(z\\bar z=1\\) and \\(z\\ne 1\\), then \\((z+1)/(z-1)\\) is purely imaginary. State the exception carefully.",
            "Factor \\(x^2+1\\) over the complexes and over the reals.",
            "Prove the conjugate root theorem for a quadratic, by hand.",
        ]},
        {"name": "Inequalities", "items": [
            "Prove Cauchy–Schwarz for two pairs of real numbers.",
            "For positive \\(x\\), minimize \\(x+4/x\\).",
            "Show \\(|a+b|\\le |a|+|b|\\) from squares or from geometry. Equality case.",
            "Solve \\(|x-1|+|x+2|<6\\).",
            "Prove \\(a^2+b^2+c^2\\ge ab+bc+ca\\).",
        ]},
        {"name": "Trigonometry as algebra", "items": [
            "Write \\(3\\cos\\theta+4\\sin\\theta\\) as a single cosine and find its maximum.",
            "Solve \\(\\sin\\theta\\cos\\theta=1/4\\) exactly.",
            "Prove \\(\\tan(\\alpha+\\beta)\\) from sine and cosine addition, and name where it is undefined.",
            "Find \\(\\sum_{k=1}^{n}\\sin k\\theta\\) by taking the imaginary part of a geometric series.",
            "A triangle has sides 2, 3, 4. Find the cosine of the angle opposite 4. Is the angle acute?",
        ]},
        {"name": "Polynomials and functions", "items": [
            "How many real roots does \\(x^5-5x+1\\) have? Write the derivative argument.",
            "Solve \\(f(x)+f(1/x)=x+1/x\\) given that you may assume a form, then check it. Better: find all functions \\(\\mathbb{R}\\setminus\\{0\\}\\to\\mathbb{R}\\) of the form \\(ax+b/x\\) that work, and say what you did not classify.",
            "Vieta: the roots of \\(x^3-6x^2+11x-6=0\\) are 1, 2, 3. Compute the sum of pairwise products without multiplying them, from the coefficients.",
            "Show that \\(x^2+x+1\\) divides \\(x^3-1\\) and also \\(x^6+x^3+1\\) or decide which of those is true.",
            "A monic cubic with real coefficients has roots \\(2\\), \\(i\\), and one more. Find it.",
        ]},
        {"name": "Ceiling", "items": [
            "Four AIME problems, number at least 10.",
            "Four AMC 12 problems, number at least 20, on this page’s topics.",
            "Five Sharygin coordinate problems.",
            "Derive De Moivre by induction from the addition formulas.",
            "Ten Alcumus problems at the top setting. Keep the writeups that took more than ten minutes.",
        ]},
    ],
    "bank": [
        "\\(\\log_2 x+\\log_x 2=5/2\\).",
        "Root count for \\(x^5-5x+1\\).",
        "AM-GM for two numbers, equality case.",
        "\\((1+i)^{10}\\).",
        "Cube roots of \\(8i\\).",
        "Maximum of \\(3\\cos\\theta+4\\sin\\theta\\).",
        "Cauchy–Schwarz for \\(n=2\\).",
        "Conjugate root theorem, quadratic case.",
        "One AIME #13 on complex numbers or trig.",
        "Sum of \\(\\sin k\\theta\\) via geometric series.",
    ],
    "oral": "Explain polar form, prove AM-GM for two numbers, and count the real roots of a quintic using only the derivative sign chart. No notes.",
}
