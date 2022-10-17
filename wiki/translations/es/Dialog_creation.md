# Dialog creation/es
{{TOCright}}

## Introduction


<div class="mw-translate-fuzzy">

En esta página vamos a mostrar cómo crear un simple letrero de diálogo con [Qt Designer](http   *//qt-project.org/doc/qt-4.8/designer-manual.html), la herramienta oficial de Qt para el diseño de interfaces, después lo convertiremos en código de Python, para luego utilizarlo en FreeCAD. Vamos a suponer en el ejemplo que ya sabes cómo editar y ejecutar archivos de guión de Python, y que puedes hacer cosas simples en una ventana de terminal, como navegar, etc. También debes tener, por supuesto, PyQt instalado.


</div>

In this example, the entire interface is defined in [Python](Python.md). Although this is possible for small interfaces, for larger interfaces the recommendation is to load the created **.ui** files directly into the program.

<img alt="" src=images/FreeCAD_creating_interfaces.svg  style="width   *600px;"> 
*Two general methods to create interfaces, by including the interface in the Python file, or by using `.ui* files.`


<div class="mw-translate-fuzzy">

## Diseñar el letrero de diálogo 

En las aplicaciones de CAD, el diseño de una buena interfaz de usuario (UI, User Interface) es muy importante. Casi todo lo que el usuario haga será a través de alguna parte de la interfaz   * leyendo los letreros de diálogo, pulsando los botones, eligiendo entre iconos, etc. Así que es muy importante pensar cuidadosamente lo que quieres hacer, cómo deseas que el usuario se comporte, y cómo será el flujo de trabajo de tu acción.


</div>

In CAD applications, designing a good UI (User Interface) is very important. About everything the user will do will be through some piece of interface   * reading dialog boxes, pressing buttons, choosing between icons, etc. So it is very important to think carefully to what you want to do, how you want the user to behave, and how will be the workflow of your action.

Hay un par de conceptos que debes saber a la hora de diseñar la interfaz   *

-   [Letreros de diálogo Modales/no modales](http   *//en.wikipedia.org/wiki/Modal_window)   * Un letrero de diálogo modal aparece delante de la pantalla, deteniendo la acción de la ventana principal, obligando al usuario a responder al cuadro de diálogo, mientras que un cuadro de diálogo no modal permite seguir trabajando en la ventana principal. En algunos casos la primera opción es mejor, pero en otros casos no.
-   Identificación de lo que es necesario y lo que es opcional   * Asegúrate de que el usuario sabe lo que debe hacer. Etiqueta todo con la descripción adecuada, utiliza etiquetas de información sobre el uso de las herramientas, etc.
-   Separar los comandos de los parámetros   * Esto se hace generalmente con botones y cuadros de texto. El usuario sabe que al hacer clic en un botón, se produce una acción mientras que al cambiar un valor dentro de un cuadro de texto va a cambiar un parámetro en alguna parte. Hoy en día, sin embargo, los usuarios suelen conocer bien lo que es un botón, lo que es un cuadro de texto, etc. El conjunto de herramientas de interfaz que está utilizando, Qt, es el conjunto de herramientas más avanzado, y no tendrás que preocuparte mucho de hacer las cosas claras, puesto que ya va a ser muy clara por sí misma.

Así que, ahora que tenemos bien definido lo que haremos, es el momento para abrir el diseñador de Qt Designer. Diseñemos un letrero de diálogo muy sencillo, como este   *

![](images/Qttestdialog.jpg )

Después podremos utilizar este letrero de diálogo en FreeCAD para producir un bonito plano rectangular. Puede que no veas muy útil hacer planos rectangulares, pero será fácil cambiarlo más adelante para hacer cosas más complejas. Cuando lo abras, el aspecto de Qt Designer es el siguiente   *

![](images/Qtdesigner-screenshot.jpg )


<div class="mw-translate-fuzzy">

Es muy sencillo de utilizar. En la barra de la izquierda tienes elementos que pueden ser arrastrados a tu widget. En el lado derecho tienes los paneles de propiedades mostrando todo tipo de propiedades editables de los elementos seleccionados. Comencemos ahora con la creación de un nuevo widget o complemento. Selecciona \"letrero de diálogo sin botones\", ya que no queremos el formato predeterminado de botones Ok/Cancelar. A continuación, arrastra sobre tu widget **3 etiquetas**, una para el título, una para escribir \"Altura\" y otra para escribir \"Ancho\". Las etiquetas son textos sencillos que aparecen en tu widget, simplemente para informar al usuario. Si seleccionas una etiqueta, en la parte derecha aparecerán varias propiedades que puedes cambiar si lo deseas, como el estilo de fuente, altura, etc.


</div>


<div class="mw-translate-fuzzy">

Ten en cuenta que he elegido aquí controles muy sencillos, pero Qt tiene muchas más opciones, por ejemplo, podría utilizar Spinboxes en lugar de LineEdits, etc. Echa un vistazo a lo que está disponible, seguramente tendrás otras ideas.


</div>


<div class="mw-translate-fuzzy">

Eso es prácticamente todo lo que necesitamos hacer en Qt Designer. Una última cosa, sin embargo, vamos a cambiar el nombre de todos nuestros elementos con nombres más adecuados, de modo que sea más fácil identificarlos en nuestros archivos de guión   *


</div>

![](images/Qtpropeditor.jpg )

## Convertir nuestro diálogo a Python 

Ahora, vamos a salvar nuestro widget en alguna parte. Se guardará como un archivo .ui, que fácilmente se convertirá en un archivo de guión de Python por medio de pyuic. En Windows, el programa pyuic se ve enriquecido con PyQt (por verificar), en linux es probable que tengas que instalarlo por separado desde tu gestor de paquetes (en sistemas basados en Debian, es parte del paquete de herramientas PyQt4-dev-tools). Para realizar la conversión, tendrás que abrir una ventana de terminal (o una ventana de símbolo de sistema en Windows), ve a donde guardaste el archivo .ui, y escribe   * 
```python
pyuic mywidget.ui > mywidget.py
``` In Windows pyuic.py is located in \"C   *Python27\\Lib\\site-packages\\PyQt4\\uic\\pyuic.py\" For conversion create a batch file called \"compQt4.bat   * 
```python
@"C   *Python27\python" "C   *Python27\Lib\site-packages\PyQt4\uic\pyuic.py" -x %1.ui > %1.py
``` In the DOS console type without extension 
```python
compQt4 myUiFile
```

In macOS, you can retrieve the appropriate version (the same that is used internally in FreeCAD 0.19) of QT and Pyside with these commands (pip required) 
```python
python3 -m pip install pyqt5
python3 -m pip install pySide2
``` This will install uic in the folder \"/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/PySide2/uic\", and Designer in \"/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/PySide2/Designer.app\". For convenience you can create a link of uic in /usr/local/bin to be able to call it simply with uic -g python \... instead of typing the whole path of the program, and a link to Designer to retrieve it in the mac\'s Applications folder with 
```python
sudo ln -s /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/PySide2/uic /usr/local/bin
ln -s /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/PySide2/Designer.app /Applications
```

Into Linux    * to do

Since FreeCAD progressively moved away from PyQt after version 0.13, in favour of [PySide](http   *//qt-project.org/wiki/PySide) (Choose your PySide install [building PySide](http   *//pyside.readthedocs.org/en/latest/building/)), to make the file based on PySide now you have to use   *


```python
pyside-uic mywidget.ui -o mywidget.py
```

In Windows uic.py are located in \"C   *Python27\\Lib\\site-packages\\PySide\\scripts\\uic.py\" For create batch file \"compSide.bat\"   * 
```python
@"C   *Python27\python" "C   *Python27\Lib\site-packages\PySide\scripts\uic.py" %1.ui > %1.py
``` In the DOS console type without extension 
```python
compSide myUiFile
``` Into Linux    * to do


<div class="mw-translate-fuzzy">

En algunos sistemas el programa se llama pyuic4 en lugar de pyuic. Esta operación simplemente convertirá el archivo .ui en un archivo de guión de Python. Si abrimos el archivo mywidget.py, su contenido es muy fácil de entender   *


</div>


```python
from PySide import QtCore, QtGui

class Ui_Dialog(object)   *
    def setupUi(self, Dialog)   *
        Dialog.setObjectName("Dialog")
        Dialog.resize(187, 178)
        self.title = QtGui.QLabel(Dialog)
        self.title.setGeometry(QtCore.QRect(10, 10, 271, 16))
        self.title.setObjectName("title")
        self.label_width = QtGui.QLabel(Dialog)
        ...

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

   def retranslateUi(self, Dialog)   *
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.title.setText(QtGui.QApplication.translate("Dialog", "Plane-O-Matic", None, QtGui.QApplication.UnicodeUTF8))
        ...
```


<div class="mw-translate-fuzzy">

Como verás, tiene una estructura muy simple   * se crea una clase denominada Ui_Dialog, que almacena los elementos de interfaz de nuestro widget o complemento. Esa clase tiene dos métodos, uno para la configuración del widget, y otro para la traducción de su contenido, eso es parte del mecanismo general de Qt para la traducción de elementos de la interfaz. El método de configuración simplemente crea, uno a uno, los widgets tal como los has definido en Qt Designer, y establece sus opciones, como hayamos decidido con anterioridad. Despues, toda la interfaz se traduce, y por último, se conectan las ranuras (slots) (hablaremos de eso más adelante).


</div>


<div class="mw-translate-fuzzy">

Ahora podemos crear un nuevo widget, y utilizar esta clase para crear su interfaz. Ya podemos ver nuestro widget en acción, poniendo nuestro archivo mywidget.py en un lugar donde FreeCAD lo encuentre (en el directorio bin de FreeCAD, o en cualquiera de los subdirectorios Mod), y, en el intérprete de Python FreeCAD, ejecutamos   *


</div>


```python
from PySide import QtGui
import mywidget
d = QtGui.QWidget()
d.ui = mywidget.Ui_Dialog()
d.ui.setupUi(d)
d.show()
```


<div class="mw-translate-fuzzy">

¡Y nuestro letrero de diálogo aparecerá! Ten en cuenta que nuestro intérprete de Python todavía está trabajando, ya que hemos usado un letrero de diálogo no modal. Por lo tanto, para cerrarlo, podemos (aparte de hacer clic en el icono de cerrar, por supuesto) escribir   *


</div>


```python
d.hide()
```

## Hacer algo con nuestro diálogo 

Ahora que podemos mostrar y ocultar nuestro letrero de diálogo, sólo tenemos que añadir una última parte   * ¡que haga algo! Si juegas un poco con Qt Designer, descubrirás rápidamente toda una sección llamada \"señales y slots\". Básicamente, funciona así   * los elementos de los widgets o complementos (en la terminología de Qt, estos elementos son a su vez widgets) pueden enviar señales. Estas señales varían según el tipo de widget. Por ejemplo, un botón puede enviar una señal cuando se presiona y cuando es soltado. Estas señales se pueden conectar a los slots, que puede ser una funcionalidad especial de otros widgets (por ejemplo, un cuadro de diálogo tiene un slot \"close\" (cerrado) en el que se puede conectar la señal de un botón close (de cierre)), o pueden ser funciones de usuario. La [Documentación de referencia de PyQt](http   *//www.riverbankcomputing.co.uk/static/Docs/PyQt4/html/classes.html) enumera todos los widgets Qt, lo que pueden hacer, que señales pueden enviar, etc.

Lo que haremos aquí, es crear una nueva función que va a formar un plano basado en la altura y anchura, y conectar dicha función a la señal de \"pulsado\" emitida por nuestro botón \"Create!\". Empezaremos con la importación de nuestros módulos FreeCAD, poniendo la siguiente línea al comienzo del archivo de guión, donde ya hemos mandado también la importación de QtCore y QtGui   * 
```python
import FreeCAD, Part
``` ahora, añadamos una nueva función a nuestra clase Ui_Dialog   * 
```python
def createPlane(self)   *
    try   *
        # first we check if valid numbers have been entered
        w = float(self.width.text())
        h = float(self.height.text())
    except ValueError   *
        print("Error! Width and Height values must be valid numbers!")
    else   *
        # create a face from 4 points
        p1 = FreeCAD.Vector(0,0,0)
        p2 = FreeCAD.Vector(w,0,0)
        p3 = FreeCAD.Vector(w,h,0)
        p4 = FreeCAD.Vector(0,h,0)
        pointslist = [p1,p2,p3,p4,p1]
        mywire = Part.makePolygon(pointslist)
        myface = Part.Face(mywire)
        Part.show(myface)
        self.hide()
``` A continuación, tenemos que informar a Qt para que conecte el botón con la función, mediante la colocación de la siguiente línea justo antes de QtCore.QMetaObject.connectSlotsByName(Dialog)   * 
```python
QtCore.QObject.connect(self.create,QtCore.SIGNAL("pressed()"),self.createPlane)
``` Como ves, esto conecta la señal pressed() de nuestro objeto create (el Botón \"Create!\"), a un slot llamado createPlane, que acabamos de definir. Eso es! Ahora, como toque final, podemos añadir una pequeña función para crear el cuadro de diálogo. Así será más fácil hacer las llamadas. Fuera de la clase Ui_Dialog, vamos a añadir este código   * 
```python
class plane()   *
   def __init__(self)   *
       self.d = QtGui.QWidget()
       self.ui = Ui_Dialog()
       self.ui.setupUi(self.d)
       self.d.show()
``` (Python reminder   * the \_\_init\_\_ method of a class is automatically executed whenever a new object is created!)

A continuación, en FreeCAD, sólo tenemos que hacer   * 
```python
import mywidget
myDialog = mywidget.plane()
``` Y eso es todo amigos\... Ahora puedes probar todo tipo de cosas, como por ejemplo insertar tu widget en la interfaz de FreeCAD (mira la página [Pedazos de código](Code_snippets/es.md)), o la creación de herramientas personalizadas mucho más avanzado, mediante el uso de otros elementos en tu widget o complemento.

## El archivo de guión completo 

Este es el archivo de guión completo, como referencia   * 
```python
# Form implementation generated from reading ui file 'mywidget.ui'
#
# Created   * Mon Jun  1 19   *09   *10 2009
#      by   * PyQt4 UI code generator 4.4.4
# Modified for PySide 16   *02   *2015 
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import FreeCAD, Part 

class Ui_Dialog(object)   *
   def setupUi(self, Dialog)   *
       Dialog.setObjectName("Dialog")
       Dialog.resize(187, 178)
       self.title = QtGui.QLabel(Dialog)
       self.title.setGeometry(QtCore.QRect(10, 10, 271, 16))
       self.title.setObjectName("title")
       self.label_width = QtGui.QLabel(Dialog)
       self.label_width.setGeometry(QtCore.QRect(10, 50, 57, 16))
       self.label_width.setObjectName("label_width")
       self.label_height = QtGui.QLabel(Dialog)
       self.label_height.setGeometry(QtCore.QRect(10, 90, 57, 16))
       self.label_height.setObjectName("label_height")
       self.width = QtGui.QLineEdit(Dialog)
       self.width.setGeometry(QtCore.QRect(60, 40, 111, 26))
       self.width.setObjectName("width")
       self.height = QtGui.QLineEdit(Dialog)
       self.height.setGeometry(QtCore.QRect(60, 80, 111, 26))
       self.height.setObjectName("height")
       self.create = QtGui.QPushButton(Dialog)
       self.create.setGeometry(QtCore.QRect(50, 140, 83, 26))
       self.create.setObjectName("create")

       self.retranslateUi(Dialog)
       QtCore.QObject.connect(self.create,QtCore.SIGNAL("pressed()"),self.createPlane)
       QtCore.QMetaObject.connectSlotsByName(Dialog)

   def retranslateUi(self, Dialog)   *
       Dialog.setWindowTitle("Dialog")
       self.title.setText("Plane-O-Matic")
       self.label_width.setText("Width")
       self.label_height.setText("Height")
       self.create.setText("Create!")
       print("tyty")
   def createPlane(self)   *
       try   *
           # first we check if valid numbers have been entered
           w = float(self.width.text())
           h = float(self.height.text())
       except ValueError   *
           print("Error! Width and Height values must be valid numbers!")
       else   *
           # create a face from 4 points
           p1 = FreeCAD.Vector(0,0,0)
           p2 = FreeCAD.Vector(w,0,0)
           p3 = FreeCAD.Vector(w,h,0)
           p4 = FreeCAD.Vector(0,h,0)
           pointslist = [p1,p2,p3,p4,p1]
           mywire = Part.makePolygon(pointslist)
           myface = Part.Face(mywire)
           Part.show(myface)

class plane()   *
  def __init__(self)   *
      self.d = QtGui.QWidget()
      self.ui = Ui_Dialog()
      self.ui.setupUi(self.d)
      self.d.show()

```

## More examples 

-   [Dialog creation with various widgets](Dialog_creation_with_various_widgets.md) with `QPushButton`, `QLineEdit`, `QCheckBox`, `QRadioButton`, and others.
-   [Dialog creation reading and writing files](Dialog_creation_reading_and_writing_files.md) with `QFileDialog`.
-   [Dialog creation setting colors](Dialog_creation_setting_colors.md) with `QColorDialog`.
-   [Dialog creation image and animated GIF](Dialog_creation_image_and_animated_GIF.md) with `QLabel` and `QMovie`.
-   [PySide usage snippets](PySide_usage_snippets.md).
-   [Qt Example](Qt_Example.md)

## Relevant links 

-   [Manual   *Creating interface tools](Manual_Creating_interface_tools.md)


<div class="mw-translate-fuzzy">


{{docnav/es|Line drawing function/es|Licence/es}}


</div>




[Category   *Developer Documentation](Category_Developer_Documentation.md) [Category   *Python Code](Category_Python_Code.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Dialog creation/es
