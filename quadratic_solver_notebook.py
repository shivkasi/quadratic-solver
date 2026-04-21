import math

# Cell 1: Import and setup
print("Quadratic Equation Solver")
print("Solve: ax² + bx + c = 0")
print("-" * 40)

# Cell 2: Input coefficients
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Cell 3: Check for special cases and calculate discriminant
if a == 0:
    if b == 0:
        print("Not a valid equation")
        solutions = None
    else:
        # Linear equation: bx + c = 0
        solution = -c / b
        solutions = (solution,)
        print(f"\nThis is a linear equation")
        print(f"Solution: x = {solution:.6f}")
else:
    # Calculate discriminant
    discriminant = b**2 - 4*a*c
    print(f"\nDiscriminant = {discriminant}")
    
    # Cell 4: Solve based on discriminant
    if discriminant > 0:
        # Two distinct real solutions
        print("Two distinct real solutions:")
        sqrt_discriminant = math.sqrt(discriminant)
        x1 = (-b + sqrt_discriminant) / (2*a)
        x2 = (-b - sqrt_discriminant) / (2*a)
        solutions = (x1, x2)
    
    elif discriminant == 0:
        # One repeated real solution
        print("One repeated real solution:")
        x = -b / (2*a)
        solutions = (x,)
    
    else:
        # Complex solutions
        print("Complex solutions:")
        real_part = -b / (2*a)
        imag_part = math.sqrt(-discriminant) / (2*a)
        solutions = (complex(real_part, imag_part), complex(real_part, -imag_part))

# Cell 5: Display solutions
if solutions:
    print("\nSolutions:")
    for i, sol in enumerate(solutions, 1):
        if isinstance(sol, complex):
            print(f"x{i} = {sol}")
        else:
            print(f"x{i} = {sol:.6f}")
