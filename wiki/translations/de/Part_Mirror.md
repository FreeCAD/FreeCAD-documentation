---
 GuiCommand:
   Name: Part Mirror
   Name/de: Part Spiegeln
   MenuLocation: Part , Spiegelung...
   Workbenches: Part_Workbench/de
---

# Part Mirror/de



## Beschreibung

**Part Spiegeln** erzeugt ein neues Objekt (Abbild), das eine Spiegelung des ursprünglichen Objekts (Quelle) ist. Das Abbildobjekt wird hinter einer Spiegelebene erzeugt. Die Spiegelebene kann eine Standardebene (**XY**, **YZ** oder **XZ**) oder ({{Version/de|1.0}}), unter Verwendung eines Referenzobjekts, eine beliebige Ebene sein.

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

    -   
        {{Version/de|1.0}}
        
        : Ein Referenzobjekt in der [Baumansicht](Tree_view/de.md) oder der [3D-Ansicht](3D_view/de.md) auswählen. Das Referenzobjekt kann eine beliebige ebene Fläche oder kreisförmige Kante sein.
5.  Die Schaltfläche **OK** drücken.
6.  Für jedes Quellobjekt wird ein eigenes Part-Mirror-Objekt erstellt.

Wenn die Beschriftung der Auswahlschaltfläche **Auswählen** anzeigt, ist der Referenz-Auswahlmodus aktiv und es ist eine Auswahlsperre aktiv, die die Auswahl von nicht unterstützten Referenzobjekten verhindert. Die Schaltfläche anklicken, um die Auswahlsperre auszuschalten; die Beschriftung wechselt zu **Referenz auswählen**.

Die Spiegelebene wird durch eine {{PropertyData/de|Normal}} (Richtung der Normale) und eine {{PropertyData/de|Base}} (Grundposition) festgelegt. Wenn die {{PropertyData/de|Mirror Plane}} (Spiegelebene) ein Referenzobjekt enthält, werden diese Eigenschaften auf schreibgeschützt geändert, da sie dann auf diesem Objekt basierend berechnet werden. Die Ebene ist unendlich, auch wenn das referenzobjekt nicht unendlich ist.

Ein Referenzobjekt kann eine ebene Fläche sein, wie eine Fläche eines [Part-Würfels](Part_Box/de.md), eine kreisförmige Kante, eine [Bezugsebene](PartDesign_Plane/de.md), eine [Ursprungsebene](App_OriginGroupExtension/de.md) eines [Std-Part](Std_Part/de.md)-Containers oder irgendein Objekt mit einer einzelnen ebenen Fläche oder einer einzelnen kreisförmigen Kante. Es werden auch [Link-Objekte](App_Link/de.md) unterstützt. Man beachte, dass B-Spline-Oberflächen, wie [Regelflächen](Part_RuledSurface/de.md) oder [Loftflächen](Part_Loft/de.md) nicht unterstützt werden.



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
