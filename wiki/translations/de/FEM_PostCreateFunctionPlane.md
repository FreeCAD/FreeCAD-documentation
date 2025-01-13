---
 GuiCommand:
   Name: FEM PostCreateFunctionPlane
   Name/de: FEM NachbereitungFunktionEbene
   MenuLocation: Ergebnisse , Filterfunktionen , Ebene
   Workbenches: FEM_Workbench/de
   SeeAlso: FEM_tutorial/de
---

# FEM PostCreateFunctionPlane/de



## Beschreibung

Die Funktion <img alt="" src=images/FEM_PostCreateFunctionPlane.svg  style="width:24px;"> **FEM NachbereitungFunktionEbene** legt die Geometrie fest, mit der ein Netzobjekt geschnitten wird. Sie wird von den Werkzeugen <img alt="" src=images/FEM_PostFilterCutFunction.svg  style="width:16px;"> [Funktion Schnitt-Filter](FEM_PostFilterCutFunction/de.md) und <img alt="" src=images/FEM_PostFilterClipRegion.svg  style="width:16px;"> [Region Ausschnitt-Filter](FEM_PostFilterClipRegion/de.md) verwendet.



## Anwendung



### Ebenenfunktion erstellen 

1.  Die Schaltfläche **<img src="images/FEM_PostCreateFunctionPlane.svg" width=16px> [Ebene](FEM_PostCreateFunctionPlane/de.md)** drücken oder den Menüeintrag **Ergebnisse → Filterfunktionen → <img src="images/FEM_PostCreateFunctionPlane.svg" width=16px> Ebene** auswählen.
2.  Der [Aufgaben-Bereich](Task_panel/de.md) Implizite Funktion wird geöffnet.
3.  Wahlweise Werte für den Ursprung und die Ausrichtung der Schnittebene eingeben.
4.  Zum Beenden die Schaltfläche **OK** drücken.



### Ebenenfunktion bearbeiten 

Wenn das Plane-Objekt in der [Baumansicht](Tree_view/de.md) ausgeblendet ist, wählt man das <img alt="" src=images/FEM_PostCreateFunctionPlane.svg  style="width:24px;"> Plane-Objekt in der [3D-Ansicht](3D_view/de.md) aus und drückt die **Leertaste**, um es anzuzeigen, so wie in diesem Beispiel:

<img alt="" src=images/FEM_Plane-Cut-Function-Example.png  style="width:300px;">



#### Die Ebene bewegen 

-   Den großen weißen Quader anklicken und ziehen um die Ebene entlang ihres Normalenvektors zu verschieben. Mit dem Mauszeiger über dem Anfasser schweben (ohne zu klicken) und **Ctrl** bzw. **Strg** drücken, um die Ausrichtung des Verschiebewerkzeugs zu ändern.
-   Das weiße Gitter anklicken und ziehen.



#### Die Ebene drehen und neigen 

-   Eine der Linien die die kleinen Würfel mit dem großen weißen Quader verbinden anklicken, um die Ebene um ihren Ursprung herum zu drehen und zu kippen.



#### Die Ebenengröße anpassen 

-   Einen der 6 kleinen Würfel anklicken und ziehen, um die Ebene zu skalieren. Die Größe spielt allerdings keine Rolle, da das Objekt eine unendliche Ebene ist.



## Hinweise

-   Vorhandene Funktionen können für unterschiedliche Filter und für unterschiedliche <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:16px;"> [Ergebnis-Pipelines](FEM_PostPipelineFromResult/de.md) genutzt werden. Es wird allerdings dazu geraten, für jede Pipeline einen separaten Satz von Funktionen zu verwenden, um den Überblick über die Elemente in der [Baumansicht](Tree_view/de.md) zu behalten.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostCreateFunctionPlane/de
