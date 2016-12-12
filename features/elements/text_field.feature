Feature: TextField Element

  Background:
    Given I am on the static elements page

  Scenario: Setting and getting a value from a text field
    When I type "abcDEF" into the text field
    Then the text field should contain "abcDEF"

  Scenario: Clear text field vlaue
    When I type "abcDEF" into the text field
    Then the text field should contain "abcDEF"
    When I clear the text field
    Then the text field should contain " "

  Scenario Outline: Locating text fields on the Page
    When I search for the text field by "<search_by>"
    Then I should be able to type "I found it" into the field
  Examples:
    | search_by  |
    | id         |
    | class      |
    | css        |
