QUESTION_BANK = {
    "maths": [
        {
            "q": "Differentiate: f(x) = x^3 + 5x^2 - 7x + 2",
            "a": "Given f(x) = x^3 + 5x^2 - 7x + 2\nDifferentiate term-wise:\n\n(d/dx)(x^3) = 3x^2\n(d/dx)(5x^2) = 10x\n(d/dx)(-7x) = -7\n(d/dx)(2) = 0\n\n✅ Final Answer: f'(x) = 3x^2 + 10x - 7"
        },
        {
            "q": "Integrate: ∫ (2x + 3) dx",
            "a": "∫(2x + 3) dx = ∫2x dx + ∫3 dx\n= 2 * (x^2/2) + 3x + C\n= x^2 + 3x + C\n\n✅ Final Answer: x^2 + 3x + C"
        },
        {
            "q": "Solve the quadratic equation: x^2 - 5x + 6 = 0",
            "a": "x^2 - 5x + 6 = 0\nFactorization:\n(x - 2)(x - 3) = 0\n\nSo, x - 2 = 0  => x = 2\nand x - 3 = 0  => x = 3\n\n✅ Final Answer: x = 2, 3"
        },
        {
            "q": "Find the determinant: |1 2; 3 4|",
            "a": "For 2x2 matrix:\n|a b|\n|c d|  determinant = ad - bc\n\nHere a=1, b=2, c=3, d=4\nDet = (1)(4) - (2)(3)\n= 4 - 6\n= -2\n\n✅ Final Answer: -2"
        },
        {
            "q": "Solve the system: 2x + y = 5 and x - y = 1",
            "a": "Given:\n(1) 2x + y = 5\n(2) x - y = 1\n\nAdd (1) and (2):\n(2x + y) + (x - y) = 5 + 1\n3x = 6\nx = 2\n\nPut x=2 in (2):\n2 - y = 1\ny = 1\n\n✅ Final Answer: x = 2, y = 1"
        },
        {
            "q": "Expand using binomial theorem: (a + b)^3",
            "a": "(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3\n\n✅ Final Answer: a^3 + 3a^2b + 3ab^2 + b^3"
        },
        {
            "q": "Find the area under curve y = x^2 from x=0 to x=2",
            "a": "Area under curve = ∫ from 0 to 2 of x^2 dx\n= [x^3/3] from 0 to 2\n= (2^3/3) - (0^3/3)\n= 8/3\n\n✅ Final Answer: 8/3 sq units"
        },
        {
            "q": "Evaluate the limit: lim(x→0) (sin x)/x",
            "a": "This is a standard limit:\nlim(x→0) (sin x)/x = 1\n\n✅ Final Answer: 1"
        },
        {
            "q": "Find eigenvalues of matrix [[2,1],[1,2]]",
            "a": "Matrix A = |2 1|\n           |1 2|\n\nEigenvalues satisfy: |A - λI| = 0\n|2-λ   1 |\n| 1   2-λ| = (2-λ)^2 - 1 = 0\n\n(2-λ)^2 = 1\n2 - λ = ±1\n\nCase 1: 2 - λ = 1  => λ = 1\nCase 2: 2 - λ = -1 => λ = 3\n\n✅ Final Answer: Eigenvalues are 1 and 3"
        },
        {
            "q": "Find sum of first 20 natural numbers",
            "a": "Sum of first n natural numbers = n(n+1)/2\nFor n=20:\nSum = 20*21/2 = 210\n\n✅ Final Answer: 210"
        }
    ],    "physics": [
        {
            "q": "Define Newton’s First Law with example",
            "a": "Newton’s First Law:\nA body remains at rest or continues in uniform motion in a straight line unless acted upon by an external force.\n\nExample:\nA book lying on a table stays at rest until someone pushes it.\n\n✅ Key Idea: Inertia (resistance to change in motion)"
        },
        {
            "q": "What is work, energy and power? Give formulas",
            "a": "✅ Work (W):\nWork is done when a force causes displacement.\nW = F × s × cosθ\nUnit: Joule (J)\n\n✅ Energy:\nCapacity to do work.\nUnit: Joule (J)\n\n✅ Power (P):\nRate of doing work.\nP = W/t\nUnit: Watt (W)"
        },
        {
            "q": "Explain Ohm’s law and V-I graph",
            "a": "✅ Answer:Ohm’s Law:\nAt constant temperature, current through a conductor is directly proportional to voltage across it.\n\nV ∝ I\nV = IR\nWhere R = resistance\n\nV-I Graph:\nStraight line passing through origin.\nSlope = Resistance (R)"
        },
        {
            "q": "Define kinetic energy and derive formula",
            "a": "Kinetic Energy:\nEnergy possessed by a body due to its motion.\n\nFormula:\nKE = (1/2)mv^2\nWhere m = mass, v = velocity\n\n✅ Final Answer: KE = ½mv²"
        },
        {
            "q": "What is momentum? State law of conservation of momentum",
            "a": "Momentum (p):\nProduct of mass and velocity.\np = mv\n\nLaw of conservation of momentum:\nTotal momentum of an isolated system remains constant if no external force acts.\n\n✅ Example: Collision between two bodies"
        },
        {
            "q": "Explain types of friction",
            "a": "Friction: force opposing motion.\n\nTypes:\n1) Static friction (before motion starts)\n2) Kinetic/Sliding friction (during sliding motion)\n3) Rolling friction (during rolling)\n\n✅ Note: Rolling friction is least."
        },
        {
            "q": "What is gravitational potential energy?",
            "a": "Gravitational Potential Energy:\nEnergy due to position of an object in a gravitational field.\n\nFormula:\nPE = mgh\nWhere m = mass, g = acceleration due to gravity, h = height\n\n✅ Final Answer: PE = mgh"
        },
        {
            "q": "State and explain Hooke’s Law",
            "a": "Hooke’s Law:\nWithin elastic limit, stress is directly proportional to strain.\n\nIn spring form:\nF = kx\nWhere k = spring constant, x = extension\n\n✅ Valid only up to elastic limit."
        },
        {
            "q": "Differentiate heat and temperature",
            "a": "✅ Heat:\n- Energy transferred due to temperature difference\n- Unit: Joule or calorie\n- Depends on mass\n\n✅ Temperature:\n- Degree of hotness/coldness\n- Unit: Kelvin / Celsius\n- Independent of mass"
        },
        {
            "q": "Explain SHM with example",
            "a": "Simple Harmonic Motion (SHM):\nMotion in which restoring force is proportional to displacement and acts towards mean position.\n\nExample:\nOscillation of a mass-spring system or pendulum (small angles).\n\n✅ Key point: Periodic motion."
        }
    ],    "mtc": [
        {
            "q": "Solve using matrix method: x + y = 3, 2x + 3y = 8",
            "a": "Given:\n(1) x + y = 3\n(2) 2x + 3y = 8\n\nFrom (1): x = 3 - y\nSubstitute in (2):\n2(3 - y) + 3y = 8\n6 - 2y + 3y = 8\ny = 2\nx = 3 - 2 = 1\n\n✅ Final Answer: x = 1, y = 2"
        },
        {
            "q": "Find inverse of matrix [[1,2],[3,4]]",
            "a": "A = |1 2|\n    |3 4|\n\nInverse of 2x2 matrix:\nA^-1 = (1/det) * | d -b |\n                 | -c a |\n\nDet = (1)(4) - (2)(3) = 4 - 6 = -2\n\nA^-1 = (1/-2) * |4 -2|\n                |-3 1|\n\n✅ Final Answer:\nA^-1 = | -2   1 |\n       | 1.5 -0.5 |"
        },
        {
            "q": "Find rank of matrix [[1,2,3],[2,4,6],[1,1,1]]",
            "a": "Matrix:\nR2 = 2*R1 (dependent)\nSo one row is dependent.\nCheck R3 is not multiple of R1.\n\nHence rank = 2\n\n✅ Final Answer: Rank = 2"
        },
        {
            "q": "Find Laplace transform of t^2",
            "a": "Laplace{t^n} = n! / s^(n+1)\nFor n=2:\nL{t^2} = 2! / s^3 = 2/s^3\n\n✅ Final Answer: 2/s^3"
        },
        {
            "q": "Find Laplace transform of sin(at)",
            "a": "Standard formula:\nL{sin(at)} = a / (s^2 + a^2)\n\n✅ Final Answer: a/(s^2 + a^2)"
        },
        {
            "q": "Solve differential equation: d²y/dx² + y = 0",
            "a": "Given: y'' + y = 0\nCharacteristic equation:\nm^2 + 1 = 0\nm = ±i\n\nGeneral solution:\ny = C1 cos x + C2 sin x\n\n✅ Final Answer: y = C1 cos x + C2 sin x"
        },
        {
            "q": "What is Fourier series? (basic definition)",
            "a": "Fourier Series:\nIt represents a periodic function as a sum of sine and cosine terms.\n\nGeneral form:\nf(x) = a0/2 + Σ(an cos(nx) + bn sin(nx))\n\n✅ Used in signals, waves, heat transfer."
        },
        {
            "q": "Find Z-transform of a^n",
            "a": "Z{a^n} = z / (z - a)\n(For |z| > |a|)\n\n✅ Final Answer: z/(z - a)"
        },
        {
            "q": "Solve: dy/dx = x + y",
            "a": "Given: dy/dx - y = x\nThis is linear differential equation.\n\nIntegrating factor (IF) = e^∫(-1)dx = e^(-x)\n\nMultiply equation by e^(-x):\ne^(-x)dy/dx - y e^(-x) = x e^(-x)\n\nLeft side becomes d/dx (y e^(-x))\nSo:\nd/dx (y e^(-x)) = x e^(-x)\n\nIntegrate both sides:\ny e^(-x) = ∫ x e^(-x) dx + C\n\n∫ x e^(-x) dx = -(x+1)e^(-x)\n\nSo:\ny e^(-x) = -(x+1)e^(-x) + C\nMultiply by e^x:\ny = -(x+1) + C e^x\n\n✅ Final Answer: y = C e^x - x - 1"
        },
        {
            "q": "Define orthogonal matrix with example",
            "a": "Orthogonal Matrix:\nA matrix A is orthogonal if:\nA^T A = I\n\nExample:\n| 0 1 |\n| -1 0 |\nThis satisfies A^T A = I\n\n✅ Key point: inverse = transpose (A^-1 = A^T)"
        }
    ],    "english": [
        {
            "q": "What is communication? Explain its process.",
            "a": "Communication is the process of exchanging information, ideas, or feelings between sender and receiver.\n\nProcess:\n1) Sender\n2) Message\n3) Encoding\n4) Channel/Medium\n5) Receiver\n6) Decoding\n7) Feedback\n8) Noise (barriers)\n\n✅ Goal: understanding and response"
        },
        {
            "q": "Types of communication (verbal and non-verbal)",
            "a": "Types of communication:\n1) Verbal communication:\n   - Oral (speaking)\n   - Written (letters, email)\n\n2) Non-verbal communication:\n   - Facial expressions\n   - Gestures\n   - Body language\n   - Eye contact\n\n✅ Both are important in professional life."
        },
        {
            "q": "What are barriers of communication?",
            "a": "Barriers of communication:\n1) Physical barriers (noise, distance)\n2) Language barriers\n3) Psychological barriers (stress, attitude)\n4) Cultural barriers\n5) Organizational barriers\n\n✅ These barriers reduce clarity and understanding."
        },
        {
            "q": "Difference between formal and informal communication",
            "a": "Formal communication:\n- Official\n- Follows hierarchy\n- Written or structured\n\nInformal communication:\n- Unofficial\n- Friendly\n- No strict rules\n\n✅ Example:\nFormal: official email\nInformal: chatting with friends"
        },
        {
            "q": "What is listening? Types of listening",
            "a": "Listening means actively understanding the message being communicated.\n\nTypes:\n1) Active listening\n2) Passive listening\n3) Critical listening\n4) Empathetic listening\n\n✅ Good listening improves communication."
        },
        {
            "q": "What is group discussion? Benefits",
            "a": "Group Discussion (GD):\nA structured discussion among 6-12 participants on a topic.\n\nBenefits:\n- Improves confidence\n- Enhances communication\n- Tests leadership and teamwork\n\n✅ Used in placements and interviews."
        },
        {
            "q": "How to write a formal email?",
            "a": "Formal Email Format:\n1) Subject line\n2) Greeting (Sir/Madam)\n3) Body (clear purpose)\n4) Closing line\n5) Name + details\n\n✅ Keep it polite, short, and professional."
        },
        {
            "q": "What is a resume? Key parts",
            "a": "Resume is a short document that highlights your education, skills, and achievements.\n\nKey parts:\n1) Personal details\n2) Objective/Summary\n3) Education\n4) Skills\n5) Projects\n6) Internships\n7) Achievements\n\n✅ Used for job applications."
        },
        {
            "q": "Difference between CV and Resume",
            "a": "Resume:\n- Short (1-2 pages)\n- Skills + job-focused\n\nCV:\n- Detailed\n- Includes research, publications\n- Longer\n\n✅ Resume is common for jobs, CV for academic roles."
        },
        {
            "q": "Importance of body language",
            "a": "Body language is non-verbal communication through posture, gestures, expressions, and eye contact.\n\nImportance:\n- Builds confidence\n- Shows interest\n- Improves personality impression\n\n✅ In interviews, body language matters a lot."
        }
    ],    "c": [
        {
            "q": "Write a C program to check even or odd number",
            "a": "Program:\n\n#include <stdio.h>\n#include <conio.h>\n\nint main()\n{\n    int n;\n    printf(\"Enter a number: \");\n    scanf(\"%d\", &n);\n\n    if(n % 2 == 0)\n        printf(\"Even number\");\n    else\n        printf(\"Odd number\");\n\n    return 0;\n}\n\n✅ Logic: Even if divisible by 2."
        },
        {
            "q": "Difference between while and do-while loop",
            "a": " while loop:\n- Condition checked first\n- May execute 0 times\n\n✅ do-while loop:\n- Executes at least once\n- Condition checked after execution\n\nExample:\nwhile(condition) { }\n\ndo { } while(condition);"
        },
        {
            "q": "What is a pointer? Give example",
            "a": "Pointer is a variable that stores the address of another variable.\n\nExample:\nint a = 10;\nint *p = &a;\n\np stores address of a.\n*p gives value of a.\n\n✅ Used in arrays, functions, memory handling."
        },
        {
            "q": "Program to find factorial using loop",
            "a": "#include <stdio.h>\n#include <conio.h>\n\nint main()\n{\n    int n, i;\n    long long fact = 1;\n\n    printf(\"Enter a number: \");\n    scanf(\"%d\", &n);\n\n    for(i = 1; i <= n; i++)\n        fact = fact * i;\n\n    printf(\"Factorial = %lld\", fact);\n\n    return 0;\n}\n\n✅ Factorial of n = 1×2×3×...×n"
        },
        {
            "q": "Program to print Fibonacci series",
            "a": "#include <stdio.h>\n#include <conio.h>\n\nint main()\n{\n    int n, i;\n    int a = 0, b = 1, c;\n\n    printf(\"Enter number of terms: \");\n    scanf(\"%d\", &n);\n\n    printf(\"Fibonacci Series: \");\n    for(i = 1; i <= n; i++)\n    {\n        printf(\"%d \", a);\n        c = a + b;\n        a = b;\n        b = c;\n    }\n\n    return 0;\n}\n\n✅ Fibonacci: 0 1 1 2 3 5 ..."
        },
        {
            "q": "Difference between break and continue",
            "a": "✅ break:\n- Stops the loop immediately\n\n✅ continue:\n- Skips current iteration and continues next iteration\n\nUsed in loops like for, while."
        },
        {
            "q": "What is recursion? Write example",
            "a": "Recursion is a function calling itself until a base condition is met.\n\nExample (factorial):\n\nint fact(int n)\n{\n    if(n == 0)\n        return 1;\n    else\n        return n * fact(n-1);\n}\n\n✅ Needs base condition to stop."
        },
        {
            "q": "What is an array? Explain with example",
            "a": "Array is a collection of similar data items stored in continuous memory.\n\nExample:\nint a[5] = {10, 20, 30, 40, 50};\n\n✅ Access using index a[0], a[1], ..."
        },
        {
            "q": "Program to find largest of 3 numbers",
            "a": "#include <stdio.h>\n#include <conio.h>\n\nint main()\n{\n    int a, b, c;\n    printf(\"Enter three numbers: \");\n    scanf(\"%d %d %d\", &a, &b, &c);\n\n    if(a >= b && a >= c)\n        printf(\"Largest = %d\", a);\n    else if(b >= a && b >= c)\n        printf(\"Largest = %d\", b);\n    else\n        printf(\"Largest = %d\", c);\n\n    return 0;\n}\n\n✅ Compares all three values."
        },
        {
            "q": "Explain functions in C with syntax",
            "a": "Function is a block of code that performs a specific task.\n\nSyntax:\nreturn_type function_name(parameters)\n{\n    // code\n    return value;\n}\n\nExample:\nint add(int a, int b)\n{\n    return a + b;\n}\n\n✅ Helps reuse and modular programming."
        }
    ]
}

