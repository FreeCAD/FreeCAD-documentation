# Manual:Import and export to other filetypes/ru
{{Manual:TOC/ru}}

FreeCAD может импортировать и экспортировать во множество типов файлов. Здесь приведён список наиболее важных из них с коротким описанием доступных особенностей:

  Формат   Импорт   Экспорт   Примечания
     
  STEP     Да       Да        Это наиболее точный из доступных форматов импорта/экспорта, поскольку он поддерживает твердотельную геометрию и NURBS. Используйте их где только можно.
  IGES     Да       Да        Более старый твердотельный формат, так же хорошо поддерживаемый. Некоторые старые приложения не поддерживают STEP, но имеют поддержку IGES.
  BREP     Да       Да        Внутренний формат [OpenCasCade](https://ru.wikipedia.org/wiki/Open_Cascade_Technology), геометрического ядра FreeCAD.
  DXF      Да       Да        Открытый формат, поддерживаемый Autodesk. Поскольку трёхмерные данные в DXF кодированы в закрытом формате, FreeCAD может импортировать/экспортировать только двумерные данные из этого формата.
  DWG      Да       Да        Закрытая версия DXF. Требует установки утилиты [Teigha File Converter](https://www.opendesign.com/guestfiles). Этот формат страдает от тех же ограничений, что и DXF.
  OBJ      Да       Да        Формат, основанный на полигональных сетках. Может содержать лишь треугольные сетки. Все твердые тела и базирующиеся на NURBS объекты FreeCAD будут при экспорте преобразованы в сетки. Альтернативный экспортёр обеспечивается верстаком Arch, более приспособленный для экспорта архитектурных моделей.
  DAE      Да       Да        Главный формат импорта/экспорта Sketchup. Может содержать лишь треугольные сетки. Все твёрдые тела и базирующиеся на NURBS объекты FreeCAD будут при экспорте преобразованы в сетки.
  STL      Да       Да        Формат, основанный на полигональных сетках, широко используемый для трёхмерной печати. Может содержать лишь треугольные сетки. Все твёрдые тела и базирующиеся на NURBS объекты FreeCAD будут при экспорте преобразованы в сетки.
  PLY      Да       Да        Старый базирующийся на полигональных сетках формат. Может содержать лишь треугольные сетки. Все твёрдые тела и базирующиеся на NURBS объекты FreeCAD будут при экспорте преобразованы в сетки.
  IFC      Да       Да        [Industry Foundation Classes](https://ru.wikipedia.org/wiki/Industry_Foundation_Classes). Требует установки [IfcOpenShell-python](http://ifcopenshell.org/python). Формат IFC и его совместимость с другими приложениями очень сложное дело, использовать с осторожностью.
  SVG      Да       Да        Превосходный, широко распространённый двумерный графический формат
  VRML     Да       Да        Немного устаревший, базирующийся на полигональных сетках web-формат.
  GCODE    Да       Да        FreeCAD теперь может импортировать и экспортировать в некоторые варианты G-кода, но сейчас поддерживается лишь небольшой набор машин.
  CSG      Да       Нет       Формат OpenSCAD [CSG](https://en.wikipedia.org/wiki/Constructive_solid_geometry) (Constructive Solid Geometry).

Некоторые из этих форматов имеют опции. Они могут быть сконфигурированы через меню **Правка → Параметры → Импорт/экспорт:**

![](images/Import_preferences.jpg )

**Читать далее**


<div class="mw-translate-fuzzy">

-   [Все форматы файлов, поддерживаемые FreeCAD](Import_Export/ru.md)
-   [Работа с файлами DXF в FreeCAD](Draft_DXF/ru.md):
-   [Включение поддержки DXF и DWG](Dxf_Importer_Install/ru.md)
-   [Работа с файлами SVG в FreeCAD](Draft_SVG/ru.md)
-   [Импорт и экспорт в IFC](Arch_IFC/ru.md)
-   [OpenCasCade](http://www.opencascade.com)
-   [Конвертер файлов Teigha](https://www.opendesign.com/guestfiles)
-   [Формат файлов IFC](http://www.buildingsmart-tech.org/ifc/IFC4/final/html/index.htm)
-   [IfcOpenShell](http://ifcopenshell.org/)


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > [Tutorials](Category_Tutorials.md) > Manual:Import and export to other filetypes/ru
