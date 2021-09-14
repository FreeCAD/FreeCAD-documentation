---
- GuiCommand:/it
   Name:Surface_Sections
   Name/it:Surface Sections
   MenuLocation:Surface → Sections
   Workbenches:[Surface](Surface_Workbench/it.md)
   Version:0.19
---

## Descrizione

Lo strumento <img alt="" src=images/Surface_Sections.svg  style="width:16px;"> [Surface Sections](Surface_Sections/it.md) viene utilizzato per creare una superficie dai bordi che rappresentano sezioni trasversali di una superficie.

<img alt="" src=images/Surface_Sections_edges_example.png  style="width:" height="250px;"> <img alt="" src=images/Surface_Sections_example.png  style="width:" height="250px;">


*A sinistra: i bordi di controllo (sezioni trasversali). A destra: la superficie prodotta da questi bordi.*

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Assicurarsii di avere almeno due bordi o curve nello spazio. Questi bordi possono essere creati con gli strumenti di <img alt="" src=images/Workbench_Draft.svg  style="width:16px;"> [Draft](Draft_Workbench/it.md) o di <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [Sketcher](Sketcher_Workbench/it.md).
2.  Premere il pulsante **<img src=images/Surface_Sections.svg style="width:16px"> [Surface sections](Surface_Sections/it.md)**.
3.  Premere **Add edge**.
4.  Usare il puntatore per selezionare i bordi desiderati nella [vista 3D](3D_view/it.md); verrà visualizzata un\'anteprima della forma finale dopo aver selezionato due bordi validi.
5.  Premere **OK** per completare l\'operazione.


</div>

## Opzioni

-    **Add edge**: press once to start picking edges in the <img src=images/Draft_BSpline.svg style="width:3D view](3D_view.md). Individual lines such as **[16px"> <img src=images/Sketcher_CreateBSpline.svg style="width:Draft BSplines](Draft_BSpline.md)** and **[16px"> <img src=images/PartDesign_Body.svg style="width:Sketcher BSplines](Sketcher_CreateBSpline.md)** can be chosen, as well as any edge from solid objects, like those of **[16px"> <img src=images/Part_Primitives.svg style="width:PartDesign Bodies](PartDesign_Body.md)** and **[16px"> [Part Primitives](Part_Primitives.md)**.

-    **Remove edge**: press once to start picking edges in the [3D view](3D_view.md); these must be edges that were previously picked with **Add edge**.

-    **Right mouse button**: open the context menu and select **Remove**, or press **Del** in the keyboard, to remove the currently selected edge in the list.

-    **Drag**: drag the currently selected element in the list in order to change the order in which it will be processed; the list is processed from top to bottom.

-   Press **Cancel** or **Esc** to abort the current operation.

## Proprietà

Una [Surface Sections](Surface_Sections/it.md) (classe `Surface::Sections`) è derivato dalla base [Part Feature](Part_Feature/it.md) (classe `Part::Feature`, attraverso la sottoclasse `Part::Spline`), quindi condivide tutte le proprietà di quest\'ultima.

Oltre alle proprietà descritte in [Part Feature](Part_Feature/it.md), Surface Sections ha le seguenti proprietà nell\'[editor delle proprietà](property_editor/it.md).

### Dati


{{TitleProperty|Sections}}


<div class="mw-translate-fuzzy">

-    **NSections|LinkSubList**: un elenco di bordi che verranno utilizzati per costruire la curva.


</div>

### Vista


{{TitleProperty|Base}}

-    **Control Points|Bool**: il valore predefinito è `FALSE`; se impostato su `TRUE`, mostrerà una sovrapposizione con i punti di controllo della superficie.

## Twisting of the surface 

The shape of the surface depends on the direction of the chosen edges; if edges are selected and the result is a surface that \"twists\" on itself, one of the edges may need its list of vertices in the reverse order. See the information in **<img src=images/Surface_GeomFillSurface.svg style="width:16px"> [GeomFillSurface](Surface_GeomFillSurface.md)** for a more complete explanation.

<img alt="" src=images/Surface_twisting_example_smooth.png  style="width:330px;"> <img alt="" src=images/Surface_twisting_example_twisted.png  style="width:330px;">

## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

The Surface Sections tool can be used in [macros](macros.md) and from the [Python](Python.md) console by adding the `Surface::Sections` object.

-   The edges to be used to define the surface must be assigned as a [LinkSubList](LinkSubList.md) to the `NSections` property of the object.
-   All objects with edges need to be computed before they can be used as input for the properties of the Sections object.


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

pl1 = App.Placement()
obj1 = Draft.make_circle(50, placement=pl1, face=False, startangle=0, endangle=180)

pl2 = App.Placement(App.Vector(0, 0, 25), App.Rotation())
obj2 = Draft.make_circle(30, placement=pl2, face=False, startangle=0, endangle=180)

points3 = [App.Vector(18, -10, 50),
           App.Vector(12, 10, 50),
           App.Vector(-12, 10, 50),
           App.Vector(-18, -10, 50)]
obj3 = Draft.make_bspline(points3)

points4 = [App.Vector(15, -20, 100),
           App.Vector(0, 6, 100),
           App.Vector(-15, -20, 100)]
obj4 = Draft.make_bspline(points4)
doc.recompute()

surf = doc.addObject("Surface::Sections", "Surface")
surf.NSections = [(obj1, "Edge1"),
                  (obj2, "Edge1"),
                  (obj3, "Edge1"),
                  (obj4, "Edge1")]
doc.recompute()
```





{{Surface Tools navi

}} 
