@ui
Feature: SauceLabs Demo Site Login and Logout

  Scenario Outline: Successful login with valid credentials
    Given a user navigates to the SauceLabs demo site
    When the user logs in with username "<username>" and password "<password>"
    Then the user should be redirected to the inventory page
    Examples:
      | username       | password     |
      | standard_user  | secret_sauce |

  Scenario Outline: Unsuccessful login with invalid credentials
    Given a user navigates to the SauceLabs demo site
    When the user logs in with username "<username>" and password "<password>"
    Then an error message "<error>" should be displayed
    Examples:
      | username       | password     | error                                  |
      | locked_out_user| secret_sauce | Epic sadface: Sorry, this user has been locked out. |
      |                |              | Epic sadface: Username is required     |
      | standard_user  |              | Epic sadface: Password is required     |
      | standard_user  | wrong_pass   | Epic sadface: Username and password do not match any user in this service |

  Scenario: Successful logout after valid login
    Given a user is logged in the SauceLabs demo site
    When the user clicks the logout button
    Then the user should be logged out and redirected to the home page

