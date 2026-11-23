from setuptools import setup, find_packages
from os import path

cwd = path.abspath(path.dirname(__file__))
with open(path.join(cwd, 'readme.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="lambdatest-selenium-driver",
    version="1.0.10",
    author="TestMu AI",
    author_email="keys@lambdatest.com",
    description="Python Selenium SDK for SmartUI visual testing on TestMu AI (formerly LambdaTest)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.testmuai.com/visual-regression-testing/",
    project_urls={
        "Documentation": "https://www.testmuai.com/support/docs/smartui-selenium-python-sdk/",
        "Source": "https://github.com/LambdaTest/lambdatest-python-sdk",
        "Issues": "https://github.com/LambdaTest/lambdatest-python-sdk/issues",
    },
    keywords="lambdatest testmu-ai smartui selenium visual-testing sdk",
    packages=find_packages(),
    license="MIT",
    install_requires=[
        "selenium>=3",
        "lambdatest-sdk-utils>=1.0.5"
    ],
    python_requires='>=3.6',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Testing",
    ],
)
