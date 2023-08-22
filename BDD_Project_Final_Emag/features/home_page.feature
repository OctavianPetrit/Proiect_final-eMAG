Feature: Testing scenarios on eMAG.ro
  Background:
    Given Home Page: I am on eMAG homepage

  @T1
  Scenario: Verify the eMAG logo is present
    Then Home Page: Verify that the eMAG logo is present

  @T2
  Scenario: Searching product on eMAG home page
    When Home Page: I search for "samsung galaxy z flip"
    Then Home Page: I have at least "50" results returned

  @T3 @outline, @parameter
  Scenario Outline: Searching product on eMAG home page with parameters
    When Home Page: I search "<product_name>" in "<category_name>"
    Then Home Page: I have at least "<number_of_results>" results returned
    Examples:
      | product_name       | category_name                   | number_of_results |  |  |
      | cauciucuri de vara | Auto, Moto  & RCA               | 10000             |  |  |
      | corturi            | Sport & Activitati in aer liber | 10                |  |  |
      | iphone 14 pro max  | Laptop, Tablete & Telefoane     | 90                |  |  |

  @TC5_select_product @shop
  Scenario: Add to cart one product
    When Home Page: I search for "s23 ultra"
    And Home Page: I add product to basket
    When I click on the shopping cart
    Then Home Page: I verify that I have the product in my cart

  @TC6_remove_product_negative_scenario_on_return_to_shop @shop
  Scenario: Remove the product from cart
    When Home Page: I search for "s23 ultra"
    And Home Page: I add product to basket
    When I click on the shopping cart
    And Home Page: I delete the product
    Then Home Page: The product is removed from the shopping cart