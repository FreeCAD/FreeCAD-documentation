---
 GuiCommand:
   Name: FEM ConstraintForce
   Name/de: FEM RandbedingungKraft
   MenuLocation: Modell , Mechanische Randbedingungen und Belastungen , Randbedingung Krafteinwirkung
   Workbenches: FEM_Workbench/de
   SeeAlso: FEM_ConstraintPressure/de
---

# FEM ConstraintForce/de



## Beschreibung

Wendet eine Kraft mit einem gegebenen Wert \[N\] auf die ausgewählte Geometrie an.



## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen, um eine Kraft in eine Fläche, eine Linie oder einen Punkt einzuleiten:
    -   Die Schaltfläche **<img src="images/FEM_ConstraintForce.svg" width=16px> [Krafteinwirkung](FEM_ConstraintForce/de.md)** drücken.
    -   Den Menüeintrag **Modell → Mechanische Randbedingungen und Belastungen →  <img src="images/FEM_ConstraintForce.svg" width=16px> Krafteinwirkung** auswählen.
2.  Das Netzobjekt wird automatisch ausgeblendet und gibt den Blick auf das originale Modell frei. Ist das Netzobjekt noch sichtbar, gibt es zwei Möglichkeiten es auszublenden:
    -   Das Netzobjekt in der [Baumansicht](Tree_view/de.md) auswählen und die **Leertaste** drücken.
    -   Das Netzobjekt in der [Baumansicht](Tree_view/de.md) mit der rechten Maustaste anklicken und **Auswahl ausblenden** aus seinem Kontextmenü auswählen.
3.  Der Dialog **Analyseelement-Parameter** im [Aufgaben-Bereich](Task_panel/de.md) wurde auch geöffnet.
4.  Die Schaltfläche **Add** drücken und eine oder mehrere von entweder *Flächen*, *Kanten* oder *Knoten* in der [3D-Ansicht](3D_view/de.md) auswählen, auf die die Krafteinwirkung angewendet werden soll. Die ausgewählten Elemente erscheinen in der Liste der geometrischen Objekte.
5.  Wahlweise die Schaltfläche **Entfernen** drücken und ein oder mehrere der ausgewählten Elemente in der [3D-Ansicht](3D_view/de.md) abwählen. Die abgewählten Elemente der werden von der Liste der geometrischen Objekte entfernt.
6.  Wahlweise den Wert der **Kraft [N]** anpassen.
7.  Wahlweise eine Fläche oder eine Kante auswählen und die Schaltfläche **Richtung** drücken, um die Kraftrichtung zu ändern. In einem typischen Anwendungsfall lässt man dieses Feld leer, um die Kraft in Richtung der Normale anzuwenden.
8.  Wahlweise die Checkbox **Richtung umkehren** aktivieren, um die Kraftrichtung umzukehren.
9.  Zum Beenden **OK** anklicken.

![](images/FEM_ConstraintForce_example.JPG )



## Hinweise

-   Die festgelegte Kraft wird gleichmäßig auf die ausgewählten Objekte angewendet. Wird z.B. eine Belastung mit einer Kraft von 200 N auf zwei Flächen angewendet, die den gleichen Flächeninhalt besitzen, wird jede Fläche gleichmäßig mit 100 N belastet.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintForce/de
