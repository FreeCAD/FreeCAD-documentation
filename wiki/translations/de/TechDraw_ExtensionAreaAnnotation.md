---
 GuiCommand:
   Name: TechDraw ExtensionAreaAnnotation
   Name/de: TechDraw ErgänzungFlächenangabe
   MenuLocation: TechDraw , Ergänzungen: Merkmale/Änderungen , Flächeninhalt der ausgewählten Flächen berechnen
   Workbenches: TechDraw_Workbench/de
   Shortcut: 
   Version: 0.20
   SeeAlso: TechDraw_AreaDimension/de
---

# TechDraw ExtensionAreaAnnotation/de



## Beschreibung

Das Werkzeug **TechDraw ErgänzungFlächenangabe** berechnet die Fläche der ausgewählten Flächenbereiche und fügt eine Flächenangabe ein.

<img alt="" src=images/TechDraw_ExtensionAreaAnnotationExample.png  style="width:400px;"> 
*Rechts die eingefügte Flächenangabe*



## Anwendung

1.  Wähle einen oder mehrere Flächenbereiche.
2.  Es gibt mehrere Möglichkeiten das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/TechDraw_ExtensionAreaAnnotation.svg" width=16px> [Flächeninhalt der ausgewählten Flächen berechnen](TechDraw_ExtensionAreaAnnotation/de.md)** drücken.
    -   Den Menüeintrag **TechDraw → Ergänzungen: Merkmale/Änderungen → <img src="images/TechDraw_ExtensionAreaAnnotation.svg" width=16px> Flächeninhalt der ausgewählten Flächen berechnen** auswählen.
3.  Die Gesamtfläche aller Flächenbereiche wird berechnet, und als Flächenangabe eingefügt.



## Einschränkungen

-    {{VersionMinus/de|0.21}}: Das Werkzeug kann keine Flächen mit gekrümmten Kanten auswerten.

-   Löcher (Inseln) in der ausgewählten Fläche werden ignoriert. Dieser [Forum-Post](https://forum.freecad.org/viewtopic.php?p=783325#p783325) zeigt eine Übergangslösung. Man kann auch [TechDraw AreaDimension](TechDraw_AreaDimension/de.md) verwenden, aber man muss dann die {{PropertyData/de|References 3D}} des erstellten Maßes korrekt angeben.

-   Der berechnete Flächeninhalt ist nicht dynamisch mit der Fläche verknüpft. Ändert sich der Flächeninhalt der Fläche, wird der Text nicht aktualisiert.





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ExtensionAreaAnnotation/de
