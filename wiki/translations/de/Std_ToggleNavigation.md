---
- GuiCommand:
   Name: Std ToggleNavigation
   Name/de: Std NavigationEditieren
   MenuLocation: Ansicht - Navigations/Editier-Modus
   Workbenches: Alle
   Shortcut: **Esc**
---

# Std ToggleNavigation/de



## Beschreibung

Der Befehl **Std NavigationEditieren** ist für bestimmte Untersuchungstätigkeiten und bestimmte interaktive Netzbearbeitungen gedacht. Diese Tätigkeiten sind rechchenintensiv und erfordern einen Editiermodus der Navigationmöglichkeiten weitestgehend deaktiviert. Mit diesem Befehl ist es möglich, zeitweilig vom Editiermodus zum Navigationsmodus umzuschalten und nach Änderung der [3D-Ansicht](3D_view/de.md) wieder zurück zum Editiermodus.

Nicht mit dem Befehl [Std Bearbeiten](Std_Edit/de.md) verwechseln.



## Anwendung

*Ein Beispiel zur Anwendung des Befehls:*

1.  Zum Arbeitsbereich <img alt="" src=images/Workbench_Mesh.svg  style="width:16px;"> [Mesh](Mesh_Workbench/de.md) wechseln.
2.  Den Menüeintrag **Netze → <img src="images/Mesh_BuildRegularSolid.svg" width=16px> Regelgeometrie...** auswählen.
3.  Das Dialogfenster Regelgeometrie wird geöffnet.
4.  **Ellipsoid** aus der Liste auswählen.
5.  Die Schaltfläche **Erstellen** drücken.
6.  Die Schaltfläche **Schließen** drücken, um das Dialogfenster zu schließen.
7.  Das Netz-Objekt auswählen.
8.  Die Schaltfläche **<img src="images/Mesh_PolyCut.svg" width=16px> [Mesh Schneiden](Mesh_PolyCut/de.md)** drücken.
9.  Punkte in der 3D-Ansicht auswählen, um ein Vieleck (Polygon) zu erstellen, das eine Hälfte des Netzes überlappt.
10. Nach einem Klick mit der rechten Maustaste **Innen** im Kontextmenü auswählen.
11. Das Ergebnis ist ein offenes Netz mit einem Rand.
12. Das Netz sollte noch immer ausgewählt sein.
13. Den Menüeintrag **Netze → <img src="images/Mesh_AddFacet.svg" width=16px> Dreieck hinzufügen** option from the menuauswählen, um den Befehl [Mesh FacetteHinzufügen](Mesh_AddFacet/de.md) aufzurufen.
14. Schwebt der Mauszeiger über einem Randpunkt, wird eine gelbe Markierung angezeigt, die mit einem Klick der linken Mausteste ausgewählt wird.
15. Wahlweise zwei weitere Punkte auswählen und ein Dreieck zum Netz hinzufügen.
16. Jetzt befindet man sich im Edit-Modus und es ist unmöglich die 3D-Ansicht zu drehen oder zu verschieben, während das Zoomen immer noch funktioniert.
17. Den Befehl **Std NavigationEditieren** aufrufen, um in den Navigations-Modus zu wechseln:
    -   Den Menüeintrag **Ansicht → <img src="images/Std_ToggleNavigation.svg" width=16px> Navigations-/Editier-Modus** auswählen.
    -   Oder das Tastaturkürzel: **Esc**.
18. Jetzt kann die 3D-Ansicht gedreht und verschoben werden, aber es können keine Punkte zum Hinzufügen von Dreiecken ausgewählt werden.
19. Den Befehl **Std NavigationEditieren** aufrufen, um in den Editier-Modus zurück zu wechseln:
    -   Den Menüeintrag **Ansicht → <img src="images/Std_ToggleNavigation.svg" width=16px> Navigations-/Editier-Modus** auswählen.
    -   Oder das Tastaturkürzel: **Esc**.
20. Jetzt können wieder Punkte ausgewählt und Dreiecke hizugefügt werden.
21. Nach einem Klick mit der rechten Maustaste **Fertig** im Kontextmenü auswählen, um den Befehl [Mesh FacetteHinzufügen](Mesh_AddFacet/de.md) zu beenden.





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ToggleNavigation/de
