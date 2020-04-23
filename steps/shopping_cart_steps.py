from behave import *

@given('browser is at {item} product page')
def step_impl(context, item):
    if(item == str("\"HP LP3065\"")):
        context.browser.get("http://mys01.fit.vutbr.cz:8055/index.php?route=product/product&path=18&product_id=47")

    if(item == str("\"Palm Treo Pro\"")):
        context.browser.get("http://mys01.fit.vutbr.cz:8055/index.php?route=product/product&path=24&product_id=29")

@when('user adds {item} to Shopping Cart')
def step_impl(context, item):
    context.browser.find_element_by_id("button-cart").click()

@given('browser is at Shopping Cart\'s page')
def step_impl(context):
    context.browser.get("http://mys01.fit.vutbr.cz:8055/index.php?route=checkout/cart")

@given('{item} is in Shopping Cart')
def step_impl(context, item):
    if(item == str("\"iPhone\"")):
        context.browser.get("http://mys01.fit.vutbr.cz:8055/index.php?route=product/product&product_id=40")
        context.browser.find_element_by_id("button-cart").click()
        context.browser.find_element_by_xpath("//div[@id='cart']/button").click()
        text = context.browser.find_element_by_xpath("//a[contains(text(),\'iPhone\')]").text
        context.browser.get("http://mys01.fit.vutbr.cz:8055/index.php?route=checkout/cart")

        assert(text == "iPhone")

    if(item == str("\"Nikon D300\"")):
        context.browser.get("http://mys01.fit.vutbr.cz:8055/index.php?route=product/product&path=33&product_id=31")
        context.browser.find_element_by_id("button-cart").click()
        context.browser.find_element_by_xpath("//div[@id='cart']/button").click()
        text = context.browser.find_element_by_xpath("//a[contains(text(),\'Nikon D300\')]").text
        context.browser.get("http://mys01.fit.vutbr.cz:8055/index.php?route=checkout/cart")

        assert(text == "Nikon D300")

@when('the quantity of {item} is changed to 42')
def step_impl(context, item):
    if(item == str("\"iPhone\"")):
        context.browser.find_element_by_css_selector(".btn-block > .form-control").clear()
        context.browser.find_element_by_css_selector(".btn-block > .form-control").send_keys("42")
        context.browser.find_element_by_css_selector(".btn-block .btn-primary").click()

    if(item == str("\"Nikon D300\"")):
        context.browser.find_element_by_css_selector("tr:nth-child(1) .form-control").clear()
        context.browser.find_element_by_css_selector("tr:nth-child(1) .form-control").send_keys("42")
        context.browser.find_element_by_css_selector("tr:nth-child(1) .btn-primary").click()

@then('user has in his Shopping Cart 42 pieces of {item}')
def step_impl(context, item):
    if(item == str("\"iPhone\"")):
        unitPrice = context.browser.find_element_by_css_selector("tbody .text-right:nth-child(5)").text
        wholePrice = context.browser.find_element_by_css_selector("tbody .text-right:nth-child(6)").text

    if(item == str("\"Nikon D300\"")):
        unitPrice = context.browser.find_element_by_css_selector("tbody > tr:nth-child(1) > .text-right:nth-child(5)").text
        wholePrice = context.browser.find_element_by_css_selector("tbody > tr:nth-child(1) > .text-right:nth-child(6)").text

    unitPrice = unitPrice[1:]
    wholePrice = wholePrice[1:]
    wholePrice = wholePrice.replace(",", "")
    wholePrice = str(wholePrice)
    wholePrice = wholePrice.split(".")[0]
    expectedPrice = float(unitPrice) * 42
    expectedPrice = str(expectedPrice)
    expectedPrice = expectedPrice.split(".")[0]
    print(unitPrice, " --- ", expectedPrice, " --- ", wholePrice)
    assert(expectedPrice == wholePrice)

@when('user deletes {item} from Shopping Cart')
def step_impl(context, item):
    context.browser.find_element_by_css_selector(".btn-danger:nth-child(2)").click()

@then('{item} is no longer in the Cart')
def step_impl(context, item):
    text = context.browser.find_element_by_css_selector("p:nth-child(2)").text

    assert(text == "Your shopping cart is empty!")
    
