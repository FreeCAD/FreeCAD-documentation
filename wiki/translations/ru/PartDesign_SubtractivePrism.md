---
 GuiCommand:
   Name/ru: Субтрактивная призма
   Name: PartDesign_SubtractivePrism
   MenuLocation: Part Design , Создать субтрактивный примитив , Субтрактивная призма
   Workbenches: PartDesign_Workbench/ru
   Version: 0.17
   SeeAlso: PartDesign_CompPrimitiveSubtractive/ru, PartDesign_AdditivePrism/ru
---

# PartDesign SubtractivePrism/ru



## Описание

Вставляет субтрактивную призму в активное Тело. Её форма вычитается из существующего тела.

![](images/PartDesign_SubtractivePrism_example.svg )

*Слева: активное тело (A) отображено серым цветом, к которому добавлена субтрактивная призма (B) отображена прозрачным красным цветом. Справа: форма полученная в результате преобразования.*



## Применение

1.  Нажмите кнопку **<img src="images/PartDesign_SubtractivePrism.svg" width=24px> '''Субтрактивная призма'''**. **Примечание**: Инструмент Субтрактивная призма входит в состав меню с названием \"Создать субтрактивная примитив\". После запуска FreeCAD на панели инструментов в этом меню по умолчанию отображается инструмент Субтрактивная куб. Чтобы перейти к кнопке создания Призмы, нажмите на стрелку указывающую вниз рядом со значком и выберите Аддитивная призма в выпадающем меню.
2.  Установите параметры геометрической формы и [настройки крепления](Part_EditAttachment/ru.md) к уже существующим конструктивным элементам, если это требуется.
3.  Нажмите **OK**.
4.  Конструктивный элемент Призма появится в иерархии документа под активным Телом.



## Опции


<div class="mw-translate-fuzzy">

Возможно также создавать наклонные призмы, указав углы наклона её боковых рёбер относительно плоскости основания. {{Version/ru|0.19}}


</div>

Параметры Призмы после её создания можно изменить двумя способами:

-   Дважды щелкнув по ней в дереве модели или щелкнув правой кнопкой мыши и выбрав **Редактировать примитив** в контекстном меню; это откроет окно параметров примитива.
-   Через [Редактор свойств](Property_editor/ru.md).



## Свойства

-    **Attachment**: defines the attachment mode as well as the Attachment Offset. See [Part EditAttachment](Part_EditAttachment.md).

-    **Label**: label given to the Prism object. Change to suit your needs.

-    **Polygon**: number of sides in the polygon cross-section of the prism.

-    **Circumradius**: [circumscribed radius](https://en.wikipedia.org/wiki/Circumscribed_circle) of the polygon cross-section of the prism.

-    **Height**: height of the prism.

-    **First Angle**: angle in first direction.

-    **Second Angle**: angle in second direction.



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractivePrism/ru
