---
 GuiCommand:
   Name: Assembly ToggleGrounded
   Name/de: Assembly VerankertUmschalten
   MenuLocation: Assembly , Festsetzen umschalten
   Workbenches: Assembly_Workbench/de
   Shortcut: **G**
   Version: 1.0
   SeeAlso: 
---

# Assembly ToggleGrounded/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Assembly_ToggleGrounded.svg  style="width:16px;"> [Assembly VerankertUmschalten](Assembly_ToggleGrounded/de.md) setzt Position und Ausrichtung einer Form im Bezug zu dem Koordinatensystem fest, zu dem sie gehört. (Die Form wird im Koordinatensystem verankert)



## Anwendung


<div lang="en" dir="ltr" class="mw-content-ltr">

1.  Select one or more parts.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Assembly_ToggleGrounded.svg" width=16px> [Toggle grounded](Assembly_ToggleGrounded.md)** button.
    -   Select the **Assembly → <img src="images/Assembly_ToggleGrounded.svg" width=16px> Toggle grounded** option from the menu.
    -   Use the keyboard shortcut: **G**.
3.  A GroundedJoint is added for each selected part.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Notes


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   A grounded joint will display a red lock icon in the 3D view, around the center of mass of the grounded component. To hide the lock, toggle the joint\'s **Visibility** to off.


</div>



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein **GroundedJoint**-Objekt wird von einem [App FeaturePython](App_FeaturePython/de.md)-Objekt abgeleitet und erbt alle seine Eigenschaften. Außerdem besitzt es die folgenden zusätzlichen Eigenschaften:



### Daten


{{TitleProperty|Ground}}

-    **Object To Ground|Link**: Das zu verankernde Objekt.

-    **Placement|Placement**: Dies gibt an, wo das Objekt verankert ist. Siehe [Positionierung](Placement/de.md).





{{Assembly_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Assembly](Assembly_Workbench.md) > Assembly ToggleGrounded/de
