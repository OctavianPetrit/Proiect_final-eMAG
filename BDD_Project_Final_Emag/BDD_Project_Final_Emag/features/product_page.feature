Feature: Testing scenarios on eMAG.ro
  Scenario: Verify that the product is present in the shopping cart by the name
    When products: I add product to basket "{product_name}"
    When products: I click Vezi detalii cos
    Then products: I verify that results contain search query "{query}"