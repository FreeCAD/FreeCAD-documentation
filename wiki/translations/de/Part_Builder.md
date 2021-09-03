---
- GuiCommand:/de
   Name:Part Builder
   Name:Part Erbauer
   MenuLocation:Formteil → Formbauer...
   Workbenches:[Part](Part_Workbench/de.md)
   SeeAlso:[Part Grundkörper](Part_Primitives/de.md)
---


</div>

## Beschreibung

Ein Werkzeug zur Erstellung von komplexeren Formen aus verschiedenen parametrischen geometrischen Grundkörpern.

## Anwendung

Dieses Werkzeug kann die folgenden Objekte erstellen:

### Kante aus zwei Knoten {#kante_aus_zwei_knoten}

1.  Wähle zwei Knoten aus
2.  Klicke auf **Erstellen**

![](images/Edge_from_verts-1.gif )

### Draht aus Kanten {#draht_aus_kanten}

1.  Wählein der [3D Ansicht](3D_view/de.md) eine Reihe von benachbarten Kanten aus.
2.  Klicke auf **Erstellen**

![](images/Wire_from_edges-1.gif )

### Fläche aus Knoten {#fläche_aus_knoten}

1.  Wähle Knoten, die die Fläche in der [3D Ansicht](3D_view/de.md) umschließen.
2.  Wähle, ob die Fläche planar sein soll.
3.  Klicke auf **Erstellen**
4.  Objekt wird in der [3D Ansicht](3D_view/de.md) erstellt und in der [Baumansicht](Tree_view/de.md) aufgelistet

![](images/Face_from_verts.gif )

### Fläche aus Kanten {#fläche_aus_kanten}

1.  Wähle eine geschlossene Satz von Kanten, die die Fläche in der [3D Ansicht](3D_view/de.md) umschließen.
2.  Wähle ob die Fläche planar sein soll.
3.  Klicke auf **Erstellen**
4.  Objekt wird in der [3D Ansicht](3D_view/de.md) erstellt und in der [Baumansicht](Tree_view/de.md) aufgelistet

![](images/Face_from_edges.gif )

### Hülle aus Flächen {#hülle_aus_flächen}

1.  Flächen in der [3D Ansicht](3D_view/de.md) auswählen
2.  Wähle ob die Form verfeinert werden soll.
3.  Wähle ob alle Flächen in die Hülle aufgenommen werden sollen.
4.  Klicke auf **Erstellen**
5.  Objekt wird in der [3D Ansicht](3D_view/de.md) erstellt und in der [Baumansicht](Tree_view/de.md) aufgelistet

### Festkörper aus Hülle {#festkörper_aus_hülle}

1.  Wähle es, wenn die Form verfeinert werden soll.
2.  Klicke auf **Erstellen**
3.  Das Objekt wird in der [3D Ansicht](3D_view/de.md) erstellt und in der [Baumansicht](Tree_view/de.md) aufgelistet

## Hinweise

Ein möglicher Arbeitsablauf könnte sein:

-   Zeichne ein Drahtgittermodell deiner Form mit den Werkzeugen in der <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Entwurf Arbeitsbereich](Draft_Workbench/de.md) (z.B. Linie und Draht)
-   Erzeuge alle Flächen mit \"Fläche aus Kanten\"
-   Erzeuge eine \"Hülle aus Flächen\"
-   Erzeuge einen \"Festkörper aus Hülle\"


<div class="mw-translate-fuzzy">





</div>


 
