---
- GuiCommand:/de
   Name/de:PartDesign Körper
   MenuLocation:Part Design → Erstelle Körper
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   Version:0.17
   SeeAlso:[Std Part](Std_Part/de.md), [Funktion bearbeiten](Feature_editing/de.md)
---

# PartDesign Body/de

## Beschreibung

Ein [PartDesign Körper](PartDesign_Body/de.md) ist das Basiselement, um mit dem [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md) Festkörper zu erzeugen. Es kann [Skizzen](Sketch/de.md), [Bezugsobjekte](Datum.md) und [PartDesign Formelementen](PartDesign_Feature/de.md) enthalten, die bei der Erstellung eines [Einfach zusammenhängender Festkörper](PartDesign_Body/de#Einfach_zusammenhängender_Festkörper/de.md) helfen.

Der Körper bietet ein {{MenuCommand/de|Ursprung}} Objekt, das lokale X-, Y- und Z-Achsen sowie Standardebenen enthält. Diese Elemente können als Referenzen verwendet werden, um [Skizzen](Sketch/de.md) und [PartDesign Grundelement](PartDesign_CompPrimitiveAdditive/de.md) anzuheften.

Die **<img src=images/PartDesign_Body.svg style="width:16px"> <img src=images/Std_Part.svg style="width:PartDesign Körper](PartDesign_Body/de.md)**-Schaltfläche darf nicht mit der **_, um ein [einzeln zusammenhängenden Körper](PartDesign_Body/de#Einzeln_zusammenhängender_Körper.md) als [PartDesign Formelemente](PartDesign_Feature/de.md) zu erstellen. [Std Part](Std_Part/de.md) ist ein gruppierendes Objekt, um [Baugruppen](assembly/de.md) zu erzeugen. Es wird nicht zur Erstellung von Objekten verwendet, sondern um unterschiedliche Objekte im Raum zu positionieren. Mehrfache Körper und andere [Standard Teile](Std_Part/de.md) können innerhalb [Standard Teilen](Std_Part/de.md) positioniert werden, um eine komplexe Baugruppe zu erstellen.

![](images/PartDesign_Body_tree.png ) ![](images/PartDesign_Body_example.png ) 
*Links: die Baumansicht, die die Merkmale zeigt, die nacheinander die endgültige Form des Objekts erzeugen. Rechts: das endgültige Objekt, das in der [3D Ansicht](3D_view/de.md) sichtbar ist.*

## Anwendung

Wenn kein vorhergehender Körper ausgewählt ist:

1.  Drücke die **<img src="images/PartDesign_Body.svg" width=16px> [Body](PartDesign_Body.md)** Taste. Es wird ein leerer Körper erzeugt, der automatisch zu


**[aktiv](PartDesign_Body#Active_status/de.md)**

wird.

1.  Jetzt kannst Du **<img src=images/PartDesign_NewSketch.svg style="width:16px"> [Neue Skizze](PartDesign_NewSketch/de.md)** drücken um

eine <img src=images/PartDesign_Pad.svg style="width:Skizze](Sketch/de.md) im Körper zu erstellen, die mit **[16px"> [Polster](PartDesign_Pad/de.md)**. verwendet werden kann.

1.  Alternativ füge ein Grundelement <img src=images/PartDesign_AdditiveBox.svg style="width:PartDesign Formelemente](PartDesign_Feature/de.md) hinzu, zum Beispiel **[16px"> [Additive box](PartDesign_AdditiveBox.md)**.

Wenn ein Festkörperobjekt ausgewählt ist:

1.  Drücke die **<img src="images/PartDesign_Body.svg" width=16px> [Körper](PartDesign_Body/de.md)** Taste. Es wird ein neuer Körper erzeugt, der ein einzelnes {{MenuCommand/de|Base Feature}} enthält. Dieses Basis Formelement ist eine einfache Referenz auf ein anderes Objekt, das zuvor erstellt oder in das Dokument importiert wurde. Siehe [Basis Formelement](PartDesign_Body#Base_Feature/de.md) für weitere Informationen. Ein vorhandener Körper oder [PartDesign Formelement](PartDesign_Feature/de.md) kann nicht ausgewählt werden, wenn Du **<img src="images/PartDesign_Body.svg" width=16px> [Körper](PartDesign_Body/de.md)** drückst.

### Hinweise

-   Wenn kein Körper derzeit existiert, wenn **<img src=images/PartDesign_NewSketch.svg style="width:16px"> [Neue Skizze](PartDesign_NewSketch/de.md)** gedrückt wird, wird automatisch ein neuer Körper erzeugt.

Wenn ein Körper bereits existiert, muss er vor der Verwendung von **<img src=images/PartDesign_NewSketch.svg style="width:16px"> [Neue Skizze](PartDesign_NewSketch/de.md)** aktiv gemacht werden.

-   Doppelklicke auf den Körper in der [Baumansicht](tree_view/de.md) oder öffne das Kontextmenü (Rechtsklick) und wähle {{MenuCommand/de|Aktiven Körper umschalten}}, um den Körper zu aktivieren oder zu deaktivieren. Wenn ein anderer Körper aktiv ist, wird er deaktiviert. Siehe [active status](PartDesign_Body#Active_status.md) für weitere Informationen.

## Eigenschaften

Ein _ abgeleitet. (`Part::Feature` Klasse), daher teilt sie alle Eigenschaften der letzteren.

Zusätzlich zu den unter [Part Formelementen](Part_Feature/de.md) beschriebenen Eigenschaften hat der PartDesign Körper die folgenden Eigenschaften im [Eigenschaftseditor](Property_Editor/de.md).

### Daten


{{TitleProperty|Base}}

-    {{PropertyData/de|Spitze}}: das [PartDesign Formelement](PartDesign_Feature/de.md), das als \"Spitze\" definiert ist, welches normalerweise das letzte im Körper erzeugte Formelement ist. Die Spitze zeigt die endgültige Form des Körpers an, die in der [3D Ansicht](3D_view/de.md) angezeigt wird, wenn **Anzeigemodus Körper** auf {{Incode|Spitze}} gesetzt ist. Siehe [Spitze](PartDesign_Body#Tip/de.md) für weitere Informationen.

-    {{PropertyData/de|Basis Formelement}}: eine externe Form, die als die erste [PartDesign Formelement](PartDesign_Feature/de.md) im Körper verwendet wird. Sie wird normalerweise beim Ziehen eines Festkörpers in einen leeren Körper gesetzt. Wenn auf diese Weise kein Festkörper importiert wird, ist diese Eigenschaft leer. Siehe [Basis Formelement](PartDesign_Body#Base_Feature/de.md) für weitere Informationen.

-    {{PropertyData/de|Platzierung}}: die Position des Objekts in der [3D Ansicht](3D_view/de.md). Die Platzierung wird durch einen `Basis` Punkt (Vektor) und eine `Drehung` (Achse und Winkel) definiert.. Siehe [Platzierung](Placement/de.md).

-    {{PropertyData/de|Gruppe}}: eine Liste mit den [PartDesign Formelemente](PartDesign_Feature/de.md) im Körper.

#### Versteckte Eigenschaften 

-    {{PropertyData/de|Ursprung|Link}}: das [App Ursprungs-](App_Origin.md) Objekt ist der Positionsbezug für alle Elemente, die in der **Group** enthalten sind.

-    **_ Group Touched|Bool**: ob die Gruppe berührt wird oder nicht.

Auch die versteckten Eigenschaften sind in [Part Formelement](Part_Feature/de.md) beschrieben.

### Ansicht


{{TitleProperty|Base}}

-    **Display Mode Body|Enumeration**: stellt den Anzeigemodus speziell für den Körper mit einem von zwei Typen ein.

    -   
        `Durch`
        
        (Standard) legt alle Objekte innerhalb des Körpers frei, das ist [/de\|Skizze](Sketch.md), [PartDesign Formelemente](PartDesign_Feature.md), Bezugsobjekte usw. Dieser Modus ermöglicht die Veranschaulichung von Teiloperationen, die innerhalb des Körpers durchgeführt werden, und ist daher der empfohlene Modus beim Hinzufügen und Bearbeiten von Formelementen.

Wähle das spezifische Formelement und setze {{PropertyView/de|Sichtbarkeit}} auf {`True`} oder drücke die **Leertaste ** auf der Tastatur.

-   -   
        `Spitze`
        
        stellt nur die endgültige Form des Körpers dar, die durch die Eigenschaft {{PropertyData/de|Spitze}} definiert ist. Alles andere, einschließlich [Skizzen](Sketch/de.md), [Teil Formelemente](PartDesign_Feature/de.md), Bezugspunkte usw., wird nicht angezeigt, auch wenn sie in der [Baumansicht](tree_view/de.md) sichtbar sind. Dieser Modus wird empfohlen, wenn der Körper nicht weiter modifiziert werden muss, so dass eine festgelegte Form angezeigt wird. Dieser Modus wird auch empfohlen, wenn Du die Unterelemente (Knoten, Kanten und Flächen) der endgültigen Form auswählen möchtest, um sie mit den Werkzeugen anderer Arbeitsbereiche zu verwenden.

## Körper Konzept 

### Einzeln zusammenhängender Körper 

Ein PartDesign Körper ist dazu gedacht, einen einzelnen, zusammenhängenden Festkörper zu modellieren. Die Bedeutung von \"zusammenhängend\" ist ein Element, das aus einem Stück gefertigt ist, ohne bewegliche Teile oder getrennte Körper. Beispiele für zusammenhängenden Festkörper sind solche, die aus einem einzigen Stück Rohmaterial durch einen Prozess des Gießens, Schneidens oder Fräsens hergestellt werden. Zum Beispiel bestehen eine Mutter, eine Unterlegscheibe und ein Bolzen jeweils aus einem einzigen massiven Stück Stahl ohne bewegliche Teile, so dass sie von einem PartDesign Körper modelliert werden können. Objekte, die durch Schweißen von zwei Teilen erzeugt werden, können auch durch einen einzigen Körper modelliert werden, solange die Schweißverbindung nicht beabsichtigt auseinander zu brechen.

Sobald diese zusammenhängenden Festkörper in irgendeiner Art von Anordnung zusammengesetzt sind, werden sie zu einer \"Baugruppe\". In einer Baugruppe werden die Objekte nicht miteinander verschmolzen, sondern sie werden einfach \"gestapelt\" oder nebeneinander platziert und bleiben Einzelteile.

<img alt="" src=images/PartDesign_Body_contiguous_separate.png  style="width:" height="200px;"> <img alt="" src=images/PartDesign_Body_contiguous_assembly.png  style="width:" height="200px;"> 
*Links: drei einzelne, zusammenhängende Festkörper, die jeweils durch einen PartDesign Körper modelliert werden. Rechts: die einzelnen Körper, die zu einer Baugruppe zusammengefügt werden.*

### Formelementbearbeitung

Ein PartDesign Körper soll funktionieren, indem ein erster Festkörper entweder aus einer [Skizze](Sketch/de.md) oder aus einer [Grundform](PartDesign_CompPrimitiveAdditive/de.md) erstellt und dann durch [\"Formelemente\"](PartDesign_Feature/de.md) geändert wird, um Material zur vorherigen Form hinzuzufügen oder zu entfernen. Für eine vollständige Erklärung gehe zu [Formelementbearbeitung](feature_editing/de.md).

Ein PartDesign Körper führt eine automatische [Verschmelzung](Part_Fuse/de.md) (Vereinigung) der festen Elemente in seinem Inneren aus . Das bedeutet, dass (1) Teilkörper sich beim Erstellen berühren sollten und (2) getrennte Körper nicht erlaubt sind.

<img alt="" src=images/PartDesign_Body_two_intersection.png  style="width:" height="200px;"> <img alt="" src=images/PartDesign_Body_two_fusion.png  style="width:" height="200px;"> 
*Links: zwei einzelne Festkörper, die sich gegenseitig schneiden. Rechts: ein einzelner PartDesign Körper mit zwei [ Additive Formelemente](PartDesign_Feature/de.md); sie werden automatisch miteinander verschmolzen, so dass sie, anstatt sich zu schneiden, einen einzelnen, zusammenhängenden Festkörper bilden.*

![](images/PartDesign_Body_non-contiguous.png ) 
*Links: zwei getrennte Festkörper; dies ist kein gültiger PartDesign Körper. Rechts: zwei sich berührende Festkörper; dies ergibt einen gültigen PartDesign Körper. Das neuere [Formelement](PartDesign_Feature/de.md) sollte immer das vorherige Formelement berühren oder schneiden, so dass es mit diesem verschmolzen wird und zu einem einzigen zusammenhängenden Festkörper wird.*


**Hinweis:**

andere CAD Programme wie Catia erlauben zusammenhängende Körper im gleichen \" Körper\". Ab v0.19 erlaubt FreeCAD dies nicht mehr. Es gab Diskussionen im [FreeCAD Forum](https://forum.freecadweb.org/index.php) über die Aufhebung dieser Einschränkung, aber es wurde noch keine konkrete Entscheidung getroffen. Wenn Du mehr wissen möchtest oder andere Standpunkte vertreten möchtest, diskutiere bitte im [Forum](https://forum.freecadweb.org/index.php).

## Ausführliche Erläuterung der Eigenschaften 

### Aktiver Status 

Ein geöffnetes Dokument kann mehrere Körper enthalten. Um ein neues Formelement zu einem bestimmten Körper hinzuzufügen, muss es **aktiv** gemacht werden. Ein aktiver Körper wird in der [Baumansicht](tree_view/de.md) mit der Hintergrundfarbe angezeigt, die durch den Wert {{MenuCommand/de|aktiver Behälter}} im [Einstellungseditor](Preferences_Editor#Colors/de.md) angegeben wird. (standardmäßig hellblau). Ein aktiver Körper wird ebenfalls fett dargestellt.

Um einen Körper zu aktivieren oder zu deaktivieren:

-   Doppelklicke auf ihn in der [Baumansicht](tree_view/de.md), oder
-   Öffne das Kontextmenü (Rechtsklick) und wähle {{MenuCommand/de|Aktiven Körper umschalten}}.

Beim Aktivieren eines Körpers wird automatisch in den [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md) umgeschaltet. Es kann jeweils nur ein Körper zu einer Zeit aktiv sein.

![](images/PartDesign_Body_active.png )



*Dokument mit zwei PartDesign Körpern, von denen der zweite aktiv ist.*

### Ursprung

Der Ursprung besteht aus den drei Standardachsen (X, Y, Z) und drei Standardebenen (XY, XZ und YZ). An diese Elemente können bei der Erstellung [Skizzen](Sketch/de.md) und andere Objekte angebunden werden.

1.  Erstelle den Körper.
2.  Wenn der Körper in der <img src=images/PartDesign_NewSketch.svg style="width:Baumansicht](tree_view/de.md) ausgewählt ist, drücke **[16px"> [Neue Skizze](PartDesign_NewSketch/de.md)**; das [Aufgaben Paneel](task_panel/de.md) wird geöffnet, um die Auswahl einer der Ebenen zu ermöglichen.
3.  Wenn der Körper nicht ausgewählt ist, wähle stattdessen den Ursprung und mache ihn in der [3D Ansicht](3D_view/de.md) sichtbar, indem Du die **Space** Leiste in der Tastatur drückst. Erweitere auch das Ursprungsobjekt, um die Achsen und Ebenen zu sehen.
4.  Wähle eine der Ebenen aus, entweder in der <img src=images/PartDesign_NewSketch.svg style="width:Baumansicht](tree_view/de.md) oder in der [3D Ansicht](3D_view/de.md), und drücke dann **[16px"> [Neue Skizze](PartDesign_NewSketch/de.md)**. Die Skizze wird auf der gewählten Ebene erstellt.

Das gleiche Verfahren kann bei der Erzeugung von Hilfsbezugsgeometrie wie [PartDesign Linien](PartDesign_Line/de.md), [PartDesign Ebenen](PartDesign_Plane/de.md) und [PartDesign KoordinatenSysteme](PartDesign_CoordinateSystem/de.md) verwendet werden.


**Hinweis:**

der Ursprung ist ein [App Ursprungs](App_Origin.md)-Objekt der Klasse `App::Origin`, während die Achsen und Ebenen Objekte vom Typ `App::Line` bzw. `App::Plane` sind. Jedes dieser Elemente kann mit der **Leertaste** einzeln ein- und ausgeblendet werden; dies ist nützlich, um bei der Erstellung anderer Objekte die richtige Referenz zu wählen.


**Hinweis 2:**

alle Elemente innerhalb des Körpers werden auf den Ursprung des Körpers referenziert, was bedeutet, dass der Körper in Bezug auf das globale Koordinatensystem bewegt und gedreht werden kann, ohne die Platzierung der Elemente innerhalb des Körpers zu beeinflussen.

<img alt="" src=images/PartDesign_Body_Origin_tree.png ) ![](images/PartDesign_Body_Origin_view.png  style="width:" height="400px;">



*Links: PartDesign Körper Ursprung in der _.*

### Basis Formelement 

Das Basis Formelement ist das erste [PartDesign Formelement](PartDesign_Feature/de.md) im Körper, wenn der Körper auf einer anderen Festkörperform basiert. Dieser Festkörper kann von einem beliebigen Arbeitsbereich erzeugt oder aus einer externen Datei, z.B. einer STEP Datei, importiert werden.

![](images/PartDesign_Body_BaseFeature_tree.png ) 
*PartDesign Körper, jeder von ihnen mit einem einzelnen Basis Formelement, die von zuvor erzeugten Festkörpern übernommen werden.*

Um das Basis Formelement zu erzeugen:

1.  Wähle eine Festkörperform außerhalb eines beliebigen Körpers aus und
2.  drücke **<img src=images/PartDesign_Body.svg style="width:16px"> [Körper](PartDesign_Body/de.md)**; dies erzeugt einen neuen Körper mit einem einzelnen Basis Formelement.


**Note:**

Du kannst keinen vorhandenen Körper oder eines seiner <img src=images/PartDesign_Body.svg style="width:Formelemente](PartDesign_Feature/de.md) auswählen, wenn Du **[16px"> [Körper](PartDesign_Body/de.md)** drückst.

Wenn du bereits einen Körper hast, kannst du das Basis Formelement auf diese Weise erzeugen:

-   Wähle in der [Baumansicht](tree_view/de.md) ein Objekt aus und ziehe es innerhalb des Körpers, oder
-   Im [Eigenschaftseditor](property_editor/de.md) bearbeite den Wert von {{PropertyData/de|Basis Formelement}}, indem Du die Ellipse **...** drückst und ein Objekt aus der Liste auswählst. In diesem Fall kannst Du einen vorhandenen Körper als Basis Formelement auswählen.


**Hinweis:**

Ziehen und Ablegen funktioniert nur bei Körpern, die noch kein Basis Formelement haben.


**Hinweis 2:**

Wenn der Körper bereits mehrere Formelemente hat, wird das Basis Formelement beim Ziehen und Ablegen des externen Festkörpers am Anfang der Liste der Formelemente erzeugt, d. h. es wird am Anfang der {{PropertyData/de|Gruppe}} Eigenschaft hinzugefügt.

Das Basis Formelement ist vollkommen optional; es ist nur dann vorhanden, wenn ein Objekt von außerhalb des Körpers einbezogen wird. Wenn kein externer Festkörper enthalten ist, kannst Du Deine Form trotzdem mit [Skizzen](Sketch/de.md), [Polster](PartDesign_Pad/de.md), [GrundObjekte](PartDesign_CompimitiveAdditive/de.md) und anderen [PartDesign Formelementen](PartDesign_Feature/de.md) erstellen. In diesem Fall bleibt die Eigenschaft {{PropertyData/de|Basis Formelement}} leer.

![](images/PartDesign_Body_BaseFeature_Tip.svg )



*Links: Bauteilkonstruktionskörper mit einem Basis Formelement, das von einem externen Festkörperobjekt übernommen wird, und viele nachfolgende [PartDesign Formelemente](PartDesign_Feature/de.md) obenauf. Rechts: Körper, der kein explizites Basis Formelement hat.*

### Spitze

Die Spitze ist das <img src=images/Part_SimpleCopy.svg style="width:PartDesign Formelement](PartDesign_Feature/de.md), das außerhalb des Körpers freiliegt; d.h. wenn ein anderes Werkzeug aus einem beliebigen Arbeitsbereich (z.B. **[16px"> <img src=images/Part_Cut.svg style="width:Part EinfacheKopie](Part_SimpleCopy/de.md)** oder **[16px"> [Part Schnitt](Part_Cut/de.md)**) die Form des Körpers verwenden muss, wird es die Form der Spitze verwenden. Anders ausgedrückt, die Spitze ist die endgültige Darstellung des Körpers, als ob die parametrische Historie nicht existieren würde.

![](images/PartDesign_Body_Tip_final.svg )



*Links: PartDesign Körper mit vollständiger parametrischer Historie inklusive Zwischenformelementen. Rechts: Die Spitze ist die endgültige Form, die aus dem Körper exportiert werden kann, wobei die Historie des Modells weggelassen wird.*

Die Spitze wird automatisch auf das zuletzt im Körper erzeugte Formelement gesetzt. Er kann jedoch auch auf jedes der Zwischen Formelemente gesetzt werden, indem Du das Kontextmenü <img src=images/PartDesign_MoveTip.svg style="width:Baumansicht](tree_view/de.md) öffnest (Rechtsklick) und **[16px"> [Setze Spitze](PartDesign_MoveTip.md)**, wählst, oder durch Ändern des Körperwertes **Spitze** im [Eigenschaftseditor](property_editor/de.md).

Das Ändern der Spitze in der Tat rollt seine Geschichte zurück, wodurch es möglich wird, Funktionen hinzuzufügen, die früher hätten hinzugefügt werden sollen. Außerdem wird es einer anderen Form externen Werkzeugen ausgesetzt.

In der [Baumansicht](tree_view/de.md) wird die Spitze des Körpers durch das [PartDesign Formelement](PartDesign_Feature/de.md) erkannt, das eine Symbol Überlagerung hat, das aus einem weißen Pfeil innerhalb eines grünen Kreises besteht.

![](images/PartDesign_Body_Tip_tree.png ) 
*Zwei PartDesign Körper, jeder von ihnen mit [PartDesign Formelementen](PartDesign_Feature/de.md). Die Spitze ist das letzte Formelement in ihnen und wird mit einem Überlagerungssymbol markiert.*

### Wechselwirkung mit anderen Arbeitsbereichen 


<div class="mw-translate-fuzzy">

Standardmäßig sind Objekte unter einem Körper auswählbar, was natürlich erforderlich ist, um Merkmale in PartDesign zu bearbeiten und hinzuzufügen. Die Auswahl der Funktionen eines Körpers zur Erstellung von Operationen aus anderen Arbeitsbereichen (wie [Part](Part_Workbench/de.md) oder [Draft](Draft_Workbench/de.md)) wird jedoch nicht empfohlen, da die Ergebnisse unerwartet sein können; in allen Fällen wird im Ausgabefenster ein Fehler gekennzeichnet mit *Links go out of the allowed scope* angezeigt.


</div>

Daher sollte bei Wechselwirkungen mit anderen Arbeitsbereichen in der [Baumansicht](tree_view/de.md) nur der Körper selbst ausgewählt werden. In Fällen, in denen es notwendig ist, bestimmte Unterelemente des Körpers (Knoten, Kanten und Flächen) auszuwählen, sollte die Eigenschaft {{PropertyView/de|Ansichtsmodus Körper}} des Körpers auf `Spitze` umgeschaltet werden. Wenn dieser Modus aktiviert ist, ist der Zugriff auf Objekte unter dem Körper ([Formelemente](PartDesign_Feature/de.md), Bezugspunkte, [Skizzen](Sketch/de.md)) deaktiviert, und alles außer der Körpereigenschaft [Spitze](PartDesign_Body#Tip/de.md) wird in der [3D-Ansicht](3D_view/de.md) ausgeblendet.

Sobald die Unterelemente mit anderen Arbeitsbereichen verwendet wurden, kann {{PropertyView/de|Anzeige Modus Körper}} auf `Durch` zurückgesetzt werden.

![](images/PartDesign_Body_Tip_Display_mode.svg )



*Links: wenn "Anzeigemodus Körper" auf `Durch* gesetzt ist, ist es möglich, Operationen mit den einzelnen [PartDesign Formelementen](PartDesign_Feature/de.md) auszuwählen und durchzuführen; dies wird im Allgemeinen nicht empfohlen. Rechts: Wenn "Anzeigemodus Körper" auf {{incode|Spitze` gesetzt ist, werden alle am Körper vorgenommenen Auswahlen und Operationen an der Spitze ausgeführt, wobei sichergestellt wird, dass nur die endgültige Form des Körpers freigelegt wird.}}

### Sichtbarkeitsmanagement

Die Sichtbarkeit des Körpers hat Vorrang vor der Sichtbarkeit seiner Elemente. Ist der Körper unsichtbar, sind alle Elemente unsichtbar. Ist dieser sichtbar kann immer nur ein Formelement sichtbar sein. Durch anklicken und die **Leertaste** schaltet man die Sichtbarkeit an oder aus.

Mehrfache [Skizzen](Sketch/de.md) können gleichzeitig sichtbar sein, aber nur ein [PartDesign Formelement](PartDesign_Feature/de.md) (Festkörper Ergebnis) kann gleichzeitig sichtbar sein. Durch Auswahl eines ausgeblendeten Formelementes und Drücken der **Space** in der Tastatur wird es sichtbar und das zuvor sichtbare Formelement automatisch ausgeblendet.

![](images/PartDesign_Body_Visibility.png ) 
*PartDesign Körper: Mehrfache [Skizzen](Sketch/de.md) können gleichzeitig sichtbar sein, aber nur ein Festkörper [PartDesign Formelement](PartDesign_Feature/de.md) kann gleichzeitig sichtbar sein, unabhängig davon, ob es sich um die Spitze handelt oder nicht.*

### Anfügung

[PartDesign Formelemente](PartDesign_Feature/de.md), genau wie [Ebene Objekte](Part_Part2DObject/de.md), können an unterschiedliche Ebenen angehängt werden, normalerweise an die Standardebenen, die durch die [Ursprung](PartDesign_Body#Origin/de.md) des Körpers definiert sind, oder an benutzerdefinierte [PartDesign Ebenen](PartDesign_Plane/de.md).


<div class="mw-translate-fuzzy">

[Skizzen](Sketch/de.md) werden normalerweise bei ihrer Erstellung an eine Ebene angehängt. Auf ähnliche Weise können auch [Grundformelemente](PartDesign_CompPrimitiveAdditive/de.md) angehängt werden. Das Anhängen dieser Objekte an eine Ebene ermöglicht es, sie innerhalb des Körpers zu bewegen, indem ihre Eigenschaft {{PropertyData/de|Anfügung Versatz}} geändert wird. Weitere Informationen zu den Anfügemodi findest Du unter [Part Anfügung](Part_Attachment/de.md).


</div>

Ein [PartDesign Formelement](PartDesign_Feature/de.md), das nicht angehängt ist, wird mit einem roten Überlagerungssymbol neben seinem Symbol in der [Baumansicht](tree_view/de.md) angezeigt.

![](images/PartDesign_Body_Feature_attachment.png ) 
*PartDesign Körper: [PartDesign Formelement](PartDesign_Feature/de.md) die nicht an eine Ebene oder ein Koordinatensystem gebunden sind, werden mit einem Überlagerungssymbol neben ihrem Symbol in der [Baumansicht](tree_view/de.md) angezeigt.*

## Vererbung

Ein _ (`Part::Feature` Klasse) ist durch die Zwischenklasse {`Part::BodyBase`} und wird um eine Origin-Erweiterung erweitert.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Vereinfachtes Diagramm der Beziehungen zwischen den Kernobjekten im Programm. Die `PartDesign::Körper* Objekte werden zum Aufbau parametrischer 3D-Körper verwendet und sind somit vom Basisobjekt {{incode|Part::Formelement` abgeleitet.}}

und haben einen Ursprung, um die Positionierung von Formen die darin verwendet werden zu steuern.

## Skripten


**Siehe auch:**

[FreeCAD Skripten Grundlagen](FreeCAD_Scripting_Basics/de.md), und [gesKriptete Objekte](scripted_objects/de.md).

Siehe [Part Formelement](Part_Feature/de.md) für allgemeine Informationen zum Hinzufügen von Objekten zu einem Dokument.

Ein PartDesign Körper wird mit der Methode `addObject()` des Dokuments erstellt. Sobald ein Körper existiert, können [PartDesign Formelemente](PartDesign_Feature.md) mit der `addObject()`- oder der `addObjects()`-Methode dieses Körpers hinzugefügt werden.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("PartDesign::Body", "Body")
obj.Label = "Custom label"

feat1 = App.ActiveDocument.addObject("PartDesign::AdditiveBox", "Box")
feat2 = App.ActiveDocument.addObject("PartDesign::AdditiveCylinder", "Cylinder")

obj.addObjects([feat1, feat2])
App.ActiveDocument.recompute()
```

In einem Dokument, das viele Körper hat, kann der [Aktive Status](PartDesign_body/de#Aktiv_status.md) mit der Methode `setzeAktivesObjekt` der {`AktiveAnsicht`} gesetzt werden. Das erste Argument ist die feste Zeichenkette `"pdbody"`, und das zweite Argument ist das Körperobjekt, das aktiviert werden soll. 
```python
import FreeCAD as App
import FreeCADGui as Gui

doc = App.newDocument()
obj1 = App.ActiveDocument.addObject("PartDesign::Body", "Body")
obj2 = App.ActiveDocument.addObject("PartDesign::Body", "Body")

Gui.ActiveDocument.ActiveView.setActiveObject("pdbody", obj1)
App.ActiveDocument.recompute()
```





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Body/de
