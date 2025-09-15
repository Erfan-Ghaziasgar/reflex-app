"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from collections import Counter
from typing import Any, Optional

import reflex as rx
from sqlmodel import Field, select

from rxconfig import config


class User(rx.Model, table=True):
    """A user."""
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    gender: str


class UserState(rx.State):
    """The app state."""

    users: list[User] = []

    def load_users(self):
        """Load all users from the DB (call on page load)."""
        with rx.session() as session:
            self.users = session.exec(select(User)).all()

    def add_user(self, form_data: dict[str, Any]) -> None:
        """Persist a new user, then update state."""
        new_user = User(
            name=form_data["name"],
            email=form_data["email"],
            gender=form_data["gender"],
        )
        with rx.session() as session:
            session.add(new_user)
            session.commit()
            session.refresh(new_user)
        # reflect change in UI state
        self.users.append(new_user)

    @rx.var
    def users_for_graph(self) -> list[dict[str, Any]]:
        """Get the users for the graph."""
        counter = Counter(user.gender for user in self.users)
        return [{"name": k, "value": v} for k, v in counter.items()]


def display_user(user: User) -> rx.Component:
    """Display a user."""
    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.email),
        rx.table.cell(user.gender),
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
            rx.dialog.title(
                "Add New User",
            ),
            rx.dialog.description(
                "Fill the form with the user's info",
            ),
            rx.form(
                # flex is similar to vstack and used to layout the form fields
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
            ),
            # max_width is used to limit the width of the dialog
            # max_width="450px",
            justify="center",
            variant="glass",
            boarder_radius="lg",
        ),
    )


def display_users() -> rx.Component:
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


def graph() -> rx.Component:
    return rx.recharts.bar_chart(
        rx.recharts.bar(
            data_key="value",
            fill=rx.color("blue", 8),
            stroke=rx.color("blue", 9),
        ),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        # This should work - accessing the property through the state
        data=UserState.users_for_graph,
        width="100%",
        height=250,
        margin_top="50px",
        justify="center",
    )


def index() -> rx.Component:
    """The main page of the app."""
    return rx.flex(
        rx.heading("Welcome to Reflex!", margin_top="20px"),
        rx.spacer(),
        rx.list.ordered(
            rx.list.item(
                rx.link("Documentation", href="https://reflex.dev/docs", is_external=True)),
            rx.list.item(rx.link(rx.text("Users"), href="/users")),
            spacing="4",
            margin_top="20px",
        ),
        padding="20px",
        direction="column",
        align_items="flex-start",
    )


def users() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("User Management", margin_top="20px"),
            display_users(),
            form_dialog(),
            rx.cond(
                UserState.users.length() > 0,
                graph(),
                rx.text("Add some users to see the gender distribution chart",
                        color="gray", size="3", margin_top="50px", text_align="center")
            ),
        ),
        padding="20px",
        on_mount=UserState.load_users,
    )


app = rx.App(
    theme=rx.theme(
        accent_color="blue",
        font_family="Poppins",
        radius="medium",
    )
)
app.add_page(index, route="/", title="Home")
app.add_page(users, route="/users", title="Users List")
