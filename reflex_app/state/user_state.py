"""User state management."""

from collections import Counter
from typing import Any

import reflex as rx
from sqlmodel import select

from ..models import User


class UserState(rx.State):
    """The user state."""

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