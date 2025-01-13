---
 GuiCommand:
   Name/ru: Обратить нормали формы
   Name: Part_ReverseShape
   MenuLocation: Деталь , Обратить нормали формы
   Workbenches: Part_Workbench/ru
---

# Part ReverseShape/ru


</div>



## Описание


<div class="mw-translate-fuzzy">

Обращает (переворачивает) нормали всех граней, выбранного объекта.


</div>



## Применение


<div class="mw-translate-fuzzy">

1.  Выберите форму.
2.  Выберите в верхнем меню **Деталь → <img src="images/Part_ReverseShape.svg" width=16px>Обратить нормали формы**.
3.  Фигура с обращенными нормалями будет создана, как отдельный новый объект.


</div>



## Примечания

-   [App Link](App_Link.md) objects linked to the appropriate object types and [App Part](App_Part.md) containers with the appropriate visible objects inside can also be used as source objects. <small>(v0.20)</small> 
-   To see the effect of the command change the **Lighting** property of the reversed shape to {{Value|On side}} and if required change **Edit → Preferences... → Display → 3D View → Rendering → Backlight color**.



## Свойства

See also: [Property editor](Property_editor.md).

A Part ReverseShape object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional property:

### Data


{{TitleProperty|Reverse}}

-    **Source|Link**: specifies the linked source shape.





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part ReverseShape/ru
