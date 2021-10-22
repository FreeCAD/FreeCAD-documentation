# <img alt="FEM Arbeitsbereichssymbol" src=images/Workbench_FEM.svg  style="width:64px;"> FEM Workbench/de


{{TOCright}}

## Einführung

Der [FEM Arbeitsbereich](FEM_Workbench/de.md) bietet einen modernen [Finite Element Methode](https://de.wikipedia.org/wiki/Finite-Elemente-Methode) (FEM) Arbeitsablauf für FreeCAD. Im Wesentlichen bedeutet dies, dass alle Werkzeuge zur Durchführung einer Analyse in einer grafischen Benutzeroberfläche (GUI) zusammengefasst sind.

<img alt="" src=images/FemWorkbench.jpg  style="width:300px;">

## Arbeitsablauf

Die Schritte zur Durchführung einer Finite Element Analyse sind:

1.  Vorverarbeitung: Einrichten des Analyseproblems.
    1.  Modellierung der Geometrie: Erstellung der Geometrie mit FreeCAD oder Import aus einer anderen Anwendung.
    2.  Erstellen einer Analyse.
        1.  Hinzufügen von Simulationsbeschränkungen wie Lasten und festen Stützpunkten zum geometrischen Modell.
        2.  Hinzufügen von Materialien zu den Teilen aus dem geometrischen Modell.
        3.  Erstellen eines Finite-Elemente-Netzes für das geometrische Modell oder Importieren aus einer anderen Anwendung.
2.  Lösen: Ausführen eines externen Lösers aus FreeCAD heraus.
3.  Nachbearbeitung: Visualisierung der Analyseergebnisse aus FreeCAD heraus oder Export der Ergebnisse, damit sie mit einer anderen Anwendung nachbearbeitet werden können.

Der FEM Arbeitsbereich kann unter Linux, Windows und Mac OSX eingesetzt werden. Da der Arbeitsbereich mit externen Lösern arbeitet, hängt der Umfang der manuellen Einrichtung von dem Betriebssystem ab, das Sie verwenden. Siehe [FEM Einrichtung](FEM_Install/de.md) für Anweisungen zum Einrichten der externen Werkzeuge.

<img alt="" src=images/FEM_Workbench_workflow.svg  style="width:600px;">



* Arbeitsablauf des FEM Arbeitsbereichs; der Arbeitsbereich ruft zwei externe Programme auf, um die Vernetzung eines festen Objekts und die eigentliche Lösung des Finite Element Problems durchzuführen.*

## Menü: Modell 

-   <img alt="" src=images/FEM_Analysis.svg  style="width:32px;"> [Analyse Container](FEM_Analysis/de.md): Erstellt einen neuen Behälter für eine mechanische Analyse. Wenn in der Baumansicht vor dem Anklicken ein Volumenkörper ausgewählt wird, wird als nächstes der Vernetzungsdialog geöffnet.

### Werkstoffe

-   <img alt="" src=images/FEM_MaterialSolid.svg  style="width:32px;"> [Werkstoff für Festkörper](FEM_MaterialSolid/de.md): Ermöglicht Dir, einen Feststoff aus der Datenbank auszuwählen.

-   <img alt="" src=images/FEM_MaterialFluid.svg  style="width:32px;"> [Werkstoff für Fluid](FEM_MaterialFluid/de.md): Ermöglicht Dir, ein flüssiges Material aus der Datenbank auszuwählen.

-   <img alt="" src=images/FEM_MaterialMechanicalNonlinear.svg  style="width:32px;"> [Nichtlinearer mechanischer Werkstoff](FEM_MaterialMechanicalNonlinear/de.md): Ermöglicht das Hinzufügen eines nichtlinearen mechanischen Materialmodells.

-   <img alt="" src=images/FEM_MaterialReinforced.svg  style="width:32px;"> [Bewehrtes Material (Beton)](FEM_MaterialReinforced/de.md): Ermöglicht dir, verstärkte Werkstoffe aus der Datenbank auszuwählen, bestehend aus einer Matrix und einer Verstärkung.

.

-   <img alt="" src=images/Arch_Material_Group.svg  style="width:32px;"> [Werkstoffeditor](Material_editor/de.md): Ermöglicht Dir, den Werkstoffeditor zu öffnen, um Werkstoffe zu bearbeiten.

### Elementgeometrie

-   <img alt="" src=images/FEM_ElementGeometry1D.svg  style="width:32px;"> [Trägerquerschnitt](FEM_ElementGeometry1D/de.md): Wird verwendet, um Querschnitte für Balkenelemente zu definieren.

-   <img alt="" src=images/FEM_ElementRotation1D.svg  style="width:32px;"> [Träger Drehung](FEM_ElementRotation1D/de.md): Wird verwendet, um Querschnitte von Balkenelementen zu drehen.

-   <img alt="" src=images/FEM_ElementGeometry2D.svg  style="width:32px;"> [Mantelblechdicke](FEM_ElementGeometry2D/de.md):

-   <img alt="" src=images/FEM_ElementFluid1D.svg  style="width:32px;"> [Strömungsquerschnitt für 1D Strömung](FEM_ElementFluid1D/de.md): Erstellt ein FEM Fluidschnittelement für pneumatische und hydraulische Netzwerke.

### Elektrostatische Beschränkungen 

-   <img alt="" src=images/FEM_ConstraintElectrostaticPotential.svg  style="width:32px;"> [Elektrostatisches Potential beschränken](FEM_ConstraintElectrostaticPotential/de.md):

### Fluidbeschränkungen

-   <img alt="" src=images/FEM_ConstraintInitialFlowVelocity.svg  style="width:32px;"> [Beschränkung der Anfangsströmungsgeschwindigkeit](FEM_ConstraintInitialFlowVelocity/de.md): Wird verwendet, um eine anfängliche Fließgeschwindigkeit für das Einsatzgebiet zu definieren.

-   <img alt="" src=images/FEM_ConstraintFlowVelocity.svg  style="width:32px;"> [ Strömungsgeschwindigkeit Beschränken](FEM_ConstraintFlowVelocity/de.md): Wird verwendet, um eine Strömungsgeschwindigkeit als Randbedingung an einer Kante (2D) oder Fläche (3D) zu definieren.

### Geometrische Beschränkungen 

-   <img alt="" src=images/FEM_ConstraintPlaneRotation.svg  style="width:32px;"> [Drehung der Beschränkungsebene](FEM_ConstraintPlaneRotation/de.md): Wird verwendet, um eine Beschränkung der Ebenendrehung auf einer ebenen Fläche festzulegen.

-   <img alt="" src=images/FEM_ConstraintSectionPrint.svg  style="width:32px;"> [Beschränkungsabschnitt drucken](FEM_ConstraintSectionPrint/de.md): {{Version/de|0.19}}

-   <img alt="" src=images/FEM_ConstraintTransform.svg  style="width:32px;"> [Transformationsbeschränkung](FEM_ConstraintTransform/de.md): Verwendet, um eine Transformationsbeschränkung für eine Fläche festzulegen.

### Mechanische Beschränkungen 

-   <img alt="" src=images/FEM_ConstraintFixed.svg  style="width:32px;"> [Beschränkung fixiert](FEM_ConstraintFixed/de.md): Wird verwendet, um eine fixierte Beschränkung für Punkt/Kante/Fläche(n) festzulegen.

-   <img alt="" src=images/FEM_ConstraintDisplacement.svg  style="width:32px;"> [Beschränkung Schiebung](FEM_ConstraintDisplacement/de.md): Wird verwendet, um eine Schiebungsbeschränkung für Punkt/Kante/Fläche(n) festzulegen.

-   <img alt="" src=images/FEM_ConstraintContact.svg  style="width:32px;"> [Kontaktbeschränkung](FEM_ConstraintContact/de.md): Wird verwendet, um eine Kontaktbeschränkung zwischen zwei Flächen festzulegen.

-   <img alt="" src=images/FEM_ConstraintTie.svg  style="width:32px;"> [Beschränkungsbindung](FEM_ConstraintTie/de.md): {{Version/de|0.19}}

-   <img alt="" src=images/FEM_ConstraintSpring.svg  style="width:32px;"> [Constraint spring](FEM_ConstraintSpring.md): Used to define a tie constraint (\"bonded contact\") between two faces. <small>(v0.20)</small> 

-   <img alt="" src=images/FEM_ConstraintForce.svg  style="width:32px;"> [Kraftbeschränkung](FEM_ConstraintForce.md): Wird verwendet, um eine Kraft in \[N\] festzulegen, die gleichmäßig auf eine wählbare Fläche in einer definierbaren Richtung wirkt.

-   <img alt="" src=images/FEM_ConstraintPressure.svg  style="width:32px;"> [Druckbeschränkung](FEM_ConstraintPressure/de.md): Wird verwendet, um eine Druckbeschränkung festzulegen.

-   <img alt="" src=images/FEM_ConstraintSelfWeight.svg  style="width:32px;"> [Eigengewichtsbeschränkung](FEM_ConstraintSelfWeight/de.md): Wird verwendet, um eine Schwerkraftbeschleunigung festzulegen, die auf ein Modell wirkt.

### Thermische Beschränkungen 

-   <img alt="" src=images/FEM_ConstraintInitialTemperature.svg  style="width:32px;"> [Anfangstemperaturbeschränkung](FEM_ConstraintInitialTemperature/de.md): Wird verwendet, um die Anfangstemperatur eines Körpers festzulegen.

-   <img alt="" src=images/FEM_ConstraintHeatflux.svg  style="width:32px;"> [Wärmestrombeschränkung](FEM_ConstraintHeatflux/de.md): Wird verwendet, um eine Wärmestrombeschränkung auf einer Fläche(n) festzulegen.

-   <img alt="" src=images/FEM_ConstraintTemperature.svg  style="width:32px;"> [Temperaturbeschränkung](FEM_ConstraintTemperature/de.md): Wird verwendet, um eine Temperaturbeschränkung für einen Punkt/Kante/Fläche(n) festzulegen.

-   <img alt="" src=images/FEM_ConstraintBodyHeatSource.svg  style="width:32px;"> [Körperwärmequelle beschränken](FEM_ConstraintBodyHeatSource/de.md):

### Beschränkungen ohne Löser 

-   <img alt="" src=images/FEM_ConstraintFluidBoundary.svg  style="width:32px;"> [Fluid Randbedingungen](FEM_ConstraintFluidBoundary/de.md):

-   <img alt="" src=images/FEM_ConstraintBearing.svg  style="width:32px;"> [Lagerbeschränkung](FEM_ConstraintBearing/de.md): Wird verwendet, um eine Lagerbeschränkung festzulegen.

-   <img alt="" src=images/FEM_ConstraintGear.svg  style="width:32px;"> [Zahnradbeschränkung](FEM_ConstraintGear/de.md): Wird verwendet, um eine Zahnradbeschränkung festzulegen.

-   <img alt="" src=images/FEM_ConstraintPulley.svg  style="width:32px;"> [Scheibenbeschränkung](FEM_ConstraintPulley/de.md): Wird verwendet, um eine Scheibenbeschränkung festzulegen.

### Überschreiben von Konstanten 

-   <img alt="" src=images/FEM_ConstantVacuumPermittivity.svg  style="width:32px;"> [Konstante Vakuumdurchlässigkeit](FEM_ConstantVacuumPermittivity/de.md): <small>(v0.19)</small> 

## Menü: Netz 

-   <img alt="" src=images/FEM_MeshNetgenFromShape.svg  style="width:32px;"> [FEM Netz aus Form durch Netgen](FEM_MeshNetgenFromShape/de.md):

-   <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width:32px;"> [FEM Netz aus Form durch GMSH](FEM_MeshGmshFromShape/de.md):

-   <img alt="" src=images/FEM_MeshBoundaryLayer.svg  style="width:32px;"> [FEM Netz Grenzschicht](FEM_MeshBoundaryLayer/de.md): Erzeugt anisotrope Netze für genaue Berechnungen in der Nähe von Grenzen.

-   <img alt="" src=images/FEM_MeshRegion.svg  style="width:32px;"> [FEM Netzbereich](FEM_MeshRegion/de.md): Erzeugt einen oder mehrere lokalisierte Bereiche für die Vernetzung, wodurch die Analysezeit stark optimiert wird.

-   <img alt="" src=images/FEM_MeshGroup.svg  style="width:32px;"> [FEM Netzgruppe](FEM_MeshGroup/de.md): Gruppiert und beschriftet Elemente eines Netzes (Knoten, Kante, Fläche) zusammen, nützlich für den Export des Netzes zu externen Lösern.

-   <img alt="" src=images/FEM_CreateNodesSet.svg  style="width:32px;"> [Knoten Satz](FEM_CreateNodesSet/de.md): Erstellt/definiert einen Knotensatz aus einem FEM etz.

-   <img alt="" src=images/FEM_FemMesh2Mesh.svg  style="width:32px;"> [FEM Netz zu Netz](FEM_FemMesh2Mesh/de.md): Wandle die Oberfläche eines FEM Netzes in ein Netz um.

## Menü: Lösen 

-   <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:32px;"> [Löser CalculiX Standard](FEM_SolverCalculixCxxtools/de.md): Erstellt einen neuen Löser für diese Analyse. In den meisten Fällen wird der Löser zusammen mit der Analyse erstellt.

-   <img alt="" src=images/FEM_SolverCalculiX.svg  style="width:32px;"> [Löser CalculiX (experimentell)](FEM_SolverCalculiX/de.md):

-   <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Löser Elmer](FEM_SolverElmer/de.md): Erstellt den Löser Steuerung für Elmer. Er ist unabhängig von anderen Löser Objekten.

-   <img alt="" src=images/FEM_SolverMystran.svg  style="width:32px;"> [Solver Mystran](FEM_SolverMystran.md):

-   <img alt="" src=images/FEM_SolverZ88.svg  style="width:32px;"> [Löser Z88](FEM_SolverZ88/de.md):

-   <img alt="" src=images/FEM_EquationElasticity.svg  style="width:32px;"> [Elastizitätsgleichung](FEM_EquationElasticity/de.md):

-   <img alt="" src=images/FEM_EquationElectricforce.svg  style="width:32px;"> [Elektrische Kraftgleichung](FEM_EquationElectricforce.md): <small>(v0.19)</small> 

-   <img alt="" src=images/FEM_EquationElectrostatic.svg  style="width:32px;"> [Elektrostatikgleichung](FEM_EquationElectrostatic/de.md):

-   <img alt="" src=images/FEM_EquationFlow.svg  style="width:32px;"> [Strömungsgleichung](FEM_EquationFlow/de.md):

-   <img alt="" src=images/FEM_EquationFlux.svg  style="width:32px;"> [Durchflussgleichung](FEM_EquationFluxsolver/de.md):

-   <img alt="" src=images/FEM_EquationHeat.svg  style="width:32px;"> [Wärmegleichung](FEM_EquationHeat/de.md):

-   <img alt="" src=images/FEM_SolverControl.svg  style="width:32px;"> [Löser Auftragssteuerung](FEM_SolverControl/de.md): Öffnet das Menü zum Einstellen und Starten des ausgewählten Lösers.

-   <img alt="" src=images/FEM_SolverRun.svg  style="width:32px;"> [Löserberechnungen ausführen](FEM_SolverRun/de.md): Führt den ausgewählten Löser der aktiven Analyse aus.

## Menü: Ergebnisse 

-   <img alt="" src=images/FEM_ResultsPurge.svg  style="width:32px;"> [Ergebnisse bereinigen](FEM_ResultsPurge/de.md): Löscht die Ergebnisse der aktiven Analyse.

-   <img alt="" src=images/FEM_ResultShow.svg  style="width:24px;"> [Ergebnisanzeige](FEM_ResultShow/de.md): Wird verwendet, um das Ergebnis einer Analyse anzuzeigen.

-   <img alt="" src=images/FEM_PostApplyChanges.svg  style="width:32px;"> [Änderungen auf die Pipeline anwenden](FEM_PostApplyChanges/de.md):

-   <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:32px;"> [Pipeline aus Ergebnis buchen](FEM_PostPipelineFromResult/de.md):

-   <img alt="" src=images/FEM_PostFilterWarp.svg  style="width:32px;"> [Warp Filter](FEM_PostFilterWarp/de.md):

-   <img alt="" src=images/FEM_PostFilterClipScalar.svg  style="width:32px;"> [Scalar clip filter](FEM_PostFilterClipScalar/de.md):

-   <img alt="" src=images/Fem-cut.svg  style="width:32px;"> [Funktion Cut Filter](FEM_PostCreateCutFilter.md):

-   <img alt="" src=images/FEM_PostFilterClipRegion.svg  style="width:32px;"> [Region Clip Filter](FEM_PostFilterClipRegion/de.md):

-   <img alt="" src=images/FEM_PostFilterDataAlongLine.svg  style="width:32px;"> [Line Clip Filter](FEM_PostFilterDataAlongLine/de.md):

-   <img alt="" src=images/FEM_PostFilterLinearizedStresses.svg  style="width:32px;"> [Stress linearization plot](FEM_PostFilterLinearizedStresses/de.md):

-   <img alt="" src=images/FEM_PostFilterDataAtPoint.svg  style="width:32px;"> [Data at point clip filter](FEM_PostFilterDataAtPoint/de.md):

-   [Filterfunktionen](FEM_PostCreateFunctions.md):
    -   <img alt="" src=images/Fem-post-geo-plane.svg  style="width:32px;">
    -   <img alt="" src=images/Fem-post-geo-sphere.svg  style="width:32px;">

## Menü: Hilfsmittel 

-   <img alt="" src=images/FEM_ClippingPlaneAdd.svg  style="width:32px;"> [Beschnittebene auf Fläche](FEM_ClippingPlaneAdd/de.md):

-   <img alt="" src=images/FEM_ClippingPlaneRemoveAll.svg  style="width:32px;"> [Alle Beschnittebenen entfernen](FEM_ClippingPlaneRemoveAll/de.md):

-   <img alt="" src=images/FEM_Examples.svg  style="width:32px;"> [FEM Beispiele öffnen](FEM_Examples/de.md): Öffne die GUI, um auf FEM Beispiele zuzugreifen.

## Kontextmenü

-   <img alt="" src=images/FEM_MeshClear.svg  style="width:32px;"> [FEM Netz löschen](FEM_MeshClear/de.md): Löscht die Netzdatei aus der FreeCAD-Datei. Nützlich, um eine FreeCAD Datei leichter zu machen.

-   <img alt="" src=images/FEM_MeshDisplayInfo.svg  style="width:32px;"> [FEM Netzinfomation anzeigen](FEM_MeshDisplayInfo/de.md):

## Einstellungen

-   <img alt="" src=images/Std_DlgPreferences.svg  style="width:32px;"> [Einstellungen\...](FEM_Preferences/de.md): Einstellungen, die in den FEM Werkzeugen verfügbar sind.

## Information

Die folgenden Seiten erläutern verschiedene Themen des FEM Arbeitsbereichs.

[FEM Installieren](FEM_Install/de.md): eine detaillierte Beschreibung, wie die im Arbeitsbereich verwendeten externen Programme eingerichtet werden.

[FEM Netz](FEM_Mesh/de.md): weitere Informationen zur Erlangung eines Netzes für die Finite Elemente Analyse.

[FEM Löser](FEM_Solver/de.md): weitere Informationen über die verschiedenen im Arbeitsbereich verfügbaren und zukünftig einsetzbaren Löser.

[FEM CalculiX](FEM_CalculiX/de.md): weitere Informationen zu CalculiX, dem Standard Löser, der im Arbeitsbereich für die Strukturanalyse verwendet wird.

[FEM Beton](FEM_Concrete/de.md): interessante Informationen zum Thema Simulation von Betonstrukturen.

[FEM Projekt](FEM_project/de.md): weitere Informationen über das Einheitensystem, Begrenzungen und die Entwicklungsideen und den Fahrplan des Arbeitsbereichs.

## Tutorien

Tutorium 1: [FEM CalculiX Cantilever 3D](FEM_CalculiX_Cantilever_3D/de.md); grundlegende, einfach unterstützte Strahlanalyse.

Tutorium 2: [FEM Tutorium](FEM_tutorial/de.md); einfache Spannungsanalyse einer Struktur.

Tutorium 3: [FEM Tutorium Python](FEM_Tutorial_Python/de.md); einrichten des Cantilever Beispiels vollständig durch Skripting in Python, einschließlich des Netzes.

Tutorium 4: [FEM Scherung eines Verbundwerkstoffblocks](FEM_Shear_of_a_Composite_Block/de.md); siehe die Verformung eines Blocks, der aus zwei Materialien besteht.

Tutorium 5: [Transiente FEM Analyse](Transient_FEM_analysis/de.md)

Tutorium 6: [Nachbearbeitung\_von\_FEM-Ergebnissen\_mit\_Paraview](Post-Processing_of_FEM_Results_with_Paraview/de.md)

Tutorium 7: [FEM Example Capacitance Two Balls](FEM_Example_Capacitance_Two_Balls.md); Elmer\'s GUI tutorium 6 \"Electrostatics Capacitance Two Balls\" using FEM Examples.

Gekoppelte Tutorien zur thermomechanischen Analyse von [openSIM](https://opensimsa.github.io/training.html).

Videotutorium 1: [FEM Video für Anfänger](https://forum.freecadweb.org/viewtopic.php?f=18&t=20499#p158353) (einschließlich YouTube-Link)

Videotutorium 2: [FEM Video für Anfänger](https://forum.freecadweb.org/viewtopic.php?f=18&t=20499&start=10#p162321) (einschließlich YouTube-Link)

Viele Videotutorien: [anisim Open Source Engineering Software](https://www.youtube.com/channel/UCnvFCm2BbXOVI3ObfXcxXhw) (in Deutsch)

## Erweiterung dea FEM Arbeitsbereichs 

Der FEM Arbeitsbereich wird ständig weiterentwickelt. Ein Ziel des Projekts ist es, Wege zu finden, wie man einfach mit verschiedenen FEM Lösern interagieren kann, so dass der Endanwender den Prozess der Erstellung, Vernetzung, Simulation und Optimierung eines Konstruktionsproblems in FreeCAD rationalisieren kann.

Die folgenden Information richtet sich an fortgeschrittene Anwender und Entwickler, die den FEM Arbeitsbereich auf unterschiedliche Weise erweitern möchten. Vertrautheit mit C++ und Python werden vorausgesetzt, ebenso wie einige Kenntnisse des in FreeCAD verwendeten \"Dokumentobjekt\" Systems; diese Informationen sind im [Verteiler für Intensivnutzer](Power_Users_Hub/de.md) und im [Verteiler für Entwickler](Developer_Hub/de.md) verfügbar. Bitte beachte, dass einige Artikel zu alt und damit veraltet sein können, da sich FreeCAD in der aktiven Entwicklung befindet. Die aktuellsten Informationen werden in den [FreeCAD Foren](https://forum.freecadweb.org/index.php), im Bereich Entwicklung, diskutiert. Für FEM Diskussionen, Ratschläge oder Unerstützung bei der Erweiterung des Arbeitsbereichs sollte sich der Leser auf das [FEM Unterforum](https://forum.freecadweb.org/viewforum.php?f=18) beziehen.

In den folgenden Artikeln wird erläutert, wie der Arbeitsbereich erweitert werden kann, z.B. durch Hinzufügen neuer Arten von Randbedingungen (Beschränkungen) oder Gleichungen.

-   [FEM Modul erweitern](Extend_FEM_Module/de.md)
-   [Tutorium FEM Beschränkungen hinzufügen](Add_FEM_Constraint_Tutorial/de.md)
-   [Tutorium FEM Gleichungen hinzufügen](Add_FEM_Equation_Tutorial/de.md)

Ein Entwicklerhandbuch wurde geschrieben, um Power-Usern zu helfen, die komplexe FreeCAD-Codebasis und die Interaktionen zwischen den Kernelementen und den einzelnen Workbenches zu verstehen. Das Buch wird bei github gehostet, so dass mehrere Benutzer dazu beitragen und es auf dem neuesten Stand halten können.

-   [Frühe Vorschau des ebook: Anleitung für Modulentwickler zur FreeCAD-Quelle](https://forum.freecadweb.org/viewtopic.php?t=17581) (Forum-Thread)
-   [FreeCAD Mod Dev Guide](https://github.com/qingfengxia/FreeCAD_Mod_Dev_Guide) (github repository)

## Erweitern der FEM Arbeitsbereichsdokumentation 

-   Weitere Informationen zur Erweiterung oder fehlenden FEM Dokumentation kann im Forum gefunden werden: [Fehlende FEM Dokumentation im Wiki](https://forum.freecadweb.org/viewtopic.php?f=18&t=20823)





{{FEM Tools navi

}} 

_

---
[documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > FEM Workbench/de
