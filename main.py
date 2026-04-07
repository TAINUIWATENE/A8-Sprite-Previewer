#A8-Sprite-Previewer
#Tainui Watene u1334460
#https://github.com/TAINUIWATENE/A8-Sprite-Previewer
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
        self.frames = load_sprite('spriteImages', self.num_frames)

        self.current_frame = 0
        self.fps = 10
        self.timer = QTimer()
        self.timer.timeout.connect(self.next_frame)

        self.setupUI()

    def setupUI(self):
        frame = QFrame()
        main_layout = QVBoxLayout()

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setPixmap(self.frames[0])

        fps_text_label = QLabel("Frames per second")
        fps_text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.fps_value_label = QLabel(str(self.fps))
        self.fps_value_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(1, 100)
        self.slider.setValue(self.fps)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.setTickInterval(10)
        self.slider.valueChanged.connect(self.change_fps)

        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.toggle_animation)

        controls_layout = QVBoxLayout()
        controls_layout.addWidget(fps_text_label)
        controls_layout.addWidget(self.slider)
        controls_layout.addWidget(self.fps_value_label)
        controls_layout.addWidget(self.start_button)

        main_layout.addWidget(self.image_label)
        main_layout.addLayout(controls_layout)

        frame.setLayout(main_layout)
        self.setCentralWidget(frame)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")

        pause_action = QAction("Pause", self)
        exit_action = QAction("Exit", self)

        pause_action.triggered.connect(self.pause_animation)
        exit_action.triggered.connect(self.close)

        file_menu.addAction(pause_action)
        file_menu.addAction(exit_action)

    def next_frame(self):
        self.current_frame += 1
        if self.current_frame >= self.num_frames:
            self.current_frame = 0
        self.image_label.setPixmap(self.frames[self.current_frame])

    def change_fps(self, value):
        self.fps = value
        self.fps_value_label.setText(str(value))

        if self.timer.isActive():
            delay = int(1000 / self.fps)
            self.timer.start(delay)

    def toggle_animation(self):
        if self.start_button.text() == "Start":
            delay = int(1000 / self.fps)
            self.timer.start(delay)
            self.start_button.setText("Stop")
        else:
            self.timer.stop()
            self.start_button.setText("Start")

    def pause_animation(self):
        self.timer.stop()
        self.start_button.setText("Start")


def main():
    app = QApplication([])
    window = SpritePreview()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()