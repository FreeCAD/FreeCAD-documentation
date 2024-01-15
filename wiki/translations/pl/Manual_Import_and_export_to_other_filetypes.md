# Manual:Import and export to other filetypes/pl
{{Manual:TOC}}

FreeCAD może importować i eksportować projekty do wielu formatów plików. Oto lista najważniejszych z nich wraz z krótkim opisem dostępnych funkcji:

  Format   Import   Eksport   Uwagi
     
  STEP     Tak      Tak       Jest to najwierniejszy dostępny format importu/eksportu, ponieważ obsługuje geometrię bryłową i NURBS. Należy go używać zawsze, gdy jest to możliwe.
  IGES     Tak      Tak       Starszy format bryłowy, również bardzo dobrze obsługiwany. Niektóre starsze aplikacje nie obsługują STEP, ale mają IGES.
  BREP     Tak      Tak       Natywny format [OpenCasCade](https://en.wikipedia.org/wiki/Open_Cascade_Technology), jądra geometrii FreeCAD.
  DXF      Tak      Tak       Otwarty format utrzymywany przez Autodesk. Ponieważ dane 3D wewnątrz pliku DXF są zakodowane w zastrzeżonym formacie, FreeCAD może importować / eksportować tylko dane 2D do / z tego formatu.
  DWG      Tak      Tak       Zastrzeżona wersja DXF. Wymaga instalacji narzędzia [Konwerter plików Teigha](https://www.opendesign.com/guestfiles). Format ten ma takie same ograniczenia jak DXF.
  OBJ      Tak      Tak       Format oparty na siatce. Może zawierać tylko siatki triangulacyjne. Wszystkie obiekty bryłowe i oparte na NURBS FreeCAD zostaną przekonwertowane na siatkę podczas eksportu. Alternatywny eksporter jest dostarczany przez środowisko robocze Arch, bardziej odpowiednie do eksportu modeli architektonicznych.
  DAE      Tak      Tak       Główny format importu i eksportu programu Sketchup. Może zawierać tylko siatki triangulacyjne. Wszystkie obiekty bryłowe i oparte na NURBS programu FreeCAD zostaną przekonwertowane na siatkę podczas eksportu.
  STL      Tak      Tak       Format oparty na siatce, powszechnie używany do drukowania 3D. Może zawierać tylko siatki trójkątów. Wszystkie obiekty bryłowe i oparte na NURBS FreeCAD zostaną przekonwertowane na siatkę podczas eksportu.
  PLY      Tak      Tak       Starszy format oparty na siatce. Może zawierać tylko siatki trójkątów. Wszystkie obiekty bryłowe i oparte na NURBS w FreeCAD zostaną przekonwertowane na siatkę podczas eksportu.
  IFC      Tak      Tak       [Industry Foundation Classes](https://en.wikipedia.org/wiki/Industry_Foundation_Classes). Wymaga instalacji [IfcOpenShell-python](http://ifcopenshell.org/python). Format IFC i jego kompatybilność z innymi aplikacjami jest skomplikowana, należy zachować ostrożność.
  SVG      Tak      Tak       Doskonały, szeroko rozpowszechniony format grafiki 2D
  VRML     Tak      Tak       Dość stary format sieciowy oparty na siatce.
  GCODE    Tak      Tak       FreeCAD może już importować i eksportować do / z kilku odmian GCode, ale obecnie obsługiwana jest tylko niewielka liczba maszyn.
  CSG      Tak      Nie       Format OpenSCAD [CSG](https://en.wikipedia.org/wiki/Constructive_solid_geometry) Geometria konstrukcyjna brył *(Constructive Solid Geometry)*.

Niektóre z tych formatów plików mają opcje konfiguracyjne. Można je przeglądnąć i zmienić w menu **Edycja → Preferencje ...→ Import / eksport:**.

![](images/Import_preferences.jpg )

**Więcej informacji:**

-   [Wszystkie formaty plików obsługiwane przez FreeCAD](Import_Export/pl.md)
-   [Praca z plikami DXF w programie FreeCAD](Draft_DXF/pl.md):
-   [Praca z plikami SVG w programie FreeCAD](Draft_SVG/pl.md)
-   [Importowanie i eksportowanie do IFC](Arch_IFC/pl.md)
-   [OpenCasCade](http://www.opencascade.com)
-   [Konwerter plików Teigha](https://www.opendesign.com/guestfiles)
-   [Baza danych specyfikacji IFC](https://technical.buildingsmart.org/standards/ifc/ifc-schema-specifications/)
-   [IfcOpenShell](http://ifcopenshell.org/)



---
⏵ [documentation index](../README.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > [Tutorials](Category_Tutorials.md) > Manual:Import and export to other filetypes/pl
