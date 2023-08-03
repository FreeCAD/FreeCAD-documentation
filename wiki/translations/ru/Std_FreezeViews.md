---
 GuiCommand:
   Name: Std FreezeViews
   Name/ru: Std FreezeViews
   Empty: 1
   MenuLocation: Вид , Положения камеры , ...
   Workbenches: All
   SeeAlso: Std_ViewIvIssueCamPos/ru
---

# Std FreezeViews/ru


</div>



## Введение

FreeCAD имеет возможность сохранять положение камеры текущего активного вида. Положения записываются в специальный список в виде пунктов меню, который ограничен 50-ю значениями. Пункты меню, относящиеся к возможности сохранения состояния камеры, можно найти в подменю **Вид → Положение камеры**. Положение камеры не сохраняется в самом документе и, если они не были сохранены с помощью пункта меню **[Сохранить в файл\...](#Save_views.md)**, то они будут потеряны после закрытия приложения FreeCAD.



## Сохранить в файл\... 



### Описание

Пункт меню **Сохранить в файл\...** сохраняет все положения камеры из списка в файл с \*.cam расширением.



### Применение

1.  To use this option one or more frozen views must exist. A frozen view is created with the **[Freeze view](#Freeze_view.md)** menu option.
2.  Select the **View → Freeze display → Save views...** option from the menu.
3.  Enter a filename in the dialog box.
4.  Press the **Save** button.



### Опции

-   Нажмите клавишу **Esc** или кнопку **Отмена**, чтобы прервать выполнение команды.



## Загрузить из файла\... 



### Описание 

Пункт меню **Загрузить из файла\...** загружает положения камер из файла с \*.cam расширением в список, при этом все значения, которые были до этого в списке будут утеряны.



### Применение 

1.  Select the **View → Freeze display → Load views...** option from the menu.
2.  Press the **Yes** button in the Restore views dialog box to confirm you want to lose all existing frozen views.
3.  Select a file.
4.  Press the **Open** button.



### Опции 

-   If the Restore views dialog box is displayed: press **Esc** or the **No** button to abort the command.
-   If the file dialog box is displayed: press **Esc** or the **Cancel** button to abort the command.



## Запомнить



### Описание 

Пункт меню **Запомнить** сохраняет текущее состояние камеры (направление, положение, масштаб и т.д.) активного [3D вида](3D_view/ru.md) в список в виде нового пункта меню. Список положений камеры может содержать в себе до 50-ти записей.



### Применение 

1.  There are several ways to invoke this option:
    -   Select the **View → Freeze display → Freeze view** option from the menu.
    -   Use the keyboard shortcut: **Shift**+**F**.
2.  The new frozen view can be selected in the **View → Freeze display** submenu.



## Отчистить список 



### Описание 

The **Clear views** menu option deletes all existing frozen views.



### Применение 

1.  Select the **View → Freeze display → Clear views** option from the menu.

## Restore view 



### Описание 

For each frozen view a **Restore view** option is added with which it can be restored. The options are numbered: **Restore view 1** - **Restore view 50**.



### Применение 

1.  There are several ways to invoke this option:
    -   Select the correct **View → Freeze display → Restore view** option from the menu.
    -   For the first 9 frozen views: use the keyboard shortcut: **Ctrl**+**1** - **Ctrl**+**9**.


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std FreezeViews/ru
