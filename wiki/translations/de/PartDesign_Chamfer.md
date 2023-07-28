---
- GuiCommand:/de
   Name:PartDesign Chamfer
   Name/de:PartDesign Fase
   MenuLocation:Part Design → Modifikationen → Fase
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   SeeAlso:[Verrundung](PartDesign_Fillet/de.md)
---

# PartDesign Chamfer/de



## Beschreibung

Das Werkzeug <img alt="" src=images/PartDesign_Chamfer.svg  style="width:24px;"> **PartDesign Fase** erzeugt Fasen (Abschrägungen) an den ausgewählten Kanten eines Objekts. Es fügt dem Dokument ein **Chamfer**-Objekt und den dazugehörigen Repräsentanten in der [Baumansicht](Tree_view/de.md) hinzu.



## Anwendung



### Eine Fase hinzufügen 

1.  Falls nötig, wird der anzufasende Körper [aktiviert](PartDesign_Body/de#Activer_Status.md).
2.  Es gibt mehrere Möglichkeiten die Kanten zum Anfasen auszuwählen:
    -   Eine oder mehrere einzelne Kanten des Körpers auswählen.
    -   Eine oder mehrere Flächen des Körpers auswählen, um alle ihrer Kanten auszuwählen.
    -   Ein Formelement (normalerweise das letzte) des Körpers auswählen, um alle seiner Kanten auszuwählen. {{Version/de|0.20}}
3.  Um eine Reihe tangential verbundener Kanten auszuwählen, muss nur eine einzige Kante ausgewählt werden, die Fase folgt dann dem kompletten Kantenzug.
4.  Es gibt mehrere Möglichkeiten das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/PartDesign_Chamfer.svg" width=16px> [Fase](PartDesign_Chamfer/de.md)** drücken.
    -   Den Menüeintrag **Part Design → Modifikationen → <img src="images/PartDesign_Chamfer.svg" width=16px> Fase** auswählen.
5.  Wenn kein Körper aktiv ist und sich zwei oder mehr Körper im Dokument befinden, offnet sich der Dialog **Active Body Required** und fordert zur Aktivierung eines Körpers auf. Ist nur ein einziger Körper vorhanden, wird er automatisch ausgewählt.
6.  Der [Aufgabenbereich](Task_panel/de.md) **Parameter der Fase** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
7.  Zum Fertigstellen die **OK**-Schaltfläche drücken.



### Eine Fase bearbeiten 

1.  Eine der folgenden Möglichkeiten startet die Bearbeitung:
    -   Das Chamfer-Objekt in der [Baumansicht](Tree_view/de.md) doppelt anklicken.
    -   Das Chamfer-Objekt in der [Baumansicht](Tree_view/de.md) mit der rechten Maustaste anklicken und **Chamfer bearbeiten** aus dem Kontextmenü auswählen.
2.  Der [Aufgabenbereich](Task_panel/de.md) **Parameter der Fase** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
3.  Zum Fertigstellen die **OK**-Schaltfläche drücken.



## Optionen

-   Zum Hinzufügen von Kanten hat man folgende Möglichkeiten:
    -   Die Schaltfläche **Hinzufügen** drücken, um die Auswahl weiterer Kanten und/oder Flächen in der [3D-Ansicht](3D_view/de.md) zu starten.
    -   Zur Auswahl aller übrigen Kanten hat man folgende Möglichkeiten:
        1.  Wenn nötig, Schaltfläche **Hinzufügen** drücken.
        2.  Tastaturkürzel **Ctrl**+**Shift**+**A** anwenden, oder mit der rechten Maustaste in die Liste klicken und **Alle Kanten verwenden** aus dem Kontextmenü auswählen. {{Version/de|0.20}}
-   Zum Entfernen von Kanten hat man folgende Möglichkeiten:
    -   Die Schaltfläche **Entfernen** drücken, um das Entfernen der Kanten und/oder Flächen in der [3D-Ansicht](3D_view/de.md) zu starten. Ausgewählte Elemente werden in violett hervorgehoben.
    -   Ein oder mehrere Elemente in der Liste auswählen und die **Del**-Taste drücken, oder mit der rechten Maustaste in die Liste klicken und **Entfernen** aus dem Kontextmenü auswählen.
-   Den **Typ** der Fase auswählen:
    -   
        **Gleiche Distanzen**
        
        : Für die Platzierung beider Fasenkanten wird der gleiche Abstand verwendet.

    -   
        **Zwei Distanzen**
        
        : Für die Platzierung der Fasenkanten werden zwei unterschiedliche Abstände verwendet.

    -   
        **Distanz und Winkel**
        
        : Für die Platzierung der einen Fasenkante wird ein Abstand verwendet, die andere Fasenkante wird durch den Winkel festgelegt.
-   Die Schaltfläche **<img src="images/PartDesign_Flip_Direction.svg" width=16px> Richtung umkehren** drücken, um die Richtung der Fase umzudrehen (deaktivaiert für **gleiche Distanz**).
-   Die **Größe** der Fase angeben.
-   Die **Größe 2** der Fase angeben (ist nur verfügbar, wenn **Zwei Distanzen** ausgewählt ist).
-   Den **Winkel** der Fase angeben (ist nur verfügbar, wenn **Distanz und Winkel** ausgewählt ist).
-   Die Checkbox **Alle Kanten verwenden** aktivieren, um alle Kanten des vorherigen Formelements auszuwählen. Dies deaktiviert die Auswahlliste und die dazugehörigen Schaltflächen. {{Version/de|0.20}}



## Hinweise

-   PartDesign Fase sollte nicht mit [Part Fase](Part_Chamfer/de.md) verwechselt werden. Solange man nicht weiß, was man macht, sollte [Part Fase](Part_Chamfer/de.md) nicht auf einen PartDesign-Body angewendet werden. Siehe [Part und PartDesign](Part_and_PartDesign/de.md).
-   Fasen können (dürfen?) die angrenzenden Flächen nicht komplett vereinnahmen.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein PartDesign-Chamfer-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:



### Daten


{{Properties_Title/de|Basis}}

-    {{PropertyData/de|Base|LinkSub}}: Link to the selected edges and faces of the parent feature. Can be a link to only the parent feature if {{PropertyData/de|Use All Edges}} is `True`.

-    {{PropertyData/de|Support Transform|Bool}}: If `True` the chamfered shape of the additive/subtractive parent feature will be used when the chamfer object is included in a [pattern](PartDesign_Workbench#Transformation_tools.md), else only the shape of the chamfer itself will be used. The default is `False`.

-    {{PropertyData/de|Add Sub Shape|PartShape|hidden}}
    

-    {{PropertyData/de|Base Feature|Link|hidden}}: Link to the parent feature.

-    {{PropertyData/de|_ Body|LinkHidden|hidden}}: Link to the parent body.


{{Properties_Title/de|Chamfer}}

-    {{PropertyData/de|Chamfer Type|Enumeration}}: Art der Fase: {{value|Equal distance}} (gleicher Abstand - Standardeinstellung), {{value|Two distances}} (zwei Abstände) oder {{value|Distance and Angle}} (Abstand und Winkel).

-    {{PropertyData/de|Größe|QuantityConstraint}}: Erster Abstand der Fase. Standardwert: {{value|1 mm}}.

-    {{PropertyData/de|Größe2|QuantityConstraint}}: Zweiter Abstand der Fase. Wird nur verwendet, wenn für die {{PropertyData/de|Chamfer Type}} {{Value|Two distances}} ausgewählt wurde. Standardwert: {{value|1 mm}}.

-    {{PropertyData/de|Angle|Winkel}}: Winkel der Fase. Wird nur verwendet, wenn für die {{PropertyData/de|Chamfer Type}} {{Value|Distance and Angle}} ausgewählt wurde. Standardwert: {{value|45 °}}.

-    {{PropertyData/de|Flip Direction|Bool}}:Wenn `True`, wird die Richtung der Fase umgedreht. Wird nicht verwendet, wenn für die {{PropertyData/de|Chamfer Type}} {{Value|Equal distance}} ausgewählt wurde. Standardwert: `False`.

-    {{PropertyData/de|Use All Edges|Bool}}: Wenn `True`, werden alle Kanten des Objekts angefast und die unter der {{PropertyData/de|Base}} angegebenen Kanten werden ignoriert. Standardwert: `False`.


{{Properties_Title/de|Part Design}}

-    {{PropertyData/de|Refine|Bool}}: Wenn auf `True` gesetzt, werden überflüssige Kanten aus dem Ergebnis der Operation entfernt. Der voreingestellte Wert wird durch die Einstellung **Modell nach skizzenbasierter Operation automatisch aufbereiten** bestimmt. Siehe [PartDesign Einstellungen](PartDesign_Preferences/de#Allgemein.md).



## Bekannte Probleme 

Siehe [PartDesign Verrundung](PartDesign_Fillet/de#Bekannte_Probleme.md).





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Chamfer/de
