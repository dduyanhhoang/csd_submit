class Empty(Exception):
    def __init__(self, message="The container is empty"):
        self.message = message
        super().__init__(self.smessage)
