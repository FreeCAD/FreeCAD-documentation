# Part Primitives/it
---
 GuiCommand:   Name: Part_Primitives   Name/it: Crea primitive   Workbenches: Part_Workbench/it   Parte---


</div>




<div class="mw-translate-fuzzy">

## Descrizione


</div>


<div class="mw-translate-fuzzy">

[Primitive](Part_Primitives/it.md) di Part apre una finestra di dialogo per creare una qualsiasi delle primitive geometriche parametriche definite nell\'ambiente <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Parte](Part_Workbench/it.md).


</div>

<img alt="" src=images/Part_Primitives_example.png  style="width:600px;">


<div class="mw-translate-fuzzy">



*Forme primitive che possono essere create con Part.*


</div>

## Usage

### Create

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Part_Primitives.svg" width=16px> [Part Primitives](Part_Primitives.md)** button.
    -   Select the **Part → <img src="images/Part_Primitives.svg" width=16px> Create Primitives...** option from the menu.
2.  The **Geometric Primitives** task panel opens.
3.  Select a primitive type from the dropdown list.
4.  Specify the properties.
5.  Press the **Create** button.
6.  The primitive object is created.
7.  Note that the task panel stays open.
8.  Optionally create additional primitives.
9.  Press the **Close** button to close the task panel and finish the command.

### Edit

1.  Double-click the primitive object in the [Tree view](Tree_view.md).
2.  The **Geometric Primitives** task panel opens.
3.  Change one or more properties.
4.  The object is dynamically updated in the [3D view](3D_view.md).
5.  Press the **OK** button.

The properties of a Part Primitive can also be changed in the [Property editor](Property_editor.md), and its **Placement** can also be changed with the <img alt="" src=images/Std_TransformManip.svg  style="width:16px;"> [Std TransformManip](Std_TransformManip.md) command.




<div class="mw-translate-fuzzy">

## Primitive geometriche 


</div>


<div class="mw-translate-fuzzy">

Alcune delle primitive geometriche (parametriche) disponibili che sono possibili:

:   <img alt="" src=images/Part_Plane.svg  style="width:32px;"> [Piano](Part_Plane/it.md): inserisce un semplice piano parametrico di 10 x 10 mm, con i parametri di posizione, lunghezza e larghezza.
:   <img alt="" src=images/Tree_Part_Box_Parametric.svg  style="width:32px;"> [Box/Cubo](Part_Box/it.md): inserisce nel documento attivo un parametrico [cuboide rettangolare](http://en.wikipedia.org/wiki/Cuboid#Rectang_cuboid), primitiva geometrica.
:   <img alt="" src=images/Tree_Part_Cylinder_Parametric.svg  style="width:32px;"> [Cilindro](Part_Cylinder/it.md): Inserisce nel documento attivo un semplice cilindro parametrico, con i parametri di posizione, angolo, raggio e altezza.
:   <img alt="" src=images/Tree_Part_Cone_Parametric.svg  style="width:32px;"> [Cono](Part_Cone/it.md): Inserisce un tronco di cono parametrico nel documento attivo.
:   <img alt="" src=images/Tree_Part_Sphere_Parametric.svg  style="width:32px;"> [Sfera](Part_Sphere/it.md): Inserisce una sfera parametrica, con i parametri di posizione, angolo1, angolo2, angolo3 e raggio.
:   <img alt="" src=images/Part_Ellipsoid.svg  style="width:32px;"> [Ellissoide](Part_Ellipsoid/it.md): Inserisce un solido ellissoide parametrico nel documento attivo.
:   <img alt="" src=images/Tree_Part_Torus_Parametric.svg  style="width:32px;"> [Toro](Part_Torus/it.md): Inserisce un semplice toro parametrico, con posizione, angolo1, angolo2, angolo3, raggio1 e raggio2 come parametri.
:   <img alt="" src=images/Part_Prism.svg  style="width:32px;"> [Prisma](Part_Prism/it.md): Inserisce un solido definito da una sezione trasversale poligonale regolare e un\'altezza. {{Version/it|0.14}}
:   <img alt="" src=images/Part_Wedge.svg  style="width:32px;"> [Cuneo](Part_Wedge/it.md): Inserisce un oggetto Cuneo parametrico.
:   <img alt="" src=images/Part_Helix.svg  style="width:32px;"> [Elica](Part_Helix/it.md): Inserisce una primitiva geometrica ad elica. L\'uso comune dell\'elica è la creazione di [filettature](Thread_for_Screw_Tutorial/it.md).
:   <img alt="" src=images/Part_Spiral.svg  style="width:32px;"> [Spirale](Part_Spiral/it.md): Inserisce una primitiva geometrica a spirale. {{Version/it|0.14}}
:   <img alt="" src=images/Part_Circle.svg  style="width:32px;"> [Cerchio](Part_Circle/it.md): Inserisce un bordo curvo circolare nel documento attivo.
:   <img alt="" src=images/Part_Ellipse.svg  style="width:32px;"> [Ellisse](Part_Ellipse/it.md): Inserisce un bordo curvo ellittico nel documento attivo.
:   <img alt="" src=images/Part_Point.svg  style="width:32px;"> [Punto](Part_Point/it.md) (Vertice): Inserisce una primitiva geometrica punto (vertice).
:   <img alt="" src=images/Part_Line.svg  style="width:32px;"> [Linea](Part_Line/it.md) (Bordo): crea un semplice segmento di linea delimitato da due vertici.
:   <img alt="" src=images/Part_RegularPolygon.svg  style="width:32px;"> [Poligono regolare](Part_RegularPolygon/it.md): Inserisce una primitiva geometrica poligonale regolare nel documento attivo. {{Version/it|0.14}}


</div>

## Notes

-   The Part Primitives command cannot create a <img alt="" src=images/Part_Tube.svg  style="width:16px;"> [Part Tube](Part_Tube.md).



## Script

See also: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/), [Part scripting](Part_scripting.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).


<div class="mw-translate-fuzzy">

Prova la creazione delle primitive con uno script.{{Version/it|0.19}}


</div>


```python
import parttests.part_test_objects as pto
pto.create_test_file("example_file")
```


<div class="mw-translate-fuzzy">

Questo script si trova nella directory di istallazione del programma, e può essere esaminato per vedere come sono create le forme primitive.


</div>


```python
$INSTALL_DIR/Mod/Part/parttests/part_test_objects.py
```


<div class="mw-translate-fuzzy">

Può essere utilizzato anche come input per il programma.


</div>


```python
freecad $INSTALL_DIR/Mod/Part/parttests/part_test_objects.py
```


<div class="mw-translate-fuzzy">





</div>


{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Primitives/it
