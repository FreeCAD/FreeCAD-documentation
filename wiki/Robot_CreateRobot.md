---
- GuiCommand:
   Name: Robot CreateRobot
   MenuLocation: Robot - Insert robot
   Workbenches: [Robot](Robot_Workbench.md)
---

# Robot CreateRobot

## Description

Insert a new robot (KUKA IR500) into the scene.

## Usage

1.  Click on <img alt="" src=images/Robot_CreateRobot.svg  style="width:32px;"> to insert a KUKA IR500 robot into the scene.
2.  Inserting different/more robots can be done in two ways via the
    -   Selecting **Robot** → **Insert Robots** from the top menu.

    :   **OR**

    -   Make sure a new document is/was created and activated (activate via double-click on document in [tree view](Tree_view.md)).
    -   Switch to the \"Tasks\"-Tab in the [tree view](Tree_view.md)).
3.  Select one of the four predefined robots.

## Limitations

Related to versions 0.15/0.16

-   Only robots with up to six axes with rotational movement are definable.
-   No robots with translational movements possible.
-   The robot must be defined via code and a VRML-file, for more info refer to [Robot 6-Axis](Robot_6-Axis.md).

## Notes

The predefined robots are:

-   KUKA IR500
-   KUKA IR210
-   KUKA IR125
-   KUKA IR16




 {{Robot_Tools_navi}}



---
⏵ [documentation index](../README.md) > [Robot](Robot_Workbench.md) > Robot CreateRobot
