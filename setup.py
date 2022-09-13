from setuptools import find_packages, setup


setup(
    name="workflow-testing",
    version="0.1",
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
    license="MIT",
    description="Fake library",
)
