# <img alt="Defeaturing workbench icon" src=images/Defeaturing_workbench_icon.svg  style="width   *64px;"> Defeaturing Workbench/de

## Einführung


{{TOCright}}

<img alt="" src=images/Defeaturing_workbench_icon.svg  style="width   *24px;"> **Arbeitsbereich Merkmal aus einer Form entfernen** ist ein Erweiterungsarbeitsbereich, der für die Bearbeitung von STEP-Modellen bestimmt ist, wobei die ausgewählten Formelemente aus dem Modell entfernt werden. Es ist ein [externer Arbeitsbereich](External_workbenches/de.md) und ist daher nicht Teil der Standard FreeCAD Installation.

## Funktionen

-   Bietet einen Werkzeugsatz zum Bearbeiten einer Form oder eines STEP-Modells, Entfernen von Bohrung(en), Fläche(n), Vereinfachen des Modells, Ändern der Toleranz, Anwenden von Fuzzy Bool\'schen Operationen usw\...
-   Es gibt auch Werkzeuge zum Erzeugen von Volumenkörperformen, aus Kante(n), Fläche(n) oder Schale(n).
-   Es ist auch möglich, die direkte Modellierung des Modells zu verwenden, wenn die Historie der Arbeitsgänge nicht verfügbar ist. (Dies ist der Fall bei 3D STEP Modellen).
-   Nützlich in Situationen, in denen proprietäre Details des Modells schnell entfernt werden müssen, bevor es gemeinsam genutzt werden kann. Siehe [Defeaturing](Defeaturing/de.md)

Hinweis   * Fortgeschrittenere Defeaturing Werkzeuge können verwendet werden, wenn [OCC7.3](OpenCASCADE.md) verfügbar ist.

## Installation

### Automatisch (empfohlen) 

Verwendung des FreeCAD <img alt="" src=images/AddonManager.svg  style="width   *24px;"> [Erweiterungsverwalter](Std_AddonMgr/de.md) verfügbar in v0.17+ über **Werkzeuge → Erweiterungsverwalter**. Suche nach dem <img alt="" src=images/Defeaturing_workbench_icon.svg  style="width   *24px;"> Defeaturing Arbeitsbereichssymbol . Der Erweiterungsverwalter benachrichtigt den Benutzer auch, wenn eine neue Version dieser Erweiterung verfügbar ist.

### Manuell

Siehe [Wie man zusätzliche Werkbänke installiert](How_to_install_additional_workbenches/de.md)

### Unterstützt

-   FreeCAD v0.15 4671
-   FreeCAD v0.16 \>= 6712
-   FreeCAD v0.17 \>= 13522
-   FreeCAD v0.18+

## Referenzen

-   Autor   * Github   * [\@easyw](https   *//github.com/easyw) \| FreeCAD Forums   * [1](https   *//forum.freecadweb.org/viewtopic.php?f=9&t=29506)
-   Quellcode auf github   * <https   *//github.com/easyw/Defeaturing_WB>
-   FC Forumsbeitrag thread <https   *//forum.freecadweb.org/viewtopic.php?t=29506>

## Werkzeuge

![Defeaturing Werkzeugdialog](images/Defeaturing_WB.png )

<img alt="" src=images/Defeaturing_Tools.svg  style="width   *32px;"> Defeaturing Werkzeuge befinden sich in einer separaten Maske.

-   <img alt="" src=images/DefeatWB_Tools_rmv_hole.png  style="width   *32px;"> [Bohrungen entfernen](DefeatWB_Tools_rmv_hole/de.md)   * Bohrung von der Fläche entfernen
-   <img alt="" src=images/DefeatWB_Tools_rmv_listed_Faces.png  style="width   *32px;"> [Aufgelistete Flächen entfernen](DefeatWB_Tools_rmv_listed_Faces/de.md)   * \'in Liste\' Flächen entfernen
-   <img alt="" src=images/DefeatWB_Tools_add_Faces_listed_Edges.png  style="width   *32px;"> [Flächen von \'in Liste\' Kanten hinzufügen](DefeatWB_Tools_add_Faces_listed_Edges/de.md)   * Flächen von \'in Liste\' Kanten hinzufügen
-   <img alt="" src=images/DefeatWB_Tools_select_Faces_Param_Defeat.png  style="width   *32px;"> [Flächen auswählen, die parametrisch Defeatured werden sollen](DefeatWB_Tools_select_Faces_Param_Defeat/de.md)   * Flächen auswählen, die parametrisch Defeatured werden sollen
-   <img alt="" src=images/DefeatWB_Tools_create_copy_listed_edges.png  style="width   *32px;"> [Erstelle eine Kopie der \'in-Liste\' Kanten](DefeatWB_Tools_create_copy_listed_edges/de.md)   * Erstelle eine Kopie der \'in-Liste\' Kanten

-   <img alt="" src=images/DefeatWB_Tools_copy_Faces_listed_faces.png  style="width   *32px;"> [kopiere Flächen aus \'in Liste\' Flächen](DefeatWB_Tools_copy_Faces_listed_faces/de.md)   * kopiere Flächen aus \'in Liste\' Flächen
-   <img alt="" src=images/DefeatWB_Tools_offset_face.png  style="width   *32px;"> [ Versatz Fläche](DefeatWB_Tools_offset_face/de.md)   * Versatz Fläche
-   <img alt="" src=images/DefeatWB_Tools_offset_edge.png  style="width   *32px;"> [Versatz Kante](DefeatWB_Tools_offset_edge/de.md)   * Versatz Kante

-   <img alt="" src=images/DefeatWB_Tools_make_solid_listed_faces.png  style="width   *32px;"> [Make Solid from in List Faces](DefeatWB_Tools_make_solid_listed_faces.md)   * make Solid from in List Faces
-   <img alt="" src=images/DefeatWB_Tools_make_solid_faces_selected_objects.png  style="width   *32px;"> [Make Solid from the Faces of the selected Objects](DefeatWB_Tools_make_solid_faces_selected_objects.md)   * make Solid from the Faces of the selected Objects
-   <img alt="" src=images/DefeatWB_Tools_select_one_object_2_make_solid_step_proc.png  style="width   *32px;"> [Make Solid from in List Faces](DefeatWB_Tools_select_one_object_2_make_solid_step_proc.md)   * select ONE object to try to make a Solid through STEP import/export process
-   <img alt="" src=images/DefeatWB_Tools_Connect.png  style="width   *32px;"> [Connect](DefeatWB_Tools_Connect.md)   * connect
-   <img alt="" src=images/DefeatWB_Tools_clean_face_rmv_holes.png  style="width   *32px;"> [clean Face(s) removing holes and merging Outwire](DefeatWB_Tools_clean_face_rmv_holes.md)   * clean Face(s) removing holes and merging Outwire

-   <img alt="" src=images/DefeatWB_Tools_show_listed_edges.png  style="width   *32px;"> [show \'in List' Edge(s)](DefeatWB_Tools_show_listed_edges.md)   * show \'in List' Edge(s)
-   <img alt="" src=images/DefeatWB_Tools_show_listed_faces.png  style="width   *32px;"> [show \'in List' Face(s)](DefeatWB_Tools_show_listed_faces.md)   * show \'in List' Face(s)
-   <img alt="" src=images/DefeatWB_Tools_refine.png  style="width   *32px;"> [refine](DefeatWB_Tools_refine.md)   * refine
-   <img alt="" src=images/DefeatWB_Tools_simple_copy.png  style="width   *32px;"> [simple copy](DefeatWB_Tools_simple_copy.md)   * simple copy
-   <img alt="" src=images/DefeatWB_Tools_parametric_refine.png  style="width   *32px;"> [parametric Refine](DefeatWB_Tools_parametric_refine.md)   * parametric Refine

-   <img alt="" src=images/DefeatWB_Tools_geometry_check.png  style="width   *32px;"> [Geometrieprüfung](DefeatWB_Tools_geometry_check/de.md)   * Geometrieprüfung
-   <img alt="" src=images/DefeatWB_Tools_get_Tolerance_value.png  style="width   *32px;"> [liefert Toleranzwert](DefeatWB_Tools_get_Tolerance_value/de.md)   * liefert Toleranzwert
-   <img alt="" src=images/DefeatWB_Tools_set_Tolerance_value.png  style="width   *32px;"> [Toleranzwert einstellen](DefeatWB_Tools_set_Tolerance_value/de.md)   * Toleranzwert einstellen

-   <img alt="" src=images/DefeatWB_Tools_make_edges_selected_vertexes.png  style="width   *32px;"> [erstelle Kante aus gewählten Knoten](DefeatWB_Tools_make_edges_selected_vertexes/de.md)   * erstelle Kante aus gewählten Knoten
-   <img alt="" src=images/DefeatWB_Tools_reset_placement.png  style="width   *32px;"> [Positionierung zurücksetzen](DefeatWB_Tools_reset_placement/de.md)   * Positionierung zurücksetzen
-   <img alt="" src=images/DefeatWB_Tools_show_hide_typeId_shape.png  style="width   *32px;"> [anzeigen/verbergen TypId der Form](DefeatWB_Tools_show_hide_typeId_shape/de.md)   * anzeigen/verbergen TypId der Form
-   <img alt="" src=images/DefeatWB_Tools_help.png  style="width   *32px;"> [Hilfe](DefeatWB_Tools_help/de.md)   * Hilfe

-   <img alt="" src=images/DefeatWB_Tools_Fuzzy_Cut.png  style="width   *32px;"> [Fuzzy Schnitt](DefeatWB_Tools_Fuzzy_Cut/de.md)   * Fuzzy Schnitt
-   <img alt="" src=images/DefeatWB_Tools_Fuzzy_Union.png  style="width   *32px;"> [Fuzzy Vereinigung](DefeatWB_Tools_Fuzzy_Union/de.md)   * Fuzzy Vereinigung
-   <img alt="" src=images/DefeatWB_Tools_Fuzzy_Common.png  style="width   *32px;"> [Fuzzy Gemeinsam](DefeatWB_Tools_Fuzzy_Common/de.md)   * Fuzzy Gemeinsam

## Videotutorien

### Defeaturing

Entfernen von Formelementen unter Verwendung neuer OCC7.3 Werkzeuge

[480px\|left\|thumb \|link=<https   *//raw.githubusercontent.com/easyw/FreeCAD-tutorials/master/testing-files/removing-holes.mp4%7CDefeaturing-Arbeitsbereich>   * entfernen von Formelementen (Bohrungen)](Image   *Defeaturing-WB-@Work_v3.png.md)

[480px\|left\|thumb \|link=<https   *//youtu.be/yrTtWFakAyE> \|alt=Defeaturing-WB-\@Work\|YouTube   * Defeaturing Werkzeuge - Vereinfachung des Modells](Image   *Defeaturing-WB-@Work_v1.png.md)

[480px\|left\|thumb \|link=<https   *//youtu.be/vgQwGI6Fk6Q%7CYouTube>   * Defeaturing Werkzeuge - Mehrfachauswahl von Flächen für Defeaturing](Image   *Defeaturing-WB-@Work_v2.png.md)

[480px\|left\|thumb \|link=<https   *//raw.githubusercontent.com/easyw/FreeCAD-tutorials/master/testing-files/removing-fillet-chamfer.mp4%7CDefeaturing-Arbeitsbereich> - Entfernen-Verrundung-Fase](Image   *Defeaturing-WB-@Work_v4.png.md)

[480px\|left\|thumb \|link=<https   *//peertube.mastodon.host/videos/watch/c6bc5abd-2eb7-48c7-af67-c4d8e6783872%7CDefeaturing-Arbeitsbereich> - Überblick-Funktionen (in deutscher Sprache)](Image   *Defeaturing-WB-@Work_v5.png.md)

[480px\|left\|thumb \|link=<https   *//raw.githubusercontent.com/easyw/FreeCAD-tutorials/master/testing-files/parametric-defeaturing.mp4%7CDefeaturing> Arbeitsbereich - parametrisches-Defeaturing](Image   *Defeaturing-WB-@Work_v6.png.md) 

### Reparieren

-   Eine Form nähen
-   Flächen entfernen oder vereinfachen
-   Bohrungen oder Taschen entfernen
-   Toleranz lesen oder ändern
-   Fuzzy Boolesche Operationen ausführen

## Externe Arbeitsbereiche 

FreeCAD Arbeitsbereiche sind einfach zu programmieren in [Python](Python/de.md), daher gibt es viele Leute, die zusätzliche Arbeitsbereiche außerhalb der FreeCAD Hauptentwickler entwickeln.

Die [Externe Arbeitsbereiche](External_workbenches/de.md) Seite hat einige Informationen und Anleitungen zu einigen von ihnen, und das Projekt [FreeCAD Erweiterungen](https   *//github.com/FreeCAD/FreeCAD-addons) hat sich zum Ziel gesetzt, diese zu sammeln und sie von FreeCAD aus leicht installierbar zu machen.

Neue Arbeitsbereiche sind in der Entwicklung, bleib\' dran!


 

[Category   *Addons](Category_Addons.md) [Category   *External Workbenches](Category_External_Workbenches.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > Defeaturing Workbench/de
