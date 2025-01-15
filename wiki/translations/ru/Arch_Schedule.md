---
 GuiCommand:
   Name: Arch Schedule
   Name/ru: Arch Schedule
   MenuLocation: Архитектура , Create schedule...
   Workbenches: Arch_Workbench/ru
   Shortcut: 
---

# Arch Schedule/ru


</div>



## Описание

The **Arch Schedule** tool allows you to create and automatically populate a [spreadsheet](Spreadsheet_Workbench.md) with contents gathered from the model.

For a more general solution, see the [Reporting Workbench](https://github.com/furti/FreeCAD-Reporting/tree/master) in the list of [external workbenches](External_workbenches.md). This workbench uses SQL syntax to extract information from the document.



## Применение

1.  Open or create a FreeCAD document which contains some objects.
2.  Press the **<img src="images/Arch_Schedule.svg" width=16px> [Schedule](Arch_Schedule.md)** button.
3.  Adjust the desired options. Enable the **Associate spreadsheet** option if you want the schedule to generate a FreeCAD [spreadsheet](Spreadsheet_Workbench.md). Or, alternatively, right-click the schedule in the [Tree view](Tree_view.md) after creation, and select **Attach spreadsheet** from the context menu.
4.  Press **OK**.



## Рабочий процесс 

Для начала требуется некоторая готовая конструкция. Например, как здание в этом документе, которое содержит множество объектов созданных в верстаке Arch (хотя на самом деле также поддерживаются и другие объекты).

![](images/Arch_schedule_example01.jpg )


<div class="mw-translate-fuzzy">

Далее нажмите на кнопку **<img src="images/Arch_Schedule.svg" width=16px> [Планирование](Arch_Schedule/ru.md)**. В результате чего откроется панель задач, как на изображении ниже. Она довольно широкая, поэтому для удобной работы, вам нужно будет расширить комбо панель по горизонтали.


</div>

![](images/ArchSchedule.png )


<div class="mw-translate-fuzzy">

Затем вы можете заполнять строки таблицы друг за другом. Каждая строка представляет собой \"запрос\" и будет отображать одну строку в электронной таблице. Нажмите кнопку **Add**, чтобы добавить новую строку, и дважды щелкните каждую ячейку из этой строки, чтобы заполнить значения. Кнопка **Del** удаляет строку, содержащую выбранную в данный момент ячейку, а кнопка **Clear** удаляет абсолютно все строки. Доступными полями для заполнения в столбцах являются:


</div>


<div class="mw-translate-fuzzy">

-   **Description**: Описание для этого запроса. Столбец \"Описание\" - Это первый столбец результирующей электронной таблицы. В описании обязательно должен быть представлен запрос. Если вы оставите ячейку описания пустой, вся строка будет пропущена и оставлена пустой в электронной таблице. Это позволяет добавлять \"разделительные\" строки.
-   **Value**: Это реальный запрос, который вы хотите выполнить для всех объектов, выбранных этим запросом. Это может быть два типа вещей: либо слово `count` или свойство объекта:
    -   Если вы войдете `count` (или `Count` или `COUNT`, не чувствителен к регистру) выбранные объекты будут просто подсчитаны.
    -   Если вы введете свойство объекта, значение этого свойства для каждого из выбранных объектов будет извлечено и суммировано. Объекты, у которых нет этого свойства, будут пропущены. Используйте точечную нотацию для извлечения свойств свойств:`PropertyOfObject.PropertyOfProperty1.PropertyOfProperty2`. Если свойство перед первой точкой начинается со строчной буквы, оно будет считаться ссылкой на сам объект и игнорироваться. Ввод, например `object.Shape.Volume` это то же самое, что`Shape.Volume`.
-   **Unit**: Дополнительная единица измерения для выражения результатов. Вы сами должны указать единицу измерения, соответствующую выполняемому вами запросу, например, если вы извлекаете тома, вы должны использовать единицу измерения объема, например `m^3`. Если вы используете неправильную единицу измерения, например, см, вы получите неправильные результаты.
-   **Objects**: Вы можете оставить это поле пустым, тогда все объекты документа будут рассматриваться этим запросом, или предоставить разделенный точкой с запятой (;) список имен объектов (не меток). Если какой-либо из объектов в этом списке является группой, то также будут выбраны его дочерние объекты. Таким образом, самый простой способ использовать эту функцию - правильно сгруппировать ваши объекты в документе и просто указать здесь имя группы. Вы также можете использовать кнопку **Selection** чтобы добавить объекты, выбранные в данный момент в документе.
-   **Filter**: Здесь вы можете добавить точку с запятой`;`-разделенный список фильтров. Каждый фильтр записывается в виде: `property:value`. Вы можете использовать только те свойства, которые содержат строковое значение. Как свойство, так и значение не чувствительны к регистру. The `value` can be left out but not the `:`. To properly handle schedules created with previous versions of Arch Schedule the `type` property will be translated to the `ifctype` property. It is advisable to not use `type` in new schedules.

:   Например:

    :   
        `label:floor1;ifctype:window`
        
        сохранит только объекты, у которых есть \"floor1\" в их **Label** и \"window\" в их **IFC Type**. Окно с **Label** \"Floor1-AA\" и **IFC Type** равным \"Window Standard Case\" будет включено.

    :   
        `label:door`
        
        Сохранит только те объекты, которые имеют \"door\" в свойстве **Label**.

    :   
        `!label:door`
        
        Сохранит только объекты, которые не имеют \"door\" в свойстве **Label**.

    :   
        `ifctype:structural`
        
        Will retain only objects that have \"structural\" in their **IFC Type**.

    :   
        `!ifctype:something`
        
        Will retain only objects that do not have \"structural\" in their **IFC Type** or that do not have the **IFC Type** property.

    :   
        `!ifctype:`
        
        Will retain only objects that do not have the **IFC Type** property.


</div>

+++
| Query                                  | Description                                                                                                                                                                                                                                                                                                                  |
+========================================+==============================================================================================================================================================================================================================================================================================================================+
|                         | Will retain only objects that have \"floor1\" in their **Label** and \"window\" in their **IFC Type**. A window with the **Label** \"Floor1-AA\" and the **IFC Type** \"Window Standard Case\" will be included. |
| `label:floor1;ifctype:window` |                                                                                                                                                                                                                                                                                                                              |
|                                     |                                                                                                                                                                                                                                                                                                                              |
+++
|                         | Will retain only objects that have \"door\" in their **Label**                                                                                                                                                                                                                                    |
| `label:door`                  |                                                                                                                                                                                                                                                                                                                              |
|                                     |                                                                                                                                                                                                                                                                                                                              |
+++
|                         | Will retain only objects that do not have \"door\" in their **Label**                                                                                                                                                                                                                             |
| `!label:door`                 |                                                                                                                                                                                                                                                                                                                              |
|                                     |                                                                                                                                                                                                                                                                                                                              |
+++
|                         | Will retain only objects that have \"structural\" in their **IFC Type**                                                                                                                                                                                                                           |
| `ifctype:structural`          |                                                                                                                                                                                                                                                                                                                              |
|                                     |                                                                                                                                                                                                                                                                                                                              |
+++
|                         | Will retain only objects that do not have \"structural\" in their **IFC Type** or that do not have the **IFC Type** property                                                                                                                                           |
| `!ifctype:something`          |                                                                                                                                                                                                                                                                                                                              |
|                                     |                                                                                                                                                                                                                                                                                                                              |
+++
|                         | Will retain only objects that do not have the **IFC Type** property                                                                                                                                                                                                                               |
| `!ifctype:`                   |                                                                                                                                                                                                                                                                                                                              |
|                                     |                                                                                                                                                                                                                                                                                                                              |
+++

: Example filter queries

The **<img src="images/Document-open.svg" width=16px> Import** button allows you to build this list in another spreadsheet application, and import that as a csv file here.


<div class="mw-translate-fuzzy">

Таким образом, мы можем составить список запросов, подобный этому:


</div>

![](images/ArchScheduleExample.png )


<div class="mw-translate-fuzzy">

После этого нажмите **OK**, и в документ будет добавлен новый объект \"Планирование\", содержащий результат в виде электронной таблицы:


</div>

![](images/Arch_schedule_example04.jpg )

To edit an existing schedule double-click it in the Tree view. By double-clicking the spreadsheet, you get the results in 3 columns: Description, Value, Unit (if applicable):

![](images/Arch_schedule_example05.jpg )

The spreadsheet can then be exported to csv normally, from the [Spreadsheet Workbench](Spreadsheet_Workbench.md).



## Динамические свойства 

It is possible to add your own properties to objects. These are called [Dynamic properties](Property_editor#Actions.md). If they have been added with the **Prefix group name** option selected, their names will indeed start with the group name, but this prefix is not displayed in the [Property editor](Property_editor.md). Their names have this form: `NameOfGroup_NameOfProperty`. To reference them in a schedule this full name must be used.



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch Schedule/ru
