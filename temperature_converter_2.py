def c_to_f(c):
    return c * 9 / 5 + 32

def c_to_k(c):
    return c + 273.15

def f_to_c(f):
    return (f - 32) * 5 / 9

def k_to_c(k):
    return k - 273.15

value = float(input("Enter Temperature: "))
unit = input("Enter Unit (C/F/K): ").upper()

if unit == "C":
    print(f"Fahrenheit: {c_to_f(value):.2f}")
    print(f"Kelvin: {c_to_k(value):.2f}")

elif unit == "F":
    celsius = f_to_c(value)
    print(f"Celsius: {celsius:.2f}")
    print(f"Kelvin: {c_to_k(celsius):.2f}")

elif unit == "K":
    celsius = k_to_c(value)
    print(f"Celsius: {celsius:.2f}")
    print(f"Fahrenheit: {c_to_f(celsius):.2f}")

else:
    print("Invalid Input")