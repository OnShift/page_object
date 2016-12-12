Feature: Text Area Element

    Background:
      Given I am on the static elements page

    Scenario: Setting and getting a value from a text area
      When I type "abcdefghijklmnop" into the text area
      Then the text area should contain "abcdefghijklmnop"

    Scenario Outline: Locating text area on the Page
      When I search for the text area by "<search_by>"
      Then I should be able to type "I found it" into the area
    Examples:
      | search_by |
      | id        |
      | class     |
      | css       |

    Scenario: Clearing the text area
      When I type "abcdefghijklmnop" into the text area
      Then the text area should contain "abcdefghijklmnop"
      When I clear the text area
      Then the text area should contain " "
