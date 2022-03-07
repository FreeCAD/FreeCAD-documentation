---
- GuiCommand:/de
   Name:Assembly3 ConstraintPointsCoincident
   Name/de:Assembly3 PunktAufPunkt
   Icon:Assembly_ConstraintPointCoincident.svg
   Workbenches:[Assembly3](Assembly3_Workbench/de.md)
---

# Assembly3 ConstraintPointsCoincident/de

## Beschreibung

Der Befehl <img alt="" src=images/Assembly_ConstraintPointCoincident.svg  style="width:24px;"> [Assembly3 PunktAufPunkt](Assembly3_ConstraintPointsCoincident/de.md) stellt eine Verbindung zwischen zwei Objekten eines Zusammenbaus her und fixiert den Abstand zwischen ihnen sowie ihre Ausrichtung zueinander. Die Gewählten Elemente beider Objekte oder genauer ihre lokalen Koordinatensysteme (LKS) werden genutzt, um ein Objekt zum anderen zu positionieren.

Davon ausgehend, dass das erste Objekt bereits mittels <img alt="" src=images/Assembly_ConstraintLock.svg‎‎  style="width:24px;"> [Festsetzen](Assembly3_ConstraintLock/de.md) unbeweglich gemacht wurde, wird das nächste Objekt auf eine Position bewegt, wo beide LKS-Ursprünge deckungsgleich sind.

Im Bezug auf das erste Element, kann sich das weitere Objekte noch um den Ursprung herum bewegen (um alle drei Achsen). Dies lässt für jede einzelne Verbindung drei Freiheitsgrade unbestimmt.

Diese Bedingung akzeptiert alle Arten von Elementen!

## Anwendung

1.  Zwei Objekte in einen Zusammenbau einfügen.
2.  Je ein Element pro Objekt auswählen.
3.  Den Befehl <img alt="" src=images/Assembly_ConstraintPointCoincident.svg  style="width:16px;"> [Assembly3 Punkt auf Punkt](Assembly3_ConstraintPointsCoincident/de.md) aktivieren durch
    -   Die Schaltfläche **<img src="images/Assembly_ConstraintPointCoincident.svg" width=16px> [Create "PlaneCoincident" constraint](Assembly3_ConstraintPointsCoincident/de.md)**.

## Kinematische Entsprechung 

In einem kinematischen Zusammenhang stellt diese Bedingung ein **Kugelgelenk** dar.

In der Realität kann man nicht mit Punkten arbeiten, daher nutzt man Kugelflächen (sphärische Flächen) als Ersatz für die verbundenen Punkte.

<img alt="" src=images/Assembly3_ConstraintPointsCoincident-01.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_ConstraintPointsCoincident-02.png  style="width:200px;">



*Objekte mit gesetzter Bedingung vor und nach Aktivierung des Lösers*



---
![](images/Right_arrow.png) [documentation index](../README.md) > Assembly3 ConstraintPointsCoincident/de
