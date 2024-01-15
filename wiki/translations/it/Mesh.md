# Mesh/it
## Introduzione

In FreeCAD la parola \"[Mesh](Mesh/it.md)\" viene normalmente utilizzata per riferirsi a un [Mesh MeshObject](Mesh_MeshObject/it.md) (classe `Mesh::MeshObject`), un tipo di oggetto che definisce dati 3D ma non è un solido \"[Shape](Shape/it.md)\".

Le mesh sono oggetti molto semplici, contenenti solo vertici (punti), bordi e facce triangolari. In generale, sono facili da creare, modificare, suddividere ed estendere e possono essere passati da un\'applicazione all\'altra senza alcuna perdita di dettagli. Inoltre, poiché le mesh contengono dati molto semplici, le applicazioni 3D come i software di animazione e i videogiochi possono gestirne quantità molto grandi (milioni di triangoli) senza utilizzare molte risorse di calcolo.

Tuttavia, nel campo dell\'ingegneria le mesh presentano una grande limitazione: sono costituite solo da superfici e non hanno informazioni sulla \"massa\", quindi non si comportano come \"solidi\". Ciò significa che le operazioni basate sui solidi, come [addizione o sottrazione booleana](Part_Boolean/it.md), sono difficili da eseguire sulle mesh. Inoltre, poiché sono definite da singoli punti, sono difficili da descrivere in modo parametrico.

Vedere [Mesh MeshObject](Mesh_MeshObject/it.md) per ulteriori informazioni su questo tipo di oggetto e vedere [Mesh poligonale](https://en.wikipedia.org/wiki/Polygon_mesh) per informazioni generiche sui sistemi informatici.

![](images/Shape_and_mesh.svg )



*Sinistra: [forma](Shape/it.md) parametrica definita dalle proprietà. A destra: [mesh](Mesh/it.md), definita da vertici e superfici triangolari.*



## Utilizzo

Le mesh vengono normalmente create mediante funzioni interne dell\'[Ambiente Mesh](Mesh_Workbench/it.md) o importando file in formato mesh, come STL e OBJ.

In sostanza, ci si aspetta che ogni oggetto derivato da una [Mesh Feature](Mesh_Feature/it.md) (classe `Mesh::Feature`) contenga e manipoli una Mesh.

Poiché FreeCAD è progettato principalmente per essere un modellatore di solidi, è più adatto a gestire [Forme](Shape/it.md) solide. Può importare e visualizzare mesh nella [vista 3D](3D_view/it.md) e l\'[Ambiente Mesh](Mesh_Workbench/it.md) offre alcuni comandi per manipolarle direttamente. Ma in molti casi la Mesh deve prima essere convertita in una [Forma](Shape/it.md) (vedere [Part ShapeFromMesh](Part_ShapeFromMesh/it.md)), oppure la geometria deve essere ricreata utilizzando tecniche di modellazione solida dall\'[Ambiente Part](Part_Workbench/it.md) o dall\'[Ambiente PartDesign](PartDesign_Workbench/it.md).



## Mesh Elementi Finiti 

In FreeCAD la parola \"[Mesh](Mesh/it.md)\" può anche riferirsi a un oggetto specifico che verrà utilizzato nell\'analisi degli elementi finiti (FEA).

Quando un oggetto con una [Forma](Shape/it.md) solida viene utilizzato nell\'[Ambiente FEM](FEM_Workbench/it.md) verrà discretizzato in una mesh triangolare. In questo caso, l\'oggetto risultante è una classe [FEM FemMeshObject](FEM_Mesh/it.md) (`Fem::FemMeshObject`) e non è derivata da una [Mesh Feature](Mesh_Feature/it.md) (` Mesh::Feature`).

Per ulteriori informazioni vedere [Ambiente FEM ](FEM_Workbench/it.md) e [FEM Mesh](FEM_Mesh/it.md).



## Ulteriori informazioni 

-   [Polygonal (mesh) geometry](https://forum.freecadweb.org/viewtopic.php?f=8&t=47493)


{{Mesh Tools navi

}} {{FEM Tools navi}} {{Document objects navi}}



---
⏵ [documentation index](../README.md) > [Glossary](Category_Glossary.md) > [Mesh](Category_Mesh.md) > [FEM](Category_FEM.md) > Mesh/it
