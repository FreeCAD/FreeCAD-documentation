---
- GuiCommand:/it   Name:Surface Filling   Name/it:Surface Filling   MenuLocation:Surface → Riempimento...   Workbenches:[Version:0.17](Surface_Workbench/it___Surface.md)|---

## Descrizione

<img alt="" src=images/Surface_Filling.svg  style="width:16px;"> [Surface Filling](Surface_Filling/it.md) crea una superficie da una serie di bordi collegati.

La superficie può essere modificata aggiungendo bordi e vertici di vincolo attraverso i quali deve passare la superficie.

<img alt="" src=images/Surface_Filling_example.png  style="width:600px;">


*Esempio di una superficie riempita, delimitata da quattro spigoli situati nel piano XY; (a sinistra) solo i quattro bordi e (a destra) una curva aggiunta nello spazio che definisce la curvatura della superficie*

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Assicurarsi di avere almeno tre bordi o curve nello spazio che formano un contorno chiuso. I bordi possono essere creati con gli strumenti di <img alt="" src=images/Workbench_Draft.svg  style="width:16px;"> [Draft](Draft_Module/it.md) o di <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [Sketcher](Sketcher_Workbench/it.md). L\'uso di tre bordi crea una superficie triangolare; quattro bordi una superficie quadrilatera.
    -   Se è il caso, all\'interno del contorno chiuso possono essere disegnate delle curve. Non è necessario che tocchino i bordi. Queste curve possono essere utilizzate per controllare la curvatura della superficie risultante.
    -   Allo stesso modo, è possibile utilizzare un numero di vertici con lo stesso scopo per indicare dove deve passare la superficie.
2.  Premere il pulsante **<img src=images/Surface_Filling.svg style="width:16px"> Surface filling**.
3.  Nella sezione {{MenuCommand|Boundary}}, premere **Add edge**.
4.  Usare il puntatore per selezionare i bordi desiderati nella [vista 3D](3D_view/it.md); viene visualizzata un\'anteprima della forma finale dopo aver selezionato i bordi validi che formano un contorno chiuso.
    -   Come opzione, andare alla sezione {{MenuCommand|Curvature: non-boundary edges}} (bordi non di confine), premere **Add edge**, e selezionare i bordi desiderati nella [vista 3D](3D_view/it.md).
    -   Come opzione, andare alla sezione {{MenuCommand|Curvature: non-boundary vertices}} (vertici non di confine), premere **Add vertex**, e scegliere i vertici desiderati nella [vista 3D](3D_view/it.md).
5.  Premere **OK** per completare l\'operazione.


</div>


<div class="mw-translate-fuzzy">

Gli spigoli di base che formano il contorno chiuso, così come i vertici e gli spigoli ausiliari, possono appartenere a curve 2D di <img alt="" src=images/Workbench_Draft.svg  style="width:16px;"> [Draft](Part_Workbench/it.md) o di <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [Sketcher](Sketcher_Workbench/it.md), ma possono anche appartenere a oggetti solidi 3D come quelli creati con <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Part](Part_Workbench/it.md) o <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [PartDesign](PartDesign_Workbench/it.md).


</div>

## Opzioni

-   Nella sezione {{MenuCommand|Boundary}}:
    -   
        **Add edge**
        
        : premere una volta per iniziare a selezionare i bordi {{MenuCommand|Boundary edges}} nella [vista 3D](3D_view/it.md). Possono essere selezionati i bordi dritti come le <img alt="" src=images/Draft_Wire.svg  style="width:16px;"> [polilinee di Draft](Draft_Wire/it.md) e le <img alt="" src=images/Sketcher_CreatePolyline.svg  style="width:16px;"> [polilinee di Sketcher](Sketcher_CreatePolyline/it.md), o i bordi curvi come le <img alt="" src=images/Draft_BSpline.svg  style="width:16px;"> [BSpline di Draft](Draft_BSpline/it.md) e le <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:16px;"> [BSpline di Sketcher ](Sketcher_CreateBSpline/it.md), così come qualsiasi bordo di oggetti solidi, come quelli di un <img alt="" src=images/PartDesign_Body.svg  style="width:16px;"> [Corpo](PartDesign_Body/it.md) e le <img alt="" src=images/Part_Primitives.svg  style="width:16px;"> [Primitive di Part](Part_Primitives/it.md).

    -   
        **Remove edge**
        
        : premere una volta per iniziare a selezionare i bordi nella vista 3D; questi bordi devono essere stati precedentemente selezionati con **Add edge**.

    -   
        **Right mouse button**
        
        : aprire il menu contestuale e selezionare **Remove**, o premere **Del** sulla tastiera, per rimuovere il bordo attualmente selezionato nell\'elenco.

-   Nella sezione {{MenuCommand|Curvature: non-boundary edges}}; il pulsante **Add edge** è disponibile per selezionare bordi ausiliari (linee rette o B-Splines) per controllare la curvatura della superficie. La superficie sarà costretta a passare attraverso questi bordi ausiliari. Funziona meglio quando i bordi ausiliari si trovano all\'interno della regione delimitata da {{MenuCommand|Boundary edges}}.
-   Nella sezione {{MenuCommand|Curvature: non-boundary vertices}}; simile a non-boundary edges, l\'utente può selezionare vertici ausiliari per controllare la curvatura. Questi vertici possono essere indipendenti <img alt="" src=images/Draft_Point.svg  style="width:16px;"> [ punti di Draft](Draft_Point/it.md) o <img alt="" src=images/Part_Point.svg  style="width:16px;"> [punti di Part](Part_Point/it.md), o possono appartenere a qualsiasi bordo (linee rette o B-Splines) o essere un vertice in un oggetto solido. In questo caso, la superficie sarà vincolata a passare attraverso questi punti ausiliari.
-   Premere **Cancel** o **Esc** per interrompere l\'operazione corrente.

## Proprietà

Una [Surface Filling](Surface_Filling/it.md) (classe `Surface::Filling`) è derivato dalla base [Part Feature](Part_Feature/it.md) (classe `Part::Feature`, attraverso la sottoclasse `Part::Spline`), quindi condivide tutte le proprietà di quest\'ultima.


<div class="mw-translate-fuzzy">

Oltre alle proprietà descritte in [Part Feature](Part_Feature/it.md), Surface Filling ha le seguenti proprietà nell\'[editor delle proprietà](property_editor/it.md).


</div>

### Dati


{{TitleProperty|Filling}}

-    **Boundary Edges|LinkSubList**: bordi di confine; C0 è richiesto per i bordi senza una faccia corrispondente.

-    **Boundary Faces|StringList**:

-    **Boundary Order|IntegerList**: ordine di vincolo sulle facce del contorno; sono possibili {{Value|0}}, {{Value|1}}, e {{Value|2}}.

-    **Unbound Edges|LinkSubList**: bordi di vincoli non legati; C0 è richiesto per i bordi senza una faccia corrispondente.

-    **Unbound Faces|StringList**:

-    **Unbound Order|IntegerList**: ordine di vincolo sulle facce non legate; sono possibili {{Value|0}}, {{Value|1}}, e {{Value|2}}.

-    **Free Faces|LinkSubList**: vincolo su una faccia libera.

-    **Free Order|IntegerList**: ordine di vincolo sulle facce libere.

-    **Points|LinkSubList**: punti di vincolo sulla superficie.

-    **Initial Face|LinkSub**: superficie iniziale da utilizzare.

-    **Degree|Integer**: grado iniziale, il valore predefinito è {{Value|3}}.

-    **Points On Curve|Integer**: numero di punti su un bordo per vincolarlo.

-    **Iterations|Integer**: numero di iterazioni, il valore predefinito è {{Value|2}}.

-    **Anisotropy|Bool**: il valore predefinito è {{false}}.

-    **Tolerance2d|Float**: tolleranza 2D, il valore predefinito è {{Value|0.0}}.

-    **Tolerance3d|Float**: tolleranza 3D, il valore predefinito è {{Value|0.0}}.

-    **Tol Angular|Float**: tolleranza G1, il valore predefinito è {{Value|0.01}}.

-    **Tol Curvature|Float**: tolleranza G2, il valore predefinito è {{Value|0.10}}.

-    **Maximum Degree|Integer**: grado massimo della curva, il valore predefinito è {{Value|8}}.

-    **Maximum Segments|Integer**: numero massimo di segmenti, il valore predefinito è {{Value|9}}.

### Vista


{{TitleProperty|Base}}

-    **Control Points|Bool**: il valore predefinito è `false`; se impostato su `true`, mostrerà una sovrapposizione con i punti di controllo della superficie.

## Limitazioni

Il codice di surface dal kernel di modellazione interno [OpenCASCADE](OpenCASCADE/it.md) è fragile e non può gestire correttamente l\'input sbagliato. Le seguenti situazioni possono causare problemi e causare il crash del programma, quindi dovrebbero essere evitate:

-   Aggiungere dei **Boundary Edges** che comporterebbe diverse facce chiuse. In questo caso, questi bordi dovrebbero essere aggiunti come **Unbound Edges** per controllare solo la curvatura.
-   Utilizzare **Boundary Edges** parametrici (ad esempio, delle <img alt="" src=images/Draft_BSpline.svg  style="width:16px;"> [BSplines](Draft_BSpline/it.md)) che quando ricalcolate non riescono a produrre una regione chiusa. Cioè, i bordi da usare come **Boundary Edges** devono sempre formare una forma chiusa, anche se le loro proprietà interne cambiano.

## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)


<div class="mw-translate-fuzzy">

Lo strumento Surface Filling può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) aggiungendo l\'oggetto `Surface::Filling`.

-   I bordi da utilizzare per definire la superficie devono essere assegnati come [LinkSubList](LinkSubList/it.md) alla proprietà `BoundaryEdges` dell\'oggetto.
-   Gli spigoli ausiliari e i vertici devono essere assegnati come [LinkSubLists](LinkSubList/it.md) alle proprietà `UnboundEdges` e `Points` dell\'oggetto.
-   Tutti gli oggetti con bordi devono essere calcolati prima di poter essere utilizzati come input per le proprietà dell\'oggetto Filling.


</div>


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

a = App.Vector(-20, -20, 0)
b = App.Vector(-18, 25, 0)
c = App.Vector(60, 26, 0)
d = App.Vector(33, -20, 0)

points1 = [a, App.Vector(-20, -8, 0), App.Vector(-17, 7, 0), b]
obj1 = Draft.make_bspline(points1)

points2 = [b, App.Vector(0, 25, 0), c]
obj2 = Draft.make_bspline(points2)

points3 = [c, App.Vector(37, 4, 0), d]
obj3 = Draft.make_bspline(points3)

points4 = [d, App.Vector(-2, -18, 0), a]
obj4 = Draft.make_bspline(points4)
doc.recompute()

surf = doc.addObject("Surface::Filling", "Surface")
surf.BoundaryEdges = [(obj1, "Edge1"),
                      (obj2, "Edge1"),
                      (obj3, "Edge1"),
                      (obj4, "Edge1")]
doc.recompute()

# ---------------------------------------------------------
points_spl = [App.Vector(-10, 0, 2),
              App.Vector(4, 0, 7),
              App.Vector(18, 0, -5),
              App.Vector(25, 0, 0),
              App.Vector(30, 0, 0)]
aux_edge = Draft.make_bspline(points_spl)
doc.recompute()

surf.UnboundEdges = [(aux_edge, "Edge1")]
doc.recompute()

# ---------------------------------------------------------
aux_v1 = Draft.make_line(App.Vector(-13, -12, 5),
                         App.Vector(-13, -12, -5))
aux_v2 = Draft.make_line(App.Vector(-3, 18, 5),
                         App.Vector(-3, 18, -5))
doc.recompute()

surf.Points = [(aux_v1, "Vertex2"),
               (aux_v2, "Vertex1")]
doc.recompute()
```





{{Surface Tools navi

}} 
