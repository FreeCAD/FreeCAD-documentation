---
- GuiCommand:/it
   Name:Std StoreWorkingView
   Name/it:Memorizza vista di lavoro
   MenuLocation:Visualizza→ Viste standard → Memorizza vista di lavoro
   Workbenches:Tutte
   Shortcut:**Shift**+**End**
   Version:1.0
   SeeAlso:[Richiama vista di lavoro](Std_RecallWorkingView/it.md), [Viste bloccate](Std_FreezeViews/it.md)
---

# Std StoreWorkingView/it



## Descrizione

Il comando **Memorizza vista di lavoro** memorizza le impostazioni della telecamera della [Vista 3D](3D_view/it.md) attiva nella sua vista di lavoro temporanea. Questa vista può essere richiamata con il comando [Richiama vista di lavoro](Std_RecallWorkingView/it.md).

Ogni vista 3D ha la propria vista di lavoro. La memorizzazione di una nuova vista di lavoro sovrascriverà la vista di lavoro esistente della vista 3D attiva. Quando una vista 3D viene chiusa, la sua vista di lavoro viene persa.



## Utilizzo

1.  Assicurarsi che una [Vista 3D](3D_view/it.md) sia attiva.
2.  Esistono diversi modi per invocare il comando:
    -   Selezionare l\'opzione **Visualizza → Viste standard → Memorizza vista di lavoro** dal menu.
    -   Usare la scorciatoia da tastiera: **Shift**+**End**.



## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

Per memorizzare le impostazioni correnti della telecamera della vista 3D attiva in una vista di lavoro:


```python
import FreeCADGui

FreeCADGui.runCommand("Std_StoreWorkingView", 0)
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std StoreWorkingView/it
