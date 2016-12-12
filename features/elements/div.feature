Feature: Div Element

  Background:
    Given I am on the static elements page

  Scenario: Getting the text from a div
    When I get the text from the div
    Then the text should be "page-object rocks!"

  Scenario Outline: Locating divs on the page
    When I search for the div by "<search_by>"
    Then the text should be "page-object rocks!"
  Examples:
      | search_by |
      | id        |
      | class     |
      | tag       |
      | css       |
