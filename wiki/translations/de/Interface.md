 {{TOCright}}

## Einleitung

Die FreeCAD [Oberfläche](interface/de.md) basiert auf Qt, einem sehr bekannten grafischen Anwenderschnittstellen Werkzeugsatz, insbesondere unter Linux verwendet, der aber auch unter Windows und MacOS verfügbar ist.

<img alt="" src=images/FreeCAD_interface_base_divisions.png  style="width:1024px;">


*Standard FreeCAD Oberfläche in v0.19.*

Das Hauptfenster der Anwendung kann grob in 11 Abschnitte unterteilt werden:

1.  Der [Hauptansichtsbereich](main_view_area/de.md), der verschiedene Registerkartenfenster enthalten kann
2.  Die [3D Ansicht](3D_view/de.md), normalerweise eingebettet in den [Hauptansichtsbereich](main_view_area/de.md)
3.  Der obere Teil der [Combo Ansicht](combo_view/de.md), der die [Baumansicht](tree_view/de.md) und [Aufgabenleiste](task_panel/de.md) beinhaltet.




1.  Der untere Teil der [Combo Ansicht](combo_view/de.md), der den [Eigenschaftseditor](property_editor/de.md) beinhaltet.
2.  Die [Auswahlansicht](selection_view/de.md)
3.  Die [Berichtsansicht](report_view/de.md)
4.  Die [Python Konsole](Python_console/de.md)
5.  Die [Statusleiste](status_bar/de.md)
6.  Der Werkzeugleistenbereich, siehe folgende Informationen zu den Werkzeugleisten
7.  Der [Arbeitsbereichsselektor](Std_Workbench/de.md), der selbst eine Werkzeugleiste ist.
8.  Das [Standardmenü](Standard_Menu/de.md)

## Oberflächenkomponenten

Wie viele andere Programmstücke enthält FreeCAD eine Standardmenüleiste und dann eine Reihe von Werkzeugleisten und Eingabefeldern, in denen sich die Anwenderwerkzeuge befinden.

### Menüs

Die [Standard Menüs](Standard_Menu/de.md) sind: {{StdMenu|[**Datei**](Std_File_Menu/de.md)}}, {{StdMenu|[**Bearbeiten**](Std_Edit_Menu/de.md)}}, {{StdMenu|[**Ansicht**](Std_View_Menu/de.md)}}, {{StdMenu|[**Werkzeuge**](Std_Tools_Menu/de.md)}}, {{StdMenu|[**Makro**](Std_Macro_Menu/de.md)}}, {{StdMenu|[**Fenster**](Std_Windows_Menu/de.md)}}, {{StdMenu|[**Hilfe**](Std_Help_Menu/de.md)}}.

### Werkzeugleisten

Die Werkzeugleisten, die in der Oberfläche erscheinen, sind:

-   Datei Werkzeugleiste: Werkzeuge zum Arbeiten mit Dateien, Öffnen von Dokumenten, Kopieren, Einfügen, Rückgängigmachen und Wiederherstellen von Aktionen.
-   [Arbeitsbereich Werkzeugleiste](Std_Workbench/de.md): Es enthält ein einziges Widget zur Auswahl der aktiven [Arbeitsbereich](workbenches/de.md).
-   Makro Werkzeugleiste: Werkzeuge zum Aufnehmen, Bearbeiten und Ausführen von [Makros](makros/de.md).
-   Ansicht Werkzeugleiste: Werkzeuge zur Steuerung der Darstellung von Objekten in der [3D Ansicht](3D_view/de.md).
-   Struktur Werkzeugleiste: Werkzeuge zum Strukturieren von Objekten im Dokument und zum Erstellen von Verknüpfungen zu weiteren Dokumenten.

Diese können ein- und ausgeschaltet werden, durch Rechtsklick auf eine leere Stelle in einer der Werkzeugleisten und Auswahl des gewünschten Elements oder über das Menü {{MenuCommand/de|Ansicht → Werkzeugleisten}}.

### Konsolen

Die Hauptkonsolen, die das Arbeiten mit Objekten ermöglichen, sind

-   [3D Ansicht](3D_view/de.md): der Bereich, in dem 2D und 3D Geometrie gezeichnet wird.
-   [Comboansicht](Combo_view/de.md): die Konsole, die die [Baumansicht](tree_view/de.md), den [Aufgabenkonsole](task_panel/de.md) und den [Eigenschafteneditor](property_editor/de.md) enthält.
-   [Baumansicht](Tree_view/de.md): das Element, das alle Objekte im Dokument und ihre parametrische Historie anzeigt.
-   [Aufgabenkonsole](Task_panel/de.md): Die Konsole, die je nach ausgewähltem Zeichenwerkzeug verschiedene Aktionen und Optionen anzeigt.
-   [Eigenschaftseditor](Property_editor/de.md): die Stelle, an der Objekteigenschaften geändert werden.
-   [Auswahlansicht](Selection_view/de.md): Die Konsole, die die aktuell ausgewählten Elemente anzeigt.
-   [Berichtansicht](Report_view/de.md): das Textfeld, in dem verschiedene Meldungen der Anwendung und ihrer Werkzeuge angezeigt werden.
-   [Python Konsole](Python_console/de.md): der Editor, mit dem [Python](Python/de.md) Code interaktiv ausgeführt werden kann, um Ergebnisse in der [3D Ansicht](3D_view/de.md) anzuzeigen.
-   [Statusleiste](Status_bar/de.md): die Leiste, die bestimmte Nachrichten aus der Anwendung anzeigt und über den Auswahlschalter [Mausnavigation](Mouse_navigation/de.md) verfügt.
-   [DAG Ansicht](DAG_view/de.md): eine Alternative zur [Baumansicht](tree_view/de.md), die die Beziehungen zwischen verschiedenen Objekten und Mausmodellen durch ein Diagramm anzeigt.

Mit Ausnahme der 3D Ansicht können alle Funktionen ein- und ausgeschaltet werden, indem man mit der rechten Maustaste auf einen leeren Bereich in einer der oberen Werkzeugleisten klicken und das gewünschte Element oder aus dem Menü {{MenuCommand/de|Ansicht → Konsolen}} auswählen.

Um die Statusleiste zu aktivieren und zu deaktivieren, verwenden Sie das Menü {{MenuCommand/de|Ansicht → Statusleiste}}.

### Andere

Weitere nützliche Oberflächen und Fenster umfassen:

-   [Scene Inspector](Std_SceneInspector/de.md): eine Konsole, die die Coin3D Knoten anzeigt, aus denen sich der [scenegraph](scenegraph/de.md) zusammensetzt. Für Erfahrene Anwender und Entwickler kann es sinnvoll sein, Vorgänge, die die Szene direkt manipulieren, und die in der [3D Ansicht](3D_view/de.md) erstellten Objekte zu beheben.
-   [Abhängigkeitsgraph](Std_DependencyGraph/de.md): ein Fenster, das den Abhängigkeitsgraphen aller Objekte im Dokument anzeigt, die mit dem Hilfsprogramm [Graphviz](Graphviz/de.md) erstellt wurden. Es ist hilfreich, Probleme bei der Erstellung von Objekten zu erkennen, wie z.B. zirkuläre Abhängigkeiten, die aus der [Baumansicht](tree_view/de.md) oder der [DAG Ansicht](DAG_view/de.md) nicht ganz ersichtlich sind.

### Anpassung

Werkzeugleisten können mehr oder weniger Schaltflächen haben, und benutzerdefinierte Werkzeugleisten können mit einer Mischung aus verschiedenen Werkzeugen erstellt werden, um entwickelte Makros zu speichern.

Diese Optionen befinden sich im Menü, {{MenuCommand/de|Werkzeuge → Benutzerdefiniert}}. Siehe [Schnittstellenanpassung](Interface_Customization/de.md).


{{Interface navi

}} 
