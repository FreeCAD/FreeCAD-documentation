---
- GuiCommand:/ru
   Name:FEM MaterialSolid
   Name/ru:FEM MaterialSolid 
   MenuLocation:Model → FEM material for solid
   Workbenches:[FEM](FEM_Workbench/ru.md)
   Shortcut:**M** **M**
   SeeAlso:[FEM tutorial](FEM_tutorial/ru.md)
---

# FEM MaterialSolid/ru


</div>

## Описание

Добавляет свойства материала к детали.

![](images/FEMMaterialSolidProperties.png ) 
*The FEM material task panel*

## Использование


<div class="mw-translate-fuzzy">

-   Щелкните <img alt="" src=images/FEM_MaterialSolid.svg  style="width:32px;"> или выберите **Model** → **<img src="images/FEM_MaterialSolid.svg" width=32px> FEM material for solid** в верхнем меню.
-   Дважды щелкните созданный объект **<img src="images/FEM_MaterialSolid.svg" width=32px> SolidMaterial
**

![](images/FEMMaterialSolidProperties.png )

-   -   Выберите материал. Для инженерного механического анализа типичным вариантом является **CalculiX-Steel**.
    -   Если вы применяете материал ко всему объекту, не выбирайте никакие геометрические объекты (оставьте список ссылок пустым). Материал будет применён ко всей модели. В противном случае присвойте материал конкретным деталям модели вручную, выбрав некоторые из них для каждого вставленного материала, но не оставляйте никакую часть модели без назначенного материала.
    -   Вы можете настроить свойства материала, такие как плотность, модуль Юнга, коэффициент Пуассона и т. Д., Однако большинство распространенных материалов уже доступно в предустановках, и их не нужно настраивать.
    -   Если вы внесете изменения, вы можете сохранить индивидуальный материал.

-   Нажмите **Close**, чтобы закрыть диалоговое окно и создать объект **<img src="images/FEM_MaterialSolid.svg" width=32px> SolidMaterial
**


</div>

## Примечания


<div class="mw-translate-fuzzy">

1.  Механический материал использует карту \*MATERIAL в CalculiX. Подробности о механическом материале объясняются на <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node216.html>


</div>


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MaterialSolid/ru
