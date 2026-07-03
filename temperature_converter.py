def c_to_f(c): return c*9/5+32
def c_to_k(c): return c+273.15
def f_to_c(f): return (f-32)*5/9
def k_to_c(k): return k-273.15
v=float(input("Value: "));u=input("From (C/F/K): ").upper()
if u=="C": print(c_to_f(v),"F",c_to_k(v),"K")
elif u=="F": c=f_to_c(v); print(c,"C",c_to_k(c),"K")
elif u=="K": c=k_to_c(v); print(c,"C",c_to_f(c),"F")
else: print("Invalid")