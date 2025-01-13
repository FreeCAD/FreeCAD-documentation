---
 GuiCommand:
   Name: Part RefineShape
   MenuLocation: Part , Create a copy , Refine Shape
   Workbenches: Part_Workbench
   SeeAlso: Part_SimpleCopy, Part_TransformedCopy, Part_ElementCopy, OpenSCAD_RefineShapeFeature
---

# Part RefineShape/ro


</div>




<div class="mw-translate-fuzzy">

## Descriere

Curata liniile inutile. După o operație booleană, unele linii care definesc forma anterioară rămân vizibile, această unealtă creează o copie total curățată a originalului.


</div>

The <img alt="" src=images/Part_RefineShape.svg  style="width:24px;"> **Part RefineShape** command creates parametric copies with a refined shape from selected objects. It removes unnecessary edges from planar and cylindrical faces.

![](images/PartRefineShape_it.png )


<div class="mw-translate-fuzzy">

![](images/PartRefineShape_it.png )


</div>




<div class="mw-translate-fuzzy">

## Utilizare

1.  Selectați forma de curățat.
2.  Click pe meniul **Part → Refine shape** .

-   O copie a obiectului este creată și complet curățată, obiectul original este randat.
-   Copia nou creată este independentă de original.


</div>

1.  Select one or more objects.
2.  Select the **Part → Create a copy → <img src="images/Part_RefineShape.svg" width=16px> Refine shape** option from the menu.
3.  For each object a cleaned, parametric copy is created
4.  The original objects are hidden.




<div class="mw-translate-fuzzy">

## Note

-   funcția nu modifică forma existentă, dar returnează o nouă formă
-   funcția este folosită în mod normal ca ultim pas în istoricul de modelare
-   funcția poate ajuta la obținerea rotunjirilor dificile pentru de lucrat
-   funcția este destinată să împiedice imprimantele 3D să printeze marginile nedorite
-   funcția poate fi utilizată după transformarea unei rețele în formă pentru a curăța marginile reziduale pe fațetele plane.


</div>

-   This command can be used as the last step in a traditional [constructive solid geometry](constructive_solid_geometry.md) workflow.
-   It may help to clean up the model before applying other features, such as [fillets](Part_Fillet.md).
-   Cleaning up an object may prevent 3D printers from printing unwanted edges once the object is exported to a mesh format.
-   This command can also be used after converting a mesh to a shape ([Part ShapeFromMesh](Part_ShapeFromMesh.md)).
-   By default this command creates parametric (linked) copies. There is [fine-tuning](Fine-tuning.md) parameter to change this to non-parametric copies. More information about parametric/non-parametric copy behavior can be found in this [forum post](https://forum.freecad.org/viewtopic.php?t=42993).
-   Some interesting information about what is happening with placement and how to access by Python can be found in this [forum post](https://forum.freecad.org/viewtopic.php?t=77568#p675456).

## Properties

See also: [Property editor](Property_editor.md).

A Part RefineShape object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional property:

### Data


{{TitleProperty|Refine}}

-    **Source|Link**: specifies the linked source shape.




<div class="mw-translate-fuzzy">

## Script

Comanda Python pentru rafinarea formei este următoarea:


</div>

The Python command for refining a shape is the following:


```python
shape.removeSplitter()
```





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part RefineShape/ro
