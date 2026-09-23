# SUSPICIOUS URL ANALYZER

## Overview
Suspicious URL analyzer is a python-based, rule-driven project that examines URLs and identifies characteristics that may indicate suspicious or potentially unsafe links and generates a risk assessment.
It focuses on analyzing the structure and properties of a URL rather than interacting with the website behind the URL. The system analyzes multiple indicators, gives the results using a rule-based approach,
and provides the user with a risk level associated with the URL along with the reasons for the assessment.

## Problem Statement
Often URLs are encountered by people all over the world through emails, text messages, websites and social media platforms. Some of these URLs may contain suspicious characteristics that are not easily 
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

## Technologies/Tools Used
- Language: Python 3.10+
- Development Environment: VS Code
- Storage: SQLite3
- Testing: pytest
- Version Control: Git
- Documentation: GitHub

## Project Structure
suspicious-url-analyzer/
suspicious-url-analyzer/
|
+-- src/
|   +-- main.py
|   +-- url_validator.py
|   +-- feature_extractor.py
|   +-- rules.py
|   +-- risk_analyzer.py
|   +-- report_generator.py
|   +-- database.py
