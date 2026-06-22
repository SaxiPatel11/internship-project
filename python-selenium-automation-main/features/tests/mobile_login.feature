Feature: Mobile Web Login Test

  Scenario: User can log in on mobile web
    Given User opens Reelly login page on mobile
    When User enters email and password
    And User clicks Login button
    Then User should be logged in successfully