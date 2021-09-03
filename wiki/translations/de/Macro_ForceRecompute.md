 {{Macro/de
|Name=Macro Force Recompute
|Icon=Force_Recompute.png
|Description=Dieses kleine Makro erzwingt eine manuelle Neuberechnung des Modells.
Manchmal nimmt der Benutzer Änderungen am Modell in FreeCAD vor.
Aber FreeCAD scheint sie nicht zu erkennen.
(Ab <small>(v0.17)</small> ) kann die Wirkung dieses Makros über die GUI erreicht werden. Klicke mit der rechten Maustaste auf das Projekt in der Modellstrukturansicht und wähle "Zum Neuberechnen markieren" aus dem Kontextmenü. Danach klicke auf die Schaltfläche Neu berechnen.
|Author=shoogen
|Version=1.0
|Date=2014-09-01
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/8/88/Force_Recompute.png ToolBar Icon]
}}

## Beschreibung

Manchmal, wenn ein Benutzer Änderungen am Modell vornimmt, scheint FreeCAD diese nicht zu erkennen und zu integrieren. Zusätzlich dazu bleibt die blaue **<img src="images/Std_Refresh.svg" width=24px> [Aktualisieren/Neuberechnen](Std_Refresh/de.md)** Taste ausgegraut. Daher wurde dieses kleine Makro entwickelt, um eine manuelle Neuberechnung des Modells zu erzwingen.

**Hinweis:** Ab {{VersionPlus/de|0.17}} kann die Wirkung dieses Makros über die GUI erreicht werden. Rechtsklicke auf das Projekt in der [Modellbaumansicht](Tree_view/de.md) und wähle **Zum Neuberechnen markieren** aus dem Kontextmenü. Dadurch wird das Symbol Aktualisieren/Neuberechnen wieder aktiv. Drücke nun auf die <img alt="" src=images/Std_Refresh.svg  style="width:24px;"> [Aktualisieren/Neuberechnen](Std_Refresh/de.md) Taste, um eine Neuberechnung auszulösen.

## Anwendung

Führe das Makro bei Bedarf aus.

## Skript

ToolBar Icon <img alt="" src=images/Force_Recompute.png  style="width:24px;">

**Macro Force\_Recompute.py**


{{MacroCode|code=
# -*- coding: utf-8 -*-
# Force Recompute
# macro provided by shoogen

import FreeCAD
for obj in FreeCAD.ActiveDocument.Objects:
 obj.touch()
FreeCAD.ActiveDocument.recompute()

}}




