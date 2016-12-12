Feature: Image Element

  Background:
    Given I am on the static elements page

  Scenario: Getting the image element
    When I get the image element
    Then the image should be "106" pixels wide
    And the image should be "106" pixels tall

  Scenario Outline: Locating an image on the page
    When I get the image element by "<search_by>"
    Then the image should be "106" pixels wide
    And the image should be "106" pixels tall
  Examples:
    | search_by |
    | id        |
    | class     |
    | css       |
