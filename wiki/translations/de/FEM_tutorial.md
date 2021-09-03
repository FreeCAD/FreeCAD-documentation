


<div class="mw-translate-fuzzy">


{{TutorialInfo/de
|Topic= Finite Element Analyse
|Level= Anfänger
|Time= 10 Minuten + Löserzeit
|Author=[http://freecadweb.org/wiki/index.php?title=User:Drei Drei]
|FCVersion=0.16.6700 oder höher
|Files=
}}


</div>

## Introduction


<div class="mw-translate-fuzzy">

## Einführung

Dieses Tutorium soll den Leser in den grundlegenden Arbeitsablauf des FEM Arbeitsbereichs sowie in die meisten Werkzeuge einführen, die zur Durchführung einer statischen Analyse zur Verfügung stehen.


</div>

<img alt="" src=images/FEM_tutorial_result.png  style="width:600px;">

## Requirements


<div class="mw-translate-fuzzy">

## Anforderungen

-   FreeCAD Version 0.16.6700 oder höher
-   [Netgen](http://sourceforge.net/projects/netgen-mesher/) und/oder [GMSH](http://geuz.org/gmsh/) ist auf dem System installiert
-   Im Falle von GMSH installiere [Makro GMSH](Macro_GMSH/de.md) aus dem [Erweiterungsverwalter](AddonManager/de.md), entwickelt von [psicofil](https://github.com/psicofil/Macros_FreeCAD).
-   [Calculix](http://www.calculix.de/) ist auf dem System installiert
-   Der Leser verfügt über die Grundkenntnisse zur Verwendung der [Part](Part_Workbench/de.md) und [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md)


</div>

## Prozedur

### Modeling


<div class="mw-translate-fuzzy">

### Modellierung

In diesem Beispiel wird ein Würfel als Studienobjekt verwendet, aber stattdessen können auch Modelle verwendet werden, die in den Part oder PartDesign Arbeitsbereichen erstellt wurden.


</div>


<div class="mw-translate-fuzzy">

1.  Erstelle ein neues Dokument
2.  Aktiviere den Formteil Arbeitsbereichs
3.  Erstelle einen Würfel
4.  Ändere seine **Abmessungen** wie folgt:
    1.  Höhe: 1.000 mm
    2.  Länge: 8.000 mm
    3.  Breite: 1.000 mm


</div>

Wir haben nun ein Modell, mit dem wir im Folgenden arbeiten können.

### Creating the Analysis 

#### Netgen


<div class="mw-translate-fuzzy">

### Erstellen der Analyse 

#### Netgen 

1.  Wähle das Modell
2.  Klicke auf <img alt="" src=images/FEM_Analysis.png  style="width:16px;"> [Neue mechanische Analyse](FEM_Analysis/de.md) aus dem Menü, um eine Analyse aus dem ausgewählten Objekt zu erstellen
3.  Klicke im Vernetzungsdialog auf **OK**


</div>


<div class="mw-translate-fuzzy">

Du kannst auch ein Netz auf eine Mechanische Analyse ziehen und ablegen, die kein Netz in der Baumansicht hat.


</div>

#### GMSH


<div class="mw-translate-fuzzy">

#### GMSH 

Die Verwendung des Makros von psicofil wird empfohlen und wird für dieses Beispiel verwendet.

1.  Aktiviere das Makro
2.  Wähle das Objekt aus, das du verwenden möchtest, in diesem Fall unseren Wüprfel
3.  Hake das Kästchen **Mechanische Analyse aus dem Netz erstellen** an
4.  Klicke auf **OK**


</div>

Wir haben unser Objekt nun vernetzt und sind bereit, Beschränkungen und Kräfte hinzuzufügen.

### Constraints and Forces 


<div class="mw-translate-fuzzy">

### Beschränkungen und Kräfte 

1.  Blende das Netz in der Baumansicht aus.
2.  Zeige das Originalmodell
3.  Wähle <img alt="" src=images/FEM_FixedConstraint.png  style="width:16px;"> [Erstelle Feste FEM Beschränkung ](FEM_ConstraintFixed/de.md)
4.  Wähle die Rückseite des Würfels (Fläche auf der **YZ** Achse) und klicke auf OK
5.  Wähle <img alt="" src=images/FEM_ForceConstraint.png  style="width:16px;"> [Erstelle FEM Kraftbeschränkung ](FEM_ConstraintForce/de.md)
6.  Wähle die Vorderseite des Würfels (die Seite parallel zur Rückseite) und setze den Wert **Flächenbelastung** auf 9000000,00
7.  Setze die **Richtung** auf **-Z**, durch Anwahl einer der Flächenkanten parallel zu dieser Richtung.
8.  Klicke auf OK.


</div>

Wir haben jetzt die Beschränkungen und Kräfte für unsere statische Studie festgelegt.

### Final preparations 


<div class="mw-translate-fuzzy">

### Letzte Vorbereitungen 

1.  Wähle <img alt="" src=images/FEM_Material.png  style="width:16px;"> [Mechanisches Material\...](FEM_MaterialSolid/de.md) und wähle als Material Calculix
2.  Klicke **OK**


</div>

### Running the Solver 

#### Standard Procedure 


<div class="mw-translate-fuzzy">

### Ausführen des Lösers 

#### Standardverfahren

1.  Wähle das Löserobjekt <img alt="" src=images/FEM_Solver.png  style="width:16px;">, das in der **Mechanischen Analyse** enthalten ist
2.  Wähle <img alt="" src=images/FEM_Calculation.png  style="width:16px;"> [Berechnung starten](FEM_SolverControl/de.md) aus dem Menü
3.  Wähle **Calculix Eingabedatei schreiben**
4.  Wähle **Run Calculix**
5.  Klicke **Schließen**


</div>

#### Quick Procedure 


<div class="mw-translate-fuzzy">

#### Schnellverfahren

1.  Wähle das Löserobjekt <img alt="" src=images/FEM_Solver.png  style="width:16px;">, das in der *\'Mechanischen Analyse* enthalten ist
2.  Klicke auf <img alt="" src=images/FEM_RunCalculiXccx.png  style="width:16px;"> [Schnellanalyse](FEM_SolverRun/de.md).


</div>

### Analyzing Results 


<div class="mw-translate-fuzzy">

### Ergebnisse analysieren 

1.  Wähle aus dem **Objektbaum** das **Ergebnisse** Objekt
2.  Wähle <img alt="" src=images/FEM_ShowResult.png  style="width:16px;"> [Ergebnis anzeigen](FEM_ResultShow/de.md)
3.  Wähle unter den verschiedenen Ergebnistypen, um die Ergebnisse anzuzeigen
4.  Der Schieberegler am unteren Rand kann verwendet werden, um die Darstellung des Netzes zu ändern. Auf diese Weise können wir die Verformung, die das Objekt erfährt, visualisieren, wobei zu beachten ist, dass es sich hierbei um eine Annäherung handelt.
5.  Um die Ergebnisse zu entfernen, wähle <img alt="" src=images/FEM_PurgeResults.png  style="width:16px;"> [Säberungsergebnisse](FEM_ResultsPurge/de.md)


</div>


{{Hinweis|Vergleich zur vorherigen Beispieldatei|Wenn du den Ergebnistyp '''Z Verschiebung''' wählst, kannst du sehen, dass der erhaltene Wert fast identisch mit dem von FreeCAD gelieferten Testbeispiel ist. Unterschiede können aufgrund der Qualität des Netzes und der Anzahl der Knoten, die es besitzt, auftreten.}}


<div class="mw-translate-fuzzy">

Wir sind nun mit dem grundlegenden Arbeitsablauf für das [FEM Modul](FEM_Workbench/de.md) fertig.


</div>


{{Tutorials navi

}} {{FEM Tools navi}} 
