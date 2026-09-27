# SUSPICIOUS URL ANALYZER

## Overview
Suspicious URL analyzer is a python-based, rule-driven project that examines URLs and identifies characteristics that may indicate suspicious or potentially unsafe links and generates a risk assessment.
It focuses on analyzing the structure and properties of a URL rather than interacting with the website behind the URL. The system checks with multiple indicators, gives the results using a rule-based approach,
and provides the user with a risk level associated with the URL along with the reasons for the assessment.

## Problem Statement
URLs are often encountered by people all over the world through emails, text messages, websites and social media platforms. Some of these URLs may contain suspicious characteristics that are not easily 
identifiable manually without technical knowledge. This project addresses this problem by developing a Python-based program that operates on a few predefined rules and helps determine if a given URL is potentially 
harmful, misleading or suspicious by providing a risk level assessment. However, a risk classification does not guarantee that a URL is safe or malicious.

## Objectives
The main objectives of this project are:
- To accept URL from the user
- To analyze the different structural characteristics of the provided URL
- To identify any suspicious characteristics in the URL using a set of predefined rules
- To calculate a risk score based on the detected indicators
- To show the risk level along with the reasons for the risk score
- To test the system by using different sample URLs

## Features
- URL input and validation: accepting and checking if the URL provided is valid.
- Extraction of features: extracting features from the URL.
- Analyzing the URL: Examine the URL against a set of predefined rules.
- Risk-score calculation: Calculating the level of risk associated with the URL.
- Risk-classification: Classifying the risk associated with the URL as LOW,MEDIUM or HIGH.
- Risk-assessment: Providing the risk-score,assessment and the reasons behind the same.

## Technologies/Tools Used
- Language: Python 3.10+
- Development Environment: VS Code
- Testing: pytest
- Version Control: Git
- Documentation: GitHub

## Project Structure
suspicious-url-analyzer/  
```
├── src/
│   ├── main.py           
│   ├── url_validator.py              
│   ├── feature_extractor.py          
│   ├── rules.py           
│   ├── risk_analyzer.py
│   └── report_generator.py
│
├── tests/
│   └── test_analyzer.py
│
├── requirements.txt
├── README.md
└── statement.md
```        
## INSTALLATION AND RUNNING
### Prerequisites
- Python 3.10(or higher installed)
- Git
- pip(Pthon Package Manager)
### Steps to install and run
1.Clone the repository: 
https://github.com/lakshyakapathak/Suspicious-URL-analyzer.git

2.Install dependencies:
`pip install -r requirements.txt`

3.Run the analyzer:
`python src/main.py`

4.Enter a URL when prompted. The program will display the risk score, risk level and the reasons for the same.Type n to exit when asked to enter another URL and type y if you want to continue.

## TESTING
This project includes a test suite built with pytest, covering url validation, feature extraction and a risk analysis.

To run the tests:
`pytest tests/test_analyzer.py -v`

All 5 tests should pass, verifying:
- Correct validation of valid and invalid URLs.
- Accurate detection of IP address hosts.
- Correct counting of suspicious keywords.
- Correct risk scoring and classification for a known high-risk URL.






