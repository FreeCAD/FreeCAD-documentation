---
- GuiCommand   */de
   Name   *PartDesign LinearPattern
   Name/de   *PartDesign LinearPattern
   MenuLocation   *Part Design → Muster anwenden → Lineares Muster
   Workbenches   *[PartDesign](PartDesign_Workbench/de.md)
---

# PartDesign LinearPattern/de

## Beschreibung

Das Werkzeug **LinearesMuster** erzeugt gleichmäßig verteilte Kopien eines Formelements entlang einer geraden Linie oder Kante.

![](images/PartDesign_LinearPattern_example.svg )

\'\'Oben   * Ein L-förmiger Block (B), der auf einer Grundplatte (A, auch als *Träger* bezeichnet) angebracht ist, wird für ein lineares Muster verwendet. Das Ergebnis (C) ist rechts dargestellt.\'\'

## Anwendung

Um ein Muster zu erstellen   *

1.  Das Formelement (oder mehrere Formelemente {{Version/de|0.19}}) auswählen, das (die) angeordnet werden soll(en).

2.  Die Schaltfläche **[<img src=images/PartDesign_LinearPattern.svg style="width   *24px">  '''Lineares Muster'''** drücken.

3.  Die **Richtung** definieren. Siehe [Optionen](#Options/de.md).

4.  Die **Länge** (Abstand) zwischen dem letzten kopierten Vorkommen und dem originalen Formelement definieren.

5.  Die Anzahl der **Vorkommen** festlegen.

6.  Wenn das Muster mehrere Formelemente enthält, kann ihre Reihenfolge wichtig sein, siehe z.B. das Bild im Abschnitt [PolaresMuster, Formelemente ordnen](PartDesign_PolarPattern/de#Anwendung.md). Die Reihenfolge kann geändert werden, indem man das Formelement in der Liste verschiebt, wobei das Ergebnis sofort als Vorschau zu sehen ist {{Version/de|0.19}}.

7.  
    **OK**drücken.

Zum Hinzufügen oder Entfernen von Formelementen zu einem bestehenden Muster   *

1.  
    **Element hinzufügen**drücken, um ein Formelement hinzuzufügen, das gemustert werden soll. Das Formelement muss in der [3D-Ansicht](3D_view/de.md) sichtbar sein   *

    1.  In den Modellbaum wechseln;

    2.  Im Baum das hinzuzufügende Formelement auswählen und die **Leertaste** drücken, um es in der [3D-Ansicht](3D_view/de.md) sichtbar zu machen;

    3.  Zum Aufgabenbereich zurück wechseln;

    4.  Das Formelement in der 3D-Ansicht auswählen; es wird der Liste hinzugefügt.

    5.  Diesen Vorgang wiederholen, um weitere Formelemente hinzuzufügen.

    6.  
        **Element entfernen**
        
        drücken, um ein Formelement aus der Liste zu entfernen, oder mit der rechten Maustaste auf das Formelement in der Liste klicken und **Entfernen** auswählen.

## Optionen

![Parameter des linearen Musters](images/Linearpattern_parameters_v017.png )

### Richtung

Bei der Erstellung eines LinearPattern-Objekts bietet der Dialog **Parameter des Linearen Musters** verschiedene Möglichkeiten, die Richtung des Musters auszuwählen.

#### Horizontale Skizzenachse 

Verwendet die horizontale Skizzenachse als Richtung.

#### Vertikale Skizzenachse 

Verwendet die vertikale Skizzenachse als Richtung.

#### Senkrecht zur Skizze 

Verwendet die Flächennormale der Skizze als Richtung.

#### Referenz auswählen\... 

Ermöglicht eine Bezugslinie (DatumLine), eine gerade Kante eines Objekts oder eine Linie aus einer Skizze als Richtung zu verwenden.

#### Angepasste Skizzenachse 

Wenn die Skizze für das zu wiederholende Muster Konstruktionslinien besitzt, werden diese Konstruktionslinien in dem Dropdown-MenüI als jeweils spezielle Achsen aufgelistet. Die erste Konstruktionslinie wird im Menü als *Konstruktionslinie 1* aufgelistet.

#### Basis (X/Y/Z) Achse 

Eine der Standardachsen (X, Y oder Z) des Körperursprungs als Richtung auswählen. 

## Einschränkungen

-   Musterformen dürfen einander nicht überlappen, außer im Sonderfall von nur zwei Vorkommen (Original plus eine Kopie)
-   Alle Musterformen, die die Auflage des Originals nicht überlappen, werden ausgeschlossen. Dies stellt sicher, dass ein PartDesign Formelement immer aus einem einzelnen, verbundenen Festkörper besteht.
-   Die PartDesign Muster sind noch nicht so optimiert wie ihre Draft Gegenstücke. Bei einer größeren Anzahl von Instanzen solltest du daher stattdessen die Verwendung von [Draft Anordnung](Draft_OrthoArray/de.md) in Kombination mit einer booleschen Part Operation in Betracht ziehen. Dies kann größere Änderungen an deinem Modell beinhalten, wenn du PartDesign verlässt, was bedeutet, dass du nicht einfach mit weiteren PartDesign Formelementen im selben Körper fortfahren kannst. Ein Beispiel wird in diesem [Forum Thema](https   *//forum.freecadweb.org/viewtopic.php?f=3&t=55192) gezeigt.
-   Eine lineare Anordnung kann nicht direkt auf andere Anordnungen angewendet werden, egal ob sie linear, polar oder eine Spiegelung sind. Dafür benutzt man die Funktion [PartDesign Mehrfach-Transformation erstellen](PartDesign_MultiTransform/de.md).
-   Für weitere Einschränkungen siehe die Funktion [PartDesign Spiegeln](PartDesign_Mirrored/de.md).





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign LinearPattern/de
