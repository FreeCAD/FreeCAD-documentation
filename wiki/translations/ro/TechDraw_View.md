---
- GuiCommand:/ro
   Name/ro:Noua vedere TechDraw
   MenuLocation:TechDraw → Insert View
   Workbenches:[TechDraw](TechDraw_Workbench.md)
   SeeAlso:[Insert Projection Group](TechDraw_ProjectionGroup.md), [Insert Section View](TechDraw_SectionView.md)
---


</div>

## Descriere

Instrumentul Vizualizare adaugă o reprezentare a unuia sau mai multor obiecte pe o pagină de desen. Acesta este blocul de bază al modulului TechDraw. La plupart des autres vues proviennent de NewView.

![](images/TechDraw_View_example.png )

The View tool adds a representation of one or more objects to a Drawing page. This is the basic building block of the TechDraw workbench. Most other Views are derived in some way from NewView.

![](images/TechDraw_View_example.png ) *View of a solid box with hidden lines*


<div class="mw-translate-fuzzy">

## Cum se utilizează {#cum_se_utilizează}

1.  Selectați unul sau mai multe obiecte (Corp, Aplicație :: Parte, Parte :: Funcție, Proiect de obiect, \... Vezi Note) în fereastra sau arborele 3D.
2.  Dacă aveți mai multe pagini de desen în document, va trebui, de asemenea, să selectați pagina dorită din arborescență.
3.  Apăsați butonul **<img src="images/Techdraw-view.png" width=24px> [View](TechDraw_NewView.md)
**


</div>

1.  Select one or more objects (Body, App::Part, Part::Feature, Draft object, \... See Notes) in the [3D view](3D_view.md) or [Tree view](Tree_view.md).
2.  If you have multiple drawing pages in your document, you will also need to select the desired page in the tree. Use the **Ctrl** to select multiple items in the tree.
3.  Press the **<img src="images/TechDraw_View.svg" width=16px> [Insert View](TechDraw_View.md)** button

View will try to draw anything with a `Shape` property. You can select [Draft](Draft_Workbench.md) objects and [PartDesign Bodies](PartDesign_Body.md) also. View will also extract any shapes from objects within an [App::Part](Std_Part.md) container or a [Group](Std_Group.md).

## Proprietăți

-    **X**: Poziția orizontală a vederii pe pagină (1)

-    **Y**: Poziția verticală a vederii pe pagină.(1)

-    **LockPosition**: Împiedică afișarea vederilor din Gui când este True. Vizualizarea poate fi în continuare mutată prin schimbarea proprietăților X, Y.(1)

-    **Rotation**: Rotație antiorară a afișării vizualizării pe pagină exporimată în grade (1)

-    **ScaleType**: \"Document\": utilizați setările de scală ale Paginii. \"Custom\": utilizați o scală unică doar pentru această vedere. \"Automatic\": potrivește vizualizarea în pagină. (1)

-    **Scale**: A view will be rendered on the page in Scale:1 ratio to the Source. (1)

-    **Caption**: Optional short text caption.

-    **Source**: Links to the Drawable Objects to be depicted

-    **Direction**: A vector representing the viewing direction. See note below. (1)

-    **Perspective**: True for perspective projection, false for orthogonal projection.

-    **Focus**: Distance from camera to projection plane for perspective projections. Needs to be adjusted to fit the object. Too far and the perspective is lost, too close and the object is distorted.

-    **CoarseView**: If true, TechDraw will use a polygon approximation to calculate drawing geometry. If false, TechDraw will use a precision algorithm. See Notes.

-    **Smooth Visible Lines**: Visible Smooth lines on/off.

-    **Seam Visible Lines**: Visible Seam lines on/off.

-    **Iso Visible Lines**:Liniile izometrice vizibile (u,v) sunt activate/dezactivate.

-    **Hard Hidden Lines**: Liniile ascunse sunt activate/dezactivate.

-    **Smooth Hidden Lines**: Liniile lise sunt activate/dezactivate.

-    **Seam Hidden Lines**: Liniile de cusătuiră ( Seam) ascunse activate/dezactivate .

-    **Iso Hidden Lines**: Linii izometrice ascunse (u, v) sunt activate /dezactivate.

-    **Iso Count**: Numărul de linii izometrice (u, v) care se desenează pe fiecare fațetă.

### Data


{{TitleProperty|Base}}

-    **X**: The view\'s horizontal position on the page. (1)

-    **Y**: The view\'s vertical position on the page. (1)

-    **LockPosition**: Prevents Views from being dragged in the Gui when true. The View can still be moved by changing X,Y properties. (1)

-    **Rotation**: Counterclockwise rotation of the View on the page in degrees. (1)

-    **ScaleType**: \"Document\": use the Page\'s scale setting. \"Custom\": use a scale unique to this view. \"Automatic\": fit view to page. (1)

-    **Scale**: A view will be rendered on the page in Scale:1 ratio to the Source. (1)

-    **Caption**: Optional short text caption.


{{TitleProperty|Cosmetics}}


{{TitleProperty|HLR Parameters}}

-    **CoarseView**: If true, TechDraw will use a polygon approximation to calculate drawing geometry. If false, TechDraw will use a precision algorithm. CoarseView can be much faster for complex models. The quality of the drawing is reduced, since every curve is approximated as a series of short line segments. Vertices are not displayed in CoarseView since each short segment would result in two new Vertices and the display becomes cluttered. Linear Dimensions can be added to a CoarseView, but are unlikely to be useful.

:   
    **Note:**CoarseView is affected by an upstream bug in OCCT ([\#3332](https://www.freecadweb.org/tracker/view.php?id=3332)) which causes the View\'s position on the Page to be slightly off from the specified X,Y values.

-    **Smooth Visible**: Visible Smooth lines on/off.

-    **Seam Visible**: Visible Seam lines on/off.

-    **Iso Visible**: Visible Isometric(u,v) lines on/off.

-    **Hard Hidden**: Hidden lines on/off.

-    **Smooth Hidden**: Hidden Smooth lines on/off.

-    **Seam Hidden**: Hidden Seam lines on/off.

-    **Iso Hidden**: Hidden Isometric(u,v) lines on/off.

-    **Iso Count**: Number of Isometric(u,v) lines to draw on each face.


{{TitleProperty|Projection}}

-    **Source**: Links to the drawable objects to be depicted.

-    **XSource**: Links to the drawable objects in an external file. <small>(v0.19)</small> 

-    **Direction**: this vector controls the direction from which you are viewing the object. +X is right, -X is left, +Y is rear, -Y is front (looking into the screen), +Z is up and -Z is down. So a Front view is (0,-1,0) and an isometric view is (1,-1,1). (1)

-    **XDirection**: this vector controls the rotation of the view around the Direction. <small>(v0.19)</small> . (1)

-    **Perspective**: True for perspective projection, false for orthogonal projection.

-    **Focus**: Distance from camera to projection plane for perspective projections. Needs to be adjusted to fit the object. Too far and the perspective is lost, too close and the object is distorted.

\(1\) Aceste proprietăți sunt comune tuturor tipurilor de vizualizare.

-    **Keep Label**: Afișați întotdeauna eticheta de vizualizare dacă este True.

-    **LineWidth**: Grosimea liniilor vizibile. Vezi [Line Groups](TechDraw_LineGroup.md).

-    **HiddenWidth**: Grosimea liniilor ascunse, dacă este activat.

-    **IsoWidth**: Grosimea liniilor suprafeței izometrice(u,v) și a linilor de cotă(Dimension).

-    **ExtraWidth**: nu este implementat încă.

-    **ShowCenters**: Marcajul centrului pentru Cerc/arc de cerc activat/dezactivat.

-    **CenterScale**: Reglarea mărimii marcajului central al arcului de cerc, dacă este activată.

-    **HorizCenterLine**: Afișează o linie orizontală pe centrul vizualizării.

-    **VertCenterLine**: Afișează o linie verticală pe centrul vizualizării.

-    **ShowSectionLine**: Arată/ascunde linia de scțiune dacă există

## Script

Vederile pot fi adăugate la Pages utilizând Python.


**See also:**

[TechDraw API](TechDraw_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The New View tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
view = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewPart','View')
rc = page.addView(view)
FreeCAD.ActiveDocument.View.Source = [App.ActiveDocument.Box]
FreeCAD.ActiveDocument.View.Direction = (0.0,0.0,1.0)
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}  
