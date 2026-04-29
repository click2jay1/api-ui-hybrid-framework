

# API & UI Hybrid Automation Framework

## Project Overview
This repository contains a Hybrid Test Automation Framework designed to demonstrate full-stack Quality Assurance capabilities. It combines Selenium WebDriver for end-to-end UI testing and the Requests library for REST API validation, all orchestrated by the Pytest framework.

The goal of this project is to showcase how to validate data consistency between the backend services and the frontend user interface.


## Key Features
- Page Object Model (POM): Enhances code maintainability and reduces duplication in UI tests.
- Service-Oriented API Layer: Abstracted API client for clean, reusable request handling.
- Unified Reporting: Integrated HTML reports showing results for both UI and API suites.
- Cross-Browser Support: Configured for easy switching between Chrome, Firefox, and Edge.
- CI/CD Ready: Prepared for GitHub Actions integration.

## Tech Stack
- Language: Python
- Test Runner: Pytest
- UI Automation: Selenium WebDriver
- API Testing: Requests
- Reporting: Pytest-HTML / Allure

## Folder Structure
```text
api-ui-hybrid-framework
├── tests/
│   ├── api/            # REST API test cases
│   └── gui/            # Selenium UI test cases
│        
├── pages/              # Page Object Model (UI elements & actions)
├── utils/              # API Clients and helper methods
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation
└── conftest.py         # Global fixtures and setup
```

## How to Run
**1. Installation**
Clone the repository and install the dependencies:

```text
git clone https://github.com/your-username/api-ui-hybrid-framework.git
cd api-ui-hybrid-framework
pip install -r requirements.txt
```

**2. Running Tests**
To run all tests (API and UI) and generate a report:

```text
pytest --html=report.html
```
To run only API tests:
```text
pytest tests/api/
```

To run only UI tests:
```text
pytest tests/gui/
```

# Why a Hybrid Framework?
In modern software development, testing the UI alone is slow, and testing the API alone misses visual regressions. This hybrid approach allows for:
- Speed: Using API calls to "setup" data before running a UI test.
- Accuracy: Verifying that a "Success" message on the UI actually corresponds to a 201 Created status in the database.

## Author
**Jay Raj Prakash**
```text
ISTQB Advanced Level (CTAL-TAE) Certified
📧 jayrajprakash@outlook.com
🔗 [GitHub Profile](https://github.com/click2jay1)
📍 Greater Seattle Area, WA
```
