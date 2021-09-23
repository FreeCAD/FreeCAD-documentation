---
- GuiCommand:/ru
   Name:Part_Sphere
   Name/ru:Сфера
   MenuLocation:Деталь → Примитивы → Сфера
   Workbenches:[Part(Деталь)](Part_Workbench/ru.md)
   SeeAlso:[Создать примитивы](Part_Primitives/ru.md)
---

# Part Sphere/ru

## Описание

Создаёт простую параметрическую сферу с параметрами положение (position), угол1(angle1), угол2(angle2), угол3(angle3) и радиус(radius).

<img alt="" src=images/SimpleSphere.jpg  style="width:400px;">

## Применение

1.  Переключитесь на <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [верстак Part](Part_Workbench.md)
2.  Существует несколько способов вызова команды:
    -   Нажмите на иконку сферы **<img src="images/Part_Sphere.svg" width=16px>Сфера** на панели инструментов.
    -   Выберите из меню **Деталь → Примитивы → <img src="images/Part_Sphere.svg" width=16px> Сфера**.

**Результат:** Будет создана сфера с центром в начале системы координат (точка 0,0,0). Угловые параметры позволяют сделать часть сферы вместо полной сферы (по умолчанию они установлены на 360°).

The properties of the object can be edited, either in the [Property editor](Property_editor.md) or by double-clicking the object in the [Tree view](Tree_view.md).

## Свойства

### Данные


{{TitleProperty|Sphere}}

-    **Radius:**Radius of the sphere

-    **Angle 1:**1nd angle to cut / define the sphere

-    **Angle 2:**2nd angle to cut / define the sphere

-    **Angle 3:**3rd angle to cut / define the sphere

Поскольку довольно трудно объяснить смысл параметров угол 1, угол 2, угол 3, на рисунке ниже дано объяснение этих параметров со следующими значениями: угол 1 = -45°, угол 2 = 45° и угол 3= 90°.

<img alt="" src=images/SphereCutThreeAngles.jpg  style="width:400px;">

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Sphere/ru
