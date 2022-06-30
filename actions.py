class Action:
    """Generic Action class"""
    pass


class EscapeAction(Action):
    """Action implementation that represents escaping out of the program"""
    pass


class MovementAction(Action):
    """Action implementation that represents player movement"""

    def __init__(self, dx: int, dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy
