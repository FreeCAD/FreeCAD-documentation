---
- GuiCommand   */de
   Name   *PartDesign Scaled
   Name/de   *PartDesign Skalieren
   Workbenches   *[PartDesign](PartDesign_Workbench/de.md)
   MenuLocation   *None (Option unter Part Design → Muster anwenden → Mehrfach-Transform erstellen)
---

# PartDesign Scaled/de

## Beschreibung

<img alt="" src=images/PartDesign_Scaled.svg  style="width   *24px;"> **PartDesign Skalieren** ist eine der Transformationsoptionen von <img alt="" src=images/PartDesign_MultiTransform.svg  style="width   *16px;"> [MehrfachTransformation](PartDesign_MultiTransform/de.md). Im Gegensatz zu den anderen Optionen ist diese nicht als eigenständiges Werkzeug vorhanden. Es wandelt das Ergebnis einer Transformation in eine Abfolge skalierter Objekte mit gleichmäßig verteilten Skalierungsfaktoren. Am nicht skalierten Ausgangselement startend, wächst oder schrumpft der Skalierungsfaktor, bis er den gegebenen Wert am letzten Element erreicht.

<img alt="" src=images/PartDesign_Scaled-01.png  style="width   *300px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/PartDesign_Scaled-02.png  style="width   *300px;"> 
*Ein lineares Muster und ein polares Muster → Skaliertes lineares Muster mit 3 Schritten (Vorkommen) und polares Muster mit 12 Schritten*

Wenn noch keine Transformation in der <img alt="" src=images/PartDesign_MultiTransform.svg  style="width   *16px;"> [MehrfachTransformation](PartDesign_MultiTransform/de.md) vorhanden ist, werden skalierte Elemente an derselben Position eingefügt, an der das Ausgangselement liegt. Dies kann zu unerwarteten Ergebnissen führen, wenn das Ausgangselement nicht komplett vom skalierten Element umhüllt wird. Und daher ist es nicht ratsam, **Skaliert** als einzige oder als erste Transformation einer MehrfachTransformation zu verwenden.

<img alt="" src=images/PartDesign_Scaled-03.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/PartDesign_Scaled-04.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/PartDesign_Scaled-05.png  style="width   *200px;"> 
*Ein Ausgangselement mit einem Loch → Skaliertes Objekt mit 2 Vorkommen → Skaliertes Objekt mit 4 Vorkommen *

## Anwendung

### Ein transformiertes Element skalieren 

1.  Man startet mit einer der folgenden Möglichkeiten   *
    -   Ein Doppelklick auf das MultiTransform-Objekt in der [Baumansicht](Tree_view/de.md).
    -   Rechtsklick auf das MultiTransform-Objekt in der [Baumansicht](Tree_view/de.md) und **MultiTransform bearbeiten** im Kontextmenü auswählen.
2.  Der [Aufgabenbereich](Task_panel/de.md) **Parameter der Mehrfach-Transformation** wird geöffnet.
3.  Rechtsklick in die Liste **Transformationen** und **Skalierte Transformation hinzufügen** im Kontextmenü auswählen.
4.  Ein **Scaled**-Objekt wird zur Liste hinzugefügt und der Aufgabenbereich unten erweitert, um **Faktor** und **Vorkommen** zu bearbeiten. Siehe [Optionen](#Optionen.md) für weitere Informationen.
5.  Untere **OK**-Leiste anklicken, um die Optionen zu bestätigen.
6.  Obere Schaltfläche **OK** anklicken zum Fertigstellen.

### Ein einzelnes Element skalieren 

1.  Ein Formelement des aktiven Körpers in der [Baumansicht](Tree_view/de.md) auswählen.
2.  Eine der folgenden Möglichkeiten auswählen   *
    -   Die Schaltfläche **<img src="images/PartDesign_MultiTransform.svg" width=16px> [Mehrfach-Transformation erstellen](PartDesign_MultiTransform/de.md)** drücken.
    -   Den Menüeintrag **Part Design → Muster anwenden → <img src="images/PartDesign_MultiTransform.svg" width=16px> Mehrfach-Transformation erstellen** auswählen.
3.  Der [Aufgabenbereich](Task_panel/de.md) **Parameter der Mehrfach-Transformation** wird geöffnet. Siehe oben.

## Optionen

-    **Faktor**   * Der Faktor bis zu dem das letzte Element skaliert wird.

-    **Vorkommen**   * Anzahl der Schritte von nicht skaliert (1) bis **Faktor** (einschließlich Ausgangs- und letztem Element).

    -   Die Transformation Skaliert akzeptiert die Anzahl der Vorkommen der vorherigen Transformation als maximalen Wert oder jeden ganzzahligen Teiler dieser Anzahl, der ein ganzzahliges Ergebnis liefert. So sind {{Value|12}}, {{Value|6}}, {{Value|4}}, {{Value|3}}und {{Value|2}} gültig für ein lineares oder polares Muster mit 12 Vorkommen.
    -   Für ein einzelnes skaliertes Formelement wird jeder ganzzahlige Wert größer als 1 akzeptiert.

## Hinweise

-   Das Zentrum der Skalierung ist der Schwerpunkt des Formelements und kann folgendes auslösen   *
    -   Ein wachsendes Element, das aus der Rückseite des übergeordneten Elements hervor tritt.
    -   Ein schrumpfendes Element, das den Kontakt mit dem übergeordneten Element verliert und verschwindet.
    -   Eine schrumpfende Tasche, die zu einem unsichtbaren Hohlraum im übergeordneten Element wird.





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Scaled/de
