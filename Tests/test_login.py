LOGIN_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"


def open_login_page(page):
    page.goto(LOGIN_URL)

    page.locator("input[name='username']").wait_for(
        state="visible"
    )


def test_login_page_loads(page):
    open_login_page(page)

    assert page.locator("input[name='username']").is_visible()
    assert page.locator("input[name='password']").is_visible()
    assert page.locator("button[type='submit']").is_visible()


def test_username_accepts_input(page):
    open_login_page(page)

    username = page.locator("input[name='username']")

    username.fill("Admin")

    assert username.input_value() == "Admin"


def test_password_is_masked(page):
    open_login_page(page)

    password = page.locator("input[name='password']")

    password.fill("admin123")

    assert password.get_attribute("type") == "password"


def test_valid_login(page):
    open_login_page(page)

    page.locator("input[name='username']").fill("Admin")
    page.locator("input[name='password']").fill("admin123")

    page.locator("button[type='submit']").click()

    dashboard = page.get_by_role(
        "heading",
        name="Dashboard"
    )

    dashboard.wait_for(state="visible")

    assert dashboard.is_visible()


def test_invalid_login(page):
    open_login_page(page)

    page.locator("input[name='username']").fill("WrongUser")
    page.locator("input[name='password']").fill("admin123")

    page.locator("button[type='submit']").click()

    error_message = page.get_by_text(
        "Invalid credentials",
        exact=True
    )

    error_message.wait_for(state="visible")

    assert error_message.is_visible()