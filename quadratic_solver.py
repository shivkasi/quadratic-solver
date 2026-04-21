import math

def solve_quadratic(a, b, c):
    """
    Solve a quadratic equation of the form ax² + bx + c = 0
    
    Args:
        a, b, c: Coefficients of the quadratic equation
        
    Returns:
        Tuple of solutions, or None if no real solutions exist
    """
    
    if a == 0:
        if b == 0:
            print("Not a valid equation")
            return None
        # Linear equation: bx + c = 0
        solution = -c / b
        return (solution,)
    
    # Calculate discriminant
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        # Two distinct real solutions
        sqrt_discriminant = math.sqrt(discriminant)
        x1 = (-b + sqrt_discriminant) / (2*a)
        x2 = (-b - sqrt_discriminant) / (2*a)
        return (x1, x2)
    
    elif discriminant == 0:
        # One repeated real solution
        x = -b / (2*a)
        return (x,)
    
    else:
        # Complex solutions
        real_part = -b / (2*a)
        imag_part = math.sqrt(-discriminant) / (2*a)
        return (complex(real_part, imag_part), complex(real_part, -imag_part))


def main():
    print("Quadratic Equation Solver")
    print("Solve: ax² + bx + c = 0")
    print("-" * 40)
    
    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))
        
        solutions = solve_quadratic(a, b, c)
        
        if solutions:
            print("\nSolutions:")
            for i, sol in enumerate(solutions, 1):
                if isinstance(sol, complex):
                    print(f"x{i} = {sol}")
                else:
                    print(f"x{i} = {sol:.6f}")
        
    except ValueError:
        print("Error: Please enter valid numbers")


if __name__ == "__main__":
    main()
