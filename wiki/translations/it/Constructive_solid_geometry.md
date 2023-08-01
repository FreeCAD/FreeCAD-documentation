# Constructive solid geometry/it
{{TOCright}}

## Introduzione

[Geometria solida costruttiva](https://en.wikipedia.org/wiki/Constructive_solid_geometry) (**CSG**) è un paradigma di modellazione che viene utilizzato in molti sistemi CAD tradizionali. Essenzialmente consiste nell\'usare oggetti solidi primitivi e fare operazioni booleane con essi, come fusione, sottrazione e intersezione, al fine di creare una forma finale.

In FreeCAD, questo metodo è per lo più utilizzato con l\'ambiente <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench/it.md), che ha la capacità di creare oggetti primitivi come <img alt="" src=images/Part_Box.svg  style="width:24px;"> [parallelepipedi](Part_Box/it.md), <img alt="" src=images/Part_Cylinder.svg  style="width:24px;"> [cilindri](Part_Cylinder/it.md), e <img alt="" src=images/Part_Sphere.svg  style="width:24px;"> [sfere](Part_Sphere/it.md) e di fonderli insieme, oppure di usarli per tagliare altri oggetti con strumenti come **<img src="images/Part_Cut.svg" width=24px> [Taglio](Part_Cut/it.md)**.

<img alt="" src=images/Part_Constructive_Solid_Geometry_workflow.svg  style="width:800px;">



*Flusso di lavoro della geometria solida costruttiva (CSG); sulle primitive solide può essere fatto qualsiasi numero di operazioni per creare altri oggetti solidi e quindi fonderli o tagliarli fino a produrre la forma finale.*

In alternativa <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/it.md) utilizza un approccio più moderno rispetto al semplice CSG; questo metodo è chiamato [Editazione delle funzioni](feature_editing/it.md), che significa creare un solido di base e quindi aggiungere trasformazioni parametriche sequenziali per ottenere un corpo finale.


**Note:**

Anche un [Corpo](PartDesign_Body/it.md) creato con l\'ambiente [PartDesign](PartDesign_Workbench/it.md) può essere usato in un\'operazione booleana con altri oggetti.

## Esempio

<img alt="" src=images/Part_CGS_workflow_example.svg  style="width:600px;">



*Esempio di flusso di lavoro di geometria solida costruttiva (CSG): due parti primitive vengono fuse (union); viene calcolata l'intersezione di altre due parti primitive (common); infine si ricava la differenza (cut) tra le due forme precedenti.*

## Tutorial

La pagina [Tutorial](tutorials/it.md) fornisce alcuni esempi che usano il metodo CSG per la creazione di solidi con l\'ambiente <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench/it.md).

-   [Modellazione tradizionale, il modo CSG](Manual:Traditional_modeling,_the_CSG_way/it.md)
-   [Tutorial Sfera traforata](Whiffle_Ball_tutorial/it.md)
-   [Guida introduttiva alla modellazione 3D](Basic_modeling_tutorial/it.md)



---
![](images/Button_right.svg) [documentation index](../README.md) > [Common Questions](Category_Common Questions.md) > [Part](Category_Part.md) > Constructive solid geometry/it
