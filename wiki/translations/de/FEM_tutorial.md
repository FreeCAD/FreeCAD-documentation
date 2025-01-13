---
 TutorialInfo:e
   Topic:  Finite-Elemente-Analyse
   Level:  Anfänger
   Time:  10 Minuten + Löserzeit
   Author: http://freecadweb.org/wiki/index.php?title=User:Drei Drei
   FCVersion: 0.17 oder höher
---

# FEM tutorial/de







## Einleitung

Dieses Tutorium soll dem Leser den grundlegenden Arbeitsablauf des Arbeitsbereichs FEM sowie die meisten Werkzeuge vorstellen, die zur Durchführung einer statischen Analyse zur Verfügung stehen.

<img alt="" src=images/FEM_tutorial_result.png  style="width:600px;">



## Voraussetzungen

-   FreeCAD Version 0.17 oder höher.
-   [Netgen](http://sourceforge.net/projects/netgen-mesher/) und/oder [GMSH](http://geuz.org/gmsh/) ist auf dem System installiert (in der FreeCAD-Installation enthalten).
-   [Calculix](http://www.calculix.de/) ist auf dem System installiert (in der FreeCAD-Installation enthalten).
-   Der Leser verfügt über Grundkenntnisse in der Anwendung der Arbeitsbereiche [Part](Part_Workbench/de.md) und [PartDesign](PartDesign_Workbench/de.md).



## Ablauf



### Modellieren

In diesem Beispiel wird ein Würfel als Studienobjekt verwendet, aber stattdessen kann auch jedes andere Modell verwendet werden, das in den Arbeitsbereichen Part oder PartDesign erstellt wurde.

1.  Die Schaltfläche **![](images/)_[Std_Neu](Std_New/de.md)** drücken, um ein neues Dokument zu erstellen.
2.  Den Arbeitsbereich <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench.md) aktivieren.
3.  Einen Würfel erstellen.
4.  Seine **Abmessungen** wie folgt ändern:
    1.  Länge: 8.000 m.
    2.  Breite: 1.000 m.
    3.  Höhe: 1.000 m.

Wir haben nun ein Modell, mit dem wir arbeiten können.



### Analyse erstellen 

1.  Den Arbeitsbereich <img alt="" src=images/Workbench_FEM.svg  style="width:24px;"> [FEM](FEM_Workbench.md) aktivieren.
2.  Den Menüeintrag **Modell → <img src="images/FEM_Analysis.svg" width=16px> Analyse-Container‏‎** auswählen.



### Randbedingungen und Kräfte 

1.  Das Netz in der Baumansicht ausblenden.
2.  Das Originalmodell anzeigen.
3.  <img alt="" src=images/FEM_ConstraintFixed.svg  style="width:24px;"> [Randbedingung Festsetzen](FEM_ConstraintFixed/de.md) auswählen.
4.  Auf die Schaltfläche **Hinzufügen** klicken, die Rückseite des Würfelobjekts (die Fläche auf der YZ-Ebene) auswählen und **OK** drücken.
5.  <img alt="" src=images/FEM_ConstraintForce.svg  style="width:24px;"> [Randbedingung Krafteinwirkung](FEM_ConstraintForce/de.md) auswählen.
6.  Auf die Schaltfläche **Hinzufügen** klicken, die Vorderseite des Würfelobjekts (die zur Rückseite parallel liegende Fläche) und den Wert für **Force \[N\]** (Flächenlast in N) auf 9000000 setzen.
7.  **Direction** (Richtung) auf **-Z** setzen durch Auswahl einer der Flächenkanten, die parallel zu dieser Richtung liegen.
8.  Auf **OK** klicken.

Wir haben jetzt die Lagerstellen und Kräfte für unsere statische Studie festgelegt.



### Material

1.  <img alt="" src=images/FEM_MaterialSolid.svg  style="width:24px;"> [Material für Feststoffe](FEM_MaterialSolid/de.md) auswählen und Calculix-Steel als Material auswählen.
2.  Auf **OK** klicken.



### Netzerstellung

Es wird empfohlen, das Erstellen eines Netzes als letzten Schritt der Analysevorbereitung auszuführen, da dies im Zusammenhang mit einer Geometrie in FreeCAD steht. Abhängig von der FreeCAD-Installation, können Die Vernetzugswerkzeuge Netgen oder GMSH vorhanden sein; beide können verwendet werden.



#### Netgen

1.  Model auswählen.
2.  <img alt="" src=images/FEM_MeshNetgenFromShape.svg  style="width:24px;"> [FEM mesh from shape by Netgen](FEM_MeshNetgenFromShape/de.md): Erstellt mit Hlfe von Netge ein Finite-Elemente-Netz eines Modells.
3.  Im Vernetzungsdialog klickt man auf **Anwenden** und anschließend auf **OK**.

Man kann auch ein Netz auf eine mechanische Anylyse ziehen und ablegen, die noch kein Netz in der [Baumansicht](Tree_view/de.md) enthält.



#### GMSH

1.  Model auswählen.
2.  <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width:24px;"> [FEMGmsh from shape by Gmsh](FEM_MeshGmshFromShape/de.md): Erstellt mit Hlfe von Gmsh ein Finite-Elemente-Netz eines Modells.
3.  Im Vernetzungsdialog klickt man auf **Anwenden** und anschließend auf **OK**.

Wir haben unser Objekt nun vernetzt und sind bereit, Randbedingungen und Kräfte hinzuzufügen.



### Berechnung



#### Standardablauf

1.  Das imAnalyse-Container enthaltene Löser-Objekt <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:24px;"> auswählen.
2.  Den Menüeintrag <img alt="" src=images/FEM_SolverControl.svg  style="width:24px;"> [Solver job control](FEM_SolverControl/de.md) auswählen.
3.  **.inp Datei schreiben** auswählen.
4.  **CalculiX ausführen** auswählen.
5.  Die Schaltfläche **Schließen** drücken.



#### Schneller Ablauf 

1.  Das Löserobjekt <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:24px;"> auswählen, das sich im **Analysis**-Container befindet.
2.  Auf <img alt="" src=images/FEM_SolverRun.svg  style="width:24px;"> [Run solver calculations](FEM_SolverRun/de.md) klicken.



### Ergebnisse analysieren 

1.  Das **CCX_Results**-Objekt im **Objektbaum** auswählen.
2.  <img alt="" src=images/FEM_ResultShow.svg  style="width:24px;"> [Ergebnis anzeigen](FEM_ResultShow/de.md) auswählen.
3.  Einen der verschiedenen Ergebnistypen auswählen, um die Ergebnisse anzuzeigen.
4.  Der Schieberegler am unteren Rand kann verwendet werden, um die Darstellung des Netzes zu ändern. Auf diese Weise können wir die Verformung, die das Objekt erfährt, visualisieren, wobei zu beachten ist, dass es sich hierbei um eine Annäherung handelt.
5.  Um die Ergebnisse zu entfernen, wähle <img alt="" src=images/FEM_ResultsPurge.svg  style="width:24px;"> [Purge results](FEM_ResultsPurge/de.md)


{{Note|Vergleich zur vorherigen Beispieldatei|Wird der Ergebnistyp '''Verschiebung Z''' gewählt, kann man sehen, dass der erhaltene Wert fast identisch mit dem von FreeCAD gelieferten Testbeispiel ist. Unterschiede können aufgrund der Qualität des Netzes und der Anzahl der Knoten, die es besitzt, auftreten.}}

Wir sind nun mit dem grundlegenden Arbeitsablauf für den Arbeitsbereich [FEM](FEM_Workbench/de.md) fertig.



## Hinweise

-   Eine Video-Anleitung, die auf dieser Anleitung basiert: [FEM MaterialReinforced tutorial](https://www.youtube.com/watch?v=SZTIqhfCSVc).


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM tutorial/de
