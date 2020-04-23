from behave import *

@given('administrator is at Analytics page')
def step_impl(context):
    context.browser.get("http://mys01.fit.vutbr.cz:8055/admin/")
    context.browser.find_element_by_xpath("//input[@id='input-username']").send_keys("admin")
    context.browser.find_element_by_xpath("//input[@id='input-password']").send_keys("admin")

    context.browser.find_element_by_xpath("//button[@type='submit']").click()

    context.browser.find_element_by_id("button-menu").click()
    context.browser.find_element_by_xpath("//li[@id='extension']/a").click()
    context.browser.find_element_by_xpath("//a[contains(text(),'Analytics')]").click()

@given('Google Analytics is in the list')
def step_impl(context):
    text = context.browser.find_element_by_css_selector("h1").text
    context.browser.find_element_by_xpath("//b")

@when('administrator starts editing the Google Analytics extension')
def step_impl(context):
    try:
        context.browser.find_element_by_css_selector(".btn-primary").click()
    except :
        context.browser.find_element_by_css_selector(".btn").click()
        context.browser.find_element_by_css_selector(".btn-primary").click()

@when('administrator fills out the code')
def step_impl(context):
    context.browser.find_element_by_id("input-code").send_keys(
    "<script> ga(\'create\', \'UA-XXXXX-Y\', \'auto\'); ga(\'send\', \'pageview\'); </script>")

@when('administrator sets status of extension')
def step_impl(context):
    context.browser.find_element_by_id("input-status").click()
    context.browser.find_element_by_xpath("//option[@value='1']").click()

@when('administrator saves changes')
def step_impl(context):
    try:
        context.browser.find_element_by_xpath("//button[@type='submit']").click()
    except:
        context.browser.find_element_by_css_selector(".btn-primary").click()

@then('administrator is back at Analytics page')
def step_impl(context):
    text = context.browser.find_element_by_css_selector("h1").text
    assert(text == "Analytics")

@then('Google Analytics extension is modifed')
def step_impl(context):
    text = context.browser.find_element_by_css_selector("tr:nth-child(2) > .text-left:nth-child(2)").text
    assert(text == "Enabled")

@given('administrator is at Captcha page')
def step_impl(context):
    context.browser.get("http://mys01.fit.vutbr.cz:8055/admin/")
    context.browser.find_element_by_xpath("//input[@id='input-username']").send_keys("admin")
    context.browser.find_element_by_xpath("//input[@id='input-password']").send_keys("admin")

    context.browser.find_element_by_xpath("//button[@type='submit']").click()

    context.browser.find_element_by_id("button-menu").click()
    context.browser.find_element_by_xpath("//li[@id='extension']/a").click()
    context.browser.find_element_by_xpath("//a[contains(text(),'Captcha')]").click()

@given('{captcha} is not installed')
def step_impl(context, captcha):
    captcha = captcha[1:-1]

    text = context.browser.find_element_by_css_selector("tbody > tr:nth-child(1) > .text-left:nth-child(1)").text

    if(text == captcha):
        context.browser.find_element_by_css_selector("tr:nth-child(1) .btn-success")
    else:
        text = context.browser.find_element_by_css_selector("tr:nth-child(2) > .text-left:nth-child(1)").text
        if(text == captcha):
            context.browser.find_element_by_css_selector("tr:nth-child(2) .btn-success")

@when('administrator installs {captcha}')
def step_impl(context, captcha):
    captcha = captcha[1:-1]

    text = context.browser.find_element_by_css_selector("tbody > tr:nth-child(1) > .text-left:nth-child(1)").text


    if(text == captcha):
        context.browser.find_element_by_css_selector("tr:nth-child(1) .btn-success").click()
    else:
        text = context.browser.find_element_by_css_selector("tr:nth-child(2) > .text-left:nth-child(1)").text
        if(text == captcha):
            context.browser.find_element_by_css_selector("tr:nth-child(2) .btn-success").click()

@when('administrator starts editing {captcha}')
def step_impl(context, captcha):
    captcha = captcha[1:-1]

    text = context.browser.find_element_by_css_selector("tbody > tr:nth-child(1) > .text-left:nth-child(1)").text
    if(text == captcha):
        context.browser.find_element_by_css_selector("tr:nth-child(1) .btn-primary > .fa").click()
    else:
        text = context.browser.find_element_by_css_selector("tr:nth-child(2) > .text-left:nth-child(1)").text
        if(text == captcha):
            context.browser.find_element_by_css_selector("tr:nth-child(2) .btn-primary").click()

@when('administrator sets status to Enabled')
def step_impl(context):
    try:
        context.browser.find_element_by_id("input-key").send_keys("blahblah")
        context.browser.find_element_by_id("input-secret").send_keys("blahblah")
        context.browser.find_element_by_id("input-status").click()
        context.browser.find_element_by_xpath("//option[@value='1']").click()
    except:
        context.browser.find_element_by_id("input-status").click()
        context.browser.find_element_by_xpath("//option[@value='1']").click()

@then('administrator is back at Captcha page')
def step_impl(context):
    text = context.browser.find_element_by_css_selector("h1").text
    assert(text == "Captchas")

@then('{captcha} is installed')
def step_impl(context, captcha):
    captcha = captcha[1:-1]

    text = context.browser.find_element_by_css_selector("tbody > tr:nth-child(1) > .text-left:nth-child(1)").text

    if(text == captcha):
        context.browser.find_element_by_css_selector("tr:nth-child(1) .btn-danger")
    else:
        text = context.browser.find_element_by_css_selector("tr:nth-child(2) > .text-left:nth-child(1)").text
        if(text == captcha):
            context.browser.find_element_by_css_selector("tr:nth-child(2) .btn-danger")

@then('{captcha} is enabled')
def step_impl(context, captcha):
    captcha = captcha[1:-1]

    text = context.browser.find_element_by_css_selector("tbody > tr:nth-child(1) > .text-left:nth-child(1)").text

    if(text == captcha):
        status = context.browser.find_element_by_css_selector("tbody > tr:nth-child(1) > .text-left:nth-child(2)").text
        assert(status == "Enabled")
    else:
        text = context.browser.find_element_by_css_selector("tr:nth-child(2) > .text-left:nth-child(1)").text
        if(text == captcha):
            status = context.browser.find_element_by_css_selector("tr:nth-child(2) > .text-left:nth-child(2)").text
            assert(status == "Enabled")
