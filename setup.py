from setuptools import setup, find_packages

setup(
    name="apia-cli",
    version="1.0.0",
    description="CLI for the APIA standard — API registry for AI agents",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="APIA Contributors",
    url="https://github.com/Komsomol39/apia-standard",
    packages=find_packages(),
    py_modules=["apia"],
    entry_points={
        "console_scripts": [
            "apia=cli.apia:main",
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)
