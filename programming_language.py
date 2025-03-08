"""
Estimate: 20 minutes
Actual: 25 minutes
"""

class ProgrammingLanguage:
    """Represent a programming language object."""

    def __init__(self, name, typing, reflection, year):
        """Initialize a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Check if the language is dynamically typed."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a formatted string representation of the object."""
        return f"{self.name}, {self.typing.capitalize()} Typing, Reflection={self.reflection}, First appeared in {self.year}"