# Body/it
## Introduzione

In FreeCAD la parola \"Body\" (Corpo) viene normalmente utilizzata per fare riferimento a un oggetto [PartDesign Body](PartDesign_Body/it.md) (classe `PartDesign::Body`) definito dall\'ambiente [PartDesign](PartDesign_Workbench/it.md). Si tratta di un oggetto contenitore che può contenere degli [Schizzi 2D](Sketch/it.md) e delle [funzioni geometriche 3D](PartDesign_Feature/it.md) per creare una forma solida.

Per ulteriori informazioni su questo tipo di oggetto vedere [Corpo di PartDesign](PartDesign_Body/it.md).

## Utilizzo

1.  Passare nell\'ambiente [PartDesign](PartDesign_Workbench/it.md).
2.  Premere **[<img src=images/PartDesign_Body.svg style="width:16px"> [Crea un corpo](PartDesign_Body/it.md)**.
3.  Premere **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [Crea uno schizzo](PartDesign_NewSketch/it.md)** per creare un nuovo [schizzo](Sketch/it.md).
4.  Creare un contorno chiuso, quindi utilizzare **[<img src=images/PartDesign_Pad.svg style="width:16px"> [Pad](PartDesign_Pad/it.md)** di PartDesign per estrudere lo schizzo e creare un solido iniziale.
5.  Aggiungere altri schizzi e pad e usare altri strumenti di [PartDesign](PartDesign_Workbench/it.md) per modificare e trasformare il solido iniziale.

In alternativa, invece di usare gli [schizzi](Sketch/it.md), si possono aggiungere [funzioni primitive](PartDesign_Feature/it.md) di PartDesign, ad esempio, un **[<img src=images/PartDesign_AdditiveBox.svg style="width:16px"> [Cubo additivo](PartDesign_AdditiveBox/it.md)**. Per creare un volume finale è possibile utilizzare qualsiasi numero di funzioni additive e sottrattive.

## Note

È richiesto un Corpo quando si utilizza [PartDesign](PartDesign_Workbench/it.md) nella metodologia di [editazione delle funzioni](feature_editing/it.md).

Non è necessario un Corpo quando si utilizza [Part](Part_Workbench/it.md), poiché questo ambiente utilizza il flusso di lavoro detto [geometria solida costruttiva](constructive_solid_geometry/it.md), che si basa sulle [forme primitive](Part_Primitives/it.md) e le operazioni booleane.


{{PartDesign Tools navi

}} {{Document objects navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Glossary](Category_Glossary.md) > [PartDesign](Category_PartDesign.md) > Body/it
