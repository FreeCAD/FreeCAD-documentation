# Draft Shape2DView/it
---
- GuiCommand:/it
   Name:Draft Shape2DView
   Name/it:Vista 2D
   Workbenches:[Draft](Draft_Workbench/it.md), [Architettura](Arch_Workbench/it.md)
   MenuLocation:Draft → Vista profilo 2D
   SeeAlso:[Part](Part_Workbench/it.md), [TechDraw](TechDraw_Workbench/it.md)---


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Questo strumento produce una proiezione 2D da un oggetto solido 3D selezionato come quelli creati con gli ambienti [Part](Part_Workbench/it.md), [PartDesign](PartDesign_Workbench/it.md), e [Arch](Arch_Workbench/it.md)


</div>


<div class="mw-translate-fuzzy">

La proiezione risultante è un oggetto Draft e viene posizionata nella vista 3D. Questo oggetto può essere visualizzato in una pagina di [TechDraw](TechDraw_Workbench/it.md), usando lo strumento [Nuova vista di Draft](TechDraw_DraftView/it.md). In alternativa, TechDraw ha i suoi propri strumenti per creare delle viste proiettate. Ma questi creano proiezioni che vengono visualizzate solo sulla pagina di disegno e non nella [3D view](3D_view.md).


</div>

![](images/Draft_Shape2DView_example.jpg )


<div class="mw-translate-fuzzy">



*Proiezione di forme solide nel piano XY*


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Ruotare la vista in modo che rifletta la direzione della proiezione desiderata. Ad esempio, una vista dall\'alto proietta l\'oggetto sul piano XY.
2.  Selezionare un oggetto 3D.
3.  Premere il pulsante **<img src="images/Draft_Shape2DView.svg" width=16px> [Vista profilo 2D](Draft_Shape2DView/it.md)**. Se non è selezionato nessun oggetto, si viene inviti a selezionarne uno.


</div>

## How to produce plans and sections with different linewidths 

<img alt="" src=images/Draft_shape2dview_example_plan.png  style="width:700px;">

Drawings with different linewidths for viewed and cut lines can easily be produced by using two shape2Dview objects from a same [Arch SectionPlane](Arch_SectionPlane.md). One of the shape2Dview objects has its projection mode set to **Solid**, which renders the viewed lines, and another set to **Cut lines** or **Cut faces** to render the cut lines. The two shape2Dviews are then placed at the same location, one on top of the other.

## Proprietà

See also: [Property editor](Property_editor.md).

A Draft Shape2DView object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

-    **Projection**: specifica la direzione della proiezione come un vettore. Ad esempio, (0,0,1) è una proiezione che guarda lungo l\'asse Z, e che proietta sul piano XY; (1,0,0) è una proiezione che guarda lungo l\'asse X, e che proietta sul piano YZ; (0,1,0) è una proiezione che guarda lungo l\'asse Y, e che proietta sul piano XZ. I valori possono anche essere negativi, nel qual caso la direzione di proiezione è invertita.

-    **Projection Mode**: può essere \"Solid\", \"Individual Faces\", \"Cutlines\", e \"Cutfaces\".

    -   La proiezione predefinita è \"Solid\", che proietta l\'intera forma selezionata.
    -   Se sono selezionate solo alcune facce dell\'oggetto base, la modalità \"Individual Faces\" proietta solo quelle facce.
    -   Se l\'oggetto selezionato è un [Piano di sezione](Arch_SectionPlane/it.md) di Arch, la modalità \"Cutlines\" proietta solo i bordi tagliati dal piano della sezione.
    -   Se l\'oggetto selezionato è un [Piano di sezione](Arch_SectionPlane/it.md) di Arch, la modalità \"Cutfaces\" mostra le aree di taglio dei solidi come facce.

-    **In Place**: se è `True`, in combinazione con la modalità \"Cutlines\" o \"Cutfaces\", la proiezione risultante appare complanare con il [Piano di sezione](Arch_SectionPlane/it.md) di Arch. {{Version/it|0.17}}

-    **HiddenLines**: se è `True` mostra le linee nascoste della proiezione.

-    **Tessellation**: se è `True` esegue la tassellatura di ellissi e spline, cioè rappresenta le curve con segmenti di linea molto sottili.

:   
    **Note:**questo potrebbe essere intensivo dal punto di vista computazionale se **Segment Length** è molto piccolo.

-    **Segment Length**: specifica la dimensione in millimetri dei segmenti lineari se **Tessellation** è `True`.

:   
    **Note:**impostare prima un valore più grande e poi cambiarlo in un valore più piccolo per ottenere una risoluzione migliore.

-    **Visible Only**: se è `True` la proiezione viene ricalcolata solo se è visibile.


</div>

### View


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: not used.

-    **Pattern Size|Float**: not used.

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Vedere anche:**

[Draft API](Draft_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Vista 2D può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione:


</div>


```python
shape2dview = make_shape2dview(baseobj, projectionVector=None, facenumbers=[])
```


<div class="mw-translate-fuzzy">

-   Crea una `Shape2DView` come proiezione del dato `baseobj`.
    -   Se `facenumbers` è dato, esso è una lista di numeri di faccia da considerare per la proiezione.
-   Se è dato un `projectionVector`, esso viene usato; altrimenti la proiezione predefinita è lungo l\'asse Z.


</div>


<div class="mw-translate-fuzzy">

L\'attributo `ProjectionMode` deve essere sovrascritto con la modalità desiderata, che può essere `"Solid"`, `"Individual Faces"`, `"Cutlines"`, o `"Cutfaces"`.


</div>

Esempio:


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
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Shape2DView/it
