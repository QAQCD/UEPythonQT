import unreal
from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtUiTools
from PySide2 import QtWidgets
import sys



#实例化编辑器级别库
editor_level_lib = unreal.EditorLevelLibrary()

class SimpleGUI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(SimpleGUI, self).__init__(parent)
        #加载QT UI的绝对路径
        self.widget = QtUiTools.QUiLoader().load("E:\\github\\UEPythonQT\\UE4_Python\\Python_GUI\\Form.ui")

        #设置父级
        self.widget.setParent(self)
        #设置几何图形
        self.widget.setGeometry(0, 0, self.widget.width(), self.widget.height())

        #获取QT文本编辑
        self.text_L = self.widget.findChild(QtWidgets.QLineEdit, "textBox_L")
        self.text_R = self.widget.findChild(QtWidgets.QLineEdit, "textBox_R")

        self.checkbox = self.widget.findChild(QtWidgets.QCheckBox, "CheckBox")

        #获取QT水平滑块
        self.slider = self.widget.findChild(QtWidgets.QSlider, "horizontalSlider")
        # 执行自定义事件
        self.slider.sliderMoved.connect(self.on_slide)

        #（QtWidgets.Class, objectName)  获取Qt Designer中 图形的  类和名称
        self.btn_ok = self.widget.findChild(QtWidgets.QPushButton, "okButton")
        # 点击后执行 自定义ok_clicked事件
        self.btn_ok.clicked.connect(self.ok_clicked)

        self.btn_canel = self.widget.findChild(QtWidgets.QPushButton, "canelButton")
        #执行自定义事件
        self.btn_canel.clicked.connect(self.canel_clicked)

    #自定义的事件
    #水平滑块
    def on_slide(self):
        slider_value = self.slider.value()

        #
        selected_actors = editor_level_lib.get_selected_level_actors()

        if len(selected_actors) > 0:
            actor = selected_actors[0]

            new_transform = actor.get_actor_transform()
            new_transform.translation.y = slider_value

            actor.set_actor_transform(new_transform, True, True)
        #unreal.log(slider_value)

    #点击OK按钮
    def ok_clicked(self):
        text_l = self.text_L.text()
        text_r = self.text_R.text()
        is_checked = self.checkbox.isChecked()

        unreal.log("左边{}".format(text_r))
        unreal.log("右边{}".format(text_l))
        unreal.log("左边{}".format(is_checked))

    # 点击Cancel关闭按钮
    def canel_clicked(self):
        unreal.log("Canceled")
        #关闭QTUI
        self.close()


#仅在GUI尚未运行时创建GUI实例
app = None
if not QtWidgets.QApplication.instance():
    app = QtWidgets.QApplication(sys.argv)

#启动GUI
main_window = SimpleGUI()
main_window.show()
