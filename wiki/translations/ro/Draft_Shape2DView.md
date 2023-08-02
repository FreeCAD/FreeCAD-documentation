---
- GuiCommand:
   Name: Draft Shape2DView
   Name/ro: Draft Shape2DView
   MenuLocation: Draft -> Shape 2D View
   Workbenches: Draft_Workbench/ro, Arch_Workbench/ro
---

# Draft Shape2DView/ro


</div>



## Descriere


<div class="mw-translate-fuzzy">

Acest instrument plasează în document un obiect 2D care este o vedere aplatizată a unui obiect selectat [Shape](Part_Workbench.md), proiectat în direcția curentă de vizualizare.


</div>

Draft Shape2DView projections can be displayed on a [TechDraw Workbench](TechDraw_Workbench.md) page using the [TechDraw DraftView](TechDraw_DraftView.md) command. Alternatively the [TechDraw Workbench](TechDraw_Workbench.md) offer its own projection commands. But these create projections that are only displayed on the drawing page and not in the [3D view](3D_view.md).

![](images/Draft_Shape2DView_example.jpg ) 
*Projection of solid shapes onto the XY plane*



## Cum se folosește 


<div class="mw-translate-fuzzy">

1.  Selectați obiectul din care doriți să extrageți o vizualizare 2D
2.  Rotiți vizualizarea (sau utilizați comenzile rapide de presetare a vizualizării), astfel încât să reflecte direcția în care doriți să proiectați obiectul. De exemplu, folosirea unei vederi de sus va proiecta obiectul pe planul XY, pe verticală de-a lungul axei Z ca în imaginea de mai sus.
3.  Apăsați butonul **<img src="images/Draft_Shape2DView.png" width=16px> [[Draft Shape2DView]]
**


</div>

## How to produce plans and sections with different linewidths 

<img alt="" src=images/Draft_shape2dview_example_plan.png  style="width:700px;">

Drawings with different linewidths for viewed and cut lines can easily be produced by using two shape2Dview objects from a same [Arch SectionPlane](Arch_SectionPlane.md). One of the shape2Dview objects has its projection mode set to **Solid**, which renders the viewed lines, and another set to **Cut lines** or **Cut faces** to render the cut lines. The two shape2Dviews are then placed at the same location, one on top of the other.



## Proprietăți

See also: [Property editor](Property_editor.md).

A Draft Shape2DView object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

-    {{PropertyData | Proiectare}}: direcția proiecției.

-    {{PropertyData | Mod de proiecție}}: Modul de proiecție: fețe solide, individuale sau tăieturi.

-    {{PropertyData | In Place}}: Dacă este adevărat, atunci când se utilizează Cutlines sau Cutfaces mode (doar [Arch SectionPlane](Arch_SectionPlane.md)), rezultatul va apărea la locația planului tăiat în loc de planul de masă {{Version | 0.17 }}

-    {{PropertyData | HiddenLines}}: Afișează linii ascunse sau nu

-    {{PropertyData | Tessellation}}: Tessellate Ellipses și BSplines în segmente de linie

-    {{PropertyData | Lungimea segmentului}}: mărimea segmentelor dacă Tessellation este activată

-    {{PropertyData | Numai vizibil}}: Dacă este adevărat, această vizualizare va fi recuperată numai dacă este vizibilă


</div>

### View


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: not used.

-    **Pattern Size|Float**: not used.

## Scripting


<div class="mw-translate-fuzzy">

## Scrip-Programare 


</div>


<div class="mw-translate-fuzzy">

InstrumentulDraft Shape2DView poate fi utilizat în [macros](macros.md) și de la consola Python folosind următoarele funcții:


</div>


```python
shape2dview = make_shape2dview(baseobj, projectionVector=None, facenumbers=[])
```


<div class="mw-translate-fuzzy">

-   Adăugă o formă 2D la document, care este o proiecție 2D a obiectului dat.
-   De asemenea, poate fi dat un vector specific de proiecție.
-   Returnează obiectul generat.
-   Puteți să furnizați, de asemenea, o listă cu numerele de față care trebuie luate în considerare.


</div>

Change the `ProjectionMode` property of the created object if required. It can be: `"Solid"`, `"Individual Faces"`, `"Cutlines"`, `"Cutfaces"` or `"Solid faces"`.

Exempluː


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

box = doc.addObject("Part::Box", "Box")
box.Length = 2300
box.Width = 500
box.Height = 1000

shape1 = Draft.make_shape2dview(box)

shape2 = Draft.make_shape2dview(box, App.Vector(1, -1, 1))

shape3 = Draft.make_shape2dview(box, App.Vector(-1, 1, 1), [0, 5])
shape3.ProjectionMode = "Individual Faces"

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Shape2DView/ro
