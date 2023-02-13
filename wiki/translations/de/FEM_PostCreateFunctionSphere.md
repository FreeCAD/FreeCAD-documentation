---
- GuiCommand:/de
   Name:FEM PostCreateFunctionSphere
   Name/de:FEM NachbearbeitungFunktionKugel
   Icon:Fem-post-geo-sphere.svg
   MenuLocation:Ergebnisse → Filterfunktionen → Kugel
   Workbenches:[FEM](FEM_Workbench/de.md)
   SeeAlso:[FEM Tutorium](FEM_tutorial/de.md)
---

# FEM PostCreateFunctionSphere/de


</div>



## Beschreibung


<div class="mw-translate-fuzzy">

Die Funktion <img alt="" src=images/Fem-post-geo-sphere.svg  style="width:24px;"> **FEM NachbearbeitungFunktionKugel** legt die Geometrie fest, mit der ein Netzobjekt geschnitten wird. Sie wird von den Werkzeugen <img alt="" src=images/FEM_PostFilterCutFunction.svg  style="width:16px;"> [Funktion Schnitt-Filter](FEM_PostFilterCutFunction/de.md) und <img alt="" src=images/FEM_PostFilterClipRegion.svg  style="width:16px;"> [Region Ausschnitt-Filter](FEM_PostFilterClipRegion/de.md) verwendet.


</div>



## Anwendung



### Kugelfunktion erstellen 


<div class="mw-translate-fuzzy">

1.  Es gibt mehrere Möglichkeiten eine Funktion zu erstellen:
    -   Die Schaltfläche **<img src="images/Fem-post-geo-sphere.svg" width=16px> [Kugel](FEM_PostCreateFunctionSphere/de.md)** drücken.
    -   Den Menüeintrag **Ergebnisse → Filterfunktionen → <img src="images/Fem-post-geo-sphere.svg" width=16px> Kugel** auswählen.
2.  Der [Aufgabenbereich](Task_panel.md) Implizite Funktion wird geöffnet.
3.  Wahlweise Werte für den Ursprung und den Radius der Schnittkugel eingeben.
4.  Zum Beenden die Schaltfläche **OK** drücken.


</div>



### Kugelfunktion bearbeiten 


<div class="mw-translate-fuzzy">

Wenn das Sphere-Objekt in der [Baumansicht](Tree_view/de.md) ausgeblendet ist, wählt man das <img alt="" src=images/Fem-post-geo-sphere.svg  style="width:24px;"> Sphere-Objekt in der [3D-Ansicht](3D_view/de.md) aus und drückt die **Leertaste**, um es anzuzeigen, so wie in diesem Beispiel:


</div>

<img alt="" src=images/FEM_Sphere-Cut-Function-Example.png  style="width:400px;">



#### Die Kugel bewegen 

-   Durch Klicken und Ziehen am kugelförmigen Gitter lässt sich die Kugel bewegen.



#### Die Kugelgröße anpassen 

-   Durch Klicken und Ziehen an einem der 8 kleinen um das kugelförmige Gitter herum platzierten Würfel lässt sich die Größe der Kugel anpassen.



## Hinweise

-   Vorhandene Funktionen können für unterschiedliche Filter und für unterschiedliche <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:16px;"> [Ergebnis-Pipelines](FEM_PostPipelineFromResult/de.md) genutzt werden. Es wird allerdings dazu geraten, für jede Pipeline einen separaten Satz von Funktionen zu verwenden, um den Überblick über die Elemente in der [Baumansicht](Tree_view/de.md) zu behalten.


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostCreateFunctionSphere/de
