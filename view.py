from PyQt5 import QtCore, QtWidgets


class View:
    ERROR_FORMAT = "Error: {}"

    def output(self, res):
        if isinstance(res, tuple):
            desc, knights = res
            print('\n'.join([' '.join(row) for row in desc]))
            print('\n{} knights on the desc.\n'.format(knights))
        elif isinstance(res, list):
            print('\n'.join([' '.join(row) for row in res]))
            print()
        elif isinstance(res, str):
            print(res)
        elif isinstance(res, Exception):
            print(self.ERROR_FORMAT.format(res))

    @staticmethod
    def input(msg):
        inp = input(msg)
        return inp


class QtView:
    def __init__(self, _model):
        self.model = _model

    def setupUi(self, form):
        form.setObjectName("form")
        form.resize(212, 362)
        self.verticalLayoutWidget = QtWidgets.QWidget(form)
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
        self.horizontalLayout.addWidget(self.spinBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.spinBox_2 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_2.addWidget(self.spinBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_3 = QtWidgets.QLabel(form)
        self.label_3.setGeometry(QtCore.QRect(40, 0, 131, 31))
        self.label_3.setStyleSheet("font: 75 italic 12pt \"Ubuntu\";")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(form)
        self.pushButton.setGeometry(QtCore.QRect(70, 100, 85, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.fill_desc)
        self.textBrowser = QtWidgets.QTextBrowser(form)
        self.textBrowser.setGeometry(QtCore.QRect(10, 130, 191, 221))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    def retranslateUi(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("form", "form"))
        self.label.setText(_translate("form", "Desc size"))
        self.label_2.setText(_translate("form", "Knights num"))
        self.label_3.setText(_translate("form", "How Many Knights"))
        self.pushButton.setText(_translate("form", "Start"))
        self.textBrowser.setHtml(_translate("form", self.model.desc_html))

    def fill_desc(self):
        return
