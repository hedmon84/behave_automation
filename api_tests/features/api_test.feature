Feature: WeatherAPI current weather information

  # Positive Scenario
  Scenario Outline: Get current weather information for various locations
    When I request current weather information for "<location>"
    Then the response status code should be 200
    And the response should contain "location" key
    And the "location" key should contain "name" equal to "<location>"

    Examples:
      | location  |
      | London    |
      | Paris     |
      | New York  |

# Negative Scenarios
Scenario Outline: Request current weather information for an invalid location
    When I request current weather information for a invalid "<location>"
    Then the response status code should be 400 or 404
    And the response should contain "error" key

    Examples:
    | location        |
    | InvalidLocation |

  Scenario: Request current weather information with missing API key
    When I request current weather information for "London" without API key
    Then the response status code should be 401 or 403
    And the response should contain "error" key







