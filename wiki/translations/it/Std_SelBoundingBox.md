---
- GuiCommand:/it
   Name:Std_SelBoundingBox
   Name/it:Box contenitore
   MenuLocation:Visualizza → Box contenitore
   Workbenches:Tutti
   SeeAlso:[Stile di disegno](Std_DrawStyle/it.md)
---


</div>

## Descrizione

Il comando **Box di selezione** attiva o disattiva la modalità di evidenziazione del riquadro di selezione globale. Se questa modalità è attivata, gli oggetti selezionati vengono contrassegnati in una [Vista 3D](3D_view.md) con un riquadro di selezione evidenziato anche se **Selection Style** è impostato su \'Forma\'.

## Utilizzo

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Std_SelBoundingBox.svg" width=16px> [Std SelBoundingBox](Std_SelBoundingBox.md)** button.
    -   Select the **View → <img src="images/Std_SelBoundingBox.svg" width=16px> Bounding box** option from the menu.

## Preferenze

The related setting is stored: **Tools → Edit parameters... → BaseApp → Preferences → View → ShowSelectionBoundingBox**. It is a boolean value, the default is `False`.

## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

To change the ShowSelectionBoundingBox setting use the `SetBool` method of the appropriate ParameterGrp. The code sample does not work if FreeCAD is in console mode.


```python
import FreeCAD, FreeCADGui

grp = FreeCAD.ParamGet('User parameter:BaseApp/Preferences/View')
if grp.GetBool('ShowSelectionBoundingBox'):
  grp.SetBool('ShowSelectionBoundingBox',False)
else:
  grp.SetBool('ShowSelectionBoundingBox',True)

FreeCADGui.updateCommands()
```


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}  
