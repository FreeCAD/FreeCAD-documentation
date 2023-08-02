---
- GuiCommand:
   Name: Arch Component
   Name/de: Arch Komponente
‎   MenuLocation: Arch -> Dienstprogramme -> Komponente
   Workbenches: Arch_Workbench/de
   Shortcut: **C** **M‏‎**
---

# Arch Component/de

## Beschreibung

Erstellt eine nicht-parametrische [Arch](Arch_Workbench/de.md)-Komponente aus jedem [Part](Part_Workbench/de.md)-basierten Objekt. Dies gibt dem Part-basierten Objekt die gleichen Attribute und Eigenschaften wie anderen Arch-Objekten und erlaubt über das Setzen der **Rollen**-Eigenschaft festzulegen, wie sie nach IFC exportiert werden soll.

## Anwendung


<div class="mw-translate-fuzzy">

1.  Wähle ein [Part](Part_Workbench/de.md)-basiertes Objekt.
2.  Rufe Arch-Komponente unter Verwendung mehrerer Methoden auf:
    -   Drücken der **<img src="images/Arch_Component.svg" width=16px>**-Schaltfläche in der Werkzeugleiste.
    -   Verwenden des Tastaturkürzels **C** **M**.
    -   Verwenden des **Arch** → **Dienstprogramme** → **<img src="images/Arch_Component.svg" width=16px> [Komponente](Arch_Component/de.md)**-Eintrags aus dem Hauptmenü.


</div>

## Gemeinsame Arch Komponenten Eigenschaften 


<div class="mw-translate-fuzzy">

Das Arch-Komponenten-Objekten ist auch eine Basis, die von allen anderen Arch-Objekten (**<img src="images/Arch_Wall.svg" width=16px> [Wand](Arch_Wall/de.md)**, **<img src="images/Arch_Structure.svg" width=16px>[Struktur](Arch_Structure/de.md)**, etc.) geteilt wird. Deshalb sind einige der Eigenschaften und der Verhaltensweisen bei allen Arch-Objekten gleich (ausgenommen Werkzeuge, die keine Volumenkörper-Objekte erzeugen wie **<img src="images/Arch_SectionPlane.svg" width=16px> [Schnittebene](Arch_SectionPlane/de.md)** oder **<img src="images/Arch_Axis.svg" width=16px>[Achse](Arch_Axis/de.md)**):


</div>


<div class="mw-translate-fuzzy">

-   **Basisformteil**: Arch-Komponenten basieren immer auf einem [Formteil](Part_Workbench/de.md)-basierenden Basisobjekt. Einige Arten von Arch-Objekten werden nur die Basisform an sich nutzen, andere (z.B. **<img src="images/Arch_Wall.svg" width=16px> [Wand](Arch_Wall/de.md)**) werden einige zusätzliche Operationen darauf ausführen, wie etwa eine Extrusion. Für einige Arten ist ein Basisobjekt nicht zwingend erforderlich (**<img src="images/Arch_Structure.svg" width=16px> [Struktur](Arch_Structure/de.md)**)


</div>

-   **Additions**: Arch-Komponenten haben eine Addition-Eigenschaft, die eine beliebige Anzahl von Verweisen auf andere [Form](Part_Workbench/de.md)-basierte Objekte enthalten kann. Die Form dieser Ergänzungen wird vereinigt mit der Basisform der Komponente, um die endgültige Form zu erstellen.

-   **Subtractions**: Arch-Komponenten haben eine Subtraction-Eigenschaft, die eine beliebige Anzahl von Verweisen auf andere [Form](Part_Workbench/de.md)-basierte Objekte enthalten kann. Die Form dieser Ergänzungen wird von der Basisform der Komponente subtrahiert, um die endgültige Form zu erstellen.

-   Das Placement von Arch-Komponenten wird nach den Additions und Subtractions vorgenommen, so dass diese gegen das Basisobjekt an der Basisposition durchgeführt werden. Dann wird das Ergebnis an den endgültigen Platz verschoben.


<div class="mw-translate-fuzzy">

-   Objekte können der Additions- bzw. Subtractions-Liste einer Komponente hinzugefügt bzw. von ihr entfernt werden durch selektieren von Objekt und Komponente und benutzen der **<img src="images/Arch_Add.svg" width=16px> [Arch Komponente hinzufügen](Arch_Add/de.md)**- bzw. **<img src="images/Arch_Remove.svg" width=16px>[Arch Komponente entfernen](Arch_Remove/de.md)**-Befehle oder aus dem Aufgaben-Panel durch doppelklicken der Komponente in der Baumansicht. Das Aufgaben-Panel erlaubt auch eine Prüfung, welches Objekt momentan Teil dieser Listen ist.


</div>


<div class="mw-translate-fuzzy">

-   **Role**: Jede Arch-Komponenente hat, neben der durch den Typ (Wand, Fenster, etc.) festgelegten Funktion, auch eine Rolleneigenschaft, die genauer definieren kann, welche Funktion sie hat. Beispielsweise kann eine **<img src="images/Arch_Structure.svg" width=16px>[Struktur](Arch_Structure/de.md)** eine Träger- oder Säulen-Rolle haben. Generische Arch-Komponenten (wie durch diesen Befehl erzeugt) können jede verfügbare Rolle im gesamten Arch-Arbeitsbereich annehmen. Die Rolle wird benutzt, um die Art von IFC-Objekt zu definieren, die beim [Exportieren nach IFC](Arch_IFC/de.md) zu exportieren ist.


</div>

-   **Clone Of**: Jede Arch-Komponente kann ein Klon einer anderen Arch-Komponente des gleichen Typs sein (eine Wand kann nur ein Klon einer anderen Wand sein, etc.). Die einzige Ausnahme ist die generische Arch-Komponente (wie von diesem Befehl erzeugt), die ein Klon jedes anderen Typs (Wand, Struktur, Fenster, etc.) sein kann. Dies erlaubt es, eine generische Arch-Komponente zu benutzen, um den Typ einer anderen zu übersteuern.


<div class="mw-translate-fuzzy">

-   **Description**: Jede Arch-Komponente hat ein Beschreibungsfeld, das beliebigen Text enthalten kann. Dies wird beim [Exportieren nach IFC](Arch_IFC/de.md) benutzt.


</div>

-   **Tag**: Die Tag-Eigenschaft ist ein weiteres Textfeld, das verwendet werden kann, um Objekten eine weitere benutzerdefinierte Identität zu geben.


<div class="mw-translate-fuzzy">

-   **Material**: Alle Arch-Komponenten haben einen Material-Slot (?), der entweder ein [Material](Arch_SetMaterial/de.md) oder ein [MultiMaterial](Arch_MultiMaterial/de.md) enthalten kann (nicht alle Arch-Objekttypen unterstützen die Verwendung von MultiMaterials). Die DiffuseColor- und Transparency-Eigenschaften des verbundenen (attached) Materials definiert die Farbe des Formteil und die Transparenz der Arch-Komponente. Das Material wird im- und exportiert von/nach [IFC](Arch_IFC/de.md), [OBJ](Arch_OBJ/de.md) und [DAE](Arch_DAE/de.md).


</div>

-   **Move with Host**: Wenn eine Komponente in einer anderen eingebettet ist (z.B. ein Fenster in einer Wand), dann sorgt das Setzen dieser Eigenschaft auf *True* dafür, dass sie verschoben und gedreht wird, wenn das Host-Objekt durch **<img src="images/Draft_Move.svg" width=16px> [Draft Verschieben](Draft_Move/de.md)** oder **<img src="images/Draft_Rotate.svg" width=16px> [Draft Drehen](Draft_Rotate/de.md)** verschoben oder gedreht wird.


<div class="mw-translate-fuzzy">

-   **Hi Res**: Arch-Komponenten können die Form eines anderen Objekts als eine höher auflösendere Version von sich selbst verwenden. Dafür müssen sowohl die Hi Res-Eigenschaft als auch der Hi Res-Anzeigemodus gesetzt sein. Dies erlaubt z.B. eine einfache Wand zu erstellen und dann jeden Backstein, aus dem die Wand besteht, zu modellieren, bspw. mit **<img src="images/Part_Box.svg" width=16px> [Part Box](Part_Box/de.md)**. Dann kann man einen Verbund dieser Backsteine als eine höher auflösende Version der Wand benutzen. Die Form der Wand wird durch die Verwendung eines Hi Res-Objekts nicht verändert. Lediglich seine Darstellung in der 3D-Ansicht wird sich durch Übernahme der höher auflösenden Version verändern.


</div>


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Component/de
