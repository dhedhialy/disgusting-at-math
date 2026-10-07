from bits import R, frame

LIN = {
    "slug": "linear-algebra",
    "short": "Linear algebra",
    "title": "Linear Algebra",
    "track": "Math",
    "needs": ["proof-logic"],
    "what": """
<p>Linear algebra is the study of maps that send lines through the origin to lines through the origin, and of the finite-dimensional spaces those maps act on. Once dimension is finite, every abstract question becomes a question about matrices, and every matrix question is secretly about a linear map that did not want coordinates. The objects you must be able to move between without thinking are: span, independence, basis, dimension, rank, nullity, determinant, eigenvalues, inner products, and the singular value decomposition.</p>
<p>Strang’s MIT course is the computational and geometric introduction. Axler’s Linear Algebra Done Right, 4th edition, is free from the author and refuses to lead with determinants; that is the right second pass, not the first, because you still need to compute. Treil’s Linear Algebra Done Wrong is the free book that keeps determinants and still proves things. Learn Anything’s linear algebra page puts the 3Blue1Brown series and the Georgia Tech interactive text near the top. Both are used below. The rest of that page is software libraries and unrelated algebra, and it was ignored.</p>
<p>The Putnam problems that are “just linear algebra” are short and brutal. They assume you can see a matrix as a map.</p>
""",
    "attack": [
        {
            "q": "<p>Do the vectors \\((1,2)\\) and \\((2,4)\\) form a basis of \\(\\mathbb{R}^2\\)?</p>",
            "a": "<p>No. The second is twice the first, so they are linearly dependent and their span is a line, not the plane. A basis of \\(\\mathbb{R}^2\\) needs two independent vectors.</p>",
        },
        {
            "q": "<p>Solve \\(x+y=1\\), \\(2x+2y=2\\), and describe the solution set.</p>",
            "a": "<p>The second equation is twice the first, so there is one constraint. The solutions are all \\((x,1-x)\\) for \\(x\\in\\mathbb{R}\\), a line.</p>",
        },
        {
            "q": "<p>Compute \\(\\det\\begin{pmatrix}1&2\\\\3&4\\end{pmatrix}\\). What does the sign tell you?</p>",
            "a": "<p>\\(1\\cdot 4-2\\cdot 3=-2\\). The absolute value is the area of the parallelogram spanned by the columns. The negative sign means the ordered basis \\((1,3)\\), \\((2,4)\\) is opposite the standard orientation.</p>",
        },
    ],
    "core": [
        {
            "name": "Bases and dimension",
            "statement": "A basis is a linearly independent spanning set. Every basis of a space has the same number of vectors; that number is the dimension. Any independent set extends to a basis, and any spanning set contains a basis.",
            "proof": "<p>The replacement theorem: if \\(n\\) vectors span and \\(m\\) vectors are independent, then \\(m\\le n\\). Apply it both ways to two bases. Extension is replacement run until the span is the whole space.</p>",
        },
        {
            "name": "Rank–nullity",
            "statement": "For a linear map \\(T:V\\to W\\) between finite-dimensional spaces, \\(\\dim\\ker T+\\dim\\operatorname{im} T=\\dim V\\).",
            "proof": "<p>Take a basis of the kernel and extend it to a basis of \\(V\\). The images of the extra basis vectors are a basis of the image. Count.</p>",
        },
        {
            "name": "Determinant",
            "statement": "The determinant is the unique alternating multilinear form on columns that is 1 on the identity. It is zero exactly when the columns are dependent. It multiplies under matrix multiplication.",
            "proof": "<p>Existence is the Leibniz formula. Uniqueness is expansion along the definition by column operations. Multiplicativity can be seen by fixing one matrix and noticing both sides, as functions of the other, are alternating and multilinear and agree on the identity after scaling.</p>",
        },
        {
            "name": "Eigenvalues",
            "statement": "\\(\\lambda\\) is an eigenvalue of \\(T\\) when \\(Tv=\\lambda v\\) for some \\(v\\ne 0\\). It is a root of the characteristic polynomial \\(\\det(A-\\lambda I)=0\\). A matrix is diagonalizable when there is a basis of eigenvectors, which happens in particular when the characteristic polynomial splits into distinct linear factors.",
            "proof": "<p>\\(A-\\lambda I\\) has a nontrivial kernel exactly when its determinant vanishes. Distinct eigenvalues produce independent eigenvectors: a shortest dependence relation can be hit with \\(A\\) and subtracted to get a shorter one.</p>",
        },
        {
            "name": "Inner products and SVD",
            "statement": "An inner product induces a norm and orthogonality. An orthonormal set is independent. The orthogonal projection onto a subspace \\(U\\) is the unique vector in \\(U\\) whose error is orthogonal to \\(U\\). Every real \\(m\\times n\\) matrix \\(A\\) factors as \\(A=U\\Sigma V^{T}\\) with \\(U,V\\) orthogonal and \\(\\Sigma\\) rectangular diagonal; the diagonal entries are the singular values, square roots of eigenvalues of \\(A^{T}A\\).",
            "proof": "<p>Projection: expand in an orthonormal basis of \\(U\\) and match coefficients, or minimize the quadratic. SVD: \\(A^{T}A\\) is symmetric positive semidefinite, hence orthogonally diagonalizable, and the nonzero eigenvalues give the squared singular values. The rest is bookkeeping with orthonormal bases of the domain and codomain.</p>",
        },
    ],
    "tiers": {
        "0": [R(
            "3Blue1Brown, Essence of Linear Algebra",
            "https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab",
            "Watch once, do not study from this. It is also the one Learn Anything linear-algebra link that earns the preview slot. Close it before you touch a problem set.",
        )],
        "1": [R(
            "MIT 18.06 (Strang) and the Georgia Tech interactive text",
            "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/",
            "18.06 is the course: lectures, problem sets, exams. The free book you can read beside it is Margalit and Rabinoff, Interactive Linear Algebra: https://textbooks.math.gatech.edu/ila/ . Strang, Introduction to Linear Algebra, ISBN 978-1-7331466-7-8, is the paid book the course tracks; the MIT page is https://math.mit.edu/~gs/linearalgebra/ . The free pair is better as a daily diet because the exams are public.",
        )],
        "2": [R(
            "Axler, Linear Algebra Done Right, 4th edition, and Treil, Linear Algebra Done Wrong",
            "https://linear.axler.net/LADR4e.pdf",
            "Axler’s PDF is free from the author; ISBN 978-3-031-41025-3. Treil is the determinant-friendly proof book: https://www.math.brown.edu/streil/papers/LADW/LADW.html . Use Axler for the spectral theorem and Treil when you still need to compute a determinant without shame.",
        )],
        "3": [R(
            "Borisov’s topic-sorted Putnam list, plus Matoušek’s miniatures",
            "https://people.math.binghamton.edu/borisov/Putnam/SelectedProblemList.pdf",
            "The PDF sorts Putnam problems by subject, including linear algebra. Matoušek, Thirty-three Miniatures, is a free PDF of serious applications: https://kam.mff.cuni.cz/~matousek/stml-53-matousek-1.pdf . Prasolov’s problem book was not verified as a stable free file, so it is not linked. Gelfand’s Lectures on Linear Algebra is the right Soviet companion and is paid; no free legal copy was verified.",
        )],
    },
    "hardest": [
        {
            "label": "MIT 18.06 exams",
            "url": "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/",
            "why": "They ask you to see a factorization or a subspace, not to row-reduce a random 4×4 for an hour.",
        },
        {
            "label": "Borisov, Selected Putnam problems, the linear algebra section",
            "url": "https://people.math.binghamton.edu/borisov/Putnam/SelectedProblemList.pdf",
            "why": "The list is short and the problems are real. Each one is a theorem in disguise.",
        },
        {
            "label": "Putnam 2008",
            "url": "https://kskedlaya.org/putnam-archive/2008.pdf",
            "why": "Use it as a second paper after Borisov tells you which problems are linear algebra. The hardness is recognizing the map.",
        },
        {
            "label": "Axler, 4th edition, the exercises on operators and the spectral theorem",
            "url": "https://linear.axler.net/LADR4e.pdf",
            "why": "No matrices to hide in. If the proof needs a basis, you have to say so.",
        },
        {
            "label": "Matoušek, Thirty-three Miniatures",
            "url": "https://kam.mff.cuni.cz/~matousek/stml-53-matousek-1.pdf",
            "why": "Short chapters, each a real application. The linear algebra is not labeled as homework.",
        },
    ],
    "gate": "<p>Pass: one MIT 18.06 exam, closed book, written in full, and five problems from Borisov’s linear-algebra section with complete proofs. You must also state and prove rank–nullity and the spectral theorem for a real symmetric matrix, from a blank page. Fail if singular value decomposition is a slogan you cannot connect to eigenvalues of \\(A^{T}A\\).</p>",
    "svg": frame(
        '<line x1="80" y1="280" x2="560" y2="80" stroke="rgba(255,255,255,0.35)"/>'
        '<line x1="120" y1="260" x2="420" y2="80" stroke="#fff" stroke-width="1.5"/>'
        '<line x1="120" y1="260" x2="300" y2="120" stroke="#fff" stroke-width="1.5"/>'
        '<line x1="300" y1="120" x2="420" y2="80" stroke="rgba(255,255,255,0.7)" stroke-dasharray="4 4"/>'
        '<circle cx="300" cy="120" r="4" fill="#fff"/>'
        '<text x="430" y="78" fill="#bbb" font-size="13" font-family="Georgia, serif">projection</text>',
        label="Orthogonal projection of a vector onto a line",
    ),
    "caption": "The error is perpendicular to the line. That sentence is the projection theorem.",
    "batches": [
        {"name": "Subspaces", "items": [
            "Which of the standard subsets of \\(\\mathbb{R}^3\\) are subspaces: planes through the origin, planes not through the origin, the set where \\(x_1x_2=0\\)?",
            "Prove that the intersection of two subspaces is a subspace, and that the union need not be.",
            "Find a basis of the solution set of \\(x+y+z=0\\).",
            "Extend \\(\\{(1,1,0),(1,0,1)\\}\\) to a basis of \\(\\mathbb{R}^3\\).",
            "State rank–nullity for a \\(3\\times 5\\) matrix of rank 3. What is the dimension of the nullspace?",
        ]},
        {"name": "Maps and matrices", "items": [
            "Write the matrix of rotation by \\(90^\\circ\\) in \\(\\mathbb{R}^2\\) and compute its square.",
            "Prove that matrix multiplication corresponds to composition of the associated maps.",
            "Compute the determinant in the attack, and the inverse if it exists.",
            "Show that a square matrix is invertible if and only if 0 is not an eigenvalue.",
            "Give a \\(2\\times 2\\) matrix that is not diagonalizable. Check the geometric multiplicity.",
        ]},
        {"name": "Inner products", "items": [
            "Apply Gram–Schmidt to \\((1,1,0)\\) and \\((1,0,1)\\).",
            "Prove that an orthonormal set is linearly independent.",
            "Derive the normal equation for least squares: \\(A^{T}A\\hat x=A^{T}b\\).",
            "Show that a real symmetric \\(2\\times 2\\) matrix has real eigenvalues.",
            "Project \\((1,2,2)\\) onto the span of \\((1,0,0)\\) and \\((0,1,0)\\).",
        ]},
        {"name": "Structure", "items": [
            "Prove rank–nullity.",
            "Prove that eigenvectors for distinct eigenvalues are independent.",
            "State the spectral theorem for real symmetric matrices and prove the \\(2\\times 2\\) case.",
            "For \\(A=\\begin{pmatrix}1&1\\\\0&2\\end{pmatrix}\\), find eigenvalues and decide diagonalizability.",
            "Explain SVD in one paragraph without using the words “just a factorization.”",
        ]},
        {"name": "Ceiling", "items": [
            "One 18.06 exam, timed.",
            "Five Borisov linear-algebra Putnam problems.",
            "Ten Axler exercises from the chapters on operators.",
            "Two Matoušek miniatures, written.",
            "Blank-page proof of rank–nullity.",
        ]},
    ],
    "bank": [
        "Why \\((1,2)\\) and \\((2,4)\\) are not a basis.",
        "Determinant and orientation of \\(\\begin{pmatrix}1&2\\\\3&4\\end{pmatrix}\\).",
        "Rank–nullity proof.",
        "Rotation by \\(90^\\circ\\), squared.",
        "A non-diagonalizable \\(2\\times 2\\).",
        "Gram–Schmidt on two vectors in \\(\\mathbb{R}^3\\).",
        "Least-squares normal equation.",
        "Spectral theorem, \\(2\\times 2\\) case.",
        "SVD in terms of \\(A^{T}A\\).",
        "One missed 18.06 exam problem.",
    ],
    "oral": "Define a basis, prove rank–nullity, and explain what an eigenvalue is in terms of a line the map preserves. No notes.",
}

C3 = {
    "slug": "calc-3",
    "short": "Vector calculus",
    "title": "Multivariable and Vector Calculus",
    "track": "Math",
    "needs": ["calc-1", "linear-algebra"],
    "what": """
<p>Multivariable calculus is single-variable calculus with linear algebra inserted at every derivative. The derivative of a map \\(\\mathbb{R}^n\\to\\mathbb{R}^m\\) at a point is the linear map that best approximates it there, represented by the Jacobian matrix. Gradients, directional derivatives, chain rules, and tangent planes are that one definition specialized. Integration becomes a limit of sums over boxes, and the change-of-variables theorem multiplies by the absolute value of the Jacobian determinant, which is why determinants were worth learning.</p>
<p>The second half is the integral theorems: Green, Stokes, and the divergence theorem. They are one theorem, the generalized Stokes theorem, cut into the cases a first course can compute. Schey’s Div, Grad, Curl, and All That (ISBN 978-0-393-92516-6, paid) is the short intuition book; the author is H. M. Schey, not Saff and Snider. Marsden and Tromba, Vector Calculus, ISBN 978-1-4292-1508-4, is a standard paid text. You will work from MIT 18.02 and OpenStax Volume 3, which are free and have exercises.</p>
<p>Learn Anything has no separate vetted path here beyond the calculus junk drawer. The multivariable items in that drawer were course fragments. 18.02 is the course.</p>
""",
    "attack": [
        {
            "q": "<p>For \\(f(x,y)=x^2+y^2\\), compute the gradient at \\((1,1)\\) and say what it points toward.</p>",
            "a": "<p>\\(\\nabla f=(2x,2y)\\), so at \\((1,1)\\) it is \\((2,2)\\). It points in the direction of steepest increase, and its length is that slope.</p>",
        },
        {
            "q": "<p>Compute both mixed second partials of \\(f(x,y)=x^2 y+y^3\\).</p>",
            "a": "<p>\\(f_x=2xy\\), \\(f_y=x^2+3y^2\\), \\(f_{xy}=2x\\), \\(f_{yx}=2x\\). They agree, as Clairaut’s theorem predicts when the second partials are continuous.</p>",
        },
        {
            "q": "<p>Why is the line integral of a gradient around a closed loop equal to 0?</p>",
            "a": "<p>If \\(\\mathbf F=\\nabla f\\), then along a path the integral is the telescope \\(f(\\text{end})-f(\\text{start})\\) by the chain rule and the single-variable fundamental theorem. On a closed loop those points agree, so the integral is 0. The domain has to make the fundamental theorem applicable along the path.</p>",
        },
    ],
    "core": [
        {
            "name": "Derivative as a linear map",
            "statement": "\\(f:\\mathbb{R}^n\\to\\mathbb{R}^m\\) is differentiable at \\(a\\) when there is a linear map \\(Df(a)\\) with \\(f(a+h)=f(a)+Df(a)(h)+o(\\|h\\|)\\). For \\(m=1\\) the matrix of \\(Df\\) is the gradient row. The chain rule is composition of those linear maps.",
            "proof": "<p>In coordinates this is the existence of partial derivatives plus a little theorem: continuous partials imply differentiability. The chain rule is the chain rule for the linear approximations, with an error that is still \\(o(\\|h\\|)\\).</p>",
        },
        {
            "name": "Extrema",
            "statement": "At an interior local extremum of a differentiable function, the gradient vanishes. On a constraint \\(g=c\\) with \\(\\nabla g\\ne 0\\), Lagrange multipliers say \\(\\nabla f=\\lambda\\nabla g\\). The Hessian test classifies nondegenerate critical points.",
            "proof": "<p>Restrict to lines through the point and apply the single-variable Fermat theorem; every directional derivative vanishes, hence the gradient does. Lagrange is the statement that \\(\\nabla f\\) is normal to the level set, and \\(\\nabla g\\) spans that normal line.</p>",
        },
        {
            "name": "Multiple integrals",
            "statement": "A continuous function on a rectangle is Riemann integrable. Fubini’s theorem reduces an integral over a rectangle to iterated one-variable integrals. Under a \\(C^1\\) change of variables with nonzero Jacobian, \\(dx\\,dy=|\\det D\\Phi|\\,du\\,dv\\).",
            "proof": "<p>Fubini for continuous functions is an ε/3 argument with uniform continuity on a compact rectangle. The change-of-variables factor is the area distortion of the derivative linear map, which is the absolute value of the determinant, integrated because the derivative varies from point to point.</p>",
        },
        {
            "name": "Vector calculus identities",
            "statement": "\\(\\operatorname{curl}\\nabla f=0\\) and \\(\\operatorname{div}\\operatorname{curl}\\mathbf F=0\\) wherever the derivatives exist and are continuous. A \(C^1\) vector field on a simply connected domain in \\(\\mathbb{R}^3\\) is conservative if and only if its curl is zero.",
            "proof": "<p>The two identities are equality of mixed partials. The conservative-field theorem in the plane is Green’s theorem plus the curl test; in space it is Stokes plus a disk spanned by the loop, which is where simple connectedness is used.</p>",
        },
        {
            "name": "Green, Stokes, divergence",
            "statement": "Green: \\(\\int_{\\partial D} P\\,dx+Q\\,dy=\\iint_D(Q_x-P_y)\\,dA\\). Stokes: \\(\\int_{\\partial S}\\mathbf F\\cdot d\\mathbf r=\\iint_S(\\nabla\\times\\mathbf F)\\cdot d\\mathbf S\\). Divergence: \\(\\iint_{\\partial W}\\mathbf F\\cdot d\\mathbf S=\\iiint_W\\nabla\\cdot\\mathbf F\\,dV\\). Orientations match.</p>",
            "proof": "<p>Green is proved for a rectangle by writing each side as an iterated integral, then extended by cutting a nice region into pieces. Stokes and the divergence theorem reduce to Green in coordinates, or they are quoted as the cases of the general Stokes theorem you will see properly in a manifolds course. For this page, be able to prove Green on a rectangle.</p>",
        },
    ],
    "tiers": {
        "0": [R(
            "Paul’s Online Math Notes, Calculus III",
            "https://tutorial.math.lamar.edu/Classes/CalcIII/CalcIII.aspx",
            "Read once, do not study from this. Use the section list as a map of topics. The notes are a reference you already know how to find, not the course.",
        )],
        "1": [R(
            "MIT 18.02SC and OpenStax Calculus Volume 3",
            "https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/",
            "18.02 is the lecture and exam path. OpenStax Volume 3 is the free book: https://openstax.org/details/books/calculus-volume-3 . Marsden and Tromba, ISBN 978-1-4292-1508-4, is the paid text if you want a tighter one. Schey, ISBN 978-0-393-92516-6, is the short paid supplement for the field theorems.",
        )],
        "2": [R(
            "18.02 problem sets and Apostol, Volume 2",
            "https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/",
            "Do the 18.02 sets before you shop. Apostol, Calculus, Volume 2, is the paid harder text; the Volume 1 ISBN was verified, the Volume 2 ISBN was not, so it is named without a number.",
        )],
        "3": [R(
            "18.02 exams and Putnam problems Kedlaya files under geometry or analysis",
            "https://kskedlaya.org/putnam-archive/",
            "The exam page is the same 18.02 site. The Putnam archive is the public ceiling. Borisov’s sorted list helps you find the vector-calculus problems: https://people.math.binghamton.edu/borisov/Putnam/SelectedProblemList.pdf",
        )],
    },
    "hardest": [
        {
            "label": "MIT 18.02 exams",
            "url": "https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/",
            "why": "Stokes and the divergence theorem under a clock, with a surface you have to parametrize yourself.",
        },
        {
            "label": "Borisov, the multivariable and vector-calculus Putnam items",
            "url": "https://people.math.binghamton.edu/borisov/Putnam/SelectedProblemList.pdf",
            "why": "They are listed. You do not get to decide that a problem “isn’t really calculus.”",
        },
        {
            "label": "Putnam 2024, any problem that is an integral, a gradient, or an inequality in several variables",
            "url": "https://kskedlaya.org/putnam-archive/2024.pdf",
            "why": "Recent papers assume the theorems and ask for an estimate. The setup is the hard part.",
        },
        {
            "label": "OpenStax Volume 3, the challenge exercises on the integral theorems",
            "url": "https://openstax.org/details/books/calculus-volume-3",
            "why": "Free, so there is no excuse. The hard items ask you to check hypotheses, not just plug in.",
        },
        {
            "label": "A change-of-variables integral you choose from 18.02 that needs polar, cylindrical, or spherical coordinates",
            "url": "https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/",
            "why": "The Jacobian is where people write \\(r\\) and hope. Derive the factor.",
        },
    ],
    "gate": "<p>Pass: one 18.02 exam, timed, plus written proofs of Green’s theorem on a rectangle and of the fact that curl of a gradient is zero. Fail if you cannot parametrize a sphere or state the hypotheses of Stokes.</p>",
    "svg": frame(
        '<path d="M80 280 Q 200 80, 320 180 T 560 100" fill="none" stroke="rgba(255,255,255,0.35)"/>'
        '<line x1="200" y1="200" x2="280" y2="120" stroke="#fff" stroke-width="1.5"/>'
        '<line x1="200" y1="200" x2="300" y2="210" stroke="#fff"/>'
        '<line x1="200" y1="200" x2="210" y2="120" stroke="#fff"/>'
        '<text x="290" y="110" fill="#bbb" font-size="13" font-family="Georgia, serif">normal</text>'
        '<text x="120" y="150" fill="#bbb" font-size="13" font-family="Georgia, serif">tangent plane</text>',
        label="A surface with a normal and a tangent plane",
    ),
    "caption": "The tangent plane is the graph of the derivative. The normal is the gradient of a defining function.",
    "batches": [
        {"name": "Derivatives", "items": [
            "Gradient and Hessian of \\(x^2+xy+y^2\\).",
            "Chain rule: \\(z=f(x,y)\\), \\(x=\\cos t\\), \\(y=\\sin t\\). Write \\(dz/dt\\).",
            "Tangent plane to \\(z=x^2-y^2\\) at \\((1,1,0)\\).",
            "Directional derivative of \\(x^2+y^2\\) at \\((1,1)\\) in the direction of \\((1,-1)\\).",
            "Show mixed partials of \\(x^2 y+y^3\\) agree.",
        ]},
        {"name": "Optimization", "items": [
            "Critical points of \\(x^3+y^3-3xy\\).",
            "Minimum of \\(x^2+y^2\\) on \\(x+2y=5\\), by Lagrange and by substitution.",
            "Farthest point of \\(x^2+y^2+z^2=1\\) from the point \\((2,0,0)\\), geometrically and by Lagrange.",
            "Why a continuous function on a closed disk attains its maximum.",
            "Give a function on \\(\\mathbb{R}^2\\) with a single critical point that is not an extremum. Or prove you cannot, and be right.",
        ]},
        {"name": "Integrals", "items": [
            "\\(\\iint_D (x+y)\\,dA\\) where \\(D\\) is the triangle with vertices \\((0,0),(1,0),(0,1)\\).",
            "Switch to polar: \\(\\iint_{x^2+y^2\\le 1} e^{-x^2-y^2}\\,dA\\).",
            "Volume of the ice cream cone: sphere \\(x^2+y^2+z^2\\le 1\\) above the cone \\(z=\\sqrt{x^2+y^2}\\). Set it up in spherical coordinates and finish it.",
            "State the change-of-variables theorem and use it for \\(u=x+y\\), \\(v=x-y\\) on a square.",
            "Derive the polar factor \\(r\\) from the Jacobian of \\((r\\cos\\theta,r\\sin\\theta)\\).",
        ]},
        {"name": "Fields", "items": [
            "Compute \\(\\nabla\\times\\nabla f\\) in coordinates.",
            "Is \\((-y/(x^2+y^2), x/(x^2+y^2))\\) conservative on \\(\\mathbb{R}^2\\setminus\\{0\\}\\)? Compute the integral around the unit circle.",
            "Green’s theorem on the unit disk for \\(P=-y\\), \\(Q=x\\).",
            "Flux of \\(\\mathbf F=(x,y,z)\\) through the unit sphere.",
            "State Stokes and name the orientations.",
        ]},
        {"name": "Ceiling", "items": [
            "One 18.02 exam.",
            "Three Borisov problems on this material.",
            "Proof of Green on a rectangle.",
            "One Putnam problem involving an integral in the plane.",
            "Oral explanation of why curl grad is zero.",
        ]},
    ],
    "bank": [
        "Gradient of \\(x^2+y^2\\) at \\((1,1)\\).",
        "Closed line integral of a gradient.",
        "Lagrange on \\(x^2+y^2\\) subject to \\(x+2y=5\\).",
        "Polar Jacobian.",
        "Ice-cream volume setup.",
        "The angular form around the origin, and the unit-circle integral.",
        "Green on the unit disk for \\((-y,x)\\).",
        "Flux of \\((x,y,z)\\) through the sphere.",
        "Proof that curl grad vanishes.",
        "One missed 18.02 problem.",
    ],
    "oral": "Define the derivative of a function of several variables, state Lagrange multipliers, and state Stokes’ theorem with orientations. Blank page.",
}

ODE = {
    "slug": "ode",
    "short": "Differential equations",
    "title": "Ordinary Differential Equations",
    "track": "Math",
    "needs": ["calc-1", "linear-algebra"],
    "what": """
<p>An ordinary differential equation asks for a function whose derivatives satisfy a relation. The first course has two layers. The computational layer is a list of solvable classes: separable equations, first-order linear equations via an integrating factor, second-order linear equations with constant coefficients, Laplace transforms, and power-series solutions at ordinary points. The structural layer is what you keep: existence and uniqueness, the phase line and the phase plane, linearization near equilibria, and the fact that an \\(n\\)th-order equation is a first-order system in a higher-dimensional space.</p>
<p>Arnold’s Ordinary Differential Equations is the ceiling. The MIT Press edition has ISBN 978-0-262-51018-9. It is paid, and it is the book whose problems are worth more than another technique chapter. Boyce and DiPrima is the standard paid course text; no edition was verified, so none is cited. Tenenbaum and Pollard, ISBN 978-0-486-64940-5, is the huge Dover problem collection. You will actually work MIT 18.03, which has the lectures, recitations, and exams.</p>
<p>A phase portrait you cannot sketch from the equation is a picture you copied. Sketch before you solve.</p>
""",
    "attack": [
        {
            "q": "<p>Solve \\(y'=y\\) with \\(y(0)=1\\).</p>",
            "a": "<p>Separable: \\(dy/y=dt\\), so \\(\\ln|y|=t+C\\), hence \\(y=Ae^{t}\\). The condition \\(y(0)=1\\) gives \\(A=1\\). Or recognize that the derivative equaling the function characterizes the exponential.</p>",
        },
        {
            "q": "<p>Solve \\(y'+y=0\\).</p>",
            "a": "<p>\\(y=Ce^{-t}\\). Integrating factor \\(e^{t}\\) turns the left side into \\((ye^{t})'\\).</p>",
        },
        {
            "q": "<p>For \\(y'=y(1-y)\\), find the equilibria and say which are stable.</p>",
            "a": "<p>Equilibria at \\(y=0\\) and \\(y=1\\). For \\(y\\in(0,1)\\) the right-hand side is positive, so arrows point up toward 1 and away from 0. For \\(y>1\\) it is negative, toward 1. For \\(y<0\\) it is negative, away from 0. So 1 is stable and 0 is unstable.</p>",
        },
    ],
    "core": [
        {
            "name": "First order",
            "statement": "Separable: \\(y'=f(x)g(y)\\). Linear: \\(y'+p(x)y=q(x)\\) has integrating factor \\(e^{\\int p}\\). Picard–Lindelöf: if \\(f(t,y)\\) is continuous and Lipschitz in \\(y\\) near \\((t_0,y_0)\\), the initial-value problem has a unique solution on some interval.",
            "proof": "<p>The integrating factor is chosen so the left side becomes a derivative. Picard iteration is the contraction mapping on a short-time space of continuous functions; you should be able to state the theorem now and prove the contraction estimate when you have analysis under your belt. Do not pretend the theorem is “just separation of variables.”</p>",
        },
        {
            "name": "Second-order linear",
            "statement": "For \\(y''+ay'+by=0\\), try \\(e^{rt}\\) and solve the characteristic polynomial. Repeated roots bring a factor of \\(t\\). A particular solution of the nonhomogeneous equation plus the homogeneous general solution is the general solution. Wronskian nonzero means the two homogeneous solutions form a basis.",
            "proof": "<p>The equation is linear, so the solution space of the homogeneous problem is a vector space; the existence theorem says the dimension equals the order. The characteristic polynomial is the computation. Variation of parameters produces a particular solution from the Wronskian.</p>",
        },
        {
            "name": "Systems and phase planes",
            "statement": "\\(\\mathbf x'=A\\mathbf x\\) is solved by the exponential \\(e^{tA}\\), computed via Jordan form or, when \\(A\\) is diagonalizable, via eigenvalues. Equilibria of \\(\\mathbf x'=\\mathbf F(\\mathbf x)\\) are where \\(\\mathbf F=0\\). The linearization \\(D\\mathbf F\\) classifies a hyperbolic equilibrium. A sign chart or nullclines sketch the rest.</p>",
            "proof": "<p>If \\(Av=\\lambda v\\) then \\(e^{\\lambda t}v\\) solves the system. The linearization theorem says a hyperbolic equilibrium looks like its linear part; the proof is Hartman–Grobman, which you may quote after you have checked the eigenvalues are off the imaginary axis.</p>",
        },
        {
            "name": "Laplace transforms",
            "statement": "\\(\\mathcal L\\{y\\}(s)=\\int_0^\\infty e^{-st}y(t)\\,dt\\). It turns \\(y'\\) into \\(sY-y(0)\\) and convolutions into products, under growth hypotheses that justify the integrals.",
            "proof": "<p>Integration by parts on the integral for \\(y'\\), with the boundary term at infinity killed by the exponential decay you assumed. Tables are not a proof. Derive the transforms of \\(1\\), \\(e^{at}\\), and \\(\\sin bt\\) once.</p>",
        },
        {
            "name": "Series and a first PDE",
            "statement": "At an ordinary point, a linear ODE has a power-series solution whose radius is at least the distance to the nearest complex singularity of the coefficients. The heat equation \\(u_t=u_{xx}\\) and the wave equation \\(u_{tt}=c^2 u_{xx}\\), with boundary conditions, are solved by separating variables into an ODE eigenvalue problem.",
            "proof": "<p>The series method is plugging in \\(\\sum a_n x^n\\) and matching coefficients; convergence needs a majorant or a citation of the existence theorem in the complex domain. Separation of variables is linear algebra: eigenfunctions of a symmetric differential operator form a basis you can expand the initial data in. You will prove the basis claim in a later course; here, do it for sine series on \\([0,\\pi]\\) by quoting Fourier.</p>",
        },
    ],
    "tiers": {
        "0": [R(
            "Paul’s Online Math Notes, Differential Equations",
            "https://tutorial.math.lamar.edu/Classes/DE/DE.aspx",
            "Read once, do not study from this. It is a technique index. Knowing the names of the techniques is the preview. Computing them is the course.",
        )],
        "1": [R(
            "MIT 18.03SC",
            "https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/",
            "Lectures, recitations, problem sets, exams. This is the main text. Boyce and DiPrima is the usual paid book; no edition was verified. Use 18.03 so the problem sets have published solutions.",
        )],
        "2": [R(
            "Tenenbaum and Pollard, Ordinary Differential Equations, ISBN 978-0-486-64940-5",
            "https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/",
            "The Dover book is the problem mountain and it is paid; the ISBN is catalogued. The link is 18.03’s problem sets, which you can do tonight. Use Tenenbaum when you want more drills of a type 18.03 only assigned twice.",
            paid=True,
        )],
        "3": [R(
            "Arnold, Ordinary Differential Equations, ISBN 978-0-262-51018-9",
            "https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/",
            "Arnold is paid and is the ceiling: geometry of phase portraits, not another integrating factor. No free legal edition was verified, so the link stays on the 18.03 exams, which are the public ceiling you can download. Do Arnold’s problems if you buy the book. Do the exams either way.",
        )],
    },
    "hardest": [
        {
            "label": "MIT 18.03 exams",
            "url": "https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/",
            "why": "Phase portraits and linear systems under time. The algebra is short. The picture is the answer.",
        },
        {
            "label": "Arnold, the problem sections on phase portraits and linearization",
            "url": "https://kskedlaya.org/putnam-archive/",
            "why": "Arnold is paid and unlinked as a file. The Putnam archive stands in as timed problems that use the same taste: qualitative, not formulaic. Buy Arnold if you can.",
        },
        {
            "label": "18.03 problem sets on linear systems",
            "url": "https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/",
            "why": "Drawing nullclines and deciding stability from a matrix is the skill that transfers to dynamics.",
        },
        {
            "label": "A series solution at an ordinary point, from the 18.03 sets",
            "url": "https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/",
            "why": "The recurrence is easy to mis-index. That is the whole difficulty.",
        },
        {
            "label": "Separation of variables for the heat equation on an interval, one 18.03 or later problem",
            "url": "https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/",
            "why": "You have to keep the boundary conditions in the eigenvalue problem. Drop them and the series is fiction.",
        },
    ],
    "gate": "<p>Pass: one 18.03 exam, timed, including a phase-plane problem drawn without a computer, plus a written statement of Picard–Lindelöf with the Lipschitz hypothesis actually present. Fail if “stable” means “I solved it and the formula looks small.”</p>",
    "svg": frame(
        '<line x1="320" y1="30" x2="320" y2="330" stroke="rgba(255,255,255,0.45)"/>'
        '<line x1="40" y1="180" x2="600" y2="180" stroke="rgba(255,255,255,0.45)"/>'
        '<path d="M80 80 C 180 40, 220 160, 320 180 C 420 200, 460 300, 560 260" fill="none" stroke="#fff" stroke-width="1.5"/>'
        '<circle cx="320" cy="180" r="5" fill="#000" stroke="#fff"/>'
        '<text x="332" y="170" fill="#bbb" font-size="13" font-family="Georgia, serif">equilibrium</text>',
        label="A phase-plane trajectory near an equilibrium",
    ),
    "caption": "The picture is the object. The closed-form solution is optional.",
    "batches": [
        {"name": "First order", "items": [
            "Solve \\(y'=y\\), \\(y(0)=1\\).",
            "Solve \\(y'+y=e^t\\).",
            "Solve \\(y'=y(1-y)\\) by separating, and compare with the phase line.",
            "Where does \\(y'=\\sqrt{y}\\), \\(y(0)=0\\), fail uniqueness? Exhibit two solutions.",
            "State Picard–Lindelöf.",
        ]},
        {"name": "Second order", "items": [
            "Solve \\(y''+y=0\\), \\(y(0)=1\\), \\(y'(0)=0\\).",
            "Solve \\(y''-3y'+2y=e^{t}\\).",
            "Repeated root: \\(y''-2y'+y=0\\).",
            "Write the Wronskian of \\(\\cos t\\) and \\(\\sin t\\) and say what it tells you.",
            "Variation of parameters for \\(y''+y=\\sec t\\) on \\((-\\pi/2,\\pi/2)\\).",
        ]},
        {"name": "Systems", "items": [
            "Solve \\(\\mathbf x'=\\begin{pmatrix}1&1\\\\0&2\\end{pmatrix}\\mathbf x\\).",
            "Classify the origin for a spiral, a node, a saddle, from the eigenvalues. Draw one of each.",
            "Linearize \\(x'=x-y\\), \\(y'=x+y-x^3\\) is optional; do \\(x'=-y\\), \\(y'=x-y\\) and classify.",
            "Nullclines of \\(x'=x(1-x-y)\\), \\(y'=y(1-2x)\\). Equilibria only, then a sketch.",
            "Convert \\(y''+y'+y=0\\) into a first-order system.",
        ]},
        {"name": "Transforms and series", "items": [
            "Laplace transform of \\(e^{at}\\) from the integral.",
            "Solve \\(y''+y=0\\), \\(y(0)=1\\), \\(y'(0)=0\\) by Laplace transforms.",
            "Series solution of \\(y''+xy=0\\) at 0, first four nonzero terms, and the recurrence.",
            "Separate variables: \\(u_t=u_{xx}\\), \\(u(0,t)=u(\\pi,t)=0\\), \\(u(x,0)=\\sin x\\).",
            "Why does a repeated Laplace calculation without growth hypotheses not count as a proof?",
        ]},
        {"name": "Ceiling", "items": [
            "One 18.03 exam.",
            "Three phase portraits from scratch.",
            "Picard–Lindelöf, hypotheses written from memory.",
            "One Arnold problem if you have the book; otherwise one extra 18.03 exam.",
            "The heat equation example, including why the eigenvalue is what it is.",
        ]},
    ],
    "bank": [
        "\\(y'=y\\), \\(y(0)=1\\).",
        "Phase line of \\(y'=y(1-y)\\).",
        "Non-uniqueness for \\(y'=\\sqrt{y}\\).",
        "\\(y''+y=0\\) with initial conditions.",
        "Repeated-root second-order equation.",
        "A saddle versus a spiral, from eigenvalues.",
        "Laplace transform of \\(e^{at}\\).",
        "Series recurrence for \\(y''+xy=0\\).",
        "Heat equation with \\(u(x,0)=\\sin x\\).",
        "One missed 18.03 phase-plane problem.",
    ],
    "oral": "Solve a first-order linear equation, classify an equilibrium from eigenvalues, and state Picard–Lindelöf. Out loud, no notes.",
}
