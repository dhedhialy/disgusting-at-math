# Answer keys and work requirements for the three opening attacks on each topic.
# "parts": every group must match the answer line (any string inside the group).
# "need": every group must match the written work. "hint" is what we say is missing.

GRADES = [
    # ap-precalc
    {"slug": "ap-precalc", "n": 1,
     "parts": [["13/4", "3.25", "3.250"]],
     "need": [
         {"hint": "state the domain", "any": ["domain", "x>=1", "x≥1"]},
         {"hint": "explain why there is only one solution", "any": ["unique", "only one", "one solution", "increasing", "injective"]},
     ]},
    {"slug": "ap-precalc", "n": 2,
     "parts": [["1"], ["2"], ["3"]],
     "need": [
         {"hint": "name the rational root theorem", "any": ["rational root", "possible rational", "divisors", "divides"]},
     ]},
    {"slug": "ap-precalc", "n": 3,
     "parts": [["x^2+y^2-4x-2y=0", "(x-2)^2+(y-1)^2=5", "x^2+y^2-4x-2y"]],
     "need": [
         {"hint": "use all three points", "any": ["(0,0)", "origin", "(4,0)", "(0,2)", "three points", "plug"]},
     ]},
    # precalc-hardening
    {"slug": "precalc-hardening", "n": 1,
     "parts": [["4"], ["sqrt(2)", "2^(1/2)", "√2"]],
     "need": [
         {"hint": "use a substitution or the reciprocal relation", "any": ["substitut", "let", "1/t", "reciprocal"]},
     ]},
    {"slug": "precalc-hardening", "n": 2,
     "parts": [["3"]],
     "need": [
         {"hint": "use the derivative or a sign chart", "any": ["derivative", "f'", "critical", "local min", "sign"]},
     ]},
    {"slug": "precalc-hardening", "n": 3,
     "parts": [["a=b", "a = b", "equal"]],
     "need": [
         {"hint": "compare a square or a difference of roots", "any": ["square", "(sqrt", "difference", "am-gm", "arithmetic"]},
     ]},
    # proof-logic
    {"slug": "proof-logic", "n": 1,
     "parts": [["no", "not rational", "irrational"]],
     "need": [
         {"hint": "use a contradiction with a fraction in lowest terms", "any": ["contradict", "lowest", "coprime", "even"]},
     ]},
    {"slug": "proof-logic", "n": 2,
     "parts": [["n(n+1)/2", "n(n+1)/2"]],
     "need": [
         {"hint": "check the base case and the inductive step", "any": ["base", "induction", "inductive"]},
     ]},
    {"slug": "proof-logic", "n": 3,
     "parts": [["n+1", "n |-> n+1", "successor"]],
     "need": [
         {"hint": "say it is injective and not surjective", "any": ["injective", "one-to-one", "not surjective", "misses"]},
     ]},
    # calc-1
    {"slug": "calc-1", "n": 1,
     "parts": [["3x^2", "3x^2"]],
     "need": [
         {"hint": "start from the difference quotient", "any": ["limit", "difference quotient", "h->0", "h→0", "binomial"]},
     ]},
    {"slug": "calc-1", "n": 2,
     "parts": [["(1,3)", "1<t<3", "(1, 3)"]],
     "need": [
         {"hint": "use the velocity, the derivative of s", "any": ["velocity", "derivative", "s'", "factor"]},
     ]},
    {"slug": "calc-1", "n": 3,
     "parts": [["0"]],
     "need": [
         {"hint": "use the definition, not a rule name alone", "any": ["difference", "limit", "f(a+h)", "constant"]},
     ]},
    # linear-algebra
    {"slug": "linear-algebra", "n": 1,
     "parts": [["no", "not a basis"]],
     "need": [
         {"hint": "say they are dependent or scalar multiples", "any": ["dependent", "multiple", "parallel", "not independent", "span"]},
     ]},
    {"slug": "linear-algebra", "n": 2,
     "parts": [["x+y=1", "the line", "infinitely many"]],
     "need": [
         {"hint": "say the solution set is infinite or has a free variable", "any": ["infinite", "free", "line", "dependent"]},
     ]},
    {"slug": "linear-algebra", "n": 3,
     "parts": [["-2"]],
     "need": [
         {"hint": "say what the sign means for orientation or area", "any": ["orientation", "area", "revers", "sign", "clockwise"]},
     ]},
    # calc-3
    {"slug": "calc-3", "n": 1,
     "parts": [["(2,2)", "<2,2>", "2i+2j"]],
     "need": [
         {"hint": "say the gradient points toward increase", "any": ["increase", "steepest", "ascent", "uphill"]},
     ]},
    {"slug": "calc-3", "n": 2,
     "parts": [["2x"]],
     "need": [
         {"hint": "compute both mixed partials", "any": ["mixed", "f_xy", "partial", "clairaut"]},
     ]},
    {"slug": "calc-3", "n": 3,
     "parts": [["0"]],
     "need": [
         {"hint": "use the fundamental theorem or path independence", "any": ["fundamental", "path independent", "telescope", "gradient"]},
     ]},
    # ode
    {"slug": "ode", "n": 1,
     "parts": [["e^t", "exp(t)", "e^{t}"]],
     "need": [
         {"hint": "use the initial condition", "any": ["initial", "y(0)", "separat", "constant"]},
     ]},
    {"slug": "ode", "n": 2,
     "parts": [["ce^{-t}", "c*e^{-t}", "c exp(-t)", "ae^{-t}"]],
     "need": [
         {"hint": "solve the equation, constant included", "any": ["integrat", "separat", "exponential", "characteristic"]},
     ]},
    {"slug": "ode", "n": 3,
     "parts": [["0"], ["1"], ["unstable"], ["stable"]],
     "need": [
         {"hint": "test the sign of y' on each side", "any": ["sign", "phase", "stable", "unstable"]},
     ]},
    # real-analysis
    {"slug": "real-analysis", "n": 1,
     "parts": [["alpha^2=2", "α^2=2", "sqrt(2)"]],
     "need": [
         {"hint": "use the least upper bound", "any": ["supremum", "least upper", "upper bound", "completeness"]},
     ]},
    {"slug": "real-analysis", "n": 2,
     "parts": [["cauchy"]],
     "need": [
         {"hint": "use the triangle inequality or an epsilon split", "any": ["triangle", "epsilon", "ε", "|a_n-a_m|"]},
     ]},
    {"slug": "real-analysis", "n": 3,
     "parts": [["not uniformly", "not uniform"]],
     "need": [
         {"hint": "use two sequences that get close while the function values do not", "any": ["1/n", "sequence", "epsilon", "δ", "delta"]},
     ]},
    # topology
    {"slug": "topology", "n": 1,
     "parts": [["[0,1]"], ["not"]],
     "need": [
         {"hint": "give an open cover of (0,1) with no finite subcover", "any": ["cover", "subcover", "heine", "1/n"]},
     ]},
    {"slug": "topology", "n": 2,
     "parts": [["no", "not connected", "disconnected"]],
     "need": [
         {"hint": "split the rationals into two nonempty separated sets", "any": ["sqrt(2)", "√2", "separated", "clopen", "two sets"]},
     ]},
    {"slug": "topology", "n": 3,
     "parts": [["connected"]],
     "need": [
         {"hint": "argue by preimages of a separation", "any": ["preimage", "separation", "continuous"]},
     ]},
    # abstract-algebra
    {"slug": "abstract-algebra", "n": 1,
     "parts": [["yes"], ["1"], ["-1/2", "-0.5"]],
     "need": [
         {"hint": "check inverses and say why zero is out", "any": ["inverse", "zero", "closure", "identity"]},
     ]},
    {"slug": "abstract-algebra", "n": 2,
     "parts": [["(12)"], ["(123)", "a3", "alternating"]],
     "need": [
         {"hint": "name a subgroup of order 2 and one of order 3", "any": ["order 2", "order 3", "subgroup", "cycle"]},
     ]},
    {"slug": "abstract-algebra", "n": 3,
     "parts": [["unique"]],
     "need": [
         {"hint": "compare two identities by multiplying them", "any": ["e=ef", "ef=f", "both identities", "e=f"]},
     ]},
    # complex-analysis
    {"slug": "complex-analysis", "n": 1,
     "parts": [["u_x=v_y", "hold"]],
     "need": [
         {"hint": "compute the partials of u and v for z^2", "any": ["u_x", "partial", "2x", "cauchy"]},
     ]},
    {"slug": "complex-analysis", "n": 2,
     "parts": [["2pii", "2πi", "2\\pi i"]],
     "need": [
         {"hint": "parametrize the circle", "any": ["parametr", "e^{i", "theta", "θ"]},
     ]},
    {"slug": "complex-analysis", "n": 3,
     "parts": [["fail", "not holomorphic", "u_x"]],
     "need": [
         {"hint": "compare u_x and v_y", "any": ["u_x", "v_y", "conjugate", "not equal"]},
     ]},
    # measure-theory
    {"slug": "measure-theory", "n": 1,
     "parts": [["0", "zero"]],
     "need": [
         {"hint": "cover the points by intervals of total length epsilon", "any": ["epsilon", "ε", "cover", "2^n", "2^{-n}"]},
     ]},
    {"slug": "measure-theory", "n": 2,
     "parts": [["1"], ["0"]],
     "need": [
         {"hint": "compare the limit of the integrals with the integral of the limit", "any": ["pointwise", "integral", "spike", "limit"]},
     ]},
    {"slug": "measure-theory", "n": 3,
     "parts": [["dominated", "integrable"]],
     "need": [
         {"hint": "name an integrable dominant g", "any": ["dominant", "|f_n|", "integrable", "almost everywhere"]},
     ]},
    # pde
    {"slug": "pde", "n": 1,
     "parts": [["e^{-t}sinx", "e^{-t}\\sin x", "exp(-t)sinx"]],
     "need": [
         {"hint": "use the boundary conditions", "any": ["boundary", "separat", "sin x", "lambda", "λ"]},
     ]},
    {"slug": "pde", "n": 2,
     "parts": [["x-ct", "x+ct"], ["dalembert", "d'alembert", "1/2"]],
     "need": [
         {"hint": "name the interval the point depends on", "any": ["domain of dependence", "x-ct", "interval", "characteristic"]},
     ]},
    {"slug": "pde", "n": 3,
     "parts": [["boundary", "parabolic", "initial"]],
     "need": [
         {"hint": "say an interior hot spot cannot be born later", "any": ["interior", "maximum", "boundary", "constant"]},
     ]},
    # number-theory
    {"slug": "number-theory", "n": 1,
     "parts": [["infinitely many", "infinite"]],
     "need": [
         {"hint": "build a number the listed primes do not divide", "any": ["factorial", "n!+1", "product", "+1", "divides"]},
     ]},
    {"slug": "number-theory", "n": 2,
     "parts": [["7", "x=7"]],
     "need": [
         {"hint": "find the inverse of 3 mod 10", "any": ["inverse", "21", "7", "mod"]},
     ]},
    {"slug": "number-theory", "n": 3,
     "parts": [["1"]],
     "need": [
         {"hint": "use Fermat or compute the power", "any": ["fermat", "10", "1024", "p-1"]},
     ]},
    # combinatorics
    {"slug": "combinatorics", "n": 1,
     "parts": [["n(n-1)/2", "\\binom{n}{2}"]],
     "need": [
         {"hint": "count ordered pairs and divide by 2", "any": ["ordered", "divide", "/2", "twice"]},
     ]},
    {"slug": "combinatorics", "n": 2,
     "parts": [["2e", "2|e|", "twice the number of edges", "2m"]],
     "need": [
         {"hint": "count each edge twice, once at each end", "any": ["twice", "both ends", "incident", "handshak"]},
     ]},
    {"slug": "combinatorics", "n": 3,
     "parts": [["74"]],
     "need": [
         {"hint": "use inclusion-exclusion", "any": ["inclusion", "floor", "intersect"]},
     ]},
    # mechanics
    {"slug": "mechanics", "n": 1,
     "parts": [["gsin", "g\\sin", "g sin"]],
     "need": [
         {"hint": "resolve gravity along the incline", "any": ["component", "newton", "free body", "mg", "along"]},
     ]},
    {"slug": "mechanics", "n": 2,
     "parts": [["(m1-m2)g/(m1+m2)", "(m_1-m_2)g/(m_1+m_2)"]],
     "need": [
         {"hint": "use the tension and Newton's second law on each mass", "any": ["tension", "newton", "second"]},
     ]},
    {"slug": "mechanics", "n": 3,
     "parts": [["45"], ["parabola"]],
     "need": [
         {"hint": "eliminate time or maximize the range", "any": ["parabola", "eliminate", "sin(2", "45"]},
     ]},
    # em
    {"slug": "em", "n": 1,
     "parts": [["q/(4\\pi\\epsilon_0 r^2)", "kq/r^2", "1/(4\\pi\\epsilon_0)"]],
     "need": [
         {"hint": "use symmetry and a spherical surface", "any": ["gauss", "flux", "sphere", "symmetry"]},
     ]},
    {"slug": "em", "n": 2,
     "parts": [["lambda/(2piepsilon0r)", "\\lambda/(2\\pi\\epsilon_0 r)", "2klambda/r"]],
     "need": [
         {"hint": "use a cylinder", "any": ["cylinder", "gauss", "flux"]},
     ]},
    {"slug": "em", "n": 3,
     "parts": [["0", "zero"]],
     "need": [
         {"hint": "say charges would still be moving otherwise", "any": ["electrostatic", "move", "accelerate", "equilibrium", "force"]},
     ]},
    # waves-optics
    {"slug": "waves-optics", "n": 1,
     "parts": [["omega/k", "\\omega/k"], ["positive"]],
     "need": [
         {"hint": "track a crest of constant phase", "any": ["phase", "crest", "kx-", "speed"]},
     ]},
    {"slug": "waves-optics", "n": 2,
     "parts": [["dsin", "d\\sin", "m\\lambda", "mlambda"]],
     "need": [
         {"hint": "compare the path difference", "any": ["path", "constructive", "fringe"]},
     ]},
    {"slug": "waves-optics", "n": 3,
     "parts": [["sin(kx)=0", "npi/k", "x=n\\pi/k"]],
     "need": [
         {"hint": "set the spatial factor to zero", "any": ["node", "sin", "zero"]},
     ]},
    # modern-physics
    {"slug": "modern-physics", "n": 1,
     "parts": [["frequency", "photon", "threshold"]],
     "need": [
         {"hint": "compare photon energy with the work function", "any": ["work function", "hf", "photon", "frequency"]},
     ]},
    {"slug": "modern-physics", "n": 2,
     "parts": [["h/p", "\\lambda=h/p"]],
     "need": [
         {"hint": "name wavelength and momentum", "any": ["wavelength", "momentum", "de broglie"]},
     ]},
    {"slug": "modern-physics", "n": 3,
     "parts": [["n^2", "n^{2}"]],
     "need": [
         {"hint": "fit a whole number of half-waves in the well", "any": ["boundary", "half", "k=n", "sine", "standing"]},
     ]},
]
