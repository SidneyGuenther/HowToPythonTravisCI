import sys
import time

from PySide.QtGui import *
from PySide.QtCore import *

MODE = 'DESKTOP'


class SimpleUi(QDialog):
    def __init__(self, parent=None):
        super(SimpleUi, self).__init__(parent)

        self.some_data = None

        self.setWindowTitle('Mighty')
        self.resize(200, 50)

        main_layout = QVBoxLayout(self)

        content_wgt = QGroupBox('Content')
        content_lyt = QVBoxLayout(content_wgt)
        self.mighty_button_a = QPushButton('Does mighty stuff!')

        content_lyt.addWidget(self.mighty_button_a)
        main_layout.addWidget(content_wgt)

        self._setup_connections()

        print('Done!')

    def _get_some_data(self):
        some_data = 'NICE DATA!'

        self.some_data = some_data

    def _setup_connections(self):
        self.mighty_button_a.clicked.connect(self._get_some_data)


def _desktop():
    simple_app = QApplication(sys.argv)

    simple_ui = SimpleUi()
    simple_ui.show()

    sys.exit(simple_app.exec_())


def start():
    print('Starting...')

    if MODE == 'DESKTOP':
        _desktop()


if __name__ == '__main__':
    start()
