---
 GuiCommand:Container|
{{GuiCommand/de
   Name: FEM ConstraintRigidBody
   Name/de: FEM RandbedingungStarrerKörper
   MenuLocation: Modell , Mechanische Randbedingungen und Belastungen , Randbedingung starrer Körper
   Workbenches: FEM_Workbench/de
   Version: 1.0
   SeeAlso: FEM_ConstraintDisplacement/de
}}
{{GuiCommandFemInfo/de
   Solvers: CalculiX
}}
---

# FEM ConstraintRigidBody/de



## Beschreibung

Definiert die Starrkörperbeschränkung von CalculiX, die die Bewegung der Knoten eines ausgewählten geometrischen Objekts an die Bewegung eines Referenzknotens bindet, dessen Position vom Benutzer definiert wird. In der Praxis kann dies verwendet werden, um eine Randbedingung oder Last anzuwenden, die auf das ausgewählte Objekt übertragen wird. Da der Referenzknoten über rotatorische Freiheitsgrade verfügt, ist es möglich, auf diese Weise eine Momentbelastung oder eine rotatorische Randbedingung auf jede Fläche anzuwenden. Die Position des Referenzknotens kann ausgewählt werden. Wenn er von einem geometrischen Objekt versetzt ist, kann eine Fernlast (eine Kraft, die auf einen Hebel wirkt) angewendet werden.



## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Drücken Sie den **<img src="images/FEM_ConstraintRigidBody.svg" width=16px> [Rigid body constraint](FEM_ConstraintRigidBody.md)** Schaltfläche.
    -   Wählen Sie den **Model → Mechanical boundary conditions and loads → <img src="images/FEM_ConstraintRigidBody.svg" width=16px> Rigid body constraint** aus dem Menü wählen.
2.  Drücken Sie die Schaltfläche **Hinzufügen**.
3.  Wählen Sie in der [3D-Ansicht](3D_view/de.md) das/die geometrische(n) Element(e) (Eckpunkte, Kanten oder Flächen, aber nicht eine Mischung davon), auf das/die die Zwangsbedingung angewendet werden soll. Um Objekte aus der Auswahl zu entfernen, drücken Sie die Schaltfläche **Entfernen** und klicken Sie auf sie.
4.  Geben Sie die Koordinaten des Referenzknotens an. Nach dem Schließen des Aufgabenfensters zeigt ein kugelförmiges Symbol diese Position an.
5.  Wählen Sie die Modi für die 3 translatorischen und 3 rotatorischen Freiheitsgrade (DOFs):
    -   *Frei* - Standard, keine Randbedingung oder Last auf diesem DOF
    -   *Constraint* - Verschiebungs-/Rotations-Randbedingung mit einem bestimmten Wert (Standard: 0 = fest) für diesen DOF - für Rotation muss man eine Achse (X, Y oder Z) und den *Winkel* angeben
    -   *Last* - Kraft-/Momentbelastung mit einem bestimmten Wert für diese DOF



## Einschränkungen

-   Derzeit können die Momenteinheiten etwas verwirrend sein. Um 1 N\*m anzuwenden, muss man 1 J in das Eingabefeld eingeben (diese Einheiten sind gleichwertig).
-   Die Funktion kann vorerst nur auf Eckpunkte, Kanten und Flächen angewendet werden, die Unterstützung für Volumenkörper (um ganze Volumen/Teile starr zu machen) sollte in Zukunft folgen.
-   Das ausgewählte Objekt wird starr gemacht. Um Lasten auf eine flexiblere Weise anzuwenden, müsste man die verteilenden Kopplungsbeschränkungen von CalculiX verwenden, die derzeit nicht unterstützt werden.



## Hinweise

-   Diese Zwangsbedingung ist die Standardmethode, um ein Drehmoment auf beliebige Teile anzuwenden. Die anderen Optionen sind die [Lokales Koordinatensystem](FEM_ConstraintTransform/de.md) (nur für zylindrische Flächen) oder ein Paar von Kräften, aber die Starrkörperbindung sollte in so gut wie allen Fällen ausreichend sein.
-   Auf die Knoten, die an einer Starrkörperbindung beteiligt sind, sollten keine anderen Bindungen/Begrenzungsbedingungen angewendet werden.
-   Wenn man diese Zwangsbedingung auf einen Scheitelpunkt oder eine Kante anwendet, sollte man eine geeignete Rotations-DOF (im Falle einer Kante diejenige, die die Rotation um sie verhindert) auf Null setzen.
-   Diese Funktion verwendet die [\*RIGID BODY card in CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node236.html).





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintRigidBody/de
