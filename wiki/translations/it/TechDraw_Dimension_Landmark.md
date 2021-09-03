---
- GuiCommand:/it
   Name:TechDraw  Dimension Landmark
   Name/it:Quota da punti di riferimento
   Icon:Techdraw-landmarkdistance.svg
   MenuLocation:TechDraw → Quota da punti di riferimento
   Workbenches:[TechDraw](TechDraw_Workbench/it.md)
   SeeAlso:[Dimensione orizzontale](TechDraw_Dimension_Horizontal/it.md), [Dimensione verticale](TechDraw_Dimension_Vertical/it.md)
   Version:0.19
---


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento Quota da punti di riferimento aggiunge una quota lineare a una vista. La dimensione si basa su due **funzioni** punto (Draft.Point o Part.Vertex) del modello 3D. Notare che i punti devono essere oggetti **funzioni** che compaiono nella [vista ad albero](tree_view/it.md) del modello. I vertici casuali di una forma non funzionano.


</div>


<div class="mw-translate-fuzzy">

Lo scopo di questo strumento è fornire una soluzione alternativa alla corruzione della dimensione causata dai problemi di \" \"[denominazione topologica](topological_naming_problem/it.md)\"\". I punti sorgente dovrebbero usare [Espressioni](Expressions/it.md) o altri meccanismi di contenimento per stabilire la loro posizione. Poiché i punti sono [Oggetti documento](Document_Objects/it.md) e non modellano i componenti, il loro nome non cambia con i ricalcoli e quindi sono facilmente reperibili.


</div>


<div class="mw-translate-fuzzy">

Vedere le sezioni Limitazione e soluzioni di [Lunghezza](TechDraw_Dimension_Length/it.md) per ulteriori informazioni su dimensioni e denominazione topologica.


</div>

La quota da punti di riferimento generalmente si comporta come qualsiasi altra quota

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare 2 oggetti Punto nella [vista ad albero](tree_view/it.md) o nella [Vista 3D](3D_view/it.md).
2.  Selezionare anche la vista a cui aggiungere la dimensione.
3.  Premere il pulsante **<img src="images/Techdraw-landmarkdistance.svg" width=20px> [Quota da punti di riferimento](TechDraw_Dimension_Landmark/it.md)** o usare {{MenuCommand|TechDraw → Dimensioni → Quota da punti di riferimento}}.
4.  Alla vista viene aggiunta una dimensione. Il testo della quota può essere trascinato nella posizione desiderata.


</div>

## Limitazioni

Lo strumento Quota da punti di riferimento è inizialmente limitato alle dimensioni \"Distanza\". Altri tipi possono essere aggiunti se richiesto.

## Proprietà

Quota da punti di riferimento non introduce nuove proprietà.

## Script


<div class="mw-translate-fuzzy">


**Vedere anche:**

[TechDraw API](TechDraw_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Quota da punti di riferimento può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione:


</div>


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw::LandmarkDimension','Landmark')
dim1.Type = "Distance"
dim1.References2D=[(TDView, 'Vertex1')]
dim1.References3D=[(Point3d1, 'Vertex1')]
dim1.References3D=[(Point3d2, 'Vertex1')]
rc = page.addView(dim1)
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}  
