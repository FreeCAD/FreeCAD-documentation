---
 TutorialInfo:e
   Topic:  Export nach STL oder OBJ
   Level: Anfänger
   Time: 20 Minuten
   Author: r-frank
   FCVersion: 0.16.6703
---

# Export to STL or OBJ/de







## Einleitung

In diesem Tutorial werden wir beschreiben, wie man STL/OBJ-Dateien aus FreeCAD exportiert. Da das Mesh-Format STL/OBJ dimensionslos ist, geht FreeCAD beim Export davon aus, dass die im Modell benutzen Einheiten in mm sind. Falls dies nicht der Fall sein sollte, muss das Modell entsprechend skaliert werden. Ein Weg dazu ist die Nutzung von <img alt="" src=images/Draft_Scale.svg  style="width:24px;"> [Draft Skalieren](Draft_Scale/de.md).



## Beispiel-Teil 

Man kann ein eigenes Modell verwenden, man kann sich aber auch schnell ein Modell zum Testen erstellen:

1.  FreeCAD starten.
2.  Ein neues Dokument erstellen.
3.  Zum Arbeitsbereich <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench/de.md) wechseln.
4.  Einen Würfel durch Anklicken von <img alt="" src=images/Part_Box.svg  style="width:24px;"> [Part Würfel](Part_Box/de.md) einfügen.
5.  Einen Kegel durch Anklicken von <img alt="" src=images/Part_Cone.png  style="width:24px;"> [Part Kegel](Part_Cone/de.md) einfügen.
6.  Beide Objekte in der [Baumansicht](Tree_view/de.md) auswählen.
7.  Eine boolesche Vereinigung durch Anklicken von <img alt="" src=images/Part_Fuse.png  style="width:24px;"> [Part Vereinigung](Part_Fuse/de.md) anwenden.
8.  Die Datei speichern.



## Export-Methode 1: Benutzung von \"Datei → Exportieren\" 

1.  With the default settings, this method creates a mesh with noticeably jagged curves. To get a smoother finish when e.g. 3D printing, the mesh resolution should be configured:
    1.  Make sure the <img alt="" src=images/Workbench_Mesh.svg  style="width:24px;"> [Mesh Workbench](Mesh_Workbench.md) has been loaded (it is not loaded by default).
    2.  Go to **Edit → Preferences... → Import-Export → Mesh Formats**.
    3.  Change **Maximum mesh deviation**. A lower value will produce a mesh with a higher resolution.
2.  Select the solid to be exported in the tree view.
3.  Choose **File → Export...** and set the file type to **STL mesh (*.stl *.ast)**.
4.  Enter your file name. The default extension is **.stl**. You must include the extension **.ast** to produce an **.ast** file.
5.  Choose **Save**.



## Export-Methode 2: Benutzung des Mesh-Design-Arbeitsbereichs in FreeCAD 

1.  Zum Arbeitsbereich [Mesh](Mesh_Workbench/de.md) wechseln.

2.  Den zu vernetzenden Festkörper in der Baumansicht auswählen.

3.  Den Menüeintrag {{MenuCommand |Netze → <img src="images/Mesh_Mesh_from_Shape.svg" width=24px> Netz aus Form erstellen...}} auswählen.

4.  Einen der drei verfügbaren Vernetzer auswählen und dann die Vernetzungs-Parameter. Für weitere Informationen siehe [NetzAusPartForm](Mesh_FromPartShape/de.md).

5.  
    **OK**auswählen und der Netzkörper wird in der Baumansicht erstellt (mit einem grünen Netz-Symbol).

6.  Das Netzobjekt in der Baumansicht mit einem Rechtsklick auswählen und **<img src="images/Mesh_Export.svg" width=24px> Netz exportieren...** auswählen.

7.  Den Dateinamen eingeben; ohne Dateiendung. Die Dateiendung wird auf Basis des Dateityps vergeben. Wird eine Endung eingegeben, die nicht mit dem ausgewählten Dateityp übereinstimmt, wird die Dateiendung angehängt, die dem ausgewählten Typ entspricht, wenn die Datei gespeichert wird.

8.  Der Standard-Dateityp ist **Binary STL (*.stl)**. Er kann bei Bedarf geändert werden.

9.  
    ** Speichern**auswählen.



## Welche Methode sollte man wählen? 

-   Methode 1 kann in den meisten Situationen verwendet werden, wo eine Netzdatei benötigt wird.
-   Mit Methode 2 lässt sich ein Netz in FreeCAD überprüfen. Und wenn mehr als ein Festkörper konvertiert werden soll, können Werkzeuge des Arbeitsbereichs [Mesh](Mesh_Workbench/de.md) verwendet werden; z.B. können Netze vereinigt werden, bevor sie exportiert werden.



## Verweise

-   [Import von STL or OBJ](Import_from_STL_or_OBJ/de.md)
-   [Import/Export](Import_Export/de.md)



---
⏵ [documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > Export to STL or OBJ/de
