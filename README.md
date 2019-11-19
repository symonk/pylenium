<kbd>
  <img src="https://github.com/symonk/pylenium/blob/master/.github/.images/pylenium_logo.png">
</kbd>
  <p></p>

[![Build Status](https://api.travis-ci.org/symonk/pylenium.svg?branch=master)](https://travis-ci.org/symonk/pylenium)
[![License Apache](https://img.shields.io/badge/license-Apache%202-brightgreen.svg)](https://github.com/symonk/pylenium/blob/master/LICENSE)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=symonk_pylenium&metric=bugs)](https://sonarcloud.io/dashboard?id=symonk_pylenium)
[![codecov](https://codecov.io/gh/symonk/pylenium/branch/master/graph/badge.svg)](https://codecov.io/gh/symonk/pylenium)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=symonk_pylenium&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=symonk_pylenium)
[![Find_Me LinkedIn](https://img.shields.io/badge/Find_Me-LinkedIn-brightgreen.svg)](https://www.linkedin.com/in/simonk09/)
[![Find_Me Slack](https://img.shields.io/badge/Find_Me-Slack-brightgreen.svg)](https://testersio.slack.com)

## What is Pylenium? :flags: 
Pylenium is a test automation framework written in python, it has two simple goals:  Increase stability and time to market
when building automated testing solutions for a frontend web application with python.  Using pytest as the test runner it boosts an assortment of feature(s) to make encapsulating web applications and executing tests on distributed architecture.

Why couple tightly to pytest? There are plenty of options in the python-selenium world for unittest etc, I struggled to find a nice pytest alternative that didn't compromise and prevent usage of some of pytests most powerful features.

```python
    @pylenium_case_information(case='testcase-101', issue_id='issue-949', description='Logging in is so easy!')
    def test_my_login():
      start('http://www.google.co.uk')
      find(name('user.name')).set_value('simon')
      find(name('password')).set_value('securepassword')
      find('#submit')).click()  # default selector
      find(id('username')).should_have(text('Hello, Simon!'))      

    # But I want page objects! - so easy: @see: below
    def test_some_cool_page(self):
        start(ExampleLoginPage()) # page loaded, page object instantiated!
```

---

### Page Objects :hearts:
Easy, hassle free, abstracted -> Exactly how page objects should be!

```python
    # driver less page objects? must be magic! -> no page factory, init elements or messing with driver code
    # pages are not necessary, but recommended! (@see: our page objectless example code!)
    # pyleniums own web element is very smart and handles waiting to increase stability
    @loadable(page='/login.php')
    class ExampleLoginPage:
        _text_field_on_login_page = ID("some_id_attribute_value")
    
        def retrieve_the_text(self) -> str:
            return self._text_field_on_login_page.text()
    
        def set_the_text(self, value: str) -> ExampleLoginPage:
            self._text_field_on_login_page.set_text(value)
            self._text_field_on_login_page.should_have(Text(value))
            return self
```
    
---

### Configuration :clipboard:
Pylenium aims to be configurable, but sensible when required to be implicit.  We consider our config a singleton tho,
when we instantiate the driver, it really shouldn't be modified! All options can be seen in the pylenium-pytest plugin
module.


```python
@dataclass
class PyleniumConfig:
    """
    Pyleniums core config, this is built as part of the plugins parse args
    Pylenium will assume sensible default value(s) here
    n.b -> This is considered a singleton, changing it mid run is not advised

    Attributes:
        --browser: The browser in which to execute tests on
        --headless: Should the browser run headlessly
        --remote: Should the browser be instantiated for the selenium grid
        --server: Server ip address of the selenium grid
        --server_port: Server port of the selenium grid
        --browser_size: Size of the instantiated browser window
        --browser_version: Version of the browser we should attempt to automatically aquire (unnecessary with --remote=True)
        --browser_maximized: Should the browser instantiated be maximized
        --aquire_binary: Should we aquire the binary automatically and cache it locally
        --browser_path: If you do not want to aquire the binary, the path to your chromedriver or geckodriver binary
        --page_load_strategy: The strategy we should use to load page(s) and ensure it is time to proceed
        --browser_capabilities: Path to a file containing a dictionary of your browser capabilities @default None
        --load_base_url: On driver instantiation, automatically load your applications base url (e.g login page)
        --explicit_wait: Time in milliseconds to explicitly wait for pyleniums smart actions
        --polling_interval: Time in milliseconds to check smart actions predicates to decipher if continuation should occur
        --screenshot_on_fail: Attach a screenshot of the browser if a test fails
        --page_source_on_fail: Attach the page source (DOM) of the browser if a test fails
        --stack_trace_on_fail: Provides basic information regarding the reason behind a test failing
        --click_with_js: Attempt to do clicks using javascript actions (not selenium click actions)
        --sendkeys_with_js: Attempt to send keys (text) using javascript actions (not selenium click actions)
        --default_selector: Default selector for PyleniumElements to use for lookup
    """
    browser: SupportedBrowser = SupportedBrowser()
    headless: bool = False
    remote: bool = False
    server: str = LOCALHOST_URL
    server_port: int = 4444
    browser_size: str = '1366x768'
    browser_version: str = 'latest'
    browser_maximized: bool = True
    aquire_binary: bool = True
    browser_path: str = None
    page_load_strategy: PageLoadingStrategy = PageLoadingStrategy()
    browser_capabilities: BrowserCapabilities = None
    load_base_url: bool = False
    base_url: ValidUrl = LOCALHOST_URL
    explicit_wait: int = 15000
    polling_interval: int = 200
    screenshot_on_fail: bool = False
    page_source_on_fail: bool = False
    stack_trace_on_fail: bool = False
    click_with_js: bool = False
    sendkeys_with_js: bool = False
    default_selector: str = 'CSS'
```
---

### Page Actions :trophy:
Repeatable steps and chains of page object commands, all wrapped under one roof!

    - clean abstractions
    - repeatable and very test friendly
    
---

###  :star: Companies who back the project:

[![Intellij IDEA](https://cloud.google.com/tools/images/icon_IntelliJIDEA.png )](http://www.jetbrains.com/idea)
[![BrowserStack](https://www.browserstack.com/images/mail/browserstack-logo-footer.png)](https://www.browserstack.com)

---
