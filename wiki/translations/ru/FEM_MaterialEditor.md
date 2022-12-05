---
- GuiCommand:/ru
   Name/ru:Редактор материалов
   Name:FEM_MaterialEditor
   MenuLocation:Модель → Материалы → Редактор материалов
   Workbenches:[FEM](FEM_Workbench/ru.md), [Arch](Arch_Workbench/ru.md)
   Version:0.18
   SeeAlso:[Material/ru](Material/ru.md), [Arch SetMaterial](Arch_SetMaterial/ru.md), [FEM tutorial](FEM_tutorial/ru.md)
---

# FEM MaterialEditor/ru


</div>

## Описание


<div class="mw-translate-fuzzy">

Редактор материалов позволяет редактировать и сохранять информацию в объекте [материала FreeCAD](Material/ru.md). Эти материалы доступны для применения в верстаках **<img src="images/Workbench_FEM.svg" width=24px> [FEM](FEM_Workbench/ru.md)** и **<img src="images/Workbench_Arch.svg" width=24px> [Arch](Arch_Workbench/ru.md)**.


</div>

![](images/Material_editor.png )

## Применение

На текущий момент редактор материалов может быть доступен:

1.  <img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> В [верстаке Arch](Arch_Workbench/ru.md) через:
    -   Кнопку **<img src="images/Arch_SetMaterial.svg" width=16px> [Set Material](Arch_SetMaterial/ru.md)**.
    -   Меню **Arch → Material tools → <img src="images/Arch_SetMaterial.svg" width=16px> Material**.
2.  <img alt="" src=images/Workbench_FEM.svg  style="width:24px;"> В [верстаке FEM](FEM_Workbench/ru.md) через:
    -   Кнопку **<img src="images/FEM_MaterialEditor.svg" width=16px> [Material editor](FEM_MaterialEditor/ru.md)**.
    -   Меню **Models → Materials → <img src="images/FEM_MaterialEditor.svg" width=16px> Material editor**.

## Опции

-   **Browser button**: Открывает содержимое ссылки на параметр в браузере

-   **Material card**: Позволяет для заполнения полей выбрать предустановки

-    **Open**: Открывает файл .FCMat

-    **Save as**: Сохраняет содержимое редактора в новом файле .FCMat

-   **Preview**: Ещё не работает

-   **Properties editor**: Позволяет редактировать содержимое параметров материала

-    **Add property**: Позволяет дать новый пользовательских параметр материала

-    **Delete property**: Удаляет выбранный параметр. Может быть удалён лишь пользовательский параметр

## Notes

-   Кнопки **OK** и **Cancel** имеют тот же эффект, если редактор материалов не используется для прямого редактирования параметров материала существующего объекта.





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MaterialEditor/ru
