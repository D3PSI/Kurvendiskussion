import sympy as sym
import numpy as np
import matplotlib.pyplot as plt


class FunctionDiscussion:

    function_input_raw = ""
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

        self.function_input_raw = input("Input function in x:    f(x) = ")
        function_raw = sym.sympify(self.function_input_raw)

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

        try:

            # Roots: f(x) = 0
            roots = sym.solveset(self.function_raw, self.x)
            print("Roots:     " + str(roots))

        except:

            pass

        try:

            # Local extrema: f'(x) = 0 && f''(x) != 0
            extrema_possible = list(sym.solveset(self.differentials[1], self.x))
            extrema = {x0 for x0 in extrema_possible if x0 not in sym.solveset(self.differentials[2], self.x)}
            print("Extrema:   " + str(extrema))

        except:

            pass

        try:

            # Inflections: f'(x) = 0 && f''(x) = 0
            inflections_possible = list(sym.solveset(self.differentials[2], self.x))
            inflections = {x0 for x0 in inflections_possible if x0 not in sym.solveset(self.differentials[3], self.x)}
            print("Inflections:    " + str(inflections))

        except:

            pass

        plt.figure(num="D3PSI's function plotter")
        plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
        x = np.arange(-4.0, 4.0, 0.01)
        plt.ylim(-20, 40)
        plt.grid()
        plt.suptitle('f(x) = ' + self.function_input_raw)

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

        try:

            temp = self.differentials_lambdified[0]
            for root in roots:

                plt.plot(root.as_expr().evalf(), temp(root.as_expr().evalf()), "or")
                plt.annotate(
                    "(" + str(sym.N(root.as_expr(), 4)) + ", " + str(sym.N(temp(root.as_expr()), 4)) + ")",
                    xy=(root.as_expr().evalf(), temp(root.as_expr().evalf())), xytext=(10, 0),
                    textcoords="offset points")

        except:

            pass

        try:

            for extreme in extrema:

                plt.plot(extreme.as_expr().evalf(), temp(extreme.as_expr().evalf()), "or")
                plt.annotate(
                    "(" + str(sym.N(extreme.as_expr(), 4)) + ", " + str(sym.N(temp(extreme.as_expr()), 4)) + ")",
                    xy=(extreme.as_expr().evalf(), temp(extreme.as_expr().evalf())), xytext=(10, 0),
                    textcoords="offset points")
        except:

            pass

        try:

            for inflection in inflections:
                plt.plot(inflection.as_expr().evalf(), temp(inflection.as_expr().evalf()), "or")
                plt.annotate(
                    "(" + str(sym.N(inflection.as_expr(), 4)) + ", " + str(sym.N(temp(inflection.as_expr()), 4)) + ")",
                    xy=(inflection.as_expr().evalf(), temp(inflection.as_expr().evalf())), xytext=(10, 0),
                    textcoords="offset points")

        except:

            pass

        plt.legend(loc="upper left")
        plt.show()


def init():

    FunctionDiscussion()


def main():

    init()


if __name__ == "__main__":

    main()

