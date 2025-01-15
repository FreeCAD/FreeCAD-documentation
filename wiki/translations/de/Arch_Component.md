---
 GuiCommand:
   Name: Arch Component
   Name/de: Arch Komponente
   MenuLocation: 3D/BIM , Generic 3D tools , Komponente
   Workbenches: BIM_Workbench/de
---

# Arch Component/de



## Beschreibung

Erstellt eine nicht-parametrische [Arch](BIM_Workbench/de.md)-Komponente aus jedem [Part](Part_Workbench/de.md)-basierten Objekt. Dies gibt dem Part-basierten Objekt die gleichen Attribute und Eigenschaften wie anderen Arch-Objekten und erlaubt über das Setzen der {{PropertyData/de|Ifc Type}} festzulegen, wie sie nach IFC exportiert werden soll.



## Anwendung

1.  Ein [Part](Part_Workbench/de.md)-basiertes Objekt auswählen.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Arch_Component.svg" width=16px> [Komponente](Arch_Component/de.md)** drücken.
    -   Den Menüeintrag **3D/BIM → Generic 3D tools → <img src="images/Arch_Component.svg" width=16px> Komponente** auswählen.



## Eigenschaften

Das Arch-Objekt Komponente ist auch eine Basis, die von allen anderen Arch-Objekten ([Arch Wand](Arch_Wall/de.md), [Arch Struktur](Arch_Structure/de.md), usw.) verwendet wird. Deshalb sind einige der Eigenschaften und der Verhaltensweisen bei allen Arch-Objekten gleich (ausgenommen Werkzeuge, die keine Festkörper-Objekte erzeugen wie [Schnittebene](Arch_SectionPlane/de.md) oder [Achse](Arch_Axis/de.md)):



### Daten


{{TitleProperty|Component}}

-    {{PropertyData/de|Additions|LinkList}}: Arch-Komponenten haben eine Addition-Eigenschaft, die eine beliebige Anzahl von Verweisen auf andere [Form](Part_Workbench/de.md)-basierte Objekte enthalten kann. Die Form dieser Ergänzungen wird vereinigt mit der Basisform der Komponente, um die endgültige Form zu erstellen. Siehe [Hinweise](#Hinweise.md).

-    **Axis|Link**: An optional axis or axis system on which this object should be duplicated.

-    {{PropertyData/de|Base|Link}}: Arch-Komponenten basieren immer auf einem [Form](Part_Workbench/de.md)-basierten Basisobjekt. Einige Arten von Arch-Objekten werden nur die Basisform an sich nutzen, andere (z.B. [Wand](Arch_Wall/de.md)) werden einige zusätzliche Operationen darauf ausführen, wie etwa eine Extrusion. Für einige Arten ist ein Basisobjekt nicht zwingend erforderlich ( [Struktur](Arch_Structure/de.md))

-    {{PropertyData/de|Clone Of|Link}}: Jede Arch-Komponente kann ein Klon einer anderen Arch-Komponente des gleichen Typs sein (eine Wand kann nur ein Klon einer anderen Wand sein, etc.). Die einzige Ausnahme ist die generische Arch-Komponente (wie von diesem Befehl erzeugt), die ein Klon jedes anderen Typs (Wand, Struktur, Fenster, etc.) sein kann. Dies erlaubt es, eine generische Arch-Komponente zu benutzen, um den Typ einer anderen zu überschreiben.

-    {{PropertyData/de|Hi Res|Link}}: Arch-Komponenten können die Form eines anderen Objekts als eine höher auflösendere Version von sich selbst verwenden. Dafür müssen sowohl die Hi Res-Eigenschaft als auch der Hi Res-Anzeigemodus gesetzt sein. Dies erlaubt z.B. eine einfache Wand zu erstellen und dann jeden Backstein, aus dem die Wand besteht, zu modellieren, bspw. mit **<img src="images/Part_Box.svg" width=16px> [Part Würfel](Part_Box/de.md)**. Dann kann man einen Verbund dieser Backsteine als eine höher auflösende Version der Wand benutzen. Die Form der Wand wird durch die Verwendung eines Hi Res-Objekts nicht verändert. Lediglich seine Darstellung in der [3D-Ansicht](3D_view/de.md) wird sich durch Übernahme der höher auflösenden Version verändern.

-    **Horizontal Area|Area**: The area of the projection of this object onto the XY plane (read-only).

-    {{PropertyData/de|Material|Link}}: Alle Arch-Komponenten haben einen Material-Slot (?), der entweder ein [Material](Arch_SetMaterial/de.md) oder ein [MultiMaterial](Arch_MultiMaterial/de.md) enthalten kann (nicht alle Arch-Objekttypen unterstützen die Verwendung von [MultiMaterial](Arch_MultiMaterial/de.md)). Die DiffuseColor- und Transparency-Eigenschaften des verbundenen (attached) Materials definiert die Farbe des Formteil und die Transparenz der Arch-Komponente. Das Material wird im- und exportiert von/nach [IFC](Arch_IFC/de.md), [OBJ](Arch_OBJ/de.md) und [DAE](Arch_DAE/de.md).

-    **Move Base|Bool**: Specifies if moving this object moves its base instead.

-    {{PropertyData/de|Move With Host|Bool}}: Wenn eine Komponente in einer anderen eingebettet ist (z.B. ein Fenster in einer Wand), dann sorgt das Setzen dieser Eigenschaft auf *True* dafür, dass sie verschoben und gedreht wird, wenn das Host-Objekt durch [Draft Verschieben](Draft_Move/de.md) oder [Draft Drehen](Draft_Rotate/de.md) verschoben oder gedreht wird.

-    **Perimeter Length|Length**: The perimeter length of the horizontal area (read-only).

-    **Standard Code|String**: An optional standard (OmniClass, etc\...) code for this component.

-    {{PropertyData/de|Subtractions|LinkList}}: Arch-Komponenten haben eine Subtraction-Eigenschaft, die eine beliebige Anzahl von Verweisen auf andere [Form](Part_Workbench/de.md)-basierte Objekte enthalten kann. Die Form dieser Ergänzungen wird von der Basisform der Komponente subtrahiert, um die endgültige Form zu erstellen. Siehe [Hinweise](#Hinweise.md).

-    **Vertical Area|Area**: The area of all vertical faces of this object (read-only).


{{TitleProperty|IFC}}

-    {{PropertyData/de|Ifc Data|Map|Hidden}}:

-    {{PropertyData/de|Ifc Properties|Map|Hidden}}:

-    **Ifc Type|Enumeration**: Jede Arch-Komponenente hat, neben der durch den Typ (Wand, Fenster, etc.) festgelegten Funktion, auch eine Rolleneigenschaft, die genauer definieren kann, welche Funktion sie hat. Beispielsweise kann eine [Struktur](Arch_Structure/de.md) eine Träger- oder Säulen-Rolle haben. Generische Arch-Komponenten (wie durch diesen Befehl erzeugt) können jede verfügbare Rolle im gesamten Arch-Arbeitsbereich annehmen. Die Rolle wird benutzt, um die Art von IFC-Objekt zu definieren, die beim [Exportieren nach IFC](Arch_IFC/de.md) zu exportieren ist.


{{TitleProperty|IFC Attributes}}

-    {{PropertyData/de|Description|String}}: Jede Arch-Komponente hat ein Beschreibungsfeld, das beliebigen Text enthalten kann. Dies wird beim [Exportieren nach IFC](Arch_IFC/de.md) benutzt.

-    {{PropertyData/de|Global Id|String}}:

-    {{PropertyData/de|Object Type|String}}:

-    {{PropertyData/de|Predefined Type|Enumeration}}:

-    **Tag|Enumeration**: Die Tag-Eigenschaft ist ein weiteres Textfeld, das verwendet werden kann, um Objekten eine weitere benutzerdefinierte Identität zu geben.



## Hinweise

-   Das Placement von Arch-Komponenten wird nach den Additions und Subtractions vorgenommen, so dass diese gegen das Basisobjekt an der Basisposition durchgeführt werden. Dann wird das Ergebnis an den endgültigen Platz verschoben.

-   Objekte können den Listen Ergänzugen bzw. Subtraktionen einer Komponente hinzugefügt bzw. von ihr entfernt werden, indem sowohl das Objekt als auch die Komponente ausgewählt werden und die Befehle [Arch Hinzufügen](Arch_Add/de.md) bzw. [Arch Entfernen](Arch_Remove/de.md) verwendet werden oder durch Doppelklick auf die Komponente in der [Baumansicht](Tree_view/de.md). Der Aufgaben-Bereich ermöglicht zu prüfen, welches Objekt momentan Teil dieser Listen ist.



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch Component/de
