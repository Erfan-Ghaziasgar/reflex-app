"""Common UI components."""

import reflex as rx


def page_header(title: str, subtitle: str = "") -> rx.Component:
    """Common page header component."""
    return rx.vstack(
        rx.heading(title, size="8", margin_bottom="2"),
        rx.text(subtitle, color="gray", size="4") if subtitle else rx.fragment(),
        spacing="2",
        align="center",
        margin_bottom="6",
    )


def navigation_menu() -> rx.Component:
    """Main navigation menu."""
    return rx.list.ordered(
        rx.list.item(
            rx.link("Home", href="/")
        ),
        rx.list.item(
            rx.link("Users", href="/users")
        ),
        rx.list.item(
            rx.link("Documentation", href="https://reflex.dev/docs", is_external=True)
        ),
        spacing="4",
        margin_top="20px",
    )