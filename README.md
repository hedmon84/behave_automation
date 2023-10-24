# Project Name (Behave_automation)

This repository contains automated tests for both UI and API. The UI tests cover login/logout functionalities of the [SauceDemo website](https://www.saucedemo.com/), and the API tests are designed for the [WeatherAPI](https://www.weatherapi.com/).

## Folder Structure

```
Project Name
│
├── api_tests                   # Contains API test features and step definitions
│   ├── features                # Gherkin feature files for API tests
│   └── steps                   # Step definition files for API tests
│
├── ui_tests                    # Contains UI test features and step definitions
│   ├── features                # Gherkin feature files for UI tests
│   └── steps                   # Step definition files for UI tests
│
├── drivers                     # Contains web drivers for different browsers
│
└── README.md                   # The description file for the project
```

## Prerequisites

- Python 3.x
- Behave (Python package)
- Selenium WebDriver (Python package)
- Requests (Python package)
- A web browser (e.g., Chrome, Firefox)
- Web drivers (e.g., ChromeDriver for Chrome, geckodriver for Firefox)

Please ensure that the web drivers are compatible with the version of the browser you are using.

## Setup

1. Clone the repository to your local machine.

   ```bash
   git clone https://github.com/your_username/your_repository.git
   ```

2. Navigate to the cloned directory.

   ```bash
   cd your_repository
   ```

3. Install the required Python packages.


   ```bash
   pip install behave selenium requests
   pip install requests
   pip install behave
   pip install selenium
   pip install webdriver-manager
   pip install assertpy
   ```



4. Update the `drivers` path in your system/environment variables or in your test scripts to point to the location of the web drivers in the `drivers` folder.

## Running the Tests

You can run tests from the command line by navigating to the root directory of the project and using the `behave` command. You can specify a particular directory (for UI or API tests) using `-i` or `--include` flag followed by the directory name.

### Running UI Tests

```bash
behave ui_tests/features
```

### Running API Tests

```bash
behave api_tests/features
```

## Reporting

Behave can generate reports after test execution. To generate a simple report after running your tests, you can use the `-f` or `--format` flag with the `plain` value, and the `-o` or `--outfile` flag to specify the output file.

```bash
behave -f plain -o report.txt ui_tests/features
```
