---
 GuiCommand:Container|
{{GuiCommand/de
   Name: FEM ConstraintContact
   Name/de: FEM RandbedingungKontakt
   MenuLocation: Modell , Mechanische Randbedingungen und Lasten , Randbedingung Kontakt
   Workbenches: FEM_Workbench/de
   SeeAlso: FEM_ConstraintFixed/de
}}
{{GuiCommandFemInfo/de
   Solvers: CalculiX
}}
---

# FEM ConstraintContact/de



## Beschreibung

Erstellt eine Randbedingung Kontakt zwischen zwei Oberflächen. Anders als im Falle der [RandbedingungVerbinder](FEM_ConstraintTie/de.md) können sich die Flächen trennen und auf einander gleiten (mit oder ohne Reibung) während der Analyse.



## Anwendung

1.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/FEM_ConstraintContact.svg" width=16px> [Randbedingung Kontakt](FEM_ConstraintContact/de.md)** drücken.
    -   Den Menüeintrag **Modell → Mechanische Randbedingungen und Belastungen → <img src="images/FEM_ConstraintContact.svg" width=16px> Randbedingung Kontakt** auswählen.

2.  Die Hauptfläche auswählen. Die erste Schaltfläche **Hinzufügen** drücken. Um eine Fläche aus der Auswahl zu entfernen, wird diese angeklickt und die erste Schaltfläche **Entfernen** gedrückt.

3.  Die untergeordnete Fläche auswählen. Die zweit Schaltfläche **Hinzufügen** drücken. Um eine Fläche aus der Auswahl zu entfernen, wird diese angeklickt und die zweite Schaltfläche **Entfernen** gedrückt.

4.  Wahlweise eine Kontaktsteifigkeit eingeben.

5.  
    {{Version/de|1.0}}: Wahlweise eine Abstandskorrektur (clearance adjustment) eingeben. Alle Knoten der untergeordneten Fläche, deren Abstand zur Hauptfläche kleiner oder gleich diesem Wert ist, werden zu Beginn der Analyse so verschoben, dass sie auf der Hauptfläche liegen. Diese Anpassung erzeugt keine (zusätzliche) Belastung.

6.  
    {{Version/de|1.0}}: Wahlweise die Checkbox *Reibung aktivieren* aktivieren, um Reibbeiwert und Haftreibungswinkel (stick slope value) zu aktivieren.

7.  Wahlweise einen Reibbeiwert eingeben. Der Standardwert 0 ergibt einen reibungsfreien Kontakt.

8.  
    {{Version/de|1.0}}: Wahlweise einen Haftreibungswinkel eingeben. Er entspricht der Kontaktsteifigkeit unter Reibungsbedingungen. Er legt die Steigung des linearen Zusammenhangs zwischen Schubspannung und relativer tangentialer Verschiebung im Haftreibungsbereich fest (bevor Gleiten einsetzt).



## Einschränkungen

-   Die Kontaktzwangsbedingung kann nur auf zwei Flächen angewendet werden.
-   Entwicklung für mehrere Kontakte auf einmal: <https://forum.freecadweb.org/viewtopic.php?f=18&t=15699&start=130#p303275>
-   Da mehrere Netze derzeit nicht unterstützt werden, muss der Kontakt auf Flächen angewendet werden, die (zumindest) durch einen kleinen Abstand voneinander getrennt sind. Wenn sich die Flächen berühren würden (keine Lücke zwischen ihnen), wäre das Ergebnis einer booleschen Vereinigungs- oder booleschen Fragmentierungs-Operation (notwendig, um zu vermeiden, dass mehrere Maschen entstehen, was derzeit nicht erlaubt ist) ein durchgehendes Netz und somit keine Notwendigkeit mehr, Kontakt zu verwenden. Siehe [Forum Diskussion](https://forum.freecadweb.org/viewtopic.php?f=18&t=62307).



## Hinweise



### Tipps für die Modellierung 

-   Von: <https://forum.freecadweb.org/viewtopic.php?f=18&p=340874#p340494>
-   Die Verwendung von linearen Elementen wird empfohlen. Andernfalls können die Berechnungen sehr zeitaufwendig sein.
-   Master/Slave-Zuordnung:
-   Die größere der beiden Flächen sollte als Masterfläche fungieren.
-   Sind die Flächen vergleichbar groß, sollte die Fläche des steiferen Körpers als Masterfläche fungieren.
-   Bei vergleichbarer Größe und Steifigkeit der Flächen sollte die Fläche mit dem gröberen Netz als Masterfläche fungieren.



### CalculiX

-   Die Kontaktsteifigkeit kann auf das 5 bis 50-fache des Elastizitätsmoduls des Materials geschätzt werden. Je höher der Wert für die Kontaktsteifigkeit ist, desto härter ist der Kontakt zwischen den Oberflächen.
-   Die Slave-Fläche ist die Fläche, die in die Master-Fläche eindringt und daher eine größere Verformung erfährt.
-   CalculiX verwendet für die Modellierung von Kontakt CONTACT PAIR. Die Zwangsbedingung verwendet den Face-to-Face-Strafkontakt, dieser wird ausführlich erklärt unter <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node112.html>
-   Übersicht über die verschiedenen Kontakttypen: <https://forum.freecadweb.org/viewtopic.php?f=18&t=15699&start=90#p188736>

 Weitere interessante Informationen:

-   <https://forum.freecadweb.org/viewtopic.php?f=18&t=23102#p180709> und folgende Beiträge !!!
-   <https://forum.freecadweb.org/viewtopic.php?f=18&t=20276>
-   <https://forum.freecadweb.org/viewtopic.php?f=18&t=21331>
-   <https://forum.freecadweb.org/viewtopic.php?f=18&t=15699> (Thema Erstkontakt)

-   Ein sehr detailliertes CalculiX-Kontaktbeispiel. ([link](http://dip28p.web.fc2.com/calculix/netgen2calculix/index.html))

-   Ein interessantes Beispiel, das im deutschen FreeCAD-Unterforum gefunden wurde. ([link](https://forum.freecadweb.org/viewtopic.php?f=13&t=39663&start=10#p337254))





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintContact/de
