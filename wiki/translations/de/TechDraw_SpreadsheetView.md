---
 GuiCommand:
   Name: TechDraw SpreadsheetView
   Name/de: TechDraw Tabellenansicht
   MenuLocation: TechDraw , Views From Other Workbenches , Tabellenansicht einfügen
   Workbenches: TechDraw_Workbench/de, Spreadsheet_Workbench/de
---

# TechDraw SpreadsheetView/de



## Beschreibung

Das Werkzeug **TechDraw Tabellenansicht** ermöglicht es, eine ausgewählte [Kalkulationstabelle](Spreadsheet_Workbench/de.md) in einer Tabellenansicht auf einem [Zeichnungsblatt](TechDraw_Workbench/de.md) darzustellen.


{{Version/de|1.0}}

: Auch das Werkzeug [TechDraw Ansicht](TechDraw_View/de.md) kann eine Tabellenansicht erstellen.

![](images/TechDraw_Spreadsheetview.png ) 
*Darstellung einer eingefügten Kalkulationstabelle (Spreadsheet-Objekt) als Tabellenansicht (Sheet-Objekt) auf einem TechDraw-Zeichnungsblatt*



## Anwendung

1.  Ein Tabellenblatt in der [Baumansicht](Tree_view/de.md) auswählen.
2.  Wenn mehrere Zeichnungsblätter im Dokument vorhanden sind: Wahlweise das gewünschte Zeichnungsblatt durch Auswählen in der [Baumansicht](Tree_view/de.md) zur Auswahl hinzufügen.
3.  Den Menüeintrag **TechDraw → Ansichten von anderen Arbeitsbereichen → <img src="images/TechDraw_SpreadsheetView.svg" width=16px> Tabellenansicht einfügen** auswählen.
4.  Wenn mehrere Zeichnungsblätter im Dokument vorhanden sind und kein Blatt im [Hauptansichtsbereich](Main_view_area/de.md) angezeigt wird und außerdem noch kein Blatt aktiviert wurde, wird das Dialogfeld **Blattauswahl** geöffnet:
    1.  Das gewünschte Blatt auswählen.
    2.  Die Schaltfläche **OK** drücken.
5.  Eine Tabellenansicht wird eingefügt
6.  Den Zellenbereich anpassen, indem die {{PropertyData/de|Cell Start}} und die {{PropertyData/de|Cell End}} geändert werden.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Eine Tabellenansicht, oder formal ein {{Incode|TechDraw::DrawViewSpreadsheet}}-Objekt, besitzt die gemeinsamen [Eigenschaften](TechDraw_View/de#Eigenschaften_der_Bauteilansicht.md) aller Ansichtsarten. Sie enthält außerdem die folgenden Eigenschaften:



### Daten


{{TitleProperty|Drawing view}}

-    {{PropertyData/de|Symbol|String|Hidden}}: Der SVG-Code, der dieses Symbol definiert.

-    {{PropertyData/de|Editable Texts|StringList|Hidden}}: Ersatzwert für bearbeitbare Zeichenfolgen in diesem Symbol. Nicht in Verwendung.

-    {{PropertyData/de|Owner|Link}}: Formelement dem das Symbol zugeordnet ist. {{Version/de|1.0}}


{{TitleProperty|Spreadsheet}}

-    {{PropertyData/de|Source|Link}}(Quelle): Das zum Zeichungsblatt hinzuzufügende Tabellenblatt.

-    {{PropertyData/de|Cell Start|String}}(Zellanfang): Die linke obere Zelle des Zellbereichs, der dieser Ansicht hinzugefügt werden soll.

-    {{PropertyData/de|Cell End|String}}(Zellenende): Die rechte untere Zelle des Zellbereichs, der in diese Ansicht aufgenommen werden soll.

-    {{PropertyData/de|Font|Font}}(Schriftart): Der Name der für Texte verwendeten Schriftart.

-    {{PropertyData/de|Text Color|Color}}(Farbe): Die Farbe von Linien und Texten, denen in der Kalkulationstabelle kein Farbe zugewiesen wurde.

-    {{PropertyData/de|Text Size|Float}}(Schriftgröße): Die Schriftgröße von Texten.

-    {{PropertyData/de|Line Width|Float}}(Strichstärke): Die Breite der Zellränder.





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw SpreadsheetView/de
