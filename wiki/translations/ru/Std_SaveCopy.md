---
- GuiCommand:/ru
   Name:Std_SaveCopy
   Name/ru:Сохранить копию...
   MenuLocation:Файл → Сохранить копию...
   Workbenches:Все
   SeeAlso:[Сохранить](Std_Save/ru.md),<br> [Сохранить как...](Std_SaveAs/ru.md) 
---

# Std SaveCopy/ru

## Описание

Команда **Сохранить копию\...** сохраняет копию активного документа под новым названием.

## Применение

1.  Выберите пункт главного меню **Файл → <img src="images/Std_SaveCopy.svg" width=16px> Сохранить копию...**.
2.  Введите имя файла в появившемся окне.
3.  Нажмите кнопку **Сохранить**.

## Опции

-   Нажмите **Esc** или кнопку **Отмена**, чтобы прервать выполнение команды.

## Настройки

-   Путь к последнему файлу к которому была применена данная команда сохраняется в параметр: **Инструменты → Редактор параметров... → BaseApp → Preferences → General → FileOpenSavePath**.

## Программирование


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).

Для сохранения копии документа используйте метод `saveCopy` объекта document.


```python
import FreeCAD
from pathlib import Path

# The folder and filename we will use:
fld = 'D:/testfiles/'
fnm = fld + 'testCopy.FCStd'

# Make sure fld exists:
Path(fld).mkdir(parents=True, exist_ok=True)

doc = FreeCAD.newDocument()
doc.saveCopy(fnm)
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std SaveCopy/ru
