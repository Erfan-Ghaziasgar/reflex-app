"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            rx.link(
                rx.button("Go to Second Page"),
                href="/second",
            ),
            rx.text(f"Count: {State.count}"),
            rx.button("Increment", on_click=State.increment),
            rx.button("Decrement", on_click=State.decrement),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),

        spacing="5",
        justify="center",
        min_height="85vh",
    )


def second_page() -> rx.Component:
    return rx.container(
        rx.heading("This is the second page", size="9"),
        rx.link(
            rx.button("Go back to Home"),
            href="/",
        ),
        spacing="5",
        justify="center",
        min_height="85vh",
    )


app = rx.App()
app.add_page(index)
app.add_page(second_page, route="/second")
