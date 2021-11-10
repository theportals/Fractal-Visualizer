import sys
import FractalInformation, ImagePainter, FractalFactory, PaletteFactory

DEFAULT_FRACTAL = FractalInformation.DEFAULT_FRACTAL_KEY
DEFAULT_PALETTE = "default"

if __name__ == '__main__':
    """Here be our main point of entry. Determine the desired fractal and palette, create them,
    and pass them on to ImagePainter.
    """

    if len(sys.argv) < 2:
        print("FractalFactory: Creating default fractal")
        desired_fractal = DEFAULT_FRACTAL
    else:
        desired_fractal = sys.argv[1]

    if len(sys.argv) < 3:
        print("PaletteFactory: Creating default palette")
        desired_palette = DEFAULT_PALETTE
    else:
        desired_palette = sys.argv[2]

    fractal_info = FractalInformation.makeFractalInfo(desired_fractal)
    fractal = FractalFactory.makeFractal(fractal_info)
    palette = PaletteFactory.makePalette(desired_palette)

    # strips down everything but the file name, without extension.
    # i.e. "../data/mandelbrot.frac" becomes "mandelbrot"
    fractal_name = desired_fractal.split("/")[-1].split(".")[0]

    # painter = new ImagePainter()
    painter = ImagePainter.ImagePainter(fractal_info["pixels"])
    painter.paint(fractal, palette)
    painter.saveImage(fractal_name)
