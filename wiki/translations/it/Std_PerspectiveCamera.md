# Std PerspectiveCamera/it
---
 GuiCommand:   Name: Std_PerspectiveCamera   Name/it: Vista in prospettiva   MenuLocation: Visualizza , Vista in prospettiva   Workbenches: Tutti   Shortcut: **V** **P**   SeeAlso: Std_OrthographicCamera/it---



## Descrizione

Il comando **Vista in prospettiva** commuta la [vista 3D](3D_view/it.md) attiva in modalità vista prospettica. In questa modalità, gli oggetti più lontani dalla fotocamera appaiono più piccoli di quelli più vicini.

![](images/Std_PerspectiveCamera_example.svg ) 
*Due cubi con le stesse dimensioni nella vista in prospettiva*



## Utilizzo

1.  Esistono diversi modi per invocare il comando:
    -   Selezionare l\'opzione **Visualizza → <img src="images/Std_PerspectiveCamera.svg" width=16px> Vista in prospettiva** dal menu.
    -   Selezionare l\'opzione **<img src="images/Std_PerspectiveCamera.svg" width=16px> Vista in prospettiva** dal menu Mini-cubo del [Cubo di navigazione](Navigation_Cube/it.md).
    -   Usare la scorciatoia da tastiera: **V** e poi **P**.



## Preferenze

-   Il tipo di camera può essere modificato nelle preferenze: **Modifica → Preferenze... → Visualizzazione → Vista 3D → Tipo di camera**. Il tipo selezionato verrà utilizzato per tutte le viste 3D di tutti i documenti aperti e anche per i nuovi documenti. Vedere in [Editor delle preferenze](Preferences_Editor/it#Vista_3D.md).



## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Per cambiare nella vista in prospettiva, utilizzare il metodo `setCameraType` dell\'oggetto ActiveView. Questo metodo non è disponibile se FreeCAD è in modalità console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setCameraType('Perspective')
FreeCADGui.ActiveDocument.ActiveView.getCameraType()
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std PerspectiveCamera/it
