# This feature tests actions within Admin Interface, specifically operations with Products Catalog
Feature: Admin Product Catalog


    Scenario Outline: Filter by name
        Given administrator is in product catalog
        When administrator fills out Product Name box with "<product>"
        Then "<product>" should be in product list

        Examples:
            |   product    |
            | iPod Classic |
            |  HP LP3065   |


    Scenario Outline: Filter by price
        Given administrator is in product catalog
        When administrator fills out Price box with "<prize>"
        Then only products which price is "<prize>" will be in product list

        Examples:
            | prize |
            |  100  |
            |   0   |


    Scenario Outline: Filter with zero results
        Given administrator is in product catalog
        When administrator sets status to "<status>"
        And all items have opposite status "<status2>"
        Then no products will be shown

        Examples:
          |  status  |  status2  |
          | Enabled  |  Disabled |
          | Disabled |  Enabled  |


    Scenario: Filter out of stock products
        Given administrator is in product catalog
        When administrator fills out quantity box with "0"
        Then only products which are out of stock are shown


    Scenario Outline: Edit product's name
        Given administrator is in product catalog
        And product catalog is not empty
        When administrator click on Edit button to edit "<product>"
        And administrator changes "<product>"' name to "<new_name>"
        And administrator saves changes
        Then administrator is again in product catalog
        And name of "<product>" is now called "<new_name>"

        Examples:
            |         product         |         new_name        |
            | Semseng Galaxy Tab 10.1 | Samsung Galaxy Tab 10.1 |
            |       ajfon fajf        |         iPhone 5        |


    Scenario Outline: Delete one product
        Given administrator is in product catalog
        And product catalog is not empty
        When administrator checks a checkbox next to "<product>"'s image
        And clicks on Delete button
        And confirms pop-up window by clicking on OK
        Then "<product>" is no longer in product catalog

        Examples:
            |   product  |
            | iPod Touch |
            |    iMac    |


    Scenario: Delete all products
        Given administrator is in product catalog
        And no filters are set
        When administrator checks the checkbox in product list header
        And clicks on Delete button
        And confirms pop-up window by clicking on OK
        Then product list ist empty
