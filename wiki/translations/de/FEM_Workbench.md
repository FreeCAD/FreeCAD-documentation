# <img alt="Symbol des Arbeitsbereichs FEM" src=images/Workbench_FEM.svg  style="width:64px;"> FEM Workbench/de






## Einleitung

Der Arbeitsbereich [FEM](FEM_Workbench/de.md) ermöglicht einen modernen Arbeitsablauf zur Finite-Elemente-Analyse (FEA) innerhalb von FreeCAD, siehe [Finite-Elemente-Methode](https://de.wikipedia.org/wiki/Finite-Elemente-Methode) (FEM). Dies bedeutet im Wesentlichen, dass alle Werkzeuge zur Durchführung einer Analyse in einer grafischen Benutzeroberfläche (GUI) zusammengefasst sind.

<img alt="" src=images/FemWorkbench.jpg  style="width:300px;">



## Arbeitsablauf

Die Schritte zur Durchführung einer Finite-Elemente-Analyse sind:

1.  Vorbereitung: Einrichten des Analyseproblems.
    1.  Modellierung der Geometrie: Erstellung der Geometrie mit FreeCAD oder Import aus einer anderen Anwendung.
    2.  Erstellen einer Analyse.
        1.  Hinzufügen von Simulationsrandbedingungen wie Lasten und starren Einspannungen zum geometrischen Modell.
        2.  Hinzufügen von Materialien zu Teilen des geometrischen Modells.
        3.  Erstellen eines Finite-Elemente-Netzes für das geometrische Modell oder Importieren eines Netzes aus einer anderen Anwendung.
2.  Berechnung: Ausführen eines externen Lösers aus FreeCAD heraus.
3.  Nachbearbeitung: Visualisierung der Analyseergebnisse aus FreeCAD heraus oder Export der Ergebnisse, damit sie mit einer anderen Anwendung nachbearbeitet werden können.

Der Arbeitsbereich FEM kann unter Linux, Windows und Mac OSX eingesetzt werden. Da der Arbeitsbereich mit externen Lösern arbeitet, hängt der Umfang der manuellen Einrichtung von dem Betriebssystem des Benutzers ab. Siehe [FEM Einrichtung](FEM_Install/de.md) für Anweisungen zum Einrichten der externen Werkzeuge.

<img alt="" src=images/FEM_Workbench_workflow.svg  style="width:600px;">



* Arbeitsablauf des Arbeitsbereichs FEM; der Arbeitsbereich ruft zwei externe Programme auf, eins zum Vernetzen eines Festkörper-Objekts zu vernetzen und eins um die eigentliche rechnerische Lösung des Finite-Elemente-Problems durchzuführen.*



## Menü Modell 

-   <img alt="" src=images/FEM_Analysis.svg  style="width:32px;"> [Analysebehälter](FEM_Analysis/de.md): Erstellt einen neuen Behälter (Analysis-Objekt) für eine mechanische Analyse. Wenn in der Baumansicht vor dem Anklicken ein Festkörper ausgewählt wird, wird als nächstes der Vernetzungsdialog geöffnet.



### Werkstoffe

  - <img alt="" src=images/FEM_MaterialSolid.svg  style="width:32px;"> [Werkstoff für Festkörper](FEM_MaterialSolid/de.md): Ermöglicht, einen Feststoff aus der Datenbank auszuwählen.

  - <img alt="" src=images/FEM_MaterialFluid.svg  style="width:32px;"> [Werkstoff für Fluide](FEM_MaterialFluid/de.md): Ermöglicht, ein \"fließendes Material\" (Gas oder Flüssigkeit) aus der Datenbank auszuwählen.

  - <img alt="" src=images/FEM_MaterialMechanicalNonlinear.svg  style="width:32px;"> [Nichtlinearer mechanischer Werkstoff](FEM_MaterialMechanicalNonlinear/de.md): Ermöglicht das Hinzufügen eines nichtlinearen mechanischen Materialmodells.

  - <img alt="" src=images/FEM_MaterialReinforced.svg  style="width:32px;"> [Bewehrtes Material (Beton)](FEM_MaterialReinforced/de.md): Ermöglicht, verstärkte Werkstoffe aus der Datenbank auszuwählen, die aus einer Matrix und einer Bewehrung (Verstärkung, Armierung) bestehen.

  - <img alt="" src=images/FEM_MaterialEditor.svg  style="width:32px;"> [Werkstoffeditor](FEM_MaterialEditor/de.md): Ermöglicht, den Werkstoffeditor zu öffnen, um Werkstoffe zu bearbeiten.



### Elementgeometrie

  - <img alt="" src=images/FEM_ElementGeometry1D.svg  style="width:32px;"> [Trägerquerschnitt](FEM_ElementGeometry1D/de.md): Wird verwendet, um Querschnitte für Balkenelemente zu definieren.

  - <img alt="" src=images/FEM_ElementRotation1D.svg  style="width:32px;"> [Träger Drehung](FEM_ElementRotation1D/de.md): Wird verwendet, um Querschnitte von Balkenelementen zu drehen.

  - <img alt="" src=images/FEM_ElementGeometry2D.svg  style="width:32px;"> [Wandstärke](FEM_ElementGeometry2D/de.md): Wird verwendet, um die Wandstärke für Schalenelemente festzulegen.

  - <img alt="" src=images/FEM_ElementFluid1D.svg  style="width:32px;"> [Strömungsquerschnitt für 1D-Strömung](FEM_ElementFluid1D/de.md): Wird verwendet, um einen FEM-Strömungsquerschnitt für pneumatische und hydraulische Netzwerke festzulegen.



### Elektromagnetische Randbedingungen 

  - <img alt="" src=images/FEM_ConstraintElectrostaticPotential.svg  style="width:32px;"> [Elektrostatisches Potential](FEM_ConstraintElectrostaticPotential/de.md): Legt ein elektrostatisches Potential fest.

  - <img alt="" src=images/FEM_ConstraintCurrentDensity.svg  style="width:32px;"> [Randbedingung Stromdichte](FEM_ConstraintCurrentDensity/de.md): Legt eine Stromdichte fest. {{Version/de|0.21}}

  - <img alt="" src=images/FEM_ConstraintMagnetization.svg  style="width:32px;"> [Randbedingung Magnetisierung](FEM_ConstraintMagnetization/de.md): Wird zum Festlegen einer Magnetisierung verwendet. {{Version/de|0.21}}



### Randbedingungen für Fluide 

  - <img alt="" src=images/FEM_ConstraintInitialFlowVelocity.svg  style="width:32px;"> [Startbedingung Strömungsgeschwindigkeit](FEM_ConstraintInitialFlowVelocity/de.md): Wird verwendet, um eine anfängliche Strömungsgeschwindigkeit für einen Körper (ein Volumen) zu definieren.

  - <img alt="" src=images/FEM_ConstraintInitialPressure.svg  style="width:32px;"> [Startbedingung Druck](FEM_ConstraintInitialPressure/de.md): Wird verwendet, um einen anfänglichen Druck für einen Körper (ein Volumen) festzulegen. {{Version/de|0.21}}

  - <img alt="" src=images/FEM_ConstraintFlowVelocity.svg  style="width:32px;"> [Randbedingung Strömungsgeschwindigkeit](FEM_ConstraintFlowVelocity/de.md): Wird verwendet, um eine Strömungsgeschwindigkeit als Grenzbedingung an einer Kante (2D) oder Fläche (3D) festzulegen.



### Geometrische Analyse-Elemente 

-   <img alt="" src=images/FEM_ConstraintPlaneRotation.svg  style="width:32px;"> [RandbedingungEbeneDurchPunkte](FEM_ConstraintPlaneRotation/de.md): Wird verwendet, um eine Randbedingung zu erstellen, die Knoten einer ebenen Oberfläche auf derselben Ebene festhält.

-   <img alt="" src=images/FEM_ConstraintSectionPrint.svg  style="width:32px;"> [Section print feature](FEM_ConstraintSectionPrint/de.md): Wird zur Ausgabe der vorgegebenen \"facial output variables\" (Kräfte und Momente) in die Daten-Datei verwendet.

-   <img alt="" src=images/FEM_ConstraintTransform.svg  style="width:32px;"> [Lokales Koordinatensystem](FEM_ConstraintTransform/de.md): Wird verwendet, um eine Randbedingung Überführen auf einer Fläche festzulegen.



### Mechanische Randbedingungen und Lasten 

  - <img alt="" src=images/FEM_ConstraintFixed.svg  style="width:32px;"> [Randbedingung Festsetzen](FEM_ConstraintFixed/de.md): Wird verwendet, um Punkte, Kanten oder Flächen festzusetzen.

  - <img alt="" src=images/FEM_ConstraintRigidBody.svg  style="width:32px;"> [Randbedingung starrer Körper](FEM_ConstraintRigidBody/de.md): Wird verwendet, um CalculiXs Randbedingung starrer Körper anzuwenden, die die Bewegung der Knoten einer ausgewählten geometrischen Einzelheit bezüglich eines durch den Benutzer festgelegten Referenzpunktes festlegt. {{Version/de|1.0}}

  - <img alt="" src=images/FEM_ConstraintDisplacement.svg  style="width:32px;"> [Randbedingung Versatz](FEM_ConstraintDisplacement/de.md): Wird verwendet, um einen Versatz für Punkte, Kanten oder Flächen festzulegen.

  - <img alt="" src=images/FEM_ConstraintContact.svg  style="width:32px;"> [Randbedingung Kontakt](FEM_ConstraintContact/de.md): Wird verwendet, um eine Randbedingung Kontakt zwischen zwei Flächen festzulegen.

  - <img alt="" src=images/FEM_ConstraintTie.svg  style="width:32px;"> [Randbedingung Verbinder](FEM_ConstraintTie/de.md): Wird verwendet, um eine Randbedingung Vebinder (wie ein Kleber- oder Schweißpunkt) zwischen zwei Flächen (\"bonded contact\") festzulegen oder, {{Version/de|1.0}}, zyklische Symmetrie.

  - <img alt="" src=images/FEM_ConstraintSpring.svg  style="width:32px;"> [Feder](FEM_ConstraintSpring/de.md): Wird verwendet, um eine Randbedingung Feder festzulegen. {{Version/de|0.20}}

  - <img alt="" src=images/FEM_ConstraintForce.svg  style="width:32px;"> [Kraftbelastung](FEM_ConstraintForce/de.md): Wird verwendet, um eine Kraft in \[N\] festzulegen, die gleichmäßig auf eine auswählbare Fläche in einer definierbaren Richtung wirkt.

  - <img alt="" src=images/FEM_ConstraintPressure.svg  style="width:32px;"> [Druckbelastung](FEM_ConstraintPressure/de.md): Wird verwendet, um eine Randbedingung Druck festzulegen.

  - <img alt="" src=images/FEM_ConstraintCentrif.svg  style="width:32px;"> [Zentrifugale Last](FEM_ConstraintCentrif/de.md): Legt eine zentrifugale Last auf einen Körper fest. {{Version/de|0.20}}

  - <img alt="" src=images/FEM_ConstraintSelfWeight.svg  style="width:32px;"> [Schwerkraft-Last](FEM_ConstraintSelfWeight/de.md): Wird verwendet, um eine Schwerkraftbeschleunigung festzulegen, die auf ein Modell wirkt.



### Thermische Randbedingungen und Lasten 

  - <img alt="" src=images/FEM_ConstraintInitialTemperature.svg  style="width:32px;"> [Startbedingung Temperatur](FEM_ConstraintInitialTemperature/de.md): Wird verwendet, um die Anfangstemperatur eines Körpers festzulegen.

  - <img alt="" src=images/FEM_ConstraintHeatflux.svg  style="width:32px;"> [Wärmestrom-Last](FEM_ConstraintHeatflux/de.md): Wird verwendet, um eine Randbedingung Wärmestrom auf einer Fläche(n) festzulegen.

  - <img alt="" src=images/FEM_ConstraintTemperature.svg  style="width:32px;"> [RandbedingungTemperatur](FEM_ConstraintTemperature/de.md): Wird verwendet, um eine Randbedingung Temperatur für einen Punkt, eine Kante oder Fläche(n) festzulegen.

  - <img alt="" src=images/FEM_ConstraintBodyHeatSource.svg  style="width:32px;"> [Körperwärmequelle](FEM_ConstraintBodyHeatSource/de.md): zum Festlegen von intern erzeugter Körperwärme.



### Konstanten Überschreiben 

  - <img alt="" src=images/FEM_ConstantVacuumPermittivity.svg  style="width:32px;"> [ElektrischeFeldkonstante](FEM_ConstantVacuumPermittivity/de.md): Wird verwendet, um die [elektrische Feldkonstante](https://de.wikipedia.org/wiki/Elektrische_Feldkonstante) (Permittivität des Vakuums) mit einem selbstgewählten Wert zu überschreiben.



## Menü Netz 

-   <img alt="" src=images/FEM_MeshNetgenFromShape.svg  style="width:32px;"> [FEM Netz aus Form durch Netgen](FEM_MeshNetgenFromShape/de.md): Generiert ein Finite-Elemente-Netz für ein Modell mit Netgen.

-   <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width:32px;"> [FEM Netz aus Form durch GMSH](FEM_MeshGmshFromShape/de.md): Generiert ein Finite-Elemente-Netz für ein Modell mit Gmsh.

-   <img alt="" src=images/FEM_MeshBoundaryLayer.svg  style="width:32px;"> [FEM Netz Grenzschicht](FEM_MeshBoundaryLayer/de.md): Erzeugt anisotrope Netze für genaue Berechnungen in der Nähe von Grenzen.

-   <img alt="" src=images/FEM_MeshRegion.svg  style="width:32px;"> [FEM Netzbereich](FEM_MeshRegion/de.md): Erzeugt einen oder mehrere lokalisierte Bereiche für die Vernetzung, wodurch die Analysezeit stark optimiert wird.

-   <img alt="" src=images/FEM_MeshGroup.svg  style="width:32px;"> [FEM Netzgruppe](FEM_MeshGroup/de.md): Gruppiert und beschriftet Elemente eines Netzes (Knoten, Kante, Fläche) zusammen, nützlich für den Export des Netzes zu externen Lösern.

-   <img alt="" src=images/FEM_CreateElementsSet.svg  style="width:32px;"> [Elemente löschen](FEM_CreateElementsSet/de.md): Blendet durch ein Polygon ausgewählte Elemente aus dem Netz aus. <small>(v1.0)</small> 

-   <img alt="" src=images/FEM_FemMesh2Mesh.svg  style="width:32px;"> [FEM-Netz zu Netz](FEM_FemMesh2Mesh/de.md): Wandelt Oberflächen von 3D-Elementen oder ganze 2D-Elemente eines ausgewählten FEM-Netzes in ein Oberflächennetz um.



## Menü Lösen 

-   <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:32px;"> [Löser CalculiX Standard](FEM_SolverCalculixCxxtools/de.md): Erstellt einen neuen Löser für diese Analyse.

-   <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Löser Elmer](FEM_SolverElmer/de.md): Erstellt die Löser-Steuerung für Elmer.

-   <img alt="" src=images/FEM_SolverMystran.svg  style="width:32px;"> [Löser Mystran](FEM_SolverMystran/de.md): Erstellt die Löser-Steuerung für Mystran. {{Version/de|0.20}}

-   <img alt="" src=images/FEM_SolverZ88.svg  style="width:32px;"> [Löser Z88](FEM_SolverZ88/de.md): Erstellt die Löser-Steuerung für Z88.



### Mechanische Gleichungen 

  - <img alt="" src=images/FEM_EquationElasticity.svg  style="width:32px;"> [Elastizitätsgleichung](FEM_EquationElasticity/de.md): Gleichung für den Löser <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Elmer](FEM_SolverElmer.md) zur Durchführung linearer mechanischer Analysen.

  - <img alt="" src=images/FEM_EquationDeformation.svg  style="width:32px;"> [Verformung](FEM_EquationDeformation/de.md): Gleichung für den Löser <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Elmer](FEM_SolverElmer/de.md) zur Durchführung nicht linearer mechanischer Analysen (Verformungen). {{Version/de|0.21}}



### Elektromagnetische Gleichungen 

  - <img alt="" src=images/FEM_EquationElectrostatic.svg  style="width:32px;"> [Gleichung Elektrostatik](FEM_EquationElectrostatic/de.md): Gleichung für den Löser <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Elmer](FEM_SolverElmer/de.md) zur Durchführung elektrostatischer Analysen.

  - <img alt="" src=images/FEM_EquationElectricforce.svg  style="width:32px;"> [Gleichung elektrische Kraft](FEM_EquationElectricforce/de.md): Gleichung für den Löser <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Elmer](FEM_SolverElmer/de.md) zur Berechnung der elektrischen Kraft auf Flächen.

  - <img alt="" src=images/FEM_EquationMagnetodynamic.svg  style="width:32px;"> [Gleichung Elektrodynamik](FEM_EquationMagnetodynamic/de.md): Gleichung für den Löser <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Elmer](FEM_SolverElmer/de.md) für elektrodynamische Berechnungen. {{Version/de|0.21}}

  - <img alt="" src=images/FEM_EquationMagnetodynamic2D.svg  style="width:32px;"> [Gleichung Elektrodynamik 2D](FEM_EquationMagnetodynamic2D/de.md): Gleichung für den Löser <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Elmer](FEM_SolverElmer/de.md) für elektrodynamische 2D-Berechnungen. {{Version/de|0.21}}

-   <img alt="" src=images/FEM_EquationFlow.svg  style="width:32px;"> [Gleichung Strömung](FEM_EquationFlow/de.md): Gleichung für den Löser <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Elmer](FEM_SolverElmer/de.md) zur Durchführung von Strömungsanalysen.

-   <img alt="" src=images/FEM_EquationFlux.svg  style="width:32px;"> [Gleichung Fluss](FEM_EquationFlux/de.md): Gleichung für den Löser <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Elmer](FEM_SolverElmer/de.md) zur Durchführung von Fluss-Analysen.

-   <img alt="" src=images/FEM_EquationHeat.svg  style="width:32px;"> [Wärmegleichung](FEM_EquationHeat/de.md): Gleichung für den Löser <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Elmer](FEM_SolverElmer/de.md) zum Durchführen von Wärmeübertragungsanalysen.

-   <img alt="" src=images/FEM_SolverControl.svg  style="width:32px;"> [Löser Auftragssteuerung](FEM_SolverControl/de.md): Öffnet das Menü zum Einstellen und Starten des ausgewählten Lösers.

-   <img alt="" src=images/FEM_SolverRun.svg  style="width:32px;"> [Löserberechnungen ausführen](FEM_SolverRun/de.md): Führt den ausgewählten Löser der aktiven Analyse aus.



## Menü Ergebnisse 

-   <img alt="" src=images/FEM_ResultsPurge.svg  style="width:32px;"> [Ergebnisse bereinigen](FEM_ResultsPurge/de.md): Löscht die Ergebnisse der aktiven Analyse.

-   <img alt="" src=images/FEM_ResultShow.svg  style="width:24px;"> [Ergebnisanzeige](FEM_ResultShow/de.md): Wird verwendet, um das Ergebnis einer Analyse anzuzeigen. Dieser Dialog ist für den Löser [Elmer](FEM_SolverElmer/de.md) nicht verfügbar, da dieser Löser nur unter Verwendung von [NachbearbeitungPipelineVonErgebnis](FEM_PostPipelineFromResult/de.md) visualisiert.

-   <img alt="" src=images/FEM_PostApplyChanges.svg  style="width:32px;"> [Änderungen auf die Pipeline anwenden](FEM_PostApplyChanges/de.md): Aktiviert oder Deaktiviert, ob Änderungen an der Ergebnis-Pipeline und den Filtern unmittelbar angewendet werden

-   <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:32px;"> [Pipeline aus Ergebnis buchen](FEM_PostPipelineFromResult/de.md): Wird verwendet, um eine neue grafische Darstellungen von FEM-Analyseergebnissen (Farbskala und weitere Darstellungsoptionen) hinzuzufügen.

-   <img alt="" src=images/FEM_PostFilterWarp.svg  style="width:32px;"> [Warp Filter](FEM_PostFilterWarp/de.md): zum Darstellen der skaliert verzerrten Form eines Modells.

-   <img alt="" src=images/FEM_PostFilterClipScalar.svg  style="width:32px;"> [Scalarer Ausschnittfilter](FEM_PostFilterClipScalar/de.md): zum Beschneiden eines Feldes mit einem bestimmten skalaren Wert.

-   <img alt="" src=images/FEM_PostFilterCutFunction.svg  style="width:32px;"> [Schnittfilter](FEM_PostFilterCutFunction/de.md): zum Darstellen der Ergebnisse auf einer Kugel oder Ebene, die durch das Modell schneidet.

-   <img alt="" src=images/FEM_PostFilterClipRegion.svg  style="width:32px;"> [Region Schnittfilter](FEM_PostFilterClipRegion/de.md): zum Beschneiden eines Feldes mit einer Kugel oder einer Ebene, die durch das Modell schneidet.

-   <img alt="" src=images/FEM_PostFilterContours.svg  style="width:32px;"> [Konturenfilter](FEM_PostFilterContours/de.md): zur Darstellung von Iso-(parametrischen-)Linien (für Analysen in 2D) oder Iso-Konturen. {{Version/de|0.21}}

-   <img alt="" src=images/FEM_PostFilterDataAlongLine.svg  style="width:32px;"> [Linienschnittfilter](FEM_PostFilterDataAlongLine/de.md): zum Plotten der Werte eines Feldes entlang einer bestimmten Linie.

-   <img alt="" src=images/FEM_PostFilterLinearizedStresses.svg  style="width:32px;"> [Spannungsdiagramm](FEM_PostFilterLinearizedStresses/de.md): Erstellt ein Spannungsdiagramm.

-   <img alt="" src=images/FEM_PostFilterDataAtPoint.svg  style="width:32px;"> [Daten zu Punkt Schnittfilter](FEM_PostFilterDataAtPoint/de.md): zur Darstellung des Wertes eines ausgewählten Feldes an einem gegebenen Punkt



### Filterfunktionen

  - <img alt="" src=images/FEM_PostCreateFunctionPlane.svg  style="width:32px;"> [Ebene](FEM_PostCreateFunctionPlane/de.md): Beschneidet das Ergebnisnetz mit einer Ebene.

  - <img alt="" src=images/FEM_PostCreateFunctionSphere.svg  style="width:32px;"> [Kugel](FEM_PostCreateFunctionSphere/de.md): Beschneidet das Ergebnisnetz mit einer Kugel.

  - <img alt="" src=images/FEM_PostCreateFunctionCylinder.svg  style="width:32px;"> [Zylinder](FEM_PostCreateFunctionCylinder/de.md): Beschneidet das Ergebnisnetz mit einem Zylinder {{Version/de|0.21}}

  - <img alt="" src=images/FEM_PostCreateFunctionBox.svg  style="width:32px;"> [Quader](FEM_PostCreateFunctionBox/de.md): Beschneidet das Ergebnisnetz mit einem Quader {{Version/de|0.21}}



## Menü Dienstprogramme 

-   <img alt="" src=images/FEM_ClippingPlaneAdd.svg  style="width:32px;"> [Beschnittebene auf Fläche](FEM_ClippingPlaneAdd/de.md): Fügt eine Beschnittebene für die gesamte Modellansicht hinzu.

-   <img alt="" src=images/FEM_ClippingPlaneRemoveAll.svg  style="width:32px;"> [Alle Schnittebenen entfernen](FEM_ClippingPlaneRemoveAll/de.md): Entfernt alle vorhandenen [Schnittebenen](FEM_ClippingPlaneAdd/de.md).

-   <img alt="" src=images/FEM_Examples.svg  style="width:32px;"> [FEM Beispiele öffnen](FEM_Examples/de.md): Öffne die GUI, um auf FEM Beispiele zuzugreifen.



## Kontextmenü

-   <img alt="" src=images/FEM_MeshClear.svg  style="width:32px;"> [FEM Netz löschen](FEM_MeshClear/de.md): Löscht die Netzdatei aus der FreeCAD-Datei. Nützlich, um eine FreeCAD Datei leichter zu machen.

-   <img alt="" src=images/FEM_MeshDisplayInfo.svg  style="width:32px;"> [FEM Netzinfomation anzeigen](FEM_MeshDisplayInfo/de.md): Zeigt die grundlegenden Daten vorhandener Netze an - Anzahl der Knoten und der Elemente von jeder Art



## Veraltete Werkzeuge 

-   <img alt="" src=images/FEM_ConstraintFluidBoundary.svg  style="width:32px;"> [Fluid Randbedingungen](FEM_ConstraintFluidBoundary/de.md): Wird zum festlegen einer Fluid-Grenzschicht-Bedingung verwendet. Besaß keinen Löser. Nicht vorhanden in {{VersionPlus/de|1.0}}.

-   <img alt="" src=images/FEM_ConstraintBearing.svg  style="width:32px;"> [Lagerbeschränkung](FEM_ConstraintBearing/de.md): Wird verwendet, um eine Lagerbeschränkung festzulegen. Besaß keinen Löser. Nicht vorhanden in {{VersionPlus/de|1.0}}.

-   <img alt="" src=images/FEM_ConstraintGear.svg  style="width:32px;"> [Zahnradbeschränkung](FEM_ConstraintGear/de.md): Wird verwendet, um eine Zahnradbeschränkung festzulegen. Besaß keinen Löser. Nicht vorhanden in {{VersionPlus/de|1.0}}.

-   <img alt="" src=images/FEM_ConstraintPulley.svg  style="width:32px;"> [Scheibenbeschränkung](FEM_ConstraintPulley/de.md): Wird verwendet, um eine Scheibenbeschränkung festzulegen. Besaß keinen Löser. Nicht vorhanden in {{VersionPlus/de|1.0}}.

-   <img alt="" src=images/FEM_SolverCalculiX.svg  style="width:32px;"> [Löser CalculiX (neuer Framework)](FEM_SolverCalculiX/de.md): Gleicht dem originalen Aufbau <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:32px;"> [Löser CalculiX Standard](FEM_SolverCalculixCxxtools/de.md) mit zusätzlichen Prüfungen. Das Werkzeug war nicht fertiggestellt. Nicht vorhanden in {{VersionPlus/de|1.0}}.

-   <img alt="" src=images/FEM_CreateNodesSet.svg  style="width:32px;"> [Knoten Satz](FEM_CreateNodesSet/de.md): Erstellt/definiert einen Knotensatz aus einem FEM-Netz. Das Werkzeug wurde nie fretiggestellt und konnte nicht verwendet werden. Nicht mehr vorhanden in {{VersionPlus/de|1.0}}.



## Einstellungen

-   <img alt="" src=images/Std_DlgPreferences.svg  style="width:32px;"> [Einstellungen\...](FEM_Preferences/de.md): Einstellungen, die in den FEM Werkzeugen verfügbar sind.

## Information

Die folgenden Seiten erläutern verschiedene Themen des FEM Arbeitsbereichs.

[FEM Installieren](FEM_Install/de.md): eine detaillierte Beschreibung, wie die im Arbeitsbereich verwendeten externen Programme eingerichtet werden.

[FEM Geometry Preparation and Meshing](FEM_Geometry_Preparation_and_Meshing.md): Tipps bezüglich Geometrievorbereitung für FEM und Netzerstellung (engl.).

[FEM Netz](FEM_Mesh/de.md): Einzelheiten zu Netzen im Arbeitsbereich FEM.

[FEM Löser](FEM_Solver/de.md): weitere Informationen über die verschiedenen im Arbeitsbereich verfügbaren und zukünftig einsetzbaren Löser.

[FEM CalculiX](FEM_CalculiX/de.md): weitere Informationen zu CalculiX, dem Standard Löser, der im Arbeitsbereich für die Strukturanalyse verwendet wird.

[FEM Beton](FEM_Concrete/de.md): interessante Informationen zum Thema Simulation von Betonstrukturen.



## Tutorien

Tutorium 1: [FEM CalculiX Cantilever 3D](FEM_CalculiX_Cantilever_3D/de.md); grundlegende, einfach unterstützte Strahlanalyse.

Tutorium 2: [FEM Tutorium](FEM_tutorial/de.md); einfache Spannungsanalyse einer Struktur.

Tutorium 3: [FEM Tutorium Python](FEM_Tutorial_Python/de.md); einrichten des Cantilever Beispiels vollständig durch Skripting in Python, einschließlich des Netzes.

Tutorium 4: [FEM Scherung eines Verbundwerkstoffblocks](FEM_Shear_of_a_Composite_Block/de.md); siehe die Verformung eines Blocks, der aus zwei Materialien besteht.

Tutorium 5: [Transiente FEM Analyse](Transient_FEM_analysis/de.md)

Tutorium 6: [Nachbearbeitung von FEM-Ergebnissen mit Paraview](Post-Processing_of_FEM_Results_with_Paraview/de.md)

Tutorium 7: [FEM Beispiel Kapazität Zweier Kugeln](FEM_Example_Capacitance_Two_Balls/de.md); Elmer\'s GUI-Tutorium 6 \"Electrostatics Capacitance Two Balls\", verwendet FEM-Beispiele.

Gekoppelte Tutorien zur thermomechanischen Analyse von [openSIM](https://opensimsa.github.io/training.html).

Videotutorium 1: [FEM Video für Anfänger](https://forum.freecadweb.org/viewtopic.php?f=18&t=20499#p158353) (einschließlich YouTube-Link)

Videotutorium 2: [FEM Video für Anfänger](https://forum.freecadweb.org/viewtopic.php?f=18&t=20499&start=10#p162321) (einschließlich YouTube-Link)

Viele Videotutorials: [anisim Open Source Engineering Software](https://www.youtube.com/channel/UCnvFCm2BbXOVI3ObfXcxXhw) (in Deutsch)



## Erweiterung des Arbeitsbereichs FEM 

Der FEM Arbeitsbereich wird ständig weiterentwickelt. Ein Ziel des Projekts ist es, Wege zu finden, wie man einfach mit verschiedenen FEM Lösern interagieren kann, so dass der Endanwender den Prozess der Erstellung, Vernetzung, Simulation und Optimierung eines Konstruktionsproblems in FreeCAD rationalisieren kann.

Die folgenden Information richtet sich an fortgeschrittene Anwender und Entwickler, die den FEM Arbeitsbereich auf unterschiedliche Weise erweitern möchten. Vertrautheit mit C++ und Python werden vorausgesetzt, ebenso wie einige Kenntnisse des in FreeCAD verwendeten \"Dokumentobjekt\" Systems; diese Informationen sind im [Verteiler für Intensivnutzer](Power_users_hub/de.md) und im [Verteiler für Entwickler](Developer_hub/de.md) verfügbar. Bitte beachte, dass einige Artikel zu alt und damit veraltet sein können, da sich FreeCAD in der aktiven Entwicklung befindet. Die aktuellsten Informationen werden in den [FreeCAD Foren](https://forum.freecadweb.org/index.php), im Bereich Entwicklung, diskutiert. Für FEM Diskussionen, Ratschläge oder Unerstützung bei der Erweiterung des Arbeitsbereichs sollte sich der Leser auf das [FEM Unterforum](https://forum.freecadweb.org/viewforum.php?f=18) beziehen.

In den folgenden Artikeln wird erläutert, wie der Arbeitsbereich erweitert werden kann, z.B. durch Hinzufügen neuer Arten von Randbedingungen (Beschränkungen) oder Gleichungen.

-   [FEM-Modul erweitern](Extend_FEM_Module/de.md)
-   [Einarbeitung FEM-Entwickler](Onboarding_FEM_Devs/de.md) versucht neuen Entwicklern eine Orientierung zu geben, wie man zum Arbeitsbereich FEM beitragen kann.
-   [Tutorium FEM-Beschränkungen hinzufügen](Add_FEM_Constraint_Tutorial/de.md)
-   [Tutorium FEM-Gleichungen hinzufügen](Add_FEM_Equation_Tutorial/de.md)

Ein Entwicklerhandbuch wurde geschrieben, um Power-Usern zu helfen, die komplexe FreeCAD-Codebasis und die Interaktionen zwischen den Kernelementen und den einzelnen Workbenches zu verstehen. Das Buch wird bei github gehostet, so dass mehrere Benutzer dazu beitragen und es auf dem neuesten Stand halten können.

-   [Frühe Vorschau des ebook: Anleitung für Modulentwickler zur FreeCAD-Quelle](https://forum.freecadweb.org/viewtopic.php?t=17581) (Forum-Thread)
-   [FreeCAD Mod Dev Guide](https://github.com/qingfengxia/FreeCAD_Mod_Dev_Guide) (github repository)



## Erweitern der FEM Arbeitsbereichsdokumentation 

-   Weitere Informationen zur Erweiterung oder fehlenden FEM Dokumentation kann im Forum gefunden werden: [Fehlende FEM Dokumentation im Wiki](https://forum.freecadweb.org/viewtopic.php?f=18&t=20823)





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [FEM](Category_FEM.md) > FEM Workbench/de
