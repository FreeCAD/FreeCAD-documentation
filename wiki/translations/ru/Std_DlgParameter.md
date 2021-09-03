---
- GuiCommand:/ru
   Name:Std DlgParameter
   Name/ru:Std DlgParameter
   MenuLocation:Инструменты → Редактор параметров
   Workbenches:All
   SeeAlso:[Preferences Editor](Preferences_Editor/ru.md)
---

## Описание

The **Std DlgParameter** command opens the Parameter Editor. In the Parameter Editor the parameters that control the behavior of FreeCAD and its workbenches can be inspected and optionally removed, added or changed. The parameters are stored in a file called {{FileName|user.cfg}}, the location of this file depends on your OS.

Working with the Parameter Editor requires some experience. For the most common parameters you can also use the more convenient [Preferences Editor](Preferences_Editor.md).

![](images/Std_DlgParameter_dialog.png ) *The Parameter Editor dialog box*

## Применение

1.  Select the {{MenuCommand|Tools → <img src="images/Std_DlgParameter.svg" width=16px> Edit parameters...}} option from the menu.
2.  The Parameter Editor dialog box opens. For more information see [Options](#Options.md).
3.  Optionally press the **Save to disk** button to immediately update the {{FileName|user.cfg}} file. This is not required as FreeCAD will automatically update that file when the application closes.
4.  Press the **Close** button to close the Parameter Editor.

## Опции

### Left panel {#left_panel}

The left panel shows a tree with parameter groups and sub-groups.

*The following options are available in the panel\'s context menu:*

#### Expand/Collapse

1.  If a selected group has one or more sub-groups it can be expanded or collapsed by choosing this option from the context menu. But you can also expand and collapse the tree in the usual manner.

#### Add sub-group {#add_sub_group}

1.  Select a group.
2.  Select the {{MenuCommand|Add sub-group}} option from the context menu.
3.  Enter a name for the new sub-group in the dialog box that opens.
4.  Press the **OK** button.

#### Remove group {#remove_group}

1.  Select a group.
2.  Select the {{MenuCommand|Remove group}} option from the context menu.
3.  Press the **Yes** button in the dialog box that opens to confirm you want to remove the group (including all its sub-groups, and all parameters in the group and its sub-groups).

#### Rename group {#rename_group}

1.  Select a group.
2.  Select the {{MenuCommand|Rename group}} option from the context menu.
3.  Enter a new name.
4.  A group can also be renamed by double-clicking it.

#### Export parameter {#export_parameter}

1.  Select a group.
2.  Select the {{MenuCommand|Export parameter}} option from the context menu.
3.  Enter a filename in the dialog box.
4.  Press the **Save** button.

#### Import parameter {#import_parameter}

1.  Select a group that does not contain any sub-groups or remove them first. Any existing parameters in the group will be lost.
2.  Select the {{MenuCommand|Import parameter}} option from the context menu.
3.  Select a \*.FCParam file in the dialog box.
4.  Press the **Open** button.

### Right panel {#right_panel}

The right panel shows the parameters in the group selected in the left panel. If this group only contains sub-groups the right panel will be empty.

*The following options are available in the panel\'s context menu:*

#### Change value {#change_value}

1.  Select a parameter.
2.  Select the {{MenuCommand|Change value}} option from the context menu.
3.  Enter a new value in the dialog box that opens.
4.  Press the **OK** button.
5.  A parameter\'s value can also be changed by double-clicking its \'Type\' or \'Value\' field.

#### Remove key {#remove_key}

1.  Select a parameter.
2.  Select the {{MenuCommand|Remove key}} option from the context menu.

#### Rename key {#rename_key}

1.  Select a parameter.
2.  Select the {{MenuCommand|Rename key}} option from the context menu.
3.  Enter a new name.
4.  A parameter can also be renamed by double-clicking its \'Name\' field.

#### New string item {#new_string_item}

1.  Select the {{MenuCommand|New string item}} or {{MenuCommand|New → New string item}} option from the context menu.
2.  Enter a name in the dialog box that opens.
3.  Press the **OK** button.
4.  Enter a value in the next dialog box.
5.  Press the **OK** button.

#### New float item {#new_float_item}

1.  Select the {{MenuCommand|New float item}} or {{MenuCommand|New → New float item}} option from the context menu.
2.  The next steps are similar to those for a [New string item](#New_string_item.md)

#### New integer item {#new_integer_item}

1.  Select the {{MenuCommand|New integer item}} or {{MenuCommand|New → New integer item}} option from the context menu.
2.  The next steps are similar to those for a [New string item](#New_string_item.md)

#### New unsigned item {#new_unsigned_item}

1.  Select the {{MenuCommand|New unsigned item}} or {{MenuCommand|New → New unsigned item}} option from the context menu.
2.  The next steps are similar to those for a [New string item](#New_string_item.md)

#### New Boolean item {#new_boolean_item}

1.  Select the {{MenuCommand|New Boolean item}} or {{MenuCommand|New → New Boolean item}} option from the context menu.
2.  The next steps are similar to those for a [New string item](#New_string_item.md)

### Sorting

By default the groups in each tree level in the left panel are sorted alphabetically, and the parameters in the right panel are sorted alphabetically as well. But the order in each panel can be reversed by clicking the \'Group\' or \'Name\' header respectively.

### Quick search {#quick_search}

Typing a (partial) string in this input box will fully expand the tree in the left panel and highlight all groups with names that match the entered value. If no matches are found the background of the input box will turn red.

### Find

1.  In the left panel select the group where you want to start your search. The search direction is down. The search is not restricted to the group and its sub-groups, but rather the selected group and everything below it in the tree will be searched.
2.  Press the **Find...** button.
3.  Enter a string in the **Find what** input box. The search is case-insensitive.
4.  Check one or more of the {{CheckBox|TRUE|Groups}}, {{CheckBox|TRUE|Names}} and {{CheckBox|TRUE|Values}} checkboxes. Note that only string values will be searched.
5.  Optionally (un)check the {{CheckBox|TRUE|Match whole string only}} checkbox.
6.  Press the **Find Next** button to select the first group with a match. Matching parameters are not individually highlighted. Optionally repeat this until no further matches can be found.
7.  It is possible to start a new search without closing the dialog box. Again selecting the group from which to start searching is then usually required.
8.  Use the **Cancel** button to close the dialog box.

## Примечания

-   The [Fine-tuning](Fine-tuning.md) page lists a number of parameters that may be of interest.

## Scripting


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).

For a scripting example see [Std SelBoundingBox](Std_SelBoundingBox.md).





{{Std Base navi

}}  
