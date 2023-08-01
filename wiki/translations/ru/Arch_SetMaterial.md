---
- GuiCommand:
   Name: Arch SetMaterial
   Name/ru: Arch SetMaterial
   MenuLocation: Arch - Инструменты материала - Материал
   Workbenches: [Arch](Arch_Workbench/ru.md), [BIM](BIM_Workbench/ru.md)
   Shortcut: **M** **T**
   SeeAlso: [Arch CompSetMaterial](Arch_CompSetMaterial/ru.md), [Arch MultiMaterial](Arch_MultiMaterial/ru.md)
---

# Arch SetMaterial/ru


</div>

## Описание


<div class="mw-translate-fuzzy">

Инструмент Материал создает и привязывает [материал](Material.md) к активному документу, и привязывает его свойства к [Архитектурному](Arch_Workbench/ru.md) объекту. Материалы могут использовать все свойства определенного материала и контролировать цвет объекта, к которому он прикреплен. Материалы хранятся в папке **Materials** в активном документе.


</div>

![](images/Arch_materials_01.jpg )

## Применение


<div class="mw-translate-fuzzy">

1.  При желании выберите один или несколько объектов, которым вы хотите задать новый материал
2.  Вызовите команду одним из способов
    -   Нажмите кнопку **<img src="images/Arch_SetMaterial.svg" width=16px> [Material](Arch_SetMaterial.md)** на панели инструментов
    -   Используйте сочетание клавиш **M** then **T**.
    -   Используйте пункт главного меню **Arch → Инструменты материала → Материал**.
3.  Загрузите предварительно заданный материал или создайте новый, заполнив поля.
4.  Нажмите **OK**.


</div>

## Опции

-   При создании нового материала панель задач позволяет вам установить различные параметры:

![](images/Arch_materials_02.jpg )


<div class="mw-translate-fuzzy">

-   **Choose preset**: Выберите один из предустановленных материалов, который будет использоваться как есть, или будет адаптирован путем изменения полей ниже
-   **Name**: Укажите имя материала
-   **Edit button**: Открывает текущий материал в FreeCAD\'s [Material editor](FEM_MaterialEditor.md), который позволяет редактировать многие дополнительные свойства и добавлять собственные параметры
-   **Description**: Более подробное описание материала
-   **Color**: Отображаемый цвет материала, который будет применяться ко всем объектам, использующим этот материал
-   **Section Color**: Цвет отображения материала, который будет применяться на страницах TechDraw, когда объект с этим материалом будет вырезан, а для свойства «Отображать материалы» содержащей его плоскости секитона установлено значение True.
-   **Code**: Код и номер спецификации, например [Masterformat](https://en.wikipedia.org/wiki/MasterFormat) или [Omniclass](http://www.omniclass.org/).
-   **Code browser button**: Пока не реализована - позволит открыть ссылку в веб-браузере
-   **URL**: Ссылка, где можно найти дополнительную информацию о материале
-   **URL button**:Открывает ссылку в веб-браузере


</div>

## Relation to IFC 

This roughly corresponds to [IfcMaterial](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/link/ifcmaterial.htm).


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch SetMaterial/ru
