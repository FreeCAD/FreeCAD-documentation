 

<img alt="Иконка верстака электронных таблиц" src=images/Workbench_Spreadsheet.svg  style="width:128px;">

## Введение

<img alt="" src=images/Workbench_Spreadsheet.svg  style="width:24px;"> [Верстак электронных таблиц](Spreadsheet_Workbench/ru.md) позволяет создать и редактировать электронные таблицы, использовать данные из электронной таблицы как параметр в модели, заполнять таблицу данными из модели, выполнять вычисления, и экспортировать данные в другие приложения текстовых таблиц, такие как LibreOffice или Microsoft Excel.


{{TOCright}}

<img alt="" src=images/Spreadsheet_screenshot.jpg  style="width:600px;"> 
*Таблица с определенными ячейками, заполненными текстом и значениями.*

## Инструменты

-   <img alt="" src=images/Spreadsheet_CreateSheet.svg  style="width:24px;"> [Create sheet](Spreadsheet_CreateSheet/ru.md): создать новую электронную таблицу.

-   <img alt="" src=images/Spreadsheet_Import.svg  style="width:24px;"> [Импорт](Spreadsheet_Import/ru.md): импортировать файл со значениями, разделёнными табуляцией (CSV), в электронную таблицу.
-   <img alt="" src=images/Spreadsheet_Export.svg  style="width:24px;"> [Экспорт](Spreadsheet_Export/ru.md): экспорт файла со значениями, разделёнными табуляцией (CSV), из электронной таблицы.

-   <img alt="" src=images/Spreadsheet_MergeCells.svg  style="width:24px;"> [Объединить ячейки](Spreadsheet_MergeCells/ru.md): объединить выбранные ячейки.
-   <img alt="" src=images/Spreadsheet_SplitCell.svg  style="width:24px;"> [Разделить ячейку](Spreadsheet_SplitCell/ru.md): разделить ранее объединённые ячейки.

-   <img alt="" src=images/Spreadsheet_AlignLeft.svg  style="width:24px;"> [Align left](Spreadsheet_AlignLeft/ru.md): выровнять содержимое выбранных ячеек по левому краю.
-   <img alt="" src=images/Spreadsheet_AlignCenter.svg  style="width:24px;"> [Align center](Spreadsheet_AlignCenter/ru.md): выровнять содержимое выбранных ячеек горизонтально по центру.
-   <img alt="" src=images/Spreadsheet_AlignRight.svg  style="width:24px;"> [Align right](Spreadsheet_AlignRight/ru.md): выровнять содержимое выбранных ячеек по правому краю.
-   <img alt="" src=images/Spreadsheet_AlignTop.svg  style="width:24px;"> [Align top](Spreadsheet_AlignTop/ru.md): выровнять содержимое выбранных ячеек по верху.
-   <img alt="" src=images/Spreadsheet_AlignVCenter.svg  style="width:24px;"> [Align vertical center](Spreadsheet_AlignVCenter/ru.md): выровнять содержимое выбранных ячеек вертикально по центру.
-   <img alt="" src=images/Spreadsheet_AlignBottom.svg  style="width:24px;"> [Align bottom](Spreadsheet_AlignBottom/ru.md): выровнять содержимое выбранных ячеек по низу.

-   <img alt="" src=images/Spreadsheet_StyleBold.svg  style="width:24px;"> [Style bold](Spreadsheet_StyleBold/ru.md): установить для выбранных ячеек жирный шрифт.
-   <img alt="" src=images/Spreadsheet_StyleItalic.svg  style="width:24px;"> [Style italic](Spreadsheet_StyleItalic/ru.md): установить для выбранных ячеек наклонный шрифт.
-   <img alt="" src=images/Spreadsheet_StyleUnderline.svg  style="width:24px;"> [Style underline](Spreadsheet_StyleUnderline/ru.md): установить для выбранных ячеек подчёркнутый шрифт.

-   <img alt="" src=images/Spreadsheet_SetAlias.svg  style="width:24px;"> [Set alias](Spreadsheet_SetAlias/ru.md): установить псевдоним для выбранных ячеек.

-    **Black**и **White** устанавливают цвета переднего и заднего плана выбранных ячеек.

-   Context-menu of the spreadsheet rows and columns: right-click onto the header of a row or column to insert a new row above or a new column at the left, or to delete the current row/column. You can also select several rows or columns to delete them.<small>(v0.20)</small>  You can also select where the the new rows/columns will be inserted. Furthermore, to insert for example 3 new columns at once, select 3 columns and use the context-menu that will now offer to insert 3 columns.

### Свойства ячейки {#свойства_ячейки}

Свойства ячейки электронной таблицы можно редактировать, щелкнув ячейку правой кнопкой мыши. Появится следующий диалог:

![](images/SpreadsheetCellPropDialog.png )

Как указано на вкладках, можно изменить следующие свойства:

-   Цвет: цвет текста и цвет фона.
-   Выравнивание: выравнивание текста по горизонтали и вертикали
-   Стиль: стиль текста: полужирный, курсив, подчеркивание.
-   Единицы: Отображение единиц измерения для этой ячейки. Прочтите раздел [Единицы измерения](#Единицы_измерения.md) ниже.
-   Псевдоним: Определение [псевдонима](Spreadsheet_SetAlias/ru.md) для этой ячейки. Этот псевдоним можно использовать в формулах ячеек, а также в общих [выражениях](Expressions/ru.md); смотри раздел [данные электронных таблиц в выражениях](#Выражения_в_ячейках.md) для получения дополнительной информации.

## Выражения в ячейках {#выражения_в_ячейках}

Ячейка таблицы может содержать любой текст или выражение. Технически, выражение должно начинаться со знака равенства \'=\'. Однако, таблица пытается быть умной, и если Вы введёте нечто, похожее на выражение, но без начального знака \'=\', он будет добавлен автоматически.

Выражения ячеек могут содержать числа, функции, ссылки на другие ячейки и ссылки на свойства модели. (Но смотрите [текущие ограничения](#Текущие_ограничения.md) ниже). Ссылки на ячейки по их столбцам (ЗАГЛАВНЫЕ буквы) и строкам (числа). На ячейки можно так же ссылаться по их [псевдонимам](#alias_name.md) (см. ниже). Пример: B4 + A6

**Примечание:** Выражения в ячейках обрабатываются FreeCAD как программный код. Поэтому при редактировании ячеек видимое содержимое не следует настройкам дисплея:

-   десятичный разделитель всегда точка
-   число показываемых десятичных чисел может отличаться от [настроек](Preferences_Editor/ru#Единицы_измерения.md)

Ссылки на объекты в модели описаны в разделе [Ссылки на данные САПР](#Ссылки_на_данные_САПР.md). Использование значений ячеек для определения параметров моделей описано в разделе [Данные таблицы в выражениях](#Данные_таблицы_в_выражениях.md). Насчёт дополнительной информации о выражениях и доступных функциях, смотрите [Выражения](Expressions/ru.md).

## Взаимодействие между электронными таблицами и моделью САПР {#взаимодействие_между_электронными_таблицами_и_моделью_сапр}

Данные в ячейках электронной таблицы могут использоваться в выражениях параметров модели САПР. Таким образом, электронная таблица может использоваться как источник значений параметров, используемых во всей модели, эффективно собирая значения в одном месте. Когда значения изменяются в электронной таблице, они распространяются по всей модели.

Точно так же свойства из объектов модели САПР могут использоваться в выражениях в ячейках электронной таблицы. Это позволяет использовать такие свойства объекта, как объем или площадь в электронной таблице. Если имя объекта в модели САПР изменяется, изменение автоматически распространяется на все ссылки в выражениях в электронной таблице, использующих изменённое имя.


<div class="mw-translate-fuzzy">

В одном документе можно использовать более одной электронной таблицы; электронным таблицам можно давать присвоенное пользователем имя (переименовывать), как и любому другому объекту.


</div>

FreeCAD will automatically assign a unique name to a spreadsheet when it is created. These names follow the pattern `Spreadsheet`, `Spreadsheet001`, `Spreadsheet002` and so on. The name can not be changed manually, and it is not visible in the properties of the spreadsheet. It can be used to refer to the spreadsheet in an [Expression](Expressions.md) (see [Spreadsheet data in expressions](#Spreadsheet_data_in_expressions.md) below.)

The label of a spreadsheet is automatically set to the name of the spreadsheet upon creation. Unlike the name, the label can be changed, for example in the properties panel or using the context menu action Rename. Note that the label of a spreadsheet within a document has to be unique; if you try to change the label to a label already used by another spreadsheet, FreeCAD will not accept the new label.

FreeCAD проверяет на циклические зависимости. Смотрите в разделе [Текущие ограничения](Spreadsheet_Workbench/ru#Текущие_ограничения.md).

### Ссылки на данные САПР {#ссылки_на_данные_сапр}

Как указано выше, можно ссылаться на данные из модели САПР в выражениях электронной таблицы.

Вычисляемые выражения в ячейках электронной таблицы начинаются со знака равенства (\'=\'). Однако механизм ввода в электронную таблицу пытается быть умным. Выражение можно вводить без символа \'=\' в начале; если введённая строка является допустимым выражением, при вводе последнего **Enter** автоматически добавляется \'=\'. Если введённая строка не является допустимым выражением (часто это результат ввода чего-то в неправильном регистре, например, «MyCube.length» вместо «MyCube.Length»), начальный знак «=» не добавляется и рассматривается как просто текстовая строка.

**Примечание:** Такое поведение (автоматическая вставка \'=\') имеет некоторые неприятные последствия:

-   Если вы хотите сохранить столбец имен, соответствующий [псевдонимам](#alias_name.md) в соседнем столбце значений, вы должны ввести имя в столбце метки перед тем как дать ячейке в колонке значений его псевдоним. В противном случае, при вводе псевдонима в столбце метки, электронная таблица предположит, что это выражение, и изменит его на «= »; а отображаемый текст станет значением из ячейки .
-   Если вы допустили ошибку при вводе имени в столбце метки и хотите исправить ее, вы не сможете просто изменить ее на псевдоним. Вместо этого вам придётся сначала изменить псевдоним на другой, затем исправить текстовое имя в столбце метки, и лишь потом вернуть псевдоним в столбце значений в исходный вид.

Один из способов обойти эти проблемы - поставить перед текстовыми метками, соответствующими псевдонимам, фиксированную строку, тем самым делая их разными. Обратите внимание, что «\_» не будет работать, так как он преобразуется в «=». Однако пробел, хотя и невидим, работать будет.

В следующей таблице показаны некоторые примеры, предполагающие, что модель имеет функцию с именем «MyCube»:

  Данные САПР                                 Ячейка в таблице               Результат
  ------------------------------------------- ------------------------------ ---------------------------------------
  Параметрическая длинна Куба верстака Part   =MyCube.Length                 Длинна в единицах mm
  Объём Cube                                  =MyCube.Shape.Volume           Объём в mm³ без указания единиц
  Тип формы Cube                              =MyCube.Shape.ShapeType        String: Solid
  Метка Cube                                  =MyCube.Label                  String: MyCube
  Координата X центра масс Cube               =MyCube.Shape.CenterOfMass.x   Координата X в mm без указания единиц

### Данные таблицы в выражениях {#данные_таблицы_в_выражениях}

In order to use spreadsheet data in other parts of FreeCAD, you will usually create an [Expression](Expressions.md) that refers to the spreadsheet and the cell that contains the data you want to use. You can identify spreadsheets by name or by label, and you can identify the cells by position or by alias. Autocompletion is available for all forms of referencing.

+------------------+-----------------------------------------------------+--------------------------------------------------------+
|                  | Spreadsheet by Name                                 | Spreadsheet by Label                                   |
+==================+=====================================================+========================================================+
| Cell by Position |                                      |                                         |
|                  | `<nowiki>=Spreadsheet042.B5</nowiki>`      | `<nowiki>=<<MySpreadsheet>>.B5</nowiki>`      |
|                  |                                                  |                                                     |
+------------------+-----------------------------------------------------+--------------------------------------------------------+
| Cell by Alias    |                                      |                                         |
|                  | `<nowiki>=Spreadsheet042.MyAlias</nowiki>` | `<nowiki>=<<MySpreadsheet>>.MyAlias</nowiki>` |
|                  |                                                  |                                                     |
+------------------+-----------------------------------------------------+--------------------------------------------------------+


<div class="mw-collapsible mw-collapsed">

The recommended way to refer to spreadsheet data is to use the spreadsheet label and cell alias name. For a more in-depth explanation of the pros and cons of the addressing modes, see the expanded section below.


<div class="mw-collapsible-content">

Using the spreadsheet label has the advantage that it can be freely changed to describe the contents of the spreadsheet. It is also easier to identify the spreadsheet that is being used since the text in the expression matches the label shown in the model and property views. If you decide to change the label of a spreadsheet, existing references to the contents of the spreadsheet will be updated, so you won\'t break your expressions by renaming the spreadsheet. The internal name of the spreadsheet is not readily available anywhere except within the expression editor, so if you use the internal name and later decide to rename the spreadsheets, you might have a hard time tracing your expression data back to its source.

Be aware that when you create a new spreadsheet, the name and the label are the same, so it is easy to accidentally use the spreadsheet name instead of the label. A simple way to avoid this is to give the spreadsheet a meaningful name before starting to use it in expressions.

While you may use the row and column number in an expression to reference a cell, best practice is to give the cell an alias name and use that. See [Cell Properties](#Cell_Properties.md) above on how to set the alias. For example, if the data in cell B1 contained the length parameter for an object, an alias name of `MyObject_Length` would allow the value to be referred to as `<<MyParams>>.MyObject_Length` instead of `Spreadsheet.B1`. Besides being much easier to read and understand, alias names are also much easier to change if you decide to adjust the structure of your spreadsheet. Using an alias also has the advantage that it is reasier to see which cells are used to control other parts of the document. Note that FreeCAD will automatically adjust the positional references in expressions if you insert or remove rows and columns in the spreadsheet, so even if you use row and column numbers in an expression, you can insert rows and columns without breaking the references to the surrounding cells.


</div>


</div>

### Complex models and recomputes {#complex_models_and_recomputes}

Editing a spreadsheet will trigger a recompute of the 3D model, even if the changes do not affect the model. For a complex model a recompute can take a long time, and having to wait after every single edit is of course quite annoying.

There are three solutions to deal with this:

1.  Temporarily skip recomputes:
    -   In the [Tree view](Tree_view.md) right-click the <img alt="" src=images/Document.svg  style="width:24px;"> document that contains the spreadsheet.
    -   Select the {{MenuCommand|Skip recomputes}} option from the context menu.
    -   There is a big disadvantage to this solution. New values entered in the spreadsheet will not be displayed until the document is recomputed. Instead `#PENDING` is shown.
    -   You can either recompute manually, using the [Std Refresh](Std_Refresh.md) command, or disable {{MenuCommand|Skip recomputes}} when you are done editing.
2.  Use a macro to automatically skip recomputes while editing a spreadsheet:
    -   Download and run [skipSheet.FCMacro](https://forum.freecadweb.org/viewtopic.php?f=8&t=48600#p419301).
    -   This solution saves a few steps compared to the first solution, but also has the mentioned disadvantage.
3.  Put the spreadsheet in a separate file:
    -   You can reference spreadsheet data from an external file with this syntax: `<nowiki>=NameOfFile#<<MySpreadsheet>>.MyAlias</nowiki>`.
    -   The advantage of having the spreadsheet in another file over switching off recomputes is that the spreadsheet itself does get recomputed.
    -   The disadvantage is that the model won\'t automatically recompute after changes to the spreadsheet.
    -   In the scenario where you first open the \'spreadsheet\' file, change one or more values and then open the \'model\' file, there won\'t be any indication that the model needs to be recomputed. But if both files are open the [Std Refresh](Std_Refresh.md) icon will update correctly for the \'model\' file after changes to the \'spreadsheet\' file.

## Единицы измерения {#единицы_измерения}

The Spreadsheet has a notion of dimension (units) associated with cell values. A number entered without an associated unit has no dimension. The unit should be entered immediately following the number value, with no intervening space. If a number has an associated unit, that unit will be used in all calculations. For example, the multiplication of two lengths with the unit mm gives an area with the unit mm².

If a cell contains a value which represents a dimension, it should be entered with its associated unit. While in many simple cases one can get by with a dimensionless value, it is unwise to not enter the unit. If a value representing a dimension is entered without its associated unit, there are some sequences of operations which cause FreeCAD to complain of incompatible units in an expression when it appears the expression should be valid. (This may be better understood by viewing [this thread](https://forum.freecadweb.org/viewtopic.php?f=3&t=34713&p=292455#p292438) in the FreeCAD forums.)

You can change the units displayed for a cell value using the properties dialog [units tab](#units_tab.md) (above). This does not change the value contained in the cell; it only converts the existing value for display. The value used for calculations does not change, and the results of formulas using the value do not change. For example, a cell containing the value \"5.08cm\" can be displayed as \"2in\" by changing the units tab value to \"in\".

A dimensionless number cannot be changed to a number with a unit by the cell properties dialog. One can put in a unit string, and that string will be displayed; but the cell still contains a dimensionless number. In order to change a dimensionless value to a value with a dimension, the value itself must be re-entered with its associated unit.

Occasionally it may be desirable to get rid of a dimension in an expression. This can be done by multiplying by 1 with a reciprocal unit.

## Импорт и экспорт {#импорт_и_экспорт}

Sheets can be imported and exported to the [csv](https://en.wikipedia.org/wiki/Comma-separated_values) format which can also be read and written by most other spreadsheet applications such as Microsoft Excel or LibreOffice Calc. When importing files into FreeCAD, the delimiter (the character that is used to separate columns) must be the TAB character (this can be set when exporting from other applications). The import of a CSV-file is available from the menu {{MenuCommand|Spreadsheet → Import Spreadsheet}} or by clicking on the icon <img alt="" src=images/SpreadsheetImport.svg  style="width:24px;">. This import function does not open Excel files or any other spreadsheet format.

Spreadsheets in Excel-format \"xlsx\" can be imported via the menu {{MenuCommand|File → Import...}}. Excel-spreadsheets can also be opened by clicking in the menu {{MenuCommand|File → Open...}} or by clicking on the icon <img alt="" src=images/Document-open.svg  style="width:24px;">. In these cases a new document with a spreadsheet inside is created. The following features are supported:

-   all functions that are also available in the FreeCAD spreadsheet. Other functions give an error in the corresponding cell after the import.
-   Alias names for cells
-   More than one \"Sheet\" in the Excel-spreadsheet. In this case one FreeCAD spreadsheet is created for each Excel sheet.

Other functionality is not imported into the FreeCAD spreadsheet. The Excel-import is <small>(v0.17)</small>  of FreeCAD.

## Printing

To handle the page setup necessary for printing, FreeCAD spreadsheets are printed by inserting them into a [TechDraw Spreadsheet View](TechDraw_SpreadsheetView.md).

## Текущие ограничения {#текущие_ограничения}


<div class="mw-translate-fuzzy">

FreeCAD проверяет циклические зависимости. По задумке эта проверка останавливается на уровне объекта электронной таблицы. Как следствие, у вас не должно быть электронной таблицы, содержащей как ячейки, значения которых используются для определения параметров модели, так и ячейки, значения которых используют выходные данные модели. Например, у вас не может быть ячеек, определяющих длину, ширину и высоту объекта, и другой ячейки, которая ссылается на общий объем полученной формы. Это ограничение можно преодолеть с помощью двух электронных таблиц: одна используется в качестве источника данных для входных параметров модели, а другая используется для расчётов на основе результирующих геометрических данных.


</div>


<div class="mw-translate-fuzzy">

При копировании ячеек копируется только содержание (выражение/значение). Описанные выше [свойства ячейки](#Свойства_ячейки/ru.md) не копируются.


</div>

## Основы составления скриптов {#основы_составления_скриптов}


```python
import Spreadsheet
sheet = App.ActiveDocument.addObject("Spreadsheet::Sheet","MySpreadsheet")
sheet.Label = "Dimensions"

sheet.set('A1','10mm')
sheet.recompute()
sheet.get('A1')

sheet.setAlias('B1','Diameter')
sheet.set('Diameter','20mm')
sheet.recompute()
sheet.get('Diameter')
```





{{Spreadsheet_Tools_navi

}} 

[Category:Workbenches{{\#translation:}}](Category:Workbenches.md)
