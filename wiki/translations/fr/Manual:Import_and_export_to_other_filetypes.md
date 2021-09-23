# Manual:Import and export to other filetypes/fr
 


{{Manual:TOC/fr}}

FreeCAD peut importer et exporter vers plusieurs types de fichiers. Voici une liste des plus importants avec une brève description des caractéristiques disponibles :

  Format   Import   Export   Notes
  -------- -------- -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  STEP     Oui      Oui      C\'est le format d\'importation/exportation le plus fidèle disponible, car il supporte la géométrie solide et NURBS. Utilisez le chaque fois que cela est possible.
  IGES     Oui      Oui      Un format solide ancien, également très bien pris en charge. Certaines anciennes applications ne supportent pas STEP mais supportent IGES.
  BREP     Oui      Oui      Le format natif d\'[OpenCasCade](https://fr.wikipedia.org/wiki/Open_CASCADE_Technology), le noyau de géométrie FreeCAD.
  DXF      Oui      Oui      Un format ouvert maintenu par Autodesk. Depuis la 3D les données contenues dans un fichier DXF sont encodées dans un format propriétaire, FreeCAD ne peut importer/exporter que des données 2D à partir de ce format.
  DWG      Oui      Oui      La version propriétaire de DXF. Nécessite l'installation de l\'utilitaire [Teigha File Converter](https://www.opendesign.com/guestfiles). Ce format souffre des mêmes limitations que DXF.
  OBJ      Oui      Oui      Un format basé sur un maillage. Ne peut contenir que des mailles triangulaires. Tous les objets solides et basés sur NURBS de FreeCAD seront convertis en maillage à l\'exportation. Un exportateur alternatif est fourni par l\'atelier Arch, plus adapté à l\'exportation des modèles d\'architecture.
  DAE      Oui      Oui      Le principal format d\'importation/exportation de Sketchup. Ne peut contenir que des maillages triangulés. Tous les objets solides et NURBS de FreeCAD seront convertis en maillage lors de l\'exportation.
  STL      Oui      Oui      Un format basé sur le maillage, couramment utilisé pour l\'impression 3D. Ne peut contenir que des maillages triangulés. Tous les objets solides et NURBS de FreeCAD seront convertis en maillage lors de l\'exportation.
  PLY      Oui      Oui      Un ancien format de maillage. Peut seulement contenir des mailles triangulaires. Tous les objets solides et basés sur NURBS de FreeCAD seront convertis en maillage à l\'exportation.
  IFC      Oui      Oui      [Classes](https://fr.wikipedia.org/wiki/Industry_Foundation_Classes). Nécessite l\'installation de [IfcOpenShell-python](http://ifcopenshell.org/python.html). Le format IFC et sa compatibilité avec d\'autres applications est une affaire complexe, à utiliser avec précaution.
  SVG      Oui      Oui      Un excellent format graphique 2D
  VRML     Oui      Oui      Un format Web assez ancien.
  GCODE    Oui      Oui      FreeCAD peut déjà importer et exporter vers/depuis plusieurs variantes de GCode, mais seulement un petit nombre de machines sont actuellement prises en charge.
  CSG      Oui      Non      OpenSCAD\'s [CSG](https://fr.wikipedia.org/wiki/G%C3%A9om%C3%A9trie_de_construction_de_solides) (Constructive Solid Geometry) format. Format [CSG](https://fr.wikipedia.org/wiki/G%C3%A9om%C3%A9trie_de_construction_de_solides) d\'OpenSCAD (géométrie constructive de solides ).

Certains de ces formats de fichiers ont des options. Celles-ci peuvent être configurées à partir du menu Édition → Préférences → Importer/Exporter :

![](images/Import_preferences.jpg )

**Lire plus d\'informations**

-   [Tous les formats de fichiers pris en charge par FreeCAD](Import_Export/fr.md)
-   [Travailler avec des fichiers DXF dans FreeCAD](Draft_DXF/fr.md)
-   [Activation du support DXF et DWG](Dxf_Importer_Install/fr.md)
-   [Travailler avec des fichiers SVG dans FreeCAD](Draft_SVG/fr.md)
-   [Importation et exportation vers le format IFC](Arch_IFC/fr.md)
-   [OpenCasCade](http://www.opencascade.com)
-   [Teigha File Converter](https://www.opendesign.com/guestfiles)
-   [Base de données des spécifications IFC](https://technical.buildingsmart.org/standards/ifc/ifc-schema-specifications/)
-   [IfcOpenShell](http://ifcopenshell.org/)




[Category:Poweruser Documentation](Category:Poweruser_Documentation.md) [Category:Tutorials](Category:Tutorials.md)
