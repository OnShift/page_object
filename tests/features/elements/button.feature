Feature: Button Element
  In order to interact with buttons
  Testers will need access and interrogation ability


    Background:
        Given I am on the static elements page

    Scenario: Clicking a button
        When I click the button
        Then I should be on the success page

    Scenario Outline: Locating buttons on the page
        When I search for the button by "<search_by>"
        Then I should be able to click the button
    Examples:
        | search_by |
        | id        |
        | class     |
        | css       |
