Feature: Paragraph Element

  Background:
    Given I am on the static elements page

  Scenario: Getting the text from a paragraph
    When I get the text from the paragraph
    Then the text should be "Static Elements Page"

  Scenario Outline: Locating divs on the page
    When I search for the paragraph by "<search_by>"
    Then the text should be "Static Elements Page"
  Examples:
    | search_by |
    | id        |
    | class     |
    | tag       |
    | css       |
