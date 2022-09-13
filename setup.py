import os

from setuptools import find_packages, setup


# Extract version number from package/__init__.py, taken from pip setup.py
def read(rel_path: str) -> str:
    here = os.path.abspath(os.path.dirname(__file__))
    # intentionally *not* adding an encoding option to open, See:
    #   https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    with open(os.path.join(here, rel_path)) as fp:
        return fp.read()


def get_version(rel_path: str) -> str:
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            # __version__ = "0.9"
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


version = get_version("workflow_testing/__init__.py")

# get long description from readme
long_description = read("README.md")


setup(
    name="workflow-testing",
    version=version,
    packages=find_packages(),
    include_package_data=True,
    package_data={"": ["*"]},
    install_requires=[
        "shapely>=1.7",
        "mip>=1.13",
        "minizinc>=0.4.2",
        "deap>=1.3.1",
        "networkx>=2.5  ",
        "numba>=0.50",
        "matplotlib>=3.1",
        "seaborn>=0.10.1",
        "pymzn>=0.18.3",
        "ortools>=8.0",
        "tqdm>=4.62.3",
        "sortedcontainers>=2.4",
        "deprecation",
        "typing-extensions>=4.0",
    ],
    author="Nolwen",
    license="MIT",
    description="Fake library",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
