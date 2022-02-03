import sys
from PySide6.QtWidgets import QApplication, QLabel, QPushButton
from PySide6.QtCore import Slot


@Slot()
def say_hello():
    print("Button clicked, Hello!")
 
# This creates the application using QApplication   
app = QApplication(sys.argv)

button = QPushButton("Click me")

# Connect the "Click me" signal from the button to the say_hello function
button.clicked.connect(say_hello)

# Show the button on the window
button.show()

# Start the Qt main loop
app.exec()