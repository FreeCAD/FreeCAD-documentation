# Surface Workbench/it
<div class="mw-translate-fuzzy">





</div>

<img alt="L\'icona dell\'ambiente Surface" src=images/Workbench_Surface.svg  style="width:128px;">


{{TOCright}}

## Introduzione

L\'ambiente <img alt="" src=images/Workbench_Surface.svg  style="width:24px;"> _ di Part quando si usa l\'opzione **Faccia dai bordi**. Tuttavia, a differenza di quello strumento, gli strumenti di Surface sono parametrici e forniscono opzioni aggiuntive. A tale riguardo, gli strumenti di questo ambiente sono simili a funzioni come <img alt="" src=images/PartDesign_AdditiveLoft.svg  style="width:16px;"> _ di PartDesign.

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

Surface si integra con gli altri ambienti di FreeCAD. L\'esempio sopra è stato creato da <img alt="" src=images/Sketcher_NewSketch.svg  style="width:16px;"> _ in <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [PartDesign](PartDesign_Workbench/it.md). Il modello può essere completamente parametrico, se tutti i piani di riferimento e gli schizzi sono definiti di conseguenza. Nella maggior parte dei casi è sufficiente disegnare uno schizzo chiuso per definire il bordo per una faccia, poi usare le opzioni per modificare ulteriormente la sua forma.

Allo stato attuale di FreeCAD (v0.17) non è possibile posizionare le superfici in un <img alt="" src=images/PartDesign_Body.svg  style="width:16px;"> _ insieme al <img alt="" src=images/PartDesign_Body.svg  style="width:16px;"> _ di Part, che non è parametrico, per creare un [shell](Glossary#Shell.md) (guscio) e infine un [solido](Glossary#Solid.md).

## Strumenti

-   <img alt="" src=images/Surface_Filling.svg  style="width:32px;"> [Filling](Surface_Filling/it.md): riempie una serie di curve di confine con una superficie. La superficie può essere modificata aggiungendo curve e vertici di vincoli. La superficie cambia forma in modo da passare attraverso gli elementi di vincolo aggiunti.
-   <img alt="" src=images/Surface_GeomFillSurface.svg  style="width:32px;"> [Fill boundary curves](Surface_GeomFillSurface/it.md): crea una superficie da due, tre o quattro bordi limite. Sono disponibili tre diverse modalità di riempimento: Stretch, Coons, Curved.

-   <img alt="" src=images/Surface_GeomFillSurface.svg  style="width:32px;"> [Fill boundary curves](Surface_GeomFillSurface.md): creates a surface from two, three or four boundary edges.

-   <img alt="" src=images/Surface_Sections.svg  style="width:32px;"> [Sections](Surface_Sections/it.md): crea una superficie dai bordi che rappresentano sezioni trasversali di superficie. {{Version/it|0.19}}
-   <img alt="" src=images/Surface_ExtendFace.svg  style="width:32px;"> [Extend face](Surface_ExtendFace/it.md): estrapola la superficie dai bordi con i sui parametri U e V locali.
-   <img alt="" src=images/Surface_CurveOnMesh.svg  style="width:32px;"> _ selezionato. Se l\'oggetto non è un _.

-   <img alt="" src=images/Surface_ExtendFace.svg  style="width:32px;"> [Extend face](Surface_ExtendFace.md): extrapolates the surface at the boundaries with its local U parameter and V parameter.

-   <img alt="" src=images/Surface_CurveOnMesh.svg  style="width:32px;"> _.


<div class="mw-translate-fuzzy">





</div>


{{Surface Tools navi

}} 

_

---
[documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Surface Workbench/it
