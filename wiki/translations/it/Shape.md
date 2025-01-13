# Shape/it
## Introduzione

In FreeCAD la parola \"[Shape](Shape/it.md)\" (Forma) viene normalmente utilizzata per riferirsi a una [Part TopoShape](Part_TopoShape/it.md) (classe `Part::TopoShape`), un tipo di oggetto che fornisce ad un elemento la sua rappresentazione geometrica e parametrica 3D (cubo, piramide, sfera, cilindro, fusione, ecc.).

Essenzialmente tutti gli oggetti visualizzati nella [Vista 3D](3D_view/it.md) hanno un [TopoShape](Part_TopoShape/it.md), ad eccezione delle \"[Mesh](Mesh/it.md)\", che hanno un \[\[Mesh_MeshObject/it\|MeshObject\] \] (classe `Mesh::MeshObject`).

Vedere [Part TopoShape](Part_TopoShape/it.md) per ulteriori informazioni su questo tipo di oggetto.

![](images/Shape_and_mesh.svg )



*Sinistra: [forma](Shape/it.md) parametrica definita dalle proprietà. A destra: [mesh](Mesh/it.md), definita da vertici e superfici triangolari.*



## Utilizzo

Le Shape (Forme) vengono normalmente create da funzioni interne del [Ambiente Part](Part_Workbench/it.md) e sono infine definite dal kernel [OpenCASCADE Technology](OpenCASCADE/it.md) (OCCT).

Una volta creata una Forma, può essere utilizzata e modificata da tutti gli [ambienti di lavoro](Workbenches/it.md) creando [oggetti con script](scripted_objects/it.md) attorno a quella Forma.

In sostanza, ci si aspetta che ogni oggetto derivato da una [Part Feature](Part_Feature/it.md) (classe `Part::Feature`) contenga e manipoli una Forma.

Qualsiasi forma OpenCascade ha una tassellatura principalmente per visualizzare la forma sullo schermo. Maggiori informazioni a riguardo possono essere trovate in questo [post del forum](https://forum.freecad.org/viewtopic.php?t=77521&start=10#p674947) e nel [/overview/html/occt_user_guides\_\_mesh.html documentazione OpenCascad Mesh](https://dev.opencascade.org/doc).



## Note

Nell\'uso informale, una \"Forma\" può essere qualsiasi figura geometrica visibile nella [vista 3D](3D_view/it.md), e quindi il suo concetto può essere confuso con quello di \"[Corpo](Body/it.md)\" o \"[Parte](Part/it.md)\".

Tuttavia, quando è richiesta maggiore precisione, è necessario fare una distinzione.

-   Un \"[Corpo](Body/it.md)\" (Body) è un oggetto derivato da una [Part Feature](Part_Feature/it.md) (classe `Part::Feature`), creato con l\'[Ambiente PartDesign](PartDesign_Workbench/it.md) .
-   Una \"Forma\" è un oggetto interno, incorporato nel \"[Corpo](Body/it.md)\".
-   Una \"[Parte](Part/it.md)\" (Part) viene utilizzata per raggruppare diversi \"[Corpi](Body/it.md)\" per formare un [assieme](assembly/it.md). Una \"Parte\" possiede una raccolta di \"Forme\", ma non ha una propria \"Forma\".


 {{Document objects navi}}



---
⏵ [documentation index](../README.md) > [Glossary](Category_Glossary.md) > [Part](Category_Part.md) > Shape/it
