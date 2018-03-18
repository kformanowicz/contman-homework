Feature: Contact Page

    Scenario: Phone number on contact page
    Given I am on home page
    When I click on "Contact" tab
    Then "Contact" page is opened
    And Phone number is displayed
    And Phone number is correct