from setuptools import setup, find_packages
from os import path

cwd = path.abspath(path.dirname(__file__))
with open(path.join(cwd, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="lambdatest-playwright-driver",
    version="1.1.1",
    author="TestMu AI",
    author_email="keys@lambdatest.com",
    description="Python Playwright SDK for SmartUI visual testing on TestMu AI (formerly LambdaTest)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.testmuai.com/visual-regression-testing/",
    project_urls={
        "Documentation": "https://www.testmuai.com/support/docs/smartui-playwright-python-sdk/",
        "Source": "https://github.com/LambdaTest/lambdatest-python-sdk",
        "Issues": "https://github.com/LambdaTest/lambdatest-python-sdk/issues",
    },
    keywords="lambdatest testmu-ai smartui playwright visual-testing sdk",
    packages=find_packages(),
    license="MIT",
    install_requires=[
        "playwright>=1.12",
        "lambdatest-sdk-utils",
    ],
    python_requires='>=3.7',  # Playwright requires Python 3.7 or newer
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
