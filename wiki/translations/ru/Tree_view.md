# Tree view/ru
## Введение


<div class="mw-translate-fuzzy">

[Древо проекта](Tree_view/ru.md) появляется на вкладке **Модель** [комбо панели](Combo_view/ru.md), одной из самых важных панелей [интерфейса](Interface/ru.md); оно показывает все пользовательские объекты, которые являются частью документа FreeCAD. Древо проекта представляет собой [структуру документа](Document_structure/ru.md) и указывает, какая информация сохраняется на диске.


</div>

Эти объекты не обязательно должны быть геометрическими фигурами, видимыми в [3D-виде](3D_view/ru.md), но также могут быть вспомогательными объектами данных, созданными с помощью любого из [верстаков](Workbenches/ru.md).

![](images/FreeCAD_Tree_view.png )



*Древо проекта, показывающее различные элементы документа*



## Работа с древом проекта 


<div class="mw-translate-fuzzy">

По умолчанию всякий раз, когда создается новый объект, он добавляется в конец списка древа проекта. Древовидное представление позволяет управлять объектами, чтобы сохранить их организованными; оно позволяет создавать [группы](Std_Group/ru.md), перемещать объекты внутри групп, перемещать группы внутри других групп, переименовывать объекты, копировать объекты, удалять объекты и другие операции в контекстном меню (щелчок правой кнопкой мыши), которые зависят от текущего выбранного объекта и текущего активного рабочего верстака.


</div>

Многие операции создают объекты, которые зависят от ранее существовавшего объекта. В этом случае древовидное представление показывает эту связь, поглощая более старый объект внутри нового объекта. Разворачивание и сворачивание объектов в древовидном представлении показывает параметрическую историю этого объекта. Объекты, которые находятся глубже внутри других, являются более старыми, в то время как объекты, которые находятся снаружи, являются более новыми и являются производными от более старых объектов. Изменяя внутренние объекты, параметрические операции распространяются до самого верха, порождая новый результат.

<img alt="" src=images/FreeCAD_Tree_view_parametric_history.png  style="width:" height="300px;">


<div class="mw-translate-fuzzy">



*Самый верхний объект создается путем выполнения параметрических операций над объектами, которые сами были созданы предыдущими операциями. Разворачивание списка в древе на много уровней, раскрывает исходные элементы, которые были использованы для создания элементов твердых тел.*


</div>

### Tree view columns 

The Tree view always displays a column with the icons and labels of objects. Two additional columns can optionally be displayed as well. To enable these columns right-click the Tree view and in the context menu select **Tree settings** and then **Show description** (<small>(v0.21)</small> ) and/or **Show internal name** (<small>(v1.0)</small> ). Column headings are added if more than one column is displayed. Note that the internal names of objects cannot be changed.

### Edit object label 

Select an object in the first column and press **F2** (on Windows and Linux), or **Enter** (on macOS), to edit its **Label** property. This property can also be edited via the context menu option **Rename** or in the [Property editor](Property_editor.md).

### Edit object description 

An object can optionally have a description. This information is stored in its **Label2** property. If the description column is displayed you can edit this property by selecting an object in that column and pressing **F2** (on Windows and Linux), or **Enter** (on macOS). The property can also be changed in the [Property editor](Property_editor.md).

### Context menu 

The options in the context menu of the Tree view depend on the selected object(s) and the currently active workbench. To display this menu right-click the background of the list, right-click an object in the list, or select multiple objects in the list and then right-click one of them.

### Keyboard modifiers 

The usual keyboard modifiers can be used in the Tree view. The modifiers can be combined as well.

-    **Ctrl**: hold down this key to select multiple objects.

-    **Shift**: hold down this key to select all objects between a previously selected object and the next selected object.




<div class="mw-translate-fuzzy">

### Действия с клавиатуры 


</div>

The following keyboard shortcuts are available when the focus is on the Tree view:

-    **Ctrl**\+**F**: opens a search box at the bottom of the tree, allowing to search and reach objects using their internal names or labels.

-   Expand and collapse actions using **Alt**+**Arrow** combinations: <small>(v0.20)</small> 
    -   
        **Alt**
        
        \+**Left**: collapses selected item(s).

    -   
        **Alt**
        
        \+**Right**: expands selected item(s).

    -   
        **Alt**
        
        \+**Up**: expands selected item(s) with all their tier-1 children collapsed (deeper children remain unchanged).

    -   
        **Alt**
        
        \+**Down**: expands selected item(s) with all their tier-1 children expanded as well (deeper children remain unchanged).



## Накладные иконки 


<div class="mw-translate-fuzzy">

Одна или несколько небольших накладных иконок могут отображаться поверх иконки по умолчанию на объекте в древе проекта. Доступные накладные иконки и их значение перечислены ниже. <small>(v0.19)</small> 


</div>



### ![](images/FreeCAD_Tree_view_recompute.png ) Белая галочка на синем фоне 

Это означает, что объект должен быть [пересчитан](Std_Refresh/ru.md) из-за изменений, внесенных в модель, или из-за того, что пользователь пометил объект в контекстном меню древа проекта для пересчёта. В большинстве случаев пересчёт запускается автоматически, но иногда он задерживается по причинам производительности.



### ![](images/FreeCAD_Tree_view_error.png ) Белый восклицательный знак на красном фоне 

Это указывает на то, что объект имеет ошибку, которую необходимо исправить. После повторного вычисления всего документа при наведении курсора мыши на объект в древе проекта появляется всплывающая подсказка с описанием ошибки. **Примечание:** Все остальные объекты, зависящие от объекта в таком состоянии ошибки, не будут правильно пересчитаны, поэтому они всё ещё могут показывать какое-то устаревшее состояние.




<div class="mw-translate-fuzzy">

### ![](images/FreeCAD_Tree_view_unattached.png ) Фиолетовое звено цепи на белом фоне 


</div>


<div class="mw-translate-fuzzy">

Это обычно показано на [sketches(эскизах)](Sketch/ru.md), геометрических примитивах, таких как коробка, цилиндр и т.п. а также [Datum(Данных)](Datum/ru.md). Это указывает на то, что объект ни к чему не привязан. Он не имеет Привязки от Смещения и получает свое положение и выравнивание исключительно из своего свойства [Размещения](Placement/ru.md).


</div>

Существует базовый учебник (англ) [Basic Attachment Tutorial](Basic_Attachment_Tutorial.md), объясняющий, как обращаться с такими объектами.



### ![](images/FreeCAD_Tree_view_notfullyconstrained.png ) Жёлтый крестик 


<div class="mw-translate-fuzzy">

Это обозначение используется только для [эскизов](Sketch/ru.md) и указывает на то, что эскиз не полностью ограничен. В среде [Sketcher](Sketcher_Workbench/ru.md) количество оставшихся степеней свободы отображается в сообщениях решателя.


</div>



### ![](images/FreeCAD_Tree_view_tip.png ) Белая стрелка на зелёном фоне 

Это указывает на, так называемый, [Кончик](PartDesign_Body#Tip/ru.md) тела. Обычно это последняя функция в [PartDesign Тело](PartDesign_Body/ru.md) и олицетворяет всё тело целиком в окружающем мире вне тела, например, когда тело экспортируется или используется в [Булевых операциях](Part_Boolean/ru.md). Кончик может быть изменён пользователем.

### ![](images/FreeCAD_Tree_view_suppressed.png ) Red backslash 


<small>(v1.0)</small> 

This indicates a suppressed [PartDesign](PartDesign_Workbench.md) feature.

### ![](images/FreeCAD_Tree_view_link.png ) White upwards curved arrow 

This indicates a [linked](Std_LinkMake.md) object.

### ![](images/FreeCAD_Tree_view_link_external.png ) Two white upwards curved arrows 

This indicates a [linked](Std_LinkMake.md) object loaded from an external document.

### ![](images/FreeCAD_Tree_view_hidden.png ) Eye symbol 

This indicates that the object will be hidden in the Tree view if the **Show items hidden in Tree view** context menu option is unchecked.

### ![](images/FreeCAD_Tree_view_frozen.png ) Cyan ice crystal 


<small>(v1.0)</small> 

This indicates a [frozen](Std_ToggleFreeze.md) object that is not recomputed when its parents change.

## Preferences

See [Combo view](Combo_view#Preferences.md).


{{Interface_navi

}} {{Std_Base_navi}}



---
⏵ [documentation index](../README.md) > Tree view/ru
