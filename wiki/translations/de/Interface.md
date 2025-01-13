# Interface/de
## Einleitung

Die FreeCAD-[Oberfläche](interface/de.md) (auch als Benutzerschnittstelle bezeichnet) basiert auf Qt, einem bekannten Werkzeugsatz für grafische Benutzerschnittstellen (GUIs), der insbesondere unter Linux eingesetzt wird, aber auch unter Windows und MacOS zur Verfügung steht.

<img alt="" src=images/FreeCAD_interface_base_divisions.png  style="width:1024px;">



*Standard-Oberfläche in Version 0.19.*

Das Hauptfenster der Anwendung kann grob in 11 Bereiche unterteilt werden:

1.  Der [Hauptansichtsbereich](main_view_area/de.md), der verschiedene Registerkartenfenster enthalten kann.
2.  Die [3D-Ansicht](3D_view/de.md), normalerweise eingebettet in den [Hauptansichtsbereich](main_view_area/de.md).
3.  Der obere Teil der [Combo-Ansicht](combo_view/de.md), der die [Baumansicht](tree_view/de.md) und den [Aufgaben-Bereich](task_panel/de.md) beinhaltet.
4.  Der untere Teil der [Combo-Ansicht](combo_view/de.md), der den [Eigenschafteneditor](property_editor/de.md) beinhaltet.
5.  Die [Auswahlansicht](selection_view/de.md).
6.  Das [Ausgabefenster](report_view/de.md).
7.  Die [Python-Konsole](Python_console/de.md).
8.  Die [Statusleiste](status_bar/de.md).
9.  Der Symbolleistenbereich, siehe folgende Informationen zu den Symbolleisten.
10. Die Auswahlliste der [Arbeitsbereiche](Std_Workbench/de.md), die selbst eine Symbolleiste ist.
11. Das [Standardmenü](Standard_Menu/de.md).



## Komponenten der Oberfläche 

Wie viele andere Programme enthält FreeCAD eine Standardmenüleiste und eine Reihe von Symbolleisten und Fenster, in denen sich die Anwenderwerkzeuge befinden.



### Menüs

Das [Standardmenü](Standard_Menu/de.md) enthält: {{StdMenu|[**Datei**](Std_File_Menu/de.md)}}, {{StdMenu|[**Bearbeiten**](Std_Edit_Menu/de.md)}}, {{StdMenu|[**Ansicht**](Std_View_Menu/de.md)}}, {{StdMenu|[**Werkzeuge**](Std_Tools_Menu/de.md)}}, {{StdMenu|[**Makro**](Std_Macro_Menu/de.md)}}, {{StdMenu|[**Fenster**](Std_Windows_Menu/de.md)}}, {{StdMenu|[**Hilfe**](Std_Help_Menu/de.md)}}.



### Symbolleisten

Die Symbolleisten, die standardmäßig in der Oberfläche dargestellt werden, sind:

-   Symbolleiste Datei: Werkzeuge zum Arbeiten mit Dateien, Öffnen von Dokumenten, Kopieren, Einfügen, Rückgängigmachen und Wiederherstellen von Aktionen.
-   Symbolleiste [Arbeitsbereich](Std_Workbench/de.md): Sie enthält ein einziges Widget zur Auswahl des aktiven [Arbeitsbereiches](workbenches/de.md).
-   Symbolleiste Makro: Werkzeuge zum Aufzeichnen, Bearbeiten und Ausführen von [Makros](macros/de.md).
-   Symbolleiste Ansicht: Werkzeuge zur Steuerung der Darstellung von Objekten in der [3D-Ansicht](3D_view/de.md).
-   Symbolleiste Struktur: Werkzeuge zum Ordnen von Objekten im Dokument und zum Erstellen von Verknüpfungen zu weiteren Dokumenten.

Diese können ein- und ausgeschaltet werden, durch Rechtsklick auf eine leere Stelle in einer der Symbolleisten und Auswahl des gewünschten Elements oder über das Menü **Ansicht → Symbolleisten**.



### Fenster

Die Hauptfenster, die das Arbeiten mit Objekten ermöglichen, sind:

-   [3D-Ansicht](3D_view/de.md): Der Bereich, in dem 2D- und 3D-Geometrie gezeichnet wird.
-   [Combo-Ansicht](Combo_view/de.md): Das Fenster, das die [Baumansicht](tree_view/de.md), den [Aufgaben-Bereich](task_panel/de.md) und den [Eigenschafteneditor](property_editor/de.md) enthält.
-   [Baumansicht](Tree_view/de.md): Das Element, das alle Objekte im Dokument und ihre parametrische Historie anzeigt.
-   [Aufgaben-Bereich](Task_panel/de.md): Das Fenster, das je nach ausgewähltem Zeichenwerkzeug verschiedene Aktionen und Optionen anzeigt.
-   [Eigenschafteneditor](Property_editor/de.md): Der Bereich, in dem Objekteigenschaften geändert werden.
-   [Auswahlansicht](Selection_view/de.md): Das Fenster, das die aktuell ausgewählten Elemente anzeigt.
-   [Ausgabefenster](Report_view/de.md): Das Textfeld, in dem verschiedene Meldungen der Anwendung und ihrer Werkzeuge angezeigt werden.
-   [Python-Konsole](Python_console/de.md): Der Editor, der ermöglicht, [Python](Python/de.md)-Code interaktiv auszuführen, um die Ergebnisse in der [3D-Ansicht](3D_view/de.md) anzusehen.
-   [Statusleiste](Status_bar/de.md): Die Leiste, die bestimmte Nachrichten der Anwendung anzeigt und ein Schaltfläche zur Auswahl der [Mausnavigation](Mouse_navigation/de.md) enthält.
-   [DAG-Ansicht](DAG_view/de.md): Eine Alternative zur [Baumansicht](tree_view/de.md), die die Beziehungen zwischen verschiedenen Objekten in einem Diagramm anzeigt.

Mit Ausnahme der 3D-Ansicht können alle Fenster ein- und ausgeschaltet werden, indem man mit der rechten Maustaste auf einen leeren Bereich in einer der oberen Symbolleisten klickt und das gewünschte Element auswählt oder im Menü **Ansicht → Fenster**.

Zum Aktivieren und Deaktivieren der Statusleiste wird im Menü **Ansicht → Statusleiste** ausgewählt.



### Andere

Weitere nützliche Oberflächen und Fenster enthalten:

-   [Scene-Inspector](Std_SceneInspector/de.md): Ein Fenster, das die Coin3D-Knoten anzeigt, aus denen sich der [Szenengraph](Scenegraph/de.md) zusammensetzt. Erfahrenen Anwendern und Entwicklern kann es bei der Fehlerbeseitigung helfen, in Vorgängen, die die Szene direkt manipulieren und in Objekten, die in der [3D-Ansicht](3D_view/de.md) erstellt wurden.
-   [Abhängigkeitsdiagramm](Std_DependencyGraph/de.md): Ein Fenster, das das Abhängigkeitsdiagramm aller Objekte im Dokument anzeigt, das mit dem Hilfsprogramm [Graphviz](https://graphviz.org/) erstellt wird. Es unterstützt dabei, Probleme bei der Erstellung von Objekten zu erkennen, wie z.B. zirkuläre Abhängigkeiten, die aus der [Baumansicht](Tree_view/de.md) oder der [DAG-Ansicht](DAG_view/de.md) nicht ganz ersichtlich sind.



### Anpassung

Symbolleisten können unterschiedlich viele Schaltflächen enthalten; selbsterstellte Symbolleisten können mit einer Mischung aus verschiedenen Werkzeugen zusammengestellt werden und Makros enthalten.

Diese Optionen befinden sich im Menü unter **Werkzeuge → Benutzerdefiniert**. Siehe [Anpassen der Oberfläche](Interface_Customization/de.md).


{{Interface navi

}}



---
⏵ [documentation index](../README.md) > Interface/de
