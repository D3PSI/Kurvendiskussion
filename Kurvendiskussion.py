import sympy as sym
import numpy as np
import matplotlib.pyplot as plt


class FunctionDiscussion:

    function_input = ""
    differentials = []
    differentials_lambdified = []
    x = sym.Symbol('x')

    def __init__(self, max_diffs=10):

        self.max_diffs = max_diffs
        self.function_raw = self.function_input()
        self.calculate_differentials()
        self.lambdify_differentials()
        self.show()

    def function_input(self):

        self.function_input = input("Input function in x:    f(x) = ")
        function_raw = sym.sympify(self.function_input)

        self.differentials.append(function_raw)
        print(self.differentials)

        return function_raw

    def calculate_differentials(self):

        for i in range(0, self.max_diffs):

            try:

                f = sym.diff(self.differentials[i], self.x)
                self.differentials.append(f)

            except:

                break

    def lambdify_differentials(self):

        for i in range(0, self.max_diffs):

            try:

                f = sym.lambdify(self.x, self.differentials[i])
                self.differentials_lambdified.append(f)

            except:

                break

    def val(self, diff, val):

        temp = self.differentials_lambdified[diff]
        return temp(val)

    def show(self):

        # Nullstellen, Kriterium: f(x) = 0
        nullstellen = sym.solveset(self.function_raw, self.x)

        # Extremstellen, Kriterium: f'(x) = 0 && f''(x) != 0
        extremstellen_mögl = list(sym.solveset(self.differentials[1], self.x))
        extremstellen = {x0 for x0 in extremstellen_mögl if x0 not in sym.solveset(self.differentials[2], self.x)}

        # Wendestellen, Kriterium: f'(x) = 0 && f''(x) = 0
        wendestellen_mögl = list(sym.solveset(self.differentials[2], self.x))
        wendestellen = {x0 for x0 in wendestellen_mögl if x0 not in sym.solveset(self.differentials[3], self.x)}

        print("Nullstellen:     " + str(nullstellen))
        print("Extremstellen:   " + str(extremstellen))
        print("Wendestellen:    " + str(wendestellen))

        plt.figure(num="D3PSI's function plotter")
        plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
        x = np.arange(-4.0, 4.0, 0.01)
        plt.ylim(-20, 40)
        plt.grid()
        plt.suptitle('f(x) = ' + self.function_input)
        for i in range(0, self.max_diffs):

            try:

                label = ["f", "(", "x", ")"]
                for j in range(0, i):

                    label.insert(1, "'")

                temp = self.differentials_lambdified[i]
                y = temp(x)
                plt.plot(x, y, label=''.join(label))

            except:

                break

        temp = self.differentials_lambdified[0]
        for nullstelle in nullstellen:
            plt.plot(nullstelle.as_expr().evalf(), temp(nullstelle.as_expr().evalf()), "or")
            plt.annotate(
                "(" + str(sym.N(nullstelle.as_expr(), 4)) + ", " + str(sym.N(temp(nullstelle.as_expr()), 4)) + ")",
                xy=(nullstelle.as_expr().evalf(), temp(nullstelle.as_expr().evalf())), xytext=(10, 0),
                textcoords="offset points")

        for extremstelle in extremstellen:
            plt.plot(extremstelle.as_expr().evalf(), temp(extremstelle.as_expr().evalf()), "or")
            plt.annotate(
                "(" + str(sym.N(extremstelle.as_expr(), 4)) + ", " + str(sym.N(temp(extremstelle.as_expr()), 4)) + ")",
                xy=(extremstelle.as_expr().evalf(), temp(extremstelle.as_expr().evalf())), xytext=(10, 0),
                textcoords="offset points")

        for wendestelle in wendestellen:
            plt.plot(wendestelle.as_expr().evalf(), temp(wendestelle.as_expr().evalf()), "or")
            plt.annotate(
                "(" + str(sym.N(wendestelle.as_expr(), 4)) + ", " + str(sym.N(temp(wendestelle.as_expr()), 4)) + ")",
                xy=(wendestelle.as_expr().evalf(), temp(wendestelle.as_expr().evalf())), xytext=(10, 0),
                textcoords="offset points")

        plt.legend(loc="upper left")
        plt.show()


def init():

    FunctionDiscussion()


def main():

    init()


if __name__ == "__main__":

    main()

