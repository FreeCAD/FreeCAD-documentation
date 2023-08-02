---
- GuiCommand:
   Name: Std ViewIvStereoInterleavedRows
   Name/it: Stereo a righe interlacciate
   MenuLocation: Visualizza -> Stereo -> Stereo a righe interlacciate
   Workbenches: Tutti
   SeeAlso: Std_ViewIvStereoRedGreen/it, Std_ViewIvStereoQuadBuff/it,  Std_ViewIvStereoInterleavedColumns/it, Std_ViewIvStereoOff/it
---

# Std ViewIvStereoInterleavedRows/it



## Descrizione

Il comando **Stereo a righe interlacciate** cambia la [Vista 3D](3D_view/it.md) attiva in modalità di visualizzazione stereo a righe interlacciate. Per utilizzare questa modalità stereo sono necessari una scheda grafica speciale, un display speciale e [occhiali con lenti polarizzate](https://en.wikipedia.org/wiki/Polarized_3D_system).



## Utilizzo

1.  Selezionare l\'opzione **Visualizza → Stereo → <img src="images/Std_ViewIvStereoInterleavedRows.svg" width=16px> Stereo a  righe interlacciate** dal menu.



## Preferenze

-   La distanza occhio-occhio può essere modificata nelle preferenze: **Modifica → Preferenze... → Visualizzazione → Vista 3D → Distanza tra gli occhi per le modalità stereo**. Vedere [Editor delle preferenze](Preferences_Editor/it#Vista_3D.md).



## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Per modificare la visualizzazione in stereo a righe interlacciate utilizzare il metodo `setStereoType` dell\'oggetto ActiveView. Questo metodo non è disponibile se FreeCAD è in modalità console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setStereoType('InterleavedRows')
FreeCADGui.ActiveDocument.ActiveView.getStereoType()
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ViewIvStereoInterleavedRows/it
