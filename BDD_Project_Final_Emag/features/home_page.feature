Feature: Testing scenarios on eMAG.ro
  Background:
    Given Home Page: I am on eMAG homepage
    Then Home Page: I have at least 2 results returned

  @T1
  Scenario: Verify the eMAG logo is present
    Given Home Page: I am on the eMAG home page
    Then Home Page: Verify that the eMAG logo is present


  @T2
  Scenario: Searching product on eMAG home page
    Given Home Page: I am on eMAG homepage
    When Home Page: I search "samsung galaxy z flip"
    Then Home Page: I have at least 50 results returned

  @T3 @parameter
  Scenario: Searching product on eMAG home page with parameter
    Given Home Page: I am on eMAG homepage1
    When Home Page: I search for "aspirator robot" in "Aspiratoare"
    Then Home Page: I have at least 500 results returned

  @T4 @outline, @parameter
  Scenario Outline: Searching product on eMAG home page with parameters
    Given Home Page: I am on eMAG homepage2
    When Home Page: I search for "<product_name>" in "<category_name>"
    Then Home Page: I have at least "<number_of_results>" results returned
    Examples:
      | product_name              | category_name        | number_of_results |  |
      | cauciucuri de vara        | Anvelope auto        | 10000             |  |
      | cor                       | Corturi camping      | 800               |  |
      | iphone 14 pro max         | Telefoane Mobile     | 90                |  |



######## Feature: Select Product and add to cart

  @TC5_select_product @shop
  Scenario: Add to cart one product
    Given Home Page: I am on eMAG homepage
    When Home Page: I have searched the "s23 ultra" product
    Then Home Page: I add product to basket

  @TC6_remove_product_negative_scenario_on_return_to_shop @shop
  Scenario: Remove the product from cart
    Given Home Page: I verify that I have the product in my cart
    When Home Page: I delete the product
    Then Home Page: I start shoping again