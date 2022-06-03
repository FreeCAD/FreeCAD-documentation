# Sketch/ru
## Введение


{{TOCright}}

В FreeCAD слово \"[Sketch(Эскиз)](Sketch/ru.md)\" обычно используется для обозначения [Sketcher SketchObject](Sketcher_SketchObject/ru.md) (`Sketcher   *   *SketchObject` класс), который определяется [Верстаком Sketcher](Sketcher_Workbench/ru.md). Это 2D-чертеж, который использует математические ограничения для точного описания 2D-геометрии.

Дополнительные сведения об этом типе объектов см. в разделе [Sketcher SketchObject](Sketcher_SketchObject/ru.md).

## Использование

Существует два наиболее распространенных способа создания эскиза   * непосредственно с помощью [верстака Sketcher](Sketcher_Workbench/ru.md) или через [верстак PartDesign](PartDesign_Workbench/ru.md).

### Верстак Sketcher 

1.  Переключитесь на <img alt="" src=images/Workbench_Sketcher.svg  style="width   *16px;"> [верстак Sketcher](Sketcher_Workbench/ru.md).
2.  Нажмите на **[<img src=images/Sketcher_NewSketch.svg style="width   *16px"> [Создать новый эскиз](Sketcher_NewSketch/ru.md)**.

### Верстак PartDesign 

1.  Переключитесь на <img alt="" src=images/Workbench_PartDesign.svg  style="width   *16px;"> [Верстак PartDesign](PartDesign_Workbench/ru.md).
2.  Нажмите на **[<img src=images/PartDesign_Body.svg style="width   *16px"> [Создать новое тело](PartDesign_Body/ru.md)**.
3.  Нажмите на **[<img src=images/PartDesign_NewSketch.svg style="width   *16px"> [Создать эскиз](PartDesign_NewSketch/ru.md)**.

После завершения редактирования эскиза закройте его, чтобы выйти из режима редактирования. Дважды щёлкните по нему, чтобы снова войти в режим редактирования.

## Примечания

Эскиз обычно используется вместе с <img alt="" src=images/Workbench_PartDesign.svg  style="width   *16px;"> [верстаком PartDesign](PartDesign_Workbench/ru.md) для создания твёрдых тел выдавливанием, используя операцию **[<img src=images/PartDesign_Pad.svg style="width   *16px"> [Выдавить выбранный эскиз](PartDesign_Pad/ru.md)**.

Тем не менее, Эскиз(Sketch) всегда может быть создан сам по себе для любой другой цели; он не обязан быть привязан к [Создать новое тело](PartDesign_Body/ru.md) верстака PartDesign. Например, инструмент **[<img src=images/Arch_Window.svg style="width   *16px"> [Arch Window(Окно)](Arch_Window.md)** в <img alt="" src=images/Workbench_Arch.svg  style="width   *16px;"> [Верстаке Arch](Arch_Workbench.md) использует эскизы для определения формы окон и дверей; точно так же эскиз может быть использован для определения формы **[<img src=images/Arch_Wall.svg style="width   *16px"> [Arch Walls(Стен)](Arch_Wall.md)**.


{{Sketcher Tools navi

}} {{Document objects navi}} 

[Category   *Glossary](Category_Glossary.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Glossary](Category_Glossary.md) > [Sketcher](Category_Sketcher.md) > Sketch/ru
