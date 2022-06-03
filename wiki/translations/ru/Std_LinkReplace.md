---
- GuiCommand   *
   Name   *Std LinkReplace
   MenuLocation   *None
   Workbenches   *All
   Version   *0.19
   SeeAlso   *[Std LinkMake](Std_LinkMake.md), [Std LinkMakeRelative](Std_LinkMakeRelative.md), [Std LinkUnlink](Std_LinkUnlink.md)
---

# Std LinkReplace/ru

## Описание


**[<img src=images/Std_LinkReplace.svg style="width   *16px"> [Std LinkReplace](Std_LinkReplace.md)**

replaces an object that is inside another for an [App Link](App_Link.md) version of the former.

This operation acts on the \"children\" of a \"parent\" object as seen in the [tree view](tree_view.md). For example, given two objects (A and B) that participate in a **[<img src=images/Part_Boolean.svg style="width   *16px"> [Part Boolean](Part_Boolean.md)** operation, say, C = A + B, the A object can be replaced by a Link, so that C = A_link + B.

This operation can be done to replace nested objects that are in a complex [assembly](assembly.md) for a Link, which may be more efficient if that nested object is used many times in different sub-assemblies. The inverse operation is **[<img src=images/Std_LinkUnlink.svg style="width   *16px"> [Std LinkUnlink](Std_LinkUnlink.md)**. To create a generic Link see **[<img src=images/Std_LinkMake.svg style="width   *16px"> [Std LinkMake](Std_LinkMake.md)**.

## Применение

1.  Make sure you have one object that is inside another one. For example, consider that a **[<img src=images/Part_Fuse.svg style="width   *16px"> [Part Fuse](Part_Fuse.md)** was used with two previously created objects, a **[<img src=images/Part_Sphere.svg style="width   *16px"> [Part Sphere](Part_Sphere.md)** and a **[<img src=images/Part_Cylinder.svg style="width   *16px"> [Part Cylinder](Part_Cylinder.md)**.
2.  Select the <img alt="" src=images/Tree_Part_Sphere_Parametric.svg  style="width   *16px;"> [Sphere](Part_Sphere.md) in the [tree view](tree_view.md).
3.  Press **[<img src=images/Std_LinkReplace.svg style="width   *16px"> [Replace with link](Std_LinkReplace.md)**.

The original <img alt="" src=images/Tree_Part_Sphere_Parametric.svg  style="width   *16px;"> [Sphere](Part_Sphere.md) must now be outside the **[<img src=images/Part_Fuse.svg style="width   *16px"> [Part Fuse](Part_Fuse.md)**, and inside there must be a Link instead (a small overlay arrow is shown in the icon).

![](images/Std_Link_tree_replace_fuse_1_example.png ) ![](images/Std_Link_tree_replace_fuse_2_example.png )



*An object inside another one is replaced by a Link; the Link is now inside, and the real object is placed outside.*

This can also be done with objects contained inside {{button|[<img src=images/Std_Part.svg style="width   *16px"> [Std Parts](Std_Part.md)}} and {{button|[<img src=images/Std_Group.svg style="width   *16px"> [Std Groups](Std_Group.md)}}.

![](images/Std_Link_tree_replace_part_1_examples.png ) ![](images/Std_Link_tree_replace_part_2_examples.png )



*An object inside a container is replaced by a Link; the Link is now inside, and the real object is placed outside.*

## Свойства

Данная команда создает новый [App Link](App_Link/ru.md); его свойства описанны на странице команды **[<img src=images/Std_LinkMake.svg style="width   *16px"> ["Создать ссылку"](Std_LinkMake/ru.md)**.





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std LinkReplace/ru
