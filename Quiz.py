import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from ui_pomodoro import Ui_MainWindow

class PomodoroApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_timer)

        self.total_time = 25 * 60
        self.remaining_time = self.total_time

        self.ui.startButton.clicked.connect(self.start_timer)
        self.ui.pauseButton.clicked.connect(self.pause_timer)
        self.ui.resetButton.clicked.connect(self.reset_timer)

        self.ui.progressBar.setValue(0)
        self.update_display()

    def apply_custom_time(self):
        custom_time = self.ui.timeInput.text()
        if custom_time.strip().isdigit():
            minutes = int(custom_time)
            if minutes > 0:
                self.total_time = minutes * 60
                self.remaining_time = self.total_time

    def update_display(self):
        minutes = self.remaining_time // 60
        seconds = self.remaining_time % 60
        self.ui.timerLabel.setText(f"{minutes:02}:{seconds:02}")


        if self.total_time > 0:
            percent = int((self.total_time - self.remaining_time) / self.total_time * 100)
            self.ui.progressBar.setValue(percent)

    def update_timer(self):
        if self.remaining_time > 0:
            self.remaining_time -= 1
            self.update_display()
        else:
            self.timer.stop()
            self.ui.timerLabel.setText("Time's up!")
            self.ui.progressBar.setValue(100)

    def start_timer(self):
        self.apply_custom_time()
        self.update_display()
        self.timer.start()

    def pause_timer(self):
        self.timer.stop()

    def reset_timer(self):
        self.timer.stop()
        self.apply_custom_time()
        self.update_display()
        self.ui.progressBar.setValue(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PomodoroApp()
    window.show()
    sys.exit(app.exec_())



