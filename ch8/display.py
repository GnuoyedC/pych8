WIDTH,HEIGHT = (64,32) # pixels

class Display:
    def __init__(self):
        self.grid = self.clear()
        return
    def clear(self):
        self.grid = self.create_empty()
    def create_empty(self):
        return [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]  # Create a 2D list with distinct rows

