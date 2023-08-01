---
- GuiCommand:/ru
   Name:Std HideSelection
   Name/ru:Std HideSelection
   Empty:1
   MenuLocation:Вид → Видимость → Скрыть выделенные
   Workbenches:All
   SeeAlso:[Std ToggleVisibility](Std_ToggleVisibility/ru.md), [Std ShowSelection](Std_ShowSelection/ru.md), [Std ToggleObjects](Std_ToggleObjects/ru.md), [Std ShowObjects](Std_ShowObjects/ru.md), [Std HideObjects](Std_HideObjects/ru.md)
---

# Std HideSelection/ru


</div>

## Описание

Команда **Скрыть выделенное** скрывает выбранные объекты [3D вида](3D_view/ru.md).

## Применение

1.  Select one or more objects.
2.  There are several ways to invoke the command:
    -   Select the **View → Visibility → <img src="images/Std_HideSelection.svg" width=16px> Hide selection** option from the menu.
    -   Select the **<img src="images/Std_HideSelection.svg" width=16px> Hide selection** option from the [Tree view](Tree_view.md) context menu. This option is not available in the [PartDesign Workbench](PartDesign_Workbench.md).

## Примечания

-   Невидимые объекты отображаются с серой меткой и серой иконкой в [ Древе проекта](Tree_view/ru.md).
-   Объекты, вложенные в [Деталь](Std_Part/ru.md) или [Ссылку](Std_LinkMake/ru.md) или в [Группу](Std_Group/ru.md) или группу ссылок, и [feature](PartDesign_Feature/ru.md) [Тела PartDesign](PartDesign_Body/ru.md) будут видны в [3D виде](3D_view/ru.md), только если их родитель также виден. Это означает, что объект в теле конструкции детали, вложенный в Деталь, будет виден в 3D-виде только в том случае, если сам объект, тело конструкции детали и деталь видны. И если Деталь, в свою очередь, вложена в другую Деталь, то этот последний объект также должен быть виден.
-   Если видимость [Группы](Std_Group/ru.md) (или объекта, производного от него, например такого как [Arch BuildingPart](Arch_BuildingPart/ru.md)) изменена, видимость его вложенных объектов соответственно изменится. Но их видимость также может быть изменена независимо друг от друга.
-   Действие этой команды не может быть отменено с помощью команды [ \"Отменить\"](Std_Undo.md).
-   Видимость объекта также может быть изменена с помощью связанного с ним свойства **Visibility** в [Редакторе свойств](Property_editor/ru.md) или [Комбо панели](Combo_view/ru.md).

## Scripting


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).

For a scripting example see [Std ToggleVisibility](Std_ToggleVisibility.md).





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std HideSelection/ru
