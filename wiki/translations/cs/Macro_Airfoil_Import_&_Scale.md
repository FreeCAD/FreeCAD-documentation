# Macro Airfoil Import & Scale/cs
{{Macro/cs
|Name=Macro Airfoil Import & Scale
|Icon=Macro_Airfoil_Import_&_Scale.png
|Description=Trace the perimeter of a Airfoil from a .dat file.
|Author=quick61
|Version=2.1.2
|Date=2019-07-16
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/0/0c/Macro_Airfoil_Import_%26_Scale.png ToolBar Icon]
}}

## Popis

Toto makro při spuštění nejprve poskytne uživateli souborový prohlížeč, který vyhledá a vybere textový soubor profilu dat .dat. Po zvolení se zadá délka akordů a po stisknutí tlačítka OK se vytvoří správně měřítko profilu. K dispozici jsou zde dvě verze. Verze 1.5 by měla pracovat na verzích FreeCADu, 0.13 stabilních i všech verzích 0.14. Verze 2 by měla být použita pouze s verzemi FreeCAD rovnajícími se nebo vyššími než 0.14 3077 a bude fungovat nejlépe s verzemi vytvořenými s verzemi OCE / OCC verze 6.7 nebo vyšší.

See also [Common Airfoil Data Import](Common_Airfoil_Data_Import.md)

<img alt="" src=images/Macro_Airfoil_Import_&_Scale_00.png  style="width:480px;">

## Jak používat - verze 1.5 

### Vyberte soubor 

Spuštění makra nejprve zobrazí uživateli prohlížeč souborů, který vám umožní vybrat požadovaný soubor datového souboru. Projděte si, kam jste uložili soubor profilu, vyberte jej a stiskněte Otevřít.

![File browser window for importing .dat airfoil files](images/File_browser.png )

### Zadejte délku chordu 

Po výběru souboru profilu se objeví nové dialogové okno s žádostí o délku akordů. Může být zadána libovolná délka, v milimetrech. Po zadání požadované délky vytvoří makro předběžný vodič (DWire) podle bodů popsaných v dříve vybraném souboru profilu .dat v měřítku, které jste zadali pro délku akordy.

![Chord length dialog for import and scale macro v1.5](images/Chord_length.png )

Křídlový profil, správně měřítko, by nyní měl být ve vašem projektu připraven k použití.

## Jak používat - verze 2 

Volba souboru je stejná jako verze 1.5. S verzí 2 máte nyní možnost mít buď výsledný profil vytvořený pomocí DWire nebo Basic Spline (BSpline). Stejně jako u verze 1.5 zadáte požadovanou délku. Dále můžete vybrat, který typ fólie chcete. Stačí kliknout na přepínač BSpline nebo nechat jako výchozí DWire.

![Version 2 Airfoil Import and scale dialog with choice of DWire or BSpline](images/V2_scale.png )

## Makra

### Latest

The latest version of the macro is to be found at [AirfoilImportAndScale.FCMacro](https://github.com/FreeCAD/FreeCAD-macros/blob/master/ObjectCreation/AirfoilImportAndScale.FCMacro) but the easiest way to install this macro is through the [Addon Manager](Std_AddonMgr.md).

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

## Úprava výchozího výběru 

Pokud si přejete, aby vaše importované a zmenšené profilové lišty byly vytvořeny s BSplines spíše než s DWires, Marco může být předem nastaven na Bspline. To se provádí úpravou řádku - {{ExampleCode|example=
self.radio1.setChecked(True)
}}
- a změnu -
{{ExampleCode|example=
self.radio2.setChecked(True)
}}
Poznámka k tomuto je obsažena v textu makra.

## Version 2 


**'''Varování - pomocí tohoto makra s verzemi FreeCADu menší než 0,14, revize 3077 nebude produkovat očekávané výsledky při použití možnosti BSpline a může mít za následek zhroucení FreeCADu a ztrátu neuložených dat!'''**


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

## Odkaz

Diskuse o [Forum](http://forum.freecadweb.org/viewtopic.php?f=22&t=5554&p=45137&hilit=Airfoil#p45137)

[UIUC Applied Aerodynamics Group Departement of Aerospace Engineering](http://aerospace.illinois.edu/m-selig/ads/coord_database.html#N)



---
![](images/Button_right.svg) [documentation index](../README.md) > Macro Airfoil Import & Scale/cs
