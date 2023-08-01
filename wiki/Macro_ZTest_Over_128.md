# Macro ZTest Over 128
**Not translate this page<br />This macro is only used by programmers<br />Test characters ASCII over 127<br />**


{{Macro
|Name=Macro ZTest Over 128
|Icon=Macro_ZTest_Over_128.png
|Description=This macro is only used by programmers.<br />Test characters ASCII over 127.
|Author=Mario52
|Version=3.0
|Date=2019-06-14
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/c/c1/Macro_ZTest_Over_128.png ToolBar Icon]
}}

## Description

This macro is only used by programmers Test characters ASCII over 127

## Usage

None

## Scripting

ToolBar Icon ![](images/Macro_ZTest_Over_128.png )

**Macro_ZTest_Over_128.FCMacro**


    # -*- coding: utf-8 -*-
    from __future__ import unicode_literals

    #this macro is only used by programmers
    #test caracteres au dessus de 127
    #this is not one macro Not download

    __title__   = "Macro_ZTest_Over_128"
    __author__  = "Programmer"
    __url__     = "https://www.freecadweb.org/wiki/Main_Page"
    __Wiki__    = "https://www.freecadweb.org/wiki/Macro_ZTest_Over_128"
    __version__ = "03.00"
    __date__    = "2019/06/14"


    try:
        print()
        print("chr()_____________________________1")
        print(chr(176))    #degree
        print(chr(178))    #exposant 2
        print(chr(179))    #exposant 3
        print(chr(181))    #micro
        print(chr(192))    #capital A accent grave
        print(chr(193))    #capital A accent aigu
        print(chr(194))    #capital A circonflex
        print(chr(196))    #capital A trema
        print(chr(197))    #capital A ring
    except Exception:
        FreeCAD.Console.PrintError("ERROR mode 1" + "\n")

    try:
        print()
        print("str(chr(176))_____________________2")
        print(str(chr(176)))    #degree
        print(str(chr(178)))    #exposant 2
        print(str(chr(179)))    #exposant 3
        print(str(chr(181)))    #micro
        print(str(chr(192)))    #capital A accent grave
        print(str(chr(193)))    #capital A accent aigu
        print(str(chr(194)))    #capital A circonflex
        print(str(chr(196)))    #capital A trema
        print(str(chr(197)))    #capital A ring
    except Exception:
        FreeCAD.Console.PrintError("ERROR mode 2" + "\n")

    try:
        print()
        print("b'\xc2\xb0'.decode('utf-8')_______3")
        print(b'\xc2\xb0'.decode('utf-8'))    #degree
        print(b'\xc2\xb2'.decode('utf-8'))    #exposant 2
        print(b'\xc2\xb3'.decode('utf-8'))    #exposant 3
        print(b'\xc2\xb5'.decode('utf-8'))    #micro
        print(b'\xc3\x80'.decode('utf-8'))    #capital A accent grave
        print(b'\xc3\x81'.decode('utf-8'))    #capital A accent aigu
        print(b'\xc3\x82'.decode('utf-8'))    #capital A circonflex
        print(b'\xc3\x83'.decode('utf-8'))    #capital A trema
        print(b'\xc3\x85'.decode('utf-8'))    #capital A ring
    except Exception:
        FreeCAD.Console.PrintError("ERROR mode 3" + "\n")

    try:
        print()
        print("b'\xb0'.decode('iso8859')_________4")
        print(b'\xb0'.decode('iso8859'))    #degree
        print(b'\xb2'.decode('iso8859'))    #exposant 2
        print(b'\xb3'.decode('iso8859'))    #exposant 3
        print(b'\xb5'.decode('iso8859'))    #micro
        print(b'\xc0'.decode('iso8859'))    #capital A accent grave
        print(b'\xc1'.decode('iso8859'))    #capital A accent aigu
        print(b'\xc2'.decode('iso8859'))    #capital A circonflex
        print(b'\xc3'.decode('iso8859'))    #capital A trema
        print(b'\xc5'.decode('iso8859'))    #capital A ring
    except Exception:
        FreeCAD.Console.PrintError("ERROR mode 4" + "\n")

    try:
        print()
        print("car_______________________________5")
        print("°")    #degree
        print("²")    #exposant 2
        print("³")    #exposant 3
        print("µ")    #micro
        print("À")    #capital A accent grave
        print("Á")    #capital A accent aigu
        print("Â")    #capital A circonflex
        print("Ã")    #capital A tilde
        print("Ä")    #capital A trema
        print("Å")    #capital A ringexcept Exception:
    except Exception:
        FreeCAD.Console.PrintError("ERROR mode 5" + "\n")

    try:
        print()
        print("u'car'.encode('utf-8')____________6")
        print(u"°".encode('utf-8'))    #degree
        print(u"²".encode('utf-8'))    #exposant 2
        print(u"³".encode('utf-8'))    #exposant 3
        print(u"µ".encode('utf-8'))    #micro
        print(u"À".encode('utf-8'))    #capital A accent grave
        print(u"Á".encode('utf-8'))    #capital A accent aigu
        print(u"Â".encode('utf-8'))    #capital A circonflex
        print(u"Ã".encode('utf-8'))    #capital A trema
        print(u"Å".encode('utf-8'))    #capital A ring
    except Exception:
        FreeCAD.Console.PrintError("ERROR mode 6" + "\n")

    print("End_______________________________")

    import sys
    import PySide
    from PySide import QtGui, QtCore
    class fen():
        label = QtGui.QLabel("FreeCAD")
        label.setGeometry(500, 300, 100, 100)
        label.setWindowFlags( QtCore.Qt.WindowStaysOnTopHint |  QtCore.Qt.CustomizeWindowHint | QtCore.Qt.FramelessWindowHint) 
        label.setAlignment(QtCore.Qt.AlignCenter)

    #    label.setWindowFlags( QtCore.Qt.CustomizeWindowHint) 
    #    label.setWindowFlags( QtCore.Qt.FramelessWindowHint) 
    #    label.setWindowFlags(PySide.QtCore.Qt.WindowStaysOnTopHint)

        label.show()

    print("End__Pipe_________________________")



---
⏵ [documentation index](../README.md) > Macro ZTest Over 128
