# Asymptote/de
## Beschreibung

[Asymptote](https://asymptote.sourceforge.io/) ist eine Vektor-Sprache für 2D- und 3D-Computergrafiken. Asymptote-Code kann in [LaTeX](https://www.latex-project.org/)-Dokumenten verwendet werden oder zum Erstellen von [PostScript](https://en.wikipedia.org/wiki/PostScript)-, [PDF](PDF.md)-, [SVG](SVG.md)-, [WebGL](https://www.khronos.org/webgl/)- und [PRC](https://en.wikipedia.org/wiki/PRC_(file_format))-Dateien. Interaktive 3D-PDF-Dateien, die mit Asymptote-Code erstellt werden, erfordern Acrobat-Reader in der Version 9 oder neuer.

Asymptote-Unterstützung wurde in FreeCAD Version 0.19 hinzugefügt.



## Exportieren

1.  Wahlweise den Flächen des Objekts, das exportiert werden soll, mit dem Befehl <img alt="" src=images/Part_FaceColors.svg  style="width:24px;"> [Part Flächenfarben](Part_FaceColors/de.md) Farben zuordnen.
2.  Zum Arbeitsbereich <img alt="" src=images/Workbench_Mesh.svg  style="width:24px;"> [Mesh](Mesh_Workbench/de.md) wechseln.
3.  Aus dem Objekt mit dem Befehl <img alt="" src=images/Mesh_FromPartShape.svg  style="width:24px;"> [Mesh NetzAusPartForm](Mesh_FromPartShape/de.md) ein Netzobjekt erstellen.
4.  Das neue Netzobjekt auswählen.
5.  Den Befehl <img alt="" src=images/Mesh_Export.svg  style="width:24px;"> [Mesh Export](Mesh_Export/de.md) aufrufen.
6.  Das ***.asy**-Dateiformat im Dialogfenster auswählen.
7.  Einen Dateinamen eingeben.
8.  Die Schaltfläche **Sichern** drücken.



## Umwandeln

Es erfordert den [Asymptote-Kompiler](https://sourceforge.net/projects/asymptote/), um ***.asy**-Dateien umzuwandeln. Für die Umwandlung in eine PDF-Datei ist außerdem ein [LaTeX](https://www.latex-project.org/get/)-System erforderlich.

Der Kompiler ist ein Befehlszeilenwerkzeug. Für das Umwandeln in eine PDF-Datei kann diese Syntax verwendet werden: 
```pythonPathToAsyExecutable/asy -f pdf AsymptoteFileName.asy```



## Verwandtes

-   [Import Export](Import_Export/de.md)



## Videoanleitungen

Die folgenden Videos sind auf Spanisch:

-   [A way of generating interactive pdf-3D files. (1/3) (From FreeCAD, MeshLab and LaTeX)](https://www.youtube.com/watch?v=U0m3643Vb1Q)
-   [A way of generating interactive pdf-3D files. (2/3) (From Asymptote and LaTex)](https://www.youtube.com/watch?v=PhVNvDZIerM)
-   [A way of generating interactive pdf-3D files. (3/3) (From FreeCAD, Asymptote and LaTeX)](https://www.youtube.com/watch?v=Q_ufaCN2hb4)


{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > [Mesh](Category_Mesh.md) > Asymptote/de
