---
- GuiCommand:/it
   Name:Std_OrthographicCamera
   Name/it:Vista ortografica
   MenuLocation:Visualizza → Vista ortografica
   Workbenches:Tutti
   Shortcut:**V** **O**
   SeeAlso:[Vista in prospettiva](Std_PerspectiveCamera/it.md)
---

# Std OrthographicCamera/it



## Descrizione

Il comando **Vista ortografica** commuta la [vista 3D](3D_view/it.md) attiva nella modalità di visualizzazione ortografica. In questa modalità, gli oggetti più lontani dalla fotocamera non appaiono più piccoli di quelli più vicini.

![](images/Std_OrthographicCamera_example.svg ) 
*Due cubi con le stesse dimensioni in vista ortografica*



## Utilizzo

1.  Esistono diversi modi per invocare il comando:
    -   Selezionare l\'opzione **Visualizza → <img src="images/Std_OrthographicCamera.svg" width=16px> Vista ortografica** dal menu.
    -   Selezionare l\'opzione **<img src="images/Std_OrthographicCamera.svg" width=16px> Vista ortografica** dal menu Mini-cubo del [Cubo di navigazione](Navigation_Cube/it.md).
    -   Usare la scorciatoia da tastiera: **V** e poi **O**.



## Preferenze

-   Il tipo di camera può essere modificato nelle preferenze: **Modifica → Preferenze... → Visualizzazione → Vista 3D → Tipo di camera**. Il tipo selezionato verrà utilizzato per tutte le viste 3D di tutti i documenti aperti e anche per i nuovi documenti. Vedere in [Editor delle preferenze](Preferences_Editor/it#Vista_3D.md).



## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Per cambiare la vista in ortografica, utilizzare il metodo `setCameraType` dell\'oggetto ActiveView. Questo metodo non è disponibile se FreeCAD è in modalità console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setCameraType('Orthographic')
FreeCADGui.ActiveDocument.ActiveView.getCameraType()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std OrthographicCamera/it
