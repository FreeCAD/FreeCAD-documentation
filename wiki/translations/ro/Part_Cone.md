---
- GuiCommand:
   Name: Part Cone
   Name/ro: Part Cone
   MenuLocation: Part -> Cone
|
   Workbenches: [Part](Part_Workbench/ro.md), Complete
   SeeAlso: [Part CreatePrimitives](Part_CreatePrimitives/ro.md)
---

# Part Cone/ro


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Un con parametric trunchiat este un element tip primitivă geometrică disponibil pe bara de instrumente Part sau în meniu (submeniul primitives) se deschide o casetă de dialog Create Primitives .


</div>

The default Part Cone is truncated. It can be turned into a full, untruncated, cone by changing its **Radius1** or **Radius2** property to zero. It can be turned into a segment of a cone by changing its **Angle** property.

<img alt="" src=images/Part_Cone_Example.png  style="width:400px;">

## Usage


<div class="mw-translate-fuzzy">

## Cum se folosește 

În atelierul Part click pe iconița <img alt="" src=images/Part_Cone.png  style="width:32px;">.


</div>

## Example

![Part Cone from the scripting example](images/Part_Cone_Scripting_Example.png )

A Part Cone object created with the [scripting example](#Scripting.md) below is shown here.

## Notes

-   A Part Cone can also be created with the <img alt="" src=images/Part_Primitives.svg  style="width:16px;"> [Part Primitives](Part_Primitives.md) command. With that command you can specify the dimensions and placement at creation time.


<div class="mw-translate-fuzzy">

### Primitive Geometriche 

+++
| ![](images/PartConePrimitivesOptions_it.png ) | Cono                                                                                                                                               |
|                                                                          |                                                                                                                                                    |
|                                                                          | #### Parametri                                                                                                                                     |
|                                                                          |                                                                                                                                                    |
|                                                                          | -   raggio 1,                                                                                                                                      |
|                                                                          | -   raggio 2,                                                                                                                                      |
|                                                                          | -   altezza,                                                                                                                                       |
|                                                                          | -   angolo                                                                                                                                         |
|                                                                          |                                                                                                                                                    |
|                                                                          | #### Posizione                                                                                                                                     |
|                                                                          |                                                                                                                                                    |
|                                                                          | Espandere la voce Posizione per stabilire:                                                                                                         |
|                                                                          |                                                                                                                                                    |
|                                                                          | -   punto di posizionamento nella vista 3D,                                                                                                        |
|                                                                          | -   direzione dell\'asse del cono, x, y, z o definita dall\'utente.                                                                                |
|                                                                          |                                                                                                                                                    |
|                                                                          | Anche le dimensioni e il posizionamento del cono prodotto utilizzando le opzioni di creazione sono modificabili tramite la scheda delle proprietà. |
+++

## Opțiuni

+++
| ![](images/PartConeProperty_en.png ) |                                                                                                                                                                                                                                                                                                                                                  |
|                                                        | **Cone**                                                                                                                                                                                                                                                                                                                                                    |
|                                                        |                                                                                                                                                                                                                                                                                                                                                              |
|                                                        | -   Radius 1 - raza cercului sau arcului de cer definit de fațeta inferioară                                                                                                                                                                                                                                                                                    |
|                                                        | -   Radius 2 - raza cercului sau arcului de cerc definită de fațeta suprioară                                                                                                                                                                                                                                                                                   |
|                                                        | -   Height - înălțimea Part Cone                                                                                                                                                                                                                                                                                                                                |
|                                                        | -   Angle - numărul de grade ale arcului sau cercurilor care definesc fațeta superioară și pe cea inferioară ale conului trunchiat. Implicit 360 crează fațete circulare, o valoare mai mică va crea o porțiune a unui con, așa cum este definită de fețele superioare și inferioare, fiecare cu marginile definite de un arc cu numărul de grade și două raze. |
+++


</div>

See also: [Property editor](Property_editor.md).

A Part Cone object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Attachment}}

The object has the same attachment properties as a [Part Part2DObject](Part_Part2DObject#Data.md).


{{TitleProperty|Cone}}

-    **Radius1|Length**: The radius of the bottom face of the cone. Can be {{Value|0mm}} if **Radius2** is larger than {{Value|0mm}}. The default is {{Value|2mm}}.

-    **Radius2|Length**: The radius of the top face of the cone. Can be {{Value|0mm}} if **Radius1** is larger than {{Value|0mm}}. The default is {{Value|4mm}}.

-    **Height|Length**: The height of the cone. The default is {{Value|10mm}}.

-    **Angle|Angle**: The angle of the circular arc that defines the top and bottom face of the cone. Valid range: {{Value|0° &lt; value &lt;&#61; 360°}}. The default is {{Value|360°}}. If it is smaller than {{Value|360°}} the resulting solid will be a segment of a cone.

## Scripting

See also: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/), [Part scripting](Part_scripting.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

A Part Cone can be created with the {{Incode|addObject()}} method of the document:


```python
cone = FreeCAD.ActiveDocument.addObject("Part::Cone", "myCone")
```

-   Where {{Incode|"myCone"}} is the name for the object.
-   The function returns the newly created object.

Example:


```python
import FreeCAD as App

doc = App.activeDocument()

cone = doc.addObject("Part::Cone", "myCone")
cone.Radius1 = 5
cone.Radius2 = 10
cone.Height = 50
cone.Angle = 270
cone.Placement = App.Placement(App.Vector(1, 2, 3), App.Rotation(30, 60, 15))

doc.recompute()
```





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Cone/ro
