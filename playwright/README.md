# lambdatest-playwright-driver
[![SmartUI-Testing](https://smartui.lambdatest.com/static/media/LTBadge.64a05e73.svg)](https://smartui.lambdatest.com)

SmartUI SDK for python playwright
- [Installation](#installation)
- [Methods](#methods)
- [Usage](#usage)

## Installation

Install Smart UI cli

```sh-session
$ npm install -g @lambdatest/smartui-cli 
```

Install Python Playwright Package

```sh-session
$ pip3 install lambdatest-playwright-driver
```

## Methods
``` python
smartui_snapshot(page,"snapshotName")
```

- `page` (**required**) - A page object instance from playwright is required.
- `snapshotName` (**required**) - Name of the screenshot

## Usage

Example playwright test using `smartui_snapshot`

``` python
from playwright.sync_api import sync_playwright, Playwright
from lambdatest_playwright_driver import smartui_snapshot

def run(playwright: Playwright):
    webkit = playwright.webkit
    browser = webkit.launch()
    context = browser.new_context()
    page = context.new_page()
    
    try:
        page.goto("https://www.lambdatest.com")
        smartui_snapshot(page, "example_snapshot", options={})
    except Exception as e:
        print(f"Error occurred during SmartUI snapshot: {e}")
    finally:
        browser.close()

with sync_playwright() as playwright:
    run(playwright)
```


Copy the project token from [SmartUI Dashboard](https://smartui.lambdatest.com/) and set on CLI via comman
<b>For Linux/macOS:</b>

```sh-session
 export PROJECT_TOKEN="****-****-****-************"
```

<b>For Windows:</b>

```sh-session
 set PROJECT_TOKEN="****-****-****-************"
```

Running test
```sh-session
$ npx smartui exec [python test command]
```
This will create new build and upload snapshot to Smart UI Project.

Executing above test

```sh-session
$ npx smartui exec python test.py
✔ Authenticated with SmartUI
  → using project token '******#ihcjks'
✔ SmartUI started
  → listening on port 8080
✔ Fetched git information
  → branch: main, commit: 7e336e6, author: Sushobhit Dua
✔ SmartUI build created
  → build id: ee2cb6c5-9541-494a-9c75-a74629396b80
✔ Execution of 'python3 test.py' completed; exited with code 0
  → INFO:@lambdatest/python-selenium-driver:Snapshot captured name
✔ Finalized build

```

## Contribute

#### Reporting bugs

Our GitHub Issue Tracker will help you log bug reports.

Tips for submitting an issue:
Keep in mind, you don't end up submitting two issues with the same information. Make sure you add a unique input in every issue that you submit. You could also provide a "+1" value in the comments.

Always provide the steps to reproduce before you submit a bug.
Provide the environment details where you received the issue i.e. Browser Name, Browser Version, Operating System, Screen Resolution and more.
Describe the situation that led to your encounter with bug.
Describe the expected output, and the actual output precisely.

#### Pull Requests

We don't want to pull breaks in case you want to customize your LambdaTest experience. Before you proceed with implementing pull requests, keep in mind the following.
Make sure you stick to coding conventions.
Once you include tests, ensure that they all pass.
Make sure to clean up your Git history, prior your submission of a pull-request. You can do so by using the interactive rebase command for committing and squashing, simultaneously with minor changes + fixes into the corresponding commits.

## About LambdaTest

[LambdaTest](https://www.lambdatest.com/) is a cloud based selenium grid infrastructure that can help you run automated cross browser compatibility tests on 2000+ different browser and operating system environments. LambdaTest supports all programming languages and frameworks that are supported with Selenium, and have easy integrations with all popular CI/CD platforms. It's a perfect solution to bring your [selenium automation testing](https://www.lambdatest.com/selenium-automation) to cloud based infrastructure that not only helps you increase your test coverage over multiple desktop and mobile browsers, but also allows you to cut down your test execution time by running tests on parallel.