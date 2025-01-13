---
 GuiCommand:
   Name: Std_New
   Name/ru: Создать
   MenuLocation: Файл , Создать
   Workbenches: All
   Shortcut: **Ctrl**+**N**
   SeeAlso: Std_Open/ru,<br>Std_Import/ru
---

# Std New/ru



## Описание

Команда **Создать** создаёт новый пустой документ и делает его активным.



## Применение


<div class="mw-translate-fuzzy">

1.  Существует несколько способов вызвать команду:
    -   Нажатием кнопки **<img src="images/Std_New.svg" width=16px> [Создать](Std_New/ru.md)** на панели инструментов.
    -   Через пункт меню: **Файл → <img src="images/Std_New.svg" width=16px> Создать**.
    -   Используя комбинацию клавиш клавиатуры: **Ctrl**+**N**.


</div>



## Настройки

See also: [Preferences Editor](Preferences_Editor.md).


<div class="mw-translate-fuzzy">

-   FreeCAD создает новый пустой документ при старте, при условии, что параметр **Инструменты → Редактор параметров... → BaseApp → Preferences → Document → CreateNewDoc** установлен как `True`. Данный параметр может быть изменен через [Редактор настроек](Preferences_Editor/ru#Документ.md).
-   Некоторые свойства документа, например такие как: имена авторов, названия компаний и информация о лицензии могут быть предварительно указаны в [Редакторе настроек](Preferences_Editor/ru#Документ.md).


</div>



## Свойства

See also: [Property editor](Property_editor.md).

Большинство свойств также можно изменить в диалоговом окне [\"Информация о проекте\...\" (команда Std ProjectInfo)](Std_ProjectInfo/ru.md).

### Data


{{TitleProperty|Base}}


<div class="mw-translate-fuzzy">

-    **Comment**: Может содержать комментарий.

-    **Company**: Название компании. **Может быть установлено предварительно**.

-    **Created By**: Инициалы автора создателя. **Может быть установлено предварительно**.

-    **Creation Date**: Автоматическая временная метка. **Нередактируемое значение**.

-    **File Name**: Полный путь к файлу. Поле будет пустым, если документ не был ещё сохранен. **Нередактируемое значение**.

-    **Id**: Не реализовано на данный момент.

-    **Label**: Название которое отображается в [Древе проекта](Tree_view/ru.md). По умолчанию используется имя документа.

-    **Last Modified By**: Инициалы автора внесшего правки. **Может быть установлено предварительно**.

-    **Last Modified Date**: Автоматическая временная метка (время последней правки). **Нередактируемое значение**.

-    **License**: Тип лицензии. **Может быть установлено предварительно**.

-    **License URL**: URL лицензии. **Может быть установлено предварительно**.

-    **Show Hidden**: Если параметр равен True, то элементы, которые были скрыты в [Древе проекта](Tree_view/ru.md) все равно будут отображаться. Сокрытие элементов в дереве проекта может быть полезно при работе с большими моделями.

-    **Tip**: Не реализовано на данный момент.

-    **Tip Name**: Не реализовано на данный момент.

-    **Transient Dir**: Путь временной папки, используемой для восстановления данных. **Нередактируемое значение**.


</div>



## Программирование


<div class="mw-translate-fuzzy">


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).


</div>

Для создания нового документа используйте `newDocument([name], [hidden<nowiki>=</nowiki>False])` метод приложения FreeCAD. Название документа должно быть уникальным, что проверяется автоматически. Если имя не будет указано, документу будет присвоено название \"Untitled\". Если `hidden<nowiki>=</nowiki>True`, тогда созданный документ не будет отображаться в графическом интерфейсе и его вкладка так же не будет создана.


```python
import FreeCAD
from pathlib import Path

# The folder and filename we will use:
fld = 'D:/testfiles/'
fnm = fld + 'test.FCStd'

# Make sure fld exists:
Path(fld).mkdir(parents=True, exist_ok=True)

doc = FreeCAD.newDocument()
doc.saveAs(fnm)

FreeCAD.closeDocument(doc.Name)

doc = FreeCAD.open(fnm)
doc.save()

FreeCAD.closeDocument(doc.Name)
```





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std New/ru
