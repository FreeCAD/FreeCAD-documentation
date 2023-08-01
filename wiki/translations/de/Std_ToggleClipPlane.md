---
- GuiCommand:/de
   Name:Std ToggleClipPlane
   Name/de:Std Schnittebene
   MenuLocation:Ansicht → Schnittebene
   Workbenches:Alle
   SeeAlso:[Part Schnittansicht](Part_SectionCut/de.md)
---

# Std ToggleClipPlane/de



## Beschreibung

Der Befehl **Std Schnittebene** blendet Objekte und Teile von Objekten aus, die sich auf jeweils einer Seite von bis zu drei virtuellen Ebenen in der [3D-Ansicht](3D_view/de.md) befinden.

![](images/Std_ToggleClipPlane_example.png ) 
*Ein beschnittenes, hohles Objekt*

![](images/Std_ToggleClipPlane_Dialog.png ) 
*Der Dialogbereich Clipping*



## Anwendung

1.  Menüeintrag **Ansicht → <img src="images/Std_ToggleClipPlane.svg" width=16px> Schnittebene** auswählen.
2.  Im Dialogbereich Clipping hat man folgende Möglichkeiten:
    -   Eine oder mehrere der Checkboxen {{CheckBox|TRUE|Abschneiden in X}} bis {{CheckBox|TRUE| Abschneiden in Z}} aktivieren.
        -   Bei Bedarf die Abstandswerte ändern.
        -   Bei Bedarf die jeweilige Schaltfläche **Flip** drücken, um die Seite zu Wählen, auf der die Objekte ausgeblendet werden.
    -   Checkbox {{CheckBox|TRUE|Abschneiden in benutzerdefinierterRichtung}} aktivieren.
        -   Bei Bedarf die Abstandswert ändern.
        -   Nun hat man diese Möglichkeiten:
            -   Schaltfläche **Ansicht** drücken, um die Richtung der aktuellen Ansicht zu verwenden.
            -   Checkbox {{CheckBox|TRUE|An Blickrichtung anpassen}} aktivieren, damit sich die Richtung dynamisch an Änderungen der Ansicht anpassen.
            -   Angabe einer Richtung durch Eingabe der X-, Y- und Z-Koordinaten eines Normalenvektors.
3.  Bei Bedarf ändert man die Ansicht zum Überprüfen des Modells.
4.  Die Schaltfläche **Schließen** drücken, um den Aufgabenbereich zu schließen und den Befehl zu beenden.



## Hinweise

-   Zur deutlichen Unterscheidung des Inneren der teilweise geschnittenen Objekte kann deren {{PropertyView/de|Lighting}} auf \'One side\' geändert werden. Die Farbe der Innenseite ihrer Flächen hängt dann von den Backlight-Einstellungen ab: **Bearbeiten → Einstellungen... → Display → 3D View → Backlight color - Intensity**. Siehe [Voreinstellungseditor](Preferences_Editor/de#3D-Ansicht.md).





{{Std_Base_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std ToggleClipPlane/de
