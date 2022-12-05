---
- GuiCommand:/ru
   Name/ru:Преобразовать в полое тело
   Name:PartDesign_Thickness
   MenuLocation:Part Design → Apply a dress up feature → Преобразовать в полое тело
   Workbenches:[PartDesign](PartDesign_Workbench/ru.md)
   Version:0.17
   SeeAlso:[Преобразовать в полое тело](Part_Thickness/ru.md)
---

# PartDesign Thickness/ru

## Описание

The <img alt="" src=images/PartDesign_Thickness.svg  style="width:24px;"> **PartDesign Thickness** tool transforms a solid body into a hollow object with at least one open face, giving to each of its remaining faces a uniform thickness. It adds a **Thickness** object to the document with its corresponding representation in the [Tree view](Tree_view.md).

<img alt="" src=images/PartDesign_Thickness_example.svg  style="width:600px;"> 
*Base solid (A) →  Solid with selected face to be opened (B) →  Resulting hollow object (C)*

## Применение

### Преобразование в полое тело 

1.  Optionally [activate](PartDesign_Body#Active_status.md) the Body to apply the Thickness to.
2.  Select one or more faces of the Body.
3.  There are several ways to invoke the tool:
    -   Press the **<img src="images/PartDesign_Thickness.svg" width=16px> [Thickness](PartDesign_Thickness.md)** button.
    -   Select the **Part Design → Apply a dress-up feature → <img src="images/PartDesign_Thickness.svg" width=16px> Thickness** option from the menu.
4.  If there is no active Body, and there are two or more Bodies in the document, the **Active Body Required** dialog will open and prompt you to activate one. If there is a single Body it will be activated automatically.
5.  The **Thickness parameters** [task panel](Task_panel.md) opens. See [Options](#Options.md) for more information.
6.  Press the **OK** button to finish.

:   *Remember*:
    -   Since there must be at least one face for the feature, the last remaining face in the list cannot be removed.

### Изменение параметров преобразования 

1.  Do one of the following:
    -   Double-click the Thickness object in the [Tree view](Tree_view.md)
    -   Right-click the Thickness object in the [Tree view](Tree_view.md) and select **Edit Thickness** from the context menu.
2.  The **Thickness parameters** [task panel](Task_panel.md) opens. See [Options](#Options.md) for more information.
3.  Press the **OK** button to finish.

## Параметры

-    **Add face**: Add faces to the selection by pressing the **Add face** button and selecting more faces.

-    **Remove face**: Choose a way to remove faces from the selection:

    -   Select one or more faces in the list and press the **Del** key or right-click the list and select **Remove** from the context menu.
    -   Press the **Remove face** button. All previously selected faces are highlighted in purple. Select each face to be removed.

-    **Thickness**: Set the wall thickness either by editing the value or by clicking the up/down arrows.

-    **Mode**:

    -   
        **Skin**
        
        : Only this option can be selected.

    -   
        **Pipe**
        
        : Not implemented. See [this forum topic](https://forum.freecadweb.org/viewtopic.php?p=484495#p484495).

    -   
        **Recto Verso**
        
        : Not implemented. See [idem](https://forum.freecadweb.org/viewtopic.php?p=484495#p484495).

-    **Join Type**:

    -   
        **Arc**
        
        : When non-tangential faces are offset, new faces that do not intersect are joined by a fillet with a radius equal to the defined thickness.

    -   
        **Intersection**
        
        : When non-tangential faces are offset, new faces that do not intersect are extended to meet at their virtual intersection.

-    **Intersection**: When checked, self-intersections in certain models are avoided. This option is not recommended as it relies on an incomplete [OpenCASCADE method](https://dev.opencascade.org/doc/refman/html/class_b_rep_offset_a_p_i___make_thick_solid.html#af78f35025a31e2ce8bd96c82fb33a981).

-    **Make thickness inwards**: When checked, faces are offset inward.

## Примечания

-   If thickness goes inwards, the value must be smaller than the smallest height of the Body.
-   The tool may fail with complex shapes. [Additive Pipe](PartDesign_AdditivePipe.md) or [Additive Loft](PartDesign_AdditiveLoft.md) may work better to create complex shapes.
-   Known errors:
    -   BRep_API: command not done.
    -   BRep_Tool: no parameter on edge.
    -   Silently fails.

## Свойства

See also: [Property editor](Property_editor.md).

A PartDesign Thickness object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Данные


{{Properties_Title|Основные}}

-    **Base|LinkSub**: Sub-link to the parent feature\'s list of selected edges and faces.

-    **Support Transform|Bool**: \"Include the base additive/subtractive shape when used in pattern features. If disabled, only the dressed part of the shape is used for patterning\". Default: `False`.

-    **Add Sub Shape|PartShape|hidden**
    

-    **Base Feature|Link|hidden**: Link to the parent feature.

-    **_ Body|LinkHidden|hidden**: Link to the parent body.


{{Properties_Title|Part Design}}

-    **Refine|Bool**: \"Refine shape (clean up redundant edges) after adding/subtracting\". The default value is determined by the **Automatically refine model after sketch-based operation** preference. See [PartDesign Preferences](PartDesign_Preferences#General.md).


{{Properties_Title|Thickness}}

-    **Value|Length**: \"Thickness value\". Default: {{value|1 mm}}.

-    **Mode|Enumeration**: \"Mode\". {{value|Skin}} (default), {{value|Pipe}} or {{Value|Recto verso}}. Only {{value|Skin}} is implemented.

-    **Join|Enumeration**: \"Join type\". {{value|Arc}} (default) or {{Value|Intersection}}.

-    **Reversed|Bool**: \"Apply the thickness towards the solids interior\". Default: `False`.

-    **Intersection|Bool**: \"Enable intersection-handling\". Default: `False`.





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Thickness/ru
