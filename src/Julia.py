from Fractal import Fractal


class Julia(Fractal):
    def __init__(self):
        pass

    def count(self, z):
        """Returns an int: given a complex coordinate, return the iteration count of the
        Mandelbrot function for that point. Can only be run in concrete subclasses.
        """
        # c = complex(-1.0, 0.0)
        #
        # for i in range(self.__MAX_ITERATIONS):
        #     z = z * z + c
        #     if abs(z) > 2:
        #         return i
        # return self.__MAX_ITERATIONS
        return 0
