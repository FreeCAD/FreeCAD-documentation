# Macro Guitar fretboard/it

 {{Macro/it
|Name=Macro Guitar fretboard
|Icon=Macro_Guitar_fretboard.png
|Translate=Tastiera per chitarra
|Description=Crea una tastiera per chitarra.
|Author=ryback08
|Version=0.3
|Date=2019-07-03
|FCVersion=Tutte
|Download=[https://www.freecadweb.org/wiki/images/b/be/Macro_Guitar_fretboard.png ToolBar Icon]
|SeeAlso=[Macro_Guitar_Nut](Macro_Guitar_Nut.md) <img src="images/Macro_Guitar_Nut.png" width=24px>
}}

## Descrizione

Guitar Fretboard Marker (Macro), lo script Python è incredibile per rendere la forma complessa \....

Questa macro crea una tastiera conica composta (o no) multiscala (o no) con slot per dado e tasto o slot per tasto zero per esportare nel software CAM

![](images/Fretboard_freecad2.png ) 

## Codice

The ToolBar Icon ![Macro\_Guitar\_fretboard](images/Macro_Guitar_fretboard.png )

**Macro Guitar fretboard.FCMacro**


{{MacroCode|code=
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created: Sat Jan 14 00:33:37 2012
#      by: PyQt4 UI code generator 4.9
#      
# WARNING! All changes made in this file will be lost!
#
#
###################################### FREECAD Macro - Draw fretboard guitar #############################################
# ressource :                                                                                                            #
# Freecad dialog creation : http://sourceforge.net/apps/mediawiki/free-cad/index.php?title=Dialog_creation               #
# Topological data scripting : http://sourceforge.net/apps/mediawiki/free-cad/index.php?title=Topological_data_scripting #
# Fret slot theory : http://www.jpbourgeois.org/guitar/frets.htm                                                         #
#                                                                                                                        #
# For personal use only and / or non-profit use                                                                          #
# (C)2012 By LEPINE Florent                                                                                              #
# (C)2020 By Jeff Siddall                                                                                                #
# V0.1  -  2012/03/18                                                                                                    #
# V0.2  -  2018/01/25 : PySide                                                                                           #
# V0.3  -  2019/07/03 : Adaptation for 0.18                                                                              #
# V0.4  -  2020/01/08 : Major refactor to add multiscale frets and zerofret (Jeff Siddall)                               #
# Special thanks to FreeCAD team                                                                                         #
#                                                                                                                        #
##########################################################################################################################
#                                                                                                                        #
#  ### English ###                                                                                                       #
#  This macro creates a conical compound (or not) multiscale (or not) fretboard with nut and fret slot to export to      #
#  CAM software                                                                                                          #
#                                                                                                                        #
#  ### Francais ###                                                                                                      #
#  Cette macro creer une touche a radius progressif (ou pas) avec les defonces du sillet et l'emplacement des frettes    #
#  afin d'etre exporter dans un module de parcourt d'outil CAM                                                           #
#                                                                                                                        #
##########################################################################################################################
#                                                                                                                        #
#  ### Extra Notes ###                                                                                                   #
#  All Y-axis measurements are relative to fretboard centerline                                                          #
#  Origin is middle of nut/zero fret                                                                                     #
#                                                                                                                        #
##########################################################################################################################



from PySide import QtCore, QtGui
import FreeCAD, Part, math
from FreeCAD import Base, Vector

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s



   ################################################################################################
   #########                                begin functions                                ########
   ################################################################################################

# Function to return the X-value for a given fret
def fretx(fret, scalelen, offset):
    xvalue = (scalelen * (1 - (0.5 ** (float(fret) / 12)))) + offset

    return(xvalue)


# Function to return the neck edge Y-value for a given X value
def edgey(xvalue, nutwidth, edgetan):
    yvalue = (xvalue * edgetan) + (nutwidth / 2)

    return(yvalue)


# Function to return the fret X-axis crossing value for a given fret
def fretxcross(fret, scalelen1, scalelen2, perpscalediff):
    offset = perpscalediff / 2
    fret1x = fretx(fret, scalelen1, offset)   
    fret2x = fretx(fret, scalelen2, -offset)
    xcross = (fret1x + fret2x) / 2

    return(xcross)


# Function to return the fret angle tangent for a given fret
def frettan(fret, scalelen1, scalelen2, perpscalediff, nutwidth, edgetan):
    offset = perpscalediff / 2
    fret1x = fretx(fret, scalelen1, offset)   
    fret2x = fretx(fret, scalelen2, -offset)
    tanval = (fret2x - fret1x) / (nutwidth + (edgetan * (fret2x + fret1x)))

    return(tanval)



   ################################################################################################
   ######### begin of dialog box definition / debut de la definition de la boite de dialogue ######
   ################################################################################################


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(600, 491)
        self.label_zerofret = QtGui.QLabel(Dialog)
        self.label_zerofret.setGeometry(QtCore.QRect(10, 10, 431, 24))
        self.label_zerofret.setToolTip(_fromUtf8("Use a zero fret instead of a nut when checked"))
        self.label_zerofret.setWhatsThis(_fromUtf8(""))
        self.label_zerofret.setObjectName(_fromUtf8("label_zerofret"))
        self.checkBox_zerofret = QtGui.QCheckBox(Dialog)
        self.checkBox_zerofret.setGeometry(QtCore.QRect(460, 10, 51, 24))
        self.checkBox_zerofret.setWhatsThis(_fromUtf8(""))
        self.checkBox_zerofret.setObjectName(_fromUtf8("checkBox_zerofret"))
        self.label_scalelen1 = QtGui.QLabel(Dialog)
        self.label_scalelen1.setGeometry(QtCore.QRect(10, 30, 431, 24))
        self.label_scalelen1.setToolTip(_fromUtf8(""))
        self.label_scalelen1.setWhatsThis(_fromUtf8(""))
        self.label_scalelen1.setObjectName(_fromUtf8("label_scalelen1"))
        self.lineEdit_scalelen1 = QtGui.QLineEdit(Dialog)
        self.lineEdit_scalelen1.setGeometry(QtCore.QRect(460, 30, 51, 24))
        self.lineEdit_scalelen1.setWhatsThis(_fromUtf8(""))
        self.lineEdit_scalelen1.setObjectName(_fromUtf8("lineEdit_scalelen1"))
        self.label_scalelen2 = QtGui.QLabel(Dialog)
        self.label_scalelen2.setGeometry(QtCore.QRect(10, 50, 431, 24))
        self.label_scalelen2.setToolTip(_fromUtf8(""))
        self.label_scalelen2.setWhatsThis(_fromUtf8(""))
        self.label_scalelen2.setObjectName(_fromUtf8("label_scalelen2"))
        self.lineEdit_scalelen2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_scalelen2.setGeometry(QtCore.QRect(460, 50, 51, 24))
        self.lineEdit_scalelen2.setWhatsThis(_fromUtf8(""))
        self.lineEdit_scalelen2.setObjectName(_fromUtf8("lineEdit_scalelen2"))
        self.label_nutwidth = QtGui.QLabel(Dialog)
        self.label_nutwidth.setGeometry(QtCore.QRect(10, 130, 431, 24))
        self.label_nutwidth.setToolTip(_fromUtf8("Width of center of outside strings measured perpendicular to the neck where the middle of the nut/zero fret crosses the neck centerline."))
        self.label_nutwidth.setObjectName(_fromUtf8("label_nutwidth"))
        self.lineEdit_nutwidth = QtGui.QLineEdit(Dialog)
        self.lineEdit_nutwidth.setGeometry(QtCore.QRect(460, 130, 51, 24))
        self.lineEdit_nutwidth.setObjectName(_fromUtf8("lineEdit_nutwidth"))
        self.lineEdit_nutradius = QtGui.QLineEdit(Dialog)
        self.lineEdit_nutradius.setGeometry(QtCore.QRect(460, 190, 51, 24))
        self.lineEdit_nutradius.setObjectName(_fromUtf8("lineEdit_nutradius"))
        self.label_nutradius = QtGui.QLabel(Dialog)
        self.label_nutradius.setGeometry(QtCore.QRect(10, 190, 431, 24))
        self.label_nutradius.setToolTip(_fromUtf8("Measured where the middle of the nut/zero fret crosses the neck centerline.  To convert to mm from inches multiply by 25.4.  Ex: 7.5 in = 191 mm."))
        self.label_nutradius.setObjectName(_fromUtf8("label_nutradius"))
        self.lineEdit_perpfret = QtGui.QLineEdit(Dialog)
        self.lineEdit_perpfret.setGeometry(QtCore.QRect(460, 110, 51, 24))
        self.lineEdit_perpfret.setObjectName(_fromUtf8("lineEdit_perpfret"))
        self.label_perpfret = QtGui.QLabel(Dialog)
        self.label_perpfret.setGeometry(QtCore.QRect(10, 110, 431, 24))
        self.label_perpfret.setToolTip(_fromUtf8(""))
        self.label_perpfret.setObjectName(_fromUtf8("label_perpfret"))
        self.lineEdit_bridgewidth = QtGui.QLineEdit(Dialog)
        self.lineEdit_bridgewidth.setGeometry(QtCore.QRect(460, 150, 51, 24))
        self.lineEdit_bridgewidth.setObjectName(_fromUtf8("lineEdit_bridgewidth"))
        self.label_bridgewidth = QtGui.QLabel(Dialog)
        self.label_bridgewidth.setGeometry(QtCore.QRect(10, 150, 431, 24))
        self.label_bridgewidth.setToolTip(_fromUtf8("Width of center of outside strings measured perpendicular to the neck where the middle of the bridge crosses the neck centerline at the saddles."))
        self.label_bridgewidth.setObjectName(_fromUtf8("label_bridgewidth"))
        self.lineEdit_bridgeradius = QtGui.QLineEdit(Dialog)
        self.lineEdit_bridgeradius.setGeometry(QtCore.QRect(460, 210, 51, 24))
        self.lineEdit_bridgeradius.setObjectName(_fromUtf8("lineEdit_bridgeradius"))
        self.label_bridgeradius = QtGui.QLabel(Dialog)
        self.label_bridgeradius.setGeometry(QtCore.QRect(10, 210, 431, 24))
        self.label_bridgeradius.setToolTip(_fromUtf8("Measured at neck centerline at saddles. To convert to mm from inches multiply by 25.4.  Ex: 25 in = 635 mm."))
        self.label_bridgeradius.setObjectName(_fromUtf8("label_bridgeradius"))
        self.label_thicknessboard = QtGui.QLabel(Dialog)
        self.label_thicknessboard.setGeometry(QtCore.QRect(10, 90, 431, 24))
        self.label_thicknessboard.setToolTip(_fromUtf8(""))
        self.label_thicknessboard.setObjectName(_fromUtf8("label_thicknessboard"))
        self.lineEdit_thicknessboard = QtGui.QLineEdit(Dialog)
        self.lineEdit_thicknessboard.setGeometry(QtCore.QRect(460, 90, 51, 24))
        self.lineEdit_thicknessboard.setObjectName(_fromUtf8("lineEdit_thicknessboard"))
        self.label_nfret = QtGui.QLabel(Dialog)
        self.label_nfret.setGeometry(QtCore.QRect(10, 70, 431, 24))
        self.label_nfret.setToolTip(_fromUtf8(""))
        self.label_nfret.setObjectName(_fromUtf8("label_nfret"))
        self.lineEdit_nfret = QtGui.QLineEdit(Dialog)
        self.lineEdit_nfret.setGeometry(QtCore.QRect(460, 70, 51, 24))
        self.lineEdit_nfret.setObjectName(_fromUtf8("lineEdit_nfret"))
        self.label_fretslotdepth = QtGui.QLabel(Dialog)
        self.label_fretslotdepth.setGeometry(QtCore.QRect(10, 270, 431, 24))
        self.label_fretslotdepth.setToolTip(_fromUtf8(""))
        self.label_fretslotdepth.setObjectName(_fromUtf8("label_fretslotdepth"))
        self.lineEdit_fretslotdepth = QtGui.QLineEdit(Dialog)
        self.lineEdit_fretslotdepth.setGeometry(QtCore.QRect(460, 270, 51, 24))
        self.lineEdit_fretslotdepth.setObjectName(_fromUtf8("lineEdit_fretslotdepth"))
        self.lineEdit_fretslotwidth = QtGui.QLineEdit(Dialog)
        self.lineEdit_fretslotwidth.setGeometry(QtCore.QRect(460, 290, 51, 24))
        self.lineEdit_fretslotwidth.setObjectName(_fromUtf8("lineEdit_fretslotwidth"))
        self.label_fretslotwidth = QtGui.QLabel(Dialog)
        self.label_fretslotwidth.setGeometry(QtCore.QRect(10, 290, 431, 24))
        self.label_fretslotwidth.setToolTip(_fromUtf8(""))
        self.label_fretslotwidth.setObjectName(_fromUtf8("label_fretslotwidth"))
        self.label_fretslotmargin = QtGui.QLabel(Dialog)
        self.label_fretslotmargin.setGeometry(QtCore.QRect(10, 310, 431, 24))
        self.label_fretslotmargin.setToolTip(_fromUtf8(""))
        self.label_fretslotmargin.setObjectName(_fromUtf8("label_fretslotmargin"))
        self.lineEdit_fretslotmargin = QtGui.QLineEdit(Dialog)
        self.lineEdit_fretslotmargin.setGeometry(QtCore.QRect(460, 310, 51, 24))
        self.lineEdit_fretslotmargin.setObjectName(_fromUtf8("lineEdit_fretslotmargin"))
        self.label_nutslotwidth = QtGui.QLabel(Dialog)
        self.label_nutslotwidth.setGeometry(QtCore.QRect(10, 350, 431, 24))
        self.label_nutslotwidth.setToolTip(_fromUtf8("Nut thickness.  Not used when zerofret is selected."))
        self.label_nutslotwidth.setObjectName(_fromUtf8("label_nutslotwidth"))
        self.lineEdit_nutslotwidth = QtGui.QLineEdit(Dialog)
        self.lineEdit_nutslotwidth.setGeometry(QtCore.QRect(460, 350, 51, 24))
        self.lineEdit_nutslotwidth.setObjectName(_fromUtf8("lineEdit_nutslotwidth"))
        self.label_nutslotdepth = QtGui.QLabel(Dialog)
        self.label_nutslotdepth.setGeometry(QtCore.QRect(10, 370, 431, 24))
        self.label_nutslotdepth.setToolTip(_fromUtf8("Bottom of nut slot is flat"))
        self.label_nutslotdepth.setObjectName(_fromUtf8("label_nutslotdepth"))
        self.lineEdit_nutslotdepth = QtGui.QLineEdit(Dialog)
        self.lineEdit_nutslotdepth.setGeometry(QtCore.QRect(460, 370, 51, 24))
        self.lineEdit_nutslotdepth.setObjectName(_fromUtf8("lineEdit_nutslotdepth"))
        self.lineEdit_lastfretlen = QtGui.QLineEdit(Dialog)
        self.lineEdit_lastfretlen.setGeometry(QtCore.QRect(460, 170, 51, 24))
        self.lineEdit_lastfretlen.setObjectName(_fromUtf8("lineEdit_lastfretlen"))
        self.label_lastfretlen = QtGui.QLabel(Dialog)
        self.label_lastfretlen.setGeometry(QtCore.QRect(10, 170, 431, 24))
        self.label_lastfretlen.setToolTip(_fromUtf8(""))
        self.label_lastfretlen.setObjectName(_fromUtf8("label_lastfretlen"))
        self.lineEdit_lengthbeforenut = QtGui.QLineEdit(Dialog)
        self.lineEdit_lengthbeforenut.setGeometry(QtCore.QRect(460, 390, 51, 24))
        self.lineEdit_lengthbeforenut.setObjectName(_fromUtf8("lineEdit_lengthbeforenut"))
        self.label_lengthbeforenut = QtGui.QLabel(Dialog)
        self.label_lengthbeforenut.setGeometry(QtCore.QRect(10, 390, 431, 24))
        self.label_lengthbeforenut.setToolTip(_fromUtf8(""))
        self.label_lengthbeforenut.setObjectName(_fromUtf8("label_lengthbeforenut"))
        self.label_stringmargin1 = QtGui.QLabel(Dialog)
        self.label_stringmargin1.setGeometry(QtCore.QRect(10, 230, 431, 24))
        self.label_stringmargin1.setToolTip(_fromUtf8("Distance from edge of fretboard measured perpendicular to neck centerline for scale length 1"))
        self.label_stringmargin1.setObjectName(_fromUtf8("label_stringmargin1"))
        self.lineEdit_stringmargin1 = QtGui.QLineEdit(Dialog)
        self.lineEdit_stringmargin1.setGeometry(QtCore.QRect(460, 230, 51, 24))
        self.lineEdit_stringmargin1.setObjectName(_fromUtf8("lineEdit_stringmargin1"))
        self.label_stringmargin2 = QtGui.QLabel(Dialog)
        self.label_stringmargin2.setGeometry(QtCore.QRect(10, 250, 431, 24))
        self.label_stringmargin2.setToolTip(_fromUtf8("Distance from edge of fretboard measured perpendicular to neck centerline for scale length 2"))
        self.label_stringmargin2.setObjectName(_fromUtf8("label_stringmargin2"))
        self.lineEdit_stringmargin2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_stringmargin2.setGeometry(QtCore.QRect(460, 250, 51, 24))
        self.lineEdit_stringmargin2.setObjectName(_fromUtf8("lineEdit_stringmargin2"))
        self.OK = QtGui.QPushButton(Dialog)
        self.OK.setGeometry(QtCore.QRect(263, 450, 75, 32))
        self.OK.setObjectName(_fromUtf8("OK"))
        self.label_mm_01 = QtGui.QLabel(Dialog)
        self.label_mm_01.setGeometry(QtCore.QRect(520, 30, 30, 24))
        self.label_mm_01.setToolTip(_fromUtf8(""))
        self.label_mm_01.setWhatsThis(_fromUtf8(""))
        self.label_mm_01.setObjectName(_fromUtf8("label_mm_01"))
        self.label_mm_02 = QtGui.QLabel(Dialog)
        self.label_mm_02.setGeometry(QtCore.QRect(520, 90, 30, 24))
        self.label_mm_02.setToolTip(_fromUtf8(""))
        self.label_mm_02.setWhatsThis(_fromUtf8(""))
        self.label_mm_02.setObjectName(_fromUtf8("label_mm_02"))
        self.label_mm_03 = QtGui.QLabel(Dialog)
        self.label_mm_03.setGeometry(QtCore.QRect(520, 170, 30, 24))
        self.label_mm_03.setToolTip(_fromUtf8(""))
        self.label_mm_03.setWhatsThis(_fromUtf8(""))
        self.label_mm_03.setObjectName(_fromUtf8("label_mm_03"))
        self.label_mm_04 = QtGui.QLabel(Dialog)
        self.label_mm_04.setGeometry(QtCore.QRect(520, 130, 30, 24))
        self.label_mm_04.setToolTip(_fromUtf8(""))
        self.label_mm_04.setWhatsThis(_fromUtf8(""))
        self.label_mm_04.setObjectName(_fromUtf8("label_mm_04"))
        self.label_mm_05 = QtGui.QLabel(Dialog)
        self.label_mm_05.setGeometry(QtCore.QRect(520, 270, 30, 24))
        self.label_mm_05.setToolTip(_fromUtf8(""))
        self.label_mm_05.setWhatsThis(_fromUtf8(""))
        self.label_mm_05.setObjectName(_fromUtf8("label_mm_05"))
        self.label_mm_06 = QtGui.QLabel(Dialog)
        self.label_mm_06.setGeometry(QtCore.QRect(520, 290, 30, 24))
        self.label_mm_06.setToolTip(_fromUtf8(""))
        self.label_mm_06.setWhatsThis(_fromUtf8(""))
        self.label_mm_06.setObjectName(_fromUtf8("label_mm_06"))
        self.label_mm_07 = QtGui.QLabel(Dialog)
        self.label_mm_07.setGeometry(QtCore.QRect(520, 310, 30, 24))
        self.label_mm_07.setToolTip(_fromUtf8(""))
        self.label_mm_07.setWhatsThis(_fromUtf8(""))
        self.label_mm_07.setObjectName(_fromUtf8("label_mm_07"))
        self.label_mm_08 = QtGui.QLabel(Dialog)
        self.label_mm_08.setGeometry(QtCore.QRect(520, 350, 30, 24))
        self.label_mm_08.setToolTip(_fromUtf8(""))
        self.label_mm_08.setWhatsThis(_fromUtf8(""))
        self.label_mm_08.setObjectName(_fromUtf8("label_mm_08"))
        self.label_mm_09 = QtGui.QLabel(Dialog)
        self.label_mm_09.setGeometry(QtCore.QRect(520, 370, 30, 24))
        self.label_mm_09.setToolTip(_fromUtf8(""))
        self.label_mm_09.setWhatsThis(_fromUtf8(""))
        self.label_mm_09.setObjectName(_fromUtf8("label_mm_09"))
        self.label_mm_10 = QtGui.QLabel(Dialog)
        self.label_mm_10.setGeometry(QtCore.QRect(520, 390, 30, 24))
        self.label_mm_10.setToolTip(_fromUtf8(""))
        self.label_mm_10.setWhatsThis(_fromUtf8(""))
        self.label_mm_10.setObjectName(_fromUtf8("label_mm_10"))
        self.label_mm_11 = QtGui.QLabel(Dialog)
        self.label_mm_11.setGeometry(QtCore.QRect(520, 150, 30, 24))
        self.label_mm_11.setToolTip(_fromUtf8(""))
        self.label_mm_11.setWhatsThis(_fromUtf8(""))
        self.label_mm_11.setObjectName(_fromUtf8("label_mm_11"))
        self.label_mm_12 = QtGui.QLabel(Dialog)
        self.label_mm_12.setGeometry(QtCore.QRect(520, 50, 30, 24))
        self.label_mm_12.setToolTip(_fromUtf8(""))
        self.label_mm_12.setWhatsThis(_fromUtf8(""))
        self.label_mm_12.setObjectName(_fromUtf8("label_mm_12"))
        self.label_mm_13 = QtGui.QLabel(Dialog)
        self.label_mm_13.setGeometry(QtCore.QRect(520, 230, 30, 24))
        self.label_mm_13.setToolTip(_fromUtf8(""))
        self.label_mm_13.setWhatsThis(_fromUtf8(""))
        self.label_mm_13.setObjectName(_fromUtf8("label_mm_13"))
        self.label_mm_14 = QtGui.QLabel(Dialog)
        self.label_mm_14.setGeometry(QtCore.QRect(520, 190, 80, 24))
        self.label_mm_14.setToolTip(_fromUtf8(""))
        self.label_mm_14.setWhatsThis(_fromUtf8(""))
        self.label_mm_14.setObjectName(_fromUtf8("label_mm_14"))
        self.label_mm_15 = QtGui.QLabel(Dialog)
        self.label_mm_15.setGeometry(QtCore.QRect(520, 210, 80, 24))
        self.label_mm_15.setToolTip(_fromUtf8(""))
        self.label_mm_15.setWhatsThis(_fromUtf8(""))
        self.label_mm_15.setObjectName(_fromUtf8("label_mm_15"))
        self.label_mm_16 = QtGui.QLabel(Dialog)
        self.label_mm_16.setGeometry(QtCore.QRect(520, 250, 80, 24))
        self.label_mm_16.setToolTip(_fromUtf8(""))
        self.label_mm_16.setWhatsThis(_fromUtf8(""))
        self.label_mm_16.setObjectName(_fromUtf8("label_mm_16"))

        self.dialog = Dialog  ### Add to close windows at end of macro



        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.OK,QtCore.SIGNAL("pressed()"),self.createFretboard)    ###### See Freecad doc - connect pushbuton #####
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.checkBox_zerofret, self.lineEdit_scalelen1)
        Dialog.setTabOrder(self.lineEdit_scalelen1, self.lineEdit_scalelen2)
        Dialog.setTabOrder(self.lineEdit_scalelen2, self.lineEdit_nfret)
        Dialog.setTabOrder(self.lineEdit_nfret, self.lineEdit_thicknessboard)
        Dialog.setTabOrder(self.lineEdit_thicknessboard, self.lineEdit_perpfret)
        Dialog.setTabOrder(self.lineEdit_perpfret, self.lineEdit_nutwidth)
        Dialog.setTabOrder(self.lineEdit_nutwidth, self.lineEdit_bridgewidth)
        Dialog.setTabOrder(self.lineEdit_bridgewidth, self.lineEdit_lastfretlen)
        Dialog.setTabOrder(self.lineEdit_lastfretlen, self.lineEdit_nutradius)
        Dialog.setTabOrder(self.lineEdit_nutradius, self.lineEdit_bridgeradius)
        Dialog.setTabOrder(self.lineEdit_bridgeradius, self.lineEdit_stringmargin1)
        Dialog.setTabOrder(self.lineEdit_stringmargin1, self.lineEdit_stringmargin2)
        Dialog.setTabOrder(self.lineEdit_stringmargin2, self.lineEdit_fretslotdepth)
        Dialog.setTabOrder(self.lineEdit_fretslotdepth, self.lineEdit_fretslotwidth)
        Dialog.setTabOrder(self.lineEdit_fretslotwidth, self.lineEdit_fretslotmargin)
        Dialog.setTabOrder(self.lineEdit_fretslotmargin, self.lineEdit_nutslotwidth)
        Dialog.setTabOrder(self.lineEdit_nutslotwidth, self.lineEdit_nutslotdepth)
        Dialog.setTabOrder(self.lineEdit_nutslotdepth, self.lineEdit_lengthbeforenut)
        Dialog.setTabOrder(self.lineEdit_lengthbeforenut, self.OK)




    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_fromUtf8("Multiscale Compound Fretboard Maker"))
        self.label_zerofret.setText(_fromUtf8("Use zero fret - Utilisez z" + chr(233) + "ro frette"))
        self.checkBox_zerofret.setChecked(True)
        self.label_scalelen1.setText(_fromUtf8("Scale Length 1 - Diapason 1"))
        self.lineEdit_scalelen1.setText(_fromUtf8("864"))
        self.label_scalelen2.setText(_fromUtf8("Scale Length 2 - Diapason 2"))
        self.lineEdit_scalelen2.setText(_fromUtf8("940"))
        self.label_nutwidth.setText(_fromUtf8("Nut outer string width"))
        self.lineEdit_nutwidth.setText(_fromUtf8("38"))
        self.label_nutradius.setText(_fromUtf8("Radius at nut - Rayon au sillet"))
        self.lineEdit_nutradius.setText(_fromUtf8("191"))
        self.label_perpfret.setText(_fromUtf8("Perpendicular fret - Frette perpendiculaire"))
        self.lineEdit_perpfret.setText(_fromUtf8("7"))
        self.label_bridgewidth.setText(_fromUtf8("Bridge outer string width"))
        self.lineEdit_bridgewidth.setText(_fromUtf8("72"))
        self.label_bridgeradius.setText(_fromUtf8("Radius at bridge - Rayon au pont"))
        self.lineEdit_bridgeradius.setText(_fromUtf8("635"))
        self.label_thicknessboard.setText(_fromUtf8("Board thickness - Epaisseur de touche"))
        self.lineEdit_thicknessboard.setText(_fromUtf8("6.4"))
        self.label_nfret.setText(_fromUtf8("No. frets - No. de frettes"))
        self.lineEdit_nfret.setText(_fromUtf8("20"))
        self.label_fretslotdepth.setText(_fromUtf8("Depth of fret slot - Pronfondeur rainure de frette"))
        self.lineEdit_fretslotdepth.setText(_fromUtf8("2.0"))
        self.label_fretslotwidth.setText(_fromUtf8("Width of fret slot - Largeur rainure de frette"))
        self.lineEdit_fretslotwidth.setText(_fromUtf8("0.6"))
        self.label_fretslotmargin.setText(_fromUtf8("Fret slot margin - Marge de fente de frette"))
        self.lineEdit_fretslotmargin.setText(_fromUtf8("3.0"))
        self.label_nutslotwidth.setText(_fromUtf8("Width of nut slot - largeur du sillet"))
        self.lineEdit_nutslotwidth.setText(_fromUtf8("3.1"))
        self.label_nutslotdepth.setText(_fromUtf8("Depth of nut slot - profondeur du sillet"))
        self.lineEdit_nutslotdepth.setText(_fromUtf8("3.0"))
        self.label_lastfretlen.setText(_fromUtf8("Length after last fret - D" + chr(233) + "port apr" + chr(232) + "s la derni" + chr(232) + "re frette"))
        self.lineEdit_lastfretlen.setText(_fromUtf8("10.0"))
        self.label_lengthbeforenut.setText(_fromUtf8("Length before zero fret/nut - D" + chr(233) + "port avant le sillet"))
        self.lineEdit_lengthbeforenut.setText(_fromUtf8("6.4"))
        self.label_stringmargin1.setText(_fromUtf8("String margin 1 - Marge de cha" + chr(238) + " ne 1"))
        self.lineEdit_stringmargin1.setText(_fromUtf8("4.1"))
        self.label_stringmargin2.setText(_fromUtf8("String margin 2 - Marge de cha" + chr(238) + " ne 2"))
        self.lineEdit_stringmargin2.setText(_fromUtf8("5.1"))
        self.OK.setText(_fromUtf8("Create"))
        self.label_mm_01.setText(_fromUtf8("mm"))
        self.label_mm_02.setText(_fromUtf8("mm"))
        self.label_mm_03.setText(_fromUtf8("mm"))
        self.label_mm_04.setText(_fromUtf8("mm"))
        self.label_mm_05.setText(_fromUtf8("mm"))
        self.label_mm_06.setText(_fromUtf8("mm"))
        self.label_mm_07.setText(_fromUtf8("mm"))
        self.label_mm_08.setText(_fromUtf8("mm"))
        self.label_mm_09.setText(_fromUtf8("mm"))
        self.label_mm_10.setText(_fromUtf8("mm"))
        self.label_mm_11.setText(_fromUtf8("mm"))
        self.label_mm_12.setText(_fromUtf8("mm"))
        self.label_mm_13.setText(_fromUtf8("mm"))
        self.label_mm_14.setText(_fromUtf8("mm"))
        self.label_mm_15.setText(_fromUtf8("mm"))
        self.label_mm_16.setText(_fromUtf8("mm"))


    ############################################################################################
    ######### end of dialog box definition / fin de la definition de la boite de dialogue ######
    ############################################################################################


    def createFretboard(self):
        try:
            #################################################################
            ####### first we check if valid numbers have been entered #######
            #################################################################
            scalelen1 = float(self.lineEdit_scalelen1.text())                           # diapason
            scalelen2 = float(self.lineEdit_scalelen2.text())                           # diapason
            nutradius = float(self.lineEdit_nutradius.text())                           # radius de la touche au sillet
            bridgewidth = float(self.lineEdit_bridgewidth.text())                       # largeur de la touche a la derniere frette
            bridgeradius = float(self.lineEdit_bridgeradius.text())                     # radius de la touche a la derniere frette
            thicknessboard = float(self.lineEdit_thicknessboard.text())                 # epaisseur de la touche
            nfret = int(self.lineEdit_nfret.text())                                     # nombre de frettes
            perpfret = float(self.lineEdit_perpfret.text())                             # perpendicular fret
            fretslotdepth = float(self.lineEdit_fretslotdepth.text())                   # profondeur du solt des frettes
            fretslotwidth = float(self.lineEdit_fretslotwidth.text())                   # epaisseur du slot des frettes
            fretmargin = float(self.lineEdit_fretslotmargin.text())                     # deport du slot des frettes par rapport au bord
            lastfretlen = float(self.lineEdit_lastfretlen.text())                       # espace entre la derniere frette et la fin de la touche
            lengthbeforenut = float(self.lineEdit_lengthbeforenut.text())               # espace restant avant le sillet
            stringmargin1 = float(self.lineEdit_stringmargin1.text())                   # string margin
            stringmargin2 = float(self.lineEdit_stringmargin2.text())                   # string margin
            nutwidth = float(self.lineEdit_nutwidth.text())                             # largeur de la touche au sillet
            nutslotwidth = float(self.lineEdit_nutslotwidth.text())                     # longueur du sille
            nutslotdepth = float(self.lineEdit_nutslotdepth.text())                     # profondeur du sillet


        except ValueError:
            print( "Error! values must be valid numbers!")
            return None


        else:
            if self.checkBox_zerofret.checkState() == 0:
                zerofret = 0
                nutslotwidth = float(nutslotwidth)
            else:
                zerofret = 1
                nutslotwidth = 0.0

            ##### convert all value in float #####
            scalelen1 = float(scalelen1)
            scalelen2 = float(scalelen2)
            nutwidth = float(nutwidth)
            nutradius = float(nutradius)
            bridgewidth = float(bridgewidth)
            bridgeradius = float(bridgeradius)
            thicknessboard = float(thicknessboard)
            nfret = float(nfret)
            perpfret = float(perpfret)
            fretslotdepth = float(fretslotdepth)
            fretslotwidth = float(fretslotwidth)
            fretmargin = float(fretmargin)
            nutslotdepth = float(nutslotdepth)
            lastfretlen = float(lastfretlen)
            lengthbeforenut = float(lengthbeforenut)
            stringmargin1 = float(stringmargin1)
            stringmargin2 = float(stringmargin2)
            print( "OK, all values are good, let's go")


            #####################################################################
            ######     calculate first/last/perpendicular fret values      ######
            #####################################################################

            perplen1 = fretx(perpfret, scalelen1, 0)                                    # see formule to calculate fret length
            perplen2 = fretx(perpfret, scalelen2, 0)
            perpscalediff = perplen2 - perplen1
            halfperpscalediff = perpscalediff / 2
            fbwidthdiff = bridgewidth - nutwidth
            edgetan = fbwidthdiff / ((scalelen1 + scalelen2) / 2) / 2                   # half of fbwidthdiff is on each side of fretboard
            zerofrettan = frettan(0, scalelen1, scalelen2, perpscalediff, nutwidth, edgetan)
            endfrettan = frettan(nfret, scalelen1, scalelen2, perpscalediff, nutwidth, edgetan)


            ########################################################################
            print("1 - Create fretboard bottom")
            ########################################################################


            ########                   Fretboard Vector                       ######
            vnb1x = fretx(0, scalelen1, halfperpscalediff) - (zerofrettan * stringmargin1) # use fret angle and X value of the zero fret to find new X value with stringmargin
            vnb1y = edgey(vnb1x, nutwidth, edgetan) + stringmargin1                     # use new X value to find the Y value
            vnb1 = Vector(vnb1x, vnb1y, 0)

            vbb1x = fretx(nfret, scalelen1, halfperpscalediff) - (endfrettan * stringmargin1) + lastfretlen
            #vbb1x = fretx(nfret, scalelen1, halfperpscalediff)
            vbb1y = edgey(vbb1x, nutwidth, edgetan) + stringmargin1
            vbb1 = Vector(vbb1x, vbb1y, 0)

            vbb2x = fretx(nfret, scalelen2, -halfperpscalediff) + (endfrettan * stringmargin2) + lastfretlen
            #vbb2x = fretx(nfret, scalelen2, -halfperpscalediff) 
            vbb2y = -edgey(vbb2x, nutwidth, edgetan) - stringmargin2
            vbb2 = Vector(vbb2x, vbb2y, 0)

            vnb2x = fretx(0, scalelen2, -halfperpscalediff) + (zerofrettan * stringmargin2)
            vnb2y = -edgey(vnb2x, nutwidth, edgetan) - stringmargin2
            vnb2 = Vector(vnb2x, vnb2y, 0)


            ########                      Nut Vector                          ######
            adjnutslotwidth = nutslotwidth / math.cos(math.atan(zerofrettan))           # if nut slot is on an angle its X values need to be corrected
            nutx = -(lengthbeforenut + adjnutslotwidth)                                 # nut is a linear negative x shift
            vbnb1x = vnb1x + nutx                                                       # add to the end of the fretboard
            vbnb1y = edgey(vbnb1x, nutwidth, edgetan) + stringmargin1
            vbnb1 = Vector(vbnb1x, vbnb1y, 0)

            vbnb2x = vnb2x + nutx
            vbnb2y = -edgey(vbnb2x, nutwidth, edgetan) - stringmargin2
            vbnb2 = Vector(vbnb2x, vbnb2y, 0)

            ########                         Draw                             ######
            pointslist = [vbnb1,vnb1,vbb1,vbb2,vnb2,vbnb2,vbnb1]
            fretboardwire = Part.makePolygon(pointslist)
            #Part.show(fretboardwire)
            fretboardbottom = Part.Face(fretboardwire)
            #Part.show(fretboardbottom)
            fbextrude=fretboardbottom.extrude(Vector(0,0,thicknessboard*2))
            #Part.show(fbextrude)

            ########################################################################
            print("2 - Create fretboard top (radius)")
            ########################################################################

            ########################  radius at nut   ##############################
            # the fretboard top must extend beyond the nut to ensure there is no clipping
            # so calculate the values for the end of the fretboard relative to the nut
            radslope = (bridgeradius - nutradius) / ((scalelen1 + scalelen2) / 2)       # Find the slope of the compound radius
            minx = min(vbnb1x, vbnb2x)                                                  # position the end of the fretboard top at the minimum X value
            cn1rad = nutradius + (minx * radslope)                                      # Calculate the correct radius for the end of the fretboard
            cn1 = Part.makeCircle(cn1rad, Vector(minx, 0, -cn1rad + thicknessboard), Vector(1,0,0), 70, 110)
            #Part.show(cn1)

            ################## radius at bridge - rayon au pont #####################
            cn2 = Part.makeCircle(bridgeradius, Vector(((scalelen1 + scalelen2) / 2), 0, -bridgeradius + thicknessboard), Vector(1,0,0), 70, 110)
            #Part.show(cn2)

            ################## face of 2 radius - assemblage des 2 radius ###########
            compradius = Part.makeRuledSurface(cn1, cn2)
            #Part.show(compradius)
            ftextrude=compradius.extrude(Vector(0,0,-(thicknessboard * 2)))
            #Part.show(ftextrude)


            ########################################################################
            print("3 - Regroup fretboard bottom & top")
            ########################################################################
            cleanfretboard = ftextrude.common(fbextrude)
            #Part.show(cleanfretboard)

            if zerofret:
                ########################################################################
                print("4 - Skipping nut because zerofret was selected")
                print("5 - Skipping nut because zerofret was selected")
                ########################################################################

            else:
                ########################################################################
                print("4 - Make nut")
                ########################################################################
                ########                      Nut Vector                          ######
                vnt1x = -(bridgewidth * zerofrettan)                                    # nut crosses centerline at x=0, y=0 and nut slot needs to be wider than fretboard (i.e.: bridgewidth)
                vnt1 = Vector(vnt1x, bridgewidth, thicknessboard)
                vnt2 = Vector(-vnt1x, -bridgewidth, thicknessboard)
                vnt3x = -vnt1x - adjnutslotwidth
                vnt3 = Vector(vnt3x, -bridgewidth, thicknessboard)
                vnt4x = vnt1x - adjnutslotwidth
                vnt4 = Vector(vnt4x, bridgewidth, thicknessboard)

                ########                     Draw nut                             ######
                pointslist = [vnt1,vnt2,vnt3,vnt4,vnt1]
                nutwire = Part.makePolygon(pointslist)
                nutface = Part.Face(nutwire)
                nutextrude=nutface.extrude(Vector(0,0,-nutslotdepth))
                #Part.show(nutextrude)

                ########################################################################
                print("5 - Add nut")
                ########################################################################
                fretboardnut = cleanfretboard.cut(nutextrude)
                #Part.show(fretboardnut)
 

            ########################################################################
            print("6 - Add " + str(int(nfret)) + " frets")
            ########################################################################


            #####################################################################
            ##############   Radius on fretboard - depth fret slot   ############
            #####################################################################
            fretslotradius=compradius.extrude(Vector(0,0,-fretslotdepth))          # radius (top of fretboard) minus fret slot depth 


            #####################################################################
            ##############   outline fretboard - margin fret slot    ############
            #####################################################################
            vnb1fs = Vector(vbnb1x, (vbnb1y - fretmargin), 0)                           # use the fretboard dimensions as a starting point since the same slope will be used
            vbb1fs = Vector(vbb1x, (vbb1y - fretmargin), 0)
            vbb2fs = Vector(vbb2x, (vbb2y + fretmargin), 0)
            vnb2fs = Vector(vbnb2x, (vbnb2y + fretmargin), 0)
            pointslistfs = [vnb1fs,vbb1fs,vbb2fs,vnb2fs,vnb1fs]
            fretboardwirefs = Part.makePolygon(pointslistfs)
            #Part.show(fretboardwirefs)
            fretboardbottomfs = Part.Face(fretboardwirefs)
            #Part.show(fretboardbottomfs)
            fbextrudefs=fretboardbottomfs.extrude(Vector(0,0,thicknessboard*2))    # fretboardbottom with margin
            #Part.show(fbextrudefs)

            i=0
            incnfret = 0

            if (zerofret):
                incnfret = -1                                                           # use a zero fret if enabled


            while (incnfret < nfret):                                                   # draw all frets
                incnfret = incnfret + 1                 
                incxcross = fretxcross(incnfret, scalelen1, scalelen2, perpscalediff)
                incfrettan = frettan(incnfret, scalelen1, scalelen2, perpscalediff, nutwidth, edgetan)
                incfretangle = math.atan(incfrettan)

                print("      Fret " + str(incnfret) + ": " + str(round(incxcross,2)) + " mm at " + str(round(math.degrees(incfretangle),1)) + " degrees")

                adjfretslotwidth = fretslotwidth/math.cos(incfretangle) / 2             # adjust for fret slot being on an angle

                #####################################################################
                ##############             Fret slot ne X                ############
                #####################################################################         

                # make slots much larger than required (i.e.: twice the bridgewidth) initially, then cut later
                fretend1x = incxcross - (incfrettan * bridgewidth)
                fretend2x = incxcross + (incfrettan * bridgewidth)
                vnfs1 = Vector((fretend1x - adjfretslotwidth), bridgewidth, 0)
                vnfs2 = Vector((fretend1x + adjfretslotwidth), bridgewidth, 0)
                vnfs3 = Vector((fretend2x + adjfretslotwidth), -bridgewidth, 0)
                vnfs4 = Vector((fretend2x - adjfretslotwidth), -bridgewidth, 0)
                pointslistvnfs = [vnfs1,vnfs2,vnfs3,vnfs4,vnfs1]
                nslotwire = Part.makePolygon(pointslistvnfs)
                nslotextrude = Part.Face(nslotwire)
                 
                while (i < 1 ):
                    i = i + 1  
                    nslot = nslotextrude.extrude(Vector(0,0,thicknessboard*2))
                else:
                    nslot2 = nslotextrude.extrude(Vector(0,0,thicknessboard*2))
                    nslot = nslot.fuse(nslot2) 
                
            else:

                nslot3 = fbextrudefs.common(nslot)                                      # assembling all part (radius, bottom and fret)
                nslot4 = fretslotradius.common(nslot3)

                if zerofret:
                    nslot5 = cleanfretboard.cut(nslot4)    
                else:
                    nslot5 = fretboardnut.cut(nslot4)    

                #Part.show(fretboardfinal)
                objet_fretboard = App.ActiveDocument.addObject("Part::Feature","Fretboard")
                objet_fretboard.Shape = nslot5

                print("End of fretboard")

                  
            ########################################################################
            print("6 - Add Scale Length")
            ########################################################################
            Plane_scale_length = Part.makePlane(thicknessboard * 2 , (bridgewidth + (stringmargin1 + stringmargin2)), Vector(((scalelen1 + scalelen2) / 2), ((bridgewidth / 2) + ((stringmargin1 + stringmargin2) /2)),0), Vector(1,0,0)) #makePlane(length,width,[start_pnt,dir_normal])
            #Part.show (Plane_scale_length)
            objet_diapason = App.ActiveDocument.addObject("Part::Feature","Scale/Diapason")
            objet_diapason.Shape = Plane_scale_length


            ###### close windows when macro is done #####
            self.dialog.hide()


class Fretboard():
    if App.ActiveDocument is None :                                                     # create new document called 'Fretboard' if no document is open
        doc = App.newDocument("Fretboard")
    dialog = QtGui.QWidget() 
    dialog.ui = Ui_Dialog()
    dialog.ui.setupUi(dialog)
    dialog.show()

}}

## Link

[Guitar fretboard macro / guitar body](https://forum.freecadweb.org/viewtopic.php?f=24&t=5827)

## Versioni

-   Version 0.1 : 2012-03-16
-   Version 0.2 : 2018-01-25 : convert to PySide
-   Version 0.4 : 2020-01-09 : major refactor to add multiscale frets and zero fret
