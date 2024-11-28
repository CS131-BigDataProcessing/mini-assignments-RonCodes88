# setup.py

from setuptools import setup, find_packages

setup(
    name="crime_test",  # Package name
    version="1.0.0",    # Package version
    description="A package for validating and cleaning crime data",
    long_description=open("README.md").read(),  
    long_description_content_type="text/markdown",
    author="Ronald Li",    # Your name
    author_email="your-email@example.com",  # Your email
    url="https://github.com/CS131-BigDataProcessing/mini-assignments-RonCodes88",
    packages=find_packages(),  # Automatically find the package
    install_requires=[        # List of dependencies
        "pandas",
        "numpy",
    ],
    classifiers=[            # Optional: add classifiers to help with finding your package
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Specify minimum Python version required
)
