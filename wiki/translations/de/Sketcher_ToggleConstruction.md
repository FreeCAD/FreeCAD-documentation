---
- GuiCommand   */de
   Name   *Sketcher ToggleConstruction
   Name/de   *Sketcher UmschalterKonstruktion
   MenuLocation   *Sketch → Skizzengeometrien → Umschalten der Hilfsgeometrie
   Workbenches   *[Sketcher](Sketcher_Workbench/de.md)
   Shortcut   ***G** **N**
   SeeAlso   *[Sketcher UmschalterRandbedingung](Sketcher_ToggleDrivingConstraint/de.md)
---

# Sketcher ToggleConstruction/de

## Beschreibung

Dieses Werkzeug schaltet die Skizzengeometrie vom/zum Konstruktionsmodus um. Es kann auf jeder Art von Geometrie angewendet werden   * Linie, Bogen oder Kreis.

Die Konstruktionsgeometrie ist ein wichtiges Werkzeug des Skizzierers. Wenn eine Skizze für einen 3D Vorgang verwendet wird, wird die Konstruktionsgeometrie ignoriert.

Im **[<img src=images/Sketcher_EditSketch.svg style="width   *16px"> [Skizzenbearbeitungsmodus](Sketcher_EditSketch/de.md)** wird die Konstruktionsgeometrie blau dargestellt und wird nicht grün, wenn eine Skizze vollständig beschränkt ist. Sobald du **[<img src=images/Sketcher_LeaveSketch.svg style="width   *16px">[Skizzierermodus verlassen](Sketcher_LeaveSketch/de.md)**, wird die Konstruktionsgeometrie in der [3D Ansicht](3D_view/de.md) ausgeblendet.

Konstruktionslinien können mit der Funktion **[<img src=images/PartDesign_Revolution.svg style="width   *16px"> [PartDesign Drehung](PartDesign_Revolution/de.md)** als Drehachse verwendet werden.

<img alt="" src=images/Sketcher_ConstructionMode_fr_01.png  style="width   *480px;">

## Anwendung


<div class="mw-translate-fuzzy">

1.  Wähle eine oder mehrere Skizzengeometrien in der [3D Ansicht](3D_view/de.md) aus
2.  Rufe das Skizzierer UmschaltenKonstruktionswerkzeug auf verschiedene Weise auf   *
    -   Klicke auf die **[<img src=images/Sketcher_ToggleConstruction.svg style="width   *16px"> [Umschalten Konstruktion](Sketcher_ToggleConstruction/de.md)**.
    -   Verwendung des **Skizze → Skizzierergeometrien → [<img src=images/Sketcher_ToggleConstruction.svg style="width   *16px"> Konstruktionsgeometrie umschalten** Eintrags im Skizzierermenü


</div>

## Beispiel

Verwende den Konstruktionsmodus für einige Skizzenelemente,

<img alt="" src=images/Sketcher_ConstructionMode_fr_01.png  style="width   *450px;">

und sobald Du **[<img src=images/Sketcher_LeaveSketch.svg style="width   *16px"> [den Skizzenbearbeitungsmodus verlassen](Sketcher_LeaveSketch/de.md)**, ist die Geometrie, die in die Konstruktion umgewandelt wurde, in der [3D Ansicht](3D_view/de.md) unsichtbar geworden (aber immer noch im Skizzenbearbeitungsmodus vorhanden).

<img alt="" src=images/Sketcher_ConstructionMode_fr_02.png  style="width   *450px;">

## Hinweise

-    **[<img src=images/Sketcher_CreatePoint.svg style="width   *16px"> [Create point](Sketcher_CreatePoint.md)**will always create points in construction mode regardless of the toolbar toggle state, select the desired points in the [3D view](3D_view.md) after creation and click **[<img src=images/Sketcher_ToggleConstruction.svg style="width   *16px"> [Toggle construction geometry](Sketcher_ToggleConstruction.md)** to change them to normal geometry. <small>(v0.19)</small> 





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ToggleConstruction/de
