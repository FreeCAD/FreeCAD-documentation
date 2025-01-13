# Draft Snap/de
## Beschreibung

In den Arbeitsbereichen <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft](Draft_Workbench/de.md) und <img alt="" src=images/Workbench_BIM.svg  style="width:24px;"> [BIM](BIM_Workbench/de.md) kann Geometrie erstellt werden durch Auswählen von Punkten in der [3D-Ansicht](3D_view/de.md) oder durch Eingabe von Koordinaten im [Aufgaben-Bereichl](Task_panel/de.md) der Befehle. Eine Weitere Möglichkeit Punkte auszuwählen ist durch Einrasten (Fangen). Einrasten erlaubt, exakte geometrische Punkte auf dem Raster auszuwählen, Punkte auf anderen Objekten, die auf dem Raster liegen oder Punkte, die durch diese Objekte festgelegt werden. Es kann z.B. auf dem Endpunkt einer Linie, dem Mittelpunkt eines Kreises oder dem Schnittpunkt zweier Kanten eingerastet werden.

Das Einrasten steht den meisten Befehlen der Arbeitsbereiche [Draft](Draft_Workbench/de.md) und [BIM](BIM_Workbench/de.md) zur Verfügung.

![](images/Draft_Snap_Endpoint_example.png ) 
*Einrasten auf dem Endpunkt einer Kante*



## Einrast-Werkzeuge 

Diese Werkzeuge sind in der Symbolleiste Draft-Einrasten und im [Draft-Widget Einrasten](Draft_snap_widget.md) vorhanden.

Man beachte, dass kreisförmige Kanten keine Vollkreise sein müssen.

-   <img alt="" src=images/Draft_Snap_Lock.svg  style="width:32px;"> [EinrastenSperren](Draft_Snap_Lock/de.md): aktiviert oder deaktiviert Einrasten global.

-   <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:32px;"> [EinrastenAufEndpunkt](Draft_Snap_Endpoint/de.md): rastet auf Endpunkten von Kanten ein.

-   <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:32px;"> [EinrastenAufMittelpunkt](Draft_Snap_Midpoint/de.md): rastet auf Mittelpunkten von Kanten ein.

-   <img alt="" src=images/Draft_Snap_Center.svg  style="width:32px;"> [EinrastenAufZentrum](Draft_Snap_Center/de.md): Rastet auf Mittelpunkten von Flächen oder kreisförmigen Kanten ein sowie auf den Punkten der {{PropertyData/de|Placement}} von [Draft-Arbeitsebenen-Proxies](Draft_WorkingPlaneProxy/de.md) und [Arch-Gebäudeteilen](Arch_BuildingPart/de.md).

-   <img alt="" src=images/Draft_Snap_Angle.svg  style="width:32px;"> [EinrastenAufWinkel](Draft_Snap_Angle/de.md): rastet auf bestimmten Hauptpunkten von kreisförmigen Kanten ein; auf Vielfachen von 30° und 45°.

-   <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:32px;"> [EinrastenAufSchnittpunkt](Draft_Snap_Intersection/de.md): rastet auf den Schnittpunkt zweier Kanten ein.

-   <img alt="" src=images/Draft_Snap_Perpendicular.svg  style="width:32px;"> [EinrastenSenkrecht](Draft_Snap_Perpendicular/de.md): rastet auf senkrechten Punkten auf Flächen ein ({{Version/de|0.21}}) und auf Kanten.

-   <img alt="" src=images/Draft_Snap_Extension.svg  style="width:32px;"> [EinrastenAufVerlängerung](Draft_Snap_Extension/de.md): rastet auf einer virtuellen Geraden ein, die über die Endpunkte gerader Kanten hinaus verläuft.

-   <img alt="" src=images/Draft_Snap_Parallel.svg  style="width:32px;"> [EinrastenParallel](Draft_Snap_Parallel/de.md): rastet auf einer virtuellen Geraden parallel zu einer geraden Kante ein.

-   <img alt="" src=images/Draft_Snap_Special.svg  style="width:32px;"> [EinrastenSpezial](Draft_Snap_Special/de.md): rastet auf Punkten ein, die durch das Objekt bestimmt werden.

-   <img alt="" src=images/Draft_Snap_Near.svg  style="width:32px;"> [EinrastenInDerNähe](Draft_Snap_Near/de.md): rastet auf dem am nächsten liegenden Punkt einer Fläche oder Kante ein.

-   <img alt="" src=images/Draft_Snap_Ortho.svg  style="width:32px;"> [EinrastenOrtho](Draft_Snap_Ortho/de.md): rastet auf virtuellen Geraden ein, die durch den vorherigen Punkt verläuft, unter einem Winkel, der ein Vielfaches von 45° ist.

-   <img alt="" src=images/Draft_Snap_Grid.svg  style="width:32px;"> [EinrastenAufRaster](Draft_Snap_Grid/de.md): rastet auf den Schnittstellen von Rasterlinien ein.

-   <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:32px;"> [EinrastenAufArbeitsebene](Draft_Snap_WorkingPlane/de.md): projiziert Einrastpunkte auf die aktuelle [Arbeitsebene](Draft_SelectPlane/de.md).

-   <img alt="" src=images/Draft_Snap_Dimensions.svg  style="width:32px;"> [EinrastenAufMaße](Draft_Snap_Dimensions/de.md): zeigt die temporären X- und Y-Maße an.

-   <img alt="" src=images/Draft_ToggleGrid.svg  style="width:32px;"> [RasterUmschalten](Draft_ToggleGrid/de.md): ändert die Sichtbarkeit des Rasters.



## Erweitertes Fangen 

-   Zusätzliche Einrast-Punkte erhält man durch Kombination von zwei Einrast-Optionen. Beispielsweise ergibt die Kombination von [Draft EinrastenOrtho](Draft_Snap_Ortho/de.md) und [Draft EinrastenAufErweiterung](Draft_Snap_Extension/de.md) einen Einrast-Punkt an der Schnittstelle ihrer gedachten Geraden.

-   Einrasten kann mit [Beschränken](Draft_Constrain/de.md) kombiniert werden.

-    **Q**drücken, um einen \"Haltepunkt\" an der aktuellen Position des Mauszeigers einzufügen. Es kann auf die orthogonalen Achsen eines Haltepunktes eingerastet werden und auf die Schnittpunkte dieser Achsen. Ist die Option [Draft EinrastenAufMittelpunkt](Draft_Snap_Midpoint/de.md) aktiv, kann auch auf den Mittelpunkt zwischen zwei Haltepunkten eingerastet werden.

-    ****einmal oder mehrmals drücken, um auf einem Objekt einzurasten, das durch eine andere Geometrie verdeckt wird. Dies nennt sich \"snap cycling\". Man beachte, dass sich der Mauszeiger etwas in der [3D-Ansicht](3D_view.md) bewegen muss, nachem die Taste gedrückt wurde.

![](images/Draft_Snap_example_cycling_1.png ) 
*Snap-Cycling 1: Das rote Rechteck wurde zuerst erstellt und hat daher die Priorität beim Einrasten. Ohne Snap-Cycling kann man nicht auf dem grünen Rechteck einrasten, wo es vom roten Rechteck überlappt wird.*

![](images/Draft_Snap_example_cycling_2.png ) 
*Snap-Cycling 2: Nach einmaliger Benutzung der Snap-Cycle-Taste erhält das grüne Rechteck die Priorität beim Einrasten. Das Einrasten auf dem Mittelpunkt der überlappten grünen Kante ist jetzt möglich.*



## Hinweise

-   Es können mehrere Einrast-Optionen gleichzeitig aktiv sein, aber es ist ratsam, nur die Einrast-Optionen zu aktivieren, die wirklich benötigt werden. Sind zu viele aktiviert, kann dies die Arbeit verlangsamen.
-   Es ist keine gute Idee, [Draft EinrastenNäher](Draft_Snap_Near/de.md) permanent zu aktivieren, da es Vorrang vor vielen anderen Einrast-Optionen hat.



## Einstellungen

Siehe auch: [Voreinstellungseditor](Preferences_Editor/de.md) und [Draft Einstellungen](Draft_Preferences/de.md).

-   Erfordert ein [Draft](Draft_Workbench.md)- oder [BIM](BIM_Workbench/de.md)-Befehl, das die Punkteingabe aktiv ist, kann der maximale Abstand, bei dem [Draft EinrastenAufRaster](Draft_Snap_Grid/de.md) einen Schnittpunkt von Rasterlinien erkennt,\"on-the-fly\" geändert werden durch Drücken von **P** (Mehr-Taste) oder **M** (Weniger-Taste). Diese Einstellung wird gespeichert unter **Werkzeuge → Parameter bearbeiten... → BaseApp → Preferences → Mod → Draft → snapRange**. Sie kann auch im Aufgaben-Bereich des Befehls [Draft EbeneAuswählen](Draft_SelectPlane/de.md) angepasst werden.
-   Um nur dann einzurasten, wenn der **Einrasten**-Umschalter gedrückt gehalten wird:
    -   Abwählen: **Bearbeiten → Einstellungen... → Draft → Raster und Einrasten → Immer einrasten (deaktiviert den Einrast-Umschalter)**.
    -   Die standardmäßige Taste für **Einrasten**, **Ctrl**, kann geändert werden: **Bearbeiten → Einstellungen... → Draft → Raster und Einrasten → Einrast-Umschalter**.
-   Soll die Symbolleiste Draft-Einrasten nur angezeigt werden, wenn ein Befehl aktiv ist: **Bearbeiten → Einstellungen... → Draft → Raster und Einrasten →  Die Symbolleiste Draft-Einrasten nur während der Ausführung von Befehlen anzeigen** aktivieren. {{Version/de|1.0}}
-   Die Einrastsymbole können geändert werden: **Bearbeiten → Einstellungen... → Draft → Raster und Einrasten → Stil der Einrastsymbole**.
-   Die Farbe der Einrastsymbole und der Maße von [Draft EinrastenAufMaße](Draft_Snap_Dimensions/de.md) kann geändert werden: **Bearbeiten → Einstellungen... → Draft → Raster und Einrasten → Farbe der Einrastsymbole**.
-   Die Größe der Einrastsymbole hängt ab von: **Bearbeiten → Einstellungen... → Anzeige → 3D-Viewer → Markergröße**. {{Version/de|1.0}}
-   Die genannten Einzelzeichen-Tastaturkürzel können geändert werden: **Bearbeiten → Einstellungen... → Draft → Schnittstelle → Befehlsinterne Tastaturkürzel**.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap/de
