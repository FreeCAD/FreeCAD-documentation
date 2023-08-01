---
- GuiCommand:
   Name: Part JoinConnect
   Name/de: Part Verbinden
   MenuLocation: Formteil - Verbinden - Objekte verbinden
   Workbenches: [Part](Part_Workbench/de.md)
   Version: 0.16
   SeeAlso: [Part Einbetten](Part_JoinEmbed/de.md), [Part Ausschneiden](Part_JoinCutout.md), [Part Boolesche Operationen](Part_Boolean/de.md), [Part Dicke](Part_Thickness/de.md)
---

# Part JoinConnect/de



## Beschreibung

Das Werkzeug Verbinden verbindet die Innenbereiche von zwei Hohlkörpern (z.B. Rohre). Es kann auch Schalenobjekte und Drähte verbinden.

![600px](images/JoinFeatures_Connect.png)



## Anwendung

1.  Die zu verbindenden Objekte auswählen.
    Die Reihenfolge der Auswahl ist nicht wichtig, da die Wirkung des Werkzeugs symmetrisch ist. Es genügt, von jedem Objekt eine Teilform (z.B. Flächen) auszuwählen. Es kann auch ein Verbund ausgewählt werden, der alle zu verbindenden Formen enthält, z.B. [Draft RechtwinkligeAnordnung](Draft_OrthoArray/de.md).
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche <img alt="" src=images/Part_JoinConnect.svg  style="width:24px;"> [Part Connect objects](Part_JoinConnect/de.md) in der Part-Werkzeugleiste drücken.
    -   Den Menüeintrag **Part → Verbinden → Objekte verbinden** auswählen.

Ein parametrisches Verbindungsobjekt wird erstellt. Originalobjekte werden ausgeblendet, und das Ergebnis der Verbindung wird in der [3D-Ansicht](3D_view/de.md) angezeigt.



## Eigenschaften


{{TitleProperty|Connect}}

-    {{PropertyData/de|Objects}}: Liste der zu verbindenden Objekte. Im Allgemeinen werden mindestens zwei Objekte benötigt, aber ein einziger Verbund, der die zu verbindenden Formen enthält, reicht ebenfalls aus. (seit FreeCAD v0.17.8053 wird diese Eigenschaft nicht mehr im [Eigenschafteneditor](Property_editor/de.md) angezeigt und kann nur über [Python](#Skripten.md) aufgerufen werden).

-    {{PropertyData/de|Refine}}: Legt fest, ob die Operation [FormAufbereiten](Part_RefineShape/de.md) auf die endgültige Form angewendet werden soll oder nicht. Der Standardwert wird durch ein Kontrollkästchen \'Form nach boolescher Operation automatisch aufbereiten\' in den [PartDesign Einstellungen](PartDesign_Preferences/.md) bestimmt.

-    {{PropertyData/de|Tolerance}}: \"Unschärfe\" Wert. Dies ist eine zusätzliche Toleranz, die bei der Suche nach Schnittmengen zusätzlich zu den in den Eingangsformen gespeicherten Toleranzen anzuwenden ist.



## Beispiel

1.  Erstelle ein Rohr, indem Du [Dicke](Part_Thickness/de.md) auf einen [Zylinder](Part_Cylinder/de.md) anwendest:
    ![320px](images/JoinFeatures_Example_step1.png)
2.  Erstelle ein weiteres Rohr mit kleinerem Durchmesser und platziere es so, dass es die Wand des ersten Rohres durchdringt:
    ![320px](images/JoinFeatures_Example_step2.png)
3.  Wähle das erste Rohr und das zweite Rohr aus und klicke auf die Option \"Objekte verbinden\" in der Symbolleiste der Verbindungswerkzeuge.
    ![320px](images/JoinFeatures_Example_step3_Connect.png)
4.  Verwende ein Querschnittswerkzeug ([Ausschnittebene](Std_ToggleClipPlane/de.md), [Arch Abschnittebene](Arch_SectionPlane/de.md), [Arch Schneideebene](Arch_CutPlane/de.md)), um Einbauten freizulegen. Auf dem Bild unten wird die Bogenschnittebene verwendet.
    ![320px](images/JoinFeatures_Example_step4_Connect.png)



## Algorithmus

Die Algorithmen hinter den Fügewerkzeugen sind recht einfach, und es ist wichtig, sie zu verstehen, um die Werkzeuge richtig zu verwenden. Insbesondere der Algorithmus von Verbinden ist etwas komplexer als andere, aber es genügt im Allgemeinen, ihn als symmetrische Variante des Einbetten-[Algorithmus](Part_JoinEmbed/de#Algorithms.md) zu betrachten.

1\. Jedes Objekt wird durch Überschneidungen mit anderen Objekten in Stücke zerlegt. (siehe [Part BoolescheFragmente](Part_BooleanFragments/de.md))

2\. Von den Teilen eines Objekts wird nur das größte beibehalten; alle anderen werden entfernt.

3\. Überschneidungselemente, die mindestens zwei Objekte berühren, werden dem Ergebnis hinzugefügt. Anschließend werden die Teile miteinander verbunden, um das Ergebnis von Verbinden zu bilden.



### Hinweise

-   Wenn bei Schritt 1 jedes Objekt in einem Stück verbleibt, entspricht das Ergebnis von Verbinden dem von [Vereinigen](Part_Union/de.md) von Objekten.
-   Jetzt werden alle gelieferten Verbindungen vor dem Anschluss zerlegt. Das bedeutet, dass selbstverschneidende Verbindungen, die für alle anderen booleschen Operationen ungültig sind, für Verbinden gültig sind. (Dies kann in Zukunft geändert werden.)
-   Das \"größte\" Stück ist dasjenige mit der größten Masse. Das heißt, für Festkörper werden Volumen verglichen; für Hüllen und Flächen werden Flächen verglichen, usw.
-   Seit FreeCAD v0.17.8053 und wenn die OCC-Version 6.9.0 und höher ist, ist Verbinden fast so schnell wie alle anderen booleschen Operationen. Bei älteren Versionen ist Verbinden etwa 5 mal langsamer als ein normaler boolescher Vorgang und funktioniert nur bei Festkörpern.



## Skripten

Die Fügewerkzeuge können in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit folgender Funktion verwendet werden:

**BOPTools.JoinFeatures.makeConnect(name)**

-   Erstellt eine leere Verbindungsfunktion. Die Eigenschaft \'Objekte\' muss anschließend explizit zugewiesen werden.
-   Liefert das neu erstellte Objekt.

Verbinden kann auch auf einfache Formen angewendet werden, ohne dass ein Dokumentenobjekt benötigt wird:

**Part.BOPTools.JoinAPI.connect(list_of_shapes, tolerance = 0.0)**

Dies kann nützlich sein, um benutzerdefinierte Python Skriptfunktionen zu erstellen.

Beispiel:


{{code|code=
import Part
j = Part.BOPTools.JoinFeatures.makeConnect(name= 'Connect')
j.Objects = FreeCADGui.Selection.getSelection()
}}

Das Werkzeug selbst ist in Python implementiert, siehe **/Mod/Part/BOPTools/JoinFeatures.py** ([GitHub link](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Part/BOPTools/JoinFeatures.py)) innerhalb des FreeCAD-Installationsverzeichnisses.



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part JoinConnect/de
