---
- GuiCommand:
   Name: Curves SketchOnSurface
   Name/de: Curves SkizzeAufFläche
   MenuLocation: Surfaces - Sketch on Surface
   Workbenches: [Curves](Curves_Workbench/de.md)
---

# Curves SketchOnSurface/de



## Beschreibung

Dieses Werkzeug legt eine Skizze über eine Fläche, wie ein Etikett auf eine Flasche. Die Skizze muss an eine Fläche angefügt sein (siehe Sketch.Support). Der `Map`-Modus der Skizze hat keinen Einfluss auf das Ergebnis.

<img alt="" src=images/Curves_SketchOnSurface_demo.png  style="width:600" height="400px;"> 
*Die Abbildung zeigt ein `Sketch_On_Surface*-Objekt auf eine Zylinderfläche angewendet (links) und die zugrundeliegende Skizze im Bearbeitungsmodus (rechts)`



## Anwendung

1.  Zum Arbeitsbereich <img alt="" src=images/Curves_workbench_icon.svg  style="width:24px;"> [Curves](Curves_Workbench/de.md) wechseln. (muss mit dem <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon-Manager](Std_AddonMgr/de.md) installiert werden, wenn noch nicht geschehen)
2.  Es gibt 2 Methoden das Werkzeug SketchOnSurface anzuwenden:

    Die Skizze, die auf eine Fläche übertragen werden soll, ist schon vorhanden:

    1.  Die Skizze an die Zielfläche anfügen:
        -   Im Anfügedialog die Fläche auswählen
        -   Anfügemodus auf Deaktiviert setzen
        -   Anfügedialog schließen
        -   Placement.z=0 setzen.
    2.  Die Skizze bearbeiten und einen Konstruktionsrahmen (blaues Rechteck) um die Geometrien herum hinzufügen. Dies Rechteck stellt die parametrischen Flächenränder dar.
    3.  Bearbeitungsmodus verlassen.
    4.  Die Skizze auswählen.
    5.  Das Werkzeug SketchOnSurface aktivieren durch:
        -   Drücken der Schaltfläche <img alt="" src=images/Curves_SketchOnSurface.svg  style="width:24px;">.
        -   Auswahl des Eintrags **Surfaces → Sketch on Surface** im Curves-Menü.

    Es ist noch keine Skizze zum Übertragen vorhanden:

    1.  Zielfläche in der [3D-Ansicht](3D_view/de.md) auswählen.
    2.  Das Werkzeug SketchOnSurface aktivieren durch:
        -   Drücken der Schaltfläche <img alt="" src=images/Curves_SketchOnSurface.svg  style="width:24px;">.
        -   Auswahl des Eintrags **Surfaces → Sketch on Surface** im Curves-Menü.
    3.  Ein Sketch_On_Surface-Objekt erscheint in der [Baumansicht](Tree_view/de.md).
    4.  Dieses Objekt ausklappen, um das Mapped_Sketch-Objekt darunter anzuzeigen.
    5.  Die Skizze bearbeiten und dabei Geometrien innerhalb des blauen Konstruktionsrahmens hinzufügen.
    6.  Es wird ein auf dieser Skizze basierendes SketchOnSurface-Objekt auf der Objektoberfläche erstellt.



## Optionen

-   Fill Extrusion: Wenn der Wert von Thickness nicht Null ist, werden Seitenflächen erstellt (die blauen Flächen im obigen Bildschirmfoto).
-   Fill Faces: Dies füllt die von Flächen eingeschlossenen geometrischen Figuren (die roten Flächen im obigen Bildschirmfoto).
-   Offset: Dies drückt die oberhalb erstellten Formen in die Zielfläche. Der Wert sollte nicht größer als die Dicke sein, da die Fläche sonst auf der Innenseite verschwindet.
-   Thickness: Wenn nicht Null, ergibt dieser Wert die Dicke bis zur oberen erstellten Fläche.



## Hinweise

Sämtliche Geometrie sollte sich innerhalb des blauen Konstruktionsrahmens befinden, einschließlich weiterer Konstruktionsgeometrien und der sichtbaren internen Geometrien komplexer Kurven (Bezier-Kurven, Ellipsen). Wenn dies nicht der Fall ist, wird das umschließende Rechteck (Bounding-Box) größer als der Konstruktionsrahmen und das übertragene Bild wird entsprechend verkleinert. Wenn nötig, kann die [interne Geometrie ausgeblendet](Sketcher_RestoreInternalAlignmentGeometry/de.md) werden, die nicht vollständig im Konstruktionsrahmen liegt.



## Eigenschaften



## Skripten





{{Curves Tools navi

}}



---
⏵ [documentation index](../README.md) > [Curves](Category_Curves.md) > Curves SketchOnSurface/de
