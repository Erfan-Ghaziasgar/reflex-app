"""Users page."""

import reflex as rx

from ..components import form_dialog, page_header, users_chart, users_table
from ..state import UserState


def users_page() -> rx.Component:
    """The users management page."""
    return rx.container(
        rx.vstack(
            page_header("User Management", "Manage your application users"),
            users_table(),
            form_dialog(),
            rx.cond(
                UserState.users.length() > 0,
                users_chart(),
                rx.text(
                    "Add some users to see the gender distribution chart",
                    color="gray",
                    size="3",
                    margin_top="50px",
                    text_align="center"
                )
            ),
            spacing="6",
        ),
        padding="20px",
        max_width="1000px",
        on_mount=UserState.load_users,
    )
