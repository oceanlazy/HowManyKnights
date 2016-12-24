from PyQt5 import QtCore, QtWidgets


class View:
    ERROR_FORMAT = "Error: {}"

    def output(self, res):
        if isinstance(res, tuple):
            desc, knights = res
            print('\n'.join([' '.join(row) for row in desc]))
            print('\n{} knights on the desc.\n'.format(knights))
        elif isinstance(res, list):
            print('\n'.join([' '.join(row) for row in res]), '\n')
        elif isinstance(res, str):
            print(res)
        elif isinstance(res, Exception):
            print(self.ERROR_FORMAT.format(res))

    @staticmethod
    def input(msg):
        return input(msg)


class QtView:
    def __init__(self, _model):
        self.model = _model

    def setupUi(self, window):
        window.setObjectName("window")
        window.resize(212, 362)
        self.verticalLayoutWidget = QtWidgets.QWidget(window)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 30, 181, 66))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.spinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox.setMaximumSize(QtCore.QSize(129, 16777215))
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setValue(8)
        self.spinBox.setMaximum(14)
        self.horizontalLayout.addWidget(self.spinBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.spinBox_2 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_2.setValue(32)
        self.horizontalLayout_2.addWidget(self.spinBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_3 = QtWidgets.QLabel(window)
        self.label_3.setGeometry(QtCore.QRect(40, 0, 131, 31))
        self.label_3.setStyleSheet("font: 75 italic 12pt \"Ubuntu\";")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(window)
        self.pushButton.setGeometry(QtCore.QRect(70, 100, 85, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.fill_desc)
        self.textBrowser = QtWidgets.QTextBrowser(window)
        self.textBrowser.setGeometry(QtCore.QRect(10, 130, 191, 221))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "HowManyKnights"))
        self.label.setText(_translate("window", "Desc size"))
        self.label_2.setText(_translate("window", "Knights num"))
        self.label_3.setText(_translate("window", "How Many Knights"))
        self.pushButton.setText(_translate("window", "Start"))
        self.textBrowser.setHtml(_translate("window", self.model.desc_html))

    def fill_desc(self):
        return
