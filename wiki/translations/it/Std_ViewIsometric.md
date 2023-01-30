---
- GuiCommand:/it
   Name:Std_ViewIsometric
   Name/it:Vista isometrica
   MenuLocation:Visualizza → Viste standard → Assonometria → Isometrica
   Workbenches:Tutti
   Shortcut:**0**
   SeeAlso:[Vista ortografica](Std_OrthographicCamera/it.md), [Assonometria dimetrica](Std_ViewDimetric/it.md), [Assonometria trimetrica](Std_ViewTrimetric/it.md)
---

# Std ViewIsometric/it



## Descrizione

Il comando **Vista isometrica** orienta la camera della [vista 3D](3D_view/it.md) in proiezione [assonometria isometrica](https://en.wikipedia.org/wiki/Isometric_projection). Per una vista veramente isometrica la vista 3D deve essere in [modalità ortografica](Std_OrthographicCamera/it.md), ma il comando funziona anche se la vista è in [modalità prospettiva](Std_PerspectiveCamera.md).

![](images/Std_ViewIsometric_example.svg ) 
*Il [sistema di assi](Std_AxisCross.md) e un cubo in vista isometrica.*



## Utilizzo

1.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Std_ViewIsometric.svg" width=16px> Vista isometrica**.
    -   Selezionare l\'opzione **Viste → Viste standard → Assonometra → <img src="images/Std_ViewIsometric.svg" width=16px> Isometrica** dal menu.
    -   Selezionare l\'opzione **Viste standard → <img src="images/Std_ViewIsometric.svg" width=16px> Isometrica** dal menu contestuale della [vista 3D](3D_view/it.md).
    -   Usare la scorciatoia da tastiera: **0**.



## Note

-   È anche possibile passare alla vista isometrica tramite il menu Mini-cubo del [Cubo di navigazione](Navigation_Cube/it.md).



## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Per passare alla vista isometrica utilizzare il metodo `viewIsometric` dell\'oggetto ActiveView. Questo metodo non è disponibile se FreeCAD è in modalità console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewIsometric()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewIsometric/it
