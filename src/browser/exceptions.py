"""
Custom exceptions for the browser layer.

These exceptions abstract away Playwright-specific errors so the rest of the
application depends only on our own exception hierarchy.
"""


class BrowserError(Exception):
    """Base class for all browser-related errors."""


class BrowserLaunchError(BrowserError):
    """Raised when the browser cannot be started."""


class BrowserNotStartedError(BrowserError):
    """Raised when the browser is used before being started."""


class BrowserAlreadyStartedError(BrowserError):
    """Raised when attempting to start an already running browser."""
