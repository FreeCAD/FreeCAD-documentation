---
 GuiCommand:
   Name: Std AxisCross
   Name/it: Origine degli assi
   Empty: 1
   MenuLocation: Visualizza , Origine degli assi
   Workbenches: Tutti
   Shortcut: **A** **C**
---

# Std AxisCross/it



## Descrizione

Il comando **Origine degli assi** attiva o disattiva il sistema di assi nella [vista 3D](3D_view/it.md) attiva.

Il sistema di assi è composto da tre frecce che rappresentano gli assi X, Y e Z positivi del sistema di coordinate globale. Il loro punto di partenza comune è l\'origine del sistema di coordinate globale.

![](images/Std_AxisCross_example.svg ) 
*Il sistema di assi (le lettere non fanno parte del sistema di assi)*



## Utilizzo

1.  Esistono diversi modi per invocare il comando:
    -   Selezionare l\'opzione **Visualizza → <img src="images/Std_AxisCross.svg" width=16px> Origine degli assi** dal menu.
    -   Usare la scorciatoia da tastiera: **A** then **C**.



## Note

-   FreeCAD può visualizzare un indicatore di sistema di coordinate più piccolo nell\'angolo in basso a destra delle viste 3D: **Modifica → Preferenze... → Display → Vista 3D → Mostra il sistema di coordinate nell'angolo**. Vedere [Editor delle preferenze](Preferences_Editor/it#Vista_3D.md).
-   Anche il [cubo di navigazione](Navigation_Cube/it.md) include un indicatore del sistema di coordinate.



## Preferenze

-   L\'impostazione predefinita per l\'origine degli assi può essere modificata nelle preferenze: **Modifica → Preferenze... → Visualizza → Vista 3D → Mostra di default il sistema di assi**. Vedi [Editor delle preferenze](Preferences_Editor/it#Vista_3D.md).



## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Per attivare o disattivare il sistema di assi, utilizzare il metodo `setAxisCross` dell\'oggetto ActiveView. Questo metodo non è disponibile se FreeCAD è in modalità console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setAxisCross(True)
FreeCADGui.ActiveDocument.ActiveView.hasAxisCross()
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std AxisCross/it
