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
Pylenium config is very powerful, but also assumes sensible defaults.  You can modify your config via:

 - Setting environment variables for any of the values (see our travis.yml)
 - Programmatically by just getting the config and modifying it! PyleniumConfig() [Singleton]
 - Do nothing, likely the default will be perfect for your needs!

```python
    # the browser, duh! -> default: [chrome]
    browser = os.getenv('pylenium.browser', Browser.CHROME)  
    
    # headless browser or not? -> default: [no]
    headless = os.getenv('pylenium.headless', False)
    
    # is a remote web driver for distributed testing -> default: [no -- requires a grid]
    remote = os.getenv('pylenium.remote', False) 
    
    # browser window size -> default: [1366 x 768]
    browser_size = os.getenv('pylenium.browser_size', '1366x768')
    
    # browser version -> default: [none - it doesn't really matter outside grid/ie]
    browser_version = os.getenv('pylenium.browser_version', None)
    
    # browser position -> default: [centered]
    browser_position = os.getenv('pylenium.browser_position', None)
    
    # is the browser maximized?: [default: true]
    browser_maximized = os.getenv('pylenium.maximized', True)
    
    # sick of managing chrome/geckodriver binaries? we will do it for you :) environment-agnostic automation!
    # only applicable for local driver(s), can support a proxy for pesky networks -> default: [enabled]
    wdm_enabled = os.getenv('pylenium.wdm_enabled', True)
    
    # with wdm_enabled disabled, specify your own binary path for the driver -> default: [empty] 
    browser_binary = os.getenv('pylenium.browser_binary', '')
    
    # how should pylenium load pages @options -> 'NORMAL', 'FAST', 'EAGER' -> default: [normal]
    # normal -> wait after click/gets, fast -> 'do some magic to move on faster', eager -> 'move on very fast!'
    page_load_strategy = os.getenv('pylenium.page_load_strategy', PageLoadStrategy.NORMAL)  
    
    # custom browser desired capabilities -> default: [Empty]
    desired_capabilities = DesiredCapabilities()
    
    # web application base url -> default: ['http://localhost:8080']
    base_url = os.getenv('pylenium.base_url', 'http://localhost:8080')
    
    # predicate/explicit waiting max timeout -> default: [15 seconds]
    explicit_wait_timeout = os.getenv('pylenium.wait_timeout', 15000)
    
    # how often should predicate be polled for truth -> default: [5 times per second]
    polling_timeout = os.getenv('pylenium.polling_timeout', 200) 
    
    # should pylenium capture screenshots on failure? -> default: [enabled]
    capture_screenshot = os.getenv('pylenium.screenshot', True)
    
    # should we capture page source as HTML on failure -> default: [enabled]
    capture_pagesource = os.getenv('pylenium.pagesource', True) 
    
    # should pylenium click with javascript?
    #  @options -> 'true', 'false', 'only-on-failure' (only when clicking is failing normally)
    # -> default: [disabled]
    javascript_clicking = os.getenv('pylenium.js_click', False)  
    
    # should pylenium send_keys with javascript?
    #  @options -> 'true', 'false', 'only-on-failure' (only when sending keys is failing normally)
    # -> default: [disabled]
    javascript_sendkeys = os.getenv('pylenium.js_sendkeys', False) 
    
    # default find() lookup, takes CSS by default but customisable
    #  @options -> All of seleniums standard BY locators
    # -> default: [css_selector]
    selector_default = Selector.CSS  
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
