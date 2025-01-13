---
 GuiCommand:
   Name: Arch Schedule
   MenuLocation: Manage , Schedule
   Workbenches: BIM_Workbench
   SeeAlso: 
---

# Arch Schedule/en

## Description

The **Arch Schedule** tool allows you to create and automatically populate a [spreadsheet](Spreadsheet_Workbench.md) with contents gathered from the model.

For a more general solution, see the [Reporting Workbench](https://github.com/furti/FreeCAD-Reporting/tree/master) in the list of [external workbenches](External_workbenches.md). This workbench uses SQL syntax to extract information from the document.

## Usage

1.  Open or create a FreeCAD document which contains some objects.
2.  Press the **<img src="images/Arch_Schedule.svg" width=16px> [Schedule](Arch_Schedule.md)** button.
3.  Adjust the desired options. Enable the **Associate spreadsheet** option if you want the schedule to generate a FreeCAD [spreadsheet](Spreadsheet_Workbench.md). Or, alternatively, right-click the schedule in the [Tree view](Tree_view.md) after creation, and select **Attach spreadsheet** from the context menu.
4.  Press **OK**.

## Workflow

First you need to have a model. For example, here is a document with a couple of Arch objects, but other objects are also supported.

![](images/Arch_schedule_example01.jpg )

When you press the **<img src="images/Arch_Schedule.svg" width=16px> [Schedule](Arch_Schedule.md)** button this dialog opens:

![](images/ArchSchedule.png )

You can now fill the schedule row by row. Each row is a \"query\" and will render one row in the spreadsheet. Press the **<img src="images/List-add.svg" width=16px> Add row** button to add a new row, and double-click each cell from that row to fill in the values. The **<img src="images/List-remove.svg" width=16px> Del row** button will delete the row which contains a currently selected cell, and **<img src="images/Delete.svg" width=16px> Clear** will delete all rows. Possible values to put in columns are:

-   **Description**: A description for this query. The Description column will be the first column of the resulting spreadsheet. The description is mandatory to have a query performed. If you leave the description cell empty, the whole row will be skipped and left blank in the spreadsheet. This allows you to add \"separator\" rows.
-   **Property**: This is the real query that you want to perform on all the objects selected by the query. It can be two things: either the word `count` or an object property:
    -   If you enter `count` (or `Count` or `COUNT`, it\'s case-insensitive) the selected objects will simply be counted.
    -   If you enter an object property the value of this property will be retrieved for each of the selected objects and summed up. Objects that do not have the given property will be skipped. Generally a property name will be that shown in the [Property editor](Property_editor.md), without spaces (e.g. type `PerimeterLength` in the Property column if the object has a `Perimeter Length` in the Property editor). Use the dot notation to retrieve properties of properties: `PropertyOfObject.PropertyOfProperty1.PropertyOfProperty2`. If the property before the first dot starts with a lowercase letter it will be considered a reference to the object itself and be ignored. Entering for example `object.Shape.Volume` is the same as entering `Shape.Volume`.
-   **Unit**: An optional unit to express the results in. It\'s up to you to give a unit that matches the query you are doing, for example, if you are retrieving volumes, you should use a volume unit, such as `m^3` or `m³`. If you use a wrong unit for the property, e.g. `cm` for volume, you\'ll get wrong results.
-   **Objects**: You can leave this empty, then all the objects of the document will be considered by this query, or give a semicolon`;`-separated list of object names. If any of the objects in this list is a group, its children will be selected as well. So the easiest way to use this feature is to group your objects meaningfully in the document, and just give a group name here. You can also use the **<img src="images/Edit-select-all.svg" width=16px> Add selection** button to add objects currently selected in the document. You must use internal names here. To select objects by their label, leave this column empty and use the Filter column instead.
-   **Filter**: Here you can add a semicolon`;`-separated list of filters. Each filter is written in the form: `property:value`. You can only use properties that hold a string value. Both the property and the value are case-insensitive. The `value` can be left out but not the `:`. To properly handle schedules created with previous versions of Arch Schedule the `type` property will be translated to the `ifctype` property. It is advisable to not use `type` in new schedules.

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

The finished schedule may look like this:

![](images/ArchScheduleExample.png )

Finally, press **OK** and a new schedule is added to the document. If the related option has been selected, the schedule will contain an associate spreadsheet:

![](images/Arch_schedule_example04.jpg )

To edit an existing schedule double-click it in the Tree view. By double-clicking the spreadsheet, you get the results in 3 columns: Description, Value, Unit (if applicable):

![](images/Arch_schedule_example05.jpg )

The spreadsheet can then be exported to csv normally, from the [Spreadsheet Workbench](Spreadsheet_Workbench.md).

## Dynamic properties 

It is possible to add your own properties to objects. These are called [Dynamic properties](Property_editor#Actions.md). If they have been added with the **Prefix group name** option selected, their names will indeed start with the group name, but this prefix is not displayed in the [Property editor](Property_editor.md). Their names have this form: `NameOfGroup_NameOfProperty`. To reference them in a schedule this full name must be used.





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch Schedule/en
