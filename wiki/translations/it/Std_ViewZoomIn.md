---
 GuiCommand:
   Name: Std ViewZoomIn
   Name/it: Ingrandisci
   MenuLocation: Visualizza , Zoom‏‎ , Ingrandisci
   Workbenches: Tutti
   Shortcut: **Ctrl**+**+**
   SeeAlso: Std ViewZoomOut/it, Std ViewBoxZoom/it
---

# Std ViewZoomIn/it



## Descrizione

Il comando **Ingrandisci** ingrandisce la [vista 3D](3D_view/it.md) attiva.



## Utilizzo

1.  Esistono diversi modi per invocare il comando:
    -   Selezionare l\'opzione **Visualizza → Zoom → <img src="images/Std_ViewZoomIn.svg" width=16px> Ingrandisci** dal menu.
    -   Usare la scorciatoia da tastiera: **Ctrl**+**+**.



## Note

-   È anche possibile eseguire lo zoom con la rotellina del mouse.



## Preferenze

-   Il fattore di zoom può essere modificato nelle preferenze: **Modifica → Preferenze... → Visualizzazione → Navigazione → Fattore di zoom**. Questa impostazione influisce anche sullo zoom della rotella di scorrimento. Vedi [Editor delle preferenze](Preferences_Editor/it#Navigazione.md).



## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Per ingrandire utilizzare il metodo `zoomIn` dell\'oggetto ActiveView. Questo metodo non è disponibile se FreeCAD è in modalità console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.zoomIn()
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ViewZoomIn/it
