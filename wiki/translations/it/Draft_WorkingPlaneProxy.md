---
 GuiCommand:
   Name: Draft SetWorkingPlaneProxy
   Name/it: Draft Piano di lavoro proxy
   MenuLocation: Utilità , Crea piano di lavoro Proxy<br>Utilità , Crea piano di lavoro Proxy
   Workbenches: Draft_Workbench/it, BIM_Workbench/it
   SeeAlso: Draft SelectPlane/it
---

# Draft WorkingPlaneProxy/it



## Descrizione

Il comando <img alt="" src=images/Draft_WorkingPlaneProxy.svg  style="width:24px;"> **Draft Piano di lavoro proxy** crea un piano di lavoro proxy per salvare il [Draft Piano di lavoro](Draft_SelectPlane/it.md) corrente. È possibile utilizzare piano di lavoro proxy per ripristinare rapidamente un piano di lavoro. La posizione della telecamera e la visibilità degli oggetti nella [Vista 3D](3D_view/it.md) vengono salvate anche nel piano di lavoro proxy e possono, [facoltativamente](#Proprietà.md), essere ripristinate.

<img alt="" src=images/Draft_WPProxy_example.png  style="width:400px;"> 
*Tre Piani di lavoro proxy con diversi orientamenti e offset*



## Utilizzo

1.  Facoltativamente modificare il [piano di lavoro](Draft_SelectPlane/it.md).
2.  Facoltativamente modificare la [Vista 3D](3D_view/it.md).
3.  Facoltativamente, modificare lo stato di visibilità degli oggetti nel documento.
4.  Esistono diversi modi per richiamare il comando:
    -   [Draft](Draft_Workbench/it.md): Premere il pulsante **<img src="images/Draft_WorkingPlaneProxy.svg" width=16px> [Crea piano di lavoro proxy](Draft_WorkingPlaneProxy/it.md)**.
    -   Draft: Selezionare l\'opzione **Utilità → <img src="images/Draft_WorkingPlaneProxy.svg" width=16px> Crea piano di lavoro proxy** dal menu, o dalla [Vista ad albero](Tree_view/it.md) o dal menu contestuale della [Vista 3D](3D_view/it.md).
    -   [BIM](BIM_Workbench/it.md): Selezionare l\'opzione **Utilità → <img src="images/Draft_WorkingPlaneProxy.svg" width=16px> Crea piano di lavoro proxy** dal menu.
5.  Viene creato un Piano di lavoro proxy.
6.  Per allineare il [piano di lavoro](Draft_SelectPlane/it.md) con un Piano di lavoro proxy, fare doppio clic sul Piano di lavoro proxy nella [Vista ad albero](Tree_view/it.md) o utilizzarlo con il comando [Draft Seleziona piano](Draft_SelectPlane/it.md).



## Menù contestuale 

Per un Draft Piano di lavoro proxy queste opzioni aggiuntive sono disponibili nel menu contestuale [Vista ad albero](Tree_view/it.md):

-    **<img src="images/Draft_SelectPlane.svg" width=16px> Memorizza la posizione della telecamera**: aggiorna la proprietà **View Data** del Piano di lavoro proxy con le impostazioni correnti della [Vista 3D](3D_view/it.md) della telecamera.

-    **<img src="images/Draft_SelectPlane.svg" width=16px> Memorizza stato oggetti**: aggiorna la proprietà **Visibility Map** del Piano di lavoro proxy con lo stato di visibilità corrente degli oggetti nel documento.



## Note

-   I Piani di lavoro proxy possono essere [spostati](Draft_Move/it.md) e [ruotati](Draft_Rotate/it.md) come qualsiasi altro oggetto. Utilizzare <img alt="" src=images/Draft_Snap_Center.svg  style="width:16px;"> [Draft Aggancia Centro](Draft_Snap_Center/it.md) per eseguire l\'aggancio al punto **Placement**.



## Proprietà

Vedere anche: [Editor delle proprietà](Property_editor/it.md).

Un oggetto Draft WorkingPlaneProxy deriva da un oggetto [App FeaturePython](App_FeaturePython/it.md) ed eredita tutte le sue proprietà. Ha inoltre le seguenti proprietà aggiuntive:

### Data


{{TitleProperty|Base}}

-    **Placement|Placement**: specifica la posizione del Piano di lavoro proxy nella [Vista 3D](3D_view/it.md). Vedere [Posizionamento](Posizionamento/it.md).

-    **Shape|Shape|Hidden**: specifica la forma del Piano di lavoro proxy.

### View


{{TitleProperty|Base}}

-    **Line Color|Color**: specifica il colore di tutti gli elementi del Piano di lavoro proxy.

-    **Line Width|Float**: specifica lo spessore della linea degli assi e dei simboli freccia.

-    **Restore State|Bool**: specifica se **Visibility Map** viene ripristinato quando il [piano di lavoro](Draft_SelectPlane/it.md) è allineato con il Piano di lavoro proxy.

-    **Restore View|Bool**: specifica se **View Data** viene ripristinato quando il [piano di lavoro](Draft_SelectPlane/it.md) è allineato con il Piano di lavoro proxy

-    **Transparency|Percent**: specifica la trasparenza della faccia del Piano di lavoro proxy.

-    **View Data|FloatList**: specifica la posizione e le impostazioni della telecamera.

-    **Visibility Map|Map|Hidden**: specifica lo stato di visibilità degli oggetti.


{{TitleProperty|Draft}}

-    **Arrow Size|Length**: specifica la dimensione dei simboli freccia visualizzati sulla punta dei tre assi.

-    **Display Size|Length**: specifica la lunghezza e la larghezza del Piano di lavoro proxy.



## Script

Vedere anche: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

Per creare un Draft WorkingPlaneProxy utilizzare il metodo `make_workingplaneproxy` del modulo Draft.

Se [Draft](Draft_Workbench/it.md) è attivo, l\'oggetto dell\'applicazione FreeCAD ha una proprietà `DraftWorkingPlane` che memorizza il piano di lavoro corrente. L\'{{Incode|Placement}} del metodo {{Incode|getPlacement}} dell\'oggetto `DraftWorkingPlane` può essere utilizzato per creare un Piano di lavoro proxy allineato. L\'{{Incode|Placement}} di un Piano di lavoro proxy a sua volta può essere utilizzato per riallineare il piano di lavoro.


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



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft WorkingPlaneProxy/it
