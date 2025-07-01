# Using built-in modules in Python can greatly enhance your code's functionality without needing to write everything from scratch.

import math

print(math.sqrt(16))  # Square root of 16
print(math.factorial(5))  # Factorial of 5
print(math.pi)  # Value of pi
print(math.e)  # Value of e
print(math.pow(2, 3))  # 2 raised to the power of 3
print(math.sin(math.pi / 2))  # Sine of 90 degrees (pi/2 radians)
print(math.cos(0))  # Cosine of 0 radians
print(math.tan(math.pi / 4))  # Tangent of 45 degrees (pi/4 radians)
print(math.log(100, 10))  # Logarithm base 10 of
print(math.radians(180))  # Convert 180 degrees to radians
print(math.degrees(math.pi))  # Convert pi radians to degrees
print(math.ceil(4.2))  # Round up to the nearest integer
print(math.floor(4.8))  # Round down to the nearest integer 
print(math.isclose(0.1 + 0.2, 0.3))  # Check if two floating-point numbers are close
print(math.gcd(48, 18))  # Greatest common divisor of 48 and 18
print(math.lcm(4, 6))  # Least common multiple of 4 and 6
print(math.comb(5, 2))  # Number of combinations of 5 items taken 2 at a time
print(math.perm(5, 2))  # Number of permutations of 5 items taken 2 at a time   
print(math.dist((1, 2), (4, 6)))  # Euclidean distance between two points
print(math.hypot(3, 4))  # Hypotenuse of a right triangle with sides 3 and 4
print(math.prod([1, 2, 3, 4]))  # Product of a list of numbers
print(math.isqrt(16))  # Integer square root of 16  
print(math.trunc(4.7))  # Truncate the decimal part of a number
print(math.fsum([1.0, 2.0, 3.0]))  # Sum of a list of floating-point numbers with higher precision
print(math.copysign(3, -1))  # Copy the sign of -1 to 3
print(math.nextafter(1.0, 2.0))  # Next representable floating-point value after 1.0 towards 2.0
print(math.ulp(1.0))  # Unit in the last place of 1     
print(math.remainder(5, 2))  # Remainder of 5 divided by 2
print(math.fmod(5, 2))  # Floating-point remainder of 5 divided by 2
print(math.frexp(8))  # Returns the mantissa and exponent of 8
