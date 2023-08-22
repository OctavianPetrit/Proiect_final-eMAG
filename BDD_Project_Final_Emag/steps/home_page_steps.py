from behave import *

@given('Home Page: I am on eMAG homepage')
def step_impl(context):
    context.home_page_object.navigate_to_home_page()

@then('Home Page: Verify that the eMAG logo is present')
def step_impl(context):
    context.home_page_object.emag_logo()

@when('Home Page: I search for "{product_name}"')
def step_impl(context,product_name):
    context.home_page_object.set_product_search(product_name)
    context.home_page_object.click_search_button()

@when('Home Page: I search "{product}" in "{category}"')
def step_impl(context,product,category):
    context.home_page_object.choose_category(category)
    context.home_page_object.set_product_search(product)
    context.home_page_object.click_search_button()

@then ('Home Page: I have at least "{number_of_results}" results returned')
def step_impl(context, number_of_results):
    context.home_page_object.search_results(number_of_results)

@when('Home Page: I add product to basket')
def step_impl(context):
    context.product_page.add_to_cart()

  # @TC6_remove_product
@then('Home Page: I verify that I have the product in my cart')
def step_impl(context):
    context.home_page_object.navigate_to_home_page()
    context.home_page_object.click_cart_button()

@when('Home Page: I delete the product')
def step_impl(context):
    context.home_page_object.remove_from_cart()
#
# @then('Home Page: I start shopping again')
# def step_impl(context):
#     context.home_page_object.continue_shop()




