# Arch SHP/fr
FreeCAD est capable d\'importer [des shapefiles ou fichier de formes](https://fr.wikipedia.org/wiki/Shapefile)

L\'importateur utilise la bibliothèque shapefile.py de <https://github.com/GeospatialPython/pyshp>. Elle ne se trouve pas sur votre système lors de la première exécution, l\'importateur proposera de la télécharger et de l\'installer pour vous.

Les fichiers de formes sont composés de 3 fichiers (un fichier .shp, un fichier .shx et un fichier .dbf). Chacun d\'entre eux peut être utilisé avec cet importateur. Ils sont composés d\'objets 2D d\'un même type de géométrie, qui peuvent être des polygones/faces, des polylignes ou un nuage de points (les 3 types sont pris en charge par cet importateur) et des champs personnalisés pour lesquels chaque face, polyligne ou point du fichier de formes possède une valeur. C\'est le véritable joyau du SIG, pour lier une base de données à la géométrie. L\'utilisation la plus courante consiste à avoir un champ pour représenter les coordonnées d\'élévation de chaque forme du fichier. À l\'ouverture du fichier, l\'importateur vous demandera de quel champ obtenir les élévations de forme.

Une forme sera créée à partir de chaque fichier de formes dans FreeCAD.

A noter que toute la question des unités géoréférencées, avec des centaines de systèmes de projection utilisés dans le monde, n\'est pas traitée pour le moment. Les coordonnées du fichier sont utilisées \"telles quelles\".

### Relation

-   Annonce du fil de discussion FreeCAD [Importateur de fichiers de formes](https://forum.freecadweb.org/viewtopic.php?f=9&t=46150)
-   Fil de discussion du forum sur la discussion [OSArch](https://community.osarch.org/discussion/comment/578#Comment_578)
-   [Importer/Exporter](Import_Export/fr.md)
-   [Comment importer/exporter sous FreeCAD](FreeCAD_Howto_Import_Export/fr.md)
-   [Préférences d\'Import Export](Import_Export_Preferences/fr.md)


 

[Category:File Formats](Category:File_Formats.md)

---
[documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch SHP/fr
