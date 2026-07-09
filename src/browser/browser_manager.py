"""
Browser lifecycle management.

This module provides the BrowserManager class, responsible for managing
Playwright initialization, browser creation, browser contexts, and pages.
"""

from __future__ import annotations

import logging

from playwright.async_api import (
    Browser,
    BrowserContext,
    Page,
    Playwright,
)

from .exceptions import (
    BrowserAlreadyStartedError,
    BrowserNotStartedError,
)


class BrowserManager:
    """
    Manages the lifecycle of a Playwright browser instance.

    Responsibilities
    ----------------
    - Start and stop Playwright.
    - Launch the browser.
    - Create browser contexts.
    - Create pages.
    """

    def __init__(self) -> None:
        self._playwright: Playwright | None = None
        self._browser: Browser | None = None
        self._logger = logging.getLogger(__name__)
