from setuptools import setup, find_packages
import lambdatest_selenium_driver

setup(
    name="lambdatest-selenium-driver",
    version=lambdatest_selenium_driver.__version__,
    author="LambdaTest <keys@lambdatest.com>",
    description="Python Selenium SDK for testing with Smart UI",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="git+https://github.com/LambdaTest/lambdatest-python-sdk",
    keywords="lambdatest python selenium sdk",
    packages=find_packages(),
    license="MIT",
    install_requires=[
        "selenium",
        "lambdatest-sdk-utils"
    ],
    python_requires='>=3.6',
    classifiers=[
        "Development Status :: 5 - Production/Stable"
        "Programming Language :: Python :: 3",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
    ],
)
