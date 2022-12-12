# FeaturePython methods/ru
{{TOCright}}

## Введение

Данная страница содержит справочные данные по доступным переопределяемым методам примененных в описаниях: [Create a FeaturePython object part I](Create_a_FeaturePython_object_part_I/ru.md) и [Программируемые объекты](Scripted_objects/ru.md).

## Основная ссылка 

Указанные ниже методы в \~ 99% случаев применяются опытными пользователями proxy классов Python.

++++
|                             | Вызывается во время перерасчета FeaturePython (или пересчета всего документа)    | Не вызывайте `recompute()` из этого метода (или любого метода, вызываемого из `execute()`), поскольку это вызовет повторный пересчет, что может привести к зацикливанию.                                                                                                                                                          |
| `execute(self, obj)`              |                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                 |
|                                         |                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                 |
++++
|                             | Вызывается перед тем, как значение свойства будет изменено                       |                                                                                                                                                                                                                                                                                                                                                                  |
| `onBeforeChange(self, obj, prop)` |                                                                                  | `prop`                                                                                                                                                                                                                                                                                                                                                                 |
|                                         |                                                                                  |                                                                                                                                                                                                                                                                                                                                                                              |
|                                            |                                                                                  | \- название изменяемого свойства, но не сам объект свойства. Изменение свойства не может быть отменено. Будущее/текущее значение свойства не доступны для сравнения одновременно.                                                                                                                                                                                               |
++++
|                             | Вызывается после того, как значение свойства было изменено                       |                                                                                                                                                                                                                                                                                                                                                                  |
| `onChanged(self, obj, prop)`      |                                                                                  | `prop`                                                                                                                                                                                                                                                                                                                                                                 |
|                                         |                                                                                  |                                                                                                                                                                                                                                                                                                                                                                              |
|                                            |                                                                                  | \- название свойства, которое подлежит изменению, но не сам объект свойства.                                                                                                                                                                                                                                                                                                    |
++++
|                             | Вызывается после восстановления документа или копирования объекта FeaturePython. | Иногда ссылки на объект FeaturePython из класса или класс из объекта FeaturePython могут быть нарушены, так как класс `__init__()` метод не вызывается при реконструкции объекта. Добавление `self.Object <nowiki>=</nowiki> obj` или `obj.Proxy <nowiki>=</nowiki> self` как правило решает эти проблемы. |
| {{Incode|onDocumentRestored(self, obj)}}   |                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                 |
|                                         |                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                 |
++++

Нередко можно столкнуться с ситуацией, когда обратные вызовы (callbacks) Python запускаются не так, как следовало бы. Начинающие в этой области могут быть уверены, что система обратного вызова FeaturePython не является хрупкой или сломанной. Неизменно, когда обратные вызовы не выполняются, это происходит из-за того, что ссылка потеряна или не определена в базовом коде. Однако, если кажется, что обратные вызовы прерываются без объяснения причин, предоставление ссылок на объекты/proxy ссылки в обратном вызове `onDocumentRestored()` (как указано в первой таблице выше) может облегчить эти проблемы. Пока вы не освоитесь с системой обратного вызова, может быть полезно добавлять инструкции вывода в консоль print() в каждый обратный вызов для вывода сообщений в консоль в процессе разработки.

## Дополнительные методы 

Приведенные ниже методы предназначены для **продвинутого** применения proxy классов Python, как правило в большинстве случаев они вам не понадобятся.

-   mustExecute
-   getViewProviderName
-   getSubObject
-   getSubObjects
-   getLinkedObject
-   hasChildElement
-   isElementVisible
-   canLinkProperties
-   allowDuplicateLabel
-   redirectSubName
-   canLoadPartial
-   onBeforeChangeLabel

## Определение всех доступных Python методов 

В случаях, когда документация к описываемому классу не актуализирована, вы можете самостоятельно определить какие методы доступны в нем , обратившись к исходному C++ коду. Например в [классе шаблоне FeaturePython](https://github.com/FreeCAD/FreeCAD/blob/76e74294894bbce46d006e149315c6274d206278/src/App/FeaturePython.h#L161-L351) перечислены различные вызовы, в виде: ().

Каждому из них соответствует аналогичный метод доступный в Python.

К примеру, imp->execute() [в строке 193](https://github.com/FreeCAD/FreeCAD/blob/76e74294894bbce46d006e149315c6274d206278/src/App/FeaturePython.h#L193) означает, что execute метод доступен в Python коде.

Обратите внимание, что getPyObject() и init() являются особыми случаями и не подлежат подобному способу определения.

## Смотрите также 

-   [FreeCAD GitHub: FeaturePython.h - public API](https://github.com/FreeCAD/FreeCAD/blob/76e74294894bbce46d006e149315c6274d206278/src/App/FeaturePython.h#L44-L86)
-   [FreeCAD GitHub: FeaturePythonT template class](https://github.com/FreeCAD/FreeCAD/blob/76e74294894bbce46d006e149315c6274d206278/src/App/FeaturePython.h#L167)
-   [FreeCAD Forum Discussion: Scripted Objects Complete Method Reference](https://forum.freecadweb.org/viewtopic.php?f=22&t=49194)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > FeaturePython methods/ru
