---
- GuiCommand:
   Name:PartDesign NewSketch
   Name/de:PartDesign NeueSkizze
   MenuLocation:Skizze - Skizze erstellen
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   Version:0.17
   SeeAlso:[Sketcher NeueSkizze](Sketcher_NewSketch/de.md)
---

# PartDesign NewSketch/de



## Beschreibung

Dieses Werkzeug erstellt eine neue Skizze und, falls es noch keinen gibt, einen neuen [PartDesign-Körper](PartDesign_Body/de.md), der die Skizze enthält. Anschließend wird der Arbeitsbereich [Sketcher](Sketcher_Workbench/de.md) automatisch geöffnet.

Werden Modelle unter Verwendung des Arbeitsbereichs [PartDesign](PartDesign_Workbench/de.md) erstellt, sollte dieses Werkzeug den Vorzug vor dem Werkzeug **[<img src=images/Sketcher_NewSketch.svg style="width:16px">[Sketcher NeueSkizze](Sketcher_NewSketch/de.md)** des Arbeitsbereichs [Sketcher](Sketcher_Workbench/de.md) bekommen.



## Anwendung

1.  Die **[<img src=images/PartDesign_NewSketch.svg style="width:24px">** Schaltfläche in der PartDesign Werkzeugleiste klicken.

2.  Im Aufgabenreiter wird der **Element auswählen**-Diaglog angezeigt. Hier kann eine der Ebenen oder die 3D-Ansicht, die für eine besser Sichtbarkeit anders ausgerichtet werden kann, gewählt werden.

3.  
    **OK**klicken.

4.  Die Oberfläche schaltet automatisch zum Skizzierer und die Skizze kann bearbeitet werden. Nach dem Verlassen des Skizzierers springt die Oberfläche automatisch in den PartDesign Arbeitsbereich und die 3D-Ansicht wird in die Ansicht zurückgestellt, wie sie vor dem Erstellen der Skizze war.

5.  Es kann auch eine Ebene oder eine Oberfläche eines existierenden Körpers gewählt werden, bevor eine Skizze erstellt wird. In diesem Fall wird die Skizze sofort erstellt.



## Optionen

-   Um die Zuordnung einer existierenden Skizze zu ändern, muss ihre Eigenschaft **Map Mode** geändert werden. (siehe [Eigenschaften](#Eigenschaften.md))

-   Der Dialog *Element auswählen* legt die Elemente der neuen Skizze fest

:   

    :   <img alt="" src=images/PartDesign.CreateSketch.SelectFeatureDialog.jpeg  style="width:300px;">
    :   Dialog *Element auswählen*. Diese Einstellungen erstellen eine Skizze auf der XY-Ebene und lassen die Verwendung von Querverweisen anderer Elemente desselben Körpers

Dialog-Einstellungen

-   Koordinatensystemkasten: definiert die Ausrichtung der Skizzierebene
-   Kontrollkästchen *Verwendete Funktionen Zulassen*: *ZuTun*

:   Optionen für externe Funktionen zulassen

-   Von anderen Körpern desselben Teils: alle im selben Körper verwendeten Elemente können referenziert werden
-   Von anderen Teilen oder freien Features: *TBD*
-   Unabhängige Kopie erstellen: alle anderen Elemente werden separate Kopien sein, d.h. sie werden sich nicht ändern, wenn sich das Original ändert.
-   Abhängige Kopie erstellen: die Elemente werden Kopien sein, aber eine Abhängigkeit zu den Originalelementen wird beibehalten. Dies ist im Grunde die Verwendung eines [Formbinder](PartDesign_ShapeBinder/de.md)
-   Querverweis erstellen: Die verknüpften Elemente sind keine Kopien, sondern verweisen auf die Originalelemente, z. B. eine Masterskizze. Alle Änderungen werden auf diese Skizze übertragen

Um beliebige Elemente im [Sketcher](Sketcher_Workbench/de.md) zu referenzieren, können die beiden Werkzeuge **<img src="images/Sketcher_External.svg" width=16px> [ExterneGeometrie](Sketcher_External/de.md)** und **[<img src=images/Sketcher_CarbonCopy.svg style="width:16px"> [Pause](Sketcher_CarbonCopy/de.md)** verwendet werden. Generell ist es empfehlenswert, andere Skizzen als Quelle für Referenzen zu verwenden, anstatt Flächen oder Kanten, da diese weniger von dem Problem der topologischen Benennung betroffen sind.



## Eigenschaften

-    {{PropertyData/de|Map Mode}}(Abbildungsmodus): Art der Befestigung der Skizze an einem anderen Objekt, normalerweise einer Ebene oder Fläche. Es können aber auch andere Objekttypen sein. Einmal in das Feld klicken, um eine Schaltfläche **...** anzuzeigen und sie dann anzuklicken, um den Dialog [Befestigen](Part_EditAttachment/de.md) zu öffnen. Wenn die Option *deaktiviert* ausgewählt ist, dann ist die Eigenschaft Positionierung aktiviert.

-    {{PropertyData/de|Positonierung}}: Steuert die Ausrichtung der Skizze im 3D-Raum; siehe [Positionierung](Std_Placement/de.md). Diese ist gesperrt, wenn die Skizze über die Eigenschaft \"Map Mode\" angehängt wurde.








{{PartDesign Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign NewSketch/de
