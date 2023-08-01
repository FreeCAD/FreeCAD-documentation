---
- GuiCommand:
   Name:Std RecallWorkingView
   Name/it:Richiama vista di lavoro
   MenuLocation:Visualizza → Viste standard → Richiama vista di lavoro
   Workbenches:Tutte
   Shortcut:**End**
   Version:0.21
   SeeAlso:[Memorizza vista di lavoro](Std_StoreWorkingView/it.md), [Viste bloccate](Std_FreezeViews/it.md)
---

# Std RecallWorkingView/it



## Descrizione

Il comando **Richiama vista di lavoro** richiama la vista di lavoro salvata della [Vista 3D](3D_view/it.md) attiva. Per ulteriori informazioni, vedere [Memorizza vista di lavoro](Std_StoreWorkingView/it.md).



## Utilizzo

1.  Assicurarsi che sia attiva una [Vista 3D](3D_view/it.md) per la quale il comando [Memorizza vista di lavoro](Std_StoreWorkingView/it.md) è stato usato almeno una volta.
2.  Esistono diversi modi per invocare il comando:
    -   Selezionare l\'opzione **Visualizza → Viste standard → Richiama vista di lavoro** dal menu.
    -   Usare la scorciatoia da tastiera: **End**.



## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

Per richiamare la vista di lavoro memorizzata della vista 3D attiva:


```python
import FreeCADGui

FreeCADGui.runCommand("Std_RecallWorkingView", 0)
```





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std RecallWorkingView/it
