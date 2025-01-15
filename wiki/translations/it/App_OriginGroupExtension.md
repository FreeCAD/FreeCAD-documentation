# App OriginGroupExtension/it
## Introduzione

Un oggetto [App Origin](App_OriginGroupExtension/it.md), o formalmente un `App::OriginGroupExtension`, è una classe che fornisce elementi selezionabili che rappresentano i tre assi standard (X, Y, Z) e tre piani standard (XY , XZ e YZ) agli oggetti che intendono disporre diversi tipi di geometria nello spazio.

<img alt="" src=images/Std_Part.svg  style="width:16px;"> Oggetti[Parte](Std_Part/it.md) [(App Part)](App_Part/it.md) e oggetti <img alt="" src=images/PartDesign_Body.svg  style="width:16px;"> [Corpi PartDesign](PartDesign_Body/it.md) vengono creati con gli oggetti Origin per impostazione predefinita. Se necessario, gli oggetti Origin possono essere aggiunti agli oggetti <img alt="" src=images/Assembly_Assembly_Tree.svg  style="width:16px;"> [Assembly](Assembly3_CreateAssembly/it.md) del workbench <img alt="" src=images/Assembly3_workbench_icon.svg  style="width:16px;"> [Assembly3](Assembly3_Workbench/it.md), pure.

<img alt="Tree view" src=images/App_OriginGroupExtension_example.png  style="width:200px;"> <img alt="3D view" src=images/App_OriginGroupExtension-02.png  style="width:400px;"> 
*Sinistra: La [vista ad albero](Tree_view/it.md)  mostra tre oggetti che utilizzano oggetti Origin. A destra: rappresentazione degli elementi Origin nella [vista 3D](3D_view/it.md).*

Gli assi e i piani sono oggetti di tipo `App::Line` e `App::Plane` rispettivamente. Ciascuno di questi elementi può essere nascosto e visualizzato individualmente con la barra **Space**. Questo può essere utile quando si seleziona il riferimento corretto per la creazione di altri oggetti, ad es. [Schizzi](Sketch/it.md).

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Diagramma semplificato delle relazioni tra gli oggetti principali del programma. Due di essi hanno un oggetto Origin per controllare il posizionamento degli oggetti raggruppati sotto di essi.*



---
⏵ [documentation index](../README.md) > App OriginGroupExtension/it
