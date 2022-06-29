class Display:
    def __init__(self):
        self.current_message = ""

    def display_message(self):
        print(self.current_message)

    def notify(self, *messages):
        for message in messages:
            self.current_message = message
            self.display_message()
