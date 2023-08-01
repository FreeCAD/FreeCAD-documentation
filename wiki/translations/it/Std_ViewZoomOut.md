---
- GuiCommand:/it
   Name:Std ViewZoomOut
   Name/it:Riduci
   MenuLocation:Visualizza → Zoom → Riduci
   Workbenches:Tutti
   Shortcut:**Ctrl**+**-**
   SeeAlso:[Ingrandisci](Std_ViewZoomIn/it.md), [Finestra di ingrandimento](Std_ViewBoxZoom/it.md)
---

# Std ViewZoomOut/it



## Descrizione

Il comando **Riduci** riduce la [Vista 3D](3D_view/it.md) attiva.



## Utilizzo

1.  Esistono diversi modi per invocare il comando:
    -   Selezionare l\'opzione **Visualizza → Zoom → <img src="images/Std_ViewZoomOut.svg" width=16px> Riduci** dal menu.
    -   Usare la scorciatoia da tastiera: **Ctrl**+**-**.



## Note

-   È anche possibile eseguire lo zoom con la rotellina del mouse.



## Preferenze

-   Il fattore di zoom può essere modificato nelle preferenze: **Modifica → Preferenze... → Visualizzazione → Navigazione → Fattore di zoom**. Questa impostazione influisce anche sullo zoom della rotella di scorrimento. Vedi [Editor delle preferenze](Preferences_Editor/it#Navigazione.md).



## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Per ridurre utilizzare il metodo `zoomOut` dell\'oggetto ActiveView. Questo metodo non è disponibile se FreeCAD è in modalità console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.zoomOut()
```





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std ViewZoomOut/it
