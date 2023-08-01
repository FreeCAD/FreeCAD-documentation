# PySide usage snippets/pl
## Introduction

These are snippets of code that are useful when [creating interfaces](Dialog_creation.md) with [PySide](PySide.md).

## Some useful commands 


```python
# Here the code to display the icon on the '''pushButton''', 
# change the name to another button, ('''radioButton, checkBox''') as well as the path to the icon,

       # Displays an icon on the button PushButton
       # self.image_01 = "C:\Program Files\FreeCAD0.13\icone01.png" # he name of the icon
       self.image_01 = path+"icone01.png" # the name of the icon
       icon01 = QtGui.QIcon() 
       icon01.addPixmap(QtGui.QPixmap(self.image_01),QtGui.QIcon.Normal, QtGui.QIcon.Off)
       self.pushButton.setIcon(icon01) 
       self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft) # This command reverses the direction of the button


# path = FreeCAD.ConfigGet("UserAppData") # gives the user path
  path = FreeCAD.ConfigGet("AppHomePath") # gives the installation path of FreeCAD

# This command reverses the horizontal button, right to left
self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft) # This command reverses the horizontal button

# Displays an info button
self.pushButton.setToolTip(_translate("MainWindow", "Quitter la fonction", None)) # Displays an info button

# This function gives a color button
self.pushButton.setStyleSheet("background-color: red") # This function gives a color button

# This function gives a color to the text of the button
self.pushButton.setStyleSheet("color : #ff0000") # This function gives a color to the text of the button

# combinaison des deux, bouton et texte
self.pushButton.setStyleSheet("color : #ff0000; background-color : #0000ff;" ) #  combination of the two, button, and text

# replace the icon in the main window
MainWindow.setWindowIcon(QtGui.QIcon('C:\Program Files\FreeCAD0.13\View-C3P.png'))

# connects a lineEdit on execute
self.lineEdit.returnPressed.connect(self.execute) # connects a lineEdit on "def execute" after validation on enter
# self.lineEdit.textChanged.connect(self.execute) # connects a lineEdit on "def execute" with each keystroke on the keyboard

# display text in a lineEdit
self.lineEdit.setText(str(val_X)) # Displays the value in the lineEdit (convert to string)

# extract the string contained in a lineEdit
 val_X = self.lineEdit.text() # extract the (string) string contained in lineEdit
 val_X = float(val_X0)        # converted the string to an floating
 val_X = int(val_X0)          # convert the string to an integer

# This code allows you to change the font and its attributes
       font = QtGui.QFont()
       font.setFamily("Times New Roman")
       font.setPointSize(10)
       font.setWeight(10)
       font.setBold(True) # same result with tags "<b>your text</b>" (in quotes)
       self.label_6.setFont(font)
       self.label_6.setObjectName("label_6")
       self.label_6.setStyleSheet("color : #ff0000") # This function gives a color to the text
       self.label_6.setText(_translate("MainWindow", "Select a view", None))
```

## Encoding problems 

### UTF8

By using the characters with accents, where you get the error: 
```python
UnicodeDecodeError: 'utf8' codec can't decode bytes in position 0-2: invalid data
```

Several solutions are possible. 
```python
# conversion from a lineEdit
App.activeDocument().CopyRight.Text = str(unicode(self.lineEdit_20.text() , 'ISO-8859-1').encode('UTF-8'))
DESIGNED_BY = unicode(self.lineEdit_01.text(), 'ISO-8859-1').encode('UTF-8')
```

or with the procedure 
```python
def utf8(unio):
    return unicode(unio).encode('UTF8')
```

### ASCII


```python
UnicodeEncodeError: 'ascii' codec can't encode character u'\xe9' in position 9: ordinal not in range(128)
```


```python
# conversion
a = u"Nom de l'élément : "
f.write('''a.encode('iso-8859-1')'''+str(element_)+"\n")
```

or with the procedure 
```python
def iso8859(encoder):
    return unicode(encoder).encode('iso-8859-1')
```

or 
```python
iso8859(unichr(176))
```

or 
```python
unichr(ord(176))
```

or 
```python
uniteSs = "mm"+iso8859(unichr(178))
print(unicode(uniteSs, 'iso8859'))
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > PySide usage snippets/pl
