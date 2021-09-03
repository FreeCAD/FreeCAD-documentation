---
- GuiCommand:/de
   Name:Sketcher ToggleConstruction
   Name/de:Skizzierer UmschaltenKonstruktion
   MenuLocation:Skizze → Skizzengeometrien → Umschalten Konstruktionsgeometrie
   Workbenches:[Skizzierer](Sketcher_Workbench/de.md)
---

## Beschreibung

Dieses Werkzeug schaltet die Skizzengeometrie vom/zum Konstruktionsmodus um. Es kann auf jeder Art von Geometrie angewendet werden: Linie, Bogen oder Kreis.

Die Konstruktionsgeometrie ist ein wichtiges Werkzeug des Skizzierers. Wenn eine Skizze für einen 3D Vorgang verwendet wird, wird die Konstruktionsgeometrie ignoriert.

Im **<img src=images/Sketcher_EditSketch.svg style="width:16px"> <img src=images/Sketcher_LeaveSketch.svg style="width:Skizzenbearbeitungsmodus](Sketcher_EditSketch/de.md)** wird die Konstruktionsgeometrie blau dargestellt und wird nicht grün, wenn eine Skizze vollständig beschränkt ist. Sobald du **[16px">[Skizzierermodus verlassen](Sketcher_LeaveSketch/de.md)**, wird die Konstruktionsgeometrie in der [3D Ansicht](3D_view/de.md) ausgeblendet.

Konstruktionslinien können mit der Funktion **<img src=images/PartDesign_Revolution.svg style="width:16px"> [PartDesign Drehung](PartDesign_Revolution/de.md)** als Drehachse verwendet werden.

<img alt="" src=images/Sketcher_ConstructionMode_fr_01.png  style="width:480px;">

## Anwendung


<div class="mw-translate-fuzzy">

1.  Wähle eine oder mehrere Skizzengeometrien in der [3D Ansicht](3D_view/de.md) aus
2.  Rufe das Skizzierer UmschaltenKonstruktionswerkzeug auf verschiedene Weise auf:
    -   Klicke auf die **<img src=images/Sketcher_ToggleConstruction.svg style="width:16px"> [Umschalten Konstruktion](Sketcher_ToggleConstruction/de.md)**.
    -   Verwendung des {{MenuCommand|Skizze → Skizzierergeometrien → <img src=images/Sketcher_ToggleConstruction.svg style="width:16px"> Konstruktionsgeometrie umschalten}} Eintrags im Skizzierermenü


</div>

## Beispiel

Verwende den Konstruktionsmodus für einige Skizzenelemente,

<img alt="" src=images/Sketcher_ConstructionMode_fr_01.png  style="width:450px;">

und sobald Du **<img src=images/Sketcher_LeaveSketch.svg style="width:16px"> [den Skizzenbearbeitungsmodus verlassen](Sketcher_LeaveSketch/de.md)**, ist die Geometrie, die in die Konstruktion umgewandelt wurde, in der [3D Ansicht](3D_view/de.md) unsichtbar geworden (aber immer noch im Skizzenbearbeitungsmodus vorhanden).

<img alt="" src=images/Sketcher_ConstructionMode_fr_02.png  style="width:450px;">





{{Sketcher Tools navi

}}  
