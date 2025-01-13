---
 GuiCommand:
   Name: Part Compound‏‎Filter
   Name/de: Part VerbundFiltern
   MenuLocation: Formteil , Verbund , Verbundfilter
   Workbenches: Part_Workbench/de
   Version: 0.17
---

# Part CompoundFilter/de

![](images/CompoundFilter.png )



## Beschreibung

Der Verbundfilter kann verwendet werden, um die einzelnen Teile des Ergebnisses zu entnehmen z.B. eines [Part-Zerschneiden](Part_Slice/de.md)-Vorgangs, bei dem ein Objekt aufgeteilt wurde.

Es kann Kinder nach ihren Indizes herausnehmen, Kinder auf Kollisionen mit Schablonenform testen und Kinder nach ihren Eigenschaften wie Länge, Fläche, Volumen filtern.

Wenn im Ergebnis nur ein Kind vorhanden ist, ist die Ausgabe das Kind. Wenn es mehr als ein Kind gibt, das ausgegeben werden soll, ist die Ausgabe ein neuer Verbund.



## Anwendung

1.  Das aufgeteilte Objekt auswählen.

2.  
    **Part → Verbund → VerbundFilter**anwenden.

3.  Das CompoundFilter-Objekt im Baum auswählen.

4.  In der Registerkarte Eigenschaften den \"Filter Type\" auf \"specific items\" einstellen.

5.  Unter \"Items\" die Elemente auflisten, die extrahiert werden sollen.
    1.  Dies ist eine Nummer für jedes einzelne Stück; die Zählung beginnt mit 0, d.h. wenn das erste Element extrahiert werden soll, wird 0 in dieses Feld eingegeben, 1 für das nächste Element\....
    2.  Soll mehr als ein Stück auf einmal extrahiert werden, trennt man die Nummern mit \";\", z.B. wird \"0;2\" eingegeben, um das erste und das dritte Element zu extrahieren.
    3.  Der allgemeine Fall - der auch die oben genannten Möglichkeiten abdeckt - ist eine Liste von Indexbereichen, die in Python-Notation angegeben ist, aber ohne Klammern. Bereiche können mit Semikolon verkettet werden. Zum Beispiel:
        -   7:10 nimmt die zu den Indizes 7, 8 und 9 gehörenden Kindobjekte auf (Indizes sind nullbasiert; das Kindobjekt, das zum letzten Index 10 gehört, ist nicht mehr enthalten).
        -   1;2 nimmt die Kindobjekte 1 und 2 auf (der erster Bereich besteht (nur) aus Kind 1, der zweite Bereich aus Kind 2; die Bereiche werden durch Semikolon verbunden).
        -   0;-1 nimmt das erste Kind (Index 0) und das letzte Kind auf (Index -1 entspricht dem letzten Kind, -2 dem vorletzten usw.).
        -   1: nimmt alles außer dem ersten Kind auf (der fehlende Index bedeutet \"bis zum Ende\").
        -   ::-1 nimmt alle Kinder in umgekehrter Reihenfolge auf.
        -   ::2 nimm alle zu ungeraden Indizes gehörenden Kinder auf, d.h. Indizes, 1,3,5,\..., das sind die Elemente 2,4,6, \...
        -   :;: wiederholt den Eingangsverbund zweimal.

6.  Soll ein weiteres Stück extrahiert werden, wird das

aufgeteilte Objekt erneut ausgewählt. Es wird nun unter dem VerbundFilter im Baum platziert.

1.  Den obigen Auswahlprozess wiederholen. Das Slice-Objekt und seine Unterelemente werden unter beiden VerbundFiltern angezeigt; sie werden natürlich im Modell nicht wiederholt. Eine sehr schnelle Möglichkeit, ein weiteres Stück zu extrahieren, ist das Kopieren des VerbundFilters. Aber **Aufgepasst**: Wenn gefragt wird, ob auch die Elemente unter dem VerbundFilter kopiert werden sollen, muss dies mit *Nein* beantwortet werden; sie sollen nicht kopiert, sondern nur referenziert werden.



## Eigenschaften

-    **Base**: Objekt, das gefiltert werden soll.

-    **Filter Type**auswählbare Optionen:

    -   bypass: kein Filter. Der ursprüngliche Verbund wird unverändert ausgegeben.
    -   specific items: sucht die Elemente heraus, die in der Eigenschaft \"Elemente\" aufgelistet sind.
    -   collision-pass: sucht Stücke heraus, die die \'Schablonen\'-Form berühren oder überschneiden.
    -   window-volume (default): sucht alle Stücke heraus, die ein Volumen zwischen \"Window From\" (von Fenster) und \"Window To\" (bis Fenster) haben, wobei 100 % das größte Stück ist - und nicht das unzerschnittene Objekt. Der Wert von 100% ist ein Referenzwert, der durch \"OverrideMaxVal\" überschrieben werden kann.
    -   window-area: dasselbe wie window-volume (Fenster-Volumen), wobei der geschnittene Bereich anstelle des Volumens die Auswahl bestimmt.
    -   window-length: dasselbe wie window-volume, wobei die Länge der Kanten anstatt des Volumens die Auswahl bestimmt.
    -   window-distance: Sucht Kindobjekte heraus, deren Abstand zur \'Schablonen\'-Form innerhalb des Wertebereichs liegt, der durch die Eigenschaften \"Window From\" (von Fenster), \"Window To\" (bis Fenster) und \"Override Max Val\" festgelegt wird.

-    **Invert**: Wenn auf true gesetzt, wird die Liste, wie oben beschrieben, ausgeschlossen statt einbezogen.

-    **Override Max Val**: Der Fenster-Wertebereich wird in Prozent des Maximalwerts definiert. Der Maximalwert wird nach den folgenden Regeln berechnet:

    -   Ist der Wert \'OverrideMaxVal\' ungleich Null, wird er verwendet.
    -   andernfalls, wenn eine Verknüpfung zu einer Schablone (Stencil) vorhanden ist, wird der zugehörige Wert aus der Schablonenform berechnet. (nicht anwendbar auf die Filterart (FilterType) window-distance)
    -   andernfalls nimmt er den höchsten Wert der Kindobjekte im zu filternden Verbund an.

-    **Stencil**: Verknüpfung zu einer Schablonenform. Bei den Filterarten collision-pass und window-distance ist Stencil das Objekt, zu dem die Kollision bzw. der Abstand getestet werden soll. Bei anderen \"window-\*\*\*\"-Filterarten wird Stencil verwendet, um Referenzwerte für Prozentangaben der Fenster zur Verfügung zu stellen (Maximalwert überschreiben). In allen anderen Modi wird \"Stencil\" ignoriert.

-    **Window From**: Oberer Prozent-Grenzwert für die Auswahl von Stücken, 100% bezieht sich auf das größte Stück.

-    **Window To**: Unterer Prozent-Grenzwert für die Auswahl von Stücken, 100% bezieht sich auf das größte Stück.

-    **items**: Liste oder Bereich von Elementen, die ausgewählt werden sollen, wenn die Filterart \"specific items\" ausgewählt ist.



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part CompoundFilter/de
