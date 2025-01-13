---
 GuiCommand:
   Name: Fasteners_BOM
   Name/ru: Спецификация
   MenuLocation: Стандартные изделия , Спецификация
   Workbenches: Fasteners_Workbench/ru
   SeeAlso: Spreadsheet_Workbench/ru
---

# Fasteners BOM/ru



## Описание

Команда <img alt="" src=images/Fasteners_BOM.svg  style="width:24px;"> **Спецификация** создает электронную таблицу с перечислением всех крепёжных изделий находящихся в документе.

<img alt="" src=images/Fasteners_BOM_Example.png  style="width:650px;"> 
*Сборка из деталей и сгенерированная электронная таблица спецификации*



## Применение

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Fasteners_BOM.svg" width=16px> [Generate BOM](Fasteners_BOM.md)** button.
    -   Select the **Fasteners → <img src="images/Fasteners_BOM.svg" width=16px> Generate BOM** option from the menu.
2.  A Fasteners BOM spreadsheet is created.



## Примечания

-   Электронная таблица спецификации крепежа не обновляется при изменении типа уже существующего крепежа, а также при добавлении или удалении крепежа. В таких случаях необходимо заново применить команду для получения новой электронной таблицы.
-   Таблицу спецификации крепежа можно экспортировать с помощью команды [экспорта таблицы](Spreadsheet_Export/ru.md)




{{Fasteners_Tools_navi}}



---
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > Fasteners BOM/ru
