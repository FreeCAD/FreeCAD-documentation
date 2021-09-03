---
- GuiCommand:/de
   Name:PartDesign MoveTip
   Name/de:PartDesign VerschiebeSpitze
   MenuLocation:Contextual menu → Spitze festlegen
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   Shortcut:None
   SeeAlso:[Objekt in anderen Körper verschieben](PartDesign_MoveFeature/de.md), [Objekt hinter anderes Objekt verschieben](PartDesign_MoveFeatureInTree/de.md)---


</div>

## Beschreibung


<div class="mw-translate-fuzzy">

**Spitze festlegen**, dieser Befehl im Kontextmenü definiert die Spitze, welche das Bauteils nach außen hin repräsentiert, neu. Standardmäßig ist die Spitze das letzte zum Körper hinzugefügte Feature. Manchmal kann es jedoch nützlich sein, die Spitze vorübergehend auf ein früheres Feature im Baum zu setzen. Dies kann getan werden, um eine Skizze, eine Bezugsgeometrie oder ein Merkmal hinzuzufügen, das im Rückblick früher in der Geschichte des Körpers erstellt worden sein sollte. Zb. ein Pad , welches von einer bereits erstellten Vertiefung MIT durchbohrt werden soll.


</div>


<div class="mw-translate-fuzzy">

Die Spitze wird im Modellbaum durch einen kleinen weißen Abwärtspfeil in einem grünen Kreis, der über dem Symbol des Features liegt, visuell unterschieden.


</div>

![](images/PartDesign_Body_tree-04.png )

## Anwendung

1.  Klicken Sie im Modellbaum mit der rechten Maustaste auf das Formelement (Feature), welches als Spitze festgelegt werden soll.
2.  Wählen Sie aus dem Kontextmenü ![ 24px](images/PartDesign_MoveTip.svg ) **Spitze**.
3.  Die nun aktuelle Spitze wird auf sichtbar gesetzt und alle Elemente unterhalb der Spitze werden ausgeblendet. Von diesem Punkt aus neu erstellte Elemente werden unter der Spitze und über den anderen vorhandenen Elementen platziert.


<div class="mw-translate-fuzzy">

\'\' \'Hinweis\' \'\': Es ist wichtig, nicht zu vergessen, die Spitze wieder auf das letzte Merkmal am unteren Rand des Körperbaums zu setzen um weiter zu konstruieren.


</div>


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}} 
