---
- GuiCommand:/it
   Name:Draft_PathArray
   Name/it:Serie su tracciato
   MenuLocation:Modifiche → Strumenti serie → Serie su tracciato
   Workbenches:[Draft](Draft_Workbench/it.md), [Arch](Arch_Workbench/it.md)
   SeeAlso:[Serie ortognale](Draft_OrthoArray/it.md), [Serie polare](Draft_PolarArray/it.md), [Serie circolare](Draft_CircularArray/it.md), [Serie di link su tracciato](Draft_PathLinkArray/it.md), [Serie su punti](Draft_PointArray/it.md), [Clone](Draft_Clone/it.md)
   Version:0.14
---

# Draft PathArray/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento **<img src="images/Draft_PathArray.svg" width=16px> [Serie su tracciato](Draft_PathArray/it.md)** posiziona le copie di una forma selezionata lungo un percorso selezionato, che può essere una [Polilinea](Draft_Wire/it.md), una [B-spline](Draft_BSpline/it.md), e bordi simili.


</div>


<div class="mw-translate-fuzzy">

Questo strumento può essere utilizzato su qualsiasi oggetto che abbia una [Part TopoShape](Part_TopoShape/it.md), che significa forme 2D create con [Draft](Draft_Workbench/it.md), ma anche solidi 3D creati con altri ambienti, ad esempio [Part](Part_Workbench/it.md), [PartDesign](PartDesign_Workbench/it.md) o [Arch](Arch_Workbench/it.md).


</div>

<img alt="" src=images/Draft_PathArray_Example.png  style="width:400px;">


<div class="mw-translate-fuzzy">


*Oggetto disposto lungo un percorso*


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare un oggetto che si desidera distribuire.
2.  Selezionare un oggetto percorso o alcuni bordi lungo i quali si vuole distribuire l\'oggetto.
3.  Premere il pulsante **<img src="images/Draft_PathArray.svg" width=16px> [Serie su tracciato](Draft_PathArray/it.md)**.
4.  L\'oggetto Array viene creato immediatamente. È necessario modificare le proprietà dell\'array per modificare il numero e la direzione delle copie create.


</div>

## Alignment

The alignment of the elements in a Draft PathArray depends on the properties of the array and the orientation of the source object. The position of the source object is ignored: for the purpose of the array the {{Value|x}}, {{Value|y}} and {{Value|z}} are set to {{Value|0}}. If the **Align** property of the array is set to `False` the orientation of the array elements is identical to that of the source object. If it is set to `True` the X axis of the local coordinate system of each element placement is tangent to the path. The Y and Z axes of the local coordinate systems depend on the **Align Mode** property of the array. Other array properties involved in the alignment include **Tangent Vector**, **Force Vertical** and **Vertical Vector**.

<img alt="" src=images/Draft_PathArray_example2.png  style="width:600px;"> *3 arrays based on the same non-planar path. From left to right: Align is false, Align is true with Align Mode Original and Align is true with Align Mode Frenet*.

### Align Mode 

Three modes are available:

#### Original

This mode comes closest to the single **Align Mode** available in version 0.18. It relies on a fixed normal vector. If the path is planar this vector is perpendicular to the plane of the path, else a default vector, the positive Z axis, is used. From this normal vector and the local tangent vector (the local X axis) a [cross product](https://en.wikipedia.org/wiki/Cross_product) is calculated. This new vector is used as the local Z axis. The orientation of the local Y axis is determined from the local X and Z axes.

#### Frenet

This mode uses the local normal vector derived from the path at each element placement. If this vector cannot be determined (for example in the case of a straight segment) a default vector, again the positive Z axis, is used instead. With this vector and the local tangent vector the local coordinate system is determined using the same procedure as in the previous paragraph.

#### Tangent

This mode is similar to **Align Mode** {{Value|Original}} but includes the possibility to pre-rotate the source object by specifying a **Tangent Vector**.

### Force Vertical and Vertical Vector 

These properties are only available if **Align Mode** is {{Value|Original}} or {{Value|Tangent}}. If **Force Vertical** is set to `True` the local coordinate system is calculated in a different manner. The **Vertical Vector** is used as a fixed normal vector. From this normal vector and the local tangent vector (the local X axis) again a cross product is calculated. But now this vector is used as the local Y axis. The orientation of the local Z axis is determined from the local X and Y axes.

Using these properties can be required if one of the edged of the path is (almost) parallel to the default normal of the path.

## Proprietà

See also: [Property editor](property_editor.md).


<div class="mw-translate-fuzzy">

Una **Serie su tracciato** deriva da una [Part Feature](Part_Feature/it.md) (classe `Part::Feature`), quindi condivide tutte le proprietà di quest\'ultima. Oltre alle proprietà descritte in [Funzione Part](Part_Feature/it.md), Serie su tracciato ha le seguenti proprietà nell\'[editor delle proprietà](property_editor/it.md).


</div>

### Data


{{TitleProperty|Link}}

The properties in this group are only available for Link arrays. See [Std LinkMake](Std_LinkMake#Properties.md) for more information.

-    **Scale|Float**
    

-    **Scale Vector|Vector|Hidden**
    

-    **Scale List|VectorList**
    

-    **Visibility List|BoolList|Hidden**
    

-    **Placement List|PlacementList|Hidden**
    

-    **Element List|LinkList|Hidden**
    

-    **_ Link Touched|Bool|Hidden**
    

-    **_ Child Cache|LinkList|Hidden**
    

-    **Colored Elements|LinkSubHidden|Hidden**
    

-    **Link Transform|Bool**
    


{{TitleProperty|Alignment}}


<div class="mw-translate-fuzzy">


{{TitleProperty|Alignment}}

-    **Align|Bool**: se è `True` le copie sono allineate al percorso; altrimenti vengono lasciate nel loro orientamento predefinito.

:   
    **Nota:**in alcuni casi la forma appare piatta, in realtà potrebbe essersi spostata nello spazio 3D, quindi, anziché utilizzare una vista piatta, cambiare la vista in assonometrica.

-    **Align Mode|Enumeration**: tre modalità, {{Value|Original}}, {{Value|Frenet}}, {{Value|Tangent}}.

-    **Extra Translation|VectorDistance**: vettore di spostamento aggiuntivo {{Value|(x, y, z)}} che verrà applicato a ciascuna copia lungo il percorso. Questo è utile per apportare piccole modifiche alla posizione delle copie, ad esempio, quando il suo punto di riferimento non corrisponde al punto centrale della sua forma.

-    **Force Vertical|Bool**: se è `True`, il valore di **Vertical Vector** verrà utilizzata come direzione Z locale, quando **Align Mode** è {{Value|Original}} o {{Value|Tangent}}. {{Version/it|0.19}}

-    **Tangent Vector|Vector**: il valore predefinito è {{Value|(1, 0, 0)}}; vettore unità di allineamento che verrà utilizzato quando **Align Mode** è {{Value|Tangent}}. {{Version/it|0.19}}

-    **Vertical Vector|Vector**: il valore predefinito è {{Value|(0, 0, 1)}}; vettore unitario della direzione Z locale che verrà utilizzato quando **Vertical Vector** è `True`. {{Version/it|0.19}}


</div>


{{TitleProperty|Objects}}


<div class="mw-translate-fuzzy">


{{TitleProperty|Objects}}

-    **Base|LinkGlobal**: specifica l\'oggetto da duplicare nel percorso.

-    **Count|Integer**: specifica il numero di copie da creare nel percorso.

-    **Path Object|LinkGlobal**: specifica l\'oggetto lungo il quale verranno distribuite le copie. Deve contenere degli {{Value|'Edges'}} nella sua <img src=images/Draft_Wire.svg style="width:topologia](Part_TopoShape/it.md); ad esempio, potrebbe essere una **[16px"> <img src=images/Draft_BSpline.svg style="width:polilinea](Draft_Wire/it.md)** o una **[16px"> [BSpline](Draft_BSpline/it.md)**.

-    **Path Subelements|LinkSubListGlobal**: specifica i sottoelementi (bordi) del **Path Object** su cui verranno create le copie. Le copie verranno create solo su questi bordi. Se questa proprietà è vuota, le copie verranno distribuite sull\'intero

**Path Object**.


</div>

### View


{{TitleProperty|Link}}

The properties in this group, with the exception of the inherited property, are only available for Link arrays. See [Std LinkMake](Std_LinkMake#Properties.md) for more information.

-    **Draw Style|Enumeration**
    

-    **Line Width|FloatConstraint**
    

-    **Override Material|Bool**
    

-    **Point Size|FloatConstraint**
    

-    **Selectable|Bool**: this is an inherited property that appears in the Selection group for other arrays

-    **Shape Material|Material**
    


{{TitleProperty|Base}}

The properties in this group, with the exception of the inherited property, are only available for Link arrays. See [Std LinkMake](Std_LinkMake#Properties.md) for more information.

-    **Child View Provider|PersistentObject|Hidden**
    

-    **Material List|MaterialList|Hidden**
    

-    **Override Color List|ColorList|Hidden**
    

-    **Override Material List|BoolList|Hidden**
    

-    **Proxy|PythonObject|Hidden**: this is an inherited property.


{{TitleProperty|Display Options}}

The properties in this group are inherited properties. See [Part Feature](Part_Feature#Properties.md) for more information.

-    **Bounding Box|Bool**: this property is not inherited by Link arrays.

-    **Display Mode|Enumeration**: for Link arrays it can be {{value|Link}} or {{value|ChildView}}. For other arrays it can be: {{value|Flat Lines}}, {{value|Shaded}}, {{value|Wireframe}} or {{value|Points}}

-    **Show In Tree|Bool**
    

-    **Visibility|Bool**
    


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: not used.

-    **Pattern Size|Float**: not used.


{{TitleProperty|Object style}}

The properties in this group are not inherited by Link arrays.

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Vedere anche:**

[Draft API](Draft_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento PathArray può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) utilizzando la seguente funzione:


</div>


```python
path_array = make_path_array(base_object, path_object,
                             count=4, extra=App.Vector(0, 0, 0), subelements=None,
                             align=False, align_mode="Original", tan_vector=App.Vector(1, 0, 0),
                             force_vertical=False, vertical_vector=App.Vector(0, 0, 1),
                             use_link=True)
```


<div class="mw-translate-fuzzy">

-   Crea un oggetto `"PathArray"` da un `base_object`, inserendo fino a `count` copie lungo un `path_object`.
    -   Invece di un riferimento a un oggetto, `base_object` e `path_object` possono anche essere delle `Labels` (stringhe) di oggetti esistenti nel documento corrente.
    -   Se viene fornito un `extra`, esso è un vettore che sposta ciascuna delle singole copie di una piccola quantità.
    -   Se vengono forniti dei `subelements`, è un elenco di bordi di `path_object`, per esempio, `['Edge1', 'Edge2']`; le copie verranno create lungo questo percorso più breve.
    -   Se `align` è `True`, le copie sono allineate lungo il `path_object` a seconda del valore di `align_mode`, che può essere `"Original"`, `"Frenet"` o `"Tangent"`.
    -   Se viene fornito un `tan_vector`, è un vettore unitario che definisce la direzione tangente locale della copia lungo il percorso. Viene utilizzato quando `align_mode` è `"Tangent"`.
    -   Se `force_vertical` è `True`, il valore di `vertical_vector` viene utilizzato per determinare la direzione Z locale della copia lungo il percorso. Viene utilizzato quando `align_mode` è `"Original"` o `"Tangent"`.
    -   Se `use_link` è `True`, il tipo di serie creata sarà una [Serie di link su tracciato](Draft_PathLinkArray/it.md), i cui elementi sono delle istanze [App Link](App_Link/it.md) invece di normali copie.


</div>

Esempio:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(500, -1000, 0)
p2 = App.Vector(1500, 1000, 0)
p3 = App.Vector(3000, 500, 0)
p4 = App.Vector(4500, 100, 0)
spline = Draft.make_bspline([p1, p2, p3, p4])
obj = Draft.make_polygon(3, 500)

path_array = Draft.make_path_array(obj, spline, 6)
doc.recompute()

wire = Draft.make_wire([p1, -p2, -p3, -p4])
path_array2 = Draft.make_path_array(obj, wire, count=3, extra=App.Vector(0, -500, 0), subelements=["Edge2", "Edge3"], align=True, force_vertical=True)
doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft PathArray/it
