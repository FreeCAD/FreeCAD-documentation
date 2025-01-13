# Manual:Import and export to other filetypes/ro
{{Manual:TOC}}


<div class="mw-translate-fuzzy">

FreeCAD poate importa și exporta multe tipuri de fișiere. Iată o listă cu cele mai importante, cu o scurtă descriere a caracteristicilor disponibile:


</div>


<div class="mw-translate-fuzzy">

  Format   Import   Export   Notes
     
  STEP     Yes      Yes      Acesta este cel mai fidel format import / export disponibil, deoarece susține geometria solidă și NURBS. Utilizați-l ori de câte ori este posibil.
  IGES     Yes      Yes      Un format solid mai vechi, de asemenea foarte bine susținut. Unele aplicații mai vechi nu acceptă PAS, dar au IGES.
  BREP     Yes      Yes      Formatul nativ al Open Cascade Technology [OpenCasCade](https://en.wikipedia.org/wiki/Open_Cascade_Technology), FreeCAD\'s geometry kernel.
  DXF      Yes      Yes      Un format deschis întreținut de Autodesk. Deoarece datele 3D din interiorul unui fișier DXF sunt codificate în format propriu, FreeCAD poate importa / exporta date 2D în / din acest format.
  DWG      Yes      Yes      Versiunea proprietară a DXF. Necesită instalarea [Teigha File Converter](https://www.opendesign.com/guestfiles) utility. Acest format suferă de aceleași limitări ca și DXF.
  OBJ      Yes      Yes      Un format bazat pe plasă. Poate conține numai ochiuri triunghiulare. Toate obiectele solide și bazate pe NURBS ale FreeCAD vor fi convertite în plasă la export. Un exportator alternativ este furnizat de atelierul de lucru Arch, mai potrivit exportului de modele arhitecturale.
  DAE      Yes      Yes      Principalul format import / export al lui Sketchup. Poate conține numai ochiuri triunghiulare. Toate obiectele solide și bazate pe NURBS ale FreeCAD vor fi convertite în plasă la export.
  STL      Yes      Yes      Un format bazat pe plasă, utilizat în mod obișnuit pentru imprimarea 3D. Poate conține numai ochiuri triunghiulare. Toate obiectele solide și bazate pe NURBS ale FreeCAD vor fi convertite în plasă la export.
  PLY      Yes      Yes      Un format mai vechi bazat pe plasă. Poate conține numai ochiuri triunghiulare. Toate obiectele solide și bazate pe NURBS ale FreeCAD vor fi convertite în plasă la export.
  IFC      Yes      Yes      [Industry Foundation Classes](https://en.wikipedia.org/wiki/Industry_Foundation_Classes). Necesită instalarea a [IfcOpenShell-python](http://ifcopenshell.org/python.html). Formatul IFC și compatibilitatea acestuia cu alte aplicații este o afacere complexă, a se utiliza cu atenție.
  SVG      Yes      Yes      Un excelent, larg răspândit format pentru grafică 2D
  VRML     Yes      Yes      Un format web vechi bazat pe plasă.
  GCODE    Yes      Yes      FreeCAD poate deja să importe și să exporte în / de la mai multe dialecte GCode, dar în acest moment este suportat doar un număr mic de mașini.
  CSG      Yes      No       OpenSCAD\'s [CSG](https://en.wikipedia.org/wiki/Constructive_solid_geometry) (Constructive Solid Geometry) format.


</div>


<div class="mw-translate-fuzzy">

Unele dintre aceste formate de fișiere au opțiuni. Acestea pot fi configurate din meniu **Edit -\> Preferences -\> Import/export:**


</div>


<div class="mw-translate-fuzzy">

![](images/Import_preferences.jpg )


</div>

**De citit în plus**


<div class="mw-translate-fuzzy">

-   [All file formats supported by FreeCAD](Import_Export.md)
-   [Working with DXF files in FreeCAD](Draft_DXF.md):
-   [Working with SVG files in FreeCAD](Draft_SVG.md)
-   [Importing and exporting to IFC](Arch_IFC.md)
-   [OpenCasCade](http://www.opencascade.com)
-   [Teigha File Converter](https://www.opendesign.com/guestfiles)
-   [The IFC format](http://www.buildingsmart-tech.org/ifc/IFC4/final/html/index.htm)
-   [IfcOpenShell](http://ifcopenshell.org/)


</div>



---
⏵ [documentation index](../README.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > [Tutorials](Category_Tutorials.md) > Manual:Import and export to other filetypes/ro
