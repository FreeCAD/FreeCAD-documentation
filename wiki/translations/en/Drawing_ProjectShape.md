---
- GuiCommand   *
   Name   *Drawing ProjectShape
   Empty   *1
   Workbenches   *[Drawing](Drawing_Workbench.md)
   MenuLocation   *Drawing → Project shape
---

# Drawing ProjectShape/en

## Description

This tool creates a projection of the selected object (Source) in the 3D view.

![](images/ProjectShape1_it.png )

## Usage

+++
| ![](images/ProjectShapeSet_it.png ) | 1.  Select an object in the 3D view or in the project tree                                                                                                                                                                         |
|                                                      | 2.  from the Drawing menu, click **Project shape**                                                                                                                                                                                 |
|                                                      | 3.  set the desired options in the Task Dialog                                                                                                                                                                                     |
|                                                      | 4.  click **OK**                                                                                                                                                                                                 |
|                                                      |                                                                                                                                                                                                                                    |
|                                                      | A projection object (**objectname\_proj**) will be added to the project. For subsequent projections of the same Source object, the projection object will be named **objectname\_projXXX**, where **XXX** is a three digit number. |
+++

### Edit an existing projection 

+++
| ![](images/ProjectShapeOptions_it.png ) | The projection parameters can be edited in the Property editor.                                                                                                                                                      |
|                                                              | **Base**                                                                                                                                                                                           |
|                                                              |                                                                                                                                                                                                                      |
|                                                              | -                                                                                                                                                                                                     |
|                                                              |     **Label**                                                                                                                                                                                           |
|                                                              |                                                                                                                                                                                                                   |
|                                                              |        *                                                                                                                                                                                                                |
|                                                              |                                                                                                                                                                                                                      |
|                                                              | -                                                                                                                                                                                                     |
|                                                              |     **Placement**                                                                                                                                                                                       |
|                                                              |                                                                                                                                                                                                                   |
|                                                              |        *                                                                                                                                                                                                                |
|                                                              |                                                                                                                                                                                                                      |
|                                                              | **Projection**                                                                                                                                                                                     |
|                                                              |                                                                                                                                                                                                                      |
|                                                              | -                                                                                                                                                                                                     |
|                                                              |     **Direction**                                                                                                                                                                                       |
|                                                              |                                                                                                                                                                                                                   |
|                                                              |        * defines the direction of the projection. This is the normal vector of the projection plane. For example, to project the object onto the xy plane, use (0,0,1). To reverse the projection, use negative values. |
|                                                              |                                                                                                                                                                                                                      |
|                                                              | -                                                                                                                                                                                                     |
|                                                              |     **HCompound**                                                                                                                                                                                       |
|                                                              |                                                                                                                                                                                                                   |
|                                                              |        *                                                                                                                                                                                                                |
|                                                              |                                                                                                                                                                                                                      |
|                                                              | -                                                                                                                                                                                                     |
|                                                              |     **Iso Line HCompound**                                                                                                                                                                              |
|                                                              |                                                                                                                                                                                                                   |
|                                                              |        *                                                                                                                                                                                                                |
|                                                              |                                                                                                                                                                                                                      |
|                                                              | -                                                                                                                                                                                                     |
|                                                              |     **Iso Line VCompound**                                                                                                                                                                              |
|                                                              |                                                                                                                                                                                                                   |
|                                                              |        *                                                                                                                                                                                                                |
|                                                              |                                                                                                                                                                                                                      |
|                                                              | -                                                                                                                                                                                                     |
|                                                              |     **Out Line HCompound**                                                                                                                                                                              |
|                                                              |                                                                                                                                                                                                                   |
|                                                              |        *                                                                                                                                                                                                                |
|                                                              |                                                                                                                                                                                                                      |
|                                                              | -                                                                                                                                                                                                     |
|                                                              |     **Out Line VCompound**                                                                                                                                                                              |
|                                                              |                                                                                                                                                                                                                   |
|                                                              |        *                                                                                                                                                                                                                |
|                                                              |                                                                                                                                                                                                                      |
|                                                              | -                                                                                                                                                                                                     |
|                                                              |     **Rg1 Line HCompound**                                                                                                                                                                              |
|                                                              |                                                                                                                                                                                                                   |
|                                                              |        *                                                                                                                                                                                                                |
|                                                              |                                                                                                                                                                                                                      |
|                                                              | -                                                                                                                                                                                                     |
|                                                              |     **Rg1 Line VCompound**                                                                                                                                                                              |
|                                                              |                                                                                                                                                                                                                   |
|                                                              |        *                                                                                                                                                                                                                |
|                                                              |                                                                                                                                                                                                                      |
|                                                              | -                                                                                                                                                                                                     |
|                                                              |     **Rg NLine HCompound**                                                                                                                                                                              |
|                                                              |                                                                                                                                                                                                                   |
|                                                              |        *                                                                                                                                                                                                                |
|                                                              |                                                                                                                                                                                                                      |
|                                                              | -                                                                                                                                                                                                     |
|                                                              |     **Rg NLine VCompound**                                                                                                                                                                              |
|                                                              |                                                                                                                                                                                                                   |
|                                                              |        *                                                                                                                                                                                                                |
|                                                              |                                                                                                                                                                                                                      |
|                                                              | -                                                                                                                                                                                                     |
|                                                              |     **Source**                                                                                                                                                                                          |
|                                                              |                                                                                                                                                                                                                   |
|                                                              |        * the object being projected                                                                                                                                                                                     |
|                                                              |                                                                                                                                                                                                                      |
|                                                              | -                                                                                                                                                                                                     |
|                                                              |     **VCompound**                                                                                                                                                                                       |
|                                                              |                                                                                                                                                                                                                   |
|                                                              |        *                                                                                                                                                                                                                |
+++


{{Drawing Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Drawing](Drawing_Workbench.md) > Drawing ProjectShape/en
