"""User model definition."""

from typing import Optional
import reflex as rx
from sqlmodel import Field


class User(rx.Model, table=True):
    """A user model."""
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    gender: str