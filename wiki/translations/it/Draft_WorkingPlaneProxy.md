---
- GuiCommand:/it
   Name:Draft SetWorkingPlaneProxy
   Name/it:Piano proxy
   MenuLocation:Draft → Utilità → Crea piano di lavoro proxy
   Workbenches:[Draft](Draft_Workbench/it.md), [Arch](Arch_Workbench/it.md)
   SeeAlso:[Seleziona piano](Draft_SelectPlane/it.md)
---


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Questo comando posiziona un oggetto Piano proxy allineato al corrente [Piano di lavoro](Draft_SelectPlane/it.md).


</div>

<img alt="" src=images/Draft_WPProxy_example.png  style="width:400px;"> 
*Tre piani di lavoro proxy con diversi orientamenti e offset*

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Assicurarsi che il [Piano di lavoro](Draft_SelectPlane/it.md) sia impostato come si desidera.
2.  Poi andare nel menu {{MenuCommand|Draft → Utilità → <img src="images/Draft_SetWorkingPlaneProxy.png" width=16px> [Crea un piano di lavoro Proxy](Draft_SetWorkingPlaneProxy/it.md)}}.


</div>

## Context menu {#context_menu}

For a Draft WorkingPlaneProxy these additional options are available in the [Tree view](Tree_view.md) context menu:

-    {{MenuCommand|<img src="images/Draft_SelectPlane.svg" width=16px> Write camera position}}: updates the **View Data** property of the working plane proxy with the current [3D view](3D_view.md) camera settings.

-    {{MenuCommand|<img src="images/Draft_SelectPlane.svg" width=16px> Write objects state}}: updates the **Visibility Map** property of the working plane proxy with the current visibility state of objects in the document.

## Notes


<div class="mw-translate-fuzzy">

## Note

-   Il piano di lavoro memorizzato nell\'oggetto Proxy può essere ripristinato facendo doppio clic sull\'oggetto nella vista ad albero o selezionando l\'oggetto Proxy e utilizzando il pulsante **<img src="images/Draft_SelectPlane.svg" width=16px> [Seleziona piano](Draft_SelectPlane/it.md)**.
-   La posizione della telecamera è memorizzata nell\'oggetto Proxy al momento della creazione. Questa posizione può essere aggiornata in qualsiasi momento: zoom, panoramica e rotazione della vista come desiderato, quindi fare clic con il pulsante destro del mouse sull\'oggetto piano Proxy nella vista ad albero e selezionare **<img src="images/Draft_SelectPlane.svg" width=16px> Write camera position**.
-   Al momento della creazione nell\'oggetto Proxy viene anche memorizzato lo stato di visibilità di tutti gli oggetti. Questo stato può essere aggiornato in qualsiasi momento: impostare la proprietà **Visibility** degli oggetti su `True` o `False` come desiderato, quindi fare clic con il pulsante destro del mouse sull\'oggetto Proxy nella vista ad albero e selezionare **<img src="images/Draft_SelectPlane.svg" width=16px> Write objects state**.
-   I piani proxy possono essere spostati e ruotati come qualsiasi altro oggetto in modo che definire il piano di lavoro desiderato. Il loro aspetto visivo può essere cambiato nell\'[editor delle proprietà](property_editor/it.md).


</div>

## Proprietà

See also: [Property editor](Property_editor.md).

A Draft WorkingPlaneProxy object is derived from an [App FeaturePython](App_FeaturePython.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Base}}


<div class="mw-translate-fuzzy">

### Dati

-    **Placement**: specifica la posizione dell\'oggetto proxy e il piano di lavoro corrispondente.

    -   
        **Position**
        
        : specifica le coordinate dell\'oggetto proxy.

    -   
        **Angle**
        
        : specifica l\'angolo di rotazione dell\'oggetto proxy.

    -   
        **Axis**
        
        : specifica l\'asse da utilizzare per l\'angolo di rotazione.


</div>

### View


{{TitleProperty|Arch}}


<div class="mw-translate-fuzzy">

### Vista

-    **Display Size**: specifica sia la lunghezza che la larghezza dell\'oggetto proxy. Se l\'oggetto viene creato nella vista ad albero ma nella vista 3D non è visibile nessun elemento, aumentare questo valore fino a renderlo visibile.

-    **Arrow Size**: specifica la dimensione delle frecce che indicano i tre assi del piano proxy.

-    **Restore View**: se è `True` la posizione della telecamera viene ripristinata nella posizione salvata quando si utilizza il proxy con **<img src="images/Draft_SelectPlane.svg" width=16px> [Seleziona piano](Draft_SelectPlane/it.md)** o facendo doppio clic su di esso.

-    **Restore State**: se è `True` lo stato di visibilità di tutti gli oggetti viene ripristinato allo stato salvato quando si utilizza il proxy con **<img src="images/Draft_SelectPlane.svg" width=16px> [Seleziona piano](Draft_SelectPlane/it.md)** o facendo doppio clic su di esso.


</div>


{{TitleProperty|Base}}

-    **Line Color|Color**: specifies the color of all elements of the working plane proxy.

-    **Line Width|Float**: specifies the line width of the axes and arrow symbols.

-    **Restore State|Bool**: specifies if the **Visibility Map** is restored when the [working plane](Draft_SelectPlane.md) is aligned with the working plane proxy.

-    **Restore View|Bool**: specifies if the **View Data** is restored when the [working plane](Draft_SelectPlane.md) is aligned with the working plane proxy.

-    **Transparency|Percent**: specifies the transparency of the face of the working plane proxy.

-    **View Data|FloatList**: specifies the camera position and settings.

-    **Visibility Map|Map|Hidden**: specifies the visibility state of objects.

## Script


<div class="mw-translate-fuzzy">


**Vedere anche:**

[API Draft](Draft_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

L\'oggetto Piano di lavoro proxy può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione:


</div>


<div class="mw-translate-fuzzy">

-   Cre un oggetto `WPProxy` con il `placement` dato, che è un `FreeCAD.Placement`.
    -   Un posizionamento è definito da un punto base, dato dal suo `FreeCAD.Vector`, e una `FreeCAD.Rotation`.


</div>


```python
# This code only works if the Draft Workbench is active!

import FreeCAD as App
import FreeCADGui as Gui
import Draft

doc = App.newDocument()

workplane = App.DraftWorkingPlane
place = workplane.getPlacement()

proxy = Draft.make_workingplaneproxy(place)
proxy.ViewObject.DisplaySize = 3000
proxy.ViewObject.ArrowSize = 200

axis2 = App.Vector(1, 1, 1)
point2 = App.Vector(3000, 0, 0)
place2 = App.Placement(point2, App.Rotation(axis2, 90))

proxy2 = Draft.make_workingplaneproxy(place2)
proxy2.ViewObject.DisplaySize = 3000
proxy2.ViewObject.ArrowSize = 200

workplane.setFromPlacement(proxy2.Placement, rebase=True)
Gui.Snapper.setGrid()

doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>


 
