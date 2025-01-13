---
 GuiCommand:
   Name/ru: Создать группу Видов
   Name: TechDraw_ClipGroup
   MenuLocation: TechDraw , Создать группу Видов
   Workbenches: TechDraw_Workbench/ru
   SeeAlso: TechDraw_ClipGroupAdd/ru, TechDraw_ClipGroupRemove/ru
---

# TechDraw ClipGroup/ru


</div>



## Описание


<div class="mw-translate-fuzzy">

Данный инструмент создает группу Видов, которая может содержать в себе один или несколько Видов. В зависимости от размеров пространства группы, Виды могут быть отсечены по краям.


</div>

![](images/TechDraw_Clipview.png ) 
*Группа Видов, содержащая в себе несколько Видов отсеченных по краям*



## Применение


<div class="mw-translate-fuzzy">

-   Нажмите кнопку **<img src="images/TechDraw_ClipGroup.svg" width=16px> [Создать группу Видов](TechDraw_ClipGroup/ru.md)** для создания новой группы Видов.


</div>



## Свойства

See also: [Property editor](Property_editor.md).

A Clip Group, formally a {{Incode|TechDraw::DrawViewClip}} object, has the [properties](TechDraw_View#Properties_Part_View.md) that are common to all View types. It also has the following additional properties.

### Data


{{TitleProperty|Clip Group}}


<div class="mw-translate-fuzzy">

-    **Width**: Ширина окна отсечения в единицах измерения

-    **Height**: Высота окна отсечения в единицах измерения

-    **ShowFrame**: Если true, вокруг пространства группы, будет отображаться рамка

-    **ShowLabels**: Если true, метки видов будут отображаться в группе. **ПРИМЕЧАНИЕ:** удалено в версии 0.19.

-    **Views**: Список Видов, содержащихся в группе


</div>


<div class="mw-translate-fuzzy">





</div>


{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ClipGroup/ru
