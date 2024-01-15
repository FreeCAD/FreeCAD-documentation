---
 GuiCommand:
   Name: Mesh EvaluateFacet
   Name/de: Mesh FacetteAuswerten
   MenuLocation:  Netze , Analysieren , Dreiecksinformation
   Workbenches: Mesh_Workbench/de
---

# Mesh EvaluateFacet/de



## Beschreibung

Der Befehl **Mesh FacetteAuswerten** zeigt Informationen über Flächen von Netzobjekten an.

Mesh: Ellipsoid Facet 3631: Points: <1817, 1818, 1866>, Neighbours: <3534, 3632, 3630>
Triangle: <[1.964574, 0.047063, 0.748046], [1.937166, 0.062461, 0.992797], [1.964574, -0.047063, 0.748046]>



*Beispiel der Informationen, die im Ausgabefenster angezeigt werden*



## Anwendung

1.  Es ist ratsam das [Ausgabefenster](Report_view/de.md) zu aktivieren. Der Befehl gibt dort detaillierte Informationen aus.
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Mesh_EvaluateFacet.svg" width=16px> [Dreiecksinformation](Mesh_EvaluateFacet/de.md)** drücken.
    -   Den Menüeintrag **Netze → Analysieren → <img src="images/Mesh_EvaluateFacet.svg" width=16px> Dreicksinformation** auswählen.
3.  Der Mauszeiger wandelt sich in ein Pipetten-Symbol.
4.  Eine Fläche eines Netzobjekts auswählen.
5.  Ihr Index wird in der [3D-Ansicht](3D_view/de.md) angezeigt.
6.  Weitere Informationen werden im Ausgabefenster ausgegeben:
    -   Der interne Name des Netzobjekts.
    -   Der Index der ausgewählten Fläche.
    -   Die Indizes der drei Eckpunkte der Fläche.
    -   Die Indizes der Flächen, die eine gemeinsame Kante mit der ausgewählten Fläche besitzen.
    -   Die Koordinaten der Eckpunkte.
7.  Wahlweise weitere Flächen auswählen.
8.  Die Option **Info-Modus verlassen** aus dem Kontextmenü der 3D-Ansicht auswählen, um den Befehl abzuschließen.





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh EvaluateFacet/de
