import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="serverless-discovery-sdk",
    version="1.0.0",
    author="Andrew Regier",
    author_email="aregier@regiernet.com",
    description="Serverless Service Discovery SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adastradev/serverless-discovery-sdk-python",
    packages=['serverless_discovery_sdk'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)