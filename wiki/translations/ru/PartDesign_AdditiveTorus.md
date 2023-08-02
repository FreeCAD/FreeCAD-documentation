---
- GuiCommand:
   Name/ru: Аддитивный тор
   Name: PartDesign_AdditiveTorus
   MenuLocation: Part Design -> Создать аддитивный примитив -> Аддитивный Тор
   Workbenches: PartDesign_Workbench/ru
   Version: 0.17
   SeeAlso: PartDesign_CompPrimitiveAdditive/ru, PartDesign_SubtractiveTorus/ru
---

# PartDesign AdditiveTorus/ru

## Описание

Вставляет в активное Тело простую геометрическую форму - тор, в качестве базового конструктивного элемента, или объединяет этот элемент с уже существующей совокупностью конструктивных элементов.

<img alt="" src=images/PartDesign_AdditiveTorus_example.png  style="width:200px;">

## Применение

1.  Нажмите кнопку **<img src="images/PartDesign_AdditiveTorus.svg" width=24px> '''Аддитивный тор'''**. **Примечание**: Инструмент Аддитивный тор входит в состав меню с названием \"Создать аддитивный примитив\". После запуска FreeCAD на панели инструментов в этом меню по умолчанию отображается инструмент Аддитивный куб. Чтобы перейти к кнопке создания Тора, нажмите на стрелку указывающую вниз рядом со значком и выберите Аддитивный тор в выпадающем меню.
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

-    **Angle1**: (labelled *V parameter* in the Primitive parameters) lower truncation of the torus, parallel to the circular cross section (-180 degrees in a full torus). A bug in the sources causes unexpected results at changing Angle1.

-    **Angle2**: (unlabelled in the Primitive parameters) upper truncation of the ellipsoid, parallel to the circular cross section (180 degrees in a full torus). A bug in the sources causes unexpected results at changing Angle2.

-    **Angle3**: (labelled *U parameter* in the Primitive parameters) angle of rotation of the circular cross section (360 degrees in a full torus).





{{PartDesign_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveTorus/ru
