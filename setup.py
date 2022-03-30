import setuptools


with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="avmath",
    version="4.0.0a1",
    author="Camillo Ballandt",
    author_email="ballandt@pm.me",
    description="Module for symbolic math",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://ballandt.github.io/p/avmath",
    project_urls={
        "Bug Tracker": "https://github.com/ballandt/avmath/issues",
        "Documentation": "https://ballandt.github.io/p/avmath/docs/4.0"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Licence :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)