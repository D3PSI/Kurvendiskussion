import sympy as sym
import numpy as np
import matplotlib.pyplot as plt

x = sym.Symbol('x')
funktion_str = input("Funktion eingeben: f(x)= ")
f0 = sym.sympify(funktion_str)
f = sym.lambdify(x, funktion_str)
f1 = sym.diff(f0, x, 1)
f1_ = sym.lambdify(x, f1.as_expr())
f2 = sym.diff(f0, x, 2)
f2_ = sym.lambdify(x, f2.as_expr())
f3 = sym.diff(f0, x, 3)
f3_ = sym.lambdify(x, f3.as_expr())

def fnc(t):
    return f(t)

def fnc1(t):
    return f1_(t)

def fnc2(t):
    return f2_(t)

def fnc3(t):
    return f3_(t)

# Nullstellen, Kriterium: f(x) = 0
nullstellen = sym.solveset(f0, x)

# Extremstellen, Kriterium: f'(x) = 0 && f''(x) != 0
extremstellen_mögl = list(sym.solveset(f1, x))
extremstellen = {x0 for x0 in extremstellen_mögl if x0 not in sym.solveset(f2, x)}

# Wendestellen, Kriterium: f'(x) = 0 && f''(x) = 0
wendestellen_mögl = list(sym.solveset(f2, x))
wendestellen = {x0 for x0 in wendestellen_mögl if x0 not in sym.solveset(f3, x)}

# Graphische Darstellung
plt.figure(1)
t1 = np.arange(-100.0, 100.0, 0.1)
plt.plot(t1, fnc(t1), label="f(x)")
plt.plot(t1, fnc1(t1), label="f'(x)")
plt.plot(t1, fnc2(t1), label="f''(x)")
plt.plot(t1, fnc3(t1), label="f'''(x)")
plt.suptitle('f(x) = ' + funktion_str + "\n" + "f'(x) = " + str(f1.as_expr()))
plt.plot(1.5, 1.5, "or")
plt.legend(loc="upper left")
plt.show()

def main():
    print("1. Ableitung:    " + str(f1))
    print("2. Ableitung:    " + str(f2))
    print("3. Ableitung:    " + str(f3))
    print("Nullstellen:     " + str(nullstellen))
    print("Extremstellen:   " + str(extremstellen))
    print("Wendestellen:    " + str(wendestellen))

if __name__ == "__main__":
    main()