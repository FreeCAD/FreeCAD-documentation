---
- GuiCommand:/ru
   Name/ru:Субтрактивный тор
   Name:PartDesign_SubtractiveTorus
   MenuLocation:Part Design → Создать субтрактивный примитив → Субтрактивный тор
   Workbenches:[PartDesign](PartDesign_Workbench/ru.md)
   Version:0.17
   SeeAlso:[Создать субтрактивный примитив](PartDesign_CompPrimitiveSubtractive/ru.md), [Аддитивный тор](PartDesign_AdditiveTorus/ru.md)
---

# PartDesign SubtractiveTorus/ru

## Описание

Вставляет субтрактивный тор в активное Тело. Его форма вычитается из существующего тела.

![](images/PartDesign_SubtractiveTorus_example.svg ) *Слева: активное тело (A) отображено серым цветом, к которому добавлен субтрактивный тор (B) отображен прозрачным красным цветом. Справа: форма полученная в результате преобразования.*

## Применение

1.  Нажмите кнопку **<img src="images/PartDesign_SubtractiveTorus.svg" width=24px> '''Субтрактивный тор'''**. **Примечание**: Инструмент Субтрактивный тор входит в состав меню с названием \"Создать субтрактивный примитив\". После запуска FreeCAD на панели инструментов в этом меню по умолчанию отображается инструмент Аддитивный куб. Чтобы перейти к кнопке создания Тора, нажмите на стрелку указывающую вниз рядом со значком и выберите Субтрактивный тор в выпадающем меню.
2.  Установите параметры геометрической формы и [настройки крепления](Part_EditAttachment/ru.md) к уже существующим конструктивным элементам, если это требуется.
3.  Нажмите **OK**.
4.  Конструктивный элемент Тор появится в иерархии документа под активным Телом.

## Опции

Параметры Тора после его создания можно изменить двумя способами:

-   Дважды щелкнув по нему в дереве модели или щелкнув правой кнопкой мыши и выбрав **Редактировать примитив** в контекстном меню; это откроет окно параметров примитива.
-   Через [Редактор свойств](Property_editor/ru.md).

## Свойства

-    **Attachment**: defines the attachment mode as well as the Attachment Offset. See [Part EditAttachment](Part_EditAttachment.md).

-    **Label**: Label given to the Torus object. Change to suit your needs.

-    **Radius1**: Radius of the imaginary orbit around which the circular cross-section revolves. (The distance between the center of the torus and the center of the revolving cross section)

-    **Radius2**: Radius of the circular cross-section defining the form of the torus.

-    **Angle1**: (labelled *V parameter* in the Primitive parameters) lower truncation of the torus, parallel to the circular cross section (-180° in a full torus). A bug in the sources causes unexpected results at changing Angle1.

-    **Angle2**: (unlabelled in the Primitive parameters) upper truncation of the ellipsoid, parallel to the circular cross section (180° in a full torus). A bug in the sources causes unexpected results at changing Angle2.

-    **Angle3**: (labelled *U parameter* in the Primitive parameters) angle of rotation of the circular cross section (360° in a full torus).





{{PartDesign_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveTorus/ru
