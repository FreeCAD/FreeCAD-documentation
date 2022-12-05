---
- GuiCommand:/ru
   Name:Part CrossSections
   Name/ru:Поперечные сечения
   MenuLocation:Деталь → Поперечные сечения
   Workbenches:[Верстак Part](Part_Workbench/ru.md)
   SeeAlso:[Разделить](Part_Section/ru.md)
---

# Part CrossSections/ru

## Описание

The **Cross-sections** utility creates one or more cross-sections through the selected shape, parallel to one of the default global planes (XY, XZ or YZ).

## Применение

1.  Select a shape.
2.  Press the **[24px|link=Part_CrossSections](File:Part_CrossSections.svg.md) '''Cross-sections'''** button.
3.  Define the guiding plane.
4.  Define the position (height of the cross-section).
5.  Optionally, check **Sections** to create more than one cross-section:
    -   Checking *On both sides* will distribute the cross-sections on each side of the guiding plane location.
    -   Set the count.
6.  Press **OK**.

## Notes

-   [App Link](App_Link.md) objects linked to the appropriate object types and [App Part](App_Part.md) containers with the appropriate visible objects inside can also be used as source objects. <small>(v0.20)</small> 
-   The resulting object is not parametric, that is it is not linked to the original shape.
-   A single object is created, even with more than one cross-section.

## Пример

![Select an object](images/SectionCross1.png )

![Dialog window](images/SectionCross2.png )

![Result](images/SectionCross3.png )



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part CrossSections/ru
