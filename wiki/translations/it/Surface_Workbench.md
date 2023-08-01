# <img alt="L\'icona dell\'ambiente Surface" src=images/Workbench_Surface.svg  style="width:64px;"> Surface Workbench/it






## Introduzione

L\'[Ambiente Surface](Surface_Workbench/it.md)<img alt="" src=images/Workbench_Surface.svg  style="width:24px;"> introdotto in FreeCAD 0.17 fornisce strumenti per creare e modificare semplici [superfici NURBS](https://en.wikipedia.org/wiki/Non-uniform_rational_B-spline). Questi strumenti hanno una funzionalità simile allo strumento <img alt="" src=images/Part_Builder.svg  style="width:16px;"> [Genera una forma\...](Part_Builder/it.md) di Part quando si usa l\'opzione **Faccia dai bordi**. Tuttavia, a differenza di quello strumento, gli strumenti di Surface sono parametrici e forniscono opzioni aggiuntive. A tale riguardo, gli strumenti di questo ambiente sono simili a funzioni come <img alt="" src=images/PartDesign_AdditiveLoft.svg  style="width:16px;"> [Loft additivo](PartDesign_AdditiveLoft/it.md) e <img alt="" src=images/PartDesign_AdditivePipe.svg  style="width:16px;"> [Sweep additivo](PartDesign_AdditivePipe/it.md) di PartDesign.

Alcune delle funzioni fornite sono:

-   Creare superfici dai bordi delimitanti.
-   Allineare la curvatura alle facce vicine,
-   Vincolare le superfici a curve o vertici aggiuntivi.
-   Estendere le facce (è necessario scoprire come!)
-   Si può usare un oggetto mesh come modello per creare curve spline sulla sua superficie.

<img alt="" src=images/Surface_example.png  style="width:350px;">



## Utilizzo

L\'obiettivo dell\'ambiente Superficie è quello di creare delle facce con delle forme che non sono disponibili con gli strumenti standard degli altri ambienti. Il kernel di OCCT fornisce ad esempio una scatola rettangolare con angoli arrotondati con raggi diversi.

<img alt="" src=images/Toy_Duck.png  style="width:350px;">



*Superficie creata con schizzi posizionati in piani di riferimento con gli strumenti di [PartDesign](PartDesign_Workbench/it.md)*

Surface si integra con gli altri ambienti di FreeCAD. L\'esempio sopra è stato creato da <img alt="" src=images/Sketcher_NewSketch.svg  style="width:16px;"> [schizzi](Sketch/it.md) posizionati su <img alt="" src=images/PartDesign_Plane.svg  style="width:16px;"> [piani di riferimento](PartDesign_Plane/it.md) in <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [PartDesign](PartDesign_Workbench/it.md). Il modello può essere completamente parametrico, se tutti i piani di riferimento e gli schizzi sono definiti di conseguenza. Nella maggior parte dei casi è sufficiente disegnare uno schizzo chiuso per definire il bordo per una faccia, poi usare le opzioni per modificare ulteriormente la sua forma.

Allo stato attuale di FreeCAD (v0.17) non è possibile posizionare le superfici in un <img alt="" src=images/PartDesign_Body.svg  style="width:16px;"> [Corpo](PartDesign_Body/it.md) di PartDesign. Tuttavia le superfici generate possono essere posizionate all\'interno di una <img alt="" src=images/Std_Part.svg  style="width:16px;"> [Parte standard](Std_Part/it.md) insieme al <img alt="" src=images/PartDesign_Body.svg  style="width:16px;"> [Corpo](PartDesign_Body/it.md) che contiene tutti i piani di riferimento e gli schizzi. Dopo, si può usare lo strumento <img alt="" src=images/Part_Builder.svg  style="width:16px;"> [Crea forme](Part_Builder/it.md) di Part, che non è parametrico, per creare un [shell](Glossary#Shell.md) (guscio) e infine un [solido](Glossary#Solid.md).



## Strumenti

-   <img alt="" src=images/Surface_Filling.svg  style="width:32px;"> [Filling](Surface_Filling/it.md): riempie una serie di curve di confine con una superficie.

-   <img alt="" src=images/Surface_GeomFillSurface.svg  style="width:32px;"> [Riempi le curve del contorno](Surface_GeomFillSurface/it.md): crea una superficie da due, tre o quattro bordi limite.

-   <img alt="" src=images/Surface_Sections.svg  style="width:32px;"> [Sections](Surface_Sections/it.md): crea una superficie dai bordi che rappresentano sezioni trasversali di superficie.

-   <img alt="" src=images/Surface_ExtendFace.svg  style="width:32px;"> [Estendi faccia](Surface_ExtendFace/it.md): estrapola la superficie dai bordi con il suo parametro U locale e il parametro V.

-   <img alt="" src=images/Surface_CurveOnMesh.svg  style="width:32px;"> [Curve on mesh](Surface_CurveOnMesh.md): crea segmenti di spline approssimati sopra un oggetto [mesh](Mesh_Workbench/it.md) selezionato.

-   <img alt="" src=images/Surface_BlendCurve.svg  style="width:32px;"> [Blend Curve](Surface_BlendCurve/it.md): crea una curva di Bezier tra due bordi, con la continuità desiderata.





{{Surface Tools navi

}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Surface](Category_Surface.md) > Surface Workbench/it
