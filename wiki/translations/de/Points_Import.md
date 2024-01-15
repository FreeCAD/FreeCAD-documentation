---
 GuiCommand:
   Name: Points Import
   Name/de: Points Importieren
   MenuLocation: Punkte , Punkte importieren...
   Workbenches: Points_Workbench/de
   SeeAlso: Import_Export/de
---

# Points Import/de



## Beschreibung

Der Befehl **Points Importieren** importiert eine Punktwolke aus einer Datei.



## Anwendung

1.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche <img alt="" src=images/Points_Import.svg  style="width:24px;"> [Punkte importieren\...](Points_Import.md) drücken.
    -   Den Menüeintrag **Punkte → <img src="images/Points_Import.svg" width=16px> Punkte importieren...** auswählen.
2.  Eine Punktwolkendatei auswählen
3.  Die Schaltfläche **Öffnen** drücken.



## Eigenschaften

Siehe [Points Umwandeln](Points_Convert/de.md).



## Dateiformat der Punktwolken 

-   Eine Punktwolkendatei muss die Erweiterung **.asc**, **.pcd** oder **.ply** besitzen.
-   Jede Zeile der Datei muss die X-, Y- und Z-Koordinaten eines Punktes auflisten.
-   Die Koordinaten müssen durch Leerzeichen getrennt sein.
-   Die Koordinaten müssen einen Dezimalpunkt verwenden, kein Dezimalkomma.



## Muster Punktewolkendatei 

0 0 0
1.4562 -7.2354 12.2367
5.9423 3.1728 -17.6439

Zum Testen kann man [diese Datei](https://raw.githubusercontent.com/FreeCAD/Examples/master/Point_cloud_ExampleFiles/PointCloud-Data_Stanford-Bunny.asc) verwenden, die eine grobe (low poly) Version des [Stanford Hasen](http://graphics.stanford.edu/data/3Dscanrep/) ist.





{{Points Tools navi

}}



---
⏵ [documentation index](../README.md) > [Points](Points_Workbench.md) > Points Import/de
