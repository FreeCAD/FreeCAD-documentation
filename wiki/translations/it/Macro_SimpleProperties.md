 {{Macro/it
|Name=SimpleProperties
|Icon=Macro_SimpleProperties.png
|Description=Questa macro fornisce proprietà semplici dell'oggetto selezionato (volume, boundbox, ...)
|Author=OpenBrain
|Date=2019-06-10
|Version=0.7
|FCVersion= 0.17+
|Download=[https://www.freecadweb.org/wiki/images/d/da/Macro_SimpleProperties.png ToolBar Icon]
|SeeAlso=[Arch_Survey](Arch_Survey/it.md) <img src="images/Arch_Survey.svg" width=24px><br />[Macro_FCInfo](Macro_FCInfo/it.md) <img src="images/FCInfo.png" width=24px>
}}

## Descrizione

### Conteste

Questa macro è stata scritta principalmente in modo che l\'utente possa accedere a informazioni rapide e concise sulle proprietà fisiche di un oggetto. Ciò mira in particolare a preparare l\'imballaggio e la spedizione degli oggetti.

### Utilizzo

Seleziona un oggetto ed esegui la macro. Verrà visualizzato in una finestra di messaggio:

-   Volume dell\'oggetto in litri
-   Dimensioni del riquadro degli oggetti in millimetri
-   Se l\'oggetto è stato selezionato facendo clic su un bordo, la sua lunghezza viene visualizzata in millimetri
-   Se l\'oggetto è stato selezionato facendo clic su una faccia, la sua area viene visualizzata in quadratini

### Installazione


<div class="mw-translate-fuzzy">

Al momento, la macro non è disponibile dal gestore addon =\> PR inviata: <https://github.com/FreeCAD/FreeCAD-macros/pull/52> Quindi devi copiare il codice seguente e incollarlo nell\'editor di macro di FreeCAD.


</div>

Per spiegazioni più dettagliate, consultare la pagina [Come installare le macro](How_to_install_macros/it.md).

## Script

### Limitazione

-   Un solo oggetto alla volta

### Codice

ToolBar Icon ![](images/Macro_SimpleProperties.png )

**Macro\_SimpleProperties.FCMacro**


{{MacroCode|code=
#!/usr/bin/python
#####################################
# Copyright (c) openBrain 2019
# Licensed under LGPL v2
#
# This FreeCAD macro will give basic properties of the selected object (volume, boundbox, ...)
#
#
# Version history :
# *0.7 : some typo improvement + commenting
# *0.6 : check if selected object has a valid shape
# *0.5 : beta release
#
#####################################

__Name__ = 'SimpleProperties'
__Comment__ = 'Gives basic properties of object (volume, boundbox, ...)'
__Author__ = 'openBrain'
__Version__ = '0.7'
__Date__ = '2019-06-10'
__License__ = 'LGPL v2'
__Web__ = 'https://www.freecadweb.org/wiki/Macro_SimpleProperties'
__Wiki__ = 'https://www.freecadweb.org/wiki/Macro_SimpleProperties'
__Icon__ = ''
__Help__ = 'Select an object and run the macro'
__Status__ = 'Beta'
__Requires__ = 'FreeCAD >= 0.17'

__dbg__ = False #True for debugging
SIGNUM = '%.3g' #Set the display format of numbers

from PySide import QtGui

def cslM(msg): #Print message in console
    FreeCAD.Console.PrintMessage('\n')
    FreeCAD.Console.PrintMessage(msg)

def cslW(msg): #Print warning in console
    FreeCAD.Console.PrintMessage('\n')
    FreeCAD.Console.PrintWarning(msg)

def cslE(msg): #Print error in console
    FreeCAD.Console.PrintMessage('\n')
    FreeCAD.Console.PrintError(msg)

def cslD(msg): #Print debug message in console
    if __dbg__:
        FreeCAD.Console.PrintMessage('\n')
        FreeCAD.Console.PrintMessage("Debug : " + str(msg))

if __dbg__:  ##Clear report view in debug mode
    FreeCADGui.getMainWindow().findChild(QtGui.QTextEdit, "Report view").clear()

cslM("Starting Simple Properties macro")

if len(Gui.Selection.getSelection()) != 1: ##If not exactly one object selected, warn user & quit
    cslE("One and only one object shall be selected ... Exiting")
elif not ("Shape" in Gui.Selection.getSelection()[0].PropertiesList): ##If selected object has no shape, warn user & exit
    cslE("Selected object has no valid shape ... Exiting") 
else:
    obj = Gui.Selection.getSelection()[0] #Get selected object
    retStr = ""
    if len(Gui.Selection.getSelectionEx()[0].SubObjects) != 1: #If several object subobjects have been selected, ignore & warn user
        cslW("No or several subobject(s) selected, will be ignored")
    else:
        objEx = Gui.Selection.getSelectionEx()[0].SubObjects[0] #If one subobject selected
        if isinstance(objEx, Part.Edge): ##If it's an edge, print its length
            retStr += "Edge length : " + '%s' % float(SIGNUM % (objEx.Length)) + " mm\n"
        elif isinstance(objEx, Part.Face): ##If it's a face, print its area
            retStr += "Face area : " + '%s' % float(SIGNUM % (objEx.Area/1000000)) + " m2\n"
        else: ##If other (unsupported) type, warn user
            cslD("Subobject type : " + str(objEx.ShapeType))
            cslW("Unsupported type of subobject")
    retStr += "Object volume : " + '%s' % float(SIGNUM % (obj.Shape.Volume/1000000)) + " l\n" #Print object volume
    bb = obj.Shape.BoundBox #Get object boundbox
    retStr += "Object boundbox : " + '%s' % float(SIGNUM % (bb.XLength)) + " x " + '%s' % float(SIGNUM % (bb.YLength)) + " x " + '%s' % float(SIGNUM % (bb.ZLength)) + " mm" + "\n" #Print object boundbox dimensions
    QtGui.QMessageBox(QtGui.QMessageBox.Information, "Object Simple Props",retStr).exec_() #Display information in a message box
    cslM("End")

}}

