# Property editor/de
## Einleitung

Der [Eigenschafteneditor](Property_editor/de.md) erscheint im unteren Bereich des Fensters **Modell** (wenn die [Combo-Ansicht](combo_view/de.md) aktiv ist) oder als eigenständiges Fenster **Eigenschafteneditor**.

Generell ist der Eigenschafteneditor dazu gedacht, nur ein Objekt zur Zeit zu behandeln. Die im Eigenschafteneditor angezeigten Werte gehören zum ausgewählten Objekt. Es gibt jedoch einige Eigenschaften, wie Farben, die für mehrere ausgewählte Objekte gleichzeitig gesetzt werden können. Wurde kein Element ausgewählt, bleibt der Eigenschafteneditor leer.

Nicht alle Eigenschaften können geändert werden; einige von ihnen sind schreibgeschützt.

<img alt="" src=images/FreeCAD_Property_editor_Data.png  style="width:300px;"> 
*Die Daten-Eigenschaften eines [Part Würfels](Part_Box/de.md)*



## Eigenschaftentypen

Eine Eigenschaft ist eine Information, wie z.B. eine Zahl oder eine Zeichenkette, die mit einem FreeCAD Dokument oder einem Objekt im Dokument verknüpft ist. Es gibt viele Arten von Eigenschaften. Einige der gebräuchlichsten Typen sind:


{{Code|lang=text|code=
App::PropertyAngle
App::PropertyBool
App::PropertyDistance
App::PropertyFloat
App::PropertyInteger
App::PropertyLength
App::PropertyPlacement
App::PropertyString
App::PropertyVector
}}



## Ansicht- und Daten-Eigenschaften 

Der Eigenschafteneditor hat zwei Tabs, die Zugang zu zwei Klassen von Eigenschaften bieten:

-   **Daten**-Eigenschaften, die sich auf die \"physischen\" Parameter des Objekts beziehen. Die **Daten**-Eigenschaften definieren die wesentlichen Merkmale des Objekts. Sie sind immer vorhanden, auch wenn FreeCAD im Konsolenmodus oder als Bibliothek verwendet wird. Das heißt, wenn ein Dokument im Konsolenmodus geladen wird, ist es möglich den Radius eines Kreises oder die Länge einer Linie zu bearbeiten, auch wenn das Ergebnis nicht auf dem Bildschirm zu sehen ist.
-   **Ansicht**-Eigenschaften, die sich auf das \"visuelle\" Erscheinungsbild des Objekts beziehen. Die **Ansicht**-Eigenschaften sind an das `ViewObject` des Objekts gebunden und sind nur zugänglich, wenn die grafische Benutzeroberfläche (GUI) geladen ist. Sie sind nicht zugänglich, wenn FreeCAD im Konsolenmodus oder als Headless Library verwendet wird. Standardmäßig werden Änderungen an den Ansicht-Eigenschaften nicht zum undo stack hinzugefügt und können nicht mit [Std Rückgängig](Std_Undo/de.md) und [Std Wiederherstellen](Std_Redo/de.md) rückgängig gemacht und wiederhergestellt werden. Es ist jedoch möglich, dies zu ändern, indem der [Feinabstimmungsparameter](Fine-tuning/de.md) **AutoTransactionView** auf `True` gesetzt wird.



## Grundlegende Eigenschaften 

Verschiedene Objekte können unterschiedliche Eigenschaften haben. Viele Objekte haben jedoch die gleichen Eigenschaften, weil sie von derselben internen Klasse abgeleitet sind.

Die meisten geometrischen Objekte, die in der [3D-Ansicht](3D_view/de.md) erstellt und angezeigt werden können, sind von einem `Part::Feature` abgeleitet. Siehe [Part Formelement](Part_Feature/de.md) für die grundlegenden Eigenschaften, die diese Objekte haben.

Für 2D-Geometrie werden die meisten Objekte von einem `Part::Part2DObject` abgeleitet (das wiederum von einem `Part::Feature` abgeleitet ist), das die Basis für [Skizzen](Sketch/de.md) und die meisten [Draft Objekte](Draft_Workbench/de.md) ist. Siehe [Part Part2DObject](Part_Part2DObject/de.md) für die grundlegenden Eigenschaften dieser Objekte.



## Kontextmenü

Um das Kontextmenü des Eigenschaftseditors aufzurufen, Rechtsklick auf den Hintergrund des Editors oder auf eine Eigenschaft.

Ein Rechtsklick auf den Hintergrund zeigt drei Optionen an:

-    **Eigenschaft hinzufügen**: Fügt dem Objekt eine dynamische Eigenschaft hinzu.

-    **Ausgeblendete anzeigen**: Wenn diese Option aktiviert ist, werden ausgeblendete Daten- und Ansicht-Eigenschaften im Editor angezeigt.

-    **Automatisch erweitern**: Wenn aktiv, werden alle Knoten im Editor erweitert, wenn ein Objekt ausgewählt wird.

Wird mit der rechten Maustaste auf eine Eigenschaft geklickt, sind die folgenden zusätzlichen Optionen verfügbar:

-    **Eigenschaften-Gruppe umbenennen**: Benennt die Eigenschaften-Gruppe der ausgewählten Eigenschaften um. Nur für dynamische Eigenschaften verfügbar. Dynamische Eigenschaften sind solche, die vom Benutzer hinzugefügt werden, sowie solche, die durch Python-Code hinzugefügt werden.

-    **Eigenschaft entfernen**: Entfernt ausgewählte Eigenschaften. Nur für dynamische Eigenschaften verfügbar.

-    **Ausdruck...**: Öffnet den Ausdruck-Editor, der die Verwendung von [Ausdrücken](Expressions/de.md) mit dem Eigenschaftswert ermöglicht.

-    **Status**:

:   Folgt auf einen Status-Wert ein Stern (*****), ist dieser statisch und kann nicht geändert werden.

  - **Hidden**: Wenn aktiv, setzt die Eigenschaft als versteckt, was bedeutet, dass sie im Eigenschafteneditor nur angezeigt wird, wenn **Ausgeblendete anzeigen** aktiv ist.

  - **Output**: Wenn aktiv, setzt die Eigenschaft als Ausgabe.

  - **NoRecompute**: Wenn aktiv, hat das Ändern der Eigenschaft keine Auswirkung auf ihren Behälter für eine Neuberechnung.

  - **ReadOnly**: Wenn aktiv, setzt die Eigenschaft als schreibgeschützt. Die Eigenschaft kann dann nicht mehr im Eigenschafteneditor bearbeitet werden und die Option **Ausdruck...** ist nicht mehr verfügbar. Es kann jedoch immer noch möglich sein, die Eigenschaft über einen Dialog zu ändern.

  - **Transient**: Wenn aktiv, setzt die Eigenschaft als vorübergehend. Der Wert einer transienten Eigenschaft wird nicht in der Datei gespeichert. Wenn eine Datei geöffnet wird, wird sie mit ihrem Standardwert instanziiert.

  - **Touched**: Wenn aktiv, wird das Objekt berührt und ist bereit für eine Neuberechnung.

  - **EvalOnRestore**: Wenn aktiv, wird die Eigenschaft beim Wiederherstellen des Dokuments ausgewertet.

  - **CopyOnChange**: Wenn aktiv, wird die Eigenschaft kopiert, wenn sie in einem Link geändert wird. Die Eigenschaft **Link Copy on Change** des Links muss auf {{Value|Tracking}} oder {{Value|Enabled}} gesetzt sein, damit dies funktioniert. Dies ist verwandt mit [Variant Links](https://forum.freecad.org/viewtopic.php?p=738833#p738833).



## Skripten

Siehe [PythonFunktion Benutzerdefinierte Eigenschaften](FeaturePython_Custom_Properties/de.md) für einen Überblick:



## Einstellungen

Siehe [Combo-Ansicht](Combo_view/de#Einstellungen.md).



---
⏵ [documentation index](../README.md) > Property editor/de
