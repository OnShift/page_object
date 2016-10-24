Feature: Link Element

    Background:
        Given I am on the static elements page

    Scenario: Selecting a link
        When I select the link labeled "Google Search"
        Then I should be on the success page

    Scenario Outline: Locating links on the Page
        When I search for the link by "<search_by>"
        Then I should be able to select the link

    Examples:
        | search_by |
        | id        |
        | class     |
        | css       |
        | tag       |
