---
- GuiCommand:/it   Name:Std_OrthographicCamera   Name/it:Vista ortografica   MenuLocation:[Workbenches:Tutti   Shortcut:**V** **O**   SeeAlso:[[Std_PerspectiveCamera/it|Vista in prospettiva](Std_View_Menu/it___Visualizza]]_→_Vista_ortografica.md)---

## Descrizione

Il comando **Vista ortografica** commuta la [vista 3D](3D_view/it.md) attiva nella modalità di visualizzazione ortografica. In questa modalità, gli oggetti più lontani dalla fotocamera non appaiono più piccoli di quelli più vicini.

![](images/Std_OrthographicCamera_example.svg ) *Due cubi con le stesse dimensioni in vista ortografica*

## Utilizzo

1.  Esistono diversi modi per invocare il comando:
    -   Selezionare l\'opzione **Visualizza → <img src="images/Std_OrthographicCamera.svg" width=16px> Vista ortografica** dal menu.
    -   Usare la scorciatoia da tastiera: **V** e poi **O**.

## Note

-   È anche possibile passare alla modalità di visualizzazione ortografica tramite il menu Mini-cubo del [Cubo di navigazione](Navigation_Cube/it.md).

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


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}  
