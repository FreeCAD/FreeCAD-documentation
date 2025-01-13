---
 GuiCommand:
   Name: FEM MaterialSolid
   Name/ru: FEM MaterialSolid 
   MenuLocation: Model , Materials , Material for solid
   Workbenches: FEM_Workbench/ru
   Shortcut: **M** **M**
   SeeAlso: FEM_tutorial/ru
---

# FEM MaterialSolid/ru


</div>



## Описание


<div class="mw-translate-fuzzy">

Добавляет свойства материала к детали.


</div>

![](images/FEMMaterialSolidProperties.png ) 
*Внешний вид панели материалов верстака МКЭ*



## Применение


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





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MaterialSolid/ru
