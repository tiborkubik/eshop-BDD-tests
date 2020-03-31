# Feature contains scenarios about actions performed on shopping cart like adding, removing, etc.
Feature: Shopping cart


    Scenario Outline: Adding an item to Shopping Cart
        Given browser is at "<item>" product page
        When user adds "<item>" to Shopping Cart
        Then "<item>" is in Shopping Cart

        Examples:
            |     item      |
            |   HP LP3065   |
            | Palm Treo Pro |
            

    Scenario Outline: Item quantity change
        Given browser is at Shopping Cart's page
        And "<item>" is in Shopping Cart
        When the quantity of "<item>" is changed to 42
        Then user has in his Shopping Cart 42 pieces of "<item>"

        Examples:
            |    item    |
            |   iPhone   |
            | Nikon D300 |


    Scenario Outline: Deleting an item from Shopping Cart
        Given browser is at Shopping Cart's page
        And "<item>" is in Shopping Cart
        When user deletes "<item>" from Shopping Cart
        Then "<item>" is no longer in the Cart

        Examples:
            |     item     |
            | Canon EOS 5D |
            | iPod Shuffle |


    Scenario Outline: Deleting an only item
        Given browser is at Shopping Cart's page
        And "<item>" is in Shopping Cart
        And there is nothing else in Shopping Cart
        When user deletes "<item>" from Shopping Cart
        Then Shopping Cart is empty

        Examples:
            |           item           |
            |        iPod Touch        |
            | Samsung SyncMaster 941BW |
