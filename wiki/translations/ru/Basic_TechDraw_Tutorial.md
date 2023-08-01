---
- TutorialInfo:/ru
   Topic:Моделирование
   Level:Для начинающих
   Author:[WandererFan](User_WandererFan.md)
   Time:Меньше часа
   FCVersion:0.17 и выше
   Files:[https://github.com/FreeCAD/Examples/blob/master/Basic_Part_Design_Tutorial_Example_017_Files/Basic_Part_Design_Tutorial_017.fcstd Разработка простой детали Basic в v0.17 Пример]<br />[https://github.com/FreeCAD/Examples/blob/master/Basic_TechDraw_Tutorial_Example_Files/Basic_TechDraw_Tutorial.fcstd Простое TechDraw руководство Пример]
---

# Basic TechDraw Tutorial/ru




<div class="mw-translate-fuzzy">




</div>

## Introduction


<div class="mw-translate-fuzzy">

## Введение

Это руководство для ознакомления начинающих пользователей с некоторыми инструментами и методами, используемыми в **<img src="images/Workbench_TechDraw.svg" width=24px> [верстаке технического черчения (TechDraw)](TechDraw_Workbench/ru.md)**. Это руководство не является полным и исчерпывающим, и многие инструменты и возможности в нем не рассматриваются. Данное руководство проведет пользователя по шагам, необходимым для создания технических чертежей из детали которая была спроектирована в [руководстве к PartDesign для начинающих](Basic_Part_Design_Tutorial/ru.md).


</div>

## Before You Begin 


<div class="mw-translate-fuzzy">

## Прежде чем начать 

Скачайте [файл содержащий 3D модель](https://github.com/FreeCAD/Examples/blob/master/Basic_Part_Design_Tutorial_Example_017_Files/Basic_Part_Design_Tutorial_017.fcstd) из руководства к верстаку Part Design.


</div>

## The Task 


<div class="mw-translate-fuzzy">

## Задание

В этом руководстве вы будете использовать верстак TechDraw для создания 2D-чертежей из 3D-детали. Мы создадим несколько видов детали и добавим ключевые размеры. В этом учебном пособии не будут использоваться все функции и инструменты, доступные в верстаке TechDraw, но этого должно быть достаточно, чтобы дать пользователю этого учебного пособия базовую основу, из которой можно будет развивать свои знания и навыки.


</div>



## Деталь

![](images/Tut17_final_refined.png )

## Creating a Drawing 

### Startup


<div class="mw-translate-fuzzy">

## Создание чертежа 

### Начало

-   Вы можете изменить [настройки](TechDraw_Preferences/ru.md) перед началом. Смотрите примечание 1.
-   Сначала откройте файл, содержащий нашу 3D деталь. Затем убедитесь, что вы находитесь в верстаке TechDraw.
-   Вы будете выбирать элементы в окне Drawing и/или на панели Combo. Выбор в TechDraw работает так же, как в 3D окне. Элементы становятся желтыми, когда курсор наводится на них, чтобы выбрать, и становятся зелеными, когда они выбраны. Чтобы выбрать несколько элементов, используйте клавишу **Ctrl** при нажатии.


</div>

### Views and Dimensions 


<div class="mw-translate-fuzzy">

### Виды и Размеры 

Вся работа в TechDraw начинается со страниц. Страницы основаны на Шаблонах и содержат Виды.

1.  Нажмите на <img alt="" src=images/TechDraw_PageDefault.svg  style="width:32px;"> [Новая Страница из Шаблона по умолчанию](TechDraw_PageDefault/ru.md) что бы создать новую страницу.
2.  Нажмите на Тело в [3D view](3D_view.md) или в [Combo view](Combo_view.md).
3.  Нажмите на <img alt="" src=images/TechDraw_View.svg  style="width:32px;"> [Создать новый вид](TechDraw_View/ru.md). Это добавит Вид на страницу, которую мы только что создали.


</div>

Теперь у нас есть Вид на Странице, смотрящий сверху на Тело. Однако, он выглядит немного мелким.

![](images/TDTut_TopView1to1.png )


<div class="mw-translate-fuzzy">

1.  Выберите Page в [Combo панели](Combo_view/ru.md) и выделите свойство Scale (Масштаб) на вкладке Данные.
2.  Измените Scale (Масштаб) с 1 на 2 и нажмите **Enter**. Вид станет больше.
3.  Перетащите Вид из блока документации наружу за правый нижний угол страницы.


</div>

![](images/TDTut_TopView2to1.png )


<div class="mw-translate-fuzzy">

Лучше, но немного скучновато. Давайте добавим немного размеров.

1.  Выберите верхнюю левую вершину (маленькая точка) нажатием **LMB**, затем выберите (**Ctrl**+**LMB**) нижнюю левую вершину.
2.  Кликните на <img alt="" src=images/TechDraw_VerticalDimension.svg  style="width:32px;"> [Новый Вертикальный Размер](TechDraw_VerticalDimension/ru.md). Перетащите текст размера за пределы тела.
3.  Повторите это с верхней левой и верхней правой вершинами и нажмите <img alt="" src=images/TechDraw_HorizontalDimension.svg  style="width:32px;"> [Новый Горизонтальный Размер](TechDraw_HorizontalDimension/ru.md).


</div>

![](images/TDTut_TopView2Dims.png )



### Заполнение основной надписи 

Основная надпись (или штамп) содержит совокупность сведений о проектном документе. Чтобы её заполнить требуется сделать следующие действия:

1.  Нажмите на маленький зеленый квадрат рядом с какой-либо надписью расположенной в штампе. В открывшемся диалоге, вы можете изменить надпись, или ввести её если она не заполнена.
2.  В качестве примера, можете просто ввести свое имя в поле Designed by Name таким же образом.

![](images/TDTut_DocBlock.png )

Чертеж выглядит теперь намного лучше. Давайте добавим текст на страницу.


<div class="mw-translate-fuzzy">

1.  Нажмите на <img alt="" src=images/TechDraw_Annotation.svg  style="width:32px;"> [Новая Аннотация](TechDraw_Annotation/ru.md). Текстовый блок появится в середине страницы.
2.  Перетащите текстовый блок за пределы Вида.
3.  Нажмите на Annotation в Combo панели и выделите свойство Text на вкладке Данные.
4.  Нажмите на многоточие справа в поле данных Значение. Вы получите всплывающее окно, где можете изменить текст на что-то более значимое.


</div>

![](images/TDTut_Annotation.png )

Прежде чем покинуть эту страницу, давайте посмотрим, как она будет выглядеть, когда мы ее распечатаем.


<div class="mw-translate-fuzzy">

1.  Нажмите на <img alt="" src=images/TechDraw_ToggleFrame.svg  style="width:32px;"> [Выключатель Рамки](TechDraw_ToggleFrame.md). Вершины и Рамки Видов исчезнут. Вы можете вернуть их обратно, нажав на Выключатель снова.


</div>

![](images/TDTut_Toggle.png )

### Multiple Views of a Single Part 


<div class="mw-translate-fuzzy">

### Несколько проекций детали 

Давайте создадим чертеж с несколькими проекциями, используя другой шаблон рамки в качестве основы. Мы будем использовать First Angle, но вы можете перейти на Third Angle, если это ваше местное соглашение.


</div>


<div class="mw-translate-fuzzy">

1.  Нажмите на <img alt="" src=images/TechDraw_PageTemplate.svg  style="width:32px;"> [Выбрать новый](TechDraw_PageTemplate/ru.md). Откроется диалоговое окно выбора файла. Выберите файл шаблона. Мы собираемся использовать \"ANSIB.SVG\". Появится новая вкладка.
2.  Выберите \"Body\" и \"Page001\" (если в вашем документе более одной страницы, вам нужно указать TechDraw, какую из них использовать).
3.  Нажмите на <img alt="" src=images/TechDraw_ProjectionGroup.svg  style="width:32px;"> [Группа Новых Проекций](TechDraw_ProjectionGroup/ru.md). Появится знакомый небольшой вид в середине страницы, и на панели задач появится диалоговое окно.
4.  Нажмите на несколько полей в разделе Secondary Views (Вторичные проекции) диалогового окна.
5.  Двигайте Вид с надписью \"Front\". Все остальные Виды будут двигаться вместе с ним.
6.  Измените раскрывающийся список Scale у Page на Custom и измените Custom Scale (Пользовательский Масштаб) на 2:1. Нажмите кнопку ОК.


</div>

![](images/TDTut_ProjGroup21.png )


<div class="mw-translate-fuzzy">

1.  У Вида с меткой «TopLeftFront» выберите две Вершины на крайних концах переднего края заготовки.
2.  Нажмите на <img alt="" src=images/TechDraw_LengthDimension.svg  style="width:32px;"> [Новая длина](TechDraw_LengthDimension/ru.md). Перетащите текст размера за пределы тела.


</div>

### Linking Dimensions to 3D Model 


<div class="mw-translate-fuzzy">

### Связывание размеров с 3D-моделью 

Вы заметили проблему с размером, который мы только что создали?


</div>

![](images/TDTut_NewLengthDim.png )


<div class="mw-translate-fuzzy">

Из первой части этого урока мы знаем, что заготовка имеет ширину 53 мм, но наш новый размер читаются как 43,27. Это связано с тем, что \"TopLeftFront\" является [изометрической проекцией](https://en.wikipedia.org/wiki/Isometric_projection), а наш первый рисунок был [ортогональной проекцией](https://en.wikipedia.org/wiki/Orthographic_projection). Чтобы получить правильное значение, нам нужно связать наше измерение непосредственно с 3D-моделью.


</div>


<div class="mw-translate-fuzzy">

1.  Обратите внимание на название нашего ошибочного измерения на Combo панели. Нам оно понадобится через минуту.
2.  Перейдите на вкладку 3D и выберите вершины на концах переднего края заготовки. Также выберите Page001 (Страница, с которой нужно размер).
3.  Нажмите на <img alt="" src=images/TechDraw_LinkDimension.svg  style="width:32px;"> [Новые ссылки](TechDraw_LinkDimension/ru.md). На панели задач откроется диалоговое окно.
4.  В диалоговом окне переместите наши размеры из доступного столбца в выбранный столбец (Здесь нужно выбрать из доступных размеров тот, который некорректен и который мы хотим исправить, связав его с реальным размером на детали). Нажмите ОК.
5.  Возвращаемся к Page001. Наш размер должен показывать корректное значение 53. (если вы все еще видите 43.27, нужно нажать кнопку Recompute (Пересчитать - F5) или немного потянуть значение размера, пока оно не изменится.)


</div>



## Идём дальше 

В этом руководстве вы узнали достаточно о TechDraw, чтобы создать рисунок, подобный этому (by [NormandC](User_Normandc.md)). Смотрите примечание 2.

![](images/TDTut_FC018_TechDraw_Dim_Iso_View_01_NC.png )

В TechDraw имеется гораздо больше функциональных возможностей, которые вы можете изучить: сечения Видов, Виды частей детали, технические знаки SVG, возможность добавления растровых изображений, штриховка областей.

## Notes


<div class="mw-translate-fuzzy">

## Примечания

1.  Существует отличный набор предлагаемых предпочтений в этом [сообщении Форума](https://www.forum.freecadweb.org/viewtopic.php?f=3&t=30083#p248189).
2.  Этот рисунок был создан в версии v0.18. Он показывает размеры в правильном формате для изометрической проекции. В версии v0.17 выносные линии будут перпендикулярны краю, а не выровнены с осями.


</div>



## Дополнительные ресурсы 


<div class="mw-translate-fuzzy">

-   FreeCAD файл этого упражнения для сравнения (создан в версии 0.17) [Скачать](https://github.com/FreeCAD/Examples/blob/master/Basic_TechDraw_Tutorial_Example_Files/Basic_TechDraw_Tutorial.fcstd)


</div>


{{TechDraw Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [TechDraw](Category_TechDraw.md) > Basic TechDraw Tutorial/ru
