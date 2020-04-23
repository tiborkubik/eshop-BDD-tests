from behave import *


@given('user is logged in')
def step_impl(context):
    context.browser.get("http://mys01.fit.vutbr.cz:8055/")

    context.browser.find_element_by_xpath("//span[contains(.,'My Account')]").click()
    context.browser.find_element_by_xpath("//a[contains(.,'Login')]").click()
    context.browser.find_element_by_id("input-email").send_keys("testing@account.com")
    context.browser.find_element_by_id("input-password").send_keys("123456789")
    context.browser.find_element_by_xpath("//input[@value='Login']").click()


@given('user is at {item}\'s product page')
def step_impl(context, item):
    if(item == str("\"HTC Touch HD\"")):
        context.browser.get("http://mys01.fit.vutbr.cz:8055/index.php?route=product/product&path=24&product_id=28")

    if(item == str("\"iMac\"")):
        context.browser.get("http://mys01.fit.vutbr.cz:8055/index.php?route=product/product&path=20_27&product_id=41")


@when('user adds {item} into his Wish List')
def step_impl(context, item):
    context.browser.find_element_by_xpath("//div[2]/div/button/i").click()


@then('{item} is in user\'s Wish List')
def step_impl(context, item):
    context.browser.find_element_by_css_selector("#wishlist-total > .hidden-xs").click()
    strItem = str(item)
    strItem = strItem[1:-1]

    if(item == str("\"HTC Touch HD\"")):
        text = context.browser.find_element_by_xpath("//a[contains(text(),'HTC Touch HD')]").text
    if(item == str("\"iMac\"")):
        text = context.browser.find_element_by_xpath("//a[contains(text(),'iMac')]").text

    assert(text == strItem)
    context.browser.find_element_by_css_selector(".btn-danger:nth-child(2)").click()


@given('user is at Wish List page')
def step_impl(context):
    context.browser.get("http://mys01.fit.vutbr.cz:8055/index.php?route=account/wishlist")


@given('{item} is in user\'s Wish List')
def step_impl(context, item):
    if(item == str("\"Samsung SyncMaster 941BW\"")):
        context.browser.get("http://mys01.fit.vutbr.cz:8055/index.php?route=product/product&path=25_28&product_id=33")
        context.browser.find_element_by_xpath("//div[2]/div/button/i").click()

    if(item == str("\"Apple Cinema 30\"\"")):
        context.browser.get("http://mys01.fit.vutbr.cz:8055/index.php?route=product/product&path=25_28&product_id=42")
        context.browser.find_element_by_xpath("//div[2]/div/button/i").click()

    context.browser.get("http://mys01.fit.vutbr.cz:8055/index.php?route=account/wishlist")


@when('user clicks on {item}\'s product name')
def step_impl(context, item):
    if(item == str("\"Samsung SyncMaster 941BW\"")):
        context.browser.find_element_by_xpath("//a[contains(text(),\'Samsung SyncMaster 941BW\')]").click()

    if(item == str("\"Apple Cinema 30\"\"")):
        context.browser.find_element_by_xpath("//a[contains(text(),\'Apple Cinema 30\"\')]").click()


@then('{item}\'s product page shows up')
def step_impl(context, item):
    if(item == str("\"Samsung SyncMaster 941BW\"")):
        text = context.browser.find_element_by_xpath("//h1[contains(text(),\'Samsung SyncMaster 941BW\')]").text

    if(item == str("\"Apple Cinema 30\"\"")):
        text = context.browser.find_element_by_xpath("//h1[contains(text(),\'Apple Cinema 30\"\')]").text

    strItem = str(item)
    strItem = strItem[1:-1]

    assert(text == strItem)


@when('user adds {item} to his Shopping Cart')
def step_impl(context, item):
    if(item == str("\"Samsung SyncMaster 941BW\"")):
        context.browser.find_element_by_css_selector("tr:nth-child(1) .btn-primary > .fa").click()
        text = context.browser.find_element_by_css_selector(".alert").text
        text = text.split(' ', 1)
        assert("Success:" == text[0])


@then('{item} is in Shopping Cart')
def step_impl(context, item):
    if(item == str("\"Samsung SyncMaster 941BW\"")):
        context.browser.find_element_by_id("cart-total").click()
        text = context.browser.find_element_by_xpath("//a[contains(text(),'Samsung SyncMaster 941BW')]").text

        assert("Samsung SyncMaster 941BW" == text)

    if(item == str("\"HP LP3065\"")):
        context.browser.find_element_by_xpath("//div[@id='cart']/button").click()

        text = context.browser.find_element_by_xpath("//a[contains(text(),'HP LP3065')]").text
        assert(text == "HP LP3065")

    if(item == str("\"Palm Treo Pro\"")):
        context.browser.find_element_by_xpath("//div[@id='cart']/button").click()

        text = context.browser.find_element_by_xpath("//a[contains(text(),'Palm Treo Pro')]").text
        assert(text == "Palm Treo Pro")


@when('user removes {item} from his Wish List')
def step_impl(context, item):
    if(item == str("\"Samsung SyncMaster 941BW\"")):
        context.browser.find_element_by_css_selector("tr:nth-child(1) > .text-right > .btn-danger").click()
    if(item == str("\"Apple Cinema 30\"\"")):
        context.browser.find_element_by_css_selector(".btn-danger:nth-child(2)").click()

@then('Wish List no longer contains {item}')
def step_impl(context, item):
    if(item == str("\"Samsung SyncMaster 941BW\"")):
        text = context.browser.find_element_by_xpath("//div/table/tbody/tr/td[2]/a").text
        assert(text != "Samsung SyncMaster 941BW")

    if(item == str("\"Apple Cinema 30\"\"")):
        text = context.browser.find_element_by_css_selector("#content > p").text
        print(text)
        assert(text != "Your wish list is empty.")
