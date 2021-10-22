---
- GuiCommand:/de
   Name:PartDesign MultiTransform
   Name/de:PartDesign MehrfachTransformation
   MenuLocation:PartDesign → Ein Muster anwenden → MehrfachTransformation
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
---

# PartDesign MultiTransform/de

## Beschreibung

\'Ein Muster aus Kombinationen von Umwandlungen herstellen\' - Die **![](images/)_[Mehrfach-Transformation](PartDesign_MultiTransform.md)** nimmt eine (oder einen Satz von) Part \'Formelementen\' als seine Eingabe und ermöglicht es dem Anwender, mehrfache Transformationen auf dieses Formelement (oder diesen Satz von Formelementen) zunehmend, der Reihe nach - eine gemeinsame oder zusammengesetzte Transformation zu erzeugen.

Zum Beispiel, um den Flansch mit einer doppelten Lochreihe, wie unten abgebildet, herzustellen, der Anwender:

1.  wählt die Bohrung als \'Element\' (Basis) im Modellbaum aus
2.  klickt auf das **![](images/)_[Erstellen_einer_Mehrfach-Transformation](PartDesign_MultiTransform/de.md)** Symbol.
3.  fügt ein lineares Muster mit zwei Vorkommen in X Richtung hinzu
4.  fügt ein polares Muster mit acht Vorkommen um die Y Achse hinzu.

<img alt="" src=images/multitransform_example.png  style="width:600px;"> 
*Flansch mit doppelter Lochreihe. Lochmuster erstellt mit 'Mehrfach-Transformation'.*

## Usage


<div class="mw-translate-fuzzy">

## Anwendung

Bevor mit einer der folgenden Methoden begonnen wird, stelle sicher, dass das erforderliche **![](images/)_[Körper](PartDesign_Body/de.md)** Objekt [aktiv](PartDesign_Body/de#Anwendungs_Hinweise.md) ist; wenn nicht, erhältst du eine Fehlermeldung, die besagt, dass du ein aktives **![](images/)_[Körper](PartDesign_Body/de.md)** Objekt vor der Anwendung des **![](images/)__[MehrfachTransformation](PartDesign_MultiTransform/de.md)**s Werkzeug benötigst.


</div>

### Standard Method 


<div class="mw-translate-fuzzy">

### Standardmethode

Diese Methode beginnt ohne vorhandene Transformations Formelementen und ohne Auswahlen im Ansichtsfenster oder im Modellobjektbaum.
Wenn mit dieser Methode begonnen und abgeschlossen wird, sollte die **![](images/)_[MehrfachTransformation](PartDesign_MultiTransform/de.md)** korrekt die \"Spitze\" des Körperobjekts werden.


</div>

1.  Klicke auf das **![](images/)__[MehrfachTransformation](PartDesign_MultiTransform/de.md)**ssymbol, um den Vorgang einzuleiten.
2.  Du wirst mit dem Fenster **Formelement auswählen** aufgefordert.
    Wähle aus der Liste ein Anfangselement aus, das für die Transformationen verwendet werden soll, und klicke auf **OK**, um fortzufahren.
    Du kannst im nächsten Schritt weitere Formelemente hinzufügen.

    :   <img alt="" src=images/PartDesign-MultiTransform-Select_feature.png  style="width:300px;">
3.  Das **Transformierte Formelemente Meldungen** und **MehrfachTransformation Parameter** Fenster erscheint.
    Du siehst die Beschriftung des Formelements, das du in der Formelementlistenansicht ausgewählt hast, unter den Schaltflächen **Element hinzufügen** und **Element entfernen**.

\#:<img alt="" src=images/PartDesign-MultiTransform-General.png  style="width:300px;">

\#:Wenn du zusätzliche Elemente für die Transformationen aufnehmen möchtest, folgen diesen Anweisungen:

1.  1.  Klicke die **Element hinzufügen** im Transformationswerkzeug
    2.  Wechsle in die Modellbaumansicht (Klicke auf den **Modell** Reiter)
    3.  Wähle das Element, das du hinzufügen möchtest, und mache es sichtbar (Leertaste, oder Rechtsklick und schalte die Sichtbarkeit um).

        :   **Hinweis:** Dadurch wird das zuvor sichtbare Element ausgeblendet.
    4.  Klicke auf ein Element in der 3D Ansicht (Ansichtsbereich).
    5.  Klicke auf den Aufgaben Reiter in der Comboansicht, um zum Fenster MultiTransform parameters zurückzukehren.
    6.  Du solltest in der Elementenliste das zuvor ausgewählte Element sehen.

2.  Unter der Elementeliste befindet sich die Transformationen Liste. Darin solltest du den Text Hinzufügen mittels Rechtsklick sehen.

3.  Füge eine Transformation durch Rechtsklick hinzu, in der Transformationenliste, um die Optionsliste anzuzeigen.

4.  <img alt="" src=images/PartDesign-MultiTransform-Transformations_Right_Click.png  style="width:300px;">
    1.  Füge die gewünschte Transformation hinzu, indem du sie in der Optionsliste auswählst.
    2.  Der neue Transformationseintrag erscheint in der Liste Transformationen mit den entsprechenden Einstellungen unterhalb der Liste.

        :   <img alt="" src=images/PartDesign-MultiTransform-Transformations-add_linear_pattern.png  style="width:300px;">
    3.  Passe die Einstellungen für die neue Transformation an. (*Du wirst die Vorschau im Ansichtsbereich sehen.*)
    4.  Klicke unter diesen Einstellungen **OK**, um die neue Transformation zu sichern.

5.  Fahre mit dem Hinzufügen von Transformationen in der gewünschten Reihenfolge unter Verwendung von Schritt 5 oben fort.

6.  Du kannst die Transformationen auch nach Bedarf bearbeiten, löschen und verschieben (die Reihenfolge der Transformationen ändern), durch Rechtsklick auf eine Transformation in der Liste Transformationen und Auswahl der entsprechende Option.

7.  Wenn du mit dem Hinzufügen und Bearbeiten der Transformationen fertig bist, klicke ganz oben **OK**, um die **![](images/)_[Mehrfach-Transformation](PartDesign_MultiTransform/de.md)** zu sichern und zu beenden.

### Alternate Method 1 


<div class="mw-translate-fuzzy">

### Alternative Methode 1 

Diese Methode beginnt mit einem vorhandenen Transformationslement im **![](images/)_[Körper](PartDesign_Body/de.md)** Objekt.


</div>

1.  Wähle im Modellbaum innerhalb des aktiven Körperobjekts die vorhandenen Formelemente aus, die einbezogen werden sollen.
2.  Klicke auf das **![](images/)_[MehrfachTransformation](PartDesign_MultiTransform/de.md)**, um die Operation zu starten.
3.  In der Formelemente Listenansicht siehst du die Beschriftung(en) des/der zuvor ausgewählten Formelement(e).
    Um weitere Formelemente hinzuzufügen, siehe **Schritt 3** in der [Standard Methode](PartDesign_MultiTransform/de#Standard_Methode.md) oben.
4.  Beende die **Schritte 5-8** in der [Standard Methode](PartDesign_MultiTransform/de#Standard_Methode.md) oben.

### Alternate Method 2 


<div class="mw-translate-fuzzy">

### Alternative Methode 2 

Diese Methode beginnt mit mehreren vorhandenen, unabhängigen Transformationen im **![](images/)_[Körper](PartDesign_Body.md)** - mit der Idee, sie zu kombinieren. ANMERKUNG: Um bestehende Transformationen zu kombinieren, müssen sie sich innerhalb desselben Körpers befinden und sollten alle dasselbe Formelement oder denselben Elementesatz in jedem Objekt verwenden.


</div>

1.  Wähle im Modellbaum innerhalb des aktiven Körperobjekts eine der vorhandenen Transformationen aus, die du einbeziehen möchtest.
2.  Klicke auf den **![](images/)_[MehrfachTransformation](PartDesign_MultiTransform/de.md)**, um den Vorgang zu starten.
3.  Klicke auf die Schaltfläche **OK** oben, um zu speichern und zu beenden.
4.  Wähle im Objektbaum den gerade erstellten **![](images/)_[MehrfachTransformation](PartDesign_MultiTransform/de.md)**.
5.  Im Fenster *Eigenschaftsansicht* suche die Eigenschaft **Transformationen** auf dem Reiter *Daten*.
6.  Bearbeite die Eigenschaft **Transformationen**, indem du auf ihren Wert klickst, und klicke dann auf das erscheinende Ellipsenfeld, um das Fenster **Verknüpfungen** für diese Eigenschaft zu öffnen.
7.  Wähle alle vorhandenen Formelement Transformationen aus, die einbezogen werden sollen. Mehrfachauswahlen sind mit **Strg** + Klick zulässig.
8.  Klicke auf **OK**, um zu speichern und das **Verknüpfungs** Fenster zu schließen.
9.  Klicke auf den **![](images/)_[Aktualisieren](Std_Refresh/de.md)**, wenn diese Schaltfläche aktiviert ist.

Wenn auf diese Weise eingeleitet und abgeschlossen, wird der **![](images/)_[MehrfachTransformation](PartDesign_MultiTransform/de.md)** möglicherweise nicht die \"Spitze\" des Körperobjekts werden. Wenn du es als \"Spitze\" benötigst:

1.  Klicke mit der rechten Maustaste auf den gerade erstellten **![](images/)_[MehrfachTransformation](PartDesign_MultiTransform/de.md)**.
2.  Falls verfügbar, wähle \"**Spitze setzen**\".

### Usage Notes 


<div class="mw-translate-fuzzy">

### Anwendungshinweise

-   Unterstützte Transformationen sind:


**<img src="images/PartDesign_Mirrored.svg" width=20px>[Gespiegelt](PartDesign_Mirrored/de.md)
**

, **<img src="images/PartDesign_LinearPattern.svg" width=20px> [Lineares Muster](PartDesign_LinearPattern/de.md)**, **<img src="images/PartDesign_PolarPattern.svg" width=20px> [Polares Muster](PartDesign_PolarPattern/de.md)** und SKALIERTE Transformation.

-   Jede mit der **![](images/)_[MehrfachTransformation](PartDesign_MultiTransform/de.md)** verknüpfte Transformationen sollte das gleiche Formelement oder den gleichen Satz von Formelementen verwenden.


</div>

### Limitations


<div class="mw-translate-fuzzy">

### Begrenzungen

-   Eine skalierte Transformation sollte nicht die erste in der Liste sein
-   Die skalierte Transformation muss die gleiche Anzahl von Vorkommen haben wie die Transformation, die ihr in der Liste unmittelbar vorausgeht
-   Für weitere Begrenzungen siehe **<img src="images/PartDesign_LinearPattern.svg" width=20px> [Lineares Muster](PartDesign_LinearPattern/de.md)
**





</div>

## Options


<div class="mw-translate-fuzzy">

## Optionen

+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ![](images/Multitransfrom_parameters.png ) | Beim Erstellen eines Mehrfach-Transformations Elements bietet der Dialog \'Mehrfach-Transformation Parameter\' zwei verschiedene Listenansichten.                                                                                                                                                                                                                                                             |
|                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                    | ### Originale auswählen                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                    | Die Listenansicht zeigt die \'Originale\', also die Formelemente, die transformiert werden sollen. Wenn du auf ein beliebiges Element klickst, wird es der Liste hinzugefügt.                                                                                                                                                                                                                                 |
|                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                    | ### Wähle Umwandlungen                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                    | Diese Liste kann mit einer Kombination aus den einfachen Transformation [gespiegelt](PartDesign_Mirrored/de.md), [lineares Muster](PartDesign_LinearPattern/de.md), [polar Muster](PartDesign_PolarPattern/de.md) und [skaliert](PartDesign_Scaled/de.md) gefüllt werden. Die Transformationen werden nacheinander angewendet. Das Kontextmenü bietet die folgenden Einträge: |
|                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                    | #### Bearbeiten                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                    | Erlaubt die Bearbeitung der Parameter einer Transformation in der Liste (Doppelklick hat den gleichen Effekt)                                                                                                                                                                                                                                                                                                 |
|                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                    | #### Löschen                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                    | Entfernt eine Transformation aus der Liste                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                    | #### Umwandlung hinzufügen                                                                                                                                                                                                                                                                                                                                                            |
|                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                    | Fügt der Liste eine Umwandlung hinzu                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                    | #### Nach oben/unten bewegen                                                                                                                                                                                                                                                                                                                                                         |
|                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                    | Erlaubt die Änderung der Reihenfolge der Transformationen in der Liste                                                                                                                                                                                                                                                                                                                                        |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+





</div>

### Select originals 

The list view shows the \'originals\', the features that are to be patterned. Clicking on any feature will add it to the list.

### Select transformations 

This list can be filled with a combination of the simple transformations [mirrored](PartDesign_Mirrored.md), [linear pattern](PartDesign_LinearPattern.md), [polar pattern](PartDesign_PolarPattern.md) and [scaled](PartDesign_Scaled.md). The transformations will be applied one after the other. The context menu offers the following entries:

#### Edit

Allows editing the parameters of a transformation in the list (double-clicking will have the same effect)

#### Delete

Removes a transformation from the list

#### Add transformation 

Adds a transformation to the list

#### Move Up/Down 

Allows changing the order of transformations in the list \|}

## Examples


<div class="mw-translate-fuzzy">

## Beispiele

![c\|800px](images/mt_example2.png ) 
*Die kleinste Aufpolsterung wurde zunächst dreimal in X Richtung gemustert und dann auf den Faktor zwei skaliert (die drei Vorkommen haben also den Skalierungsfaktor 1,0, 1,5 und 2,0). Dann wurde ein lineares Muster mit 8 Vorkommen angewendet.* ![c\|800px](images/mt_example3.png ) 
*Die Tasche wurde zunächst auf der YZ Ebene gespiegelt und dann mit zwei linearen Mustern gemustert, um ein rechteckiges Muster zu erhalten.* 


</div>





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign MultiTransform/de
