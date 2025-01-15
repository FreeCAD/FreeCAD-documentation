---
 GuiCommand:
   Name/ru: Проект
   Name: Arch_Project
   MenuLocation: Arch , Проект
   Workbenches: Arch_Workbench/ru
   Shortcut: **P** **O**
   SeeAlso: Arch_Site/ru, Arch_Building/ru
---

# Arch Project/ru



## Описание

Проект Arch - это специальный объект, предназначенный для улучшения совместимости с [IFC](Arch_IFC/ru.md) файлами. Каждый файл IFC должен содержать [IfcProject](https://standards.buildingsmart.org/IFC/RELEASE/IFC4_1/FINAL/HTML/schema/ifckernel/lexical/ifcproject.htm) сущность. IfcProject в основном используется для определения общих параметров проекта, таких как проекционные системы, для совместимости с GIS или системы единиц измерения.

При экспорте модели FreeCAD в формат файла IFC, если ваша модель не содержит какого-либо объекта проекта, автоматически будет создан объект по умолчанию, чего в большинстве случаев будет достаточно. Однако вы можете захотеть иметь возможность точно настроить параметры проекта, и в этом случае добавление объекта проекта может оказаться полезным. При импорте файла IFC всегда будет создаваться объект проекта. Однако, если вы специально не используете его, вы можете просто удалить его после импорта.

Note that, although any other BIM object can be added to a Project, which the IFC standard does not prohibit, the common way of doing is always to only have [sites](Arch_Site.md) or [buildings](Arch_Building.md) as direct children of a project. All other BIM objects should be inside these sites or buildings. The Project itself should always be at the top of your model structure, that is, it shouldn\'t be included in any other object.



## Применение

1.  Нажмите кнопку **<img src="images/Arch_Project.svg" width=16px> [Проект](Arch_Project/ru.md)** или нажмите клавиши **P**, затем **O**.
2.  Добавьте любой объект в свой проект, перетащив его в Проект находящийся в [иерархии документа](Tree_view/ru.md).


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch Project/ru
