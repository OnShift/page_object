Feature: TextField Element

    Background:
        Given I am on the static elements page

    Scenario: Clear an element
        When I type "abcDEF" into the text field
        Then the text field should contain "abcDEF"
        When I clear the text field
        Then the text field should contain " "
