# PartDesign Feature/it
## Introduzione

Per [PartDesign Feature](PartDesign_Feature/it.md) (funzione di PartDesign) si intende a un \"passaggio\" nel processo di modellazione che si verifica all\'interno di un [Corpo di PartDesign](PartDesign_Body/it.md). Ad esempio, ogni volta che si aggiunge un cubo solido con [Cubo additivo](PartDesign_AdditiveBox/it.md), si aggiunge una funzione; quando si aggiunge uno smusso a un bordo con [Smusso di PartDesign](PartDesign_Chamfer/it.md), si aggiunge un\'altra funzione; quando si intaglia un foro usando uno [schizzo](Sketch/it.md) per creare una [Tasca](PartDesign_Pocket/it.md), si aggiunge un\'altra funzione.

<img alt="" src=images/PartDesign_Feature_example.png  style="width   *600px;"> 
*Editazione delle funzioni in un Corpo di PartDesign con tre funzioni sequenziali.*

Esistono molti tipi di funzioni che possono aggiungere o rimuovere del volume da un solido iniziale. La parola \"funzione\" si riferisce all\'operazione stessa e anche al solido risultante dopo tale operazione.

Per ulteriori informazioni sulla creazione di oggetti solidi con [PartDesign](PartDesign_Workbench/it.md) vedere [editazione delle funzioni](feature_editing/it.md).

## Utilizzo

Quasi tutti gli strumenti di PartDesign hanno lo scopo di aggiungere funzioni a un Corpo. È possibile accedere a questi strumenti dal menu e dai pulsanti della barra degli strumenti mentre è selezionato un oggetto o un sottoelemento (vertice, bordo, faccia).

The features can be placed in different categories   *

-   Feature base   * refers to the Base Feature object that can be created in a [PartDesign Body](PartDesign_Body.md).
-   Additive and subtractive
    -   Primitive shapes   * [Box](PartDesign_AdditiveBox.md), [Cone](PartDesign_AdditiveCone.md), [Cylinder](PartDesign_AdditiveCylinder.md), [Ellipsoid](PartDesign_AdditiveEllipsoid.md), [Prism](PartDesign_AdditivePrism.md), [Sphere](PartDesign_AdditiveSphere.md), [Torus](PartDesign_AdditiveTorus.md), and [Wedge](PartDesign_AdditiveWedge.md).
    -   Primitive shapes subtractive   * [Subtractive Box](PartDesign_SubtractiveBox.md), [Subtractive Cone](PartDesign_SubtractiveCone.md), [Subtractive Cylinder](PartDesign_SubtractiveCylinder.md), [Subtractive Ellipsoid](PartDesign_SubtractiveEllipsoid.md), [Subtractive Prism](PartDesign_SubtractivePrism.md), [Subtractive Sphere](PartDesign_SubtractiveSphere.md), [Subtractive Torus](PartDesign_SubtractiveTorus.md), and [Subtractive Wedge](PartDesign_SubtractiveWedge.md).
    -   Profile based   * [Pad](PartDesign_Pad.md), [Revolution](PartDesign_Revolution.md), [Loft](PartDesign_AdditiveLoft.md), [Pipe](PartDesign_AdditivePipe.md).
    -   Profile based subtractive   * [Pocket](PartDesign_Pocket.md), [Hole](PartDesign_Hole.md), [Groove](PartDesign_Groove.md), [Subtractive Loft](PartDesign_SubtractiveLoft.md), [Subtractive Pipe](PartDesign_SubtractivePipe.md).
-   [Boolean](PartDesign_Boolean.md), including fuse, cut, and common.
-   Dress up
    -   [Chamfer](PartDesign_Chamfer.md)
    -   [Draft](PartDesign_Draft.md)
    -   [Fillet](PartDesign_Fillet.md)
    -   [Thickness](PartDesign_Thickness.md)
-   Transform
    -   [Linear pattern](PartDesign_LinearPattern.md)
    -   [Mirrored](PartDesign_Mirrored.md)
    -   [Multi-transformed](PartDesign_MultiTransform.md)
    -   [Polar pattern](PartDesign_PolarPattern.md)
    -   [Scaled](PartDesign_Scaled.md)

## Eredità

<img alt="" src=images/FreeCAD_core_objects.svg  style="width   *800px;">



*Diagramma semplificato delle relazioni tra gli oggetti principali del programma. Gli oggetti `PartDesign   *   *Feature* sono usati per costruire solidi 3D parametrici e quindi sono derivati dall'oggetto base {{incode|Part   *   *Feature`.}}

## Script


**Vedere anche   ***

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md), e [script di oggetti](scripted_objects/it.md).

Vedere [Part Feature](Part_Feature/it.md) per le informazioni generali su come aggiugere oggetti tramite la [console Python](Python_console/it.md).

Vedere [Corpo di PartDesign](PartDesign_Body/it.md) per le informazioni generali su come aggiungere un Corpo. Quando esiste un Corpo, le funzioni possono essere collegate ad esso usando il metodo `addObject()` del Corpo.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject('PartDesign   *   *Body', 'Body')
obj.Label = "Custom label"

feature = App.ActiveDocument.addObject('PartDesign   *   *AdditiveBox', 'Box')
feature.Width = 200
feature.Length = 300
feature.Height = 500
obj.addObject(feature)
App.ActiveDocument.recompute()

feature2 = App.ActiveDocument.addObject('PartDesign   *   *SubtractiveBox', 'Box')
feature2.Width = 50
feature2.Length = 200
feature2.Height = 400
obj.addObject(feature2)
App.ActiveDocument.recompute()
```


{{PartDesign Tools navi

}} {{Document objects navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Feature/it
