"""Home page."""

import reflex as rx

from ..components import navigation_menu, page_header


def home_page() -> rx.Component:
    """The home page."""
    return rx.container(
        page_header("Welcome to Reflex!", "A modern web framework for Python"),
        navigation_menu(),
        padding="20px",
        max_width="800px",
    )
