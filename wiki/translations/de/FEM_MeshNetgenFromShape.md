---
 GuiCommand:Container|
{{GuiCommand/de
   Name: FEM MeshNetgenFromShape
   Name/de: FEM NetzNetgenAusForm
   MenuLocation: Netz , FEM mesh from shape by Netgen
   Workbenches: FEM_Workbench/de
   SeeAlso: FEM_tutorial/de
}}
{{GuiCommandFemInfo/de
   Solvers: CalculiX, Mystran, Z88
}}
---

# FEM MeshNetgenFromShape/de



## Beschreibung

Für eine Finite-Elemente-Analyse muss die Geometrie in ein [FEM-Netz](FEM_Mesh/de.md) diskretisiert werden. Dieser Befehl verwendet [Netgen](https://www.ngsolve.org/) (das auf dem System installiert sein muss), um das Netz zu erstellen. Netgen-Netze werden von [Elmer](FEM_SolverElmer/de.md) nicht unterstützt.

Je nach Betriebssystem und Installationspaket kann Netgen mit FreeCAD gebündelt sein oder nicht. Für weitere Informationen siehe [FEM Installation](FEM_Install/de.md).



## Anwendung

1.  Die zu analysierende Form auswählen. Bei einem Volumen muss es sich um ein Solid oder Compsolid handeln. Ein Compsolid ist erforderlich, wenn das Teil aus mehreren Materialien besteht. (ein Compsolid kann mit dem Befehl [Part BooleanFragments](Part_BooleanFragments/de.md) erstellt werden).
2.  Das Werkzeug durch eine der folgenden Möglichkeiten aktivieren:
    -   Die Schaltfläche **<img src="images/FEM_MeshNetgenFromShape.svg" width=16px> [FEM Netz aus Form - Netgen](FEM_MeshNetgenFromShape/de.md)** drücken.
    -   Den Menüeintrag **Mesh → <img src="images/FEM_MeshGmshFromShape.svg" width=16px> FEM-Netz aus Form - Netgen** auswählen.
3.  Wahlweise minimale und maximale Elementgröße einstellen (Die vorgegebene Einstellung erstellt oft zu grobe Netze) sowie die Ordnung des Elements anpassen (die Checkbox *Zweite Ordnung* aktivieren).
4.  Wahlweise die *Feinheit* aus einer der vorgegebenen Möglichkeiten auswählen oder *Benutzerdefiniert* auswählen, um die Parameter von Hand einzugeben.
5.  Die Schaltfläche **Anwenden** drücken, um das Netz zu erstellen. {{Version/de|1.0}}: Wahlweise die Schaltfläche **Abbrechen** drücken, um das Vernetzen abzubrechen, wenn die neue Netgen-Implementation eingesetzt wird.
6.  Die Schaltfläche **OK** drücken, um das Netz zu erstellen und den Dialog zu schließen. Oder die Schaltfläche **Abbrechen** drücken, um die Änderungen oder das Erstellen des Netzobjekts abzubrechen.



## Eigenschaften

-    **Max. Größe**: Maximale Größe des Elements in mm.

-    **Min. Größe**: <small>(v1.0)</small> : Mindestgröße des Elements in mm.

-    **Zweite Ordnung**: Elemente zweiter Ordnung enthalten mehr Knoten pro Element. Normalerweise reicht es aus, ein gröberes Netz zu verwenden, um die gleiche Lösungsgenauigkeit wie mit Elementen erster Ordnung zu erhalten,

    -   true (Standard); Elemente zweiter Ordnung,
    -   false; Elemente erster Ordnung.

-    **Feinheit**: Bietet vordefinierte Stufen der Netzdichte.

-    **Wachstumsrate**: Legt fest, wie stark sich benachbarte Elemente in der Größe unterscheiden können.

-    **Number of Segmente per Edge**: Legt die minimale Anzahl von Netzsegmenten pro Kante fest.

-    **Number of Segments per Radius**: Definiert die minimale Anzahl von Mesh-Segmenten pro Radius.

-    **Optimieren**:

    -   true (Standard): Wendet einen Optimierungsalgorithmus an, um die Netzqualität zu verbessern
    -   false





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MeshNetgenFromShape/de
