"""Console script for pypolinsar."""

import fire


def help():
    print("pypolinsar")
    print("=" * len("pypolinsar"))
    print(
        "PyPolInSAR is a Python package designed for PolInSAR (Polarimetric Interferometric Synthetic Aperture Radar) data processing and analysis. It provides a comprehensive set of tools for various PolInSAR applications, such as data visualization, speckle filtering, decomposition, classification, and inversion. With PyPolInSAR, users can easily load, manipulate, and analyze PolInSAR data in Python, making it a valuable tool for researchers and professionals in the field of radar remote sensing."
    )


def main():
    fire.Fire({"help": help})


if __name__ == "__main__":
    main()  # pragma: no cover
