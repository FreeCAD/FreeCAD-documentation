---
 GuiCommand:
   Name: Std ViewIvStereoOff
   Name/it: Stereo off
   MenuLocation: Visualizza , Stereo , Stereo off
   Workbenches: Tutti
   SeeAlso: Std_ViewIvStereoRedGreen/it, Std_ViewIvStereoQuadBuff/it,  Std_ViewIvStereoInterleavedRows/it, Std_ViewIvStereoInterleavedColumns/it
---

# Std ViewIvStereoOff/it



## Descrizione

Il comando **Stereo off** disattiva la modalità stereo nella [Vista 3D](3D_view/it.md) attiva.



## Utilizzo

1.  Selezionare l\'opzione **Visualizza → Stereo → <img src="images/Std_ViewIvStereoOff.svg" width=16px> Stereo off** dal menu.



## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Per modificare la visualizzazione in stereo off utilizzare il metodo `setStereoType` dell\'oggetto ActiveView. Questo metodo non è disponibile se FreeCAD è in modalità console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setStereoType('None')
FreeCADGui.ActiveDocument.ActiveView.getStereoType()
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ViewIvStereoOff/it
