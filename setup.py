from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Machine_Efficiency_Prediction",
    version="0.1",
    author="Gaurav Pahwa",
    packages=find_packages(),
    install_requires = requirements,
)