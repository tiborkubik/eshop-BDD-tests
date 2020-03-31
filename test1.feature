Feature: User registration and logging

  Scenario: Successful account registration
      Given User is not registrated yet
      And is on registration page
      When User fills out all required boxes
      And accepts terms of privacy policy
      And confirms registration
      Then User is registrated

  Scenario: Unsuccessful account registration - terms not accepted
      Given User is not registrated yet
      And is on registration page
      When User fills out all required boxes
      And does not accept terms of privacy policy
      And confirms registration
      Then User is not registrated

  Scenario: Unsuccessful account registration - required box not filled out
      Given User is not registrated yet
      And is on registration page
      When User does not fill out required box
      And accepts terms of privacy policy
      And confirms registration
      Then User is not registrated

  Scenario: Unsuccessful account registration - passwords do not match
      Given User is not registrated yet
      And is on registration page
      When User fills out password box
      And user fills out box where he should reenter password
      And these passwords do not match
      And user fills out the rest of required boxes
      And confirms registration
      Then User is not registrated
