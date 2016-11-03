Feature: Button Element

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

    Scenario: Finding a button dynamically
       When I find a button while the script is executing
       Then I should see that the button exists
       And I should be able to click the button
