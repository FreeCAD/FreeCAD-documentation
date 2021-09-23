---
- GuiCommand:/it
   Name:Std AxisCross
   Name/it:Origine degli assi
   Empty:1
   MenuLocation:Visualizza → Origine degli assi
   Workbenches:Tutti
---

# Std AxisCross/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Il comando **Origine degli assi** attiva o disattiva il sistema di assi nella vista 3D attiva. L\'impostazione vale anche su tutte le nuove viste 3D, comprese quelle appartenenti a nuovi documenti, ma non sulla vista 3D iniziale di documenti esistenti.


</div>

Il sistema di assi è composto da tre frecce che rappresentano gli assi X, Y e Z positivi del sistema di coordinate globale. Il loro punto di partenza comune è l\'origine del sistema di coordinate globale.

![](images/Std_AxisCross_example.svg ) *Il sistema di assi (le lettere non fanno parte del sistema di assi)*

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare **Visualizza → Origine degli assi**.


</div>

## Note

-   FreeCAD può visualizzare un indicatore di sistema di coordinate più piccolo nell\'angolo in basso a destra delle viste 3D: **Modifica → Preferenze... → Display → Vista 3D → Mostra il sistema di coordinate nell'angolo**. Vedere [Editor delle preferenze](Preferences_Editor/it#Vista_3D.md).
-   Anche il [cubo di navigazione](Navigation_Cube/it.md) include un indicatore del sistema di coordinate.

## Preferenze


<div class="mw-translate-fuzzy">

-   L\'impostazione del sistema di assi è memorizzata in: **Strumenti → Modifica parametri... → BaseApp → Preferences → View → ShowAxisCross**.


</div>

## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Per attivare o disattivare il sistema di assi, utilizzare il metodo `setAxisCross` dell\'oggetto ActiveView. Questo metodo non è disponibile se FreeCAD è in modalità console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setAxisCross(True)
FreeCADGui.ActiveDocument.ActiveView.hasAxisCross()
```


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}

---
[documentation index](../README.md) > Std AxisCross/it
