import os
os.system("pyuic4 -o gui.py gui.ui")
<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>240</width>
    <height>320</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QRadioButton" name="radioButton">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>20</y>
      <width>62</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>manual input</string>
    </property>
   </widget>
   <widget class="QRadioButton" name="radioButton_2">
    <property name="geometry">
     <rect>
      <x>110</x>
      <y>20</y>
      <width>62</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>CSV input</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>60</y>
      <width>181</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QPlainTextEdit" name="plainTextEdit">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>60</y>
      <width>61</width>
      <height>21</height>
     </rect>
    </property>
    <property name="plainText">
     <string>user input
</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit_2">
    <property name="geometry">
     <rect>
      <x>70</x>
      <y>130</y>
      <width>161</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QPlainTextEdit" name="plainTextEdit_2">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>130</y>
      <width>71</width>
      <height>21</height>
     </rect>
    </property>
    <property name="plainText">
     <string>output file name</string>
    </property>
   </widget>
   <widget class="QDialogButtonBox" name="buttonBox">
    <property name="geometry">
     <rect>
      <x>60</x>
      <y>260</y>
      <width>116</width>
      <height>17</height>
     </rect>
    </property>
    <property name="standardButtons">
     <set>QDialogButtonBox::Cancel|QDialogButtonBox::Ok</set>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit_3">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>90</y>
      <width>231</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit_4">
    <property name="geometry">
     <rect>
      <x>-8</x>
      <y>160</y>
      <width>241</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>240</width>
     <height>18</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
if __name__ == "__main__":
    window = MyWindow()
    sys.exit(app.exec_())