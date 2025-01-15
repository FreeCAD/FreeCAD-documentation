---
 GuiCommand:
   Name/ru: Отправить в консоль Python
   Name: Std_SendToPythonConsole
   MenuLocation: Правка , Отправить в консоль Python
   Workbenches: Все
   Shortcut: **Ctrl**+**Shift**+**P**
   Version: 0.19
---

# Std SendToPythonConsole/ru



## Описание

The **Std SendToPythonConsole** command creates variables in the [Python console](Python_console.md) referencing a selected object and its selected subshapes, along with some other useful references. The variables and the code involved can be used in the development of Python code.

В зависимости от выбранного объекта и входящих в его состав выбранных форм, создаются следующие переменные:

+++
| Название переменной | Пояснение                                                                                                                                           |
+=====================+=====================================================================================================================================================+
|      | Документ в котором содержится вбранный объект                                                                                                       |
| {{Incode|doc}}      |                                                                                                                                                     |
|                  |                                                                                                                                                     |
+++
|      | Выбранный объект ссылки (создается только в том случае, если выбранный объект является ссылкой)                                                     |
| {{Incode|lnk}}      |                                                                                                                                                     |
|                  |                                                                                                                                                     |
+++
|      | В зависимости от выбранного объекта:                                                                                                                |
| {{Incode|obj}}      | Сам выбранный объект (если выбранный объект не является ссылкой)                                                                                    |
|                  | Связанный объект (если выбранный объект является ссылкой)                                                                                           |
+++
|      | Зависит от типа {{Incode|obj}}:                                                                                                       |
| {{Incode|shp}}      | {{Incode|Shape}} свойство {{Incode|obj}} (для объектов унаследованных от {{Incode|Part::Feature}} класса) |
|                  | {{Incode|Mesh}} свойство {{Incode|obj}} (для Mesh объектов)                                                             |
|                     | {{Incode|Points}} свойство {{Incode|obj}} (для Points объектов)                                                         |
+++
|      | Первая выбранная вложенная фигура (создается только в том случае, если выбрана хотя бы одна вложенная фигура)                                       |
| {{Incode|sub}}      |                                                                                                                                                     |
|                  |                                                                                                                                                     |
+++
|      | Список, содержащий все вложенные фигуры (создается только в том случае, если выбраны две или более вложенных фигур)                                 |
| {{Incode|subs}}     |                                                                                                                                                     |
|                  |                                                                                                                                                     |
+++

>>> ### Begin command Std_SendToPythonConsole
>>> try:
>>>     del(doc,lnk,obj,shp,sub,subs)
>>> except Exception:
>>>     pass
>>> 
>>> doc = App.getDocument("Unnamed")
>>> lnk = doc.getObject("Link")
>>> obj = lnk.getLinkedObject()
>>> shp = obj.Shape
>>> sub = obj.getSubObject("Edge10")
>>> subs = [obj.getSubObject("Edge10"),obj.getSubObject("Face3"),obj.getSubObject("Vertex5"),]
>>> ### End command Std_SendToPythonConsole



*Example output: an edge, a face, and a vertex of a [Link](Std_LinkMake.md) to a [Part Box](Part_Box.md) were selected*



## Применение

1.  Select a single object or one or more subshapes belonging to a single object.
2.  There are several ways to invoke the command:
    -   Select the **Edit → <img src="images/Std_SendToPythonConsole.svg" width=16px> Send to Python Console** option from the menu.
    -   Select the **<img src="images/Std_SendToPythonConsole.svg" width=16px> Send to Python Console** option from the [Tree view](Tree_view.md) context menu or [3D view](3D_view.md) context menu.
    -   Use the keyboard shortcut: **Ctrl**+**Shift**+**P**.
3.  If required the [Python console](Python_console.md) opens.
4.  The [Python console](Python_console.md) receives the keyboard focus.



## Примечания

-   Все ранее созданные переменные удаляются (перезаписываются новыми значениями) при каждом запуске команды.

-   If the selected object is a Link ({{Incode|App::Link}}) and the Linked object is derived from the {{Incode|Part::Feature}} class, the {{Incode|shp}} variable will be the shape of the Linked object. If the Link has been transformed or scaled and you want to access the scaled/transformed shape, you can do so with this code:

:   
    
```pythonlnk_shp = Part.getShape(lnk)```



---
⏵ [documentation index](../README.md) > Std SendToPythonConsole/ru
