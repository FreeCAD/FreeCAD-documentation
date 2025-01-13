---
 TutorialInfo:e
   Topic: Finite-Elemente-Analyse
   Level: Beginner
   Time: 10 minutes
   Author: http://www.freecadweb.org/wiki/index.php?title=User:Berndhahnebach Bernd
   FCVersion: 0.16.6377 or above
---

# FEM CalculiX Cantilever 3D/de







## Einleitung

Dieses Beispiel soll zeigen, wie eine einfache Finite Elemente Analyse (**FEA**) in FreeCAD\'s [Arbeitsbereich FEM](FEM_Workbench/de.md) im FreeCAD Interface aussieht und wie die Ergebnisse visualisiert werden können. Es wird gezeigt, wie man eine FEA auslöst und wie man den Lastwert und die Lastrichtung ändert. Da die Beispieldatei mit jeder FreeCAD-Installation mitgeliefert wird, ist sie außerdem ein nützlicher und einfacher Test, um festzustellen, ob die FEM-Workbench richtig eingerichtet ist.

<img alt="" src=images/FEM_example01_pic10.png  style="width:700px;">



## Voraussetzungen

-   Eine kompatible Version von FreeCAD, die in der Übersicht des Tutorials angegeben ist.

    :   Verwenden Sie den **Help → About FreeCAD**, um die installierte Version von FreeCAD zu sehen.
-   Für das Laden der Beispieldatei, das Betrachten des Netzes und der Geometrie sowie für die Visualisierung der Ergebnisse wird keine externe Software benötigt.
-   Für die Durchführung der FEA muss die Solver-Software CalculiX auf Ihrem Computer installiert sein. Wahrscheinlich ist der Solver bereits zusammen mit FreeCAD installiert worden. Falls der Solver CalculiX nicht installiert ist, siehe [FEM Installation](FEM_Install/de.md).



## Beispieldatei vorbereiten 



### Beispieldatei laden 

-   FreeCAD starten.
-   Ist der Arbeitsbereich Start nicht aktiviert, sollte er geladen und die Startseite geöffnet werden.
-   Das Beispiel \"FemCalculixCantilever3D.FcStd\" öffnen.

<img alt="" src=images/FEM_example01_pic11.png  style="width:700px;">



### Analyse-Container aktivieren 

-   Um mit einer Analyse arbeiten zu können, muss diese aktiviert sein.
-   In der [Baumansicht](Tree_view/de.md), Doppelklick auf den <img alt="" src=images/FEM_Analysis.svg  style="width:24px;"> **Analyse**,
-   oder Rechtsklick auf das <img alt="" src=images/FEM_Analysis.svg  style="width:24px;"> **Analyse** und wählen Sie **Analyse aktivieren**.

<img alt="" src=images/FEM_example01_pic12.png  style="width:700px;">



### Der Analyse-Container und seine Objekte 

-   Wenn die Analyse aktiviert ist, wechselt FreeCAD selbst die aktuelle Workbench auf FEM.
-   Es werden mindestens 5 Objekte benötigt, um eine statische mechanische Analyse durchzuführen.
-   <img alt="" src=images/FEM_Analysis.svg  style="width:24px;"> Analyse-Container

1.  <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:24px;"> ein Solver
2.  <img alt="" src=images/FEM_MaterialSolid.svg  style="width:24px;"> ein Material
3.  <img alt="" src=images/FEM_MaterialSolid.svg  style="width:24px;"> eine feste Randbedingung
4.  <img alt="" src=images/FEM_ConstraintForce.svg  style="width:24px;"> eine Kraftbelastung
5.  <img alt="" src=images/FEM_FEMMesh.svg  style="width:24px;"> ein FEM-Netz

-   In diesem Beispiel sind auch die Ergebnisse <img alt="" src=images/FEM_ResultShow.svg  style="width:24px;"> bereits enthalten.



### Ergebnisse darstellen 

1.  Vergewissern Sie sich, dass die Analyse aktiviert ist.
2.  Vergewissern Sie sich, dass die Analyse noch das Ergebnisobjekt enthält, wenn nicht, laden Sie einfach die Beispieldatei neu.
3.  Doppelklicken Sie auf das Ergebnisobjekt <img alt="" src=images/FEM_ResultShow.svg  style="width:24px;">, oder wählen Sie es aus und klicken Sie auf die <img alt="" src=images/FEM_ResultShow.svg  style="width:24px;"> Schaltfläche [Ergebnis anzeigen](FEM_ResultShow/de.md) in der FEM-Symbolleiste.
4.  Wählen Sie im Aufgabenfenster `z-Verschiebung`. Es zeigt `-86.93 mm` in negativer z-Richtung. Dies ist sinnvoll, da die Kraft auch in negativer z-Richtung wirkt.
5.  Aktivieren Sie das Kontrollkästchen neben dem unteren Schieberegler der Verschiebungsanzeige.
6.  Mit dem Schieberegler kann das Netz verändert werden, um die Verformung auf vereinfachte Weise zu betrachten.
7.  Wählen Sie zwischen den verschiedenen Ergebnistypen, um alle in der GUI verfügbaren Ergebnistypen anzuzeigen.

<img alt="" src=images/FEM_example01_pic13.png  style="width:400px;">



### Ergebnisse entfernen 

1.  Stellen Sie sicher, dass die Analyse aktiviert ist.
2.  Um die Ergebnisse zu entfernen: Wählen Sie in der Symbolleiste die Schaltfläche <img alt="" src=images/FEM_ResultsPurge.svg  style="width:24px;"> Schaltfläche [FEM-Netz löschen](FEM_ResultsPurge/de.md).



### Die FEA durchführen 

-   In der [Baumansicht](Tree_view/de.md) doppelklicken Sie auf das Solverobjekt <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:24px;">.
-   Stellen Sie sicher, dass im [Aufgabenbereich](Task_panel/de.md) des Solverobjekts die statische Analyse ausgewählt ist.
-   Klicken Sie auf **Schreibe .inp Datei** im gleichen Aufgabenfenster. Beobachten Sie das Log-Fenster, bis es \"write completed\" ausgibt.
-   Klicken Sie auf **Run CalculiX**. Da dies eine sehr kleine Analyse ist, sollte die Ausführung weniger als eine Sekunde dauern.
-   Im Textfenster sollte in grüner Schrift \"CalculiX done without error!\" und in der nächsten Zeile \"loading result sets \...\" stehen.
-   Sie haben gerade Ihre erste FEA in FreeCAD beendet, wenn keine Fehlermeldung erscheint.
-   Klicken Sie auf **Schließen** im Aufgabenfenster.
-   Ein neues Ergebnisobjekt sollte erstellt werden. Sie wissen bereits, wie Sie die Ergebnisse visualisieren können.
-   Wenn Sie beim Auslösen der Analyse eine Fehlermeldung no solver binary oder ähnliches erhalten, überprüfen Sie [FEM Installation](FEM_Install/de.md).

<img alt="" src=images/FEM_example01_pic14.png  style="width:400px;">



### FEA auf die schnelle Art durchführen 

-   Wählen Sie in der Baumansicht das Solverobjekt <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:24px;"> der Analyse <img alt="" src=images/FEM_Analysis.svg  style="width:24px;">.
-   Klicken Sie in der Icon-Symbolleiste auf <img alt="" src=images/FEM_SolverRun.svg  style="width:24px;"> [Solver starten](FEM_SolverRun/de.md).
-   Die Calculix-Eingabedatei wird geschrieben, CalculiX wird gestartet und das Ergebnisobjekt sollte erstellt werden.



### Lastrichtung und Lastwert ändern 

-   In der [Baumansicht](Tree_view/de.md) erweitern Sie <img alt="" src=images/FEM_ResultShow.svg  style="width:24px;"> CCX_Results und wählen Sie das <img alt="" src=images/FEM_MeshResult.svg  style="width:24px;"> ResultMesh-Objekt und drücken Sie die **Space**-Taste.
    -   **Ergebnis:** Die Sichtbarkeit des FEM-Netzes wird ausgeschaltet. Das geometrische Modell ist weiterhin sichtbar.
-   In der [Baumansicht](Tree_view/de.md) doppelklicken Sie auf das <img alt="" src=images/FEM_ConstraintForce.svg  style="width:24px;"> FEMConstraintForce-Objekt, um dessen [Aufgabenbereich](Task_panel/de.md) zu öffnen.
-   Im Aufgabenfenster ändern Sie den Lastwert auf **500000000 N = 500 MN** (**Hinweis:** Krafteinheit im Aufgabenfenster muss in N sein)
-   Klicken Sie auf dem geometrischen Modell auf eine der langen Kanten in x-Richtung.
-   Klicken Sie auf die Schaltfläche **Richtung**.
    -   **Ergebnis:** Die roten Pfeile, die die Kraft darstellen, ändern ihre Richtung in x-Richtung. Sie zeigen die Richtung der Kraft an.
-   Da auf die Box eine Zugkraft wirken soll, muss die Umkehrung der Richtung durch Anklicken ausgelöst werden.
-   Die roten Pfeile der Kraft ändern ihre Richtung.
-   Klicken Sie auf **OK** im Aufgabenfenster.

<img alt="" src=images/FEM_example01_pic15.png  style="width:700px;">

-   Sie wissen bereits, wie man eine Analyse auslöst und wie man die Ergebnisse visualisiert.
-   Die Verformung in x-Richtung sollte 18,95 mm betragen.

<img alt="" src=images/FEM_example01_pic16.png  style="width:400px;">



## Wie geht es weiter? 

-   Wir sind nun mit dem grundlegenden Arbeitsablauf für die [Arbeitsbereich FEM](FEM_Workbench/de.md) fertig.
-   Sie sind nun bereit, das zweite [FEM-Tutorial](FEM_tutorial/de.md) zu bearbeiten.
-   Wir werden den CalculiX-Kragarm selbst erzeugen und die Ergebnisse mit der Balkentheorie vergleichen.


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM CalculiX Cantilever 3D/de
