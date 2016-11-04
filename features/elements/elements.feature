Feature: Generic Element Behavior

  Background:
    Given I am on the static elements page

  Scenario: Elements enabled?
    When I check an enabled button
    Then it should know it is enabled
    And it should know that is it not disabled
    When I check a disabled button
    Then it should know it is not enabled
    And it should know that it is disabled
