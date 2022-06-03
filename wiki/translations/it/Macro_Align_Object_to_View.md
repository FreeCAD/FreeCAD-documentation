# Macro Align Object to View/it
{{Macro/it
|Name=Macro Align Object to View
|Icon=Macro_Align_Object_to_View.png
|Translate=Alinea l'obietto su la vista
|Description=Questa macro allinea l'oggetto selezionato alla vista corrente.
|Author=Mario52
|Version=0.1
|Date=2015-01-16
|FCVersion=All
|Download=[https   *//www.freecadweb.org/wiki/images/f/f4/Macro_Align_Object_to_View.png ToolBar Icon]
|SeeAlso=[32px|FCCamera](File   *FCCamera_00.png.md) [Macro_FCCamera](Macro_FCCamera/it.md)
}}

## Descrizione

Questa macro posiziona e allinea l\'oggetto selezionato alla Vista corrente.


<div class="mw-translate-fuzzy">

## Uso

-   Orientare la visualizzazione, selezionare l\'oggetto ed eseguire la macro
-   L\'oggetto assume il posizionamento delle coordinate della camera


</div>

## Script

ToolBar Icon ![](images/Macro_Align_Object_to_View.png )

**Macro\_Align\_Object\_to\_View.FCMacro**


{{MacroCode|code=
# This macro place your object selected to the position ActiveView (camera)
# extact FCCamera
# 16/01/2015

__title__  ="Align Object to View"
__author__ = "Mario52"
__date__   = "16/01/2015"
__version__= "0.1"

import pivy
from pivy import coin

sel = FreeCADGui.Selection.getSelection()
Nameelement = sel[0].Name
App.Console.PrintMessage(str(Nameelement)+"\n")

pl = FreeCAD.Placement()
pl.Rotation = FreeCADGui.ActiveDocument.ActiveView.getCameraOrientation()
pl.Base = FreeCAD.Vector(0.0,0.0,0.0)

App.ActiveDocument.getObject(Nameelement).Placement=pl

}}

## Esempio


<center>

Image   *Macro Align Object to View 01.png\|L\'oggetto nella sua posizione XY originale. Image   *Macro Align Object to View 02.png\|Si può ruotare la vista con X? Y? Z? oppure usare la macro Rotate View per una rotazione di precisione.


</center>


<center>

Image   *Macro Align Object to View 03.png\|Selezionare l\'oggetto ed eseguire la macro (l\'oggetto con la faccia rivolta verso lo schermo). Image   *Macro Align Object to View 04.png\|L\'oggetto è visualizzato nel piano XY e nelle coordinate della sua nuova posizione (Placement e Angle)


</center>

## Crediti

Grazie a rentlau\_64 per il codice semplificato



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Align Object to View/it
