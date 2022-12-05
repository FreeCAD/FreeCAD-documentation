---
- GuiCommand:/de
   Name:Curves Pipeshell
   Name/de:Curves Rohrschale
   MenuLocation:Surfaces → Pipeshell 
   Workbenches:[Curves](Curves_Workbench/de.md)
---

# Curves Pipeshell/de

## Beschreibung

Das Werkzeug <img alt="" src=images/Curves_Pipeshell.svg  style="width:24px;"> [Curves Rohrschale](Curves_Pipeshell/de.md) erstellt eine Rohrschale (PipeShell-Objekt). Dieses Werkzeug ist Teil des [externen Arbeitsbereichs](external_workbenches/de.md) [Curves](Curves_Workbench/de.md).

## Anwendung

1.  Zum Arbeitsbereich <img alt="" src=images/Curves_workbench_icon.svg  style="width:24px;"> [Curves](Curves_Workbench/de.md) wechseln (muss mit dem <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon-Manager](Std_AddonMgr/de.md) installiert werden, wenn noch nicht geschehen)
2.  Die Kante in der [3D-Ansicht](3D_view/de.md) auswählen, die als Leitkurve (Sweep-Path) verwendet wird.
3.  Eine oder mehrere benötigte Rohrschalenprofile (Profile-Objekte) in der [Baumansicht](Tree_view/de.md) auswählen.
4.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche <img alt="" src=images/Curves_Pipeshell.svg  style="width:24px;"> [Pipeshell](Curves_Pipeshell/de.md) In der Symbolleiste drücken.
    -   Den Menüeintrag **Surfaces → Pipeshell** auswählen.
5.  Die `Pipeshell`-Parameter an die geforderten Randbedingungen anpassen.

## Eigenschaften

### Daten


{{Properties_Title/de|Basis}}

-    **Placement**: [Placement](Placement.md) is the location and orientation of an object in space.

-    **Label**: User name of the object in the [Tree view](Tree_view.md).


{{Properties_Title|Main}}

-    **Mode**: Default is **Frenet**. Mode is used to select the sweeping algorithm. Choices: Frenet, DiscreteTrihedron, FixedTrihetron, Binormal, ShapeSupport, AuxiliarySpine.

-    **Output**: Default is **Surface**. Output determines the shape of the object. Choices: Surface, Sections, Lofted Sections.

-    **Profile**: List of the used profiles.

-    **Spine**:


{{Properties_Title|Mode}}

-    **Auxiliary**:

-    **Contact**:

-    **Corrected**:

-    **Direction**:

-    **Equi Curvi**:

-    **Location**:

-    **Support**:


{{Properties_Title|Settings}}

-    **Max Degree**:

-    **Max Segments**:

-    **Samples**:

-    **Solid**: Default is **False**

-    **Tol3d**: Default is **0.00**.

-    **Tol Ang**: Default is **0.00**.

-    **Tol Bound**: Default is **0.00**.

## Hinweise

-    **Pipeshell**erfordert ein Drahtobjekt als Leitkurve (Sweep-Path), und mindestens ein Rohrschalenprofil (Pipeshell-**Profile**).

-   Die beiden Werkzeuge **Rohrschale** und **Rohrschalenprofil** arbeiten zusammen, wie ein \"erweitertes\" Austragungswerkzeug (Sweep-Tool).

## Einschränkungen

## Skripten





{{Curves Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Curves](Category_Curves.md) > Curves Pipeshell/de
