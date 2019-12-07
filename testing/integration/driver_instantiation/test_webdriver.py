def test_something(driver):
    driver.get("http://localhost:1337")
    assert "Directory listing for /" in driver.title
