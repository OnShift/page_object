Feature: Async Elements

    Background:
      Given I am on the async elements page

    Scenario: Wait for an element to be enabled
      Given I disable the button
      When I enable the button
      Then I should be able to wait for the button to be enabled

    Scenario: Wait for an element to be present
      When I create a new button
      Then I should be able to wait for the button to be present
