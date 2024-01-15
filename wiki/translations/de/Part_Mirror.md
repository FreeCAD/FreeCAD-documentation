---
 GuiCommand:
   Name: Part Mirror
   Name/de: Part Spiegeln
   MenuLocation: Part , Spiegelung...
   Workbenches: Part_Workbench/de
---

# Part Mirror/de



## Beschreibung

**Part Spiegeln** erzeugt ein neues Objekt (Abbild), das eine Spiegelung des ursprünglichen Objekts (Quelle) ist. Das Abbildobjekt wird hinter einer Spiegelebene erzeugt. Die Spiegelebene kann eine Standardebene (**XY**, **YZ** oder **XZ**) oder ({{Version/de|0.22}}), unter Verwendung eines Referenzobjekts, eine beliebige Ebene sein.

Ein Beispiel:

![](images/PARTMirrorBeforev11.png )



*Vorher*

![](images/PARTMirrorAfterv11.png )



*Nach dem Spiegeln über die YZ-Ebene*



## Anwendung

![](images/PartMirroring_Scr1.png )

1.  Wahlweise ein oder mehrere Quellobjekte auswählen.
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Part_Mirror.svg" width=16px> [Spiegelung...](Part_Mirror/de.md)** drücken.
    -   Den Menüeintrag **Part → <img src="images/Part_Mirror.svg" width=16px> Spiegelung...** auswählen.
3.  Wurde noch kein Objekt ausgewählt oder soll die Auswahl geändert werden: Ein oder mehrere Objekte in der Liste **Formen** auswählen.
4.  Eine der folgenden Möglichkeiten auswählen:
    -   Eine vorgegebene **Spiegelebene** in der Ausklappliste auswählen.
    -   Ein Referenzobjekt in der [Baumansicht](Tree_view/de.md) oder der [3D-Ansicht](3D_view/de.md) auswählen. Das Referenzobjekt kann eine beliebige ebene Fläche oder kreisförmige Kante sein.
5.  Die Schaltfläche **OK** drücken.
6.  Für jedes Quellobjekt wird ein eigenes Part-Mirror-Objekt erstellt.

When the select button label says **Selecting** you are in reference selection mode and there is a selection gate in effect, which disallows the selection of unsupported reference objects. Click the button to toggle the selection gate off, the button label then changes to **Select reference**.

The mirror plane is defined by a **Normal** (direction) and a **Base** (position). When the **Mirror Plane** property contains a reference object these properties are made read-only as they are then computed based on that object. The plane is infinite even if the reference object is not.

A reference object can be a planar face, such as the face of a [Part Box](Part_Box.md), a circular edge, a [Datum Plane](PartDesign_Plane.md), an [origin plane](App_OriginGroupExtension.md) of a [Std Part](Std_Part.md) container, or any object with a single planar face or single circular edge. There is also support for [Links](App_Link.md). Note, however, that B-spline surfaces, such as [ruled surfaces](Part_RuledSurface.md) or [loft faces](Part_Loft.md) are not supported.



## Optionen

Wenn eine Standardebene anstelle eines Referenzobjekts ausgewählt wurde, können die Eingabefelder unter **Basispunkt** verwendet werden, um die Spiegelebene parallel zu verschieben. Nur eins der **X-** , **Y-** oder **Z-** Eingabefelder ist für eine vorgegebene Standardebene wirksam.

  Standardebene   Basispunkt-Feld   Auswirkung
    
  **XY**          **Z**             Verschiebt die Spiegelebene entlang der **Z**-Achse.
  **XY**          **X**, **Y**      Keine Auswirkung.
  **XZ**          **Y**             Verschiebt die Spiegelebene entlang der **Y**-Achse.
  **XZ**          **X**, **Z**      Keine Auswirkung.
  **YZ**          **X**             Verschiebt die Spiegelebene entlang der **X**-Achse.
  **YZ**          **Y**, **Z**      Keine Auswirkung.



## Hinweise

-   [App Link](App_Link.md)-Objekte, die mit geeigneten Objektarten verknüpft sind und [App Part](App_Part.md)-Container, die geeignete sichtbare Objekte enthalten, können auch als Quellobjekte verwendet werden. {{Version/de|0.20}}
-   Nach der Auswahl einer Standard-Spiegel können die {{PropertyData/de|Normal}} und {{PropertyData/de|Base}} des Part-Mirror-Objekts auf beliebige Werte geändert werden. So ist man auch ohne ein Referenzobjekt nicht auf die Standardebenen eingeschränkt.



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Mirror/de
