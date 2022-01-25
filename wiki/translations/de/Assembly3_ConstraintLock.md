---
- GuiCommand:/de
   Name:Assembly3 ConstraintLock    Name/de:Assembly3 Festsetzen
   Icon:Assembly_ConstraintLock.svg
   Workbenches:[Assembly3](Assembly3_Workbench.md)
---

# Assembly3 ConstraintLock/de

## Beschreibung

Dieses Werkzeug verbindet ein Objekt mit dem globalen Koordinatensystem (GKS) unter Verwendung des lokalen Koordinatensystems (LKS) eines ausgewählten Elements.

:   \- Wurde ein Punkt ausgewählt, werden die Koordinaten seines LKS mit Bezug auf das GKS festgelegt.

    :   Das Objekt kann sich noch um den Punkt herum drehen.
:   \- Wenn eine (gerade) Kante ausgewählt wurde, werden die Koordinaten seines LKS und die Richtung seiner Z-Achse mit Bezug auf das GKS festgelegt.

    :   Das Objekt kann sich noch um die Kante herum drehen.
:   \- Wurde eine Fläche ausgewählt, werden die Koordinaten ihres LKS und dessen Ausrichtung mit Bezug auf das GKS festgelegt.

    :   Das Objekt ist starr mit dem GKS verbunden.

Dies kann genutzt werden, um ein unbewegliches Set zu definieren, sowohl für einen statischen Zusammenbau, als auch für ein kinematische System.

## Anwendung

1.  Ein Objekt in einen Zusammenbau einfügen.
2.  Ein Element des Objekts auswählen.
3.  Den **<img src="images/Assembly_ConstraintLock.svg" width=16px> [Festsetzen](Assembly3_ConstraintLock.md)** Knopf drücken.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Assembly3 ConstraintLock/de
