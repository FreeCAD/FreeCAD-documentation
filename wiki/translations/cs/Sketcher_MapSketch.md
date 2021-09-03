---
- GuiCommand:/cs   Name:Sketcher_MapSketch   Name/cs:Skicář Vyznač náčrt   Vytvoří náčrt na ploše|Workbenches:[Návrh dílu](Sketcher_Workbench/cs___Skicář]],_[[PartDesign_Workbench/cs.md)|MenuLocation:Návrh dílu → Vytvoř náčrt na ploše   SeeAlso:[Vytvoř náčrt](Sketcher_NewSketch/cs.md)---


</div>


<div class="mw-translate-fuzzy">

## Popis

Vytvoří náčrt na ploše objektu. <img alt="Vytvoří náčrt na ploše objektu." src=images/Sketcher_MapSketch_00.png  style="width:480px;"> 


</div>

Please note that this tool is not used to create new sketches. It only maps, or remaps an existing sketch to the face of a solid or a PartDesign feature. Typical use cases are:

-   The sketch was created on a standard plane (XY, XZ, YZ) and you want to map it to the face of a solid in order to build a feature upon it.
-   The sketch was mapped on a specific face of a solid but you need to map it to a different face.
-   Repairing a broken model.

<img alt="" src=images/Sketcher_MapSketch_00.png  style="width:480px;">

## Usage


<div class="mw-translate-fuzzy">

## Použití

Vyberte plochu na objektu nebo aplikujte změnu a potom klikněte na tlačítko **![](images/)_[Vytvoř_náčrt_na_ploše](Sketcher_MapSketch/cs.md)** což vede na [Skicář](Sketcher_NewSketch/cs.md) 


</div>

## Use when repairing a broken model 

Sketcher MapSketch is often used when repairing a broken model.

One common use case is when the dependency graph has been broken. (You can view the dependency graph by **Tools** → **[Dependency graph](Std_DependencyGraph.md)**.) This can happen when you delete a feature in the middle of your model tree. In the following example we will break and repair a model.

This is the base model. It has one pad, a pocket, and a pad inside that pocket. Note that the dependency graph is linear.

![](images/JschremppFCADEdit1.png )

Now we have deleted the pocket and the sketch that created the pocket (Pocket and Sketch001). Note that the dependency graph is broken. To repair this model we want to attach Sketch002 to the top face of Pad. In the view of the model you can see that it would be easy to select the wrong face.

![](images/JschremppFCADEdit2.png )

To repair the model we first change the visibility of the solids. We make Pad001 hidden and we make Pad visible.

![](images/JschremppFCADEdit3.png )

Now we select the top face of Pad and then select the Map A Sketch To A Face tool. In the dialog that appears we select Sketch002. Our model is now repaired. In the model view we make Pad001 visible and Pad hidden and we can see the correct model.

![](images/JschremppFCADEdit4.png )


<div class="mw-translate-fuzzy">


</div>


{{Sketcher Tools navi

}}  

[Category:Sketcher/cs](Category:Sketcher/cs.md)
