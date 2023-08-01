---
- GuiCommand:
   Name:Std ViewIvStereoQuadBuff
   Name/it:Stereo quad buffer
   MenuLocation:Visualizza - Stereo - Stereo quad buffer
   Workbenches:Tutti
   SeeAlso:[Stereo rosso/ciano](Std_ViewIvStereoRedGreen/it.md), [Stereo a righe interlacciate](Std_ViewIvStereoInterleavedRows/it.md), [Stereo a colonne interlacciate](Std_ViewIvStereoInterleavedColumns/it.md), [Stereo Off](Std_ViewIvStereoOff/it.md)
---

# Std ViewIvStereoQuadBuff/it



## Descrizione

Il comando **Stereo quad buffer** cambia la [Vista 3D](3D_view/it.md) attiva in modalità di visualizzazione stereo quad buffer. Per utilizzare questa modalità stereo sono necessari una scheda grafica speciale, un display speciale e [occhiali con otturatore](https://en.wikipedia.org/wiki/Active_shutter_3D_system).



## Utilizzo

1.  Selezionare l\'opzione **Visualizza → Stereo → <img src="images/Std_ViewIvStereoQuadBuff.svg" width=16px> Stereo quad buffer** dal menu.



## Preferenze

-   La distanza occhio-occhio può essere modificata nelle preferenze: **Modifica → Preferenze... → Visualizzazione → Vista 3D → Distanza tra gli occhi per le modalità stereo**. Vedere [Editor delle preferenze](Preferences_Editor/it#Vista_3D.md).



## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Per modificare la visualizzazione in stereo quad buffer utilizzare il metodo `setStereoType` dell\'oggetto ActiveView. Questo metodo non è disponibile se FreeCAD è in modalità console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setStereoType('QuadBuffer')
FreeCADGui.ActiveDocument.ActiveView.getStereoType()
```





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std ViewIvStereoQuadBuff/it
