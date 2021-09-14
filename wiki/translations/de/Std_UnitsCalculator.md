---
- GuiCommand:/de
   Name:Std UnitsCalculator
   Name/de:Std Einheitenrechner
   MenuLocation:Werkzeuge → Einheitenrechner...
   Workbenches:Alle
---

## Beschreibung

Der **Std Einheitenrechner**-Befehl öffnet die Einheitenrechner-Dialogbox. Der Einheitenrechner kann genutzt werden, um Werte von einem Einheitensystem in ein anderes zu konvertieren.

![](images/Units_Calculator_it.png ) *Die Einheitenrechner-Dialogbox*

## Anwendung

1.  Wähle die **Werkzeuge → <img src="images/Std_UnitsCalculator.svg" width=16px> Einheitenrechner...**-Option aus dem Menü.
2.  Die Einheitenrechner-Dialogbox öffnet sich. Mehr Informationen findest du unter [Optionen](#Options.md).
3.  Die Dialogbox ist nicht modal, d.h sie kann während der Arbeit mit FreeCAD geöffnet bleiben.
4.  Drücke die **Schließen**-Schaltfläche, um die Dialogbox zu schließen.

## Optionen

### Oberste Zeile 

1.  Gib einen Wert mit Einheit in das erste Eingabefeld ein, z.B. {{Value|10 mm}}.
    -   Einheiten mit Exponenten sollten in der {{Value|^}}-Notation eingegeben werden, z.B. {{Value|1 m^2}}.
    -   Falls der Eingabewert nicht erkannt werden kann oder die Einheit unbekannt ist, wird im **=\>**-Feld die Meldung \'syntax error\' angezeigt.
2.  Gib die Zieleinheit in das **als**-Eingabefeld ein, z.B. {{Value|in}}.
    -   Falls die Einheit unbekannt ist, wird im **=\>**-Feld die Meldung \'unknown unit\' angezeigt.
    -   Falls die Einheit im ersten und zweiten Eingabefeld nicht in der gleichen Maßeinheitkategorie sind, wird im **=\>**-Feld die Meldung \'unit mismatch\' angezeigt. Im Beispiel sind die Einheiten in der gleichen Kategorie, weil \'mm\' und \'in\' beides Längeneinheiten sind.
3.  Wenn es keine Eingabefehler gibt, wird im **=\>**-Feld sofort das Ergebnis angezeigt. Für die Beispielwerte ist das Ergebnis {{Value|0,394 in}}.
4.  Wahlweise kannst du die **Kopieren**-Schaltfläche drücken, um den Inhalt des **=\>**-Feldes in die Zwischenablage zu kopieren. Der Wert kann dann bspw. in ein FreeCAD-Aufgaben-Feld oder eine Dialogbox eingefügt werden.

### Textbereich

1.  Die in der obersten Zeile durchgeführte Konvertierung kann durch Drücken von **Enter** im ersten oder zweiten Eingabefeld in den Textbereich kopiert werden.
2.  Der Textbereich kann mehrere Konvertierungen enthalten und sein Inhalt kann ausgewählt und durch gleichzeitiges Betätigen von **Strg**+**C** in die Zwischenablage kopiert und in anderen Programmen benutzt werden.

### Anzahl


**Dieser neue Teil ({{Version/de|0.19**) des Einheitenrechners enthält noch einige Fehlerchen.}}

1.  Wähle eine Option aus der **Einheitensystem**-Aufklappliste. Dies wird das Zieleinheitensystem. Wähle **Preference system**, um das Einheitensystem zu verwenden, das in den [Einstellungen](Preferences_Editor/de#Units.md) definiert ist.
2.  Wähle eine Option aus der **Maßeinheitenkategorie**-Aufklappliste.
3.  Gib einen Wert mit Einheit in das **Anzahl**-Eingabefeld ein. Die Einheit muss zur Maßeinheitenkategorie passen.
    -   Falls die **Area**-Einheitenkategorie (Fläche) ausgewählt wurde, ist die Eingabe von bestimmten Einheiten problematisch. Um bspw. {{Value|m^2}} einzugeben, musst du zuerst {{Value|^2}} eingeben, den Cursor dann vor dem {{Value|^}}-Zeichen platzieren und dann {{Value|m}} eingeben.
4.  Klicke in das **Dezimalstellen**-Eingabefeld und drücke **Enter**, um den Wert im **Anzahl**-Eingabefeld zu konvertieren.

## Hinweise

-   Siehe die [Ausdrücke](Expressions/de#Units.md)-Seite für eine Liste aller bekannten Einheiten.





{{Std Base navi

}}  
