# Feature contains scenarios describing several situations when a new user is registrated
Feature: User registration


    Scenario: Successful account registration
        Given user is on registration page
        When user fills out all required boxes
        And accepts terms of privacy policy
        And confirms registration
        Then user is registrated


    Scenario: Unsuccessful account registration - e-mail is invalid
        Given user is on registration page
        When user fills out invalid e-mail address
        And fills out the rest of required boxes
        And accepts terms of privacy policy
        And confirms registration
        Then user is not registrated


    Scenario: Unsuccessful account registration - terms not accepted
        Given user is on registration page
        When user fills out all required boxes
        And does not accept terms of privacy policy
        And confirms registration
        Then user is not registrated


    Scenario: Unsuccessful account registration - required box not filled out
        Given user is on registration page
        When user does not fill out required box
        And accepts terms of privacy policy
        And confirms registration
        Then user is not registrated
        

    Scenario: Unsuccessful account registration - passwords do not match
        Given user is on registration page
        When user fills out password box
        And user fills out box where he should reenter password
        And these passwords do not match
        And user fills out the rest of required boxes
        And confirms registration
        Then user is not registrated
