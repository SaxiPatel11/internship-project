Feature: Change Password

  Scenario: User can open change password page
    Given User opens Reelly login page
    When User logs in
    And User clicks Settings option
    And User clicks Change Password option
    Then Verify Change Password page opens
    And User enters test passwords
    And Verify Change Password button is displayed