 {{TOCright}}

## Importieren

### Unterstützte Elemente {#unterstützte_elemente}

-   Grundelemente: Würfel, Kugel, Zylinder, Quadrat, Kreis, Polygon, Polyeder
-   Boolesche Operationen: Vereinigung, Differenz, Schnittpunkt
-   linearextrude, rotateextrude
-   Importieren (dxf, stl, off) (ohne Skalierung oder Transformation des Ursprungs)
-   multmatrix
-   Farbe

### Nicht unterstützte Elemente {#nicht_unterstützte_elemente}

-   Projektion
-   Oberfläche
-   rendern (ignoriert)
-   cgal Operationen: minkowski, glide, path, subdiv, hull

## Exportieren

### Unterstützte Elemente {#unterstützte_elemente_1}

-   Grundelemente: Quader, Zylinder, Kegel, Torus
-   boolesche Operationen: Schneiden, Verschmelzen, Gemeinsam

### Rückgriff

Jedes von Part::Feature abgeleitete Objekt, das (noch) nicht unterstützt wird, wird vernetzt und als Polyederelement exportiert

## Verwandtes

-   [Arbeitsbereich OpenSCAD](OpenSCAD_Workbench/de.md)
-   [Importieren Exportieren](Import_Export/de.md)
-   [FreeCAD Wie Importieren Exportieren](FreeCAD_Howto_Import_Export/de.md)


 {{OpenSCAD Tools navi}}

[Category:File\_Formats{{\#translation:}}](Category:File_Formats.md)
