"""Main application file."""

import reflex as rx
from .pages import home_page, users_page

# App configuration
app = rx.App(
    theme=rx.theme(
        accent_color="blue",
        font_family="Poppins",
        radius="medium",
    )
)

# Add pages
app.add_page(home_page, route="/", title="Home")
app.add_page(users_page, route="/users", title="Users List")
