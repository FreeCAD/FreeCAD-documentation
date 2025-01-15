---
 GuiCommand:
   Name/ru: Видимость
   Name: Std_ToggleVisibility
   MenuLocation: Вид , Видимость
   Workbenches: Все
   Shortcut: **Space**
   SeeAlso: Std_ShowSelection/ru, Std_HideSelection/ru, Std_ToggleObjects/ru, Std_ShowObjects/ru, Std_HideObjects/ru
---

# Std ToggleVisibility/ru



## Описание

Команда **Видимость** переключает видимость выделенных объектов в окне [трёхмерного вида](3D_view/ru.md).



## Применение


<div class="mw-translate-fuzzy">

1.  Выберите один или более чем один объект.
    -   Невидимые объекты могут быть выбраны в [древе проекта](Tree_view/ru.md).
    -   Будьте осторожны при использовании **Ctrl**+**A** для выделения всех объектов в древе проекта. Так как эта комбинация выделяет подэлементы [тел PartDesign](PartDesign_Body/ru.md) и объекты, используемые для [булевых операций в Part](Part_Boolean/ru.md). В большинстве случаев их надо оставлять невидимыми.
    -   Объекты, используемые для [булевых операций в Part](Part_Boolean/ru.md) так же выделяются при использовании **Ctrl**+**A** в окне трёхмерного вида.
2.  Есть несколько способов вызвать команду:
    -   Выбрать **Вид → <img src="images/Std_ToggleVisibility.svg" width=16px> Видимость** из меню.
    -   Выбрать **Вид → Видимость → <img src="images/Std_ToggleVisibility.svg" width=16px> Видимость** из меню.
    -   Выбрать **<img src="images/Std_ToggleVisibility.svg" width=16px> Видимость** из контекстного меню в древе проекта. Эта опция не доступна в [верстаке PartDesign](PartDesign_Workbench/ru.md).
    -   Выбрать **<img src="images/Std_ToggleVisibility.svg" width=16px> Видимость** из контекстного меню окна трёхмерного вида.
    -   Используя **пробел** на клавиатуре.


</div>



## Примечания


<div class="mw-translate-fuzzy">

-   Невидимые объекты отображаются с выделенной серым цветом меткой и выделенным серым цветом значком в [древовидном представлении](Tree_view/ru.md).
-   Объекты, вложенные в [деталь](Std_Part/ru.md), или [ссылку](Std_LinkMake/ru.md) на [группу](Std_Group/ru.md), или группу ссылок, а также [features](PartDesign_Feature/ru.md) [тела PartDesign](PartDesign_Body/ru.md) будут видны на 3D-видах только в том случае, если их родитель также виден. Это означает, что в PartDesign теле, вложенный в деталь Std, будет виден в 3D-виде только в том случае, если сам объект, тело дизайна детали и деталь Std являются видимыми. И если Std_Part, в свою очередь, вложена в другую часть Std_Part, то этот последний объект также должен быть виден.
-   Если видимость [группы](Std_Group/ru.md) (или производного от нее объекта, такого как [часть здания](Arch_BuildingPart/ru.md)) будет изменена, видимость ее вложенных объектов изменится соответствующим образом. Но их видимость также может быть изменена независимо.
-   Действие этих команд не может быть отменено через команду [Отменить](Std_Undo/ru.md).
-   Видимость объекта может быть изменена через соответствующее свойство **Visibility** в [редакторе свойств](Property_editor/ru.md) или [combo панель](Combo_view/ru.md).


</div>



## Программирование


<div class="mw-translate-fuzzy">


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).


</div>


<div class="mw-translate-fuzzy">

Используйте методы `show` и `hide` объектов для изменения их видимости.


</div>


```python
import FreeCADGui

obj = FreeCADGui.ActiveDocument.myObjectName

if obj.Visibility == True:
    obj.hide()
else:
    obj.show()

# Alternatively:
obj.Visibility = not obj.Visibility
```



---
⏵ [documentation index](../README.md) > Std ToggleVisibility/ru
