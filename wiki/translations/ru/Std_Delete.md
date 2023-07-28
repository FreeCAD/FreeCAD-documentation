---
- GuiCommand:/ru
   Name:Std_Delete
   Name/ru:Удалить
   MenuLocation:Правка → Удалить
   Workbenches:Все
   Shortcut:**Del**
---

# Std Delete/ru



## Описание

Команда **Удалить**, удаляет выбранные объекты.



## Применение

1.  Выберите один или несколько объектов.
2.  Существует несколько способов вызвать команду:
    -   Через пункт меню **Правка → <img src="images/Std_Delete.svg" width=16px> Удалить**.
    -   Через пункт **<img src="images/Std_Delete.svg" width=16px> Удалить** меню [древовидного представления](Tree_view/ru.md) или аналогичный пункт контекстного меню [3D вида](3D_view/ru.md).
    -   Нажатием клавиши клавиатуры: **Del**.



## Программирование


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).

Для удаления объекта используйте метод `removeObject` объекта document.


```python
import FreeCAD

FreeCAD.ActiveDocument.removeObject("myObjectName")
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std Delete/ru
