def discriminant(a, b, c):
    # D = b^2 - 4ac
    b2 = b * b
    return b2 - 4 * a * c

print("D = b^2 - 4ac")

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

print("D = " + str(b) + "^2 - 4 * " + str(a) + " * " + str(c) + " = " + str(discriminant(a, b, c)))