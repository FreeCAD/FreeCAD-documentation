---
- GuiCommand:/ru
   Name:Part_Plane
   Name/ru:Плоскость
   MenuLocation:[Деталь](Part_Workbench/ru.md) → [Создать примитивы...](Part_Primitives/ru.md) → Плоскость
   Workbenches:[Part(Деталь)](Part_Workbench/ru.md)
   SeeAlso:[Создать примитивы...](Part_Primitives/ru.md)
---

# Part Plane/ru

## Описание

Создаёт простую параметрическую плоскость 10х10мм с параметрами положение, длина и ширина. По умолчанию плоскость расположена в начале координат (0,0,0).

![](images/PartPlane.png )

## Применение

По умолчанию плоскость создаётся с нижним левым углом расположенным в начале координат`0,0,0`. Для изменения этих параметров, откройте раздел Расположение и введите нужные значения в соответствующие поля ввода или нажмите на кнопку [3D-вида](3D_view/ru.md) и выберите точку, координаты точки берутся из полей. В меню Направление вы также можете определить стандартный вектор (X, Y или Z), перпендикулярный плоскости, или нажать кнопку Определяемый Пользователем \... чтобы открыть диалоговое окно , позволяющее установить другую несущую направляющую (например, направление 1.0, -1 создаст плоскость, наклонённую на 45° относительно осей X и Z).


<div class="mw-translate-fuzzy">

Свойства могут быть изменены позже в **Комбо панели → Данные**, после выбора элемента.


</div>

## Свойства

### Данные


{{TitleProperty|Основные}}

-    **Label**: String name of the object, defaults to \'Plane\'. User may rename it.

-    **Placement**: Placement of feature is defined by below angle, axis and position.

-    **Angle**: Angle of rotation relative to the below axis.

-    **Axis**: Defines the axis of rotation plane: X, Y, or Z. Defaults to Z axis, Z = 1

-    **Position**: Position X, Y, Z, relative to the origin 0, 0, 0.


{{TitleProperty|Plane}}

-    **Length**: Length is the dimension along the X axis The default value is 10 mm

-    **Width**: Width is the size of the Y-axis The default value is 10 mm

### Вид

You have the standard properties view.

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Plane/ru
