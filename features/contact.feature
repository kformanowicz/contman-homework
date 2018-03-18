Feature: Contact Page

  Scenario: Phone and fax numbers on contact page
    Given I am on home page
    When I click on "Contact" tab
    Then "Contact" page is opened
    And Phone number is displayed
    And Phone number is correct
    And Fax number is displayed
    And Fax number is correct