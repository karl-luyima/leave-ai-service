class LeaveAIException(Exception):
    """
    Base exception for Leave AI service errors.
    """


    def __init__(
        self,
        message: str
    ):

        self.message = message

        super().__init__(
            self.message
        )