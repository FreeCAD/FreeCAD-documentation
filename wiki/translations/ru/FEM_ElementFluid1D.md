---
 GuiCommand:
   Name/ru: Одномерная секция для текучего вещества
   Name: FEM_ElementFluid1D
   MenuLocation: Модель , Геометрия элемента , Одномерная секция для текучего вещества
   Workbenches: FEM_Workbench/ru
   SeeAlso: FEM_tutorial/ru
---

# FEM ElementFluid1D/ru



## Описание

Создает секцию для анализа жидкостей методом конечных элементов в пневматических и гидравлических сетях.



## Применение


<div class="mw-translate-fuzzy">

1.  Существует несколько способов вызова команды:
    -   Нажмите кнопку **<img src="images/FEM_ElementFluid1D.svg" width=16px> [FEM ElementFluid1D](FEM_ElementFluid1D.md)**.
    -   Или выберите пункт меню **Model → Element Geometry → <img src="images/FEM_ElementFluid1D.svg" width=16px> Fluid section for 1D flow**.
2.  Выберите тип жидкости: жидкость, газ или открытый канал
3.  Выберите тип секции: заполнение трубы, ввод трубы и т.д.
4.  Введите параметры типа раздела.
5.  Выберите и добавьте ребро.


</div>



## Ограничения

1.  Карта работает только с 3 узловыми конечными элементами. Подробную информацию можно см. : <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node54.html>



## Примечания

1.  С примером построения гидравлической системы трубопроводов можно ознакомится по ссылке: <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node13.html>
2.  Модель расчета **fluid elements for 1D flow** использует \*FLUID SECTION параметры карточки материала. Подробную информацию о данном разделе параметров можно найти здесь:


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ElementFluid1D/ru
