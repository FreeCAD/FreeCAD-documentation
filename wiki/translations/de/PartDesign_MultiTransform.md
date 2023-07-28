---
- GuiCommand:/de
   Name:PartDesign MultiTransform
   Name/de:PartDesign MultiTransform
   MenuLocation:Part Design → Muster anwenden → Mehrfach-Transformation erstellen
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   SeeAlso:[PartDesign Spiegeln](PartDesign_Mirrored/de.md), [PartDesign LinearesMuster](PartDesign_LinearPattern/de.md), [PartDesign PolaresMuster](PartDesign_PolarPattern/de.md), [PartDesign Skalieren](PartDesign_Scaled/de.md)
---

# PartDesign MultiTransform/de



## Beschreibung

Das Werkzeug <img alt="" src=images/PartDesign_MultiTransform.svg  style="width:24px;"> **PartDesign MehrfachTransformation** erstellt ein Muster aus einem oder mehreren Formelementen. Das Muster kann mehrere Transformationen enthalten, wobei jede folgende Transformation auf das Ergebnis der vorherigen Transformation angewendet wird.

Folgende Transformationen stehen zur Verfügung: <img alt="" src=images/PartDesign_Mirrored.svg  style="width:16px;"> [Spiegeln](PartDesign_Mirrored/de.md), <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:16px;"> [LinearesMuster](PartDesign_LinearPattern/de.md), <img alt="" src=images/PartDesign_PolarPattern.svg  style="width:16px;"> [PolaresMuster](PartDesign_PolarPattern/de.md) und <img alt="" src=images/PartDesign_Scaled.svg  style="width:16px;"> [Skaliert](PartDesign_Scaled/de.md). Die ersten drei stehen auch als separate Werkzeuge zur Verfügung.

<img alt="" src=images/multitransform_example.png  style="width:600px;"> 
*Ein Lochmuster, das aus einem einzelnen Loch erstellt wurde, wobei zuerst ein lineares Muster mit 2 Vorkommen und danach ein polares Muster mit 8 Vorkommen angewendet wurde.*



## Anwendung



### Erstellen

1.  Bei Bedarf den korrekten Körper [aktivieren](PartDesign_Body#Active_status/de.md).
2.  Wahlweise können ein oder mehrere Elemente in der [Baumansicht](Tree_view/de.md) oder der [3D-Ansicht](3D_view/de.md) ausgewählt werden.
3.  Es gibt mehrere Möglichkeiten das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/PartDesign_MultiTransform.svg" width=16px> [Mehrfach-Transformation erstellen](PartDesign_MultiTransform/de.md)** drücken.
    -   Den Menüeintrag **Part Design → Muster anwenden → <img src="images/PartDesign_MultiTransform.svg" width=16px> Mehrfach-Transformation erstellen** auswählen.
4.  Falls kein Körper aktiviert ist und sich zwei oder mehr Körper im Dokument befinden, öffnet sich der Dialog **Aktiver Körper erforderlich** mit der Aufforderung einen zu aktivieren. Wenn nur ein einziger Körper vorhanden ist, wird dieser automatisch aktiviert.
5.  Wenn kein Formelement ausgewählt wurde, öffnet sich der [Aufgabenbereich](Task_panel/de.md) **Element auswählen**: Ein oder mehrere (**Ctrl**-Taste gedrückt halten) aus der Liste auswählen und die Schaltfläche **OK** drücken.
6.  Der [Aufgabenbereich](Task_panel/de.md) **Parameter der Mehrfach-Transformation** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
7.  Zum Fertigstellen die Schaltfläche **OK** am oberen Rand drücken.



### Bearbeiten

1.  Eine der folgenden Möglichkeiten startet die Bearbeitung:
    -   Das MultiTransform-Objekt in der [Baumansicht](Tree_view/de.md) doppelt anklicken.
    -   Das MultiTransform-Objekt in der [Baumansicht](Tree_view/de.md) mit der rechten Maustaste anklicken und **MultiTransform bearbeiten** aus dem Kontextmenü auswählen.
2.  Der [Aufgabenbereich](Task_panel/de.md) **Parameter der Mehrfach-Transformation** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
3.  Zum Fertigstellen die Schaltfläche **OK** am oberen Rand drücken.



### Kombinieren vorhandener Transformationen 

Es ist möglich ein MultiTransform-Objekt von vorhandenen Transformationen wie [Spiegeln](PartDesign_Mirrored/de.md), [Lineares Muster](PartDesign_LinearPattern/de.md) und [Polares Muster](PartDesign_PolarPattern/de.md) zu erstellen.

1.  Die {{PropertyData/de|Originals}} der bestehenden Transformationen überprüfen, ob sie auf dieselben Formelemente angewendet werden.
2.  Diese Formelemente in der [Baumansicht](Tree_view/de.md) auswählen.
3.  Es gibt mehrere Möglichkeiten das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/PartDesign_MultiTransform.svg" width=16px> [Mehrfach-Transformation erstellen](PartDesign_MultiTransform/de.md)** drücken.
    -   Den Menüeintrag **Part Design → Muster anwenden → <img src="images/PartDesign_MultiTransform.svg" width=16px> Mehrfach-Transformation erstellen** auswählen.
4.  Der [Aufgabenbereich](Task_panel/de.md) **Parameter der Mehrfach-Transformation** wird geöffnet.
5.  Die Schaltfläche **OK** am oberen Rand drücken.
6.  Die {{PropertyData/de|Tranformations}} des erstellten MultiTransform-Objekts bearbeiten:
    1.  Auf das Feld klicken.
    2.  Die Schaltfläche **...**, die dann erscheint, anklicken.
    3.  Der Dialog **Link** wird geöffnet.
    4.  Mit gedrückter **Ctrl**-Taste werden die bestehenden Transformationen ausgewählt.
    5.  Die Schaltfläche **OK** drücken.
7.  Wahlweise das MultiTransform-Objekt [bearbeiten](#Bearbeiten.md), siehe oben.



## Optionen

-   Formelemente hinzufügen:
    1.  Die Schaltfläche **Element hinzufügen** drücken.
    2.  Ein Formelement in der [Baumansicht](Tree_view/de.md) oder in der [3D-Ansicht](3D_view/de.md) auswählen.
    3.  Wiederholen, um weitere Formelemente hinzuzufügen.
-   Formelemente entfernen:
    1.  Die Schaltfläche **Element entfernen** drücken.
    2.  Eine der folgenden Möglichkeiten wählen:
        -   Ein Formelement in der [Baumansicht](Tree_view/de.md) oder in der [3D-Ansicht](3D_view/de.md) auswählen.
        -   Ein Formelement in der oberen Liste auswählen und die **Del**-Taste drücken.
        -   Mit der rechten Maustaste ein Formelement in der oberen Liste anklicken und **Entfernen** aus dem Kontextmenü auswählen.
    3.  Wiederholen, um weitere Formelemente zu entfernen.
-   Wenn ein Muster mehrere Formelemente enthält, kann deren Reihenfolge wichtig sein. Siehe [PartDesign PolaresMuster](PartDesign_PolarPattern/de#Formelemente_ordnen.md).
-   Transformationen hinzufügen:
    1.  Wenn schon Transformationen vorhanden sind: Die Transformation auswählen, hinter der die neue Transformation eingefügt werden soll.
    2.  Mit der rechten Maustaste in die Liste **Transformationen** klicken.
    3.  Eine der folgenden Möglichkeiten des Kontextmenüs auswählen:
        -   
            **Spiegelung hinzufügen**
            
            . Siehe [PartDesign Mirrored](PartDesign_Mirrored.md).

        -   
            **Lineares Muster hinzufügen**
            
            . Siehe [PartDesign LinearesMuster](PartDesign_LinearPattern/de.md).

        -   
            **Polares Muster hinzufügen**
            
            Siehe [PartDesign PolaresMuster](PartDesign_PolarPattern/de.md).

        -   
            **Skalierte Transformation hinzufügen**
            
            . Siehe [PartDesign Skalieren](PartDesign_Scaled/de.md).
    4.  Die ausgewählte Transformation wird zur Liste hinzugefügt und die Einstellungen der Transformationen werden unterhalb der Liste angezeigt.
    5.  Die Einstellungen nach Bedarf anpassen.
    6.  Die **OK**-Leiste am unteren Rand drücken.
    7.  Wiederholen, um weitere Transformationen hinzuzufügen.
-   Transformationen bearbeiten:
    1.  Mit der rechten Maustaste in die Liste **Transformationen** klicken.

    2.  
        **Bearbeiten**
        
        aus dem Kontextmenü auswählen.

    3.  Die Einstellungen nach Bedarf anpassen.

    4.  Die **OK**-Leiste am unteren Rand drücken.
-   Die Reihenfolge der Transformationen ändern:
    1.  Mit der rechten Maustaste in die Liste **Transformationen** klicken.

    2.  
        **Nach oben verschieben**
        
        or **Nach unten verschieben** aus dem Kontextmenü auswählen.
-   Wenn die Checkbox **Ansicht aktualisieren** aktiviert ist, erfolgt die aktualisierung in Echtzeit.



## Einschränkungen

Siehe [PartDesign PolaresMuster](PartDesign_PolarPattern/de#Einschränkungen.md).



## Beispiel

Dieses Werkzeug kann zur Erstellung eines vollparametrischen Teils, symetrisch über zwei Achsen aus einer Skizze heraus, verwendet werden.

Das kann eine 150x100x10mm große Montageplatte für einen Motor mit symetrisch angeordneten Bohrungen sein.

<img alt="" src=images/PartDesign_MultiTransform_Example2.png  style="width:400px;">

1.  Erzeuge einen <img alt="" src=images/PartDesign_Body.svg  style="width:16px;"> [Körper](PartDesign_Body.md) und füge eine <img alt="" src=images/PartDesign_NewSketch.svg  style="width:16px;"> [Skizze](PartDesign_NewSketch.md) of einer seiner Basisebenen ein.
2.  Erzeuge in der Skizze die Geometrie für einen Quadranten des Teiles (d.h. den oberen rechten Quadranten).
    -   Beachte, dass die Einschränkungen nur ein Viertel des Teiles überdecken dürfen, d.h. statt der gesamten Abmessung {{value|150mm}} gebe {{value|150/2mm}} oder {{value|75mm}} ein.
    -   Stelle durch Anfügen von Linien entlang der vertikalen und horizontalen Achsen sicher, dass die Skizze geschlossen ist.
3.  Polstere den Teil mit <img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> [Aufpolsterung](PartDesign_Pad.md) auf.
4.  Wähle <img alt="" src=images/PartDesign_MultiTransform.svg  style="width:16px;"> **PartDesign Mehrfachtransformation**.
5.  Das Dialogfenster öffnet.
6.  Die letzte Feature des Körpers ist bereits ausgewählt. Da wir diese Feature spiegeln wollen, können wir die **Element hinzufügen** und die **Element entfernen** Schaltflächen ignorieren.
7.  Rechts-Klicke in das **Transformationen** Feld und wähle **Spiegelung hinzufügen** aus dem Kontextmenü.
8.  Als **Ebene** wähle **Vertikale Skizzenachse**.
9.  Wenn die **Ansicht aktualisieren** Checkbox ausgewählt ist, dann kann man jetzt den an einer Achse gespiegelten Teil sehen.
10. Wähle wieder **Spiegelung hinzufügen** aus dem Kontextmenü des **Transformationen** Feldes.
11. Wähle jetzt als **Ebene** die **Horizontale Skizzenachse**.
12. Wähle die **OK** Schaltfläche um zu beenden.
13. Um die Kanten entlang der Symmetrieachsen zu entfernen, setze die **Refine** Eigenschaft der neuen Feature im [Property Editor](Property_editor.md) auf {{Value|wahr}}.

Um zu gewährleisten, dass das Teil vollparametrisch ist, öffnet man die Ursprungsskizze mit dem Viertelteil und ändert ein Maß, z.B. den Bohrungsdurchmesser. Nach dem Schließen der Skizze werden die drei anderen Bohrungen entsprechend geändert sein. Das funktioniert für alle anderen Maße gleichermaßen. Eine Skizze die ein vollständiges Teil durch eine einfache Formung ohne Spiegelung erstellt, wäre sehr viel komplizierter und alle möglichen Änderungen wäre sehr viel komplizierter.





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign MultiTransform/de
