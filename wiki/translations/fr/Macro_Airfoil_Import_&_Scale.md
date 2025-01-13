# Macro Airfoil Import & Scale/fr
{{Macro/fr
|Name=Macro Airfoil Import & Scale
|Icon=Macro_Airfoil_Import_&_Scale.png
|Description=Au démarrage de la macro, la fenêtre de configuration s'affiche. Entrez la longueur de la corde et choisissez le type de ligne désiré, DWire ou BSpline et cliquez sur le bouton OK pour voir la fenêtre de l'explorateur s'afficher choisissez le fichier pour construire le profil. Si un profil est sélectionné, lancez la macro la fenêtre de configuration s'affiche et le bouton Save est disponible. Si le bouton Save est cliqué, la fenêtre de l'explorateur s'affiche choisissez le chemin et un nom de fichier pour enregistrer votre profil sur disque,  la longueur de la corde et le type de fil sont ignorés seul les coordonnées X et Y sont enregistrés dans le fichier. 
|Author=quick61
|Version=3.0.0
|Date=2024-11-27
|FCVersion=All
|Download=[https://www.freecad.org/wiki/images/0/0c/Macro_Airfoil_Import_%26_Scale.png Icône de la barre d'outils]
}}

## Description

Au démarrage de la macro, la fenêtre de configuration s\'affiche. Entrez la longueur de la corde et choisissez le type de ligne désiré, DWire ou BSpline et cliquez sur le bouton **OK** pour voir la fenêtre de l\'explorateur s\'afficher choisissez le fichier pour construire le profil. Si un profil est sélectionné, lancez la macro la fenêtre de configuration s\'affiche et le bouton Save est disponible. Si le bouton **Save** est cliqué, la fenêtre de l\'explorateur s\'affiche choisissez le chemin et un nom de fichier pour enregistrer votre profil sur disque, la longueur de la corde et le type de fil sont ignorés seul les coordonnées X et Y sont enregistrées dans le fichier.

Voir aussi [Common Airfoil Data Import](Common_Airfoil_Data_Import/fr.md)

<img alt="" src=images/Macro_Airfoil_Import_&_Scale_00.png  style="width:480px;">



### Entrer la longueur de la corde 

Demande de longueur de corde. N\'importe quelle longueur peut être saisie, en millimètres. Une fois la longueur souhaitée saisie, la macro produira une Draft polyligne (DWire) suivant les points décrits dans le fichier de profil aérodynamique .dat précédemment sélectionné à l\'échelle que vous avez saisie pour la longueur de corde.

![Sélection du type de ligne](images/Import_Airfoil_Scale_Enter_V3.png )



### Sélectionner le fichier 

Après la configuration, un explorateur de fichiers s\'affiche et vous permettra de sélectionner le fichier .dat du profil aérodynamique souhaité. Accédez à l\'emplacement où vous avez enregistré le fichier de profil aérodynamique, sélectionnez-le et appuyez sur Ouvrir.

![Sélection du fichier](images/Import_Airfoil_Scale_Open_V3.png )



### Profil sélectionné 

Si le profil aérodynamique a été sélectionné dans la vue 3D, exécuter la macro et {{RadioButton|Save}} est disponible dans la boîte de dialogue.



### Profil sauvegardé 

Si le bouton {{RadioButton|TRUE|Save}} est activé la fenêtre de l\'explorateur de fichier apparait.

![Sauvegarde du fichier .dat](images/Import_Airfoil_Scale_Save_Enter_V3.png )

### Save

Spécifier un nom de fichier.

![Donner un nom au fichier](images/Import_Airfoil_Scale_Save_V3.png )

Le fichier est enregistré avec 150 points de définition et ne vérifie pas si la longueur du profil suit les règles NACA *(longueur 1 mm)*

Pour modifier la valeur de définition allez à :


**Outils**

→ **Éditer les paramètres...** \"BaseApp/Preferences/Macros/Airfoil_Import_and_Scale\" puis modifier la valeur **numberCut**.

Le fichier est enregistré sous le format \"Titre et coordonnées X Y séparés par des virgules\".

![Format du fichier NACA](images/Import_Airfoil_Scale_Format.png )



## La macro 

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
__Version__ = '3.0.0'
__Date__ = '2024-11-27'
__License__ = ''
__Web__ = "https://forum.freecad.org/viewtopic.php?f=22&t=5554"
__Wiki__ = "https://www.freecad.org/wiki/Macro_Airfoil_Import_%26_Scale"
__Icon__ = 'https://www.freecad.org/wiki/images/0/0c/Macro_Airfoil_Import_%26_Scale.png'
__Help__ = ''
__Naca__ = "http://airfoiltools.com/airfoil/index"
__Status__ = 'stable'
__Requires__ = 'Freecad >= 0.14.3706'
__Communication__ = ''
__Files__ = ''


import FreeCAD as app
import FreeCADGui as Gui
import PySide
from PySide import QtCore, QtGui
from PySide.QtGui import QLineEdit, QRadioButton
import Draft
import importAirfoilDAT
import os

# Select .dat airfoil data file to be imported
# PySide returns a tuple (filename, filter) instead of just a string like in PyQt

global filename
global nameFile

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

        self.s1 = QtGui.QDoubleSpinBox()
        self.s1.setDecimals(5)
        self.s1.setMinimum(-9999999.9999999)
        self.s1.setMaximum(9999999.9999999)
        self.s1.setSuffix(" mm (Length)")
        self.s1.setValue(1.0)
        la.addWidget(self.s1)

        ####
        self.FreeCAD_ParamGetSet = FreeCAD.ParamGet(u"User parameter:BaseApp/Preferences/Macros/Airfoil_Import_and_Scale")
        self.FreeCAD_ParamGetSet.SetString(u"Version", __Version__ + " (" + __Date__ + ")")
        self.numberCut = self.FreeCAD_ParamGetSet.GetInt("numberCut", 150)       # number of coordinates
        self.FreeCAD_ParamGetSet.SetInt("numberCut", self.numberCut)
        ####
        # Add radio buttons to select between DWire and BSpline
        self.radio1 = QtGui.QRadioButton("Make DWire")
        self.radio2 = QtGui.QRadioButton("Make BSpline")
        self.radio3 = QtGui.QRadioButton("Save")

        # set default to DWire & make radio buttons - Change self.radio1.setChecked(True) to
        # self.radio2.setChecked(True) to set BSpline as default

        self.radio1.setChecked(True)
        la.addWidget(self.radio1)
        self.radio1.setToolTip("Create DWire Airfoil")
        la.addWidget(self.radio2)
        self.radio2.setToolTip("Create BSplinee Airfoil")
        #### save button
        la.addWidget(self.radio3)
        self.numberCut = self.FreeCAD_ParamGetSet.GetInt("numberCut")       # number of coordinates
        self.radio3.setToolTip(u"Only available if one Airfoil to save is selected" + "\n"
                               u"The actual value of definition is " + str(self.numberCut) + " points" + "\n"
                               u"For change this value, go to" + "\n"
                               u"User parameter:BaseApp/Preferences/Macros/Airfoil_Import_and_Scale" + "\n"
                               u"Change the 'numberCut' value")
        self.radio3.setEnabled(False)
        selected = ""
        selected = FreeCADGui.Selection.getSelection()
        if len(selected) != 0:
            self.radio3.setEnabled(True)
        ####
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

        param = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Macro")# macro path
        macroPath = param.GetString("MacroPath","") + "/"                   # macro path

        filePath = ""
        filePath = self.FreeCAD_ParamGetSet.GetString(u"filePath", filePath)
        filePath = filePath.replace(u"\\","/")      # convert the "\" to "/"

        if filePath == "":
            filePath = self.FreeCAD_ParamGetSet.GetString(u"filePath", macroPath)

        if self.radio1.isChecked() or self.radio2.isChecked():

            OpenName, filefilter = QtGui.QFileDialog.getOpenFileName(None, "Open An Airfoil File", filePath, "*.dat")
            if OpenName != "":
                ####new2
                pathFile      = os.path.dirname(OpenName) + "/"  #1# = C:/Provisoire400/
                racineDrive   = os.path.splitdrive(OpenName)[0]  #2# = C:
                formatFichier = os.path.splitext(OpenName)[1]    #3# = .png
                OpenName      = os.path.splitext(OpenName)[0]    #4# = /home/kubuntu/.FreeCAD/Macro/Texture_007_H #= C:/Provisoire400/image3D
                nameFile      = os.path.basename(OpenName)       #5# = image3D
                SaveNameformatFichier = OpenName + formatFichier #6# = C:/Provisoire400/image3D.png
                pathFileSaveNameformatFichier = pathFile + nameFile + formatFichier #7# = C:/Provisoire400/image3D.png
                ####new2
                self.FreeCAD_ParamGetSet.SetString("filePath", pathFile)

                if self.radio1.isChecked():
                    try:
                        # This produces a scaled Airfoil with a DWire
                        scalefactor=self.s1.value()
                        f1=SaveNameformatFichier
                        importAirfoilDAT.insert(f1,"Unnamed")
                        points = FreeCAD.ActiveDocument.Wire
                        nacaDWire = Draft.scale([points], scale=FreeCAD.Vector(scalefactor,scalefactor,scalefactor), center=FreeCAD.Vector(0.0, 0.0, 0.0), copy=True)
                        nacaDWire.MakeFace = False
                        nacaDWire.Label = nameFile + "_(DWire)(" + str(scalefactor) + ")"
                    except Exception:
                        app.Console.PrintError("Error, not a valid .dat file\n")

                if self.radio2.isChecked():
                    try:
                        # This produces a scaled Airfoil with a BSpline
                        scalefactor=self.s1.value()
                        f1=SaveNameformatFichier
                        importAirfoilDAT.insert(f1,"Unnamed")
                        points = FreeCAD.ActiveDocument.Wire.Points
                        bspline = Draft.make_bspline(points, closed=True)
                        App.getDocument('Unnamed').recompute()
                        nacaBSpline = Draft.scale(bspline, scale=FreeCAD.Vector(scalefactor,scalefactor,scalefactor), center=FreeCAD.Vector(0.0, 0.0, 0.0), copy=True)
                        nacaBSpline.MakeFace = False
                        nacaBSpline.Label = nameFile + "_(BSpline)(" + str(scalefactor) + ")"
                        App.activeDocument().removeObject(bspline.Name)
                    except Exception:
                        app.Console.PrintError("Error, not a valid .dat file\n")

                try:    
                    App.getDocument("Unnamed").getObject(nameFile).removeObjectsFromDocument()
                    App.getDocument('Unnamed').removeObject(nameFile)
                    App.getDocument('Unnamed').recompute()
                except Exception:
                    None

                Gui.SendMsgToActiveView("ViewFit")
            self.close()    # close the window

        if self.radio3.isChecked():

            SaveName, Filter = QtGui.QFileDialog.getSaveFileName(None, "Save An Airfoil File", filePath, "*.dat")
            if SaveName != "":
                ####new2
                pathFile      = os.path.dirname(SaveName) + "/"  #1# = C:/Provisoire400/
                racineDrive   = os.path.splitdrive(SaveName)[0]  #2# = C:
                formatFichier = os.path.splitext(SaveName)[1]    #3# = .png
                SaveName      = os.path.splitext(SaveName)[0]    #4# = /home/kubuntu/.FreeCAD/Macro/Texture_007_H #= C:/Provisoire400/image3D
                nameFile      = os.path.basename(SaveName)       #5# = image3D
                SaveNameformatFichier = SaveName + formatFichier #6# = C:/Provisoire400/image3D.png
                pathFileSaveNameformatFichier = pathFile + nameFile + formatFichier #7# = C:/Provisoire400/image3D.png
                ####new2
                self.FreeCAD_ParamGetSet.SetString("filePath", pathFile)

                if "." in SaveNameformatFichier:
                    None
                else:
                    SaveNameformatFichier += ".dat"    # Mint

                try:
                    selected = FreeCADGui.Selection.getSelection()[0]
                    pointsDirection = []
                    pointsDirection = selected.Shape.discretize(Number=self.numberCut)  # discretize pour calculer la direction (avec un deuxieme point)

                    f = open(SaveNameformatFichier, 'w')     # path to write
                    f.write("NACA" + nameFile + "\n")        # title 

                    for coor in pointsDirection:
                        f.write(" " + str(round(coor.x, 5)) + "  " + str(round(coor.y, 5)) + "\n")

                    f.close()     # close the file
                except Exception:
                    app.Console.PrintError("Error, to Save .dat file\n")
            self.close()  # close the window

    def close(self):
        self.dialog.hide()

AirfoilImporterAndScaler()

</nowiki>
}}


<div class="toccolours mw-collapsible mw-collapsed">



## Anciennes versions 


<div class="mw-collapsible-content">



### Utilisation - Version 1.5 



#### Sélectionner le fichier 

L\'exécution de la macro présente d\'abord à l\'utilisateur un navigateur de fichiers qui lui permet de sélectionner le fichier .dat du profil aérodynamique souhaité. Naviguez jusqu\'à l\'endroit où vous avez enregistré le fichier de profils aérodynamiques, sélectionnez-le et appuyez sur Ouvrir.

![Fenêtre du navigateur de fichiers pour l\'importation de fichiers de profils aérodynamiques .dat](images/File_browser.png )



#### Entrer la longueur de la corde 

Une fois le fichier de profil sélectionné, une nouvelle boîte de dialogue apparaît et vous demande une longueur de corde. Vous pouvez saisir n\'importe quelle longueur, en millimètres. Une fois la longueur souhaitée saisie, la macro produira une Draft polyligne (DWire) suivant les points décrits dans le fichier de profil .dat précédemment sélectionné à l\'échelle que vous avez saisie pour la longueur de corde.

![Fenêtre de dialogue des longueurs des cordes pour l\'importation et mise à l\'échelle, macro v1.5](images/Chord_length.png )

L\'aile, optimisée, devrait maintenant être prête à être utilisé dans votre projet.



### Utilisation - Version 2 

Sélectionner le fichier de la même manière que la version 1.5. Avec la version 2, vous avez le choix de disposer soit de l\'aile qui en résulte fait avec une Draft polyligne (DWire) ou une spline de base (BSpline). Comme avec la version 1.5, vous entrez la longueur de la corde désirée. En outre, vous pouvez maintenant sélectionner quel type de papier souhaitée. Il suffit de cliquer sur la case d\'option BSpline ou laisser la valeur par défaut DWire.

![La boîte de dialogue de la version 2 Airfoil Import and scale avec le choix de DWire ou BSpline](images/V2_scale.png )



### Les macros 

#### Version 1.5 

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

#### Version 2 


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

#### Version 2.1 

Mis à jour par mangtronix pour utiliser PySide au lieu de PyQt (utilisé dans les anciennes versions de FreeCAD).


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

#### Version 2.1.2 

Icône de la barre d\'outils ![](images/Macro_Airfoil_Import_&_Scale.png )

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
__Web__ = "https://forum.freecad.org/viewtopic.php?f=22&t=5554"
__Wiki__ = "https://www.freecad.org/wiki/Macro_Airfoil_Import_%26_Scale"
__Icon__ = 'https://www.freecad.org/wiki/images/0/0c/Macro_Airfoil_Import_%26_Scale.png'
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


</div>


</div>



## Liens

Discussion sur le [Forum](https://forum.freecad.org/viewtopic.php?f=22&t=5554&p=45137&hilit=Airfoil#p45137)

[UIUC Applied Aerodynamics Group Departement of Aerospace Engineering](http://aerospace.illinois.edu/m-selig/ads/coord_database.html#N)



---
⏵ [documentation index](../README.md) > Macro Airfoil Import & Scale/fr
