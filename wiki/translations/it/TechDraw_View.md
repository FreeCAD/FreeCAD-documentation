---
- GuiCommand:
   Name: TechDraw_View
   Name/it: Vista
   MenuLocation: TechDraw -> Vista
   Workbenches: TechDraw_Workbench/it
   SeeAlso: TechDraw_ProjectionGroup/it, TechDraw_SectionView/it
---

# TechDraw View/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento Vista aggiunge in una pagina di disegno una rappresentazione di uno o più oggetti. Questo è l\'elemento base del modulo TechDraw. La maggior parte delle altre viste sono derivate in qualche modo da Nuova vista.


</div>


<div class="mw-translate-fuzzy">

-   Vista disegna qualsiasi cosa che abbia una proprietà `Shape`. È anche possibile selezionare oggetti [Draft](Draft_Workbench/it.md) o [Corpi di PartDesign](PartDesign_Body/it.md). Vista estrae anche qualsiasi forma dagli oggetti all\'interno di un contenitore [App::Part](Std_Part/it.md) o di un [Grouppo](Std_Group/it.md).


</div>

![](images/TechDraw_View_example.png ) 
*Vista di un solido con linee nascoste*



## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare uno o più oggetti (Body, App::Part, Part::Feature, Draft object, \... Vedere Note) nella [vista 3D](3D_view.md) o nella [vista a albero](Tree_view.md).
2.  Se nel documento ci sono più pagine di disegno, è anche necessario selezionare la pagina desiderata nella struttura. Utilizzare il **Ctrl** per selezionare più elementi nella struttura.
3.  Premere il pulsante **<img src="images/TechDraw_View.svg" width=16px> [Vista](TechDraw_View/it.md)
**


</div>



## Proprietà

### Data


{{TitleProperty|Base}}


<div class="mw-translate-fuzzy">

### Dati

-    **X**: la posizione orizzontale della vista nella pagina. (1)

-    **Y**: la posizione verticale della vista nella pagina. (1)

-    **LockPosition**: quando è vero, impedisce che le viste vengano trascinate nella Gui. La vista può ancora essere spostata cambiando le proprietà X, Y. (1)

-    **Rotation**: rotazione in gradi in senso antiorario della vista sulla pagina. (1)

-    **ScaleType**: \"Document\": usa l\'impostazione della scala della Pagina. \"Custom\": usa una scala unica per questa vista. \"Automatic\": adatta la vista alla pagina. (1)

-    **Scale**: la vista viene resa sulla pagina in Scala: 1 è equivalente alla fonte. (1)

-    **Caption**: breve didascalia di testo opzionale.

-    **Source**: collegamenti agli oggetti disegnabili da rappresentare.

-    **Direction**: un vettore che rappresenta la direzione della vista. Direzioni comuni sono Frontale: (0,-1,0), Dall\'alto: (0,0,1), Destra: (1,0,0), Assonometria: (1,1,1). Vedere le note sottostanti. (1)

-    **XDirection**: questo vettore controlla la rotazione della vista attorno alla Direction. Introdotto in v0.19. (1)

-    **Perspective**: vero per la proiezione prospettica, falso per la proiezione ortogonale.

-    **Focus**: distanza dalla telecamera al piano di proiezione per le proiezioni prospettiche. Deve essere regolata per adattarsi all\'oggetto. Se è troppo lontana si perde la prospettiva, se è troppo vicina l\'oggetto viene distorto.

-    **CoarseView**: se è vero, TechDraw usa un\'approssimazione poligonale per calcolare la geometria del disegno. Se è false, TechDraw usa un algoritmo di precisione. CoarseView può essere molto più veloce per modelli complessi. La qualità del disegno è ridotta, poiché ogni curva è approssimata come una serie di segmenti di linee corte. In CoarseView i vertici non vengono visualizzati poiché ogni segmento breve comporterebbe due nuovi vertici e il display si ingombrerebbe. A CoarseView possono essere aggiunte le quote lineari, ma è improbabile che siano utili.

:   
    **Note:**CoarseView è affetto da un bug in OCCT ([#3332](https://www.freecadweb.org/tracker/view.php?id=3332)) che fa sì che la posizione della vista sulla pagina sia leggermente diversa dai valori X, Y specificati.

-    **Smooth Visible Lines**: mostra o nasconde le Smooth lines.

-    **Seam Visible Lines**: mostra o nasconde le linee di congiunzione.

-    **Iso Visible Lines**: mostra o nasconde le linee Isometriche(u,v).

-    **Hard Hidden Lines**: mostra o nasconde le linee degli spigoli nascosti.

-    **Smooth Hidden Lines**: mostra o nasconde le linee Smooth lines nascoste.

-    **Seam Hidden Lines**: mostra o nasconde le linee di congiunzione nascoste.

-    **Iso Hidden Lines**: mostra o nasconde le linee Isometriche(u,v).

-    **Iso Count**: numero di linee Isometriche(u,v) da disegnare su ogni faccia.


</div>


{{TitleProperty|Cosmetics}}

-    **Cosmetic Vertexes|TechDraw::PropertyCosmeticVertexList|Hidden**
    

-    **Cosmetic Edges|TechDraw::PropertyCosmeticEdgeList|Hidden**
    

-    **Center Lines|TechDraw::PropertyCenterLineList|Hidden**
    

-    **Geom Formats|TechDraw::PropertyGeomFormatList|Hidden**
    


{{TitleProperty|HLR Parameters}}

-    **Coarse View|Bool**: If `True`, TechDraw will use a polygon approximation to calculate drawing geometry. If `False`, TechDraw will use a precision algorithm. CoarseView can be much faster for complex models. The quality of the drawing is reduced, since every curve is approximated as a series of short line segments. Vertices are not displayed in CoarseView since each short segment would result in two new Vertices and the display becomes cluttered. Linear Dimensions can be added to a CoarseView, but are unlikely to be useful.

-    **Smooth Visible|Bool**: Visible Smooth lines on/off.

-    **Seam Visible|Bool**: Visible Seam lines on/off.

-    **Iso Visible|Bool**: Visible Isometric(u,v) lines on/off.

-    **Hard Hidden|Bool**: Hidden lines on/off.

-    **Smooth Hidden|Bool**: Hidden Smooth lines on/off.

-    **Seam Hidden|Bool**: Hidden Seam lines on/off.

-    **Iso Hidden|Bool**: Hidden Isometric(u,v) lines on/off.

-    **Iso Count|Integer**: Number of Isometric(u,v) lines to draw on each face.


{{TitleProperty|Projection}}

-    **Source|LinkList**: Links to the drawable objects to be depicted.

-    **XSource|XLinkList**: Links to the drawable objects in an external file.

-    **Direction|Vector**: This vector controls the direction from which you are viewing the object. +X is right, -X is left, +Y is rear, -Y is front (looking into the screen), +Z is up and -Z is down. So a Front view is (0,-1,0) and an isometric view is (1,-1,1).

-    **XDirection|Vector**: This vector controls the rotation of the view around the Direction.

-    **Perspective|Bool**: `True` for perspective projection, `False` for orthogonal projection.

-    **Focus|Distance**: Distance from camera to projection plane for perspective projections. Needs to be adjusted to fit the object. Too far and the perspective is lost, too close and the object is distorted.

### View


{{TitleProperty|Base}}

-    **Keep Label|Bool**: Always show view label if `True`. (1)

-    **Stack Order|Integer**: Over or under lap relative to other views. (1) <small>(v0.21)</small> 


{{TitleProperty|Decoration}}

-    **Arc Center Marks|Bool**: Circular arc center marks on/off.

-    **Center Scale|Float**: Circular arc center mark size adjustment, if enabled.

-    **Horiz Center Line|Bool**: Show a horizontal centerline through the view.

-    **Section Line Color|Color**: Set the section line color if applicable.

-    **Section Line Style|Enumeration**: Set the section line style if applicable.

-    **Show All Edges|Bool**: Temporarily show invisible lines.

-    **Show Section Line|Bool**: Show/hide the section line if applicable.

-    **Vert Center Line|Bool**: Show a vertical centerline through the view.


{{TitleProperty|Highlight}}

-    **Highlight Adjust|Float**: Adjust the rotation of the Detail highlight if applicable.

-    **Highlight Line Color|Color**: Set the highlight line color if applicable.

-    **Highlight Line Style|Enumeration**: Set the highlight line style if applicable.


{{TitleProperty|Lines}}

-    **Extra Width|Length**: Not implemented yet.

-    **Hidden Width|Length**: The thickness of hidden lines, if enabled.

-    **Iso Width|Length**: The thickness of isometric(u,v) surface lines and Dimension lines.

-    **Line Width|Length**: The thickness of visible lines. See [Line Groups](TechDraw_LineGroup.md).

\(1\) queste proprietà sono comuni a tutti i tipi di Viste.



## Script


<div class="mw-translate-fuzzy">


**Vedere anche:**

[API TechDraw](TechDraw_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>

A View can be created with [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
import FreeCAD as App

doc = App.ActiveDocument
box = doc.addObject("Part::Box", "Box")

page = doc.addObject("TechDraw::DrawPage", "Page")
template = doc.addObject("TechDraw::DrawSVGTemplate", "Template")
template.Template = App.getResourceDir() + "Mod/TechDraw/Templates/A4_LandscapeTD.svg"
page.Template = template

# Toggle the visibility of the page to ensure its width and height are updated (hack):
page.Visibility = False
page.Visibility = True

view = doc.addObject("TechDraw::DrawViewPart", "View")
page.addView(view)
view.Source = [box]
view.Direction = (0, 0, 1)

view.X = page.PageWidth / 2
view.Y = page.PageHeight / 2

doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw View/it
