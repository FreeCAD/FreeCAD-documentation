---
- GuiCommand   */de
   Name   *PartDesign_PolarPattern
   Name/de   *PartDesign PolaresMuster
   MenuLocation   *PartDesign → Muster anwenden → Polares Muster
   Workbenches   *[PartDesign](PartDesign_Workbench/de.md)
---

# PartDesign PolarPattern/de

## Beschreibung

Das Werkzeug **PolaresMuster** erstellt auf Basis eines ausgewählten Formelements eine Reihe von Kopien, die um eine ausgewählte Achse herum angeordnet werden. Es können auch mehrere Formelemente angeordnet werden {{Version/de|0.17}}.

![](images/PartDesign_PolarPattern_example.png )

*Oben   * Eine schlitzförmige Tasche (B), die in einem Grundkörper (A, auch als Träger bezeichnet) eingebracht ist, wird für ein polares Muster verwendet. Das Ergebnis (C) ist rechts dargestellt.*

## Anwendung

#### Ein Muster erstellen 

1.  (Optional) Das Formelement (oder mehrere Formelemente {{Version/de|0.19}}) auswählen, das (die) angeordnet werden soll(en).

2.  Die Schaltfläche **[<img src=images/PartDesign_LinearPattern.svg style="width   *24px">  '''Polares Muster'''** drücken.
    -   Falls anfangs noch kein Element ausgewählt wurde, kann jetzt ein *einzelnes* Grundelement ausgewählt werden.

3.  Die **Achse** festtlegen, siehe [Optionen](#Optionen.md).

4.  Den **Winkel** zwischen dem letzten kopierten Vorkommen und dem originalen Formelement festlegen.

5.  Die Anzahl der **Vorkommen** festlegen.

6.  Wenn das Muster mehrere Formelemente enthält, kann ihre Reihenfolge wichtig sein, siehe Abbildung unten.

7.  
    **OK**drücken.

#### Formelemente ordnen 

![](images/PartDesign_feature-order.gif ) 
*Auswirkung der Formelementreihenfolge*

Die Reihenfolge kann geändert werden, indem man das Formelement in der Liste verschiebt, wobei das Ergebnis sofort als Vorschau zu sehen ist {{Version/de|0.19}}.

#### Formelemente hinzufügen 

###### v0.18

1.  Drücke **Element hinzufügen**, um ein Formelement hinzuzufügen, das gemustert werden soll. Das Formelement muss in der [3D-Ansicht](3D_view/de.md) sichtbar sein   *
    1.  Wechsle in den Baumansicht;
    2.  Wähle in der Baumansicht das hinzuzufügende Formelement aus und drücke die **Leertaste**, um es in der [3D-Ansicht](3D_view/de.md) sichtbar zu machen.
    3.  Wechsle zurück in die Aufgabenansicht;
    4.  Wähle das Formelement in der 3D-Ansicht; es wird der Liste hinzugefügt.
    5.  Wiederhole dies um weitere Formelemente hinzuzufügen.

###### v0.19

1.  Drücke **Element hinzufügen**, um ein Formelement hinzuzufügen, das einem Muster beigefügt werden soll.
2.  Wechsle zur Baumansicht.
3.  Wähle in der Baumansicht das hinzuzufügende Formelement.
4.  Wiederhole den Vorgang, um weitere Formelemente hinzuzufügen.

#### Formelemente entfernen 

-   Rechtsklicke auf das Formelement in der Liste und wähle *Entfernen*.

oder

###### v0.18 

1.  Drücke **Element entfernen** um ein Formelement aus der Liste zu entfernen. Das Formelement muss in der [3D-Ansicht](3D_view/de.md) sichtbar sein   *
    1.  Wechsle in die Baumansicht.
    2.  Wähle in der Baumansicht das zu entfernende Formelement aus und drücke die **Leertaste**, um es in der [3D-Ansicht](3D_view/de.md) sichtbar zu machen;
    3.  Wechsle zurück zum Aufgabenansicht.
    4.  Wähle das Formelement in der 3D-Ansicht; es sollte aus der Liste entfernt worden sein.
    5.  Wiederhole dies um weitere Formelemente zu entfernen.

###### v0.19 

1.  Drücke **Element entfernen**, um ein Formelement aus der Liste zu entfernen.
2.  Wechsle zur Baumansicht;
3.  Wähle in der Baumansicht das zu entfernende Formelement.
4.  Wiederhole den Vorgang, um andere Formelemente zu entfernen.

## Optionen

![](images/Polarpattern_parameters.png )

### Achse

Beim Erstellen eines Polaren Musters bietet der Dialog \"Parameter des polaren Musters\" verschiedene Möglichkeiten die Rotationsachse des Musters festzulegen.

#### Senkrecht zur Skizze 

Eine Achse, die eine Normale zur Skizze ist und im Ursprung der Skizze des verwendeten Formelementes beginnt, wird als Achse für das polare Muster genommen.
Die Ausrichtung des Musters kann umgekehrt werden, indem Sie auf \"Richtung umkehren\" klicken.

#### Horizontale Skizzenachse 

Benutzt die horizontale Achse der Skizze als Achse.

#### Vertikale Skizzenachse 

Benutzt die vertikale Achse der Skizze als Achse.

#### Individuelle Achse in der Skizze 

Wenn die Skizze für das zu wiederholende Muster Konstruktionslinien besitzt, werden diese Konstruktionslinien in dem Dropdown-MenüI als jeweils spezielle Achsen aufgelistet. Die erste Konstruktionslinie wird im Menü als *Konstruktionslinie 1* aufgelistet.

#### Basis (X/Y/Z) Achse 


<small>(v0.17)</small> 

Die Standardachsen des Koordinatensystems des Körpers (Body) stehen als Basis X, Y oder Z-Richtung zur Verfügung. 

#### Referenz auswählen\... 

Ermöglicht entweder eine Bezugslinie (DatumLine) oder eine Kante eines Objekts oder eine Linie einer Skizze als Achse zu verwenden.

### Winkel und Häufigkeiten 

Gibt den Winkel an, der vom Muster abgedeckt werden soll, sowie die Gesamtzahl der Musterformen (einschließlich des ursprünglichen Formelements). Zum Beispiel würden vier Vorkommen in einem Winkel von 180 Grad einen Abstand von 60 Grad zwischen Mustern ergeben. Es gibt eine Ausnahme   * Wenn der Winkel 360 Grad beträgt, sodass das erste und das letzte Vorkommen identisch sind, werden vier Vorkommen um 90 Grad voneinander getrennt.

## Begrenzungen

-   Siehe [Begrenzungen](PartDesign_LinearPattern/de#Begrenzungen.md) unter PartDesign Lineare Anordnung.





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign PolarPattern/de
