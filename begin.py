from control.MainWindow import mainWidget
from PyQt5 import QtWidgets
import os
if __name__ == "__main__":
    os.environ["TF_CPP_MIN_LOG_LEVEL"] = '2'
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = mainWidget()
    Form.showMaximized()
    sys.exit(app.exec_())

