

## Introduzione

Questo è un esempio di [creazione di dialoghi](Dialog_creation/it.md) con [PySide](PySide/it.md).

In questo esempio, l\'intera interfaccia è definita in [Python](Python/it.md). Sebbene ciò sia possibile per interfacce di piccole dimensioni, per le interfacce più grandi si raccomanda di creare i file {{FileName|.ui}} tramite Qt Designer e caricarli nel programma. Vedere [Creazione di una interfaccia con dei file UI](Interface_creation_with_UI_files/it.md).

## Finestra di dialogo per scrivere in un file {#finestra_di_dialogo_per_scrivere_in_un_file}

Codice completo: 
```python
# -*- coding: utf-8 -*-
import PySide
from PySide import QtGui ,QtCore
from PySide.QtGui import *
from PySide.QtCore import *
path = FreeCAD.ConfigGet("UserAppData")

try:
    SaveName = QFileDialog.getSaveFileName(None,QString.fromLocal8Bit("Save a file txt"),path,             "*.txt") # PyQt4
#                                                                     "here the text displayed on windows" "here the filter (extension)"   
except Exception:
    SaveName, Filter = PySide.QtGui.QFileDialog.getSaveFileName(None, "Save a file txt", path,             "*.txt") # PySide
#                                                                     "here the text displayed on windows" "here the filter (extension)"   
if SaveName == "":                                                            # if the name file are not selected then Abord process
    App.Console.PrintMessage("Process aborted"+"\n")
else:                                                                         # if the name file are selected or created then 
    App.Console.PrintMessage("Registration of "+SaveName+"\n")                # text displayed to Report view (Menu > View > Report view checked)
    try:                                                                      # detect error ...
        file = open(SaveName, 'w')                                            # open the file selected to write (w)
        try:                                                                  # if error detected to write ...
            # here your code
            print("here your code")
            file.write(str(1)+"\n")                                           # write the number convert in text with (str())
            file.write("FreeCAD the best")                                    # write the the text with ("  ")
        except Exception:                                                     # if error detected to write
            App.Console.PrintError("Error write file "+"\n")                  # detect error ... display the text in red (PrintError)
        finally:                                                              # if error detected to write ... or not the file is closed
            file.close()                                                      # if error detected to write ... or not the file is closed
    except Exception:
        App.Console.PrintError("Error Open file "+SaveName+"\n")      # detect error ... display the text in red (PrintError)

```

## Finestra di dialogo per leggere un file {#finestra_di_dialogo_per_leggere_un_file}

Codice completo: 
```python
# -*- coding: utf-8 -*-
import PySide
from PySide import QtGui ,QtCore
from PySide.QtGui import *
from PySide.QtCore import *
path = FreeCAD.ConfigGet("UserAppData")

OpenName = ""
try:
    OpenName = QFileDialog.getOpenFileName(None,QString.fromLocal8Bit("Read a file txt"),path,             "*.txt") # PyQt4
#                                                                     "here the text displayed on windows" "here the filter (extension)"   
except Exception:
    OpenName, Filter = PySide.QtGui.QFileDialog.getOpenFileName(None, "Read a file txt", path,             "*.txt") #PySide
#                                                                     "here the text displayed on windows" "here the filter (extension)"   
if OpenName == "":                                                            # if the name file are not selected then Abord process
    App.Console.PrintMessage("Process aborted"+"\n")
else:
    App.Console.PrintMessage("Read "+OpenName+"\n")                           # text displayed to Report view (Menu > View > Report view checked)
    try:                                                                      # detect error to read file
        file = open(OpenName, "r")                                            # open the file selected to read (r)  # (rb is binary)
        try:                                                                  # detect error ...
            # here your code
            print("here your code")
            op = OpenName.split("/")                                          # decode the path
            op2 = op[-1].split(".")                                           # decode the file name 
            nomF = op2[0]                                                     # the file name are isolated

            App.Console.PrintMessage(str(nomF)+"\n")                          # the file name are displayed

            for ligne in file:                                                # read the file
                X  = ligne.rstrip('\n\r') #.split()                           # decode the line
                print(X)                                                      # print the line in report view other method 
                                                                              # (Menu > Edit > preferences... > Output window > Redirect internal Python output (and errors) to report view checked) 
        except Exception:                                                     # if error detected to read
            App.Console.PrintError("Error read file "+"\n")                   # detect error ... display the text in red (PrintError)
        finally:                                                              # if error detected to read ... or not error the file is closed
            file.close()                                                      # if error detected to read ... or not error the file is closed
    except Exception:                                                         # if one error detected to read file
        App.Console.PrintError("Error in Open the file "+OpenName+"\n")       # if one error detected ... display the text in red (PrintError)

```


{{Powerdocnavi

}} 

[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Python Code{{\#translation:}}](Category:Python_Code.md)
