Feature: Select List Element

Background:
    Given I am on the static elements page

    Scenario: Selecting an element on the select list
        When I select "Test 2" from the select list
        Then the current item should be "Test 2"

    Scenario Outline: Locating select lists on the Page
        When I search for the select list by "<search_by>"
        Then I should be able to select "Test 2"
        And the text for the selected item should be "Test 2"
        And the value for the option should be "option2"
    Examples:
      | search_by |
      | id        |
      | css       |
      | class     |
      | tag       |

    Scenario: Iterating through the options in the select list
        When I search for the select list by "id"
        Then option "1" should contain "Test 1"
        And option "2" should contain "Test 2"
        And each option should contain "Test"
