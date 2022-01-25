---
- GuiCommand:/de
   Name:Part Fillet
   Name/de:Part Verrundung
   MenuLocation:Part → Verrundung
   Workbenches:[Part Arbeitsbereich](Part_Workbench/de.md)
   SeeAlso:[Part Fase](Part_Chamfer/de.md)
---

# Part Fillet/de

## Beschreibung


<div class="mw-translate-fuzzy">

Dieses Werkzeug erzeugt eine Verrundung auf den ausgewählten Kanten eines Objekts. Die Auswahl des Objekts und der Kanten, die verrundet werden sollen, erfolgt in einem Dialog.


</div>

## Anwendung


<div class="mw-translate-fuzzy">

-   Starte das Werkzeug aus der Formteil Werkzeugleiste oder aus dem Menü. Du kannst das Objekt entweder vor oder nach dem Start des Werkzeugs auswählen.
-   Wenn die Form vor dem Start des Werkzeugs nicht ausgewählt wurde, wähle sie in der Form Aufklappliste im [Aufgabenpaneel](Task_Panel/de.md) aus.
-   Wähle den Verrundungstyp, entweder konstanter Radius (Standard) oder variabler Radius.
-   Wähle die Kanten entweder in der [3D Ansicht](3D_view/de.md) oder durch Ankreuzen in der Kantenliste im [Aufgabenpaneel](Task_Panel/de.md) aus.
-   Lege den Radiuswert fest.
-   Klicke zum Bestätigen auf **OK**.


</div>

![](images/Dialog-fillet.png )

## Formteilverrundung VS. PartDesign Verrundung 

Es gibt ein weiteres Verrundungswerkzeug in der <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md). Bitte beachte, dass ihre Bedienung recht unterschiedlich ist. Siehe sich das <img alt="" src=images/PartDesign_Fillet.svg  style="width:24px;"> [PartDesign Verrundung](PartDesign_Fillet/de.md) Referenzseite für weitere Einzelheiten zu ihren Unterschieden.


<div class="mw-translate-fuzzy">

## Hinweise zur Anwendung der Teilverrundung 

Die Teilverrundung könnte nichts bringen, wenn das Ergebnis die nächste benachbarte Kante berühren oder überqueren würde. Wenn Du also nicht das erwartete Ergebnis bekommst, versuche es mit einem kleineren Wert. Dies gilt auch für <img alt="" src=images/Part_Chamfer.svg  style="width:24px;"> [Part Fase](Part_Chamfer/de.md).


</div>


<div class="mw-translate-fuzzy">

Das Verrundungswerkzeug schlägt manchmal fehl, wenn versucht wird, komplexe Objekte zu verrunden. Eine gängige Ursache dafür kann sein, dass die zu verrundende Form nicht geometrisch korrekt ist. Dies kann darauf zurückzuführen sein, dass Linien/Ebenen usw. nicht nach früheren Operationen zur Konstruktion der Form entfernt wurden (z.B. Schneiden/Überschneidung/Fügen). Eine Reihe von Schritten kann genutzt werden, um Probleme zu minimieren:

-   Wenn möglich, lasse das Verrunden eines Teils, bis das Teil vollständig erzeugt ist. Dies minimiert die Wechselwirkung von Verrundungen mit nachfolgenden booleschen Operationen;
-   Verwende die **Part → Gemetrie prüfen**, um auf Fehler in der Formgeometrie zu prüfen und zu korrigieren;
-   Verwende **Teil → Form verfeinern**, um Artefakte zu entfernen, die durch frühere boolesche Operationen vor dem Verrundungsvorgang (und in einigen Fällen zwischen den Verrundungsvorgängen in Folge) verursacht wurden;
-   Erwäge die Verwendung von **Bearbeiten → Einstellungen → PartDesign**, um die automatische Überprüfung und Verfeinerung des Modells nach booleschen und skizzenbasierten Operationen zu ermöglichen (die Leistung kann beeinträchtigt werden, wenn diese Optionen eingeschaltet bleiben).


</div>


<div class="mw-translate-fuzzy">

Beachte auch, dass die Funktion Verrundung des Teils von dem Problem topologische Benennung betroffen ist, wenn die Änderung an einem Modellierungsschritt vorgenommen wird, der früher in der Prozesskette liegt und die Anzahl der Facetten oder Eckpunkte beeinflusst. Dies kann zu unvorhersehbaren Ergebnissen führen. Bis dies gelöst ist (möglicherweise mit V0.19), wird empfohlen, die Operationen Fase und [Verrundung](Part_Fillet/de.md) auf den letzten Schritten in der Kette anzuwenden.


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Fillet/de
