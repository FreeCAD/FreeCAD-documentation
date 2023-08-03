---
 GuiCommand:
   Name: Std ViewIvStereoRedGreen
   Name/it: Stereo rosso/ciano
   MenuLocation: Visualizza , Stereo , Stereo rosso/ciano
   Workbenches: Tutti
   SeeAlso: Std_ViewIvStereoQuadBuff/it, Std_ViewIvStereoInterleavedRows/it, Std_ViewIvStereoInterleavedColumns/it, Std_ViewIvStereoOff/it
---

# Std ViewIvStereoRedGreen/it



## Descrizione

Il comando **Stereo rosso/ciano** cambia la [Vista 3D](3D_view/it.md) attiva in rosso/ciano, [anaglyph](https://en.wikipedia.org/wiki/Anaglyph_3D), modalità di visualizzazione stereo. Per utilizzare questa modalità stereo sono necessari occhiali con lenti colorate.



## Utilizzo

1.  Selezionare l\'opzione **Visualizza → Stereo → <img src="images/Std_ViewIvStereoRedGreen.svg" width=16px> Stereo rosso/ciano** dal menu.



## Preferenze

-   La distanza occhio-occhio può essere modificata nelle preferenze: **Modifica → Preferenze... → Visualizzazione → Vista 3D → Distanza tra gli occhi per le modalità stereo**. Vedi [Editor delle preferenze](Preferences_Editor/it#Vista_3D.md).



## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Per modificare la visualizzazione in stereo rosso/ciano utilizzare il metodo `setStereoType` dell\'oggetto ActiveView. Questo metodo non è disponibile se FreeCAD è in modalità console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setStereoType('Anaglyph')
FreeCADGui.ActiveDocument.ActiveView.getStereoType()
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ViewIvStereoRedGreen/it
