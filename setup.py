from setuptools import setup, find_packages
import python_selenium

setup(
    name="@lambdatest/python-selenium-sdk",
    version=python_selenium.__version__,
    author="LambdaTest <keys@lambdatest.com>",
    description="Python Selenium SDK for testing with Smart UI",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="git+https://github.com/LambdaTest/lambdatest-python-sdk",
    keywords="lambdatest python selenium sdk",
    packages=find_packages(),
    license="MIT",
    install_requires=[
        "requests",
        "selenium"
    ],
    python_requires='>=3.6',
    classifiers=[
        "Development Status :: 5 - Production/Stable"
        "Programming Language :: Python :: 3",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
    ],
)
