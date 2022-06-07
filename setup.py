from pathlib import Path

from setuptools import find_namespace_packages, setup

# Load packages from requirements.txt
BASE_DIR = Path(__file__).parent
with open(Path(BASE_DIR, "requirements.txt"), "r") as file:
    required_packages = [ln.strip() for ln in file.readlines()]

# Define our package
setup(
    name="TP",
    version=0.1,
    description="Classification des individus selons les caractéristiques de  leurs colonnes vertébrales. ",
    author="Assia DEHILES",
    author_email="assia.dehiles21@gmail.com",
    url="",
    python_requires=">=3.9.3",
    packages=find_namespace_packages(),
    install_requires=[required_packages],
)
