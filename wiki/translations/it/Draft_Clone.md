---
- GuiCommand:/it
   Name:Draft Clone
   Name/it:Clona
   Workbenches:[Draft](Draft_Workbench/it.md), [Architettura](Arch_Workbench/it.md)
   MenuLocation:Draft → Clona
   Shortcut:**C** **L**
   SeeAlso:[Sposta](Draft_Move/it.md), [Scala](Draft_Scale/it.md)
---

# Draft Clone/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento **<img src="images/Draft_Clone.svg" width=16px> Clona** produce delle copie collegate di una forma selezionata. Ciò significa che se l\'oggetto originale cambia forma e proprietà, cambiano anche tutti i cloni. Ciononostante, ogni clone mantiene la sua posizione, rotazione e scala uniche, così come le sue proprietà di visualizzazione come il colore della forma, la larghezza della linea e la trasparenza.


</div>


<div class="mw-translate-fuzzy">

Questo strumento può essere utilizzato su forme 2D create con [Draft](Draft_Workbench/it.md) ma può anche essere utilizzato su molti tipi di oggetti 3D come quelli creati con [Part](Part_Workbench/it.md) o [PartDesign](PartDesign_Workbench/it.md) o [Arch](Arch_Workbench/it.md).


</div>

<img alt="" src=images/Draft_Clone_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">



*Clone accanto all'oggetto originale*


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare un oggetto che si desidera clonare
2.  Premere il pulsante **<img src="images/Draft_Clone.svg" width=16px> [Clona](Draft_Clone/it.md)
**


</div>

## Properties

See also: [Property editor](property_editor.md).

An object created with the Draft Clone command is derived from a [Part Part2DObject](Part_Part2DObject.md), a [Part Feature](Part_Feature.md) object or, if an Arch Clone is created, from the object type of the source object. It inherits all properties from that object. A clone derived from one of the first two objects also has the following additional properties:

### Data


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

## Proprietà

-    {{PropertyData/it|Objects}}: specifica una lista di oggetti base che vengono clonati.

-    {{PropertyData/it|Scale}}: specifica il fattore di scala per il clone, in ciascuna direzione X, Y e Z.

-    {{PropertyData/it|Fuse}}: se è `True` e {{PropertyData/it|Objects}} include molte forme che si intersecano l\'una con l\'altra, il clone risultante le fonde insieme in una singola forma, o crea un composto. {{Version/it|0.17}}


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Vedere anche:**

[Draft API](Draft_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Clone può essere usato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) utilizzando la seguente funzione:


</div>


```python
cloned_object = make_clone(obj, delta=None, forcedraft=False)
```


<div class="mw-translate-fuzzy">

-   Crea un oggetto `cloned_object` da un dato `obj`, che può essere un singolo oggetto o un elenco di oggetti.
-   Se dato, `delta` è un `FreeCAD.Vector` che sposta il nuovo clone dalla posizione originale dell\'oggetto base.
-   Se `forcedraft` è `True`, l\'oggetto risultante sarà un clone di Draft, e non un clone di Arch, anche se `obj` è un oggetto [Arch](Arch_Workbench/it.md).


</div>

Esempio:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

place = App.Placement(App.Vector(1000, 0, 0), App.Rotation())
polygon1 = Draft.make_polygon(3, 750)
polygon2 = Draft.make_polygon(5, 750, placement=place)

vector = App.Vector(2600, 500, 0)
cloned_object = Draft.clone([polygon1, polygon2], delta=vector)

cloned_object.Fuse = True

doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Clone/it
