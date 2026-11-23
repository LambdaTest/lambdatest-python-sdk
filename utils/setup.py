from setuptools import setup, find_packages

setup(
    name="lambdatest-sdk-utils",
    version="1.0.6",
    author="TestMu AI",
    author_email="keys@lambdatest.com",
    description="Shared utilities for the TestMu AI (formerly LambdaTest) SmartUI Python SDKs",
    long_description="Shared utilities used by the [TestMu AI](https://www.testmuai.com/) (formerly LambdaTest) SmartUI SDKs "
        "`lambdatest-selenium-driver` and `lambdatest-playwright-driver`. You normally don't install it directly.",
    long_description_content_type="text/markdown",
    url="https://www.testmuai.com/visual-regression-testing/",
    project_urls={
        "Documentation": "https://www.testmuai.com/support/docs/smart-visual-regression-testing/",
        "Source": "https://github.com/LambdaTest/lambdatest-python-sdk",
        "Issues": "https://github.com/LambdaTest/lambdatest-python-sdk/issues",
    },
    keywords="lambdatest testmu-ai smartui visual-testing sdk",
    packages=find_packages(),
    license="MIT",
    install_requires=[
        "requests==2.*",
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
