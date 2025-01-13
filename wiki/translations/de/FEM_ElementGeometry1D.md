---
 GuiCommand:Container|
{{GuiCommand/de
   Name: FEM ElementGeometry1D
   Name/de: FEM ElementGeometrie1D
   MenuLocation: Modell , Element-Geometrie , Stabquerschnitt
   Workbenches: FEM_Workbench/de
   Shortcut: **C** **B**
   SeeAlso: FEM_tutorial/de
}}
{{GuiCommandFemInfo/de
   Solvers: CalculiX, Mystran, Z88
}}
---

# FEM ElementGeometry1D/de



## Beschreibung

**ElementGeometrie1D** wird zur Festlegung der Querschnitte (BeamCrossSection-Objekte) von Stabelementen (Träger, Balken, Säulen usw.) verwendet. Derzeit sind folgende drei Querschnittformen vorhanden: Rechteck, Kreis und Ring.


{{VersionPlus/de|1.1}}

: Box und elliptischer Querschnitt stehen auch zur Verfügung.



## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/FEM_ElementGeometry1D.svg" width=16px> [Stabquerschnitt](FEM_ElementGeometry1D/de.md)** drücken.
    -   Den Menüeintrag **Modell → Element-Geometrie → <img src="images/FEM_ElementGeometry1D.svg" width=16px> Stabquerschnitt** auswählen.
2.  Die Art des Querschnitts auswählen und die erforderlichen Abmaße eingeben:
    -   Rectangular (Rechtwinklig): Breite und Höhe.

    -   Circular (Kreis): Durchmesser.

    -   Pipe (Ring): Außendurchmesser und Wandstärke,

    -   
        {{VersionPlus/de|1.1}}
        
        : Elliptical (Elliptisch): axis 1 length und axis 2 length,

    -   
        {{VersionPlus/de|1.1}}
        
        : Box: Höhe, Breite, Wandstärken T1 - T4.
3.  Wahlweise die Schaltfläche **Hinzufügen** im Aufgabenbereich drücken und anschließend die Kante anklicken, die einen festgelegten Querschnitt erhalten soll. Ist die Auswahl leer, werden alle verbleibenden Kanten (deren Querschnitte nicht durch andere [ElementGeometrie1D](FEM_ElementGeometry1D/de.md)-Objekte festgelegt sind) automatisch zugeordnet.



## Eigenschaften

-    {{PropertyData/de|Section Type}}: Legt die Art des Balkenquerschnitts fest (*Rectangular* (rechteckig), *Circular* (Kreisförmig), *Pipe* (Röhre), {{VersionPlus/de|1.1}}: *Elliptical* (Elliptisch) und *Box*).

-    {{VersionPlus/de|1.1}}: {{PropertyData/de|Box Height}}: Höhe des Box-Querschnitts, wird verwendet, wenn die {{PropertyData/de|Section Type}} *Box* ausgewählt ist.

-    {{VersionPlus/de|1.1}}: {{PropertyData/de|Box T1}}: Wandstärke T1 des Box-Querschnitts, wird verwendet, wenn die {{PropertyData/de|Section Type}} *Box* ausgewählt ist.

-    {{VersionPlus/de|1.1}}: {{PropertyData/de|Box T2}}: Wandstärke T2 des Box-Querschnitts, wird verwendet, wenn die {{PropertyData/de|Section Type}} *Box* ausgewählt ist.

-    {{VersionPlus/de|1.1}}: {{PropertyData/de|Box T3}}: Wandstärke T3 des Box-Querschnitts, wird verwendet, wenn die {{PropertyData/de|Section Type}} *Box* ausgewählt ist.

-    {{VersionPlus/de|1.1}}: {{PropertyData/de|Box T4}}: Wandstärke T4 des Box-Querschnitts, wird verwendet, wenn die {{PropertyData/de|Section Type}} *Box* ausgewählt ist.

-    {{VersionPlus/de|1.1}}: {{PropertyData/de|Box Width}}: Breite des Box-Querschnitts, wird verwendet, wenn die {{PropertyData/de|Section Type}} *Box* Länge der Achse 1 eines elliptischen Querschnitts, wird verwendet, wenn die

-    {{PropertyData/de|Circ Diameter}}: Durchmesser des kreisförmigen Querschnitts; wird verwendet, wenn die {{PropertyData/de|Section Type}} *Circular* ausgewählt ist.

-    {{VersionPlus/de|1.1}}: {{PropertyData/de|Axis 1 Length}}: Länge der Achse 1 eines elliptischen Querschnitts, wird verwendet, wenn die {{PropertyData/de|Section Type}} *Elliptical* ausgewählt ist.

-    {{VersionPlus/de|1.1}}: {{PropertyData/de|Axis 2 Length}}: Länge der Achse 2 eines elliptischen Querschnitts, wird verwendet, wenn die {{PropertyData/de|Section Type}} *Elliptical* ausgewählt ist.

-    {{PropertyData/de|Pipe Diameter}}: Außendurchmesser des Röhrenquerschnitts; wird verwendet, wenn die {{PropertyData/de|Section Type}} *Pipe* ausgewählt ist.

-    {{PropertyData/de|Pipe Thickness}}: Wandstärke des Röhrenquerschnitts; wird verwendet, wenn die {{PropertyData/de|Section Type}} *Pipe* ausgewählt ist.

-    {{PropertyData/de|Rect Height}}: Höhe des Rechteckquerschnitts; wird verwendet, wenn die {{PropertyData/de|Section Type}} *Rectangular* ausgewählt ist.

-    {{PropertyData/de|Rect Width}}: Breite des Rechteckquerschnitts; wird verwendet, wenn die {{PropertyData/de|Section Type}} *Rectangular* ausgewählt ist.



## Einschränkungen

-    {{VersionMinus/de|1.0}}: Andere Arten von Querschnitten, die in CalculiX zur Verfügung stehen, (elliptical, box und general) werden zurzeit nicht unterstützt. Man kann die Input-Datei bearbeiten, um sie zu verwenden.

-    {{VersionPlus/de|1.1}}: Der Balkenquerschnitt general wird derzeit nicht unterstützt. Man kann die Eingabedatei bearbeiten, um ihn zu verwenden.



## Hinweise

-   Um die Ergebnisse sehen zu können, die der CalculiX-Löser aus dem Netz ableitet, das auf dem vorgegebenen Querschnitt basiert, muss die Eigenschaft `Beam Shell Result Output 3D` des [FEM LöserCalculixCxxtools](FEM_SolverCalculixCxxtools/de.md)-Objekts auf `True` gesetzt werden.
-   Einige Querschnitte erfordern bestimmte Elementarten:
    -   Kreisquerschnitt - Elemente zweiter Ordnung

    -   Ringquerschnitt - Elemente zweiter Ordnung mit verringerter Vernetzung ({{Version/de|1.0}}: Verringerte Vernetzung ist für Stabelemente standardmäßig aktiviert und kann mit der Eigenschaft *Beam Reduced Integration* des Lösers [CalculiX](FEM_SolverCalculixCxxtools/de.md) umgeschaltet werden.)

    -   
        {{VersionPlus/de|1.1}}
        
        : elliptischer Querschnitt - Elemente zweiter Ordnung

    -   
        {{VersionPlus/de|1.1}}
        
        : Box-Querschnitt - Elemente zweiter Ordnung mit verringerter Vernetzung (wie oben erklärt).
-   Diese Funktion verwendet die [\*BEAM SECTION-Karte in CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node162.html).





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ElementGeometry1D/de
