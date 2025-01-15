---
 GuiCommand:Container|
{{GuiCommand/de
   Name: FEM ConstraintTie
   Name/de: FEM RandbedingungVerbinder
   MenuLocation: Modell , Mechanische Randbedingungen und Belastungen , Randbedingung Verbinder
   Workbenches: FEM_Workbench/de
   Version: 0.19
   SeeAlso: FEM_ConstraintPressure/de
}}
{{GuiCommandFemInfo/de
   Solvers: CalculiX
}}
---

# FEM ConstraintTie/de



## Beschreibung

Legt eine Randbedingung Verbinder fest, die zwei ausgewählte Flächen in einer Weise verbindet, dass sie (anders als ein Kontakt funktioniert) während der Analyse nicht getrennt werden können und nicht aufeinander gleiten können. So bleiben die Flächen dauerhaft untrennbar verbunden.


{{Version/de|1.0}}

: Kann auch zum Festlegen von zyklischer Symmetrie verwendet werden.



## Anwendung

1.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/FEM_ConstraintTie.svg" width=16px> [Randbedingung Verbinder](FEM_ConstraintTie/de.md)** drücken.
    -   Den Menüeintrag **Modell → Mechanische Randbedingungen und Belastungen → <img src="images/FEM_ConstraintTie.svg" width=16px> Randbedingung Verbinder** auswählen.

2.  Die Schaltfläche **Hinzufügen** im Aufgaben-Bereich drücken und dann die Fläche anklicken, die der Randbedingung Verbinder zugeordnet werden soll. Nacheinander genau zwei Flächen auswählen. Die zuerst ausgewählte Fläche ist die untergeordnete Fläche, während die zweite die Hauptfläche ist.

3.  Wahlweise die Toleranz festlegen - Die Randbedingung Verbinder wird nur auf Knoten der untergeordneten Fläche angewendet, die zur Hauptfläche einen Abstand haben, der nicht größer ist, als der hier angegebene.

4.  
    {{Version/de|1.0}}: Wahlweise die Checkbox *Enable Adjust* aktivieren, um den Knoten der untergeordneten Fläche zu erlauben, automatisch bewegt und auf die Hauptfläche gelegt zu werden, wenn sie von der Randbedingung betroffen sind (d.h. dass sie dem Toleranzkriterium entsprechen).



## Zyklische Symmetrie 


{{Version/de|1.0}}

: Die Randbedingung Verbinder kann auch zum festlegen zyklischer Symmetrie verwendet werden Dies ermöglicht Modelle, die periodische Drehsymmetrie aufweisen (eine sich wiederholende Abfolge kreisförmig um eine Symmetrieachse herum angeordnet), mit nur einem repräsentativen Sektor zu analysieren. Dies kann teilweise nützlich sein für Rotoren, Wellen, Turbinen, Propeller, Schwungräder und ähnliche Bauteile, oft auch in Kombination mit [zentrifugaler Last](FEM_ConstraintCentrif/de.md) (Auch die Belastung muss diese Form von Symmetrie aufweisen). Zyklische Symmetrie kann durch Auswahl der zwei Flächen des Abschnitts für die Randbedingung Verbinder und die Angabe folgender Eigenschaften erfolgen:

-    {{PropertyData/de|Cyclic Symmetry}}: Auf *true* gesetzt aktiviert sie die zyklische Symmetrie.

-    {{PropertyData/de|Sectors}}: Gesamtanzahl der Sektoren; ist gleich 360° geteilt durch den Winkel des repräsentativen Sektors (z.B. 8 für einen 45°-Sector oder 6 für einen 60°-Sektor)

-    {{PropertyData/de|Connected Sectors}}: Anzahl der Sektoren, die in den Ergebnissen dargestellt werden. Zum Darstellen des ganzen 360°-Bauteils wird hier dieselbe Anzahl wie in der {{PropertyData/de|Sectors}} eingegeben.

-    {{PropertyData/de|Symmetry Axis}}\- Achse der zyklischen Symmetrie - Standrdmäßig die globale Z-Achse. Kann durch Anwenden einer Positionierung (Placement transformation) auf den Z-Versor (Vektor?) bewegt werden. (Ähnlich zu dem, was mit [Part-Linien](Part_Line/de.md) gemacht werden kann - Um zu verstehen, wie die Symmetrieachse bewegt wird, kann es tatsächlich hilfreich sein, die Positionierung der Part-Linie zu ändern, was normalerweise für die zentrifugale Last auch erforderlich ist). Eine wichtige Einschränkung dieser Funktion in FEM ist, dass Randbedingungen nicht auf die Knoten der abhängigen Oberflächen zyklischer Symmetrie angewendet werden können (abhängige Oberflächen in der Definition der Randbedingung Verbinder) da dies eine Überbestimmung ergäbe. Daher kann es in einigen Fällen nötig sein, die Knoten aus der Definition der Randbedingung zu entfernen, die sich auf der Kante zwischen der Oberfläche mit der Randbedingung und der von der zyklischen Symmetrie abhängigen Oberfläche befinden. Leider verarbeitet FreeCAD keine Knotenmengen (node sets) und einzelne Knoten können nicht abgewählt werden; daher müssen Übergangslösungen verwendet werden, wie das Hinzufügen einer begrenzenden [Teilfläche](FEM_Geometry_Preparation_and_Meshing/de#Geometrie_partitionieren.md) als Übergang zwischen der abhängigen Oberfläche und der Oberfläche mit der Randbedingung.



## Hinweise

-   Diese Funktion verwendet die [TIE-Karte in CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node251.html).

-    {{Version/de|1.0}}: Zyklische Symmetrie verwendet auch die [CYCLIC-SYMMETRY-MODEL-Karte in CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node183.html).





{{FEM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintTie/de
