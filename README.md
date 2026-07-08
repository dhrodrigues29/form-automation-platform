# Form Automation Platform

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Status](https://img.shields.io/badge/status-under%20development-yellow)
![License](https://img.shields.io/badge/license-TBD-lightgrey)

A modular Python platform for discovering, analyzing, storing, and automatically completing web forms through browser automation and structured HTML analysis.

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
- Support for multiple user profiles
- Automatic form filling
- Manual review before submission
- Export and import of form templates
- Configuration system
- CLI interface
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

**Current Version**

v0.1.0 (Development)

**Current Milestone**

Milestone 2 — Browser Automation

**Overall Progress**

- _Completed_ Milestone 1 — Project Foundation
- _In Progress_ Milestone 2 — Browser Automation
- _Waiting_ Milestone 3 — Form Detection
- _Waiting_ Milestone 4 — Field Classification
- _Waiting_ Milestone 5 — Storage Layer
- _Waiting_ Milestone 6 — Automatic Form Filling

## Development Progress

### Milestone 1 — Project Foundation

**Completed**

- Repository initialized with Git and uv
- Python project configured
- Modern `src` project layout created
- Package architecture defined
- Development tooling configured (Ruff, MyPy, Pytest)
- Playwright installed and configured
- Initial architecture documentation created

### Milestone 2 — Browser Automation

**In Progress**

- Browser abstraction layer
- Browser session management
- Configuration system
- Initial Playwright integration

## Roadmap

- [x] Milestone 1 — Project Foundation
- [ ] Milestone 2 — Browser Automation
- [ ] Milestone 3 — Form Detection
- [ ] Milestone 4 — Field Classification
- [ ] Milestone 5 — Storage Layer
- [ ] Milestone 6 — Automatic Form Filling

## Repository Structure

```text
docs/        Project documentation
examples/    Example forms and sample workflows
logs/        Development logs (ignored by Git)
output/      Generated artifacts (ignored by Git)
scripts/     Development and maintenance scripts
src/         Application source code
tests/       Automated tests
```

## License

This project is currently under active development.

The license will be defined before the first public release.
