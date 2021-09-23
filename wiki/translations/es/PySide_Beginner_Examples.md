# PySide Beginner Examples/es
## Introducción

El propósito de esta página es cubrir ejemplos de nivel de principiante del [PySide](PySide/es.md) Administrador de la interfaz gráfica de usuario (hay páginas que acompañan a [Ejemplos intermedios de PySide](PySide_Intermediate_Examples/es.md) y [Ejemplos avanzados de PySide](PySide_Advanced_Examples/es.md)).

Los recién llegados a la programación de la interfaz gráfica de usuario pueden tropezar con la palabra \"widget\". Su significado fuera de la informática se da normalmente como

> \"un pequeño artilugio o dispositivo mecánico, especialmente uno cuyo nombre es desconocido o no especificado\"

Para el trabajo con GUI como PySide el término \"widget\" se utiliza más a menudo para referirse a los elementos visibles de la GUI - ventanas, diálogos y características de entrada/salida. Todos los elementos visibles de PySide se denominan widgets, y, para aquellos que estén interesados, todos ellos descienden de una clase parental común, QWidget. Además de los elementos visibles, PySide también ofrece widgets para la integración de redes, XML, multimedia y bases de datos.

Un widget que no está incrustado en un widget padre se llama ventana y normalmente las ventanas tienen un marco y una barra de título. Los tipos de ventanas más comunes son la \"ventana principal\" (de la Clase QMainWindow) y las diversas subclases del cuadro de diálogo (de la Clase QDialog). Una gran diferencia es que QDialog es modal (es decir, el usuario no puede hacer nada fuera de la ventana de diálogo mientras está abierta) y la QMainWindow es no modal, lo que permite al usuario interactuar con otras ventanas en paralelo.

Esta guía es una lista de atajos para hacer que un programa PySide funcione rápidamente en FreeCAD, no está pensada para enseñar Python o PySide. Algunos sitios que lo hacen son:

-   [Tutorial de PySide](http://zetcode.com/gui/pysidetutorial/) en zetcode.com
-   [Tutorial de PySide/PyQt](http://www.pythoncentral.io/series/python-pyside-pyqt-tutorial/) en PythonCentral.io
-   [Referencia PySide 1.0.7](http://srinikom.github.io/) en Srinikom.github.io (note que esto es una referencia, no un tutorial)

## Declaración de importación 

PySide no está cargado con Python por defecto, debe ser solicitado antes de usarlo. El siguiente comando: 
```python
from PySide import QtCore
from PySide import QtGui
``` hace que se carguen las 2 partes de PySide - QtGui contiene clases para la gestión de la interfaz gráfica de usuario mientras que QtCore contiene clases que no se relacionan directamente con la gestión de la interfaz gráfica de usuario (por ejemplo, temporizadores y geometría). Aunque sólo es posible importar la que se necesita, generalmente se necesitan y se importan ambas.

Las declaraciones de importación no se repiten en los fragmentos que figuran a continuación; se supone que se hace al principio en cada caso.

## Ejemplo simple 

La interacción más simple con PySide es presentar un mensaje al usuario que sólo puede aceptar: 
```python
reply = QtGui.QMessageBox.information(None,"","Houston, we have a problem")
```

![](images/PySideScreenSnapshot5.jpg )

## Sí o no consulta 

La siguiente interacción más simple es pedir una respuesta de sí/no: 
```python
reply = QtGui.QMessageBox.question(None, "", "This is your chance to answer, what do you think?",
         QtGui.QMessageBox.Yes {{!``` QtGui.QMessageBox.No, QtGui.QMessageBox.No) if reply == QtGui.QMessageBox.Yes:

        # this is where the code relevant to a 'Yes' answer goes
        pass

if reply == QtGui.QMessageBox.No:

        # this is where the code relevant to a 'No' answer goes
        pass

}}

![](images/PySideScreenSnapshot6.jpg )

## Introducir consulta de texto 

El siguiente fragmento de código le pide al usuario un trozo de texto: 
```python
reply = QtGui.QInputDialog.getText(None, "Ouija Central","Enter your thoughts for the day:")
if reply[1]:
    # user clicked OK
    replyText = reply[0]
else:
    # user clicked Cancel
    replyText = reply[0] # which will be "" if they clicked Cancel
```

![](images/PySideScreenSnapshot7.jpg )

Recuerde que aunque el usuario introduzca sólo dígitos, \"1234\" por ejemplo, son cadenas y deben ser convertidos en representación numérica con cualquiera de los siguientes elementos: 
```python
anInteger = int(userInput) # to convert to an integer from a string representation

aFloat = float(userInput) # to convert to a float from a string representation
```

## Más de 2 botones 

El último ejemplo del Nivel de Principiantes es de cómo construir un diálogo con un número arbitrario de botones. Este ejemplo es programáticamente demasiado complejo para ser invocado desde una sola sentencia Python, así que de alguna manera debería estar en la siguiente página que son ejemplos de PySide Medium. Pero por otro lado esto es a menudo todo lo que se necesita sin entrar en definiciones complejas de GUI, así que el código se coloca al final de la página de esta página de PySide Principiante en lugar de al principio de la siguiente página de PySide Medio. 
```python
from PySide import QtGui, QtCore

class MyButtons(QtGui.QDialog):
    """"""
    def __init__(self):
        super(MyButtons, self).__init__()
        self.initUI()
    def initUI(self):      
        option1Button = QtGui.QPushButton("Option 1")
        option1Button.clicked.connect(self.onOption1)
        option2Button = QtGui.QPushButton("Option 2")
        option2Button.clicked.connect(self.onOption2)
        option3Button = QtGui.QPushButton("Option 3")
        option3Button.clicked.connect(self.onOption3)
        option4Button = QtGui.QPushButton("Option 4")
        option4Button.clicked.connect(self.onOption4)
        option5Button = QtGui.QPushButton("Option 5")
        option5Button.clicked.connect(self.onOption5)
        #
        buttonBox = QtGui.QDialogButtonBox()
        buttonBox = QtGui.QDialogButtonBox(QtCore.Qt.Horizontal)
        buttonBox.addButton(option1Button, QtGui.QDialogButtonBox.ActionRole)
        buttonBox.addButton(option2Button, QtGui.QDialogButtonBox.ActionRole)
        buttonBox.addButton(option3Button, QtGui.QDialogButtonBox.ActionRole)
        buttonBox.addButton(option4Button, QtGui.QDialogButtonBox.ActionRole)
        buttonBox.addButton(option5Button, QtGui.QDialogButtonBox.ActionRole)
        #
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        # define window     xLoc,yLoc,xDim,yDim
        self.setGeometry(   250, 250, 0, 50)
        self.setWindowTitle("Pick a Button")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    def onOption1(self):
        self.retStatus = 1
        self.close()
    def onOption2(self):
        self.retStatus = 2
        self.close()
    def onOption3(self):
        self.retStatus = 3
        self.close()
    def onOption4(self):
        self.retStatus = 4
        self.close()
    def onOption5(self):
        self.retStatus = 5
        self.close()

def routine1():
    print 'routine 1'

form = MyButtons()
form.exec_()
if form.retStatus==1:
    routine1()
elif form.retStatus==2:
    routine2()
elif form.retStatus==3:
    routine3()
elif form.retStatus==4:
    routine4()
elif form.retStatus==5:
    routine5()

``` Cada pieza de código bajo prueba estaría en una función con el nombre \"rutina1()\", \"rutina2()\", etc. Se pueden utilizar tantos botones como quepan en la pantalla. Siga los patrones de la muestra de código y añada botones adicionales según sea necesario - el cuadro de diálogo establecerá su ancho en consecuencia, hasta el ancho de la pantalla.

![](images/PySideScreenSnapshot8.jpg )

Hay una línea de código: 
```python
buttonBox = QtGui.QDialogButtonBox(QtCore.Qt.Horizontal)
``` lo que hace que los botones estén en una línea horizontal. Para ponerlos en una línea vertical, cambia la línea de código a leer: 
```python
buttonBox = QtGui.QDialogButtonBox(QtCore.Qt.Vertical)
```


{{Powerdocnavi

}} 

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)

---
[documentation index](../README.md) > [Developer Documentation](Category:Developer Documentation.md) > PySide Beginner Examples/es
