---
- GuiCommand:
   Name: Sketcher CreateBSplineByInterpolation
   Name/de: Sketcher B-SplineDurchInterpolationErstellen
   MenuLocation: Skizze - Skizzengeometrien - B-Spline durch Knoten erstellen
   Workbenches: [Sketcher](Sketcher_Workbench/de.md)
   Shortcut: **G** **B** **I**
   Version: 0.21
   SeeAlso: [Sketcher GeschlossenenB-SplineErstellen](Sketcher_CreatePeriodicBSpline/de.md)
---

# Sketcher CreateBSplineByInterpolation/de



## Beschreibung

Dieses Werkzeug erstellt eine B-Spline-Kurve durch vorgegebene Kurvenpunkte. (Siehe [diese Seite](B-Splines/de.md) für weitere Informationen über B-Splines).



## Anwendung

1.  Die Schaltfläche **[<img src=images/Sketcher_CreateBSplineByInterpolation.svg style="width:16px"> [B-Spline durch Knoten](Sketcher_CreateBSplineByInterpolation/de.md)** drücken.
2.  Eine Reihe von Punkten durch Klicken in der [3D-Ansicht](3D_view.md) auswählen. Während der Befehl aktiv ist, werden die erstellten Punkte mit geraden Linien verbunden.
3.  Wahlweise kann **M** gedrückt werden, bevor die Eingabe beendet wird, um die Vielfachheit des Knotens am zuletzt gesetzten Punkt festzulegen. (Man beachte, dass dies nicht immer berücksichtigt wird; siehe [Einschränkungen](#Einschränkungen.md) für Einzelheiten).
4.  Wahlweise kann **Backspace** (\<-) gedrückt werden, bevor die Eingabe beendet wird, um den zuletzt erstellten Kontrollpunkt zu löschen.
5.  Ein Rechtsklick beendet die Eingabe und generiert die Kurve.
6.  Abhängig von den Voreinstellungen könnte das Werkzeug aktiv bleiben, um eine neue Kurve zu zeichnen. Erneut mit der rechten Maustaste klicken, um den Befehl zu verlassen.



## Hinweise

Siehe [Sketcher B-SplineErstellen](Sketcher_CreateBSpline/de#Hinweise.md).



## Einschränkungen

-   Die Ergebniskurve unterscheidet sich nicht von einem (nichtuniformen) B-Spline, der durch Kontrollpunkte festgelegt wurde; daher treffen all dort beschriebenen Einschränkungen auch hier zu. Siehe [Sketcher B-SplineErstellen](Sketcher_CreateBSpline/de#Einschränkungen.md).
-   Die erstellten B-Splines sind immer kubisch (d.h. vom Grade 3).
-   Die festgelegte Vielfachheit wird nicht immer berücksichtigt:
    -   Bei einem geschlossenen Spline hat der erste Knoten (deckungsgleich mit dem letzten) immer eine Vielfachheit von 2.
    -   Bei einem nicht geschlossenen Spline haben der erste und der letzte Knoten immer eine Vielfachheit von 4.
    -   Wenn die Punkte direkt davor und danach eine Vielfachheit \>= 3 besitzen, ist das Kurvenstück zwischen diesen Punkten vollständig stetig und dieser (Mittel-) Punkt wird nur mit der Randbedingung Punkt auf Objekt festgelegt. Wird ein Knoten benötigt, sollte man das Werkzeug Knoten einfügen in Betracht ziehen.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateBSplineByInterpolation/de
