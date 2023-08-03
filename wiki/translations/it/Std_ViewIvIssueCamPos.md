# Std ViewIvIssueCamPos/it
---
 GuiCommand:   Name: Std ViewIvIssueCamPos   Name/it: Pubblica la posizione della camera   MenuLocation: Visualizza , Stereo , Pubblica la posizione della camera   Workbenches: Tutti   Shortcut:    SeeAlso: Std_FreezeViews/it---



## Descrizione

Il comando **Pubblica la posizione della camera** stampa le impostazioni della fotocamera della [Vista 3D](3D_view/it.md) attiva nella [Finestra dei Report](Report_view/it.md) e nella [Console Python](Python_console/it.md).


```python   OrthographicCamera {   viewportMapping ADJUST_CAMERA   position 57.73505 -57.73502 57.735027   orientation 0.74290609 0.30772209 0.59447283  1.2171158   nearDistance 81.588844   farDistance 109.60551   aspectRatio 1   focalDistance 100   height 100  } 
```



*Esempio di output: impostazioni della fotocamera dopo la modifica in [vista isometrica](Std_ViewIsometric/it.md) in un nuovo documento*



## Utilizzo

1.  Selezionare l\'opzione **Visualizza → Stereo → <img src="images/Std_ViewIvIssueCamPos.svg" width=16px> Pubblica la posizione della camera** dal menu.



## Note

-   Le impostazioni della fotocamera possono essere utilizzate per aggiungere viste bloccate a un file \*.cam. Vedere [Viste bloccate](Std_FreezeViews/it.md).



## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Il metodo `getCamera` dell\'oggetto ActiveView restituisce le stesse impostazioni della fotocamera in una singola stringa. Questo metodo non è disponibile se FreeCAD è in modalità console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.getCamera()
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ViewIvIssueCamPos/it
