from behave import *

@given('user is on registration page')
def step_impl(context):
    context.browser.get(context.homepage)
    context.browser.find_element_by_xpath("//span[contains(.,'My Account')]").click()
    context.browser.find_element_by_xpath("//a[contains(.,'Register')]").click()

@when('user fills out all required boxes')
def step_impl(context):
    context.browser.find_element_by_id("input-firstname").send_keys("Peter")
    context.browser.find_element_by_id("input-lastname").send_keys("Novak")
    context.browser.find_element_by_id("input-email").send_keys("testing@account.com")
    context.browser.find_element_by_id("input-telephone").send_keys("+421905123123")
    context.browser.find_element_by_id("input-address-1").send_keys("Brno 1")
    context.browser.find_element_by_id("input-city").send_keys("Brno")
    context.browser.find_element_by_id("input-postcode").send_keys("12345")
    context.browser.find_element_by_id("input-country").click()
    context.browser.find_element_by_css_selector("option:nth-child(240)").click()
    context.browser.find_element_by_id("input-zone").click()
    context.browser.find_element_by_css_selector("#input-zone > option:nth-child(42)").click()
    context.browser.find_element_by_id("input-password").send_keys("123456789")
    context.browser.find_element_by_id("input-confirm").send_keys("123456789")

@when('accepts terms of privacy policy')
def step_impl(context):
    context.browser.find_element_by_xpath("//input[@name='agree']").click()

@when('confirms registration')
def step_impl(context):
    context.browser.find_element_by_css_selector(".btn-primary").click()

@then('user is registrated')
def step_impl(context):
    text = context.browser.find_element_by_xpath("//h1[contains(.,'Your Account Has Been Created!')]").text
    assert("Your Account Has Been Created!" == text)

@when('user fills out invalid e-mail address')
def step_impl(context):
    context.browser.find_element_by_id("input-email").send_keys("asdadasd@a")

@when('fills out the rest of required boxes(except e-mail)')
def step_impl(context):
    context.browser.find_element_by_id("input-firstname").send_keys("Peter")
    context.browser.find_element_by_id("input-lastname").send_keys("Novak")
    context.browser.find_element_by_id("input-telephone").send_keys("+421905123123")
    context.browser.find_element_by_id("input-address-1").send_keys("Brno 1")
    context.browser.find_element_by_id("input-city").send_keys("Brno")
    context.browser.find_element_by_id("input-postcode").send_keys("12345")
    context.browser.find_element_by_id("input-country").click()
    context.browser.find_element_by_css_selector("option:nth-child(240)").click()
    context.browser.find_element_by_id("input-zone").click()
    context.browser.find_element_by_css_selector("#input-zone > option:nth-child(42)").click()
    context.browser.find_element_by_id("input-password").send_keys("asdfgh")
    context.browser.find_element_by_id("input-confirm").send_keys("asdfgh")

@then('user is not registrated')
def step_impl(context):
    text = context.browser.find_element_by_xpath("//h1[contains(.,'Register Account')]").text
    assert("Register Account" == text)

@when('does not accept terms of privacy policy')
def step_impl(context):
    context.browser.find_element_by_xpath("//input[@name='agree']").click()
    context.browser.find_element_by_xpath("//input[@name='agree']").click()

@when('user does not fill out required box')
def step_impl(context):
    context.browser.find_element_by_id("input-firstname").clear()

@when('user fills out password box')
def step_impl(context):
    context.browser.find_element_by_id("input-password").send_keys("pwpwpw1")

@when('user fills out box where he should reenter password with different value')
def step_impl(context):
    context.browser.find_element_by_id("input-confirm").send_keys("pwpwpw2")

@when('user fills out the rest of required boxes(except passwords)')
def step_impl(context):
    context.browser.find_element_by_id("input-firstname").send_keys("Peter")
    context.browser.find_element_by_id("input-lastname").send_keys("Novak")
    context.browser.find_element_by_id("input-email").send_keys("test@mail.com")
    context.browser.find_element_by_id("input-telephone").send_keys("+421905123123")
    context.browser.find_element_by_id("input-address-1").send_keys("Brno 1")
    context.browser.find_element_by_id("input-city").send_keys("Brno")
    context.browser.find_element_by_id("input-postcode").send_keys("12345")
    context.browser.find_element_by_id("input-country").click()
    context.browser.find_element_by_css_selector("option:nth-child(240)").click()
    context.browser.find_element_by_id("input-zone").click()
    context.browser.find_element_by_css_selector("#input-zone > option:nth-child(42)").click()
