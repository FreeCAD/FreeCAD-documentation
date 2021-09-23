# Combo view/de
 {{TOCright}}

## Einführung

Die [Comboansicht](combo_view/de.md) ist eines der Hauptpaneele in der FreeCAD [Benutzeroberfläche](interface/de.md). Sie befindet sich standardmäßig auf der linken Seite des Bildschirms. Sie ist \'\'zusammengesetzt aus zwei Abschnitten\", der:

-   [Oberer Bereich](#Upper_section/de.md), der zwei Reiter enthält: den {{MenuCommand/de|Modell}} Reiter und {{MenuCommand/de|Aufgaben Reiter}}
-   [Unterer Bereich](#Lower_section/de.md) zeigt den [Eigenschafteneditor](property_editor/de.md). Er enthält zwei Reiter: die {{MenuCommand/de|Ansicht}} und {{MenuCommand/de|Daten}} Eigenschaften. Der [Eigenschafteneditor](property_editor/de.md) wird nur angezeigt, wenn der {{MenuCommand/de|Modell}} Reiter **aktiv** ist, d. h. wenn die [Baumansicht](tree_view/de.md) sichtbar ist.


**Hinweis:**

Ursprünglich war der obere Teil ([Baumansicht](tree_view/de.md)) vom unteren Teil ([Eigenschaftseditor](property_editor/de.md)) getrennt, aber dann wurden sie kombiniert und so wurde die \"Combo\" ansicht erstellt.

## Oberer Bereich 

Die Registerkarte {{MenuCommand/de|Modell}} zeigt die Registerkarte [Baumansicht](tree_view/de.md), die eine Darstellung des Inhalts des Dokuments ist, einschließlich 2D- und 3D-Geometrie mit ihrer parametrischen Historie, aber auch unterstützende Objekte, die im Dokument gespeicherte Daten enthalten.

Die Registerkarte {{MenuCommand/de|Aufgaben}} zeigt die Registerkarte [Aufgabenleiste](task_panel/de.md), die je nach aktivem Arbeitsbereich und aktivem Werkzeug unterschiedliche Aktionen anzeigt.

<img alt="" src=images/FreeCAD_Combo_view_Tree_View_properties.png  style="width:" height="600px;"> <img alt="" src=images/FreeCAD_Combo_view_Task_panel.png  style="width:" height="600px;">


*Die Kombiansicht hat zwei Registerkarten: die Registerkarte Modell, die die Anzeige der [Baumansicht](tree_view/de.md) und der [Eigenschaftseditor](property_editor/de.md), und die Registerkarte Aufgaben, die die Anzeige der [Aufgabenpanel](task_panel/de.md).*

## Unterer Bereich 

Der untere Teil der Comboansicht zeigt den [Eigenschaftseditor](property_editor/de.md), der zwei Reiter anzeigt für {{MenuCommand/de|Ansicht}} und {{MenuCommand/de|Daten}} Eigenschaften. Der Eigenschaftseditor wird nur angezeigt, wenn der {{MenuCommand/de|Modell}} Reiter aktiv ist, d. h. wenn die [Baumansicht](tree_view/de.md) sichtbar ist.

-   Der {{MenuCommand/de|Ansicht}} Reiter zeigt Visualisierungseigenschaften der Objekte, die nur ihr Aussehen in der [3D Ansicht](3D_view/de.md) beeinflussen.

-   Der {{MenuCommand/de|Daten}} Reiter zeigt die parametrischen Eigenschaften der Objekte, die bestimmen, wie die geometrischen Formen wirklich definiert werden.

<img alt="" src=images/FreeCAD_Combo_view_Tree_View_properties.png  style="width:" height="600px;"> <img alt="" src=images/FreeCAD_Combo_view_Tree_Data_properties.png  style="width:" height="600px;">


*Der untere Teil der Comboansicht ist der Eigenschaftseditor, der die Eigenschaften von Ansicht und Daten anzeigt.*

## Deaktivieren der Comboansicht 

Um diese Ansichten selbst zu verwenden, verwende die Option [Parametereditor](Std_DlgParameter/de.md). Legen Sie die folgenden Untergruppen an, wenn sie nicht vorhanden sind

-    `BaseApp/Einstellungen/Andockfenster/Baumansicht`
    

-    `BaseApp/Einstellungen/Andockfenster/Eigenschaftsansicht`
    

dann füge den Parameter `Enabled` vom Typ `Boolean` hinzu und setze ihn auf `True`.

Aktiviere dann die Ansicht über das Menü {{MenuCommand/de|Ansicht → Paneele → Baumansicht}} oder {{MenuCommand/de|→ Eigenschaftsansicht}}.


{{Std Base navi

}} {{Interface navi}} 
