import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="square root testing",
    version="0.0.1",
    author="dfleta",
    author_email="gelpiorama@gmail.com",
    description="CI kata",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dfleta/kata_tdd_pytest",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
