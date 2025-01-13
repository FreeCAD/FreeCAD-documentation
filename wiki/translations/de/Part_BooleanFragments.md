---
 GuiCommand:
   Name: Part BooleanFragments
   Name/de: Part BoolescheBestandteile
   MenuLocation: Part , Teilen , Boolesche Bestandteile
   Workbenches: Part_Workbench/de
   Version: 0.17
   SeeAlso: Part_Slice/de, Part_XOR/de, Part_CompJoinFeatures/de, Part_Boolean/de
---

# Part BooleanFragments/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Part_BooleanFragments.svg  style="width:24px;"> **BoolescheBestandteile** berechnet alle Bruchteile, die sich aus der Anwendung boolescher Verknüpfungen zwischen Eingabeformen ergeben können. So werden beispielsweise aus zwei sich schneidende Kugeln drei nicht überlappende, aber berührende Festkörper erzeugt.

![600px](images/Part_BooleanFragments_Demo.png) 
*Auf dem obigen Bild wurden die Teile anschließend manuell auseinandergezogen, um die Schnitte zu erkennen.*

Die Ausgabeform ist immer ein Verbund. Der Inhalt des Verbundes hängt von der Art der Eingangsformen und der Betriebsart ab. Das bedeutet, dass man nicht sofort Zugriff auf einzelne Bestendteile des Ergebnisses hast - die Teile bleiben gruppiert. Die einzelnen Stücke können durch Auflösen des Verbundes entnommen werden ([Draft Zurückstufen](Draft_Downgrade/de.md)).

Das Werkzeug verfügt über drei Modi: \"Standard\", \"Teilen\" und \"VerbundFestkörper\".

\"Standard\" und \"Teilen\" unterscheiden sich durch die Wirkung des Werkzeugs auf Drähte, Hüllen und Verbundkörper: Wenn \"Teilen\", werden diese getrennt; wenn \"Standard\", werden sie zusammen gehalten (erhalten zusätzlicher Segmente).

Die Verbundstruktur im \"Standard\" und \"Teilen\" Modus folgt der Verbundstruktur der Eingänge. Das heißt, wenn du zwei Verbindungen einspeist, die jeweils eine Kugel enthalten, wie zum Beispiel oben, enthält das Ergebnis auch zwei Verbünde, die jeweils die Stücke der ursprünglich enthaltenen Kugel enthalten. Das bedeutet, dass das vereinigte Stück zweimal im Ergebnis wiederholt wird. Nur wenn die Eingangskugeln beide nicht in Verbünden vorliegen, enthält das Ergebnis das vereinigte Stück einmal.

Im \"Verbundkörper\" Modus werden die Festkörper zu einem Verbundkörper verbunden (Verbundkörper ist ein Satz von Festkörpern, die durch Flächen verbunden sind; sie sind mit Festkörpern verbunden, wie Drähte mit Kanten und Schalen mit Flächen; der Name ist wahrscheinlich ein verkürzter Satz \"Verbundkörper\"). Die Ausgabe ist eine nicht verschachtelte Verbindung von Verbundkörpern.



## Anwendung

1.  Die zu (ver-) schneidenden Objekte auswählen. Die Reihenfolge der Auswahl ist nicht wichtig, da die Auswirkung des Werkzeugs symmetrisch ist. Es genügt, von jedem Objekt eine Teilform (z.B. eine Fläche) auszuwählen. Es kann auch ein Verbund ausgewählt werden, der alle zu verbindenden Formen enthält, z.B. eine [rechtwinklige Anordnung](Draft_OrthoArray/de.md).
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Part_BooleanFragments.svg" width=16px> [Boolesche Bestandteile](Part_BooleanFragments/de.md)** drücken.
    -   Den Menüeintrag **Part → Teilen → Boolesche Bestandteile** auswählen.
3.  Ein parametrisches Boolesche-Bestandteile-Objekt wird erstellt. Die originalen Objekte werden ausgeblendet und das Ergebnis des Schneidens wird in der [3D-Ansicht](3D_view/de.md) angezeigt.



## Eigenschaften


{{TitleProperty|Boolesche Fragmente}}

-    {{PropertyData/de|Objekte}}}: Liste der zu kreuzenden Objekte. Im Allgemeinen werden mindestens zwei Objekte benötigt, aber eine einzige Verbindung, die die zu schneidenden Formen enthält, reicht ebenfalls aus. (ab FreeCAD v0.17.8053 wird diese Eigenschaft nicht mehr im Eigenschaftseditor angezeigt und kann nur noch über Python aufgerufen werden).

-   {{{PropertyData/de|Modus}}: \"Standard\", \" Teilen \" oder \" VerbundKörper \". \"Standard\" ist die Voreinstellung. Standard und Teilen unterscheiden sich durch die Wirkung des Werkzeugs auf Aggregationstypen: Wenn Teilen, werden diese getrennt; ansonsten werden sie zusammen gehalten (zusätzliche Segmente erhalten).

-    {{PropertyData/de|Toleranz}}: \"Unschärfe\" Wert. Dies ist eine zusätzliche Toleranz, die bei der Suche nach Schnittmengen zusätzlich zu den in den Eingabeformen gespeicherten Toleranzen angewendet wird.



## Implementierungsdetails

Das Werkzeug Boolesche Bestandteile im \"Standardmodus\" ist der allgemeine Verschmelzungs-Operator (engl.: General Fuse Operator (GFA)) von OpenCascade. Es akzeptiert eine Kombination von wahrscheinlich allen Formtypen, und die Logik der Ausgabe ist ziemlich kompliziert. Siehe [OpenCascade Benutzerhandbuch: Boolesche Verknüpfungen](https://www.opencascade.com/doc/occt-7.0.0/overview/html/occt_user_guides__boolean_operations.html).

Für die Modi \"Teilen\" und \"VerbundKörper\" erfolgt eine zusätzliche Nachbearbeitung durch FreeCAD.



## Skripten

Das Werkzeug kann in [Makros](macros/de.md) und von der Python-Konsole aus mit der folgenden Funktion verwendet werden:

**BOPTools.SplitFeatures.makeBooleanFragments(name)**

-   Erzeugt ein leeres BooleanFragment-Formelement. Die Eigenschaft \'Objects\' muss anschließend explizit zugewiesen werden.
-   Gibt das neu erstellte Objekt zurück.

BoolescheFragmente kann auch auf einfache Formen angewendet werden, ohne dass ein Dokumentobjekt erforderlich ist, via:


{{code|code=
import BOPTools.SplitAPI
BOPTools.SplitAPI.booleanFragments(list_of_shapes, mode, tolerance = 0.0)

# OR, for Standard mode:

list_of_shapes = [App.ActiveDocument.Sphere.Shape, App.ActiveDocument.Sphere001.Shape]
pieces, map = list_of_shapes[0].generalFuse(list_of_shapes[1:], tolerance)
# pieces receives a compound of shapes; map receives a list of lists of shapes, defining list_of_shapes <--> pieces correspondence 
}}

Dies kann nützlich sein, um benutzerdefinierte Python Skriptfunktionen zu erstellen.

Beispiel: {{code|code=
import BOPTools.SplitFeatures
j = BOPTools.SplitFeatures.makeBooleanFragments(name= 'BooleanFragments')
j.Objects = FreeCADGui.Selection.getSelection() 
}}

Das Werkzeug selbst ist in Python implementiert, siehe /Mod/Part/BOPTools/SplitFeatures.py unter dem FreeCAD installiert ist.



## Hinweise

Das Werkzeug wurde in FreeCAD v0.17.8053 eingeführt. FreeCAD muss mit OCC 6.9.0 oder höher kompiliert werden, da das Werkzeug sonst nicht verfügbar ist.





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part BooleanFragments/de
