# PartDesign Feature/it
## Introduzione

Per [PartDesign Feature](PartDesign_Feature/it.md) (funzione di PartDesign) si intende a un \"passaggio\" nel processo di modellazione che si verifica all\'interno di un [Corpo di PartDesign](PartDesign_Body/it.md). Ad esempio, ogni volta che si aggiunge un cubo solido con [Cubo additivo](PartDesign_AdditiveBox/it.md), si aggiunge una funzione; quando si aggiunge uno smusso a un bordo con [Smusso di PartDesign](PartDesign_Chamfer/it.md), si aggiunge un\'altra funzione; quando si intaglia un foro usando uno [schizzo](Sketch/it.md) per creare una [Tasca](PartDesign_Pocket/it.md), si aggiunge un\'altra funzione.

<img alt="" src=images/PartDesign_Feature_example.png  style="width:600px;"> 
*Editazione delle funzioni in un Corpo di PartDesign con tre funzioni sequenziali.*

Esistono molti tipi di funzioni che possono aggiungere o rimuovere del volume da un solido iniziale. La parola \"funzione\" si riferisce all\'operazione stessa e anche al solido risultante dopo tale operazione.

Per ulteriori informazioni sulla creazione di oggetti solidi con [PartDesign](PartDesign_Workbench/it.md) vedere [editazione delle funzioni](feature_editing/it.md).



## Utilizzo

Quasi tutti gli strumenti di PartDesign hanno lo scopo di aggiungere funzioni a un Corpo. È possibile accedere a questi strumenti dal menu e dai pulsanti della barra degli strumenti mentre è selezionato un oggetto o un sottoelemento (vertice, bordo, faccia).

Le funzioni possono essere inserite in diverse categorie:

-   Funzione base: si riferisce all\'oggetto Funzione Base che può essere creato in un [Corpo di Part Design](PartDesign_Body/it.md).
-   Additive e sottrattive
    -   Forme primitive additive: [Cubo](PartDesign_AdditiveBox/it.md), [Cono](PartDesign_AdditiveCone/it.md), [Cilindro](PartDesign_AdditiveCylinder/it.md), [Elissoide](PartDesign_AdditiveEllipsoid/it.md), [Prisma](PartDesign_AdditivePrism/it.md), [Sfera](PartDesign_AdditiveSphere/it.md), [Toro](PartDesign_AdditiveTorus/it.md), e [Cuneo](PartDesign_AdditiveWedge/it.md).
    -   Forme primitive sottrattive: [Cubo sottrattivo](PartDesign_SubtractiveBox/it.md), [Cono sottrattivo](PartDesign_SubtractiveCone/it.md), [Cilindro sottrattivo](PartDesign_SubtractiveCylinder/it.md), [Elissoide sottrattivo](PartDesign_SubtractiveEllipsoid/it.md), [Prisma sottrattivo](PartDesign_SubtractivePrism/it.md) [Sfera sottrattiva](PartDesign_SubtractiveSphere/it.md), [Toro sottrattivo](PartDesign_SubtractiveTorus/it.md), e [Cuneo sottrattivo](PartDesign_SubtractiveWedge/it.md).
    -   Additive basate sul profilo: [Estrusione](PartDesign_Pad/it.md), [Rivoluzione](PartDesign_Revolution/it.md), [Loft](PartDesign_AdditiveLoft/it.md), [Sweep](PartDesign_AdditivePipe/it.md).
    -   Sottrattive basate sul profilo: [Tasca](PartDesign_Pocket/it.md), [Foro](PartDesign_Hole/it.md), [Gola](PartDesign_Groove/it.md), [Loft sottrattivo](PartDesign_SubtractiveLoft/it.md), [Sweep sottrattivo](PartDesign_SubtractivePipe/it.md).
-   [Booleane](PartDesign_Boolean/it.md), compreso fusione, taglio e intersezione.
-   Spoglia
    -   [Smusso](PartDesign_Chamfer/it.md)
    -   [Sformo](PartDesign_Draft/it.md)
    -   [Raccordo](PartDesign_Fillet/it.md)
    -   [Spessore](PartDesign_Thickness/it.md)
-   Trasformazione
    -   [Serie rettangolare](PartDesign_LinearPattern/it.md)
    -   [Specchiato](PartDesign_Mirrored/it.md)
    -   [Multi-trasformazione](PartDesign_MultiTransform/it.md)
    -   [Serie Polare](PartDesign_PolarPattern/it.md)
    -   [Scala](PartDesign_Scaled/it.md)



## Eredità

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Diagramma semplificato delle relazioni tra gli oggetti principali del programma. Gli oggetti `PartDesign::Feature* sono usati per costruire solidi 3D parametrici e quindi sono derivati dall'oggetto base {{incode|Part::Feature`.}}



## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md), e [script di oggetti](scripted_objects/it.md).

Vedere [Part Feature](Part_Feature/it.md) per le informazioni generali su come aggiugere oggetti tramite la [console Python](Python_console/it.md).

Vedere [Corpo di PartDesign](PartDesign_Body/it.md) per le informazioni generali su come aggiungere un Corpo. Quando esiste un Corpo, le funzioni possono essere collegate ad esso usando il metodo `addObject()` del Corpo.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject('PartDesign::Body', 'Body')
obj.Label = "Custom label"

feature = App.ActiveDocument.addObject('PartDesign::AdditiveBox', 'Box')
feature.Width = 200
feature.Length = 300
feature.Height = 500
obj.addObject(feature)
App.ActiveDocument.recompute()

feature2 = App.ActiveDocument.addObject('PartDesign::SubtractiveBox', 'Box')
feature2.Width = 50
feature2.Length = 200
feature2.Height = 400
obj.addObject(feature2)
App.ActiveDocument.recompute()
```


{{PartDesign Tools navi

}} {{Document objects navi}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Feature/it
