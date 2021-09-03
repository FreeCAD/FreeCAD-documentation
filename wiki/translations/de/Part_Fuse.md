---
- GuiCommand:/de
   Name:Part Fuse
   Name/de:Part Verschmelzung
   MenuLocation:Part → Boolesche Operation → Vereinigung
   Workbenches:[Part](Part_Workbench/de.md)
   SeeAlso:[Part Boolsche Operationen](Part_Boolean/de.md), [Part Schneiden](Part_Cut/de.md), [Part Gemeinsam](Part_Common/de.md), 
---


</div>

## Beschreibung

Das **![](images/)_[Part_verschmelzen](Part_Fuse/de.md)** Werkzeug verschmilzt (vereint) ausgewählte Part Objekte zu einem. Diese Operation ist voll parametrisch und die Komponenten können geändert und das Ergebnis erneut berechnet werden.

**Hinweis:** Dieser Befehl ist eine automatisierte Form der <img alt="" src=images/Part_Boolean.svg  style="width:24px;"> [Booleschen Operation](Part_Boolean/de.md).

## Anwendung

1.  Wähle zwei oder mehr Formen
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Drücke die **![](images/) Part Verschmelzung** Schaltfläche in der **Part Werkzeuge** Werkzeugleiste
    -   Verwende den {{MenuCommand|Part → Boolesche  Operation → Vereinigen}} Eintrag im Part Menü

## Unterstützte Eingaben {#unterstützte_eingaben}

Eingabeobjekte müssen [OpenCascade](OpenCascade.md) Formen sein. Beispiele: Dinge, die mit den Arbeitsbereichen Part, PartDesign, Skizzierer erstellt wurde. Keine Polygonnetze (es sei denn, diese wurden in Formen konvertiert) - für Polygonnetze gibt es gesonderte boolesche Werkzeuge im Netzkonstruktionsarbeitsbereich.

-   Festkörper + Festkörper: das Ergebnis ist ein Festkörper, der das gesamte von den Eingaben abgedeckte Volumen einnimmt

-   Hülle + Hülle, Hülle + Fläche, Fläche + Fläche: Das Ergebnis ist eine Hülle. Wo sich Flächen kreuzen, werden sie geteilt. Hüllen können nicht-vielfältig sein. Nach der Verschmelzung können Flächen durch das Ergebnis [Verfeinerung](Part_RefineShape/de.md) vereinigt werden.

-   Linienzug + Linienzug, Kante + Linienzug, Kante + Kante: Das Ergebnis ist ein Linienzug. Kanten werden geteilt, wo sie sich kreuzen.

Verbunde werden unterstützt; es wird jedoch davon ausgegangen, dass sich in einen Verbund gepackte Formen nicht berühren oder kreuzen. Wenn sie es tatsächlich tun, wird die Verschmelzung wahrscheinlich fehlschlagen oder ein falsches Ergebnis liefern.

## Optionen

Elemente können der Verschmelzung hinzugefügt und entfernt werden, indem sie mit der Maus in der Baumansicht in das Verschmelzungsformelement hinein oder aus ihm heraus gezogen werden. Eine manuelle Neuberechnung (drücke **F5** Taste oder klicke auf das <img alt="" src=images/Std_Refresh.svg  style="width:24px;"> [Aktualisieren/Neuberechnen](Std_Refresh/de.md) Symbol) ist erforderlich, um die Ergebnisse zu sehen.

Nachdem dieser Vorgang abgeschlossen ist, kann es notwendig sein, die Form mit <img alt="" src=images/Part_RefineShape.svg  style="width:24px;"> [FormVerfeinern](Part_RefineShape/de.md) zu säubern.


<div class="mw-translate-fuzzy">





</div>


  
