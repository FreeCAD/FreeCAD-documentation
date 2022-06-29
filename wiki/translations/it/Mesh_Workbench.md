# <img alt="L\'icona dell\'ambiente Mesh" src=images/Workbench_Mesh.svg  style="width   *64px;"> Mesh Workbench/it


{{TOCright}}

## Introduzione

L\'ambiente [Mesh](Mesh_Workbench/it.md) gestisce i reticoli triangolari degli oggetti [mesh](http   *//en.wikipedia.org/wiki/Triangle_mesh). Gli oggetti mesh sono un tipo speciale di oggetti 3D, composti da facce triangolari (le maglie della griglia) connesse lungo i loro bordi e nei loro vertici. Oggetti tessellati.

Molte applicazioni 3D utilizzano i mesh come tipo principale di oggetti 3D, ad esempio   * [Sketchup](http   *//en.wikipedia.org/wiki/Sketchup), [Blender](http   *//en.wikipedia.org/wiki/Blender_(software)), [Maya](http   *//en.wikipedia.org/wiki/Maya_(software)) e [3D Studio Max](http   *//en.wikipedia.org/wiki/3d_max). Dato che i mesh sono oggetti molto semplici, contenenti solo vertici (punti), bordi e facce (triangoli), sono molto facili da creare, modificare, suddividere, allungare, e altrettanto facili da trasferire da un\'applicazione all\'altra senza alcuna perdita di informazioni. Inoltre, dal momento che contengono dati molto semplici, le applicazioni 3D ne possono gestire grandi quantità senza alcun problema. Per queste ragioni, gli oggetti mesh sono spesso il tipo di oggetto 3D utilizzato dalle applicazioni che si occupano di cinema, animazione e creazione di immagini.

Tuttavia, nel campo ingegneristico le mesh presentano una grande limitazione   * non possono definire con precisione le superfici curve. Questo è il motivo per cui FreeCAD si affida invece a [Brep](wikipedia_Boundary_representation.md). L\'ambiente Mesh offre alcuni comandi per manipolare direttamente le mesh, ma viene spesso utilizzato per importare dati di mesh 3D e convertirle in un solido da utilizzare con <img alt="" src=images/Workbench_Part.svg  style="width   *24px;"> [Part](Part_Workbench/it.md) o <img alt="" src=images/Workbench_PartDesign.svg  style="width   *24px;"> [PartDesign](PartDesign_Workbench/it.md).

<img alt="" src=images/Mesh_example.jpg  style="width   *500px;">

## Strumenti

Tutti gli strumenti dell\'ambiente Mesh sono accessibili dal menu **Meshes**. Quasi tutti sono disponibili anche in una delle barre degli strumenti Mesh.

-   <img alt="" src=images/Mesh_Import.svg  style="width   *32px;"> [Importa mesh\...](Mesh_Import/it.md)   * importa un oggetto mesh da un file.

-   <img alt="" src=images/Mesh_Export.svg  style="width   *32px;"> [Esporta mesh\...](Mesh_Export/it.md)   * esporta un oggetto mesh in un file.

-   <img alt="" src=images/Mesh_FromPartShape.svg  style="width   *32px;"> [Crea mesh da una forma\...](Mesh_FromPartShape/it.md)   * crea oggetti mesh da oggetti forma.

-   <img alt="" src=images/Mesh_RemeshGmsh.svg  style="width   *32px;"> [Affinamento\...](Mesh_RemeshGmsh/it.md)   * affina un oggetto mesh. {{Version/it|0.19}}

-   Analizza
    -   <img alt="" src=images/Mesh_Evaluation.svg  style="width   *32px;"> [Valuta e ripara la mesh\...](Mesh_Evaluation/it.md)   * analizza e ripara un oggetto mesh.
    -   <img alt="" src=images/Mesh_EvaluateFacet.svg  style="width   *32px;"> [Dettagli della faccia](Mesh_EvaluateFacet/it.md)   * fornisce informazioni sulle facce di un oggetto mesh.
    -   <img alt="" src=images/Mesh_CurvatureInfo.svg  style="width   *32px;"> [Dettagli della curvatura](Mesh_CurvatureInfo/it.md)   * mostra la curvatura assoluta di [oggetti curvati](Mesh_VertexCurvature/it.md) in punti selezionati.
    -   <img alt="" src=images/Mesh_EvaluateSolid.svg  style="width   *32px;"> [Controlla se è un solido](Mesh_EvaluateSolid/it.md)   * controlla se l\'oggetto mesh è un solido.
    -   <img alt="" src=images/Mesh_BoundingBox.svg  style="width   *32px;"> [Info limiti d\'ingombro\...](Mesh_BoundingBox/it.md)   * valuta il cuboide di delimitazione di un oggetto mesh.

-   <img alt="" src=images/Mesh_VertexCurvature.svg  style="width   *32px;"> [Grafico della curvatura](Mesh_VertexCurvature/it.md)   * Crea oggetti Curvatura mesh per oggetti mesh.

-   <img alt="" src=images/Mesh_HarmonizeNormals.svg  style="width   *32px;"> [Armonizza le normali](Mesh_HarmonizeNormals/it.md)   * armonizza le normali di un oggetto mesh.

-   <img alt="" src=images/Mesh_FlipNormals.svg  style="width   *32px;"> [Inverti le normali](Mesh_FlipNormals/it.md)   * capovolge le normali di un oggetto mesh.

-   <img alt="" src=images/Mesh_FillupHoles.svg  style="width   *32px;"> [Riempi i buchi\...](Mesh_FillupHoles/it.md)   * riempie i buchi negli oggetti mesh.

-   <img alt="" src=images/Mesh_FillInteractiveHole.svg  style="width   *32px;"> [Chiudi il buco](Mesh_FillInteractiveHole/it.md)   * riempie i fori selezionati negli oggetti mesh.

-   <img alt="" src=images/Mesh_AddFacet.svg  style="width   *32px;"> [Aggiungi triangolo](Mesh_AddFacet/it.md)   * aggiunge facce lungo un bordo di un oggetto mesh aperto.

-   <img alt="" src=images/Mesh_RemoveComponents.svg  style="width   *32px;"> [Rimuovi componente\...](Mesh_RemoveComponents/it.md)   * rimuove le facce dagli oggetti mesh.

-   <img alt="" src=images/Mesh_RemoveCompByHand.svg  style="width   *32px;"> [Rimuovi componente a mano\...](Mesh_RemoveCompByHand/it.md)   * rimuove i componenti dagli oggetti mesh.

-   <img alt="" src=images/Mesh_Segmentation.svg  style="width   *32px;"> [Crea segmenti di mesh\...](Mesh_Segmentation/it.md)   * crea segmenti di mesh separati per tipi di superfici specificate di un oggetto mesh.

-   <img alt="" src=images/Mesh_SegmentationBestFit.svg  style="width   *32px;"> [Adatta i segmenti\...](Mesh_SegmentationBestFit/it.md)   * crea segmenti di mesh separati per tipi di superficie specifiche di un oggetto mesh e può identificarne i parametri.

-   <img alt="" src=images/Mesh_Smoothing.svg  style="width   *32px;"> [Leviga\...](Mesh_Smoothing/it.md)   * leviga un oggetto mesh.

-   <img alt="" src=images/Mesh_Decimating.svg  style="width   *32px;"> [Decima\...](Mesh_Decimating/it.md)   * riduce il numero di facce negli oggetti mesh. {{Version/it|0.19}}

-   <img alt="" src=images/Mesh_Scale.svg  style="width   *32px;"> [Scala\...](Mesh_Scale/it.md)   * scala un oggetto mesh.

-   <img alt="" src=images/Mesh_BuildRegularSolid.svg  style="width   *32px;"> [Solido regolare\...](Mesh_BuildRegularSolid/it.md)   * Crea un oggetto mesh solido parametrico regolare.

-   Operazioni booleane
    -   <img alt="" src=images/Mesh_Union.svg  style="width   *32px;"> [Unione](Mesh_Union/it.md)   * crea un oggetto mesh che è l\'unione di due oggetti mesh.
    -   <img alt="" src=images/Mesh_Intersection.svg  style="width   *32px;"> [Intersezione](Mesh_Intersection/it.md)   * crea un oggetto mesh che è l\'intersezione di due oggetti mesh.
    -   <img alt="" src=images/Mesh_Difference.svg  style="width   *32px;"> [Differenza](Mesh_Difference/it.md)   * crea un oggetto mesh che è la differenza di due oggetti mesh.

-   Taglio
    -   <img alt="" src=images/Mesh_PolyCut.svg  style="width   *32px;"> [Taglia la mesh](Mesh_PolyCut/it.md)   * taglia facce intere da oggetti mesh.
    -   <img alt="" src=images/Mesh_PolyTrim.svg  style="width   *32px;"> [Rifila con un poligono](Mesh_PolyTrim/it.md)   * taglia facce e parti di facce da oggetti mesh..
    -   <img alt="" src=images/Mesh_TrimByPlane.svg  style="width   *32px;"> [Rifila con un piano](Mesh_TrimByPlane/it.md)   * taglia facce e parti di facce su un lato di un piano da un oggetto mesh.
    -   <img alt="" src=images/Mesh_SectionByPlane.svg  style="width   *32px;"> [Sezione da mesh e piano](Mesh_SectionByPlane/it.md)   * crea una sezione trasversale attraverso un oggetto mesh.
    -   <img alt="" src=images/Mesh_CrossSections.svg  style="width   *32px;"> [Sezioni\...](Mesh_CrossSections/it.md)   * crea più sezioni trasversali su oggetti mesh. {{Version/it|0.19}}

-   <img alt="" src=images/Mesh_Merge.svg  style="width   *32px;"> [Unisci](Mesh_Merge/it.md)   * crea un oggetto mesh combinando le maglie di due o più oggetti mesh.

-   <img alt="" src=images/Mesh_SplitComponents.svg  style="width   *32px;"> [Dividi in componenti](Mesh_SplitComponents/it.md)   * Divide un oggetto mesh nei suoi componenti. {{Version/it|0.19}}

-   <img alt="" src=images/MeshPart_CreateFlatMesh.svg  style="width   *32px;"> [Sviluppa una mesh](MeshPart_CreateFlatMesh/it.md)   * crea una rappresentazione piatta di un oggetto mesh. {{Version/it|0.19}}

-   <img alt="" src=images/MeshPart_CreateFlatFace.svg  style="width   *32px;"> [Sviluppa una faccia](MeshPart_CreateFlatFace/it.md)   * Crea una rappresentazione piatta di una faccia di un oggetto forma. {{Version/it|0.19}}

## Preferenze

-   Esistono alcune [preferenze di esportazione correlate ai formati mesh](Import_Export_Preferences/it#Formati_mesh.md) ma esse non vengono utilizzate dai comandi appartenenti a questo ambiente. Sono utilizzate dal comando [Esporta](Std_Export/it.md).

Le preferenze di Mesh si trovano nelle seguenti categorie dell\'[editor delle preferenze](Preferences_Editor/it.md)   *

-   <img alt="" src=images/Preferences-display.svg  style="width   *32px;"> [Visualizzazione](Preferences_Editor/it#Visualizzazione.md)   * Nella scheda [Visualizzazione mesh](Preferences_Editor/it#Visualizzazione_mesh.md) possono essere impostate diverse preferenze.
-   <img alt="" src=images/Preferences-openscad.svg  style="width   *32px;"> [OpenSCAD](OpenSCAD_Preferences/it.md)   * I comandi [Mesh Unione](Mesh_Union/it.md), [Mesh Intersezione](Mesh_Intersection/it.md) e [Mesh Differenza](Mesh_Difference/it.md) richiedono [OpenSCAD](http   *//www.openscad.org/) e usano le preferenze **OpenSCAD executable** per trovare il loro eseguibile.

## Note

-   Altri strumenti mesh sono disponibili nell\'ambiente <img alt="" src=images/Workbench_OpenSCAD.svg  style="width   *24px;"> [OpenSCAD](OpenSCAD_Workbench/it.md).
-   Vedere [Scipt Mesh](Mesh_Scripting/it.md) per manipolare e creare mesh utilizzando [Python](Python/it.md).
-   Vedere anche [Importare oggetti Mesh in FreeCAD](FreeCAD_and_Mesh_Import/it.md).
-   Vedere [Asintoto](Asymptote/it.md) per esportare le mesh nel formato Asymptote.





{{Mesh Tools navi

}} 

[Category   *Workbenches](Category_Workbenches.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Mesh](Category_Mesh.md) > Mesh Workbench/it
