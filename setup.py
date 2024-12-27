from setuptools import find_packages, setup

setup(
    name="JavaLib",
    version="0.1",
    packages=find_packages(),
    description="JavaLib is a Python library that provides several functions and classes to manipulate strings and count the number of elements, using Java language terms.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Arizal Firdaus",
    author_email="bangmulukkeren@gmail.com",
    url="https://github.com/ArizalMuluk/JavaLib",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
