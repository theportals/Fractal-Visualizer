from Fractal import Fractal


class Julia(Fractal):
    def __init__(self, fractal_information):
        self.__max_iterations = fractal_information["iterations"]
        self.minx = fractal_information["centerx"] - (fractal_information["axislength"] / 2.0)
        self.maxx = fractal_information["centerx"] + (fractal_information["axislength"] / 2.0)
        self.miny = fractal_information["centery"] - (fractal_information["axislength"] / 2.0)

    def count(self, z):
        """Returns an int: given a complex coordinate, return the iteration count of the
        Mandelbrot function for that point. Can only be run in concrete subclasses.
        """
        c = complex(-1.0, 0.0)

        for i in range(self.__max_iterations):
            z = z * z + c
            if abs(z) > 2:
                return i
        return self.__max_iterations
