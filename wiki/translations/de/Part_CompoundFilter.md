---
- GuiCommand:/de
   Name:Part Compound‏‎Filter
   Name/de:Part VerbundFilter
   MenuLocation:Part → Verbund Filter
   Workbenches:[Part](Part_Workbench/de.md)
   Version:0.17
---

# Part CompoundFilter/de


</div>

![](images/CompoundFilter.png )

## Beschreibung


<div class="mw-translate-fuzzy">

Der VerbundFilter kann verwendet werden, um die einzelnen Teile des Ergebnisses z.B. eines [Part Scheibe](Part_Slice/de.md) Vorgangs zu entnehmen, bei dem Du ein Objekt geteilt hast.


</div>

Es kann Kinder nach ihren Indizes herausnehmen, Kinder auf Kollisionen mit Schablonenform testen und Kinder nach ihren Eigenschaften wie Länge, Fläche, Volumen filtern.

Wenn im Ergebnis nur ein Kind vorhanden ist, ist die Ausgabe das Kind. Wenn es mehr als ein Kind gibt, das ausgegeben werden soll, ist die Ausgabe ein neuer Verbund.

## Anwendung


<div class="mw-translate-fuzzy">

1.  Wähle das geschnittene Objekt
2.  Wende {{MenuCommand/de|Menü → Teil → Verbund → VerbundFilter}} an
3.  Wähle das VerbundFilterObjekt im Baum aus
4.  In der Registerkarte Eigenschaften stelle \"Filtertyp\" auf \"bestimmte Punkte\" ein.
5.  Setze Punkte auf die Elemente, die Sie herausnehmen möchten.
    1.  Für ein einzelnes Stück ist dies eine Zahl, die mit 0 beginnt, d.h. wenn du das erste Element extrahieren möchtest, gib 0 in dieses Feld ein, 1 für das nächste Element\....
    2.  Wenn Du mehr als ein Stück auf einmal extrahieren möchtest, trenne die Zahlen mit \";\", z.B. wird ein Wert von \"0;2\" das erste und das dritte Element extrahieren.
    3.  Der allgemeine Fall - der auch die oben genannten Möglichkeiten abdeckt - ist eine Liste von Indexbereichen, die in Python-Notation angegeben ist, aber ohne Klammern. Bereiche können mit Semikolon verkettet werden. Zum Beispiel:
        -   7:10 nehmen Kinder der Indizes 7, 8 und 9 auf (Indizes sind nullbasiert; Bereich bis Index ist ausgeschlossen).
        -   1;2 Kinder 1 und 2 nehmen (erster Bereich ist Kind 1, zweiter Bereich ist Kind 2, Bereiche, die durch Semikolon verbunden sind).
        -   0;-1 erste Kinder (Index 0) und letztes Kind (Index -1 bedeutet letztes Kind, -2 - eines aber letztes, und so weiter) nehmen.
        -   1: nimm alles außer dem ersten Kind (fehlender Index bedeutet \"bis zum Ende\").
        -   ::-1 nimm alle Kinder in umgekehrter Reihenfolge.
        -   ::2 nimm alle ungeraden Kinder, d.h. Indizes, 1,3,5,\...., das sind die Einschübe 2,4,6, \.....
        -   :;: wiederhole den Eingangsverbund zweimal.
6.  Wenn du ein anderes Stück extrahieren möchtest, wähle das geschnittene Objekt erneut aus. Es wird nun unter dem VerbundFilter im Baum platziert.
7.  Wiederhole den Auswahlprozess von oben. Die Scheibe und seine Unterelemente werden unter beiden VerbundFiltern angezeigt; sie werden natürlich im Modell nicht wiederholt. Eine sehr schnelle Möglichkeit, ein anderes Stück zu extrahieren, ist das Kopieren des VerbundFilters. Aber **Achtung**: Du wirst gefragt, ob du auch die Elemente unter dem VerbundFilter kopieren möchtest, was du mit *Nein* beantworten musst, du willst sie nicht kopieren, du referenzierst sie nur.


</div>

## Eigenschaften

-    {{PropertyData/de|Basis}}: Objekt, das gefiltert werden soll.

-    {{PropertyData/de|Filtertyp}}wählbare Optionen:

    -   Umgehung; kein Filter. Der ursprüngliche Verbund wird unverändert ausgegeben.
    -   bestimmte Elemente; extrahiere die Elemente, die in der Eigenschaft \"Elemente\" aufgelistet sind
    -   Kollisions-Umgehung; Stücke herausnehmen, die die \'Schablonen\' Form berühren oder kreuzen.
    -   Fenster-Volumen (Standard); extrahiere alle Stücke, die ein Volumen zwischen \"Fenster von\" und \"Fenster bis\" haben, wobei 100 % das größte Stück ist - und nicht das ungeschnittene Objekt. Der Wert von 100% ist ein Referenzwert, der durch \"ÜberschreibeMaxWert\" außer Kraft gesetzt werden kann.
    -   Fenster-Bereich; dasselbe wie Fenster-Volumen, wobei der geschnittene Bereich anstelle des Volumens die Auswahl bestimmt.
    -   Fenster-Länge; dasselbe wie Fenster-Volumen, wobei die Länge der Kanten statt des Volumens die Auswahl bestimmt.
    -   Fenster-Abstand; extrahiere Kinder, deren Abstand zur \'Schablonen\' Form innerhalb des Wertefensters liegt, definiert durch die Eigenschaften \"FensterVon\", \" FensterBis\", \"ÜberschreibenMaxWert\".

-    {{PropertyData/de|Umkehrung}}: Wenn auf true gesetzt, wird die Liste, wie oben beschrieben, ausgeschlossen statt einbezogen.

-    {{PropertyData/de|Überschreiben Max Wert}}: Der Wertefensterbereich wird in Prozent des Maximalwerts definiert. Der Maximalwert wird nach den folgenden Regeln berechnet:

    -   andernfalls, wenn die\'Schablonen\' Verknüpfung geliefert wird - berechne den entsprechenden Wert der Schablonenform (nicht anwendbar für den Fensterabstand \'FilterTyp\')
    -   andernfalls nimm den Maximalwert von Kindern im zu filternden Verbund.

-    {{PropertyData/de|Schablone}}: Verknüpfung zu einer Schablonenform. Bei den FilterTypen Kollisions-Umgehung und Fenster-Abstand ist Schablone das Objekt, gegen das die Kollision/der Abstand getestet werden soll. Bei anderen \"Fenster-\*\*\*\" Filtertypen wird Schablone verwendet, um Referenzwerte für Fensterprozentsätze zu liefern (Maximalwert Überschreiben). In allen anderen Modi wird \"Schablone\" ignoriert.

-    {{PropertyData/de|Fenster von}}: Oberer Schwellenprozentsatz für die Auswahl von Stücken, 100% ist relativ zum größten Stück.

-    {{PropertyData/de|Fenster bis}}: Unterer Schwellenprozentsatz für die Auswahl der Stücke, 100 % ist relativ zum größten Stück.

-    {{PropertyData/de|Elemente}}: Liste oder Bereich von Elementen, die ausgewählt werden sollen, wenn Filtertyp \"bestimmte Elemente\" ist.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part CompoundFilter/de
