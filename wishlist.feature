# This feature contains scenarios describing actions with wishlist like adding, deleting, moving to cart etc.
Feature: Wishlist


    Scenario Outline: Adding an item into a Wish List
        Given user is at "<item>"'s product page
        And user is logged in
        When user adds "<item>" into his Wish List
        Then "<item>" is in user's Wish List

        Examples:
            |     item     |
            | HTC Touch HD |
            |     iMac     |


    Scenario Outline: Visiting item's product page from Wish List
        Given user is at Wish List page
        And user is logged in
        And "<item>" is in user's Wish List
        When user clicks on "<item>"'s product name
        Then "<item>"'s product page shows up

        Examples:
            |           item           |
            | Samsung SyncMaster 941BW |
            |     Apple Cinema 30"     |


    Scenario Outline: Adding an item from Wish List to Shopping Cart
        Given user is at Wish List page
        And user is logged in
        And "<item>" is in user's Wish List
        When user adds "<item>" to his Shopping Cart
        Then "<item>" is in Shopping Cart

        Examples:
            |           item           |
            | Samsung SyncMaster 941BW |
            |         Sony VAIO        |
            

    Scenario Outline: Removing an item from Wish List
        Given user is at Wish List page
        And user is logged in
        And "<item>" is in user's Wish List
        When user removes "<item>" from his Wish List
        Then Wish List no longer contains "<item>"

        Examples:
            |           item          |
            |       MacBook Air       |
            | Samsung Galaxy Tab 10.1 |
