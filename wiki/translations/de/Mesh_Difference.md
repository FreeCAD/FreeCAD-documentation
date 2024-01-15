---
 GuiCommand:
   Name: Mesh Difference
   Name/de: Mesh Differenz
   MenuLocation: Netze , Boolesche Verknüpfung , Differenz
   Workbenches: Mesh_Workbench/de
   SeeAlso: Mesh_Union/de, Mesh_Intersection/de
---

# Mesh Difference/de



## Beschreibung

Der Befehl **Mesh Differenz** erstellt ein neues, nicht parametrisches Netzobjekt, ein [Mesh Formelement](Mesh_Feature/de.md), das die Differenz zweier Netzobjekte darstellt: ein Netzobjekt wird aus dem anderen herausgeschnitten.

[OpenSCAD](http://www.openscad.org/) muss installiert sein, um diesen Befehl zu verwenden und der Pfad zu seiner ausführbaren Datei muss in den Einstellungen von [OpenSCAD](OpenSCAD_Preferences/de.md) eingetragen sein.

![](images/Mesh_Difference_example.png ) 
*Links: zwei Netzobjekte. Rechts: das Differenzobjekt beider Objekte; der Würfel ist hier als Hauptobjekt ausgewählt, aus dem der Zylinder (das als zweites ausgewählte Abzugsobjekt) herausgeschnitten wird*



## Anwendung

1.  Das Haupt-Netzobjekt auswählen.
2.  Das vom Hauptobjekt abzuziehende Netzobjekt zur Auswahl hinzufügen. Die Netzobjekte müssen sich überlappen.
3.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Mesh_Difference.svg" width=16px> [Differenz](Mesh_Difference/de.md)** drücken.
    -   Den Menüeintrag **Netze → Boolesche Verknüpfung → <img src="images/Mesh_Difference.svg" width=16px> Differenz** auswählen.



## Eigenschaften

Siehe: [Mesh Formelement](Mesh_Feature/de.md).





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh Difference/de
