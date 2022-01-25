---
- GuiCommand:
   Name:Material editor
   Name/ru:Material editor
   Icon:Arch_Material_Group.svg
   MenuLocation:Model → Material → Material editor
   Workbenches:[FEM](FEM_Workbench/ru.md), [Arch](Arch_Workbench/ru.md)
   Shortcut:
   Version:0.18
   SeeAlso:[Material](Material/ru.md), [Arch SetMaterial](Arch_SetMaterial/ru.md), [FEM tutorial](FEM_tutorial/ru.md)
---

# Material editor/ru


</div>

## Описание


<div class="mw-translate-fuzzy">

Редактор материалов позволяет редактировать и сохранять информацию в объекте [материала FreeCAD](Material/ru.md). Сейчас эти материалы используются в верстаках **<img src="images/Workbench_FEM.svg" width=24px> [FEM](FEM_Workbench/ru.md)** и **<img src="images/Workbench_Arch.svg" width=24px> [Arch](Arch_Workbench/ru.md)**.


</div>

![](images/Material_editor.jpg )

## Использование

Редактор материалов сейчас может быть доступен через:


<div class="mw-translate-fuzzy">

1.  <img alt="" src=images/Workbench_Arch.svg  style="width:32px;"> [Верстак Arch](Arch_Workbench/ru.md)
    -   Кнопку <img alt="" src=images/Arch_SetMaterial.svg  style="width:32px;"> [Set Material](Arch_SetMaterial/ru.md) панели создания [нового материала](Arch_SetMaterial/ru.md) в [верстаке Arch](Arch_Workbench/ru.md)
    -   Меню **Arch → Set material...**
2.  <img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> [Верстак FEM](FEM_Workbench/ru.md)
    -   Иконку <img alt="" src=images/Arch_Material_Group.svg  style="width:32px;"> [Material editor](Material_editor/ru.md)
    -   Меню **Models → Material → Material editor**
3.  Или через Python (см. ниже секцию [Scripting](#Scripting.md))


</div>

## Опции

-   **Browser button**: Открывает содержимое ссылки на параметр в браузере

-   **Material card**: Позволяет для заполнения полей выбрать предустановки

-    **Open**: Открывает файл .FCMat

-    **Save as**: Сохраняет содержимое редактора в новом файле .FCMat

-   **Preview**: Ещё не работает

-   **Properties editor**: Позволяет редактировать содержимое параметров материала

-    **Add property**: Позволяет дать новый пользовательских параметр материала

-    **Delete property**: Удаляет выбранный параметр. Может быть удалён лишь пользовательский параметр

Примечание:

-   Кнопки **OK** и **Cancel** имеют тот же эффект, если редактор материалов не используется для прямого редактирования параметров материала существующего объекта.

## Scripting


```python
import MaterialEditor
MaterialEditor.openEditor()
```


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > [Arch](Category_Arch.md) > [Material](Material_Workbench.md) > Material editor/ru
