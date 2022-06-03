---
- GuiCommand   */de
   Name   *PartDesign MultiTransform
   Name/de   *PartDesign MehrfachTransformation
   MenuLocation   *PartDesign → Muster anwenden → Mehrfach-Transformation erstellen
   Workbenches   *[Part Design](PartDesign_Workbench/de.md)
---

# PartDesign MultiTransform/de

## Beschreibung

\'Ein Muster aus Kombinationen von Umwandlungen herstellen\' - Die **![](images/)_[Mehrfach-Transformation](PartDesign_MultiTransform.md)** nimmt eine (oder einen Satz von) Part \'Formelementen\' als seine Eingabe und ermöglicht es dem Anwender, mehrfache Transformationen auf dieses Formelement (oder diesen Satz von Formelementen) zunehmend, der Reihe nach - eine gemeinsame oder zusammengesetzte Transformation zu erzeugen.

Zum Beispiel, um den Flansch mit einer doppelten Lochreihe, wie unten abgebildet, herzustellen, der Anwender   *

1.  wählt die Bohrung als \'Element\' (Basis) im Modellbaum aus
2.  klickt auf das **![](images/)_[Erstellen_einer_Mehrfach-Transformation](PartDesign_MultiTransform/de.md)** Symbol.
3.  fügt ein lineares Muster mit zwei Vorkommen in X Richtung hinzu
4.  fügt ein polares Muster mit acht Vorkommen um die Y Achse hinzu.

<img alt="" src=images/multitransform_example.png  style="width   *600px;"> 
*Flansch mit doppelter Lochreihe. Lochmuster erstellt mit 'Mehrfach-Transformation'.*

## Anwendung

Bevor mit einer der folgenden Methoden begonnen wird, muß das erforderliche **![](images/)_[Körper](PartDesign_Body/de.md)** -Objekt [aktiv](PartDesign_Body/de#Anwendungs_Hinweise.md) sein. Ansonsten erscheint die Fehlermeldung, dass ein **![](images/)_[Körper](PartDesign_Body/de.md)** -Objekt vor der Anwendung des **![](images/)__[MehrfachTransformation](PartDesign_MultiTransform/de.md)**s-Werkzeuges aktiv sein muss.

### Standardmethode

Diese Methode beginnt ohne vorhandene Transformationsformelemente und ohne ausgewählte Elemente im Ansichtsfenster oder im Modellobjektbaum.
Wenn mit dieser Methode begonnen und abgeschlossen wird, sollte die **![](images/)_[Mehrfachtransformation](PartDesign_MultiTransform/de.md)** korrekterweise das oberste Element des Körperobjekts werden.

1.  Klicke auf das **![](images/)__[MehrfachTransformation](PartDesign_MultiTransform/de.md)**ssymbol, um den Vorgang einzuleiten.
2.  Du wirst mit dem Fenster **Formelement auswählen** aufgefordert, eines auszuwählen.
    Wähle aus der Liste ein Anfangselement aus, das für die Transformationen verwendet werden soll und klicke auf **OK**, um fortzufahren.
    Du kannst im nächsten Schritt weitere Formelemente hinzufügen.

       *   <img alt="" src=images/PartDesign-MultiTransform-Select_feature.png  style="width   *300px;">
3.  Das Fenster **Transformierte Funktionsmeldungen** und das Fenster **Parameter Mehrfachtransformation** erscheint.
    Du siehst die Beschriftung des Formelements, das du in der Formelementlistenansicht ausgewählt hast, unter den Schaltflächen **Element hinzufügen** und **Element entfernen**.
    <img alt="" src=images/PartDesign-MultiTransform-General.png  style="width   *300px;">
4.  Wenn du zusätzliche Elemente für die Transformationen aufnehmen möchtest,   *
    1.  klicke auf **Element hinzufügen** im Transformationswerkzeug
    2.  wechsle in die Modellbaumansicht (Klicke auf den **Modell**-Reiter)
    3.  wähle das Element, das du hinzufügen möchtest und mache es sichtbar (Leertaste oder Rechtsklick und schalte die Sichtbarkeit um).

           *   **Hinweis   *** Dadurch wird das zuvor sichtbare Element ausgeblendet.
    4.  klicke auf ein Element in der 3D Ansicht (Ansichtsbereich).
    5.  klicke auf den Aufgaben-Reiter in der Comboansicht, um zum Fenster Multitransformparameter zurückzukehren.
        Du solltest in der Elementenliste das zuvor ausgewählte Element sehen.
5.  Unter der Elementenliste befindet sich die Transformationen-Liste. Darin solltest du den Text Hinzufügen mittels Rechtsklick sehen.
6.  Füge in der Transformationenliste eine Transformation durch Rechtsklick hinzu, um die Optionsliste anzuzeigen.
    <img alt="" src=images/PartDesign-MultiTransform-Transformations_Right_Click.png  style="width   *300px;">
    1.  Füge die gewünschte Transformation hinzu, indem du sie in der Optionsliste auswählst.
    2.  Der neue Transformationseintrag erscheint in der Liste Transformationen mit den entsprechenden Einstellungen unterhalb der Liste.

           *   <img alt="" src=images/PartDesign-MultiTransform-Transformations-add_linear_pattern.png  style="width   *300px;">
    3.  Passe die Einstellungen für die neue Transformation an. (*Du wirst die Vorschau im Ansichtsbereich sehen.*)
    4.  Klicke unter diesen Einstellungen **OK**, um die neue Transformation zu sichern.
7.  Fahre mit dem Hinzufügen von Transformationen in der gewünschten Reihenfolge unter Verwendung von Schritt 5 oben fort.
8.  Du kannst durch Rechtsklick auf eine Transformation in der Liste Transformationen und Auswahl der entsprechenden Option die Transformationen auch nach Bedarf bearbeiten, löschen und verschieben, also die Reihenfolge der Transformationen ändern.
9.  Wenn du mit dem Hinzufügen und Bearbeiten der Transformationen fertig bist, klicke ganz oben auf **OK**, um die **![](images/)_[Mehrfach-Transformation](PartDesign_MultiTransform/de.md)** zu speichern und zu beenden.

### Alternative Methode 1 

Diese Methode beginnt mit einem vorhandenen Transformationslement im **![](images/)_[Körper](PartDesign_Body/de.md)**-Objekt.

1.  Wähle im Modellbaum innerhalb des aktiven Körperobjekts die vorhandenen Formelemente aus, die einbezogen werden sollen.
2.  Klicke auf das **![](images/)_[MehrfachTransformation](PartDesign_MultiTransform/de.md)**, um die Operation zu starten.
3.  In der Formelemente Listenansicht siehst du die Beschriftung(en) des/der zuvor ausgewählten Formelement(e).
    Um weitere Formelemente hinzuzufügen, siehe **Schritt 3** in der [Standard Methode](PartDesign_MultiTransform/de#Standard_Methode.md) oben.
4.  Beende die **Schritte 5-8** in der [Standard Methode](PartDesign_MultiTransform/de#Standard_Methode.md) oben.

### Alternative Methode 2 

Diese Methode beginnt mit mehreren vorhandenen, unabhängigen Transformationen im **![](images/)_[Körper](PartDesign_Body.md)**, um sie zu kombinieren.
ANMERKUNG   * um bestehende Transformationen zu kombinieren, müssen sie sich innerhalb desselben Körpers befinden und sollten alle dasselbe Formelement oder denselben Elementesatz in jedem Objekt verwenden.

1.  Wähle im Modellbaum innerhalb des aktiven Körperobjekts eine der vorhandenen Transformationen aus, die du einbeziehen möchtest.
2.  Klicke auf den **![](images/)_[MehrfachTransformation](PartDesign_MultiTransform/de.md)**, um den Vorgang zu starten.
3.  Klicke auf die Schaltfläche **OK** oben, um zu speichern und zu beenden.
4.  Wähle im Objektbaum die gerade erstellte **![](images/)_[MehrfachTransformation](PartDesign_MultiTransform/de.md)**.
5.  Suche im Fenster *Eigenschaftsansicht* die Eigenschaft **Transformationen** auf dem Reiter *Daten*.
6.  Bearbeite die Eigenschaft **Transformationen**, indem du auf ihren Wert klickst, und klicke dann auf das erscheinende Ellipsenfeld, um das Fenster **Verknüpfungen** für diese Eigenschaft zu öffnen.
7.  Wähle alle vorhandenen Formelementtransformationen aus, die einbezogen werden sollen. Eine Mehrfachauswahl ist mit **Strg** + Klick zulässig.
8.  Klicke auf **OK**, um zu speichern und das **Verknüpfungs**-Fenster zu schließen.
9.  Klicke auf **![](images/)_[Aktualisieren](Std_Refresh/de.md)**, wenn diese Schaltfläche aktiviert ist.
    Wenn auf diese Weise eingeleitet und abgeschlossen wird, wird die **![](images/)_[MehrfachTransformation](PartDesign_MultiTransform/de.md)** möglicherweise nicht an der \"Spitze\" des Körperobjekts stehen.

Wenn du es an der \"Spitze\" benötigst   *

1.  klicke mit der rechten Maustaste auf die gerade erstellte **![](images/)_[Mehrfachtransformation](PartDesign_MultiTransform/de.md)**.
2.  falls verfügbar, wähle \"**Spitze setzen**\".

### Anwendungshinweise

-   Unterstützte Transformationenfunktionen sind   *
    **<img src="images/PartDesign_Mirrored.svg" width=20px>[Gespiegelt](PartDesign_Mirrored/de.md)**, **<img src="images/PartDesign_LinearPattern.svg" width=20px> [Lineares Muster](PartDesign_LinearPattern/de.md)**, **<img src="images/PartDesign_PolarPattern.svg" width=20px> [Polares Muster](PartDesign_PolarPattern/de.md)** und SKALIERTE Transformation.
-   Jede mit der **![](images/)_[MehrfachTransformation](PartDesign_MultiTransform/de.md)** verknüpfte Transformation sollte das gleiche Formelement oder den gleichen Satz von Formelementen verwenden.

### Einschränkungen

-   Eine skalierte Transformation sollte nicht die erste in der Liste sein
-   Die skalierte Transformation muss die gleiche Anzahl von Vorkommen haben, wie die Transformation, die ihr in der Liste unmittelbar vorausgeht
-   Für weitere Einschränkungen siehe **<img src="images/PartDesign_LinearPattern.svg" width=20px> [Lineares Muster](PartDesign_LinearPattern/de.md)
**




## Optionen

+++
| ![](images/Multitransfrom_parameters.png ) | Beim Erstellen eines Mehrfachtransformationselementes bietet der Dialog \'Mehrfachtransformation Parameter\' zwei verschiedene Listenansichten.                                                                                                                                                                                                                                                                 |
|                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                    | ### Originale auswählen                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                    | Die Listenansicht zeigt die \'Originale\', also die Formelemente, die transformiert werden sollen. Wenn du auf ein beliebiges Element klickst, wird es der Liste hinzugefügt.                                                                                                                                                                                                                                   |
|                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                    | ### Wähle Umwandlungen                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                    | Diese Liste kann mit einer Kombination aus den einfachen Transformation [gespiegelt](PartDesign_Mirrored/de.md), [lineares Muster](PartDesign_LinearPattern/de.md), [polares Muster](PartDesign_PolarPattern/de.md) und [skaliert](PartDesign_Scaled/de.md) gefüllt werden. Die Transformationen werden nacheinander angewendet. Das Kontextmenü bietet die folgenden Einträge   * |
|                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                    | #### Bearbeiten                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                    | Erlaubt die Bearbeitung der Parameter einer Transformation in der Liste (Doppelklick hat den gleichen Effekt)                                                                                                                                                                                                                                                                                                   |
|                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                    | #### Löschen                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                    | Entfernt eine Transformation aus der Liste.                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                    | #### Transformation hinzufügen                                                                                                                                                                                                                                                                                                                                                      |
|                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                    | Fügt der Liste eine Transformation hinzu.                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                    | #### Nach oben/unten bewegen                                                                                                                                                                                                                                                                                                                                                           |
|                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                    | Erlaubt die Änderung der Reihenfolge der Transformationen in der Liste.                                                                                                                                                                                                                                                                                                                                         |
+++

## Beispiele

![c\|800px](images/mt_example2.png ) 
*Die kleinste Aufpolsterung wurde zunächst dreimal in X Richtung aufgereiht und dann mit dem Faktor zwei skaliert (die drei Vorkommen haben also den Skalierungsfaktor 1,0, 1,5 und 2,0). Dann wurde ein lineares Muster 8-fach angewendet.* ![c\|800px](images/mt_example3.png ) 
*Die Tasche wurde zunächst auf der YZ Ebene gespiegelt und dann mit zwei linearen Mustern aufgereiht, um ein rechteckiges Muster zu erhalten.* 





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign MultiTransform/de
