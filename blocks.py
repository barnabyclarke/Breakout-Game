from turtle import Turtle

COLOUR_LIST = ["green", "yellow", "orange", "red", "purple"]


class Blocks(Turtle):

    def __init__(self):
        super().__init__()
        self.blocks = []
        self.y = -100
        self.x = 254.25
        self.make_blocks()

    def make_blocks(self):
        for color_row in range(len(COLOUR_LIST)):  # ROWS
            self.x = 254.25
            for block_col in range(10):  # COLUMNS
                new_block = Turtle(shape="square")
                new_block.shapesize(2, 2.675)
                new_block.color(COLOUR_LIST[color_row])
                new_block.penup()
                new_block.goto(self.x, self.y)
                self.blocks.append(new_block)
                self.x -= 56.5  # Block width + 5px gap to left block
            self.y += 45
