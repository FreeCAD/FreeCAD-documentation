---
 GuiCommand:
   Name: Ship LoadExample
   Name/de: Ship BeispielLaden
   MenuLocation: Ship design , Lade ein Beispiel einer Schiffsgeometrie
   Workbenches: Ship_Workbench/de
   Shortcut: 
   SeeAlso: 
---

# Ship LoadExample/de



## Beschreibung

Dieses Werkzeug lädt Geometriebeispiele.

Ship arbeitet über **Schiffseinheiten**, die auf der bereitgestellten Geometrie erstellt werden müssen. Die Geometrie muss ein Festkörper oder ein Satz von Festkörpern sein, wobei folgende Kriterien berücksichtigt werden müssen:

-   Die gesamte Rumpfgeometrie muss bereitgestellt werden (einschließlich symmetrischer Körper).
-   Die Steuerbordgeometrie muss im negativen *y*-Bereich bereitgestellt werden.
-   Ursprungspunkt (0,0,0) ist der Schnittpunkt der *Mittschiffssektion* (Mittelpunkt zwischen der hinteren und vorderen Senkrechten) und der *Basislinie*.

![](images/FreeCAD-Ship-SignCriteria.jpg ) 
*Kriterien für Schiffszeichen*

Um neuen Anwendern zu helfen, enthält Schiff ein Ladeprogramm für Geometriebeispiele mit den folgenden Auswahlmöglichkeiten:

-   Serie 60 von der Universität Iowa
-   Kanonisches Schiff Wigley
-   Katamaran der Serie 60
-   Wigley Katamaran



## Anwendung

1.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Ship_LoadExample.svg" width=16px> [Lade ein Beispiel einer ‏‎Schiffsgeometrie](Ship_LoadExample/de.md)** drücken.
    -   Den Menüeintrag **Ship design → <img src="images/Ship_LoadExample.svg" width=16px> Lade ein Beispiel einer ‏‎Schiffsgeometrie** auswählen.




1.  Eine Aufgaben-Tafel wird angezeigt, die zum Auswählen eines Schiffsgeometriebeispiels auffordert.
    -   Das Beispiel, das geladen werden soll, auswählen und **OK** drücken.
2.  Ergebnis: Das Werkzeug lädt ein neues Dokument mit der ausgewählten Geometrie.


**Warnung, bevor irgendetwas editiert wird! Du arbeitest jetzt mit der ursprünglichen Beispieldatei. Um das unbearbeitete Original-Beispiel zu erhalten, musst du es zuerst als neue Datei speichern, bevor irgendetwas bearbeitet werden kann.**



## Tutorien

-   [FreeCAD Schiffs s60 Tutorium](FreeCAD-Ship_s60_tutorial/de.md)
-   [FreeCAD Schiffs s60 Tutorium (II)](FreeCAD-Ship_s60_tutorial_(II)/de.md)



---
⏵ [documentation index](../README.md) > [Ship](Category_Ship.md) > Ship LoadExample/de
