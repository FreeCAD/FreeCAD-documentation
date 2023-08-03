---
 GuiCommand:
   Name: Assembly3 TracePartMove
   Name/de: Assembly3 BewegungAufzeichnen
   Icon: Assembly_Trace.svg‎‎
   MenuLocation: Assembly3 , Trace part move
   Workbenches: Assembly3_Workbench/de
---

# Assembly3 TracePartMove/de

## Beschreibung

Der Befehl <img alt="" src=images/Assembly_Trace.svg  style="width:24px;"> [Bewegung aufzeichnen](Assembly3_TracePartMove/de.md) verfolgt einen einzelnen Punkt eines kinematischen Zusammenbaus, wenn eines der zusammengebauten Objekte mit einem der Werkzeuge <img alt="" src=images/Assembly_Move.svg‎‎  style="width:16px;"> [TeilBewegen](Assembly3_MovePart/de.md) oder <img alt="" src=images/Assembly_AxialMove.svg‎‎  style="width:16px;"> [AxialBewegen](Assembly3_AxialMove/de.md) bewegt wird.

## Anwendung

1.  Wahlweise einen Linienzug-Objekt auswählen:
    -   Einen Punkt, der selbst verfolgt wird.
    -   Eine Kante oder Fläche, um den Mittelpunkt ihrer Form zu verfolgen.
2.  Den Befehl <img alt="" src=images/Assembly_Trace.svg  style="width:16px;"> **Bewegung aufzeichnen** aktivieren durch:
    -   Die Schaltfläche **<img src="images/Assembly_Trace.svg" width=16px> [Bewegung aufzeichnen](Assembly3_TracePartMove/de.md)**.
    -   Den Menüeintrag **Assembly3 → <img src="images/Assembly_Trace.svg" width=16px> Bewegung aufzeichnen**.
3.  Ein Objekt des Zusammenbaus auswählen und mit einem der Folgenden bewegen:
    -   Dem Werkzeug <img alt="" src=images/Assembly_Move.svg‎‎  style="width:16px;"> [Teil bewegen](Assembly3_MovePart/de.md).
    -   Dem Werkzeug <img alt="" src=images/Assembly_AxialMove.svg‎‎  style="width:16px;"> [Axial bewegen](Assembly3_AxialMove.md).
4.  Die **esc**-Taste oder die Schaltfläche **OK** drücken (nur Axial bewegen) um die Verfolgung zu beenden.
5.  Jetzt sieht man ein AsmTrace-Objekt in der [Baumansicht](Tree_view/de.md).

## Hinweise

-   Wenn man im ersten Schritt keine Form auswählt, wird die Form verfolgt, die im dritten Schritt ausgewählt wurde.
-   Um das zu verfolgende Element zu wechseln, muss man dieses Werkzeug deaktivieren, bevor ein neues Element ausgewählt wird und danach wieder aktivieren.
-   Wenn man die Bewegung mit einem anderen Werkzeug steuern möchte wie z.B. der [Kinematiksteuerung](Tutorial_KinematicController/de.md), das den parallelen Einsatz eines Bewegungswerkzeugs erlaubt, könnte man dieses Werkzeug benutzen, um den Zusammenbau Schritt für Schritt zu verändern und das Bewegungswerkzeug, um für jeden Schritt einen Punkt und eine Verbindungslinie zu erstellen. Es ist möglich das Bewegungswerkzeug als Auslöser zu benutzen, indem man auf einen der Pfeile klickt und ihn etwas zieht - nur ein winziges bisschen, bis der nächste Punkt mit Linie erscheint (bei Bedarf Transparenz verwenden).

:   (Ich hoffe hierfür findet sich zukünftig noch eine etwas elegantere Lösung)



---
⏵ [documentation index](../README.md) > Assembly3 TracePartMove/de
