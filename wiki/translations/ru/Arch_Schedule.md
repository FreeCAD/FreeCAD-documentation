---
- GuiCommand:
   Name: Arch Schedule
   Name/ru: Arch Schedule
   MenuLocation: Архитектура - Create schedule...
   Workbenches: [Arch](Arch_Workbench/ru.md)
   Shortcut: 
---

# Arch Schedule/ru


</div>

## Описание

The Schedule tool allows you to create and automatically populate a [spreadsheet](Spreadsheet_Workbench.md) with contents gathered from the model.


**Примечание**

: Данный инструмент был значительно переработан в FreeCAD 0.17 и отличается от предыдущих версий.

For a more general solution, see the [Reporting Workbench](https://github.com/furti/FreeCAD-Reporting/tree/master) in the list of [external workbenches](External_workbenches.md). This workbench uses SQL syntax to extract information from the document.

## Применение

1.  Open or create a FreeCAD document which contains some objects.
2.  Press the **<img src="images/Arch_Schedule.svg" width=16px> [Schedule](Arch_Schedule.md)** button.
3.  Adjust the desired options.
4.  Press **OK**.

## Рабочий процесс 

Для начала требуется некоторая готовая конструкция. Например, как здание в этом документе, которое содержит множество объектов созданных в верстаке Arch (хотя на самом деле также поддерживаются и другие объекты).

![](images/Arch_schedule_example01.jpg )

Далее нажмите на кнопку **<img src="images/Arch_Schedule.svg" width=16px> [Планирование](Arch_Schedule/ru.md)**. В результате чего откроется панель задач, как на изображении ниже. Она довольно широкая, поэтому для удобной работы, вам нужно будет расширить комбо панель по горизонтали.

![](images/Arch_schedule_example02.jpg )

Затем вы можете заполнять строки таблицы друг за другом. Каждая строка представляет собой \"запрос\" и будет отображать одну строку в электронной таблице. Нажмите кнопку **Add**, чтобы добавить новую строку, и дважды щелкните каждую ячейку из этой строки, чтобы заполнить значения. Кнопка **Del** удаляет строку, содержащую выбранную в данный момент ячейку, а кнопка **Clear** удаляет абсолютно все строки. Доступными полями для заполнения в столбцах являются:

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

The **Import** button allows you to build this list in another spreadsheet application, and import that as a csv file here.

Таким образом, мы можем составить список запросов, подобный этому:

![](images/Arch_schedule_example03.jpg )

После этого нажмите **OK**, и в документ будет добавлен новый объект \"Планирование\", содержащий результат в виде электронной таблицы:

![](images/Arch_schedule_example04.jpg )

By double-clicking the Schedule object, you get back to the task panel and change the values. By double-clicking the spreadsheet itself, you get the results in 3 columns: description, value, unit (if applicable):

![](images/Arch_schedule_example05.jpg )

The spreadsheet can then be exported to csv normally, from the Spreadsheet workbench.

## Динамические свойства 

It is possible to add your own properties to objects. These are called [Dynamic properties](Property_editor#Actions.md). If they have been added with the **Prefix group name** option selected, their names will indeed start with the group name, but this prefix is not displayed in the [Property editor](Property_editor.md). Their names have this form: `NameOfGroup_NameOfProperty`. To reference them in a schedule this full name must be used.



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Schedule/ru
