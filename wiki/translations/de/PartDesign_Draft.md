---
- GuiCommand:
   Name:PartDesign Draft
   Name/de:PartDesign Formschräge
   MenuLocation:Part Design → Modifikationen → Formschräge
   Workbenches:[Part Design](PartDesign_Workbench/de.md)
   Shortcut:-
   SeeAlso:Keine
---

# PartDesign Draft/de

## Beschreibung

Das Werkzeug <img alt="" src=images/PartDesign_Draft.svg  style="width:24px;"> **PartDesign Formschräge** versieht die ausgewähleten Flächen eines Objekts mit einer (Entform-)Schräge. Es fügt dem Dokument ein **Draft**-Objekt und den dazugehörigen Repräsentanten in der [Baumansicht](Tree_view/de.md) hinzu.

   --
  ![Eine oder mehrere Flächen des Objekts auswählen, bevor das Werkzeug gestartet wird. Hier wurden 2 Flächen ausgewählt.](images/PartDesign_Draft-01.png ) ![Anzeige der Parameter der Fomschräge im Aufgabenbereich.](images/PartDesign_Draft-02.png ) ![2 Flächen wurden hinzugefügt und mit 10 Grad Schräge versehen. Die Bodenebene ist maßlich unverändert geblieben, während die Deckelebene verkleinert wurde.](images/PartDesign_Draft-03.png ) ![Die neutrale Ebenen wurde nach oben versetzt. Jetzt bleibt die Deckelebene maßlich unverändert, während die Bodenebene vergrößert wurde.](images/PartDesign_Draft-04.png ) ![Die untere rechte Kante wurde als Zugrichtung (Entformrichtung) festgelegt, daraus ergibt sich, dass die Schräge nach links gezogen wird.](images/PartDesign_Draft-05.png ) ![Die Aktivierung der Checkbox Entformungsrichtung umkehren sorgt dafür, dass die Schräge nach innen statt nach außen verläuft.](images/PartDesign_Draft-06.png )   
   --





## Anwendung

### Eine Formschräge hinzufügen 

1.  Falls nötig, wird der abzuschrägende Körper [aktiviert](PartDesign_Body/de#Activer_Status.md).
2.  Eine oder mehrere Flächen des Körpers auswählen.
3.  Es gibt mehrere Möglichkeiten das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/PartDesign_Draft.svg" width=16px> [Formschräge](PartDesign_Draft/de.md)** drücken.
    -   Den Menüeintrag **Part Design → Modifikationen → <img src="images/PartDesign_Draft.svg" width=16px> Formschräge** auswählen.
4.  Wenn kein Körper aktiv ist und sich zwei oder mehr Körper im Dokument befinden, offnet sich der Dialog **Active Body Required** und fordert zur Aktivierung eines Körpers auf. Ist nur ein einziger Körper vorhanden, wird er automatisch ausgewählt.
5.  Der [Aufgabenbereich](Task_panel/de.md) **Parameter der Formschräge** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
6.  Zum Fertigstellen die **OK**-Schaltfläche drücken.

:   *Nicht vergessen*:
    -   Da das Werkzeug immer mindestens eine Fläche erfordert, kann die letzte vorhandene Fläche nicht aus der Liste entfernt werden.

### Eine Formschräge bearbeiten 

1.  Eine der folgenden Möglichkeiten startet die Bearbeitung:
    -   Das Draft-Objekt in der [Baumansicht](Tree_view/de.md) doppelt anklicken.
    -   Das Draft-Objekt in der [Baumansicht](Tree_view/de.md) mit der rechten Maustaste anklicken und **Draft bearbeiten** aus dem Kontextmenü auswählen.
2.  Der [Aufgabenbereich](Task_panel/de.md) **Parameter der Formschräge** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
3.  Zum Fertigstellen die **OK**-Schaltfläche drücken.

## Optionen

-    **Fläche hinzufügen**: Flächen werden zur Auswahl hinzugefügt, indem man die Schaltfläche **Fläche hinzufügen** drückt und weitere Flächen auswählt.

-    **Fläche entfernen**: Möglichkeiten eine Fläche aus der Auswahl zu entfernen:

    -   Eine oder mehrere Flächen in der Liste auswählen und die **Del**-Taste drücken oder mit der rechte Maustaste in die Liste klicken und **Entfernen** aus dem Kontextmenü auswählen.
    -   Die Schaltfläche **Fläche entfernen** drücken. Alle zuvor ausgewählten Flächen werden violett hervorgehoben. Jede zu entfernende Fläche auswählen.

-    **Formschrägenwinkel**: Den Winkel der Schräge verändern, indem man einen Wert eingibt oder die Pfeiltasten anklickt.

-    **Neutrale Ebene**: Die neutrale Ebene angeben, indem man die Schaltfläche **Neutrale Ebene** drückt und die Fläche auswählt, die sich maßlicht nicht verändern soll.

-    **Zugrichtung**: Die Zugrichtung festlegen, indem man die Schaltfläche **Zugrichtung** drückt und dann eine Kante auswählt. Die Zugrichtung hat nur dann eine Wirkung, wenn eine neutrale Ebenen angegeben wurde. Die Ergebnisse können unvorhersehbar sein.

-    **Zugrichtung umkehren**: Umkehren der Zugrichtung durch aktivieren der Checkbox **|Entformungsrichtung umkehren**. Dies schaltet den Winkel der Schräge von positiv zu negativ um.

## Hinweise

-   Das Werkzeug Formschräge arbeitet nur mit Flächen, die nicht tangential mit anderen Flächen verbunden sind. (Hier sollte das englische Original präzisiert werden\...) A common mistake is to attempt to apply draft to a face that already has a fillet applied to it. To solve this, remove the fillet, apply the draft as needed, then re-apply the fillet.

## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein PartDesign-Draft-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:

### Daten


{{Properties_Title/de|Basis}}

-    {{PropertyData/de|Angle|Angle}}: Kann nicht negativ sein. Standardwert: {{value|1,5 °}}.

-    {{PropertyData/de|Reversed|Bool}}: Standardwert: `False`.

-    {{PropertyData/de|Base|LinkSub}}: Sub-link to the parent feature\'s list of selected edges and faces.

-    {{PropertyData/de|Support Transform|Bool}}: \"Include the base additive/subtractive shape when used in pattern features. If disabled, only the dressed part of the shape is used for patterning\". Standardwert: `False`.

-    {{PropertyData/de|Add Sub Shape|PartShape|hidden}}
    

-    {{PropertyData/de|Base Feature|Link|hidden}}: Link to the parent feature.

-    {{PropertyData/de|_ Body|LinkHidden|hidden}}: Link to the parent body.


{{Properties_Title/de|Draft}}

-    {{PropertyData/de|Neutral Plane|LinkSub}}: Sub-link to the parent feature\'s list containing the neutral plane.

-    {{PropertyData/de|Pull Direction|LinkSub}}
    


{{Properties_Title/de|Part Design}}

-    {{PropertyData/de|Refine|Bool}}: \"Form aufbereiten (überflüssige Kanten entfernen) nach einer Hinzufügen- oder Entfernen-Operation. Der voreingestellte Wert wird durch die Einstellung **Modell nach skizzenbasierter Operation automatisch aufbereiten** bestimmt. Siehe [PartDesign Einstellungen](PartDesign_Preferences/de#Allgemein.md).





{{PartDesign Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Draft/de
