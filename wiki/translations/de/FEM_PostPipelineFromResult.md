---
 GuiCommand:
   Name: FEM PostPipelineFromResult
   Name/de: FEM PostPipelineFromResult
   MenuLocation: Ergebnisse , Nachbearbeitungs-Pipeline aus Ergebnis
   Workbenches: FEM_Workbench/de
   Version: 0.17
   SeeAlso: FEM_ResultShow/de, FEM_tutorial/de
---

# FEM PostPipelineFromResult/de



## Beschreibung

ResultPipeline ist ein Ergebnisobjekt, das eine neue grafische Darstellung von FEM-Analyse-Ergebnissen des analysierten Teils erstellt. Es fügt eine Farbskala und einige Darstellungsoptionen hinzu.



## Anwendung

1.  Wähle ein Ergebnisobjekt.
2.  Klicke auf die Schaltfläche **<img src="images/FEM_PostPipelineFromResult.svg" width=16px> '''Nachbearbeitungspipeline aus Ergebnis'''** oder wähle die Option **Ergebnisse → <img src="images/FEM_PostPipelineFromResult.svg" width=16px> Nachbearbeitungspipeline aus Ergebnis** aus dem Menü.
3.  Ein neues Objekt namens \"Pipeline\" wird zur Analyse hinzugefügt.
4.  Doppelklicke auf das neue Pipeline-Objekt in der [Baumansicht](Tree_view.md) und wähle einen Anzeigemodus und das Ergebnisfeld aus. Für den Modus {{Value|Oberfläche}} und das Feld {{Value|Von Mises Spannung}} sieht die Pipeline zum Beispiel so aus:

<img alt="" src=images/Pipeline.PNG  style="width:500px;">

Wenn kein Modell im grafischen Bereich zusehen ist, aktiviere die Hintergrundbeleuchtung **FreeCad → Einstellungen → Anzeige → 3D-Ansicht → Rendern → Farbe der Hintergrundbeleuchtung**.

Wenn ein vom [SI](https://en.wikipedia.org/wiki/International_System_of_Units) abgeleitetes FreeCAD [Einheiten System](Preferences_Editor#Units.md) verwendet wird, basieren auch die Werte der Ausgabeskala auf SI-Einheiten. Das bedeutet, dass die Verschiebung in Meter, die Spannung in Pascal und die Temperatur in Kelvin angegeben wird.



## Eigenschaften



### Dialog Fenster 

Dieses Pipeline-Dialogfenster hat die folgenden Einstellungen:

-   **Modus**: Darstellungsmöglichkeiten für das Ergebnisnetz
    -   **Outline**: Ein Quader dessen Flächen auf den äußersten Punkten vom Netz liegt.
    -   **Nodes**: Die Knoten vom Netz.
    -   **Surface**: Dies ist die Standardeinstellung und zeigt die Oberfläche.
    -   **Surface with Edges**: Wie **Sureface**, aber mit den Maschenumrisskanten und den Verbindungslinien der Oberflächenknoten.
    -   **Wireframe**: Drahtgitter
    -   **Wireframe (Nur Oberfläche)**: Das Drahtgitter nur von der Oberfläche.
    -   **Nodes (Nur Oberfläche)**: Die Knoten vom Netz nur von der Oberfläche.
-   **Feld**: Hier ist der darzustellende Wert zu wählen.
-   **Vektor**: Ist nur aktiv, wenn das **Feld** ein Vektor ist. Wählbar ist der Vektor *Magnitude* oder einer seiner X-, Y- und Z-Komponenten.



### Farbscala

Duch Doppelklick auf die Skala öffnet dieses Einstellungsfenster:

![](images/SIMTUT_05.PNG )

Diese Eigenschaften können geändert werden:

-   **Farbmodell**: Es kann die umgekehrte Reihenfolge des Standardfarbverlaufs oder *Rot-Weiß-Blau*, *Schwarz-Weiß* und *Weiß-Schwarz* gewählt werden.
-   **Stil**: Die Standardoption *Fließend* verwendet den gesamten Farbverlauf. Die Option *Null-basiert* verwendet nur den Farbvbereich, beginnend mit der Farbe, die den Mittelwert bis zum Maximum anzeigt.
-   **Sichtbarkeit**: Die Option *Ausgegraut* färbt alle Netzknoten, deren Werte außerhalb des eingestellten Minimal-/Maximalbereichs liegen, grau. Die Option *Transparent* macht diese Maschenknoten transparent.
-   **Parameterbereich**: Mindest- und Höchstwerte werden automatisch ausgefüllt, diese Werte können geändert werden. Es können auch die Anzahl der angezeigten Dezimalstellen und die Anzahl der über den Parameterbereich verteilten Beschriftungen eingestellt werden.



### Eigenschaftseditor

Im [Eigenschaftseditor](Property_editor/de.md) können auf der Registerkarte *Ansicht* und *Daten* ebenfalls die Einstellungen aus dem Dialogfeld, und weitere, vorgenommen werden.

-    **Mode**: Wie die in der Pipeline verwendeten Filter behandelt werden sollen. Diese Modi sind möglich:

    -   **Serial**: In diesem Modus nimmt jeder Filter den vorherigen Filter als Eingabe. Die Reihenfolge ist dabei die Reihenfolge der Erstellung. Der erste erstellte Filter nimmt die Pipeline als Eingabe. Seine **Input** Eigenschaft ist daher leer.
    -   **Parallel**: In diesem Modus nehmen alle Filter die Rohrleitung als Eingabe.
    -   **Costum**: <small>(v0.20)</small>  Dies ist die Voreinstellung und lässt die Eingabe der Filter so, wie sie sind. Daher ist es möglich, z.B. zwei Filter zu haben, die die Pipeline als Input nehmen, und einen dritten Filter, der einen der beiden Filter als Input nimmt.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostPipelineFromResult/de
