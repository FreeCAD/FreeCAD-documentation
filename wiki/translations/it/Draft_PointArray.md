---
- GuiCommand:/it
   Name:Draft_PointArray
   Name/it:Serie su punti
   Icon:Draft_PointArray.svg
   MenuLocation:Modificche → Strumenti serie →  Serie su punti
   Workbenches:[Draft](Draft_Workbench/it.md), [Arch](Arch_Workbench/it.md)
   Version:0.18
   SeeAlso:[Serie ortogonale](Draft_OrthoArray/it.md), [Serie polare](Draft_PolarArray/it.md), [Serie circolare](Draft_CircularArray/it.md), [Serie su tracciato](Draft_PathArray/it.md), [Serie di link su tracciato](Draft_PathLinkArray/it.md), [Serie di link su punti](Draft_PointLinkArray/it.md), [Clona](Draft_Clone/it.md)
---


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento <img alt="" src=images/Draft_PointArray.svg  style="width:16px;"> Serie su punti posiziona le copie di una forma selezionata lungo vari punti selezionati.


</div>


<div class="mw-translate-fuzzy">

Questo strumento può essere utilizzato su qualsiasi oggetto che abbia una [Part TopoShape](Part_TopoShape/it.md), che significa forme 2D create con [Draft](Draft_Workbench/it.md), ma anche solidi 3D creati con altri ambienti, ad esempio [Part](Part_Workbench/it.md), [PartDesign](PartDesign_Workbench/it.md) o [Arch](Arch_Workbench/it.md).


</div>

<img alt="" src=images/Draft_PointArray_Example.png  style="width:400px;">


<div class="mw-translate-fuzzy">


*Oggetto duplicato in punti specifici*


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare un oggetto che si desidera distribuire.
2.  Selezionare un composto di punti.
3.  Premere il pulsante **<img src="images/Draft_PointArray.svg" width=16px> [Serie su punti](Draft_PointArray/it.md)**.


</div>

## Point compound 


<div class="mw-translate-fuzzy">

L\'oggetto composto di punti può essere creato in diversi modi.

-   Creare vari **<img src=images/Draft_Point.svg style="width:16px"> <img src=images/Part_Point.svg style="width:punti Draft](Draft_Point/it.md)** o **[16px"> <img src=images/Part_Compound.svg style="width:punti Part](Part_Point/it.md)**, e poi premere **[16px"> [Crea un composto](Part_Compound/it.md)** per creare il composto .
-   Creare i punti con il metodo precedente ma invece di creare un composto usare **<img src="images/Draft_Upgrade.svg" width=16px> [Upgrade](Draft_Upgrade/it.md)** per creare un \"Blocco\".
-   Creare uno **<img src=images/Sketcher_NewSketch.svg style="width:16px"> [Schizzo](Sketch/it.md)**, e dentro aggiungere vari punti.


</div>

## Proprietà

See also: [Property editor](property_editor.md).

A Draft PointArray object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties (with the exception of some View properties that are not inherited by Link arrays). The following properties are additional unless otherwise stated:

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
    


{{TitleProperty|Objects}}


<div class="mw-translate-fuzzy">


{{TitleProperty|Objects}}

-    **Base|Link**: l\'oggetto da duplicare; deve avere una [Part TopoShape](Part_TopoShape/it.md).

-    **Count|Integer**: (sola lettura) specifica il numero di copie nella serie. Questa proprietà è di sola lettura perché il numero di copie è determinato dal numero di punti all\'interno di **Point Object**.

-    **Extra Placement|Placement**: specifica un [posizionamento](Placement/it.md) aggiuntivo, traslazione e rotazione, che verrà applicato a ciascuna copia della serie. Ogni copia appare normalmente con la stessa rotazione dell\'oggetto **Base**; con questa proprietà è possibile fornire una rotazione aggiuntiva o contrastare la rotazione originale e apportare piccole modifiche alla posizione delle copie. <small>(v0.19)</small> 

-    **Point Object|Link**: specifica un oggetto composto di punti che indicano dove verranno visualizzate le copie dell\'oggetto **Base**. L\'oggetto composto deve avere una proprietà **Links**, **Components**, o **Geometry**, e contenere almeno un elemento con gli attributi **X**, **Y**, e **Z**.


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

Lo strumento PointArray può essere utilizzato nelle [macro](macros/it.md) e dalla [console di Python](Python/it.md) tramite la seguente funzione:


</div>


```python
point_array = make_point_array(base_object, point_object, extra=None, use_link=True)
```


<div class="mw-translate-fuzzy">

-   Crea un oggetto `"PointArray"` da un `base_object`, posizionando le copie nei punti contenuti all\'interno di `point_object`.
    -   
        `point_object`
        
        deve avere uno degli attributi `Geometry`, `Links` o `Components` contenenti punti.

    -   Invece di un riferimento a un oggetto, `base_object` e `point_object` possono anche essere delle `Labels` (stringhe) di oggetti esistenti nel documento corrente.

    -   
        `extra`
        
        può essere un `App.Placement` completo o solo un `App.Vector` o `App.Rotation`.


</div>

Esempio:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

polygon = Draft.make_polygon(3, radius=500.0)

p1 = Draft.make_point(App.Vector(1500, 0, 0))
p2 = Draft.make_point(App.Vector(2500, 0, 0))
p3 = Draft.make_point(App.Vector(2000, 1000, 0))

compound = doc.addObject("Part::Compound", "Compound")
compound.Links = [p1, p2, p3]

point_array = Draft.make_point_array(polygon, compound)
doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>


 
