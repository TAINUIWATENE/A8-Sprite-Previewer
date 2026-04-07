import math

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

def load_sprite(sprite_folder_name, number_of_frames):
    frames = []
    padding = math.ceil(math.log(number_of_frames - 1, 10))
    for frame in range(number_of_frames):
        folder_and_file_name = sprite_folder_name + "/sprite_" + str(frame).rjust(padding, '0') + ".png"
        frames.append(QPixmap(folder_and_file_name))

    return frames

class SpritePreview(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sprite Animation Preview")
        self.num_frames = 21
        self.frames = load_sprite('spriteImages',self.num_frames)

        class SpritePreview(QMainWindow):

            def __init__(self):
                super().__init__()
                self.setWindowTitle("Sprite Animation Preview")

                self.num_frames = 20
                self.frames = load_sprite('spriteImages', self.num_frames)

                self.current_frame = 0
                self.fps = 10
                self.timer = QTimer()
                self.timer.timeout.connect(self.next_frame)



        self.setupUI()


    def setupUI(self):
        # An application needs a central widget - often a QFrame
        frame = QFrame()

        # Add a lot of code here to make layouts, more QFrame or QWidgets, and
        # the other components of the program.
        # Create needed connections between the UI components and slot methods
        # you define in this class.

        self.setCentralWidget(frame)


    # You will need methods in the class to act as slots to connect to signals


def main():
    app = QApplication([])
    # Create our custom application
    window = SpritePreview()
    # And show it
    window.show()
    app.exec()


if __name__ == "__main__":
    main()