import os
import sys
import unittest

from Qt.QtWidgets import *
from Qt.QtGui import *
from Qt.QtCore import *
from Qt.QtTest import QTest

import mighty

app = QApplication(sys.argv)


class MargaritaMixerTest(unittest.TestCase):
    """Test the mighty GUI"""
    def setUp(self):
        """Create the GUI"""
        self.mighty_ui = mighty.SimpleUi()

    def test_button_a_pressed(self):
        self.mighty_ui.mighty_button_a.click()
        print('Button A clicked!')
        self.assertIsNotNone(self.mighty_ui.some_data)


if __name__ == '__main__':
    unittest.main()
