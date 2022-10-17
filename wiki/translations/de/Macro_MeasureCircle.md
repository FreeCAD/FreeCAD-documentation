# Macro MeasureCircle/de
{{Macro/de
|Name=Macro MeasureCircle|Name/de=Makro Kreis messen
|Icon=Macro_MeasureCircle.png
|Description=Compute the radius of a circle by 3 points or a circular edge
|Author=galou_breizh
|Version=1.0
|Date=2016-04-08
|FCVersion=All
|Download=[https   *//www.freecadweb.org/wiki/images/b/bd/Macro_MeasureCircle.png ToolBar Icon]
}}

## Beschreibung

Dieses Makro zeigt nach der Angabe von drei Punkten oder einer kreisförmigen Kante den berechneten Mittelpunkt und den berechneten Radius eines Kreises an. Eine Linie wird vom Mittelpunkt zum ersten Punkt auf dem Kreis gezeichnet, der für spätere Messungen verwendet werden kann.


{{Codeextralink|https   *//raw.githubusercontent.com/FreeCAD/FreeCAD-macros/master/Information/MeasureCircle.FCMacro}}

## Anwendung

Kopiere das Makro in den Makro-Zielpfad und starte es (siehe [How to install macros](How_to_install_macros/de.md) für weitere Details).

Wähle die drei Punkte und das Ergebnis wird in dem \"Report view\" angezeigt. Kanten können auch ausgewählt werden und zählen als zwei Punkte. Eine kreisförmige Kante kann auch ausgewählt werden. Wenn zwei Kanten ausgewählt wurden, wird der Endpunkt der zweiten Kante in der Berechnung nicht berücksichtigt.

Man kann entweder die Elemente auswählen und dann das Makro starten oder das Makro ohne Auswahl starten und die Elemente nach dem Start des Makros auswählen. Wenn nicht genug Elemente ausgewählt werden, bevor das Makro gestartet wird, wird man aufgefordert, die fehlenden Elemente auszuwählen.

## Code

Die neueste Version des Makros ist zu finden auf [MeasureCircle.FCMacro](https   *//raw.githubusercontent.com/FreeCAD/FreeCAD-macros/master/Information/MeasureCircle.FCMacro), aber der einfachste Weg zur Installation dieses Makros ist die Nutzung des [Addon-Managers](Std_AddonMgr/de.md).

ToolBar Icon ![](images/Macro_MeasureCircle.png )

**Macro_MeasureCircle.FCMacro**



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro MeasureCircle/de
