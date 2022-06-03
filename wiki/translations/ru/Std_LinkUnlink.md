---
- GuiCommand   *
   Name   *Std LinkUnlink
   MenuLocation   *None
   Workbenches   *All
   Version   *0.19
   SeeAlso   *[Std LinkMake](Std_LinkMake.md), [Std LinkMakeRelative](Std_LinkMakeRelative.md), [Std LinkReplace](Std_LinkReplace.md)
---

# Std LinkUnlink/ru

## Описание


**[<img src=images/Std_LinkUnlink.svg style="width   *16px"> [Std LinkUnlink](Std_LinkUnlink.md)**

is essentially the opposite operation to **[<img src=images/Std_LinkReplace.svg style="width   *16px"> [Std LinkReplace](Std_LinkReplace.md)**.

This operation is used to remove a Link from a container like **[<img src=images/Std_Part.svg style="width   *16px"> [Std Part](Std_Part.md)**, and instead place the real object inside.

## Применение

1.  Make sure you have a Link that is inside a container, for example, a Link to a **[<img src=images/Part_Sphere.svg style="width   *16px"> [Part Sphere](Part_Sphere.md)** inside a **[<img src=images/Std_Part.svg style="width   *16px"> [Std Part](Std_Part.md)**.
2.  Select the internal Link in the [tree view](tree_view.md).
3.  Press **[<img src=images/Std_LinkUnlink.svg style="width   *16px"> [Unlink](Std_LinkUnlink.md)**.

The original <img alt="" src=images/Tree_Part_Sphere_Parametric.svg  style="width   *16px;"> [Sphere](Part_Sphere.md) must now be inside the **[<img src=images/Std_Part.svg style="width   *16px"> [Std Part](Std_Part.md)**, and the Link must be outside. Now this Link can be deleted if it\'s no longer needed, and it won\'t break the container.

![](images/Std_Link_tree_replace_1_example.png ) ![](images/Std_Link_tree_unlink_1_example.png )



*A Link inside another object is unlinked, and the real object is placed inside instead.*

![](images/Std_Link_tree_replace_2_example.png ) ![](images/Std_Link_tree_unlink_2_example.png )



*A Link inside a group is unlinked, and the real object is placed inside instead.*





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std LinkUnlink/ru
