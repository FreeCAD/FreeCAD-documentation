---
- GuiCommand:/ru
   Name:Arch ToggleIfcBrepFlag
   Name/ru:Arch ToggleIfcBrepFlag
   MenuLocation:Архитектура → Утилиты → Toggle Ifc Brep flag
   Workbenches:[Arch](Arch_Workbench/ru.md)
   Shortcut:
   SeeAlso:[Arch IfcExplorer](Arch_IfcExplorer.md), [Arch IFC](Arch_IFC.md)
---

# Arch ToggleIfcBrepFlag/ru


</div>

## Описание


<div class="mw-translate-fuzzy">

Этот инструмент включает / выключает флаг IfcBrep выбранного объекта [ Arch](Arch_Workbench/ru.md) (значение по умолчанию всегда выключено). Если флаг включен, при экспорте в IFC объект будет экспортироваться как [IfcFacetedBrep](http://www.buildingsmart-tech.org/ifc/IFC4/final/html/schema/ifcgeometricmodelresource/lexical/ifcfacetedbrep.htm) объект, даже если возможен экспорт более высокого уровня, например IfcExtrudedAreaSolid или IfcBooleanResult. Хотя объекты IfcFacetedBrep более тяжелые и менее редактируемые (они теряют некоторую информацию о геометрии, такую ​​как история моделирования), они часто менее подвержены ошибкам. Установка этого флага позволяет разрешить некоторые случаи объектов, которые не экспортируются правильно, когда флаг не установлен.


</div>


<div class="mw-translate-fuzzy">

## Использование


</div>


<div class="mw-translate-fuzzy">

1.  Выберите объект Arch
2.  Выберите менюArch → Utilities → **<img src="images/Arch_ToggleIfcBrepFlag.png" width=16px> [Toggle IfcBrepFlag](Arch_ToggleIfcBrepFlag.md)
**


</div>

---
[documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch ToggleIfcBrepFlag/ru
