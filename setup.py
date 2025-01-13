import setuptools

if __name__ == "__main__":
    setuptools.setup(
        name="nnUNet-UHN-quiz",
        version="0.1.0",
        packages=setuptools.find_packages(exclude=["dataset", "dataset.*"]),
    )
