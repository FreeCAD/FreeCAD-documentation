---
- GuiCommand:
   Name:PartDesign Groove
   Name/de:PartDesign Nut
   MenuLocation:Part Design → Objekte abziehen → Nut
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   SeeAlso:[PartDesign Drehkörper](PartDesign_Revolution/de.md)
---

# PartDesign Groove/de

## Beschreibung

Das Werkzeug **Nut** dreht eine ausgewählte Skizze oder ein Profil um eine gegebene Achse und entfernt Material aus dem aktiven Körper.

![](images/PartDesign_Groove_example.svg )



*Oben: Skizze (A) ist um die Achse (B) gedreht; die resultierende Nut auf dem Volumenkörper (C) ist rechts dargestellt.*

## Anwendung

1.  Wähle die Skizze, die gedreht werden soll.

    :    v0.17 und höher  Alternativ kann auch eine Fläche auf dem vorhandenen Festkörper verwendet werden.
    :    v0.16 und niedriger  Die Skizze muss auf die Planfläche eines bestehenden Festkörpers oder Bauteilkonstruktionsmerkmals abgebildet werden, sonst erscheint eine Fehlermeldung.{{VersionMinus|0.16}}
2.  Drücke **<img src="images/_PartDesign_Groove.svg" width=24px> '''Nut'''** Schaltfläche.
3.  Lege die Nut-Parameter fest (siehe nächster Abschnitt).
4.  Drücke **OK**.

## Optionen

Beim Erstellen einer Nut bietet der **Nutparameter** Dialog mehrere Parameter, die festlegen, wie die Skizze gedreht werden soll.

+++
| ![](images/partdesign_groove_parameters.png ) | ### Achse                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                          | Diese Option legt die Achse fest, um die die Skizze gedreht werden soll.                                                                                                                                                                                                                                                                                                                 |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                          | -   **Vertikale Skizzenachse**: wählt die vertikale Skizzenachse aus.                                                                                                                                                                                                                                                                                                                    |
|                                                                          | -   **Horizontale Skizzenachse**: wählt die horizontale Skizzenachse aus.                                                                                                                                                                                                                                                                                                                |
|                                                                          | -   **Skizzenachse**:  v0.16 und darunter                                                                                                                                                                                                                                                                         |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                          | wählt eine Konstruktionslinie aus, die in der von Nut verwendeten Skizze enthalten ist. Die erste Konstruktionslinie, die in der Skizze erstellt wurde, trägt die Bezeichnung *Skizzenachse 0*. Die Aufklappliste enthält eine benutzerdefinierte Skizzenachse für jede Konstruktionslinie.                                                                                              |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                          | -   **Konstruktionslinie**: v0.17 und höher wählt eine Konstruktionslinie aus, die in der von Nut verwendeten Skizze enthalten ist. Die Aufklappliste wird einen Eintrag für jede Konstruktionslinie enthalten. Die erste in der Skizze erstellte Konstruktionslinie trägt die Bezeichnung *Konstruktionslinie 1*. |
|                                                                          | -   Basis (X/Y/Z) Achse\'\'\'\': v0.17 und höher wählt die X, Y oder Z Achse des Körperursprungs;                                                                                                                                                                                                                  |
|                                                                          | -   **Referenz auswählen\...**: v0.17 und höher ermöglicht die Auswahl in der 3D Ansicht einer Kante auf dem Körper oder einer [Bezugslinie](PartDesign_Line/de.md).                                                                                                                                       |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                          | <small>(v0.17)</small>                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                          | ### Winkel                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                          | Dies steuert den Winkel, über den die Nut zu bilden ist, z. 360 ° wäre eine vollständige, zusammenhängende Revolution. Es ist nicht möglich, negative Winkel anzugeben (verwende stattdessen die Option **Umgekehrt**) oder Winkel größer als 360 °.                                                                                                                                     |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                          | ### Symmetrisch zur Ebene                                                                                                                                                                                                                                                                                                                                        |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                          | Wenn diese Option aktiviert ist, wird die Nut um die Hälfte des angegebenen Winkels in beide Richtungen von der Skizzierebene aus verlängert.                                                                                                                                                                                                                                            |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                          | ### Umgekehrt                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                          | Wenn diese Option aktiviert ist, wird die Drehrichtung umgekehrt von standardmäßig im Uhrzeigersinn auf gegen den Uhrzeigersinn.                                                                                                                                                                                                                                                         |
+++

## Eigenschaften

Nachfolgend findest Du Eigenschaften, die nach der Erstellung des Merkmals definiert werden können. Die Dateneigenschaften \'Basis\'\' und \' Achse\' sind nicht editierbar.

-    **Winkel**: Drehwinkel. Siehe [Winkel](#Angle.md) .

-    **Kennzeichen**: Beschriftung des Arbeitsgangs, kann bei Bedarf geändert werden.

-    **Mittelebene**: wahr oder falsch. Siehe [Symmetrisch zur Ebene](#Symmetric_to_plane/de.md).

-    **Umgekehrt**: wahr oder falsch. Siehe [Umgekehrt](#Reversed/de.md).

-    **Verfeinern**: v0.17 und höher wahr oder falsc. Wenn auf *true* gesetzt wird die Form von überflüssigen Kanten bereingt . Siehe [Part FormVerfeinern](Part_RefineShape/de.md) für mehr Details.


<small>(v0.17)</small> 





{{PartDesign Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Groove/de
