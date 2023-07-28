---
- GuiCommand:/it
   Name:Std_SelBoundingBox
   Name/it:Box contenitore
   MenuLocation:Visualizza → Box contenitore
   Workbenches:Tutti
   Version:0.19
   SeeAlso:[Stile di disegno](Std_DrawStyle/it.md)
---

# Std SelBoundingBox/it



## Descrizione

Il comando **Box di selezione** attiva o disattiva la modalità di evidenziazione del riquadro di selezione globale. Se questa modalità è attivata, gli oggetti selezionati vengono contrassegnati in una [Vista 3D](3D_view.md) con un riquadro di selezione evidenziato anche se **Selection Style** è impostato su \'Forma\'.



## Utilizzo

1.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Std_SelBoundingBox.svg" width=16px> [Box contenitore](Std_SelBoundingBox/it.md)**.
    -   Selezionare l\'opzione **Visualizza → <img src="images/Std_SelBoundingBox.svg" width=16px> Box contenitore** dal menu.



## Preferenze

Viene memorizzata la relativa impostazione: **Strumenti → Modifica parametri... → BaseApp → Preferenze → View → ShowSelectionBoundingBox**. È un valore booleano, il valore predefinito è `False`.



## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Per modificare l\'impostazione ShowSelectionBoundingBox utilizzare il metodo `SetBool` del ParameterGrp appropriato. L\'esempio di codice non funziona se FreeCAD è in modalità console.


```python
import FreeCAD, FreeCADGui

grp = FreeCAD.ParamGet('User parameter:BaseApp/Preferences/View')
if grp.GetBool('ShowSelectionBoundingBox'):
  grp.SetBool('ShowSelectionBoundingBox',False)
else:
  grp.SetBool('ShowSelectionBoundingBox',True)

FreeCADGui.updateCommands()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std SelBoundingBox/it
