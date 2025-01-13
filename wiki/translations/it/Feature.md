# Feature/it
## Introduzione

In FreeCAD la parola \"[Feature](Feature/it.md)\" viene normalmente utilizzata per fare riferimento a un oggetto [Feature di PartDesign](PartDesign_Feature/it.md) (classe `PartDesign::Feature`) definito dalla classe [Ambiente di lavoro PartDesign](PartDesign_Workbench/it.md). Questa è un\'operazione o un passaggio di modellazione eseguito per creare o modificare una [Shape](Shape/it.md) solida seguendo il paradigma [feature editing](feature_editing/it.md).

Vedere [PartDesign Feature](PartDesign_Feature/it.md) per ulteriori informazioni su questo tipo di oggetto.



## Utilizzo

1.  Passare a <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/it.md).
2.  Premere **[<img src=images/PartDesign_Body.svg style="width:16px"> [Crea un corpo](PartDesign_Body/it.md)**.
3.  Premere **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [Crea uno schizzo](PartDesign_NewSketch/it.md)** per creare un nuovo [Schizzo](Sketch/it.md).
4.  Creare una figura chiusa, quindi utilizzare **[<img src=images/PartDesign_Pad.svg style="width:16px"> [Estrusione](PartDesign_Pad/it.md)** per estrudere lo schizzo e creare un solido iniziale. Questo solido iniziale è la Feature iniziale.
5.  Aggiungere altri schizzi e pad e utilizzare gli altri strumenti di [PartDesign](PartDesign_Workbench/it.md) per modificare e trasformare il solido iniziale. Ciascuno di questi passaggi corrisponde alle Feature del [Corpo](Body/it.md).
6.  In alternativa, aggiungere oggetti primitivi, come **[<img src=images/PartDesign_AdditiveBox.svg style="width:16px"> [Cubo additivo](PartDesign_AdditiveBox/it.md)** e **[<img src=images/PartDesign_SubtractiveCylinder.svg style="width:16px"> [Cilindro sottrattivo](PartDesign_SubtractiveCylinder/it.md)**. Tutti i passaggi additivi e sottrattivi inseriscono feature utilizzate per creare un volume finale.



## Note

In senso generale, una \"Feature\" può essere un qualsiasi passaggio di modellazione utilizzato per creare una [Shape](Shape/it.md) finale, con qualsiasi strumento di ogni [Ambiente di lavoro](Workbenches/it.md).

-   Ad esempio, in [Ambiente Part](Part_Workbench/it.md), nel flusso di lavoro della [geometria solida costruttiva](constructive_solid_geometry/it.md), una \"Feature\" potrebbe essere una qualsiasi operazione booleana, come **[<img src=images/_Part_Fuse.svg style="width:16px"> [Unione](Part_Fuse/it.md)**, **[<img src=images/Part_Cut.svg style="width:16px"> [Taglio](Part_Cut/it.md)** o **[<img src=images/Part_Common.svg style="width:16px"> [Intersezione](Part_Common/it.md)**.

In un senso più specifico, una \"Feature\" è un passaggio di modellazione utilizzato all\'interno di un [Corpo](PartDesign_Body/it.md).

-   Ad esempio, **[<img src=images/PartDesign_AdditiveCylinder.svg style="width:16px"> [Cilindro additivo](PartDesign_AdditiveCylinder/it.md)**, **[<img src=images/PartDesign_AdditiveLoft.svg style="width:16px"> [Loft additivo](PartDesign_AdditiveLoft/it.md)**, **[<img src=images/PartDesign_Pocket.svg style="width:16px"> [Tasca](PartDesign_Pocket/it.md)**, **[<img src=images/PartDesign_SubtractiveCone.svg style="width:16px"> [Cono sottrattivo](PartDesign_SubtractiveCone/it.md)**, ecc., sono tutte \"Feature\".


{{PartDesign Tools navi

}}  {{Document objects navi}}



---
⏵ [documentation index](../README.md) > [Glossary](Category_Glossary.md) > [PartDesign](Category_PartDesign.md) > [Part](Category_Part.md) > Feature/it
