---
 GuiCommand:
   Name: Sketcher CreatePolyline
   Name/de: Sketcher LinienzugErstellen
   MenuLocation: Skizze , Skizzengeometrien , Linienzug erstellen
   Workbenches: Sketcher_Workbench/de
   Shortcut: **G** **M**
   SeeAlso: Sketcher_CreateLine/de
---

# Sketcher CreatePolyline/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_CreatePolyline.svg  style="width:24px;"> [Sketcher LinienzugErstellen](Sketcher_CreatePolyline/de.md) erstellt eine Abfolge von Linien- und Kreisbogenabschnitten, die an ihren Endpunkten verbunden sind. Das Werkzeug besitzt mehrere Modi.

![](images/Sketcher_PolylineExample1.png )



*Polylinie beginnt mit einer Linie, einem tangentialen Bogen, einem senkrechten Bogen und dann einer tangentialen Linie.*



## Anwendung

Siehe auch: [Zeichnungshilfen](Sketcher_Workbench/de#Zeichnungshilfen.md).

1.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Sketcher_CreatePolyline.svg" width=16px> [Linienzug erstellen](Sketcher_CreatePolyline/de.md)** drücken.
    -   Den Menüeintrag **Skizze → Skizzengeometrien → <img src="images/Sketcher_CreatePolyline.svg" width=16px> Linienzug erstellen** auswählen.
    -   Ein Rechtsklick in die [3D-Ansicht](3D_view/de.md) und die Menüoption **<img src="images/Sketcher_CreatePolyline.svg" width=16px> Linienzug erstellen** im Kontextmenü auswählen.
    -   Das Tastaturkürzel **G** then **M**.
2.  Der Mauszeiger wandelt sich zu einem Kreuz mit Werkzeugsymbol.
3.  Die Modi dieses Werkzeugs erfordern einen vorherigen Abschnitt. Dafür eine der folgenden Möglichkeiten auswählen:
    -   Zwei Punkte auswählen, um einen Linienabschnitt festzulegen.
    -   Den Endpunkt eines vorhandenen Linien- oder Kreisbogenabschnitts auswählen ([automatische Randbedingungen](Sketcher_Workbench/de#Automatische_Randbedingungen.md) müssen aktiviert sein).
4.  Wahlweise die **M**-Taste einmal oder mehrmals drücken, um durch die unterschiedlichen Modi für den nächsten Abschnitt zu wechseln. Diese Modi stehen zur Verfügung:
    -   Linie rechtwinklig zum vorherigen Abschnitt.
    -   Linie tangential zum vorherigen Abschnit (dies ist der Ausgangsmodus, wenn der vorherige Abschnitt ein Kreisbogen ist).
    -   Kreisbogen tangential zum vorherigen Abschnitt.
    -   Kreisbogen rechtwinklig (links) zum vorherigen Abschnitt.
    -   Kreisbogen rechtwinklig (rechts) zum vorherigen Abschnitt.
    -   Linie nur mit dem vorherigen Abschnitt verbunden.
5.  Während ein Kreisbogen-Modus aktiv ist, kann wahlweise die **Ctrl**-Taste gedrückt gehalten werden, um den Kreisbogen in 45°-Schritten, bezogen auf den vorherigen Abschnitt, einrasten zu lassen.
6.  Den Endpunkt des Abschnitts auswählen.
7.  Wahlweise wiederholen, um weitere Abschnitte zu erstellen.
8.  Zum Beenden eine der folgenden Möglichkeiten auswählen:
    -   Auf den Startpunkt einrasten, um einen geschlossenen Linienzug zu erstellen.
    -   Die rechte Maustaste oder **Esc** drücken, um einen offenen Linienzug zu erstellen.
9.  Die Linienzugabschnitte werden erstellt und passende Randbedingungen hinzugefügt.
10. Wenn das Werkzeug im [Fortsetzen-Modus](Sketcher_Workbench/de#Fortsetzen-Modi.md) läuft:
    1.  Wahlweise weitere Linienzüge erstellen.
    2.  Zum Beenden die rechte Maustaste oder **Esc** drücken; oder ein anderes Werkzeug zum Erstellen von Geometrien oder Randbedingungen aufrufen.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreatePolyline/de
