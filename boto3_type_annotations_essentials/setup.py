
from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="boto3_type_annotations_essentials",
    version="0.2.0",
    packages=find_packages(),
    url="https://github.com/ybastide/boto3_type_annotations",
    license="MIT License",
    author="Allie Fitter",
    author_email="fitterj@gmail.com",
    description="Type annotations for boto3. Adds code completion in IDEs such as PyCharm.",
    classifiers=(
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
)
