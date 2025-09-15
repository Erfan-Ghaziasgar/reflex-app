"""User-related UI components."""

import reflex as rx

from ..models import User
from ..state import UserState


def display_user(user: User) -> rx.Component:
    """Display a user in a table row."""
    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.email),
        rx.table.cell(user.gender),
    )


def user_form() -> rx.Component:
    """User input form."""
    return rx.form(
        rx.flex(
            rx.input(
                placeholder="User Name",
                name="name",
                required=True,
            ),
            rx.input(
                placeholder="user@reflex.dev",
                name="email",
                required=True,
            ),
            rx.select(
                ["Male", "Female"],
                placeholder="Male",
                name="gender",
                required=True,
            ),
            rx.flex(
                rx.dialog.close(
                    rx.button(
                        "Cancel",
                        variant="soft",
                        color_scheme="gray",
                    ),
                ),
                rx.dialog.close(
                    rx.button("Submit", type="submit"),
                ),
                spacing="3",
                justify="end",
            ),
            direction="column",
            spacing="4",
            margin_top="20px",
        ),
        on_submit=UserState.add_user,
        reset_on_submit=False,
        spacing="6",
    )


def form_dialog() -> rx.Component:
    """A dialog to add a user."""
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("plus", size=26),
                rx.text("Add User", size="4"),
            ),
            justify="end",
            margin_top="20px",
        ),
        rx.dialog.content(
            rx.dialog.title("Add New User"),
            rx.dialog.description("Fill the form with the user's info"),
            user_form(),
            justify="center",
            variant="glass",
            boarder_radius="lg",
        ),
    )


def users_table() -> rx.Component:
    """Display all users in a table."""
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.cell("Name"),
                rx.table.cell("Email"),
                rx.table.cell("Gender"),
            )
        ),
        rx.table.body(
            rx.foreach(UserState.users, display_user)
        ),
        border="1px solid black",
        margin_top="50px",
        variant="surface",
    )


def users_chart() -> rx.Component:
    """Display users gender distribution chart."""
    return rx.recharts.bar_chart(
        rx.recharts.bar(
            data_key="value",
            fill=rx.color("blue", 8),
            stroke=rx.color("blue", 9),
        ),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        data=UserState.users_for_graph,
        width="100%",
        height=250,
        margin_top="50px",
        justify="center",
    )