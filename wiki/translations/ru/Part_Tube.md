---
- GuiCommand:/ru
   Name:Part_Tube
   Name/ru:Создать трубу
   MenuLocation:Деталь → Примитивы → Создать трубу
   Workbenches:[Part(Деталь)](Part_Workbench/ru.md)
   Version:0.19
   SeeAlso:[Создать примитивы](Part_CreatePrimitives/ru.md)
---

# Part Tube/ru

## Описание

Команда Создать Трубу вставляет трубку в активный документ. Труба геометрически рассматривается как вырез меньшего цилиндра из большего. По умолчанию команда создаст трубку высотой 10 мм с наружным радиусом 5 мм и внутренним радиусом 2 мм. Эти параметры могут быть изменены после добавления объекта.

![Трубка на снимке экрана](images/Part_Tube-screenshot.png )

## Применение


<div class="mw-translate-fuzzy">

Трубу можно создать следующими способами:

-   нажмите кнопку **<img src="images/Part_Tube.svg" width=16px> '''Труба'''** на панели задач
-   используйте меню **Деталь → Примитивы → Создать трубу**


</div>


<div class="mw-translate-fuzzy">

Для редактирования трубы

-   используйте один из способов
    -   выберите её в древе проекта и сделайте двойной щелчок мышью
    -   отредактируйте параметры в открывшемся диалоговом окне
-   или используйте [ редактор свойств](Property_editor/ru.md) для изменения параметров


</div>

## Свойства


<div class="mw-translate-fuzzy">

-   Через [Редактор Свойств](Property_editor/ru.md):
    -   **Высота (Height):** Установите высоту (по умолчанию 10 мм).
    -   **Внутренний Радиус (Inner Radius):** Установите внутренний радиус (по умолчанию 2 мм).
    -   **Внешний Радиус (Outer Radius):** Установите внешний радиус (по умолчанию 5 мм).
    -   **Расположение (Placement):** Задаёт ориентацию и положение описанного Короба в трёхмерном пространстве. Смотри [Placement/Расположение](Placement/ru.md). Ориентиром служит левый передний нижний угол короба.
    -   **Label (Ярлык):** Ярлык это имя, присвоенное для операции. Вы можете его изменить в любое время.


</div>

## Scripting

A Part Tube can be created using the following function:


```python
tube = FreeCAD.ActiveDocument.addObject("Part::Tube", "myTube")
```

-   Where {{Incode|"myTube"}} is the name for the object.
-   The function returns the newly created object.

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Tube/ru
