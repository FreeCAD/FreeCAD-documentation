---
 GuiCommand:
   Name/ru: Создать преобразованную копию
   Name: Part_TransformedCopy
   MenuLocation: Деталь , Создать копию , Создать преобразованную копию
   Workbenches: Part_Workbench/ru
   Version: 0.19
   SeeAlso: Part_SimpleCopy/ru, Part_ElementCopy/ru, Part_RefineShape/ru
---

# Part TransformedCopy/ru


</div>



## Описание

The <img alt="" src=images/Part_TransformedCopy.svg  style="width:24px;"> **Part TransformedCopy** command creates non-parametric copies of objects. It is intended for objects nested in containers.

The **Placement** of the copies is adjusted, accounting for the placement of the container(s), so that their position and rotation relative to the global coordinate system is the same as that of the original objects. If the selected objects are not nested, or nested in a container with a default placement, this command produces the same results as [Part SimpleCopy](Part_SimpleCopy.md).



## Применение

1.  Select one or more objects.
2.  Select the **Part → Create a copy → <img src="images/Part_TransformedCopy.svg" width=16px> Create transformed copy** option from the menu.



## Свойства

See also: [Property editor](Property_editor.md).

The created objects are [Part Feature](Part_Feature.md) objects with no additional properties.





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part TransformedCopy/ru
