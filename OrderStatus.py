import enum
class OrderStatus(enum.Enum):
    Status_0 = 0, "Creating"
    Status_1 = 1, "Created"
    def __init__(self, Status, desc):
        self._Status = Status
        self._desc = desc
    @property
    def desc(self):
        return self._desc
    @property
    def Status(self):
        return self._Status