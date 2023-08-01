# Dialog creation setting colors
## Introduction

This is an example of [dialog creation](Dialog_creation.md) with [PySide](PySide.md).

In this example, the entire interface is defined in [Python](Python.md). Although this is possible for small interfaces, for larger interfaces the recommendation is to create **.ui** files through Qt Designer, and load these in the program.

## Use QColorDialog to get a color 

Complete code:  
```python
# -*- coding: utf-8 -*-
# https://deptinfo-ensip.univ-poitiers.fr/ENS/pyside-docs/PySide/QtGui/QColor.html
import PySide
from PySide import QtGui ,QtCore
from PySide.QtGui import *
from PySide.QtCore import *
path = FreeCAD.ConfigGet("UserAppData")

couleur = QtGui.QColorDialog.getColor()
if couleur.isValid():
    red   = int(str(couleur.name()[1:3]),16)    # decode hexadecimal to int()
    green = int(str(couleur.name()[3:5]),16)    # decode hexadecimal to int()
    blue  = int(str(couleur.name()[5:7]),16)    # decode hexadecimal to int()

    print(couleur)                              # 
    print("hexadecimal ",couleur.name())        # color format hexadecimal mode 16
    print("Red   color ",red)                   # color format decimal
    print("Green color ",green)                 # color format decimal
    print("Blue  color ",blue)                  # color format decimal

```

## Use QColorDialog to create a palette of colors (standard and custom) 

This example modify the Standard color and the Customize color with the Tango FreeCAD guide.

 
```python
# -*- coding: utf-8 -*-
# https://deptinfo-ensip.univ-poitiers.fr/ENS/pyside-docs/PySide/QtGui/QColor.html
import PySide
from PySide import QtGui ,QtCore
from PySide.QtGui import *
from PySide.QtCore import *

###############################################
##        Window colors organisation         ##
##        __________________________         ##
## StandardColor:                            ##
##                                           ##
##           Colonnes:                       ##
##           1:  2:  3:  4:  5:  6:  7:  8:  ##
##          _______________________________  ##
## Line 1:   0   6   12  18  24  30  36  42  ##
## Line 2:   1   7   13  19  25  31  37  43  ##
## Line 3:   2   8   14  20  26  32  38  44  ##
## Line 4:   3   9   15  21  27  33  39  45  ##
## Line 5:   4   10  16  22  28  34  40  46  ##
## Line 6:   5   11  17  23  29  35  41  47  ##
##                                           ##
## CustomColor:                              ##
##                                           ##
##           Colonnes:                       ##
##           1:  2:  3:  4:  5:  6:  7:  8:  ##
##          _______________________________  ##
## Line 1:   0   2   4   6   8   10  12  14  ##
## Line 2:   1   3   5   7   9   11  13  15  ##
##                                           ##
###############################################

color_Dialog   = QtGui.QColorDialog()
# FreeCAD-Tango
# Customize the colors in the standard box (in numeric mode)
#
#### Dialog line 1
color_Dialog.setStandardColor( 0, QtGui.QColor(252, 233,  79 , 0).rgba())    # Butte 1
color_Dialog.setStandardColor( 6, QtGui.QColor(237, 212,   0 , 0).rgba())    # Butte 2
color_Dialog.setStandardColor(12, QtGui.QColor(196, 160,   0 , 0).rgba())    # Butte 3
color_Dialog.setStandardColor(18, QtGui.QColor( 48,  43,   0 , 0).rgba())    # Butte 4

color_Dialog.setStandardColor(24, QtGui.QColor(138, 226,  52 , 0).rgba())    # Chameleo 1
color_Dialog.setStandardColor(30, QtGui.QColor(115, 210,  22 , 0).rgba())    # Chameleo 2
color_Dialog.setStandardColor(36, QtGui.QColor( 78, 154,   6 , 0).rgba())    # Chameleo 3
color_Dialog.setStandardColor(42, QtGui.QColor( 23,  42,   4 , 0).rgba())    # Chameleo 4
#### Dialog line 2
color_Dialog.setStandardColor( 1, QtGui.QColor(252, 175,  62 , 0).rgba())    # Orang 1
color_Dialog.setStandardColor( 7, QtGui.QColor(245, 121,   0 , 0).rgba())    # Orang 2
color_Dialog.setStandardColor(13, QtGui.QColor(206,  92,   0 , 0).rgba())    # Orang 3
color_Dialog.setStandardColor(19, QtGui.QColor( 50,  25,   0 , 0).rgba())    # Orang 4

color_Dialog.setStandardColor(25, QtGui.QColor(114, 159, 207 , 0).rgba())    # Sky Blu 1
color_Dialog.setStandardColor(31, QtGui.QColor( 52, 101, 164 , 0).rgba())    # Sky Blu 2
color_Dialog.setStandardColor(37, QtGui.QColor( 32,  74, 135 , 0).rgba())    # Sky Blu 3
color_Dialog.setStandardColor(43, QtGui.QColor( 11,  21,  33 , 0).rgba())    # Sky Blu 4
#### Dialog line 3
color_Dialog.setStandardColor( 2, QtGui.QColor(173, 127, 168 , 0).rgba())    # Plu 1
color_Dialog.setStandardColor( 8, QtGui.QColor(117,  80, 123 , 0).rgba())    # Plu 2
color_Dialog.setStandardColor(14, QtGui.QColor( 92,  53, 102 , 0).rgba())    # Plu 3
color_Dialog.setStandardColor(20, QtGui.QColor( 23,  16,  24 , 0).rgba())    # Plu 4

color_Dialog.setStandardColor(26, QtGui.QColor(233, 185, 110 , 0).rgba())    # Chocolat 1
color_Dialog.setStandardColor(32, QtGui.QColor(193, 125,  17 , 0).rgba())    # Chocolat 2
color_Dialog.setStandardColor(38, QtGui.QColor(143,  89,   2 , 0).rgba())    # Chocolat 3
color_Dialog.setStandardColor(44, QtGui.QColor( 39,  25,   3 , 0).rgba())    # Chocolat 4
#### Dialog line 4
color_Dialog.setStandardColor( 3, QtGui.QColor(239,  41,  41 , 0).rgba())    # Scarle Re 1
color_Dialog.setStandardColor( 9, QtGui.QColor(204,   0,   0 , 0).rgba())    # Scarle Re 2
color_Dialog.setStandardColor(15, QtGui.QColor(164,   0,   0 , 0).rgba())    # Scarle Re 3
color_Dialog.setStandardColor(21, QtGui.QColor( 40,   0,   0 , 0).rgba())    # Scarle Re 4

color_Dialog.setStandardColor(27, QtGui.QColor( 52, 224, 226 , 0).rgba())    # FreeTea 1
color_Dialog.setStandardColor(33, QtGui.QColor( 22, 208, 210 , 0).rgba())    # FreeTea 2
color_Dialog.setStandardColor(39, QtGui.QColor(  6, 152, 154 , 0).rgba())    # FreeTea 3
color_Dialog.setStandardColor(45, QtGui.QColor(  4,  42,  42 , 0).rgba())    # FreeTea 4
#### Dialog line 5
color_Dialog.setStandardColor( 4, QtGui.QColor(255, 255, 255 , 0).rgba())    # Snow White

color_Dialog.setStandardColor(10, QtGui.QColor(238, 238, 236 , 0).rgba())    # Aluminiu 1
color_Dialog.setStandardColor(16, QtGui.QColor(211, 215, 207 , 0).rgba())    # Aluminiu 2
color_Dialog.setStandardColor(22, QtGui.QColor(186, 189, 182 , 0).rgba())    # Aluminiu 3

color_Dialog.setStandardColor(28, QtGui.QColor(136, 138, 133 , 0).rgba())    # Aluminiu 4
color_Dialog.setStandardColor(34, QtGui.QColor( 85,  87,  83 , 0).rgba())    # Aluminiu 5
color_Dialog.setStandardColor(40, QtGui.QColor( 46,  52,  54 , 0).rgba())    # Aluminiu 6

color_Dialog.setStandardColor(46, QtGui.QColor(  0,   0,   0 , 0).rgba())    # Je Black
#### Dialog line 6
color_Dialog.setStandardColor( 5, QtGui.QColor(255, 255, 255 , 0).rgba())    # Snow White
color_Dialog.setStandardColor(11, QtGui.QColor(255,   0,   0 , 0).rgba())    # Aluminiu 1
color_Dialog.setStandardColor(17, QtGui.QColor(  0, 255,   0 , 0).rgba())    # Aluminiu 2
color_Dialog.setStandardColor(23, QtGui.QColor(  0,   0, 255 , 0).rgba())    # Aluminiu 3

color_Dialog.setStandardColor(29, QtGui.QColor(255, 255,   0 , 0).rgba())    # Aluminiu 4
color_Dialog.setStandardColor(35, QtGui.QColor(255,   0, 255 , 0).rgba())    # Aluminiu 5
color_Dialog.setStandardColor(41, QtGui.QColor(  0, 255, 255 , 0).rgba())    # Aluminiu 6
color_Dialog.setStandardColor(47, QtGui.QColor(  0,   0,   0 , 0).rgba())    # Je Black
color_Dialog.setStandardColor(47, QtGui.QColor(  0,   0,   0 , 0).rgba())    # Je Black

#### Customize the colors to Dialog CustomColor (in hexadecimal converted in numeric mode)
# Use the Yellow tones for tools that create objects.
# Dialog line 1
color_Dialog.setCustomColor(0, QtGui.QColor( int("fc",16),int("e9",16),int("4f",16) , 0).rgba()) # hexadecimal converted in int
color_Dialog.setCustomColor(2, QtGui.QColor( int("ed",16),int("d4",16),int("00",16) , 0).rgba()) # hexadecimal converted in int
color_Dialog.setCustomColor(4, QtGui.QColor( int("c4",16),int("a0",16),int("00",16) , 0).rgba()) # hexadecimal converted in int
color_Dialog.setCustomColor(6, QtGui.QColor( int("30",16),int("2b",16),int("00",16) , 0).rgba()) # hexadecimal converted in int

# Use the Blue tones for tools that modify objects
color_Dialog.setCustomColor(8, QtGui.QColor( int("72",16),int("9f",16),int("cf",16) , 0).rgba()) # hexadecimal converted in int
color_Dialog.setCustomColor(10,QtGui.QColor( int("34",16),int("65",16),int("a4",16) , 0).rgba()) # hexadecimal converted in int
color_Dialog.setCustomColor(12,QtGui.QColor( int("20",16),int("4a",16),int("87",16) , 0).rgba()) # hexadecimal converted in int
color_Dialog.setCustomColor(14,QtGui.QColor( int("0b",16),int("15",16),int("21",16) , 0).rgba()) # hexadecimal converted in int

# Use the Teal tones for view-related tools
# Dialog line 2
color_Dialog.setCustomColor(1, QtGui.QColor( int("34",16),int("e0",16),int("e2",16) , 0).rgba()) # hexadecimal converted in int
color_Dialog.setCustomColor(3, QtGui.QColor( int("16",16),int("d0",16),int("d2",16) , 0).rgba()) # hexadecimal converted in int
color_Dialog.setCustomColor(5, QtGui.QColor( int("06",16),int("98",16),int("9a",16) , 0).rgba()) # hexadecimal converted in int
color_Dialog.setCustomColor(7, QtGui.QColor( int("04",16),int("2a",16),int("2a",16) , 0).rgba()) # hexadecimal converted in int

# Use the Red tones for Constraint related tools
color_Dialog.setCustomColor(9, QtGui.QColor( int("ef",16),int("29",16),int("29",16) , 0).rgba()) # hexadecimal converted in int
color_Dialog.setCustomColor(11,QtGui.QColor( int("cc",16),int("00",16),int("00",16) , 0).rgba()) # hexadecimal converted in int
color_Dialog.setCustomColor(13,QtGui.QColor( int("a4",16),int("00",16),int("00",16) , 0).rgba()) # hexadecimal converted in int
color_Dialog.setCustomColor(15,QtGui.QColor( int("28",16),int("00",16),int("00",16) , 0).rgba()) # hexadecimal converted in int

Color = color_Dialog.getColor()                                   # Color.name() extract the color in Hexadecimal mode (#ad7fa8)

if Color.isValid():

    print("__.name()___________")
    print("hexadecimal         ", Color.name())                   # color format hexadecimal mode 16
    red   = int(str( Color.name()[1:3]),16 )                      # decode hexadecimal to int()
    green = int(str( Color.name()[3:5]),16 )                      # decode hexadecimal to int()
    blue  = int(str( Color.name()[5:7]),16 )                      # decode hexadecimal to int()

    print("Red   color decimal ", str( Color.name()[1:3]), red )  # color format hex to decimal
    print("Green color decimal ", str( Color.name()[3:5]), green )# color format hex to decimal
    print("Blue  color decimal ", str( Color.name()[5:7]), blue ) # color format hex to decimal

    print("__.red()____________")
    print("Red   color decimal ", Color.red() )                   # extract the color RGBa with Qt (0 to 255)
    print("Green color decimal ", Color.green() )                 # extract the color RGBa with Qt (0 to 255)
    print("Blue  color decimal ", Color.blue() )                  # extract the color RGBa with Qt (0 to 255)
    print("Alpha       decimal ", Color.alpha() )                 # extract the color RGBa with Qt (0 to 255)

    print("__.redF()___________")
    print("Red   color float   ", Color.redF() )                  # extract the color RGBa with Qt (0.0 to 1.0) as FreeCAD
    print("Green color float   ", Color.greenF() )                # extract the color RGBa with Qt (0.0 to 1.0) as FreeCAD
    print("Blue  color float   ", Color.blueF() )                 # extract the color RGBa with Qt (0.0 to 1.0) as FreeCAD
    print("Alpha       float   ", Color.alphaF() )                # extract the color RGBa with Qt (0.0 to 1.0) as FreeCAD
    print("__enjoy_____________")

else:
    Color = ""
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Dialog creation setting colors
