from setuptools import setup, find_packages

setup(
    name="gra-asi-metric-space",
    version="0.1.0",
    description="GRA ASI metric space: foam, hierarchical stability, swarm coherence",
    author="GRA-ASI Contributors",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy>=1.21.0",
        "scipy>=1.7.0",
    ],
    python_requires=">=3.8",
)
