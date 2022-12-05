---
- GuiCommand:/es
   Name:PartDesign Draft
   Name/es:DiseñoPiezas Borrador
   MenuLocation:DiseñoPiezas → Borrador
   Workbenches:[DiseñoPiezas](PartDesign_Workbench/es.md)
   Shortcut:Ninguno
   SeeAlso:Ninguno
---

# PartDesign Draft/es


</div>

## Description


<div class="mw-translate-fuzzy">

### Descripción

Esta herramienta crea una corriente de aire angular en las caras seleccionadas de un objeto. Se crea una nueva entrada de borrador separada (seguida de un número secuencial si ya existen borradores en el documento) en el árbol de proyecto.


</div>

   --
  ![Select one or more faces of the object before starting the tool. Here, 2 faces have been selected.](images/PartDesign_Draft-01.png ) ![Showing Draft Parameters in TaskPanel.](images/PartDesign_Draft-02.png ) ![2 faces have been added, and a 10 deg. draft applied. The bottom plane has remained dimensionally stable, while the draft has made the top plane smaller.](images/PartDesign_Draft-03.png ) ![The Neutral Plane has been changed to the top. Now, the top plane has stayed dimensionally stable, while the draft has made the bottom plane larger.](images/PartDesign_Draft-04.png ) ![Pull direction is set to the lower right edge, resulting in the draft pulling to the left.](images/PartDesign_Draft-05.png ) ![Checking the Reverse Direction box has applied an inward draft rather than outward.](images/PartDesign_Draft-06.png )   
   --





## Usage

### Add a draft 

1.  Optionally [activate](PartDesign_Body#Active_status.md) the Body to apply the Draft to.
2.  Select one or more faces of the Body.
3.  There are several ways to invoke the tool:
    -   Press the **<img src="images/PartDesign_Draft.svg" width=16px> [Draft](PartDesign_Draft.md)** button.
    -   Select the **Part Design → Apply a dress-up feature → <img src="images/PartDesign_Draft.svg" width=16px> Draft** option from the menu.
4.  If there is no active Body, and there are two or more Bodies in the document, the **Active Body Required** dialog will open and prompt you to activate one. If there is a single Body it will be activated automatically.
5.  The **Draft parameters** [task panel](Task_panel.md) opens. See [Options](#Options.md) for more information.
6.  Press the **OK** button to finish.

:   *Remember*:
    -   Since there must be at least one face for the feature, the last remaining face in the list cannot be removed.

### Edit a draft 

1.  Do one of the following:
    -   Double-click the Draft object in the [Tree view](Tree_view.md).
    -   Right-click the Draft object in the [Tree view](Tree_view.md) and select **Edit Draft** from the context menu.
2.  The **Draft parameters** [task panel](Task_panel.md) opens. See [Options](#Options.md) for more information.
3.  Press the **OK** button to finish.

## Options

-    **Add face**: Add faces to the selection by pressing the **Add face** button and selecting more faces.

-    **Remove face**: Choose a way to remove faces from the selection:

    -   Select one or more faces in the list and press the **Del** key or right-click the list and select **Remove** from the context menu.
    -   Press the **Remove face** button. All previously selected faces are highlighted in purple. Select each face to be removed.

-    **Draft angle**: Set the Draft angle either by entering a value or by clicking the up/down arrows.

-    **Neutral plane**: Set the the neutral plane by pressing the **Neutral plane** button and selecting the plane that must not change dimensionally.

-    **Pull direction**: Set the the pull direction by pressing the **Pull direction** button, then select an edge. Pull Direction is only effective if the Neutral Plane has been set. Results can be unpredictable.

-    **Reverse pull direction**: Invert the pull direction by checking the **Reverse pull direction** checkbox. This will toggle the draft between positive and negative angles.

## Notes

-   The Draft tool will only work on faces that are not tangentially connected to other faces. A common mistake is to attempt to apply draft to a face that already has a fillet applied to it. To solve this, remove the fillet, apply the draft as needed, then re-apply the fillet.

## Properties

See also: [Property editor](Property_editor.md).

A PartDesign Draft object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{Properties_Title|Base}}

-    **Angle|Angle**: Cannot be negative. Default: {{value|1.5 °}}.

-    **Reversed|Bool**: Default: `False`.

-    **Base|LinkSub**: Sub-link to the parent feature\'s list of selected edges and faces.

-    **Support Transform|Bool**: \"Include the base additive/subtractive shape when used in pattern features. If disabled, only the dressed part of the shape is used for patterning\". Default: `False`.

-    **Add Sub Shape|PartShape|hidden**
    

-    **Base Feature|Link|hidden**: Link to the parent feature.

-    **_ Body|LinkHidden|hidden**: Link to the parent body.


{{Properties_Title|Draft}}

-    **Neutral Plane|LinkSub**: Sub-link to the parent feature\'s list containing the neutral plane.

-    **Pull Direction|LinkSub**
    


{{Properties_Title|Part Design}}

-    **Refine|Bool**: \"Refine shape (clean up redundant edges) after adding/subtracting\". The default value is determined by the **Automatically refine model after sketch-based operation** preference. See [PartDesign Preferences](PartDesign_Preferences#General.md).


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Draft/es
