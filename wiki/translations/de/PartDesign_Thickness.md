---
- GuiCommand:
   Name:PartDesign Thickness
   Name/de:PartDesign Dicke
   MenuLocation:Part Design - Modifikationen - Dicke
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   Version:0.17
   SeeAlso:[Part Dicke](Part_Thickness/de.md)
---

# PartDesign Thickness/de

## Beschreibung

Das Werkzeug <img alt="" src=images/PartDesign_Thickness.svg  style="width:24px;"> **PartDesign Dicke** wandelt einen Volumenkörper in ein hohles Objekt (Schalenobjekt) mit mindestens einer offenen Fläche, und gibt allen verbleibenden Flächen eine konstante Wandstärke. Es fügt dem Dokument ein **Thickness**-Objekt und den dazugehörigen Repräsentanten in der [Baumansicht](Tree_view/de.md) hinzu.

<img alt="" src=images/PartDesign_Thickness_example.svg  style="width:600px;"> 
*Ausgangsvolumenkörper (A) →  Volumenkörper mit der ausgewählten Fläche, die geöffnet werden soll (B) →  Das resultierende hohle Objekt (C)*

## Anwendung

### Dicke hinzufügen 

1.  Optional [aktiviert](PartDesign_Body/de#Aktiver_Status.md) man den Körper, der ausgehöhlt werden soll.
2.  Eine oder mehrere Flächen des Körpers auswählen.
3.  Es gibt mehrere Möglichkeiten das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/PartDesign_Thickness.svg" width=16px> [Dicke](PartDesign_Thickness/de.md)** drücken.
    -   Den Menüeintrag **Part Design → Modifikationen → <img src="images/PartDesign_Thickness.svg" width=16px> Dicke** auswählen.
4.  Wenn zwei oder mehr Körper vorhanden sind und kein Körper aktiviert ist, wird der der Dialog **Active Body Required** geöffnet mit der Aufforderung einen zu aktivieren. Ist nur ein einziger Körper vorhanden, wird dieser automatisch aktiviert.
5.  Der [Aufgabenbereich](Task_panel/de.md) **Parameter der Wandstärke** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
6.  Zum Fertigstellen die **OK**-Schaltfläche drücken.

:   *Nicht vergessen*:
    -   Da das Werkzeug immer mindestens eine Fläche erfordert, kann die letzte vorhandene Fläche nicht aus der Liste entfernt werden.

### Dicke bearbeiten 

1.  Eine der folgenden Möglichkeiten startet die Bearbeitung:
    -   Das Thickness-Objekt in der [Baumansicht](Tree_view/de.md) doppelt anklicken.
    -   Das Thickness-Objekt in der [Baumansicht](Tree_view/de.md) mit der rechten Maustaste anklicken und **Thickness bearbeiten** aus dem Kontextmenü auswählen.
2.  Der [Aufgabenbereich](Task_panel/de.md) **Parameter der Wandstärke** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
3.  Zum Fertigstellen die **OK**-Schaltfläche drücken.

## Optionen

-    **Fläche hinzufügen**: Fügt Flächen hinzu, durch Drücken der Schaltfläche **Fläche hinzufügen** und die Auswahl weiterer Flächen.

-    **Fläche entfernen**: Möglichkeiten eine Fläche aus der Auswahl zu entfernen:

    -   Eine oder mehrere Flächen in der Liste auswählen und die **Del**-Taste drücken oder mit der rechte Maustaste in die Liste klicken und Entfernen aus dem Kontextmenü auswählen.
    -   Die Schaltfläche **Fläche entfernen** drücken. Alle zuvor ausgewählten Flächen werden violett hervorgehoben. Jede zu entfernende Fläche auswählen.

-    **Dicke**: Die Wandstärke verändern, indem man einen Wert eingibt oder die Pfeiltasten anklickt.

-    **Modus**:

    -   
        **Oberfläche**
        
        : Nur diese Möglichkeit wird verwendet.

    -   
        **Rohr**
        
        : Nicht implementiert. Siehe [diesen Forumsbeitrag (engl.)](https://forum.freecadweb.org/viewtopic.php?p=484495#p484495).

    -   
        **Recto Verso**
        
        : Nicht implementiert. Siehe [derselbe](https://forum.freecadweb.org/viewtopic.php?p=484495#p484495).

-    **Verbindungstyp**:

    -   
        **Kreisbogen**
        
        : Wenn nicht tangentiale Flächen versetzt werden und sich die neuen Flächen nicht überschneiden, werden sie mit einer Rundung verbunden, deren Radius der festgelegten Wandstärke entspricht.

    -   
        **Schnitt**
        
        : Wenn nicht tangentiale Flächen versetzt werden und sich die neuen Flächen nicht überschneiden, werden sie bis zu ihrer virtuellen Schnittlinie verlängert.

-    **Schnitt**: Wenn aktiviert, werden bei bestimmten Modellen Selbstdurchdringungen verhindert. Diese Möglichkeit wird nicht empfohlen, da sie auf einer unvollständigen [OpenCASCADE-Methode](https://dev.opencascade.org/doc/refman/html/class_b_rep_offset_a_p_i___make_thick_solid.html#af78f35025a31e2ce8bd96c82fb33a981) basiert.

-    **Dicke nach innen auftragen**: Wenn aktiviert, werden Flächen nach innen versetzt.

## Hinweise

-   Wenn die Wandstärke nach innen aufgetragen wird, muss der Wert kleiner sein als die kleinste Höhe des Körpers.
-   Das Wekzeug kann bei komplexen Formen versagen. [Rohr](PartDesign_AdditivePipe/de.md) oder [Ausformung](PartDesign_AdditiveLoft.md) können geeigneter sein, um komplexe Formen zu erstellen.
-   Bekannte Fehler:
    -   BRep_API: command not done (Befehl nicht ausgeführt).
    -   BRep_Tool: no parameter on edge (Kein Parameter auf der Kante).
    -   Silently fails (Stilles Versagen).

## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein PartDesign-Thickness-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:

### Daten


{{Properties_Title/de|Basis}}

-    **Base|LinkSub**: Sub-link zu der Liste des übergeordneten Formelements, die die ausgewählten Kanten und Flächen enthält.

-    **Support Transform|Bool**: \"Beinhaltet das ursprüngliche Formelement zur Verwendung in Muster-Objekten. Wenn deaktiviert, wird nur der angepasste (bearbeitete) Anteil der Form zum Erstellen von Mustern verwendet. Standardwert: `False`.

-    **Add Sub Shape|PartShape|hidden**
    

-    **Base Feature|Link|hidden**: Verknüpfung mit dem übergeordneten Formelement.

-    **_ Body|LinkHidden|hidden**: Verknüpfung mit dem übergeordneten Körper.


{{Properties_Title/de|Part Design}}

-    {{PropertyData/de|Refine|Bool}}: \"Form aufbereiten (überflüssige Kanten entfernen) nach einer Hinzufügen- oder Entfernen-Operation. Der voreingestellte Wert wird durch die Einstellung **Modell nach skizzenbasierter Operation automatisch aufbereiten** bestimmt. Siehe [PartDesign Einstellungen](PartDesign_Preferences/de#Allgemein.md).


{{Properties_Title/de|Thickness}}

-    **Value|Length**: \"Wert der Wandstärke (Dicke)\". Standardwert: {{value|1 mm}}.

-    **Mode|Enumeration**: \"Modus\". {{value|Skin}} (Standard), {{value|Pipe}} oder {{Value|Recto verso}}. Nur {{value|Skin}} ist implementiert.

-    **Join|Enumeration**: \"Verbindungstyp\". {{value|Arc}} (Standard) oder {{Value|Intersection}}.

-    **Reversed|Bool**: \"Wandstärke in Richtung des Körperinneren auftragen\". Standardwert: `False`.

-    **Intersection|Bool**: \"Bearbeitung von Überschneidungen aktivieren\". Standardwert: `False`.





{{PartDesign Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Thickness/de
