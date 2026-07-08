# Form Automation Platform

A Python platform for automatically discovering, understanding, storing, and completing web forms.

The project combines browser automation, HTML analysis, and structured data models to provide a reusable framework capable of interacting with virtually any online form.

## Motivation

Modern organizations repeatedly complete online forms for registrations, applications, surveys, customer onboarding, government services, and internal workflows.

Although the information being submitted often remains the same, each website presents different layouts, technologies, and field names, making automation difficult.

The goal of this project is to build a generic platform capable of identifying form structures, understanding their fields, storing reusable data, and automatically completing forms with minimal manual intervention.

## Objectives

- Automatically detect HTML forms.
- Identify and classify form fields.
- Store reusable user profiles.
- Automatically populate supported forms.
- Support manual review before submission.
- Produce reusable form templates.
- Maintain a modular and extensible architecture.

## Planned Features

- Browser automation using Playwright
- HTML parsing
- Form extraction
- Field classification
- Automatic form filling
- Support for multiple profiles
- Configuration system
- CLI interface
- Export and import of form templates
- Logging
- Validation
- Plugin architecture

## Architecture

Browser
│
▼
Playwright
│
▼
HTML Parser
│
▼
Form Detection
│
▼
Field Classification
│
▼
Data Mapping
│
▼
Automatic Filling
│
▼
Validation
│
▼
Submission

## Technology Stack

| Layer              | Technology           |
| ------------------ | -------------------- |
| Language           | Python 3.13          |
| Browser Automation | Playwright           |
| HTML Parsing       | BeautifulSoup + lxml |
| Models             | Pydantic             |
| CLI                | Typer                |
| Testing            | Pytest               |
| Linting            | Ruff                 |
| Type Checking      | MyPy                 |

## Project Status

Current milestone:

- Project Foundation

Current implementation progress:

- Repository initialization
- Architecture definition
- Development environment setup
- Playwright installed and configured

No browser automation has been implemented yet.

## Roadmap

Milestone 1
Project Foundation

Milestone 2
Browser Automation

Milestone 3
Form Detection

Milestone 4
Field Classification

Milestone 5
Storage Layer

Milestone 6
Automatic Form Filling

Milestone 7
Production Release

## Repository Structure

form-automation-platform/
├── docs/
├── examples/
├── logs/
├── output/
├── scripts/
├── src/
│ └── form_automation/
│ ├── browser/
│ ├── cli/
│ ├── config/
│ ├── core/
│ ├── models/
│ ├── parser/
│ ├── services/
│ ├── storage/
│ └── utils/
├── tests/
├── pyproject.toml
└── README.md

## License

This project is being developed for educational, research, and portfolio purposes.

A production license will be defined later.
