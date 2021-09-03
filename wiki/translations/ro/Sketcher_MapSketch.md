---
- GuiCommand:   Name:Sketcher MapSketch   Create a sketch on a face|Workbenches:[PartDesign](Sketcher_Workbench___Sketcher]],_[[PartDesign_Workbench.md)|MenuLocation:Part Design/Sketch → Map sketch to face...   SeeAlso:[Create a new sketch](Sketcher_NewSketch.md)---


</div>

## Descriere

Acest instrument pune o schiță existentă pe fața unei forme. PartDesign features created from this sketch will be fused with the underlying solid for additive features (Pad, Revolution) or be subtracted from the underlying solid in case of subtractive features (Pocket, Groove).

Rețineți că acest instrument nu este utilizat pentru a crea schițe noi. It only maps, or remaps an existing sketch to the face of a solid or a PartDesign feature. Typical use cases are:

-   The sketch was created on a standard plane (XY, XZ, YZ) and you want to map it to the face of a solid in order to build a feature upon it.
-   The sketch was mapped on a specific face of a solid but you need to map it to a different face.
-   Repairing a broken model.

<img alt="" src=images/Sketcher_MapSketch_00.png  style="width:480px;">

## Usage


<div class="mw-translate-fuzzy">

## Cum se utilizează {#cum_se_utilizează}

-   Select the face of a PartDesign feature or a solid.
-   Click on the **![](images/)_[Map_sketch_to_face](Sketcher_MapSketch.md)** icon in the toolbar (or go to the PartDesign or Sketch menu depending on which workbench is active)
-   In the **Select sketch** dialog window that opens, select from the list the sketch to map to the face and click OK.
-   The sketch is automatically opened in edit mode.


</div>

## Utilizarea când se repară un model distrus {#utilizarea_când_se_repară_un_model_distrus}

Sketcher MapSketch este adesea utilizat pentru a repara un model distrus.


<div class="mw-translate-fuzzy">

One common use case is when the dependency graph has been broken. (You can view the dependency graph by {{MenuCommand|Tools->Dependency graph}}.) This can happen when you delete a feature in the middle of your model tree. In the following example we will break and repair a model.


</div>

This is the base model. It has one pad, a pocket, and a pad inside that pocket. Note that the dependency graph is linear.

![](images/JschremppFCADEdit1.png )

Now we have deleted the pocket and the sketch that created the pocket (Pocket and Sketch001). Note that the dependency graph is broken. To repair this model we want to attach Sketch002 to the top face of Pad. In the view of the model you can see that it would be easy to select the wrong face.

![](images/JschremppFCADEdit2.png )

Pentru a repara modelul, schimbăm mai întâi vizibilitatea corpurilor solide. Facem Pad001 ascuns și facem Pad-ul vizibil.

![](images/JschremppFCADEdit3.png )

Acum, selectăm fața superioară a Plăcii și apoi selectăm instrumentul Map A Sketch To A Face. In the dialog that appears we select Sketch002. Our model is now repaired. In the model view we make Pad001 visible and Pad hidden and we can see the correct model.

![](images/JschremppFCADEdit4.png )


<div class="mw-translate-fuzzy">


</div>


{{Sketcher Tools navi

}}  

[Category:Sketcher/ro](Category:Sketcher/ro.md)
