Feature: Check Box Element

    Background:
        Given I am on the static elements page

    Scenario: Selecting a check box
        When I select the First check box
        Then the First check box should be selected
        When I unselect the First check box
        Then the First check box should not be selected

    Scenario Outline: Locating check boxes on the page
        When I search for the check box by "<search_by>"
        Then I should be able to check the check box

    Examples:
        | search_by |
        | id        |
        | class     |
        | css       |
