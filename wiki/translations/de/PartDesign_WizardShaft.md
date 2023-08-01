---
- GuiCommand:
   Name: PartDesign WizardShaft
   Name/de: PartDesign EntwurfsassistentWellen
   MenuLocation: Part Design - Entwurfsassistent für Wellen...
   Workbenches: [PartDesign](PartDesign_Workbench/de.md)
---

# PartDesign WizardShaft/de



## Beschreibung

Dieses Werkzeug ermöglicht, eine Welle mit Hilfe einer Wertetabelle zu erstellen und Kräfte und Momente zu analysieren.



## Anwendung

Der Entwurfsassistent kann aus dem PartDesign-Menü **Part Design → [<img src=images/PartDesign_WizardShaft.svg style="width:20px"> Entwurfsassistent für Wellen...** gestartet werden.

Der Entwurfsassistent startet und zeigt eine Standardtabelle, den entsprechenden Wellenteil und Kraft-/Momenten-Diagramme an.

<img alt="" src=images/WizardShaft_Part.jpg  style="width:780px;">

Der obere Teil des Fensters wird von der Tabelle eingenommen. Diese ist in nummerierten Spalten organisiert, welche den Segmenten der Welle entsprechen. Ein Wellensegment ist dadurch gekennzeichnet, dass es eine bestimmte Länge und einen bestimmten Durchmesser aufweist. Das Hauptfenster zeigt zwei Registerkarten. Einer ist der Wellenteil selbst (eine Umdrehungseigenschaft), der im Bild oben gezeigt wird. Die zweite Registerkarte zeigt Diagramme der Scherkräfte und Momente, die durch die in der Tabelle definierten Lasten erzeugt werden.

<img alt="" src=images/shaftwizard1.jpg  style="width:1024px;">



## Voraussetzungen

Der Entwurfsassistent für Wellen hängt von der Bibliothek [matplotlib](http://matplotlib.org/) ab, um die Diagramme der Scherkraft und des Biegemoments zu erstellen und anzuzeigen. Auf Debian / Ubuntu-basierten Systemen ist diese über das Paket python-matplotlib verfügbar.



## Parameter

Für jedes Wellensegment können die folgenden Parameter definiert werden:

-   Länge des Segments
-   Durchmesser des Segments
-   Lasttyp. Beachten Sie, dass Sie nach dem Scrollen auf den gewünschten Eintrag im Menü klicken müssen, sonst wird er nicht ausgewählt!
    -   Keine: Keine Last
    -   Feststehend: Das Ende der Welle ist fixiert (z. B. mit einem anderen Teil verschweißt). Dieser Lasttyp kann nur für das erste oder letzte Segment definiert werden.
    -   Statisch: Dieses Wellensegment ist statisch belastet.
-   Belastung des Wellensegments
-   Position, an der die Last auf das Segment aufgebracht wird. Der Standort wird vom linken Rand des Segments gezählt (andere Zeilen und Lastarten existieren, aber es ist noch keine Funktionalität implementiert)



## Menüs

Um ein neues Wellensegment hinzuzufügen, klickt man mit der rechten Maustaste in den leeren Bereich rechts neben der Tabelle und wählt \"Add column\" (Spalte hinzufügen) aus.



## Einschränkungen

-   Es ist nicht möglich, benachbarte Wellensegmente mit demselben Durchmesser zu haben.



## Geplante Funktionalität 

-   Tabellengesteuerte Fasen und Rundungen an den Wellenkanten.
-   Erkennen eines zuvor mit dem Entwurfsassistenten für Wellen erstellten Bauteils und Initialisieren der Tabellenwerte von diesem.
-   Wellenspannungsberechnung.
-   Visualisierung von Lasten auf der Welle (kann die gleiche Funktionalität wie das FEM-Modul nutzen).
-   Definition von Lasten als Dokumentobjekt (kann die gleiche Funktionalität wie das FEM-Modul nutzen).
-   Materialdatenbank.
-   Zulassen von Lasten in Z-Richtung sowie in Y-Richtung (Definition von Lasten als Dokumentobjekt erforderlich, sonst wird die Tabelle sehr lang).





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign WizardShaft/de
