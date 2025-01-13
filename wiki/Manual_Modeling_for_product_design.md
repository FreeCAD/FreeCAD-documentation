# Manual:Modeling for product design
The [PartDesign Workbench](PartDesign_Workbench.md) in FreeCAD is a versatile tool for creating parametric 3D models, particularly useful for solid body designs. It allows you to start with 2D sketches, which can then be transformed into 3D objects using operations like <img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> [padding](PartDesign_Pad.md), <img alt="" src=images/PartDesign_Revolution.svg  style="width:16px;"> [revolving](PartDesign_Revolution.md), and <img alt="" src=images/PartDesign_Pocket.svg  style="width:16px;"> [pocketing](PartDesign_Pocket.md). This workbench is essential for designing parts that require precision and parametric control, as changes to sketches or features automatically update the entire model.

One of the key advantages of the PartDesign Workbench is its suitability for creating parts for 3D printing. Since 3D printers require solid, watertight models, the PartDesign Workbench ensures that all features remain within a single coherent body. This eliminates common issues like gaps or overlapping faces, which can cause problems during slicing for 3D printing. Once your design is complete, you can easily export the model as an STL file---a format widely supported by 3D printers. This makes the PartDesign Workbench a go-to option for creating high-quality, printable objects, whether you\'re prototyping, designing functional parts, or creating intricate models for 3D printing.

To illustrate how the PartDesign Workbench works, let\'s model this well-known piece of [Lego](https://en.wikipedia.org/wiki/Lego). You can also refer to [Basic Part Design Tutorial 019](Basic_Part_Design_Tutorial_019.md) if you wish to try a different object.

![](images/FreeCAD_Exercise1_RedBrick.png )

We will now use exclusively the [Sketcher](Sketcher_Workbench.md) and [PartDesign](PartDesign_Workbench.md) tools. Since all the tools from the Sketcher Workbench are also included in the Part Design Workbench, we can stay in Part Design and we will not need to switch back and forth between the two.

In FreeCAD\'s PartDesign Workbench, objects are primarily built from Sketches, which are 2D profiles made up of linear segments such as lines, arcs, or ellipses, along with a series of constraints. These constraints dictate specific geometric rules for the sketch and can be applied to both the segments themselves and their key points, like endpoints or center points. For example, you can use a vertical constraint on a line to keep it perfectly vertical, or a position (lock) constraint to fix an endpoint in place, preventing it from moving.

A sketch is considered fully constrained when every point is locked into position by the appropriate number of constraints, meaning no part of the sketch can be moved freely. Achieving a fully constrained sketch is ideal because it ensures the design is well-defined and stable, allowing for predictable changes later in the design process. On the other hand, if more constraints are added than necessary---referred to as an over-constrained sketch---this can cause conflicts in the geometry. FreeCAD will alert you to any redundant or conflicting constraints, as over-constraining can cause issues in further operations like extrusions or cuts.

Adding the right constraints is key to creating a stable, parametric model. By carefully balancing constraints, you can easily modify or adjust sketches without breaking the geometry. This control makes the Part Design Workbench a powerful tool for precise, parametric modeling, especially for tasks like 3D printing, where maintaining proper geometric relationships is crucial to producing accurate, functional parts.

Sketches have an edit mode, where their geometry and constraints can be changed. When you are done with editing, and leave edit mode, sketches behave like any other FreeCAD object, and can be used as building blocks for all the Part Design tools, but also in other workbenches, such as [Part](Part_Workbench.md) or [Arch](Arch_Workbench.md). The [Draft workbench](Draft_Workbench.md) also has a tool that converts Draft objects to Sketches, and vice-versa.

-   Switch to the <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [PartDesign Workbench](PartDesign_Workbench.md)
-   Click on the <img alt="" src=images/PartDesign_NewSketch.svg  style="width:16px;"> [New Sketch](PartDesign_NewSketch.md) button and choose the **XY** plane, which is the \"ground\" plane. The sketch will be created and will immediately be switched to edit mode, and the view will be rotated to look at your sketch orthogonally.
-   Draw a rectangle, by selecting the <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:16px;"> [Rectangle](Sketcher_CreateRectangle.md) tool and clicking 2 corner points. You can place the two points anywhere since their correct location will be set in the next step.
-   You will notice that a couple of constraints have automatically been added to our rectangle: the vertical segments have received a vertical constraint, the horizontal ones a horizontal constraint, and each corner a point-on-point constraint that glues the segments together. You can experiment with moving the rectangle around by dragging its lines with the mouse, all the geometry will keep obeying the constraints.
-   Right now our sketch is under-constrained, as it\'s missing four constraints: its length, width, and its X and Y positioning. This lack of constraints allows you to freely move the sketch along the X and Y axes. Until these constraints are defined, the geometry is not fully locked in place, meaning both the size and position of the sketch remain adjustable. To fully define the sketch, we need to apply constraints that specify these values and lock the sketch in position.

![](images/FreeCAD_Exercise1_re_UC.png )

-   Now, let\'s add three more constraints:
    -   Select one of the vertical segments, and apply the <img alt="" src=images/Sketcher_Dimension.svg  style="width:16px;"> [ automatic dimension](Sketcher_Dimension.md) constraint to set its length to 23.7mm.
    -   Similarly, select the horizontal segment and set its length to 47.7mm using the same dimension constraint tool.
    -   Finally, select the upper left corner point of the rectangle, then the origin point (the dot where the red and green axes intersect), and the lower right corner point. Use the <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:16px;"> [symmetry constraint](Sketcher_ConstrainSymmetric.md) to make the rectangle symmetric about both the X and Y axes. This ensures the rectangle stays centered on the origin, limiting its range of movement and providing symmetry across the two axes.
-   You will now notice that our rectangle has turned green, indicating that it is fully constrained. This means every aspect of the sketch, including its position, size, and shape, is now fully defined and locked in place. It is generally a good practice to ensure that sketches are fully constrained, as this helps maintain control over your design and prevents unintended changes during further operations.

![](images/FreeCAD_Exercise1_re.png )

-   Our base sketch is now ready, we can leave edit mode by pressing the **Close** button on top of its task panel, or simply by pressing the **Escape** key. If needed later on, we can reenter edit mode anytime by double-clicking the sketch in the tree view, or by right-clicking and pressing on the edit sketch option.
-   Let\'s extrude it by using the <img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> [Pad](PartDesign_Pad.md) tool, and giving it a distance of 14.4mm. The other options can be left at their default values:

![](images/FreeCAD_Exercise1_padding.png )

-   The **Pad** tool is similar to the <img alt="" src=images/Part_Extrude.svg  style="width:16px;"> [Part Extrude](Part_Extrude.md) from the <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Workbench](Part_Workbench.md), but with a key difference: a pad is always linked to its sketch and cannot be moved independently. To reposition the pad, you must move the base sketch, ensuring that the pad remains securely attached. The pad will always remain part of the same body, maintaining the continuity of your design, which is especially useful for complex parts where features need to be built progressively and in alignment with one another. This adds stability to your design, especially when you want to ensure everything stays properly aligned and fixed in place.

-   Let\'s create the eight cylinders on the top face of the block. First, select the top face of the block and then click on the <img alt="" src=images/Std_AlignToSelection.svg  style="width:16px;"> [Align to selection](Std_AlignToSelection.md) option to align the view to this face. This will provide a clear and direct view, making it easier to accurately place the cylinders.
-   Click on the <img alt="" src=images/PartDesign_NewSketch.svg  style="width:16px;"> [New Sketch](PartDesign_NewSketch.md) button. The new sketch will be created directly on the top face.
-   Create two <img alt="" src=images/Sketcher_Circle.svg  style="width:16px;"> [circles](Sketcher_CreateCircle.md) anywhere you want.
-   Choose the center of both circles and the x axis (red line). Then press on the <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:16px;"> [symmetry constraint](Sketcher_ConstrainSymmetric.md) option.
-   Choose both circles and apply an <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:16px;"> [equal constraint](Sketcher_ConstrainEqual.md).
-   Using the <img alt="" src=images/Sketcher_Dimension.svg  style="width:16px;"> [ automatic dimension](Sketcher_Dimension.md) tool, set the diameter of one circle to 7.2 mm. Since we've already constrained both circles to have the same diameter, there's no need to set the diameter for the second circle---it will automatically adjust to match the first one.
-   We now need to position the circles relative to the edges of the face. However, you may notice that we are unable to select any points or edges directly. To resolve this, we can use the <img alt="" src=images/Sketcher_External.svg  style="width:16px;"> [External geometry](Sketcher_External.md) tool to reference the face's edges, allowing us to accurately constrain the circles in relation to the face. Press on the button and select the left edge of the face. This edge will now be highlighted in red and you will be able to create reference points from it, enabling you to apply constraints to precisely position the circles relative to the face\'s boundaries.
-   You can now set the X and Y center distances for one of the circles to 6 mm. Since the circles are constrained to each other, the second circle will adjust accordingly.

![](images/FreeCAD_Exercise1_TopFaceSketch.png )

-   Notice how, once again, when you lock the position and dimension of everything in your sketch, it becomes fully constrained. This always keeps you on the safe side. You could change the first sketch now, everything we did afterwards would keep tight.
-   Leave edit mode, select this new sketch, and create a <img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> [Pad](PartDesign_Pad.md) of 2.7mm:

![](images/FreeCAD_Exercise1_topCylPad.png )

-   Since we used the top face of our base block as the foundation for this new sketch, any Part Design operation applied to it will be correctly built on top of the base shape. The two circles are not independent objects; they will be extruded directly from the existing block. This is the key advantage of working in the Part Design Workbench---as long as you ensure each step is built upon the previous one, you are effectively constructing a single, cohesive solid object.
-   We can now duplicate our two dots four times. Select the latest Pad we just created.
-   Press the <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:16px;"> [Linear pattern](PartDesign_LinearPattern.md) button.
-   Give it a length of 36mm (which is the total \"span\" we want our copies to fit in), in the \"horizontal sketch axis\" direction, and make it 4 occurrences:

![](images/FreeCAD_Exercise1_topPattern.png )

-   We will now carve the inside of the block, using the <img alt="" src=images/PartDesign_Pocket.svg  style="width:16px;"> [Pocket](PartDesign_Pocket.md) tool, which is the PartDesign version of [Part Cut](Part_Cut.md). To make a pocket, we will create a sketch on the bottom face of our block, which will be used to remove a part of the block.
-   With the bottom face selected, press the <img alt="" src=images/PartDesign_NewSketch.svg  style="width:16px;"> [New Sketch](PartDesign_NewSketch.md) button.
-   Draw a <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:16px;"> [Rectangle](Sketcher_CreateRectangle.md) on the face.
-   Apply a <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:16px;"> [symmetry constraint](Sketcher_ConstrainSymmetric.md) by selecting the upper left corner point of the rectangle, then the origin point (the dot where the red and green axes intersect), and the lower right corner point.
-   By using the \[Image:Sketcher_External.svg\|16px\]\] [External geometry](Sketcher_External.md) choose the left edge of the bottom face. Notice again that it will be highlighted in red.
-   Set the horizontal and vertical distance of the rectangle in regards to the upper right point to 1.8 by using the <img alt="" src=images/Sketcher_Dimension.svg  style="width:16px;"> [ automatic dimension](Sketcher_Dimension.md) constraint.

![](images/FreeCAD_Exercise1_BottomRec.png )

-   Create three <img alt="" src=images/Sketcher_Circle.svg  style="width:16px;"> [circles](Sketcher_CreateCircle.md) by making sure their center is located on the X-axis (red line).
-   By choosing all three circles apply an <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:16px;"> [equal constraint](Sketcher_ConstrainEqual.md).
-   Set the diameter of one circle to 9.765mm.
-   Set the center distance of the left circle in regards to the bottom edge of the rectangle we created before to 10.2mm.
-   Set the distance between the left and middle circles to 12 mm. Repeat this step to set the same 12 mm distance between the middle and right circles

![](images/FreeCAD_Exercise1_BottomOuterCirc.png )

-   We are almost done.
-   Create three additional <img alt="" src=images/Sketcher_Circle.svg  style="width:16px;"> [circles](Sketcher_CreateCircle.md) , ensuring that each new circle is concentric with one of the previously drawn circles. Alternatively, you can place the new circles anywhere in the sketch and use the <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:16px;"> [coincident constraint](Sketcher_ConstrainCoincident.md) tool to align their centers with the centers of the existing circles.
-   By choosing all three circles apply an <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:16px;"> [equal constraint](Sketcher_ConstrainEqual.md).
-   Set the diameter of one circle to 7.2mm.
-   You can now exit the sketch.

![](images/FreeCAD_Exercise1_bottomSketchCom.png )

-   By choosing the completed sketch use the <img alt="" src=images/PartDesign_Pocket.svg  style="width:16px;"> [Pocket](PartDesign_Pocket.md) tool setting the length to 12 mm.

![](images/FreeCAD_Exercise1_BottomPad.png )

-   This is it. Our brick is ready. If you wish to change its color, you can do so by going to the **View tab**.

![](images/FreeCAD_Exercise1_redBrick2.png )

You may notice that the modeling history in the tree view has become quite extensive. This is incredibly valuable, as it allows us to revisit and modify any step in the design process at any time. For instance, adapting this model to create a 2x2 brick instead of a 2x4 would be a breeze---just a few adjustments to the dimensions and pattern occurrences would do the trick. This same flexibility allows us to design larger, custom pieces that aren\'t part of the original Lego set. The parametric nature of FreeCAD makes it easy to modify existing models, giving us full control to adapt or expand the design as needed.

But we could also want to get rid of the history, for example, if we are going to model a castle with this brick, and we don\'t want to have this whole history repeated 500 times in our file.

There are two simple ways to get rid of the history, one is using the [Create simple copy](Part_SimpleCopy.md) tool from the [Part Workbench](Part_Workbench.md), which will create a copy of our piece that doesn\'t depend anymore on the history (you can delete the whole history afterwards), the other way is exporting the piece as a STEP file and re-importing it.

**Downloads**

-   The model produced during this exercise: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/lego.FCStd>

**Read more**

-   [The Sketcher](Sketcher_Workbench.md)
-   [The Part Design Workbench](PartDesign_Workbench.md)
-   [The Assembly2 Workbench](https://github.com/hamish2014/FreeCAD_assembly2)



---
⏵ [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > Manual:Modeling for product design
