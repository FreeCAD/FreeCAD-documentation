---
- GuiCommand:/de
   Name:Part Cylinder
   Name/de:Part Zylinder
   MenuLocation:Formteil → Grundkörper → Zylinder
   Workbenches:[Part](Part_Workbench/de.md)
   SeeAlso:[Part Grundkörper](Part_Primitives/de.md)
---

# Part Cylinder/de

## Beschreibung

Erstellt einen einfachen parametrischen Zylinder mit den Parametern Position, Winkel, Radius und Höhe.

## Anwendung


<div class="mw-translate-fuzzy">

1.  Öffne den **<img src="images/Workbench_Part.svg" width=16px> [Part](Part_Workbench.md)** Arbeitsbereich.
2.  Rufe den Befehl Part Zylinder auf verschiedene Weise auf:
    -   Drücke die **<img src="images/Part_Cylinder.svg" width=24px>** Schaltfläche
    -   Verwende den {{MenuCommand/de|Formteil → Grundkörper → Zylinder}} Eintrag aus dem oberen Menü


</div>


<div class="mw-translate-fuzzy">

**Ergebnis:** Das Standardergebnis ist, dass ein voller Zylinder durch eine kreisförmige Fläche zentriert werden soll, die mit dem globalen Ursprung (Punkt 0,0,0) deckungsgleich ist, mit einem Radius von 2 mm und einer Höhe von 10 mm.


</div>

The cylinder properties can later be edited, either in the [Property editor](Property_editor.md) or by double-clicking the cylinder in the [Tree view](Tree_view.md).

<img alt="ein Zylinder, der mit dem Werkzeug Zylinder erstellt wurde" src=images/cylinder.png  style="width:650px;">

## Eigenschaften

-    **Angle**: This is the rotation angle that permits the creation of a portion of cylinder (it is set to 360° by default)

-    **Height**: The height is the distance in the z-axis

-    **Radius**: The radius defines a plane in x-y.

-    **First Angle**: Angle in first direction. <small>(v0.20)</small> 

-    **Second Angle**: Angle in second direction. <small>(v0.20)</small>

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Cylinder/de
