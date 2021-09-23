---
- GuiCommand:Addon/ru
   Name:BIM Library
   Name/ru:BIM Library
   MenuLocation:3D Modeling → Library
   Workbenches:<img src="images/IFC.svg" width=16px> [BIM](BIM_Workbench/ru.md)
   Addon:BIM
   SeeAlso:[Arch Equipment](Arch_Equipment/ru.md)
---

# BIM Library/ru

## Описание

Инструмент «Библиотека BIM» позволяет разместить в текущей модели объект из [FreeCAD Parts Library](Parts_Library.md), который должен быть установлен с помощью <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Addon Manager](Addon_Manager.md), чтобы этот инструмент был доступен.

<img alt="" src=images/BIM_Library_screenshot.png  style="width:800px;"> 
*Выше: Смотрите диалог '''Library browser''' [панели задач](Task_panel/ru.md) слева*

## Применение

1.  Нажмите кнопку **<img src="images/BIM_Library.png" width=16px> [BIM Library](BIM_Library/ru.md)
**

    :   Result: In the [Combo view](Combo_view.md) → [Task panel](Task_panel.md) a dialog titled **Library browser** will display
2.  Щелкните файл в браузере библиотеки
3.  Дважды щелкните его или нажмите кнопку **Insert**
4.  Щелкните точку в [трехмерном виде](3D_view/ru.md) или введите координату вручную, чтобы поместить объект

## Опции

-   Поддерживаются файлы [FCStd](FCStd/ru.md), [STEP](STEP/ru.md) и [BREP](BREP/ru.md). Доступны для размещения только файлы STEP и BREP. Файлы FCStd не позволят вам выбрать место размещения, так как они могут состоять из сложной серии объектов со значительными позициями. При выборе файла FCStd его содержимое будет вставлено в позицию, определенную в файле.
-   Объекты STEP и BREP вставляются как <img alt="Arch Equipment" src=images/Arch_Equipment.svg  style="width:24px;"> [Equipment](Arch_Equipment/ru.md), без отдельной формы основания. Добавление базовой формы к этим объектам впоследствии уничтожит их текущую форму.
-   При размещении объекта вы можете выбрать их точку вставки между оригинальной (точкой (`0,0,0`), определенной в файле), верхней, средней, нижней и левой, центральной и правой.
-   Библиотека может работать в автономном режиме, в этом случае она зависит от устанавливаемой надстройки библиотеки компонентов (и обновляется пользователем), или в сети, и в этом случае она просматривается непосредственно с [репозитория Git библиотеки Parts](https://github.com/FreeCAD/FreeCAD-library) и позволяет скачивать прямо оттуда.


 

[Category:BIM](Category:BIM.md)

---
[documentation index](../README.md) > [BIM](Category:BIM.md) > BIM Library/ru
