Feature: Label Element

    Background:
        Given I am on the static elements page

    Scenario: Getting the text from a label
        When I get the text from the label
        Then the text should be "page-object is the best!"

    Scenario Outline: Locating labels on the page
        When I search for the label by "<search_by>"
        Then the text should be "page-object is the best!"

    Examples:
        | search_by |
        | id        |
        | class     |
        | css       |
