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
    python_requires=">=3.10",
    install_requires=[
        "appdirs==1.4.4",
        "attrs==20.3.0",
        "distlib==0.3.1",
        "filelock==3.0.12",
        "importlib-metadata==2.1.1",
        "importlib-resources==4.1.1",
        "iniconfig==1.1.1",
        "packaging==20.8",
        "pluggy==0.13.1",
        "py==1.10.0",
        "pyparsing==2.4.7",
        "pytest==6.2.1",
        "six==1.15.0",
        "toml==0.10.2",
        "tox==3.20.1",
        "typing-extensions==3.7.4.3",
        "virtualenv==20.2.2",
        "zipp==3.4.0",
    ],
)
