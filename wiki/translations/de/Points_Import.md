---
- GuiCommand:/de
   Name:Points Import
   Name/de:Punkte Importieren
   MenuLocation:Punkte → Punkte Importieren...
   Workbenches:[Punkte](Points_Workbench/de.md)
   SeeAlso:[Punkte Exportieren](Points_Export/de.md)
---

## Beschreibung

Der **Punkte Importieren** Befehl importiert eine Punktwolke aus einer Datei.

## Anwendung

1.  Rufe den Befehl Import Punkte auf verschiedene Weise auf:
    -   Drücke auf die <img alt="" src=images/Points_Import.svg  style="width:24px;"> [Points Import](Points_Import.md) Schaltfläche in der Punkte Werkzeugleiste
    -   Verwende den {{MenuCommand/de|Punkte → <img src="images/Points_Import.svg" width=16px> Punkte importieren}} aus dem Punkte Menü .
2.  Wähle die Punktwolkendatei
3.  Drücke **Öffnen**.

## Eigenschaften

Siehe [Punkte Umwandeln](Points_Convert/de.md).

## Punktwolkendateiformat

-   Eine Punktwolkendatei muss die {{FileName|.asc}}, {{FileName|.pcd}} or {{FileName|.ply}} Erweiterung haben.
-   Jede Linie in der Datei muss die X, Y und Z Koordinaten eines Punktes auflisten.
-   Die Koordinaten müssen durch Leerzeichen getrennt sein.
-   Die Koordinaten müssen einen Dezimalpunkt verwenden, kein Dezimalkomma.

## Muster Punktewolkendatei {#muster_punktewolkendatei}

0 0 0
1.4562 -7.2354 12.2367
5.9423 3.1728 -17.6439


<div class="mw-translate-fuzzy">

Zum Testen kannst du diese [diese Datei](https://github.com/FREECAD/Examples/blob/master/Point_cloud_ExampleFiles/PointCloud-Data_Stanford-Bunny.asc) verwenden, die eine Niedrigpolygon Version des [Stanford Hasen](http://graphics.stanford.edu/data/3Dscanrep/) ist.


</div>





{{Points Tools navi

}} 
