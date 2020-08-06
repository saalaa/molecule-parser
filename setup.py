import importlib

from setuptools import setup, find_packages

version = importlib.import_module("molecule_parser").__version__

with open("requirements.txt") as fh:
    requirements = fh.read().split()


setup(
    name="molecule-parser",
    version=version,
    url="https://github.com/saalaa/molecule-parser",
    license="Proprietary",
    author="Benoit Myard",
    author_email="myardbenoit@gmail.com",
    description="Molecule formula parser",
    long_description="See https://github.com/saalaa/molecule-parser",
    zip_safe=False,
    packages=find_packages(),
    # package_data={"": ["data/formula.g"]},
    # include_package_data=True,
    install_requires=requirements,
    setup_requires=["pytest-runner"],
    tests_requires=["pytest-runner"],
    python_requires="~=3.6",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: OS Independent",
        "Operating System :: POSIX :: BSD",
        "Operating System :: POSIX :: Linux",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
)
