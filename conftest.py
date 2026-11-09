import pytest

@pytest.fixture
def page(browser): 
    page = browser.new_page(
        viewport = {"width" : 1920, "height" : 1080}
    )
    
    yield page 
    
    page.close()