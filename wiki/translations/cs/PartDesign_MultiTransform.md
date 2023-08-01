# PartDesign MultiTransform/cs
---
- GuiCommand:   Name: PartDesign_MultiTransform   Name/cs: Návrh dílu MultiTransformace   Workbenches: [[PartDesign Workbench/cs   Návrh dílu]], Kompletace|MenuLocation: Návrh dílu -> MultiTransformace---


</div>


<div class="mw-translate-fuzzy">

## Úvod

\'Vytváří tvar pomocí kombinací více transformací\' - Tento nástroj vezme množinu jednoho nebo více objektů jako vstup (originály) a umožní na nich postupně aplikovat několik transformací. Například vytvoří přírubu se dvěma řadami otvorů. Otvor (\'originál\') je nejdříve upraven v přímém vzoru ve směru osy X a potom osmkrát vzorkován v polárním vzorku kolem osy Y. <img alt="" src=images/multitransform_example.png  style="width:600px;"> 


</div>

The <img alt="" src=images/PartDesign_MultiTransform.svg  style="width:24px;"> **PartDesign MultiTransform** tool creates a pattern of one or more features. The pattern can include multiple transformations where each subsequent transformation is applied to the result of the previous transformation.

The available transformations are: <img alt="" src=images/PartDesign_Mirrored.svg  style="width:16px;"> [Mirrored](PartDesign_Mirrored.md), <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:16px;"> [LinearPattern](PartDesign_LinearPattern.md), <img alt="" src=images/PartDesign_PolarPattern.svg  style="width:16px;"> [PolarPattern](PartDesign_PolarPattern.md) and <img alt="" src=images/PartDesign_Scaled.svg  style="width:16px;"> [Scaled](PartDesign_Scaled.md). The first three are also available as separate tools.

<img alt="" src=images/multitransform_example.png  style="width:600px;"> 
*A pattern of holes created from a single Hole feature by applying a LinearPattern with 2 occurences, followed by a PolarPattern with 8 occurrences.*

## Usage

### Create

1.  Optionally [activate](PartDesign_Body#Active_status.md) the correct Body.
2.  Optionally select one or more features in the [Tree view](Tree_view.md) or the [3D view](3D_view.md).
3.  There are several ways to invoke the tool:
    -   Press the **<img src="images/PartDesign_MultiTransform.svg" width=16px> [Create MultiTransform](PartDesign_MultiTransform.md)** button.
    -   Select the **Part Design → Apply a pattern → <img src="images/PartDesign_MultiTransform.svg" width=16px> Create MultiTransform** option from the menu.
4.  If there is no active Body, and there are two or more Bodies in the document, the **Active Body Required** dialog will open and prompt you to activate one. If there is a single Body it will be activated automatically.
5.  If no features were selected the **Select feature** [task panel](Task_panel.md) opens: select one or more (hold down the **Ctrl** key) from the list and press the **OK** button.
6.  The **MultiTransform parameters** [task panel](Task_panel.md) opens. See [Options](#Options.md) for more information.
7.  Press the **OK** button at the top to finish.

### Edit

1.  Do one of the following:
    -   Double-click the MultiTransform object in the [Tree view](Tree_view.md).
    -   Right-click the MultiTransform object in the [Tree view](Tree_view.md) and select **Edit MultiTransform** from the context menu.
2.  The **MultiTransform parameters** [task panel](Task_panel.md) opens. See [Options](#Options.md) for more information.
3.  Press the **OK** button at the top to finish.

### Combine existing transformations 

It is possible to create a MultiTransform object from existing [Mirrored](PartDesign_Mirrored.md), [LinearPattern](PartDesign_LinearPattern.md) and [PolarPattern](PartDesign_PolarPattern.md) transformations.

1.  Check the **Originals** property of the existing transformations to make sure they have been applied to the same features.
2.  Select those features in the [Tree view](Tree_view.md).
3.  There are several ways to invoke the tool:
    -   Press the **<img src="images/PartDesign_MultiTransform.svg" width=16px> [Create MultiTransform](PartDesign_MultiTransform.md)** button.
    -   Select the **Part Design → Apply a pattern → <img src="images/PartDesign_MultiTransform.svg" width=16px> Create MultiTransform** option from the menu.
4.  The **MultiTransform parameters** [task panel](Task_panel.md) opens.
5.  Press the **OK** button at the top.
6.  Edit the **Tranformations** property of the created MultiTransform object:
    1.  Click in the field.
    2.  Press the **...** button that appears.
    3.  The **Link** dialog opens.
    4.  Hold down the **Ctrl** key and select the existing transformations.
    5.  Press the **OK** button.
7.  Optionally [edit](#Edit.md) the MultiTransform object, see above.

## Options

-   To add features:
    1.  Press the **Add feature** button.
    2.  Select a feature in the [Tree view](Tree_view.md) or the [3D view](3D_view.md).
    3.  Repeat to add more features.
-   To remove features:
    1.  Press the **Remove feature** button.
    2.  Do one of the following:
        -   Select a feature in the [Tree view](Tree_view.md) or the [3D view](3D_view.md).
        -   Select a feature in the list at the top and press the **Del** key.
        -   Right-click a feature in the list at the top and select **Remove** from the context menu.
    3.  Repeat to remove more features.
-   If there are several features in the pattern, their order can be important. See [PartDesign PolarPattern](PartDesign_PolarPattern#Ordering_features.md).
-   To add transformations:
    1.  If there are existing transformations: select the transformation after which the new transformation should be added.
    2.  Right-click the **Transformations** list.
    3.  Select one the following options from the context menu:
        -   
            **Add mirrored transformation**
            
            . See [PartDesign Mirrored](PartDesign_Mirrored.md).

        -   
            **Add linear pattern**
            
            . See [PartDesign LinearPattern](PartDesign_LinearPattern.md).

        -   
            **Add polar pattern**
            
            See [PartDesign PolarPattern](PartDesign_PolarPattern.md).

        -   
            **Add scaled transformation**
            
            . See [PartDesign Scaled](PartDesign_Scaled.md).
    4.  The selected transformation is added to the list and the settings for the transformation are displayed below the list.
    5.  Adjust the settings to suit.
    6.  Press the **OK** bar at the bottom.
    7.  Repeat to add more transformations.
-   To edit a transformation:
    1.  Right-click the transformation in the **Transformations** list.
    2.  Select **Edit** from the context menu.
    3.  Adjust the settings to suit.
    4.  Press the **OK** bar at the bottom.
-   To change the order of the transformations:
    1.  Right-click a transformation in the **Transformations** list.
    2.  Select **Move up** or **Move down** from the context menu.
-   If the **Update view** checkbox is checked the view will update in real time.

## Limitations

See [PartDesign PolarPattern](PartDesign_PolarPattern#Limitations.md).

## Example

You can use this tool to create a fully parametric part that is symmetrical about two axes from a sketch.

This could be a 150x100x10mm large mounting plate for a motor with symmetric holes.

<img alt="" src=images/PartDesign_MultiTransform_Example2.png  style="width:400px;">

1.  Create a <img alt="" src=images/PartDesign_Body.svg  style="width:16px;"> [Body](PartDesign_Body.md) and add a <img alt="" src=images/PartDesign_NewSketch.svg  style="width:16px;"> [sketch](PartDesign_NewSketch.md) on one of its base planes.
2.  In the sketch create geometry for one quadrant of the part (i.e. the upper right quadrant).
    -   Note that the constraints must also only cover a quarter of the part, e.g. instead of the full dimension of {{Value|150mm}} enter {{Value|150/2mm}} or {{Value|75mm}}.
    -   Make sure the sketch is closed by adding lines along the vertical and horizontal axes.
3.  Extrude the part with <img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> [PartDesign Pad](PartDesign_Pad.md).
4.  Select <img alt="" src=images/PartDesign_MultiTransform.svg  style="width:16px;"> **PartDesign MultiTransform**.
5.  The task dialog opens.
6.  The last feature of the Body is already selected. Since we want to mirror that feature we can ignore the **Add feature** and **Remove feature** buttons.
7.  Right-click in the **Transformations** field and select **Add mirrored transform** from the context menu.
8.  For the **Plane** select **Vertical sketch axis**.
9.  If the **Update view** checkbox is checked, you should now see the part mirrored about one axis.
10. Again select **Add mirrored transform** from the context menu of the **Transformations** field.
11. Now for the **Plane** select **Horizontal sketch axis**.
12. Press the **OK** button to finish.
13. To remove the edges along the axes of symmetry in the final result, set the **Refine** property of the new feature to {{Value|true}} in the [Property editor](Property_editor.md).

To verify that the part is fully parametric open the initial sketch with the quarter part and change one dimension, say a hole diameter. After closing the sketch the three other holes will have changed accordingly. This works with all other dimensions as well. A sketch modelling the full part with a single extrusion and no mirroring would be a lot more complex and all later changes would be more complicated.





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign MultiTransform/cs
