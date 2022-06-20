from enum import Enum


class OperationType(Enum):
    """
    Enum for the different types of CRUD operations.
    """
    CREATE = ("PluralView", "post")
    READ = ("SingleView", "get")
    UPDATE = ("SingleView", "put")
    DELETE = ("SingleView", "delete")
    READ_ALL = ("PluralView", "get")

    @property
    def view_name(self) -> str:
        """
        Get the name of the view for the given operation type.
        """
        return self.value[0]

    @property
    def method_name(self) -> str:
        """
        Get the name of the method for the given operation type.
        """
        return self.value[1]
