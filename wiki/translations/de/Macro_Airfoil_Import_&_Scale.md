# Macro Airfoil Import & Scale/de
{{Macro/de
|Name=Macro Airfoil Import & Scale
|Translate=Macro Airfoil Import & Scale
|Icon=Macro_Airfoil_Import_&_Scale.png
|Description=Verfolgen Sie den Umfang eines Airfoil aus einer DAT-Datei.
|Author=quick61
|Version=2.1.2
|Date=2019-07-16
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/0/0c/Macro_Airfoil_Import_%26_Scale.png ToolBar Icon]
}}

## Beschreibung

Wenn dieses Makro ausgeführt wird, wird es dem Benutzer zunächst mit einem Dateibrowser zur Verfügung gestellt, um eine .dat-Profildatei zu finden und auszuwählen. Nach der Auswahl wird eine Akkordlänge eingegeben und beim Drücken der OK-Taste wird ein ordnungsgemäß skaliertes Strömungsprofil erzeugt. Hier gibt es zwei Versionen. Version 1.5 sollte auf FreeCAD-Versionen funktionieren, 0,13 stabil sowie alle 0,14-Versionen. Version 2 sollte nur mit FreeCAD-Versionen größer oder gleich 0,14 3077 verwendet werden und funktioniert am besten mit Versionen, die mit OCE/OCC-Versionen 6.7 oder höher erstellt wurden.

Siehe auch [Common Airfoil Data Import](Common_Airfoil_Data_Import.md)

<img alt="" src=images/Macro_Airfoil_Import_&_Scale_00.png  style="width:480px;">

## Wie benutzt man - Version 1.5 

### Wähle die Datei 

Beim Ausführen des Makros wird dem Benutzer zunächst ein Dateibrowser angezeigt, in dem Sie die gewünschte DAT-Datei auswählen können. Navigieren Sie zu dem Speicherort der Airfoil-Datei, wählen Sie sie aus und drücken Sie Öffnen.

![File browser window for importing .dat airfoil files](images/File_browser.png )

### Geben Sie die Akkordlänge ein 

Nachdem die Airfoil-Datei ausgewählt wurde, erscheint ein neuer Dialog, in dem Sie nach einer Akkordlänge gefragt werden. Jede Länge kann in Millimetern eingegeben werden. Nachdem Sie die gewünschte Länge eingegeben haben, erzeugt das Makro einen Zugdraht (DWire), der den Punkten entspricht, die in der zuvor ausgewählten .dat-Profildatei auf der für die Akkordlänge eingegebenen Skala angegeben sind.

![Chord length dialog for import and scale macro v1.5](images/Chord_length.png )

Das Airfoil ist nun richtig skaliert und kann nun in Ihrem Projekt verwendet werden.

## Verwendung - Version 2 

Die Dateiauswahl entspricht der Version 1.5. Mit Version 2 haben Sie nun die Wahl, entweder das resultierende Profil mit einem Zugseil (DWire) oder einem Basic Spline (BSpline) herstellen zu lassen. Wie bei Version 1.5 geben Sie die gewünschte Akkordlänge ein. Zusätzlich können Sie jetzt auswählen, welchen Folientyp Sie wünschen. Klicken Sie einfach auf das Optionsfeld BSpline oder belassen Sie es wie für das Standard-DWire.

![Version 2 Airfoil Import and scale dialog with choice of DWire or BSpline](images/V2_scale.png )

## Makros

## Neueste Version 

Die neueste Version des Makros ist zu finden auf [AirfoilImportAndScale.FCMacro](https://github.com/FreeCAD/FreeCAD-macros/blob/master/ObjectCreation/AirfoilImportAndScale.FCMacro), aber der einfachste Weg zur Installation dieses Makros ist die Nutzung des [Addon-Managers](Std_AddonMgr/de.md).

### Version 2.1.2 

ToolBar icon ![](images/Macro_Airfoil_Import_&_Scale.png )

**Macro_Airfoil_Import\_&\_Scale.FCMacro**


{{MacroCode|code=
<nowiki>

# This Macro, when run, will first provide the user with a file browser to
# locate and select a .dat airfoil text file. Once selected, a chord length is
# entered and upon pressing the OK button, a properly scaled airfoil is
# produced. There are two versions provided here. Version 1.5 should work on
# FreeCAD versions, 0.13 stable as well as all 0.14 versions. Version 2 should
# only be used with FreeCAD versions equal to or greater than 0.14 3077 and
# will work best with versions built with OCE/OCC versions 6.7 or greater (See
# the Wiki page for all available version).
#
# (c) quick61

__Name__ = 'Airfoil Import and Scale'
__Comment__ = 'Imports and scales an Airfoil in the form of a Draft Wire (DWire) or Basic Spline (BSpline)'
__Author__ = "quick61"
__Version__ = '2.1.2'
__Date__ = '2019-07-16'
__License__ = ''
__Web__ = "http://forum.freecadweb.org/viewtopic.php?f=22&t=5554"
__Wiki__ = "http://www.freecadweb.org/wiki/Macro_Airfoil_Import_%26_Scale"
__Icon__ = 'https://www.freecadweb.org/wiki/images/0/0c/Macro_Airfoil_Import_%26_Scale.png'
__Help__ = ''
__Status__ = 'stable'
__Requires__ = 'Freecad >= 0.14.3706'
__Communication__ = ''
__Files__ = ''


import FreeCAD as app
import PySide
from PySide import QtCore, QtGui
from PySide.QtGui import QLineEdit, QRadioButton
import Draft
import importAirfoilDAT


# Select .dat airfoil data file to be imported

# PySide returns a tuple (filename, filter) instead of just a string like in PyQt

global filename
global nameFile

try:
    filename, filefilter = QtGui.QFileDialog.getOpenFileName(QtGui.qApp.activeWindow(), 'Open An Airfoil File', '*.dat')
except Exception:
    param = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Macro")# macro path
    path = param.GetString("MacroPath","") + "/"                        # macro path
    filename, filefilter = PySide.QtGui.QFileDialog.getOpenFileName(None, "Open An Airfoil File", path, "*.dat")

nameFile = filename.split("/")[-1][:-4]

class AirfoilImporterAndScaler():
    def __init__(self):
        self.dialog = None
        self.s1 = None

        # Make dialog box and get the scale size
        self.dialog = QtGui.QDialog()
        self.dialog.resize(350,100)
        self.dialog.setWindowTitle("Airfoil Import & Scale")
        la = QtGui.QVBoxLayout(self.dialog)
        t1 = QtGui.QLabel("Chord Length")
        la.addWidget(t1)
        self.s1 = QtGui.QLineEdit()
        la.addWidget(self.s1)

        # Add radio buttons to select between DWire and BSpline
        self.radio1 = QtGui.QRadioButton("Make DWire")
        self.radio2 = QtGui.QRadioButton("Make BSpline")

        # set default to DWire & make radio buttons - Change self.radio1.setChecked(True) to
        # self.radio2.setChecked(True) to set BSpline as default

        self.radio1.setChecked(True)
        la.addWidget(self.radio1)
        la.addWidget(self.radio2)

        # Add OK / Cancel buttons
        okbox = QtGui.QDialogButtonBox(self.dialog)
        okbox.setOrientation(QtCore.Qt.Horizontal)
        okbox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        la.addWidget(okbox)
        QtCore.QObject.connect(okbox, QtCore.SIGNAL("accepted()"), self.proceed)
        QtCore.QObject.connect(okbox, QtCore.SIGNAL("rejected()"), self.close)
        QtCore.QMetaObject.connectSlotsByName(self.dialog)
        self.dialog.show()
        self.dialog.exec_()



    def proceed(self):
        global filename
        global nameFile

        if self.radio1.isChecked():
            try:
                # This produces a scaled Airfoil with a DWire
                scalefactor=float(self.s1.text())
                f1=str(filename)
                importAirfoilDAT.insert(f1,"Unnamed")
                try:
                    Draft.scale(App.ActiveDocument.ActiveObject,delta=App.Vector(scalefactor,scalefactor,scalefactor),center=App.Vector(0,0,0),legacy=True)
                except Exception:
                    Draft.scale(App.ActiveDocument.ActiveObject,scale=App.Vector(scalefactor,scalefactor,scalefactor),center=App.Vector(0.0,0.0,0.0),copy=False)
                
                App.ActiveDocument.ActiveObject.Label = nameFile + "_(DWire)"

            except Exception as e:
                app.Console.PrintError("Error, not a valid .dat file\n")

        if self.radio2.isChecked():
            try:
                # This produces a scaled Airfoil with a BSpline
                scalefactor=float(self.s1.text())
                f1=str(filename)
                importAirfoilDAT.insert(f1,"Unnamed")
                points = app.ActiveDocument.ActiveObject.Points
                App.getDocument("Unnamed").removeObject(App.ActiveDocument.ActiveObject.Name)
                Draft.makeBSpline(points, closed=True)
                try:
                    Draft.scale(App.ActiveDocument.ActiveObject,delta=App.Vector(scalefactor,scalefactor,scalefactor),center=App.Vector(0,0,0),legacy=True)
                except Exception:
                    for i in range(len(points)):
                        Draft.scaleVertex(App.ActiveDocument.ActiveObject, i, App.Vector(scalefactor,scalefactor,scalefactor), App.Vector(0.0,0.0,0.0))

                App.ActiveDocument.ActiveObject.Label = nameFile + "_(BSpline)"

            except:
                app.Console.PrintError("Error, not a valid .dat file\n")

        try:    
            # delete the directory created by importAirfoilDAT
            for obj in App.ActiveDocument.Objects:
                if (obj.TypeId == "App::DocumentObjectGroup") and (obj.Name == nameFile):
                    App.getDocument("Unnamed").removeObject(nameFile)
        except Exception:
            None

        self.close()    # close the window

    def close(self):
        self.dialog.hide()


AirfoilImporterAndScaler()

</nowiki>
}}

### Version 1.5 

**Macro_Airfoil_Import\_&\_Scale.FCMacro**


{{MacroCode|code=
# # # #
#
# AIRFOIL IMPORT & SCALE v1.5
# 
# Imports and scales an Airfoil in the form of a Draft Wire (DWire) 
#
# # # #


from PySide import QtCore, QtGui
from PySide.QtGui import QLineEdit
import FreeCAD, FreeCADGui, Draft
import importAirfoilDAT

# Select .dat airfoil data file to be imported

filename = QtGui.QFileDialog.getOpenFileName(QtGui.qApp.activeWindow(),'Open An Airfoil File','*.dat')

class p():

    def proceed(self):
            try:
                
                # This produces a scaled Airfoil with a DWire

                scalefactor=float(self.s1.text())
                f1=str(filename)
                importAirfoilDAT.insert(f1,"Unnamed")
                Draft.scale(App.ActiveDocument.ActiveObject,delta=App.Vector(scalefactor,scalefactor,scalefactor),center=App.Vector(0,0,0),legacy=True)
            
            except:
                FreeCAD.Console.PrintError("Error, not a valid .dat file\n")

            self.close()

    def close(self):
        self.dialog.hide()

    def __init__(self):
        self.dialog = None
        self.s1 = None

        # Make dialog box and get the scale size

        self.dialog = QtGui.QDialog()
        self.dialog.resize(350,100)
        self.dialog.setWindowTitle("Airfoil Import & Scale")
        la = QtGui.QVBoxLayout(self.dialog)
        t1 = QtGui.QLabel("Chord Length")
        la.addWidget(t1)
        self.s1 = QtGui.QLineEdit()
        la.addWidget(self.s1)

        # Add OK / Cancel buttons

#ori        okbox = QtGui.QDialogButtonBox(self.dialog)
#ori        okbox.setOrientation(QtCore.Qt.Horizontal)
#ori        okbox.setStandardButtons(QtGui.QDialogButtonBox.Cancel -PIPE- QtGui.QDialogButtonBox.Ok)
#        modify original code for install with addon-install cause -PIPE- 05-12-2016 FC 0.16

        okbox = QtGui.QDialogButtonBox(self.dialog)
        okbox.setOrientation(QtCore.Qt.Horizontal)
        okbox.setStandardButtons(QtGui.QDialogButtonBox.Ok)

        cancelbox = QtGui.QDialogButtonBox(self.dialog)
        cancelbox.setOrientation(QtCore.Qt.Horizontal)
        cancelbox.setStandardButtons(QtGui.QDialogButtonBox.Cancel)
        cancelbox.move(0,62)

        la.addWidget(okbox)
        QtCore.QObject.connect(okbox, QtCore.SIGNAL("accepted()"), self.proceed)
        QtCore.QObject.connect(cancelbox, QtCore.SIGNAL("rejected()"), self.close)
        QtCore.QMetaObject.connectSlotsByName(self.dialog)
        self.dialog.show()
        self.dialog.exec_()

p()

}}

## Bearbeiten der Standardauswahl 

Wenn Sie vor allem möchten, dass Ihre importierten und skalierten Tragflächen mit BSplines anstatt mit DWires erstellt werden, kann der Marco so bearbeitet werden, dass er standardmäßig auf Bspline gesetzt wird. Dies geschieht durch Editieren der Zeile - {{ExampleCode|example=
self.radio1.setChecked(True)
}}
- und ändern Sie es in -
{{ExampleCode|example=
self.radio2.setChecked(True)
}}
Ein Hinweis dazu ist im Text des Makros enthalten.

## Version 2 


**'''Warning - Bei Verwendung dieses Makros mit weniger als 0.14-Versionen von FreeCAD liefert die Version 3077 bei Verwendung der Option BSpline nicht die erwarteten Ergebnisse. Dies kann zum Absturz von FreeCAD und zum Verlust nicht gespeicherter Daten führen
!'''**


{{MacroCode|code=
<nowiki>
# # # #
#
# AIRFOIL IMPORT & SCALE v2.
# 
# Imports and scales an Airfoil in the form of a Draft Wire (DWire) or Basic Spline (BSpline)
#
# For FreeCAD Versions = or > 0.14 Revision 3077
#
# Works best with OCC/OCE = or > 6.7
#
# # # #


from PySide import QtCore, QtGui
from PySide.QtGui import QLineEdit, QRadioButton
import FreeCAD, FreeCADGui, Draft
import importAirfoilDAT

# Select .dat airfoil data file to be imported

filename = QtGui.QFileDialog.getOpenFileName(QtGui.qApp.activeWindow(),'Open An Airfoil File','*.dat')

class p():

    def proceed(self):
        if self.radio1.isChecked():
            try:
                
                # This produces a scaled Airfoil with a DWire

                scalefactor=float(self.s1.text())
                f1=str(filename)
                importAirfoilDAT.insert(f1,"Unnamed")
                Draft.scale(App.ActiveDocument.ActiveObject,delta=App.Vector(scalefactor,scalefactor,scalefactor),center=App.Vector(0,0,0),legacy=True)
            
            except:
                FreeCAD.Console.PrintError("Error, not a valid .dat file\n")

            self.close()

        if self.radio2.isChecked():
            try:

                # This produces a scaled Airfoil with a BSpline

                scalefactor=float(self.s1.text())
                f1=str(filename)
                importAirfoilDAT.insert(f1,"Unnamed")
                points = FreeCAD.ActiveDocument.ActiveObject.Points
                Draft.makeBSpline(points, closed=True)
                Draft.scale(App.ActiveDocument.ActiveObject,delta=App.Vector(scalefactor,scalefactor,scalefactor),center=App.Vector(0,0,0),legacy=True)
                App.getDocument("Unnamed").removeObject("DWire")

            except:
                FreeCAD.Console.PrintError("Error, not a valid .dat file\n")

            self.close()

    def close(self):
        self.dialog.hide()


    def __init__(self):
        self.dialog = None
        self.s1 = None


        # Make dialog box and get the scale size

        self.dialog = QtGui.QDialog()
        self.dialog.resize(350,100)
        self.dialog.setWindowTitle("Airfoil Import & Scale")
        la = QtGui.QVBoxLayout(self.dialog)
        t1 = QtGui.QLabel("Chord Length")
        la.addWidget(t1)
        self.s1 = QtGui.QLineEdit()
        la.addWidget(self.s1)

        # Add radio buttons to select between DWire and BSpline

        self.radio1 = QRadioButton("Make DWire")
        self.radio2 = QRadioButton("Make BSpline")

            # set default to DWire & make radio buttons - Change self.radio1.setChecked(True) to
            # self.radio2.setChecked(True) to set BSpline as default

        self.radio1.setChecked(True)
        la.addWidget(self.radio1)
        la.addWidget(self.radio2)

        # Add OK / Cancel buttons

        okbox = QtGui.QDialogButtonBox(self.dialog)
        okbox.setOrientation(QtCore.Qt.Horizontal)
        okbox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        la.addWidget(okbox)
        QtCore.QObject.connect(okbox, QtCore.SIGNAL("accepted()"), self.proceed)
        QtCore.QObject.connect(okbox, QtCore.SIGNAL("rejected()"), self.close)
        QtCore.QMetaObject.connectSlotsByName(self.dialog)
        self.dialog.show()
        self.dialog.exec_()

p()
</nowiki>
}}

### Version 2.1 

Updated by mangtronix to use PySide instead of PyQt (used in older versions of FreeCAD)


{{MacroCode|code=
<nowiki>
# # # #
#
# AIRFOIL IMPORT & SCALE v2.1
# 
# Imports and scales an Airfoil in the form of a Draft Wire (DWire) or Basic Spline (BSpline)
#
# For FreeCAD Versions = or > 0.14 Revision 3703
#
# Works best with OCC/OCE = or > 6.7
#
# # # #
 
 
from PySide import QtCore, QtGui
from PySide.QtGui import QLineEdit, QRadioButton
import FreeCAD, FreeCADGui, Draft
import importAirfoilDAT
 
# Select .dat airfoil data file to be imported
 
# PySide returns a tuple (filename, filter) instead of just a string like in PyQt
filename, filefilter = QtGui.QFileDialog.getOpenFileName(QtGui.qApp.activeWindow(),'Open An Airfoil File','*.dat')

class p():
 
    def proceed(self):
        global filename
        if self.radio1.isChecked():
            #if True:
            try:
 
                # This produces a scaled Airfoil with a DWire
 
                scalefactor=float(self.s1.text())
                f1=str(filename)
                importAirfoilDAT.insert(f1,"Unnamed")
                Draft.scale(App.ActiveDocument.ActiveObject,delta=App.Vector(scalefactor,scalefactor,scalefactor),center=App.Vector(0,0,0),legacy=True)
 
            except Exception, e:
                FreeCAD.Console.PrintError("Error, not a valid .dat file\n")
 
            self.close()
 
        if self.radio2.isChecked():
            try:
 
                # This produces a scaled Airfoil with a BSpline
 
                scalefactor=float(self.s1.text())
                f1=str(filename)
                importAirfoilDAT.insert(f1,"Unnamed")
                points = FreeCAD.ActiveDocument.ActiveObject.Points
                Draft.makeBSpline(points, closed=True)
                Draft.scale(App.ActiveDocument.ActiveObject,delta=App.Vector(scalefactor,scalefactor,scalefactor),center=App.Vector(0,0,0),legacy=True)
                App.getDocument("Unnamed").removeObject("DWire")
 
            except:
                FreeCAD.Console.PrintError("Error, not a valid .dat file\n")
 
            self.close()
 
    def close(self):
        self.dialog.hide()
 
 
    def __init__(self):
        self.dialog = None
        self.s1 = None
 
 
        # Make dialog box and get the scale size
 
        self.dialog = QtGui.QDialog()
        self.dialog.resize(350,100)
        self.dialog.setWindowTitle("Airfoil Import & Scale")
        la = QtGui.QVBoxLayout(self.dialog)
        t1 = QtGui.QLabel("Chord Length")
        la.addWidget(t1)
        self.s1 = QtGui.QLineEdit()
        la.addWidget(self.s1)
 
        # Add radio buttons to select between DWire and BSpline
 
        self.radio1 = QRadioButton("Make DWire")
        self.radio2 = QRadioButton("Make BSpline")
 
            # set default to DWire & make radio buttons - Change self.radio1.setChecked(True) to
            # self.radio2.setChecked(True) to set BSpline as default
 
        self.radio1.setChecked(True)
        la.addWidget(self.radio1)
        la.addWidget(self.radio2)
 
        # Add OK / Cancel buttons
 
        okbox = QtGui.QDialogButtonBox(self.dialog)
        okbox.setOrientation(QtCore.Qt.Horizontal)
        okbox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        la.addWidget(okbox)
        QtCore.QObject.connect(okbox, QtCore.SIGNAL("accepted()"), self.proceed)
        QtCore.QObject.connect(okbox, QtCore.SIGNAL("rejected()"), self.close)
        QtCore.QMetaObject.connectSlotsByName(self.dialog)
        self.dialog.show()
        self.dialog.exec_()
 
p()
</nowiki>
}}

## Link

Diskussion über [Forum](http://forum.freecadweb.org/viewtopic.php?f=22&t=5554&p=45137&hilit=Airfoil#p45137)

[UIUC Applied Aerodynamics Group Departement of Aerospace Engineering](http://aerospace.illinois.edu/m-selig/ads/coord_database.html#N)



---
⏵ [documentation index](../README.md) > Macro Airfoil Import & Scale/de
