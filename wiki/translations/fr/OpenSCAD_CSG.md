 {{TOCright}}

## Importation

### Éléments Supportés {#éléments_supportés}

-   **primitives** : cube, sphère, cylindre, carré, cercle, polygones, polyèdre
-   **booléenne** : union, différence, intersection
-   linéaires extrudées, rotation extrudées
-   importation (dxf, stl, off) (sans mise à l\'échelle ou la transformation d\'origine)
-   multmatrix
-   couleur

### Elements non supportés {#elements_non_supportés}

-   projection
-   surface
-   rendu (ignored)
-   cgal opérations: minkowski, glide, path, subdiv, hull

## Exportation

### Éléments Supportés {#éléments_supportés_1}

-   **primitives**: Box, Cylindre, Cône, Tore
-   **booléen**: Coupure, Fusion, Common

### Secours

Les objets dérivés de **Part::Feature** ne sont pas (encore) pris en charge, les mailles sont exportées, comme un élément de polyèdre

## Relation

-   [atelier OpenSCAD](OpenSCAD_Workbench/fr.md)
-   [Import Export](Import_Export/fr.md)
-   [FreeCAD Comment importer exporter](FreeCAD_Howto_Import_Export/fr.md)


 {{OpenSCAD Tools navi}}

[Category:File\_Formats{{\#translation:}}](Category:File_Formats.md)
