from bits import R, frame

MECH = {
    "slug": "mechanics",
    "short": "Mechanics",
    "title": "Mechanics",
    "track": "Physics",
    "needs": ["ap-precalc", "calc-1"],
    "what": """
<p>Newtonian mechanics is the claim that a force changes momentum, together with the models of the forces you actually meet: gravity near the earth, gravity between point masses, springs, and friction. The subject becomes mathematics the moment you write \\(\\mathbf F=d\\mathbf p/dt\\) as a differential equation. Energy and momentum are not extra laws. They are the consequences of Newton’s laws when the forces are what they are: momentum is conserved when the total external force vanishes, and mechanical energy is conserved when the forces are gradients of a potential.</p>
<p>OpenStax University Physics Volume 1 is free, calculus-based, and the working book. Halliday, Resnick, and Walker is the traditional paid text; no edition was verified. Kleppner and Kolenkow, and Morin’s Introduction to Classical Mechanics (ISBN 978-0-521-87622-3), are the harder books. Morin’s ISBN was confirmed in the Open Library catalog. MIT 8.01 is the course with exams. Irodov is the ceiling. Feynman is the preview, and Feynman is a bad place to learn to solve problems.</p>
<p>A free-body diagram that does not name the body is a decoration. Draw the body, then the arrows that act on it, then the equation.</p>
""",
    "attack": [
        {"q": "<p>A block slides down a frictionless incline of angle \\(\\theta\\). Find its acceleration along the incline.</p>",
         "a": "<p>The forces are gravity and the normal. Along the incline, the component of weight is \\(mg\\sin\\theta\\) and the normal does no work along that direction. Newton’s second law gives \\(a=g\\sin\\theta\\) down the incline.</p>"},
        {"q": "<p>Atwood’s machine: masses \\(m_1>m_2\\) over a massless frictionless pulley. Find the acceleration.</p>",
         "a": "<p>Equations: \\(m_1 g-T=m_1 a\\), \\(T-m_2 g=m_2 a\\). Add them: \\((m_1-m_2)g=(m_1+m_2)a\\), so \\(a=(m_1-m_2)g/(m_1+m_2)\\).</p>"},
        {"q": "<p>A projectile is launched with speed \\(v\\) at angle \\(\\theta\\) from level ground. Show the trajectory is a parabola and that the range is maximized at \\(45^\\circ\\).</p>",
         "a": "<p>\\(x=v\\cos\\theta\\, t\\), \\(y=v\\sin\\theta\\, t-\\tfrac12 gt^2\\). Eliminate \\(t\\): \\(y=x\\tan\\theta-gx^2/(2v^2\\cos^2\\theta)\\), a parabola. Range is the positive \\(x\\) when \\(y=0\\): \\(R=v^2\\sin 2\\theta/g\\), maximized when \\(\\sin 2\\theta=1\\), so \\(\\theta=45^\\circ\\).</p>"},
    ],
    "core": [
        {"name": "Newton", "statement": "In an inertial frame, \\(\\mathbf F_{\\mathrm{net}}=d\\mathbf p/dt\\). For constant mass this is \\(m\\mathbf a\\). Superposition: the net force is the vector sum. The third law, in the form of equal-and-opposite central forces, is what makes internal forces cancel in the momentum balance of a system.",
         "proof": "<p>These are the laws, not theorems. The derived statement you must prove is the momentum theorem: the total external force equals the derivative of total momentum, once internal forces cancel by the third law.</p>"},
        {"name": "Energy", "statement": "The work–energy theorem: the work of the net force equals the change in kinetic energy. If every force is conservative, mechanical energy is conserved. Gravity near Earth has potential \\(mgy\\). A spring has potential \\(\\tfrac12 kx^2\\).",
         "proof": "<p>Work–energy is the chain rule: \\(\\mathbf F\\cdot\\mathbf v=m\\mathbf a\\cdot\\mathbf v=\\frac{d}{dt}(\\tfrac12 mv^2)\\). A conservative force is minus the gradient of a potential, so its work is minus the change in potential.</p>"},
        {"name": "Momentum and rotation", "statement": "External impulse equals change in momentum. For a rigid body about a fixed axis, \\(\\tau=I\\alpha\\), and \\(I\\) depends on the axis by the parallel-axis theorem. Angular momentum about a point fixed in an inertial frame, or the center of mass, satisfies \\(\\boldsymbol\\tau=d\\mathbf L/dt\\) under the usual hypotheses.",
         "proof": "<p>The rotational law for a particle is \\(\\mathbf r\\times\\mathbf F=d(\\mathbf r\\times\\mathbf p)/dt\\) because \\(\\mathbf v\\times\\mathbf p=0\\). Sum over particles. The parallel-axis theorem is the expansion of \\(\\int |\\mathbf r-\\mathbf r_{\\mathrm{cm}}+\\mathbf d|^2 dm\\).</p>"},
        {"name": "Orbits", "statement": "An inverse-square central force conserves angular momentum and energy, and the orbit is a conic. For gravity, closed orbits are ellipses with the center of force at a focus.",
         "proof": "<p>Angular momentum conservation is the torque of a central force vanishing. The orbit equation comes from the substitution \\(u=1/r\\) in the radial equation. The conic section is the solution of that linear oscillator equation for \\(u(\\theta)\\).</p>"},
        {"name": "Oscillations", "statement": "\\(m\\ddot x=-kx\\) has solutions of period \\(2\\pi\\sqrt{m/k}\\). Small oscillations about a stable equilibrium are harmonic, with \\(k\\) equal to the second derivative of the potential at the minimum. Damping and driving add the standard linear terms.",
         "proof": "<p>The characteristic equation \\(r^2+\\omega^2=0\\) gives the period. The small-oscillation claim is Taylor expansion of the potential to second order; the linear term vanishes at an equilibrium.</p>"},
    ],
    "tiers": {
        "0": [R("The Feynman Lectures on Physics, Volume I, opened from the official site",
                "https://www.feynmanlectures.caltech.edu/",
                "Read once, do not study from this. Read the table of contents of Volume I and one lecture if you want the voice. Feynman will not teach you to finish Irodov. Close it.")],
        "1": [R("OpenStax University Physics Volume 1, and MIT 8.01SC",
                "https://openstax.org/details/books/university-physics-volume-1",
                "Free calculus-based text. The course with exams is https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/ . Halliday is the paid traditional book; no edition was verified. OpenStax plus 8.01 is the better pair because you can start tonight and sit a real exam.")],
        "2": [R("Morin, Introduction to Classical Mechanics, ISBN 978-0-521-87622-3, and Kleppner & Kolenkow",
                "https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/",
                "Both books are paid. Morin’s ISBN was catalogued. Kleppner’s ISBN was not, so it is unnamed. The link is 8.01’s problem sets, which are the hard layer you can do before you buy either book.")],
        "3": [R("Irodov, Problems in General Physics, and Krotov",
                "https://archive.org/details/IrodovProblemsInGeneralPhysics",
                "Irodov is the ceiling. Krotov’s Aptitude Test Problems in Physics is the olympiad companion: https://archive.org/details/ptitudetestproblemsinphysics . Use the mechanics parts. The answers in the back of Irodov are a check after the writeup.")],
    },
    "hardest": [
        {"label": "Irodov, the mechanics problems, in order, especially the later ones in each section",
         "url": "https://archive.org/details/IrodovProblemsInGeneralPhysics",
         "why": "The early items are drills. The later items add a constraint, a noninertial frame, or an energy argument you must notice."},
        {"label": "Krotov, mechanics", "url": "https://archive.org/details/ptitudetestproblemsinphysics",
         "why": "Olympiad flavor: the setup is the problem, and the physics is short once you see it."},
        {"label": "MIT 8.01 exams", "url": "https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/",
         "why": "Timed, with free-body diagrams that are part of the grade."},
        {"label": "Morin, the problems on oscillations and central forces",
         "url": "https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/",
         "why": "Morin is paid and unlinked as a file. These 8.01 topics are the public stand-in. Morin’s problems are hard because they ask for a clever frame or a conserved quantity."},
        {"label": "Derive the range formula and the 45° result from Newton’s laws",
         "url": "https://openstax.org/details/books/university-physics-volume-1",
         "why": "If this is not clean, Irodov will be misery for no good reason."},
    ],
    "gate": "<p>Pass: one 8.01 exam, timed, plus ten Irodov mechanics problems with free-body diagrams and a sentence naming the conserved quantity if there is one. Fail if a solution uses a formula you cannot derive from \\(\\mathbf F=m\\mathbf a\\) in one line.</p>",
    "svg": frame(
        '<polygon points="80,280 520,280 520,80" fill="none" stroke="#fff"/>'
        '<rect x="300" y="150" width="70" height="40" fill="#000" stroke="#fff" transform="rotate(-22 335 170)"/>'
        '<line x1="330" y1="160" x2="330" y2="80" stroke="#fff"/>'
        '<text x="338" y="100" fill="#bbb" font-size="13" font-family="Georgia, serif">mg</text>'
        '<text x="250" y="200" fill="#bbb" font-size="13" font-family="Georgia, serif">normal</text>',
        label="A block on an incline with weight drawn straight down"),
    "caption": "Weight is vertical. The axes you compute in are along the incline. Do not mix them.",
    "batches": [
        {"name": "Newton", "items": ["Incline, frictionless.", "Incline with friction \\(\\mu\\), find the acceleration and the condition for sliding.", "Atwood machine.", "Two blocks in contact, a force on the first. Find the contact force.", "A mass on a string in a horizontal circle. Tension."]},
        {"name": "Energy and momentum", "items": ["Prove the work–energy theorem in one dimension.", "A spring launches a mass. Find the speed.", "Elastic collision in one dimension, equal masses.", "Inelastic collision, the combined speed.", "Ballistic pendulum: combine the two conservation laws and say which applies to which stage."]},
        {"name": "Rotation", "items": ["Parallel-axis theorem for a point mass.", "A pulley of nonzero moment of inertia in an Atwood machine. Write the equations. You need \\(\\tau=I\\alpha\\).", "Rolling without slipping: \\(v=\\omega R\\). Where does it come from?", "Angular momentum of a particle, \\(\\mathbf r\\times\\mathbf p\\).", "A force through the center of mass does not torque about the center of mass. Prove it."]},
        {"name": "Orbits and oscillators", "items": ["Period of a spring.", "Physical pendulum, small angles, period \\(2\\pi\\sqrt{I/mgd}\\). Derive it.", "Circular orbit speed for gravity, from \\(GMm/r^2=mv^2/r\\).", "Escape speed.", "Projectile range, the attack, written cleanly."]},
        {"name": "Ceiling", "items": ["Ten Irodov mechanics problems.", "Three Krotov problems.", "One 8.01 exam.", "Derive Kepler’s equal-area law from angular momentum.", "Oral free-body diagram of the incline."]},
    ],
    "bank": ["Frictionless incline.", "Atwood.", "Projectile range at 45°.", "Work–energy theorem.", "Ballistic pendulum.", "Spring period.", "Escape speed.", "Rolling condition \\(v=\\omega R\\).", "One Irodov problem that took over an hour.", "Kepler equal areas."],
    "oral": "State Newton’s second law, derive the incline acceleration, and explain when mechanical energy is conserved. No notes.",
}

EM = {
    "slug": "em",
    "short": "Electromagnetism",
    "title": "Electricity and Magnetism",
    "track": "Physics",
    "needs": ["mechanics", "calc-3", "linear-algebra"],
    "what": """
<p>Electromagnetism in this course is Maxwell’s equations in integral and differential form, and the special cases you can compute: electrostatics, magnetostatics, induction, and electromagnetic waves in vacuum. The mathematical content is the divergence theorem and Stokes’ theorem applied to the electric and magnetic fields. Gauss’s law computes the field when the symmetry kills the flux through most of a surface. Ampère’s law does the same for steady currents. Faraday’s law is induction. The Lorentz force is how fields act on charges.</p>
<p>OpenStax Volume 2 is the free working text. Griffiths, Introduction to Electrodynamics, ISBN 978-1-108-42041-9, is the paid book you should buy when you want the subject at the level of a physics major; the ISBN was catalogued and is the standard fourth edition’s number in that catalog entry. MIT 8.02 is the course. Irodov’s electrodynamics problems are the ceiling alongside Griffiths’ harder exercises. Feynman Volume II is the preview, not the drill.</p>
<p>A Gaussian surface that does not match the symmetry is a calculation you invented. State the symmetry before you integrate.</p>
""",
    "attack": [
        {"q": "<p>Use Gauss’s law to find the electric field of a point charge.</p>",
         "a": "<p>Spherical symmetry: \\(\\mathbf E\\) is radial and constant in magnitude on a sphere of radius \\(r\\). Flux is \\(E\\cdot 4\\pi r^2=q/\\varepsilon_0\\), so \\(E=q/(4\\pi\\varepsilon_0 r^2)\\).</p>"},
        {"q": "<p>Find the field of an infinite line charge with density \\(\\lambda\\).</p>",
         "a": "<p>Cylindrical symmetry. A Gaussian cylinder of radius \\(r\\) and length \\(L\\) has flux \\(E\\cdot 2\\pi r L\\) through the curved wall and none through the caps. Enclosed charge \\(\\lambda L\\). Thus \\(E=\\lambda/(2\\pi\\varepsilon_0 r)\\).</p>"},
        {"q": "<p>Why is the electric field inside the material of a conductor, in electrostatics, equal to zero?</p>",
         "a": "<p>If it were not, free charges would accelerate. Electrostatics means they are not accelerating, so the field in the conducting material is zero. The excess charge sits on the surface.</p>"},
    ],
    "core": [
        {"name": "Electrostatics", "statement": "\\(\\nabla\\cdot\\mathbf E=\\rho/\\varepsilon_0\\), \\(\\nabla\\times\\mathbf E=0\\) in electrostatics, so \\(\\mathbf E=-\\nabla V\\). Gauss’s law in integral form is the flux statement. The potential of a localized charge distribution that vanishes at infinity is the usual Coulomb integral.",
         "proof": "<p>The curl-free claim is Faraday’s law with no changing magnetic field. Existence of the potential is the vector-calculus theorem you proved on the calc-3 page, on a simply connected domain. Gauss’s law is Maxwell’s equation, taken as a law, checked on a point charge by the attack.</p>"},
        {"name": "Magnetostatics", "statement": "\\(\\nabla\\cdot\\mathbf B=0\\). For steady currents, \\(\\nabla\\times\\mathbf B=\\mu_0\\mathbf J\\). The Biot–Savart law is the integral solution. The Lorentz force is \\(q(\\mathbf E+\\mathbf v\\times\\mathbf B)\\).",
         "proof": "<p>These are the laws in the steady case. Ampère’s law in integral form follows from Stokes’ theorem. Use it for a wire, a sheet, and a solenoid, and say why the symmetry lets the field come out of the integral.</p>"},
        {"name": "Induction", "statement": "Faraday: the circulation of \\(\\mathbf E\\) around a closed loop equals minus the derivative of the magnetic flux through a surface bounded by the loop. Lenz’s law is the minus sign. Motional emf for a rod is the Lorentz force on charges in the rod.",
         "proof": "<p>The flux rule is the law. For a moving rod on rails, computing \\(\\oint (\\mathbf v\\times\\mathbf B)\\cdot d\\mathbf l\\) reproduces the flux rule. Do that once so the two pictures are the same fact.</p>"},
        {"name": "Maxwell and waves", "statement": "The displacement current \\(\\mu_0\\varepsilon_0\\partial\\mathbf E/\\partial t\\) repairs Ampère’s law. In vacuum the fields satisfy the wave equation with speed \\(1/\\sqrt{\\mu_0\\varepsilon_0}\\). A plane wave has \\(\\mathbf E\\), \\(\\mathbf B\\), and the direction of propagation mutually perpendicular, with \\(E=cB\\) in SI.",
         "proof": "<p>Take the curl of Faraday, use the vacuum Maxwell equations, and the vector identity for \\(\\nabla\\times(\\nabla\\times\\mathbf E)\\), together with \\(\\nabla\\cdot\\mathbf E=0\\). The speed is read off the wave equation. The relation \\(E=cB\\) is the content of Faraday or Ampère applied to a monochromatic plane wave.</p>"},
        {"name": "Circuits, as lumped Maxwell", "statement": "Kirchhoff’s voltage law is Faraday with no changing flux through the circuit. Kirchhoff’s current law is charge conservation. \\(RC\\), \\(RL\\), and \\(RLC\\) transients are linear ODEs.",
         "proof": "<p>Write the ODE for a series RLC from the loop rule and solve it with the methods of the ODE page. The underdamped, critically damped, and overdamped cases are the discriminant of that characteristic polynomial.</p>"},
    ],
    "tiers": {
        "0": [R("Feynman Lectures, Volume II, from the official contents",
                "https://www.feynmanlectures.caltech.edu/",
                "Read once, do not study from this. Open Volume II from that page and read the contents. It is the conceptual preview. It is not where you learn to do Gauss’s law under a clock.")],
        "1": [R("OpenStax University Physics Volume 2 and MIT 8.02",
                "https://openstax.org/details/books/university-physics-volume-2",
                "Free text plus the course https://ocw.mit.edu/courses/8-02-physics-ii-electricity-and-magnetism-spring-2019/ . Griffiths, ISBN 978-1-108-42041-9, is the paid upgrade when the OpenStax problems feel short on theory.")],
        "2": [R("8.02 problem sets and Griffiths’ problems, if you own the book",
                "https://ocw.mit.edu/courses/8-02-physics-ii-electricity-and-magnetism-spring-2019/",
                "The public hard layer is 8.02. Griffiths is paid. Do the exam problems before you buy anything else.")],
        "3": [R("Irodov, electrodynamics",
                "https://archive.org/details/IrodovProblemsInGeneralPhysics",
                "The ceiling. Krotov’s relevant problems sit in the same archive item as the mechanics olympiad set: https://archive.org/details/ptitudetestproblemsinphysics")],
    },
    "hardest": [
        {"label": "Irodov, the electricity and magnetism problems", "url": "https://archive.org/details/IrodovProblemsInGeneralPhysics",
         "why": "Symmetry plus a differential equation. The hard ones are the ones where the Gaussian surface is not obvious."},
        {"label": "MIT 8.02 exams", "url": "https://ocw.mit.edu/courses/8-02-physics-ii-electricity-and-magnetism-spring-2019/",
         "why": "They mix a circuit transient with a field problem. You do not get to stay in one chapter."},
        {"label": "Derive the infinite line charge field", "url": "https://openstax.org/details/books/university-physics-volume-2",
         "why": "If the factor of \\(2\\pi\\) is memorized, the solenoid will be wrong too."},
        {"label": "Plane electromagnetic wave from Maxwell’s equations", "url": "https://ocw.mit.edu/courses/8-02-physics-ii-electricity-and-magnetism-spring-2019/",
         "why": "The vector identity is the step people skip. Write it."},
        {"label": "RLC transient, all three damping cases", "url": "https://ocw.mit.edu/courses/8-02-physics-ii-electricity-and-magnetism-spring-2019/",
         "why": "This is the ODE page coming back. The physics is the loop rule."},
    ],
    "gate": "<p>Pass: one 8.02 exam, plus written derivations of the point-charge field, the line-charge field, and the vacuum wave speed. Ten Irodov electrodynamics problems. Fail if a Gaussian surface is chosen without a symmetry sentence.</p>",
    "svg": frame(
        '<circle cx="320" cy="180" r="6" fill="#fff"/>'
        '<circle cx="320" cy="180" r="50" fill="none" stroke="#fff"/>'
        '<circle cx="320" cy="180" r="100" fill="none" stroke="rgba(255,255,255,0.6)"/>'
        '<circle cx="320" cy="180" r="150" fill="none" stroke="rgba(255,255,255,0.35)"/>'
        '<text x="340" y="170" fill="#bbb" font-size="13" font-family="Georgia, serif">+q</text>',
        label="Spherical Gaussian surfaces around a point charge"),
    "caption": "Symmetry says the field is constant on the sphere. Gauss’s law does the rest.",
    "batches": [
        {"name": "Electrostatics", "items": ["Point charge from Gauss.", "Line charge.", "Infinite sheet, \\(E=\\sigma/(2\\varepsilon_0)\\). Derive it.", "Field inside a conductor.", "Potential of a point charge, and the field as minus its gradient."]},
        {"name": "Magnetostatics", "items": ["Field of a long wire from Ampère.", "Solenoid, interior field \\(\\mu_0 n I\\).", "Lorentz force on a charge in a uniform B field: circular motion, radius \\(mv/qB\\).", "Why a velocity selector needs crossed E and B.", "\\(\\nabla\\cdot B=0\\) implies no magnetic monopoles. Say what the integral form says."]},
        {"name": "Induction", "items": ["A rod sliding on rails in a uniform B field. Compute the emf two ways.", "Lenz’s law, one example where the induced current opposes the change.", "Self-inductance definition.", "Energy in an inductor, \\(\\tfrac12 LI^2\\), from the power integral.", "A transformer, ideal, voltage ratio."]},
        {"name": "Waves and circuits", "items": ["Derive the wave equation for \\(E\\) in vacuum.", "\\(c=1/\\sqrt{\\mu_0\\varepsilon_0}\\).", "Series RLC, underdamped solution.", "RC charging curve.", "Displacement current: why Ampère’s law needed a repair. One paragraph."]},
        {"name": "Ceiling", "items": ["Ten Irodov E&M problems.", "One 8.02 exam.", "Wave derivation from memory.", "Line charge from memory.", "Oral Gauss’s law."]},
    ],
    "bank": ["Point charge field.", "Line charge.", "Sheet field.", "Conductor, interior field zero.", "Wire from Ampère.", "Solenoid.", "Motional emf two ways.", "Wave speed.", "RLC discriminant.", "One Irodov problem with a non-obvious surface."],
    "oral": "State Gauss’s law, derive the line-charge field, and say what Faraday’s law asserts. No notes.",
}

WAV = {
    "slug": "waves-optics",
    "short": "Waves and optics",
    "title": "Waves and Optics",
    "track": "Physics",
    "needs": ["mechanics", "ode", "calc-3"],
    "what": """
<p>This page is oscillations that travel. A wave on a string, sound, and light are the same mathematics with different restoring mechanisms: a shape \\(f(x-vt)\\) that propagates, a linear wave equation, and superposition. Interference is what superposition does when two waves occupy the same place. Optics in this course means geometrical rays as the short-wavelength limit, and then interference and diffraction as the wave phenomena that rays cannot explain: double slit, single slit, and thin films.</p>
<p>OpenStax Volume 3 and MIT 8.03 are the working pair. The course is called vibrations and waves and it is the right level: normal modes, dispersion, and the wave equation, not a museum of lens formulas. Geometrical optics is in OpenStax and you should be able to do a thin lens, but it is not the ceiling. The ceiling is an 8.03 exam and the optics problems in Irodov that require a path difference.</p>
<p>A phase you cannot track is an interference problem you will get backwards. Write the phase before you write the intensity.</p>
""",
    "attack": [
        {"q": "<p>Show that \\(y=A\\sin(kx-\\omega t)\\) travels in the positive \\(x\\) direction with speed \\(\\omega/k\\), if \\(\\omega\\) and \\(k\\) are positive.</p>",
         "a": "<p>A crest is where the phase is \\(\\pi/2\\), so \\(kx-\\omega t=\\pi/2\\), hence \\(x=\\omega t/k+\\mathrm{const}\\). The crest moves at \\(\\omega/k\\) toward increasing \\(x\\).</p>"},
        {"q": "<p>Two slits separated by \\(d\\) are illuminated by wavelength \\(\\lambda\\). Where are the bright fringes on a distant screen?</p>",
         "a": "<p>The path difference is \\(d\\sin\\theta\\). Bright fringes when that is an integer number of wavelengths: \\(d\\sin\\theta=m\\lambda\\). On a distant screen, \\(y\\approx L\\tan\\theta\\approx L\\sin\\theta\\) for small angles, so \\(y_m\\approx m\\lambda L/d\\).</p>"},
        {"q": "<p>A standing wave \\(2A\\sin(kx)\\cos(\\omega t)\\) has nodes where?</p>",
         "a": "<p>Where \\(\\sin(kx)=0\\), so \\(x=n\\pi/k\\), independent of time. Those points never move.</p>"},
    ],
    "core": [
        {"name": "The wave equation", "statement": "\\(u_{tt}=v^2 u_{xx}\\) has right- and left-moving solutions \\(f(x-vt)\\) and \\(g(x+vt)\\). On a finite string with fixed ends, the normal modes are standing waves with a discrete spectrum.",
         "proof": "<p>The traveling-wave claim is the factoring you did for the PDE page, or a direct chain-rule check. Fixed ends force nodes at the endpoints, hence \\(k=n\\pi/L\\) and frequencies that are integer multiples of the fundamental.</p>"},
        {"name": "Superposition and beats", "statement": "The sum of two close frequencies is a rapid oscillation inside a slow envelope. The beat frequency is the difference of the frequencies.",
         "proof": "<p>Use the sum-to-product identity from the precalculus page. The envelope is the slow cosine. Count how often the envelope peaks.</p>"},
        {"name": "Impedance and reflection", "statement": "At a boundary, part of a wave reflects and part transmits. A fixed end inverts the pulse. A free end does not. The reflection coefficient is fixed by continuity of the transverse displacement and the balance of transverse forces.",
         "proof": "<p>Write the incoming, reflected, and transmitted waves, match the displacement at the joint, and match the slopes with the tensions. The fixed-end limit is infinite mass on the far side, which forces the reflected amplitude to be minus the incoming amplitude.</p>"},
        {"name": "Interference", "statement": "Coherent sources interfere. The phase difference is \\(2\\pi\\) times the path difference over \\(\\lambda\\), plus any reflection phase shift of \\(\\pi\\). Constructive interference when the phase difference is a multiple of \\(2\\pi\\).",
         "proof": "<p>Superpose \\(A\\cos(\\omega t)\\) and \\(A\\cos(\\omega t+\\phi)\\). The amplitude is \\(2A\\cos(\\phi/2)\\). Maxima when \\(\\phi=2\\pi m\\).</p>"},
        {"name": "Diffraction and thin lenses", "statement": "A single slit of width \\(a\\) has minima at \\(a\\sin\\theta=m\\lambda\\) for nonzero integers \\(m\\). A thin lens in the paraxial limit obeys \\(1/s+1/s'=1/f\\). Ray optics is the limit in which interference fringes are too fine to resolve.",
         "proof": "<p>The single-slit minima come from pairing Huygens sources across the slit so each pair differs by half a wavelength. The lens equation is similar triangles in the paraxial ray diagram, or Fermat’s principle. State which one you are using.</p>"},
    ],
    "tiers": {
        "0": [R("Feynman Lectures, the waves chapters via the official site",
                "https://www.feynmanlectures.caltech.edu/",
                "Read once, do not study from this. Volume I contains the waves and the start of optics. Read the contents and one chapter. Then go to 8.03.")],
        "1": [R("MIT 8.03SC and OpenStax Volume 3",
                "https://ocw.mit.edu/courses/8-03sc-physics-iii-vibrations-and-waves-fall-2016/",
                "8.03 is the course. OpenStax Volume 3 holds the optics chapters in a standard order: https://openstax.org/details/books/university-physics-volume-3")],
        "2": [R("8.03 problem sets",
                "https://ocw.mit.edu/courses/8-03sc-physics-iii-vibrations-and-waves-fall-2016/",
                "Normal modes, dispersion, and boundary conditions. This is the hard layer. Lens worksheets are not.")],
        "3": [R("Irodov, oscillations and wave optics",
                "https://archive.org/details/IrodovProblemsInGeneralPhysics",
                "The ceiling. Path differences, coherence, and waves on strings with boundary conditions.")],
    },
    "hardest": [
        {"label": "8.03 exams", "url": "https://ocw.mit.edu/courses/8-03sc-physics-iii-vibrations-and-waves-fall-2016/",
         "why": "Coupled oscillators and boundary conditions, timed."},
        {"label": "Irodov, wave optics", "url": "https://archive.org/details/IrodovProblemsInGeneralPhysics",
         "why": "The geometry of the path difference is the problem. The formula is one line after that."},
        {"label": "Derive the double-slit condition", "url": "https://openstax.org/details/books/university-physics-volume-3",
         "why": "If you cannot draw the triangle, you will not notice a reflection phase shift later."},
        {"label": "Standing waves on a string with one free end", "url": "https://ocw.mit.edu/courses/8-03sc-physics-iii-vibrations-and-waves-fall-2016/",
         "why": "The spectrum changes. People write \\(n\\pi\\) out of habit."},
        {"label": "Beats, from the trig identity, including the beat frequency", "url": "https://openstax.org/details/books/university-physics-volume-1",
         "why": "The factor of 2 is the classic mistake. Volume 1 has the oscillation chapter that feeds this."},
    ],
    "gate": "<p>Pass: one 8.03 exam, plus written derivations of the traveling-wave speed, the fixed-end normal modes, and the double-slit maxima. Five Irodov optics or wave problems. Fail if a phase shift of \\(\\pi\\) on reflection is inserted without a reason.</p>",
    "svg": frame(
        '<path d="M40 180 Q 80 80, 120 180 T 200 180 T 280 180 T 360 180 T 440 180 T 520 180 T 600 180" fill="none" stroke="#fff"/>'
        '<path d="M40 180 Q 80 280, 120 180 T 200 180 T 280 180 T 360 180 T 440 180 T 520 180 T 600 180" fill="none" stroke="rgba(255,255,255,0.4)"/>'
        '<line x1="200" y1="40" x2="200" y2="320" stroke="rgba(255,255,255,0.5)"/>'
        '<text x="208" y="60" fill="#bbb" font-size="13" font-family="Georgia, serif">node</text>',
        label="A standing wave with a node"),
    "caption": "A standing wave is two traveling waves. The node is where they cancel for all time.",
    "batches": [
        {"name": "Traveling waves", "items": ["Speed \\(\\omega/k\\).", "Write \\(f(x+vt)\\) and say which way it moves.", "Check that \\(f(x-vt)\\) solves the wave equation.", "Wavelength, period, and \\(v=f\\lambda\\).", "A pulse hits a fixed end. Sketch the reflection."]},
        {"name": "Standing waves", "items": ["Nodes of \\(\\sin(kx)\\cos(\\omega t)\\).", "String of length \\(L\\), both ends fixed. Frequencies.", "One end free. Frequencies.", "Beats of 440 Hz and 444 Hz.", "Energy in a standing wave, qualitatively: where is it kinetic?" ]},
        {"name": "Interference", "items": ["Double slit, the condition.", "Path difference for a thin film with one reflection phase shift. State the extra \\(\\lambda/2\\).", "Two speakers, constructive interference on the perpendicular bisector. Why?", "Intensity proportional to amplitude squared. What happens to intensity when amplitude doubles?", "Coherence: why a light bulb and a laser are not the same kind of source."]},
        {"name": "Diffraction and rays", "items": ["Single-slit minima.", "Thin lens equation, one numerical example with signs you explain.", "A real image versus a virtual image.", "Why geometrical optics fails at a narrow slit.", "Resolution, Rayleigh criterion, stated."]},
        {"name": "Ceiling", "items": ["One 8.03 exam.", "Five Irodov wave or optics problems.", "Fixed-end spectrum from memory.", "Double slit from memory.", "Oral explanation of a node."]},
    ],
    "bank": ["Wave speed \\(\\omega/k\\).", "Fixed-end frequencies.", "Free-end frequencies.", "Beats.", "Double slit.", "Single slit.", "Reflection at a fixed end.", "Wave equation check for \\(f(x-vt)\\).", "Thin lens signs.", "One Irodov optics problem."],
    "oral": "Derive the speed of a sinusoidal wave, state the fixed-end spectrum, and derive the double-slit maxima. No notes.",
}

MOD = {
    "slug": "modern-physics",
    "short": "Modern physics",
    "title": "Modern Physics",
    "track": "Physics",
    "needs": ["waves-optics", "linear-algebra", "calc-1"],
    "what": """
<p>Modern physics on this page is the break with classical mechanics that happens in the first quantum course and the special-relativity chapter that usually sits beside it: photons, de Broglie waves, the Schrödinger equation in one dimension, the infinite well, the harmonic oscillator, tunneling, and the hydrogen atom at the level of its spectrum. Special relativity is the statements you need in order not to lie about simultaneity, time dilation, length contraction, and \\(E^2=p^2c^2+m^2c^4\\).</p>
<p>This is an entrance, not a graduate quantum course. OpenStax Volume 3 contains the standard modern-physics chapters. MIT 8.04 is the real quantum course and it is the ceiling’s doorway: if you can do its first problem sets, you are past “modern physics” and into quantum mechanics. Griffiths’ Introduction to Quantum Mechanics is the paid book people use next; no edition was verified, so no ISBN is printed. Feynman Volume III is the preview and will not replace 8.04.</p>
<p>A wavefunction is not a smear of the particle. \\(|\\psi|^2\\) is a probability density. Say that sentence correctly or the rest of the page will be mush.</p>
""",
    "attack": [
        {"q": "<p>In the photoelectric effect, why does a brighter light not eject electrons if the frequency is below a threshold?</p>",
         "a": "<p>Each electron absorbs one photon of energy \\(hf\\). If \\(hf\\) is less than the work function, no electron leaves, no matter how many photons arrive. Intensity changes the number of photons, not the energy of each one. \\(K_{\\max}=hf-\\phi\\).</p>"},
        {"q": "<p>State the de Broglie relation and the wavelength of an electron with momentum \\(p\\).</p>",
         "a": "<p>\\(\\lambda=h/p\\). It is a statement about the wavelength of the wavefunction associated with a free particle of momentum \\(p\\), not a claim that the electron is a little wave on a string.</p>"},
        {"q": "<p>For a particle in a one-dimensional infinite well from 0 to \\(a\\), why are the energies proportional to \\(n^2\\)?</p>",
         "a": "<p>The stationary states vanish at the walls, so the wavefunction is a sine with \\(k a=n\\pi\\). Then \\(E=\\hbar^2 k^2/2m\\), so \\(E_n=n^2\\pi^2\\hbar^2/(2ma^2)\\).</p>"},
    ],
    "core": [
        {"name": "Photons and relativity, briefly", "statement": "\\(E=hf\\), \\(p=h/\\lambda\\) for a photon, and \\(E^2=p^2c^2+m^2c^4\\) for a particle. Time dilation and length contraction follow from the invariance of the interval.",
         "proof": "<p>The photon relations are the empirical start of the subject, tied to the photoelectric effect and Compton scattering. Time dilation is a light-clock argument in one frame versus another. Write the light clock once.</p>"},
        {"name": "Schrödinger", "statement": "\\(i\\hbar\\partial_t\\Psi=\\hat H\\Psi\\). For a stationary state, \\(\\Psi(x,t)=\\psi(x)e^{-iEt/\\hbar}\\) and \\(\\hat H\\psi=E\\psi\\). \\(\\int|\\Psi|^2=1\\). Observables are expectation values.",
         "proof": "<p>The separation of the time-dependent equation when \\(H\\) is time-independent is ordinary separation of variables. Normalization is the requirement that the probability density integrates to 1. The expectation-value formula is the definition you will use; derive \\(d\\langle x\\rangle/dt=\\langle p\\rangle/m\\) for a standard Hamiltonian once.</p>"},
        {"name": "Infinite well and oscillator", "statement": "Infinite well energies are \\(n^2\\pi^2\\hbar^2/(2ma^2)\\), wavefunctions sines. The harmonic oscillator has \\(E_n=\\hbar\\omega(n+\\tfrac12)\\), and the ground state is a Gaussian.",
         "proof": "<p>The well is the attack. The oscillator can be solved with Hermite polynomials or with ladder operators. Learn one method well enough to get the zero-point energy without looking.</p>"},
        {"name": "Tunneling and hydrogen", "statement": "A barrier of finite height gives exponential decay inside the barrier and a nonzero transmission probability. The hydrogen spectrum is \\(E_n=-13.6\\,\\mathrm{eV}/n^2\\), from the Coulomb Schrödinger equation, with degeneracy you should be able to state.",
         "proof": "<p>Tunneling is matching oscillatory and exponential solutions and their derivatives at the boundaries. The hydrogen energies you may derive for the radial ground-state ansatz and otherwise quote the separation in spherical coordinates after you have seen it once.</p>"},
        {"name": "Spin, stated", "statement": "Electron spin is a two-state system. The Pauli matrices represent the spin operators in the \\(S_z\\) basis. A spin measurement along an axis yields \\(\\pm\\hbar/2\\).",
         "proof": "<p>This is linear algebra: a Hermitian operator on \\(\\mathbb{C}^2\\) with the right commutation relations. Compute one expectation value, \\(\\langle +x|S_z|+x\\rangle\\), so the matrix language is not decorative.</p>"},
    ],
    "tiers": {
        "0": [R("Feynman Lectures, Volume III, from the official site",
                "https://www.feynmanlectures.caltech.edu/",
                "Read once, do not study from this. Volume III starts from amplitudes. It is a preview of the taste of the subject. 8.04 is the course.")],
        "1": [R("OpenStax Volume 3, modern physics chapters, then MIT 8.04",
                "https://openstax.org/details/books/university-physics-volume-3",
                "OpenStax is the gentle entrance. 8.04 is the real course and becomes the main text as soon as the infinite well feels easy: https://ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2016/")],
        "2": [R("8.04 problem sets",
                "https://ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2016/",
                "This is the hard layer. Griffiths is the paid book to buy when you want a second source; no edition was verified.")],
        "3": [R("8.04 exams",
                "https://ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2016/",
                "The ceiling of this page. A graduate quals in quantum is the next ceiling and is not linked because no specific public exam was verified.")],
    },
    "hardest": [
        {"label": "MIT 8.04 problem sets on the infinite well and the harmonic oscillator",
         "url": "https://ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2016/",
         "why": "Normalization, orthogonality, and expectation values. The algebra is finite and the mistakes are conceptual."},
        {"label": "8.04 exams", "url": "https://ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2016/",
         "why": "They mix formalism and a computation. You cannot pattern-match a textbook example."},
        {"label": "Photoelectric effect, quantitative, from OpenStax",
         "url": "https://openstax.org/details/books/university-physics-volume-3",
         "why": "The threshold is the whole point. A problem that only asks for \\(K_{\\max}\\) at one frequency is too easy; do one that asks for the stopping potential."},
        {"label": "Tunneling transmission for a rectangular barrier, the matching",
         "url": "https://ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2016/",
         "why": "Four coefficients, continuity of \\(\\psi\\) and \\(\\psi'\\). The hardness is bookkeeping."},
        {"label": "Hydrogen ground-state energy, the variational Gaussian or the exact radial solution",
         "url": "https://openstax.org/details/books/university-physics-volume-3",
         "why": "You should see \\(-13.6\\,\\mathrm{eV}\\) come out of a calculation once, not out of a table."},
    ],
    "gate": "<p>Pass: derive the infinite-well spectrum, state the photoelectric equation and the reason for the threshold, and complete one early 8.04 problem set. Fail if \\(|\\psi|^2\\) is described as the particle being smeared out, without the word probability.</p>",
    "svg": frame(
        '<line x1="80" y1="300" x2="80" y2="40" stroke="#fff"/>'
        '<line x1="80" y1="300" x2="560" y2="300" stroke="#fff"/>'
        '<line x1="560" y1="300" x2="560" y2="40" stroke="#fff"/>'
        '<path d="M80 220 Q 200 80, 320 220 T 560 220" fill="none" stroke="#fff"/>'
        '<path d="M80 250 Q 160 120, 240 250 Q 320 380, 400 250 Q 480 120, 560 250" fill="none" stroke="rgba(255,255,255,0.55)"/>'
        '<text x="90" y="60" fill="#bbb" font-size="13" font-family="Georgia, serif">n = 1, 2</text>',
        label="Infinite well wavefunctions"),
    "caption": "The walls force nodes. The energies go as n squared because k does.",
    "batches": [
        {"name": "Light and relativity", "items": ["Photoelectric equation, and a stopping-potential problem you invent numbers for and solve.", "Compton formula, stated, and the classical limit.", "Light-clock time dilation.", "\\(E^2=p^2c^2+m^2c^4\\) for a photon, which forces \\(E=pc\\).", "de Broglie wavelength of a 1 eV electron, order of magnitude, with the arithmetic shown."]},
        {"name": "Formalism", "items": ["Separate the time-dependent Schrödinger equation.", "Normalize a sine on \\([0,a]\\).", "Expectation value of \\(x\\) in the infinite-well ground state.", "Show two different infinite-well eigenfunctions are orthogonal.", "Probability current, stated."]},
        {"name": "Wells and oscillators", "items": ["Infinite well spectrum, derived.", "A well from \\(-a\\) to \\(a\\), even and odd states.", "Harmonic oscillator energies, including the zero-point.", "Sketch the first three oscillator wavefunctions. Nodes.", "A finite well, qualitatively: why the energy is lower than the infinite well of the same width."]},
        {"name": "Beyond one dimension, lightly", "items": ["Tunneling, the matching conditions.", "Hydrogen energies, the formula, and one derivation sketch.", "Degeneracy of the hydrogen level \\(n\\), stated.", "Spin: measure \\(S_z\\) on an \\(S_x\\) eigenstate. Probabilities.", "Pauli matrix \\(\\sigma_z\\), eigenvalues."]},
        {"name": "Ceiling", "items": ["One 8.04 problem set.", "Infinite well from memory.", "Photoelectric threshold explanation, oral.", "Orthogonality computation.", "One exam problem from 8.04 if the set exists on the course site."]},
    ],
    "bank": ["Photoelectric threshold.", "de Broglie.", "Infinite well \\(E_n\\).", "Normalization of the ground state.", "Orthogonality of two modes.", "Harmonic oscillator zero-point energy.", "Light clock.", "Tunneling matching.", "Hydrogen \\(E_n\\).", "One 8.04 problem you could not start."],
    "oral": "Explain the photoelectric threshold, derive the infinite-well energies, and say what \\(|\\psi|^2\\) is. No notes.",
}

PHYSICS = [MECH, EM, WAV, MOD]
