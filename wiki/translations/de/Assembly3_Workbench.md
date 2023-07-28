# <img alt="Symbol des Arbeitsbereichs Assembly3" src=images/Assembly3_workbench_icon.svg  style="width:64px;"> Assembly3 Workbench/de


{{TOCright}}



## Einleitung

<img alt="" src=images/Assembly3_workbench_icon.svg  style="width:24px;"> [Assembly3](Assembly3_Workbench/de.md) ist ein [externer Arbeitsbereich](External_workbenches/de.md), der dem Zusammenbau von verschiedenen Körpern dient, die entweder in einem einzigen oder in mehreren separaten Dokumenten gespeichert sind. Der Arbeitsbereich basiert auf einigen Änderungen der Kernfunktionen, die mit FreeCAD 0.19 eingeführt wurden (z.B. [App-Link](App_Link/de.md)), sodass der Arbeitsbereich Assembly3 nicht mit früheren Versionen verwendet werden kann.

Die Hauptmerkmale des Assembly3-Arbeitsbereichs sind

-   ein **dynamischer/interaktiver Löser**. Das heißt, dass man Teile mit der Maus bewegen kann, während der Löser die Bewegung(sfreiheit) einschränkt. Dies erlaubt z. B. ein Rad mit einer Achse zu verbinden und das Rad interaktiv mit der Maus zu drehen.
-   **Verknüpfungen**. Damit kann ein einzelnes Teil, z. B. eine Schraube, mehrfach (an unterschiedlichen Stellen) in einem Zusammenbau (einer Baugruppe) zu verwenden, ohne die Geometrie zu vervielfachen.
-   **externe Verknüpfungen**. Es ist möglich, dass ein FreeCAD-Dokument nur einen Zusammenbau und keine Einzelteile enthält. Alle Bauteile können in separaten Dateien abgelegt sein. Die Dateien könnten auch in einer Bibliothek oder anderswo im Dateisystem abgelegt sein. Die einzige Voraussetzung ist die, dass die Datei geladen sein muss, wenn die Verknüpfung angelegt wird. Nachdem die Verknüpfung erstellt wurde, muss die Datei geöffnet sein, um Verknüpfungen, die die Datei betreffen, zu aktualisieren. Assembly3 erreicht dies, indem es die Dateien bei Bedarf im Hintergrund öffnet.
-   **hierarchische Baugruppen**. Wie im wirklichen Leben darf ein mechanischer Zusammenbau aus Unterbaugruppen bestehen. Auch diese können aus Unterbaugruppen bestehen und so weiter.
-   das **Einfrieren von Baugruppen**. Da die CPU nur eine bestimmte Anzahl gleichzeitiger Bedingungen in Echtzeit verarbeiten kann, ermöglicht das Einfrieren von Baugruppen die Anwendung von Bedingungen sogar für große Baugruppen. Durch das Einfrieren von fertigen Baugruppen oder Bedingungen, die nicht dynamisch verändert werden müssen (z.B. bei verschweißten, vernieteten oder verklebten Bauteilen), werden diese von Aktualisierungsberechnungen ausgenommen und vom Assembly3-Löser als fixierte Geometrie angesehen.

    :   Man beachte, dass andere Herangehensweisen andere Lösungen für dieses Problem anbieten, z. B. der Arbeitsbereich <img alt="" src=images/Assembly4_workbench_icon.svg  style="width:24px;"> [Assembly4](Assembly4_Workbench/de.md).

[Anfang](#top.md)



### Symbolleisten

Seit 2020 enthält der Arbeitsbereich Assembly3 die folgenden Symbolleisten.



#### Hauptwerkzeugleiste

:   <img alt="" src=images/Assembly_New_Assembly.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_New_Group.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_New_Element.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_Import.svg‎‎  style="width:28px;"><img alt="" src=images/AngleDown.svg‎‎  style="width:14px;"><img alt="" src=images/Assembly3_workbench_icon.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_QuickSolve.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_Move.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_AxialMove.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_QuickMove.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_LockMover.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_TogglePartVisibility.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_Trace.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_AutoRecompute.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_SmartRecompute.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_AutoFixElement.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_AutoElementVis.svg‎‎  style="width:28px;"><img alt="" src=images/AngleDown.svg‎‎  style="width:14px;"><img alt="" src=images/Assembly_Add_Workplane.svg‎‎  style="width:28px;"><img alt="" src=images/AngleDown.svg‎‎  style="width:14px;"><img alt="" src=images/Assembly_TreeItemUp.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_TreeItemDown.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintMultiply.svg‎‎  style="width:28px;">


<div class="mw-collapsible mw-collapsed">


:   Die **Hauptwerkzeugleiste** enthält Werkzeuge, die die am häufigsten gebrauchten Funktionen des Arbeitsbereiches abdecken. Die zugehörigen Tastaturkürzel findet man in den Tooltips.


<div class="mw-collapsible-content toccolours">

  - <img alt="" src=images/Assembly_Add_Existing_Part.svg‎‎  style="width:32px;"> [Baugruppe anlegen](Assembly3_CreateAssembly/de.md): Einen Baugruppenordner hinzufügen

  - <img alt="" src=images/Assembly_New_Group.svg‎‎  style="width:32px;"> [Objekte gruppieren](Assembly3_GroupObjects/de.md): Eine Objektgruppe erstellen

  - <img alt="" src=images/Assembly_New_Element.svg‎‎  style="width:32px;"> [Element anlegen](Assembly3_CreateElement/de.md): Ein Element hinzufügen. Dies ist auch im Kontextmenü verfügbar

  - STEP-Dateien importieren. Hier gibt es zwei Einstellungen

  -\* <img alt="" src=images/Assembly_Import.svg‎‎  style="width:32px;"> [STEP-Dateien importieren](Assembly3_ImportFromSTEP/de.md): STEP-Dateien importieren

  -\* <img alt="" src=images/Assembly_ImportMulti.svg‎‎  style="width:32px;"> [Als Mehrfachdokument einfügen](Assembly3_ImportMultiDocument/de.md): STEP-Baugruppen in separate Dokumente importieren

  - <img alt="" src=images/Assembly3_workbench_icon.svg‎‎  style="width:32px;"> [Beziehungen anwenden](Assembly3_ResolveConstraints/de.md): Festgelegte Beziehungen berechnen (auflösen)

  - <img alt="" src=images/Assembly_QuickSolve.svg‎‎  style="width:32px;"> [Schnelle Berechnung](Assembly3_QuickSolve/de.md): Beziehungen schnell berechnen (auflösen)

  - <img alt="" src=images/Assembly_Move.svg‎‎  style="width:32px;"> [Teil bewegen](Assembly3_MovePart/de.md): Teil in 3D bewegen, dies ist ein spezielles Assembly3-Werkzeug

  - <img alt="" src=images/Assembly_AxialMove.svg‎‎  style="width:32px;"> [Axial bewegen](Assembly3_AxialMove/de.md): Teil axial in 3D bewegen, dies ist das übliche Werkzeug, das auch anderen Bereichen von FreeCAD zur Verfügung steht

  - <img alt="" src=images/Assembly_QuickMove.svg‎‎  style="width:32px;"> [Schnelles Bewegen](Assembly3_QuickMove/de.md): Schnelles Bewegen. Dies hängt das im Baum ausgewählte Teil an den Mauszeiger. Es verändert die Position des Teils, mit einem Mausklick.

  -: Oft befinden sich hinzugefügte Teile übereinander gestapelt im Ursprung. Diese Funktion kann benutzt werden, um nicht sichtbare Teile zu erreichen.

  - <img alt="" src=images/Assembly_LockMover.svg‎‎  style="width:32px;"> [Bewegung verhindern](Assembly3_LockMover/de.md): Bewegung ausschließen für fixierte Teile. Umschaltknopf. Wenn dieser abgewählt ist, können auch Teile bewegt werden, die durch die Fixiereinschränkung festgelegt sind.

  - <img alt="" src=images/Assembly_TogglePartVisibility.svg‎‎  style="width:32px;"> [Sichtbarkeit umschalten](Assembly3_TogglePartVisibility/de.md): Dies schaltet die Sichtbarkeit des ausgewählten Teils ein oder aus.

  -: Achtung, dies unterscheidet sich von der Benutzung der Leertaste. Die Benutzung der Leertaste mit ausgewählten Elementen einer Unterbaugruppe in der 3D-Ansicht liefert oft nicht das erwartete Verhalten. In solchen Fällen sollte diese Funktion benutzt werden (oder das Tastenkürzel A, Leertaste)

  - <img alt="" src=images/Assembly_Trace.svg‎‎  style="width:32px;"> [Bewegung aufzeichnen](Assembly3_TracePartMove/de.md):Bewegungsbahn aufzeichnen (TBD)

  - <img alt="" src=images/Assembly_AutoRecompute.svg‎‎  style="width:32px;"> [Automatische Berechnung](Assembly3_AutoRecompute/de.md):Automatische Berechnung. Standardmäßig aktiviert.

  -: Kann deaktiviert werden für die Reparatur von Einschränkungen oder die Fixierung von Teilen, für die der Löser Die Nachricht *\"do not converge\"* ausgibt (z.B. wenn das Teil um 180° gedreht wird)

  - <img alt="" src=images/Assembly_SmartRecompute.svg‎‎  style="width:32px;"> [Smarte Berechnung](Assembly3_SmartRecompute/de.md): Smarte Berechnung. Standardmäßig aktiviert.

  - <img alt="" src=images/Assembly_AutoFixElement.svg‎‎  style="width:32px;"> [Element automatisch fixieren](Assembly3_AutoFixElement/de.md): Automatische Elementfixierung. Experimentelle Funktion in 0.19_pre

  - Element Darstellung. Dies hat zwei Einstellmöglichkeiten:

  -\* <img alt="" src=images/Assembly_AutoElementVis.svg‎‎  style="width:32px;"> [Element automatisch anzeigen](Assembly3_AutoElementVisibility/de.md): Element automatisch anzeigen

  -\* <img alt="" src=images/Assembly_ShowElementCS.svg‎‎  style="width:32px;"> [Element-Koordinatensystem anzeigen](Assembly3_ShowElementCS/de.md): Koordinatensystem des Elements anzeigen

  - Arbeitsebene und Ursprung. Fügt eine Arbeitsebene, eine Platzierung oder einen Ursprung hinzu. Es muss ein Teil ausgewählt sein. Hier gibt es fünf Einstellungen.

  -\* <img alt="" src=images/Assembly_Add_Workplane.svg‎‎  style="width:32px;"> [Arbeitsebene hinzufügen](Assembly3_AddWorkplane/de.md): Arbeitsebene hinzufügen

  -\* <img alt="" src=images/Assembly_Add_WorkplaneXZ.svg‎‎  style="width:32px;"> [XZ-Arbeitsebene hinzufügen](Assembly3_AddXZWorkplane/de.md): XZ-Arbeitsebene hinzufügen

  -\* <img alt="" src=images/Assembly_Add_WorkplaneZY.svg‎‎  style="width:32px;"> [ZY-Arbeitsebene hinzufügen](Assembly3_AddZYWorkplane/de.md):YZ-Arbeitsebene hinzufügen

  -\* <img alt="" src=images/Assembly_Add_Placement.svg‎‎  style="width:32px;"> [Bezugssystem hinzufügen](Assembly3_AddPlacement/de.md): Bezugssystem hinzufügen

  -\* <img alt="" src=images/Assembly_Add_Origin.svg‎‎  style="width:32px;"> [Ursprung hinzufügen](Assembly3_AddOrigin/de.md): Ursprung hinzufügen

  - <img alt="" src=images/Assembly_TreeItemUp.svg‎‎  style="width:32px;"> [Objekt aufwärts bewegen](Assembly3_MoveItemUp/de.md): Ausgewähltes Baumobjekt aufwärts bewegen

  - <img alt="" src=images/Assembly_TreeItemDown.svg‎‎  style="width:32px;"> [Objekt abwärts bewegen](Assembly3_MoveItemDown/de.md): Ausgewähltes Baumobjekt abwärts bewegen

  -: Erlaubt es Teile, Elemente oder Einschränkungen im Baum umzusortieren. Mit \"Element roll over\" (von der ersten zur letzten Position und umgekehrt). Funktioniert nur mit einer einzelnen Auswahl.

  - <img alt="" src=images/Assembly_ConstraintMultiply.svg‎‎  style="width:32px;"> [Beziehung vervielfältigen](Assembly3_MultiplyConstraint/de.md): Beziehung vervielfachen. Dies kann ausgewählt werden, wenn Teile und geeignete Elemente mehrfach vorhanden sind. Es kann z.B. benutzt werden um mehrfach vorhandene Befestigungselemente mehrfach vorhandenen Löchern mit nur einer Beziehung zuzuordnen.


</div>


</div>



#### Hauptwerkzeugleiste für Bedingungen 

:   <img alt="" src=images/Assembly_ConstraintLock.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintAlignment.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintCoincidence.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintAttachment.svg‎‎  style="width:28px;"><img alt="" src=images/AngleDown.svg‎‎  style="width:14px;"><img alt="" src=images/Assembly_ConstraintAxial.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintSameOrientation.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintMultiParallel.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintAngle.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPerpendicular.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointCoincident.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointInPlane.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointOnLine.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointOnCircle.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointsDistance.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointPlaneDistance.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointLineDistance.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintSymmetric.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintMore.svg‎‎  style="width:28px;">


<div class="mw-collapsible mw-collapsed">


:   Einige dieser Werkzeuge sind eigentlich Menüs für weitere Werkzeuge.


<div class="mw-collapsible-content toccolours">

  - <img alt="" src=images/Assembly_ConstraintLock.svg‎‎  style="width:32px;"> [Festsetzen](Assembly3_ConstraintLock/de.md): Zum Fixieren eines oder mehrerer Teile.

  -: Es muss ein (Geometrie-) Element eines Teiles ausgewählt werden.

  -: Wird ein Knotenpunkt oder eine Kante festgesetzt, lässt sich das Teil immer noch frei um den Knotenpunk oder die Kante drehen.

  -: Das Festsetzen einer Fläche fixiert das Teil vollständig.

  - <img alt="" src=images/Assembly_ConstraintAlignment.svg‎‎  style="width:32px;"> [Ebenen ausrichten](Assembly3_ConstraintAlignment/de.md): Zum Ausrichten ebener Flächen zweier oder mehrerer Teile.

  -: Die Flächen werden komplanar ausgerichtet oder optional parallel mit Abstand.

  - <img alt="" src=images/Assembly_ConstraintCoincidence.svg‎‎  style="width:32px;"> [Deckungsgleiche Ebenen](Assembly3_ConstraintCoincidence/de.md): Zum deckungsgleich Festlegen ebener Flächen zweier oder mehrerer Teile.

  -: Die Flächen werden mit deckungsgleichen Ursprüngen komplanar ausgerichtet oder optional parallel mit Abstand.

  - Befestigung. Dies hat zwei Varianten

  -\* <img alt="" src=images/Part_Attachment.svg‎‎  style="width:32px;"> [Befestigung](Assembly3_ConstraintAttachment/de.md): Zum Befestigen eines Teils an ein zweites mittels der ausgewählten (Geometrie-) Elemente.

  -\*: Diese Bedingung verbindet beide Teile starr miteinander.

  -\* <img alt="" src=images/Assembly_ConstraintAttachmentOffset.svg‎‎  style="width:32px;"> [BefestigungVersatz](Assembly3_ConstraintAttachmentOffset/de.md): Wie die Bedingung \"Befestigung\", aber unter Beibehaltung der relativen Ausrichtung der beteiligten Teile durch Anpassung der Offset-Werte eines Elements.

  -\*: Diese Bedingung verbindet beide Teile starr miteinander.

  - <img alt="" src=images/Assembly_ConstraintAxial.svg‎‎  style="width:32px;"> [Axiale Ausrichtung](Assembly3_ConstraintAxial/de.md): Zum axialen Ausrichten (Fluchten) von Kanten und Flächen zweier oder mehrerer Teile.

  -: Die Bedingung akzeptiert:

  -:: lineare Kanten; sie werden kollinear ausgerichtet,

  -:: ebene Flächen; sie werden unter Nutzung ihrer Flächennormalen (Z-Achse) ausgerichtet,

  -:: und zylindrische Flächen; sie werden unter Nutzung ihrer (Z-) Achsrichtung ausgerichtet.

  -: Verschiedene Arten von (Geometrie-) Elementen können gemischt werden.

  - <img alt="" src=images/Assembly_ConstraintSameOrientation.svg‎‎  style="width:32px;"> [Richtungen angleichen](Assembly3_ConstraintSameOrientation/de.md): Zum identischen Ausrichten der (ebenen) Flächen zweier oder mehrerer Teile.

  -: Die Ebenen werden so ausgerichtet, dass ihre (Z-) Achsen in dieselbe Richtung zeigen.

  - <img alt="" src=images/Assembly_ConstraintMultiParallel.svg‎‎  style="width:32px;"> [Mehrfach parallel](Assembly3_ConstraintMultiParallel/de.md): Zum parallelen Ausrichten von ebenen Flächen oder geraden Kanten zweier oder mehrerer Teile.

  - <img alt="" src=images/Assembly_ConstraintAngle.svg‎‎  style="width:32px;"> [Winkel festlegen](Assembly3_ConstraintAngle/de.md): Zum Festlegen des Winkels zwischen ebenen Flächen oder geraden Kanten zweier Teile.

  - <img alt="" src=images/Assembly_ConstraintPerpendicular.svg‎‎  style="width:32px;"> [Rechtwinklig festlegen](Assembly3_ConstraintPerpendicular/de.md): Zum rechtwinkligen Festlegen von ebenen Flächen oder geraden Kanten zweier Teile.

  - <img alt="" src=images/Assembly_ConstraintPointCoincident.svg‎‎  style="width:32px;"> [Punkt auf Punkt](Assembly3_ConstraintPointsCoincident/de.md): Zum deckungsgleich Festlegen zweier Punkte in 2D oder 3D.

  - <img alt="" src=images/Assembly_ConstraintPointInPlane.svg‎‎  style="width:32px;"> [Punkt auf Ebene](Assembly3_ConstraintPointInPlane/de.md): Zum Festlegen eines oder mehrerer Punkte auf einer Ebene (Punktberührung).

  - <img alt="" src=images/Assembly_ConstraintPointOnLine.svg‎‎  style="width:32px;"> [Punkt auf Linie](Assembly3_ConstraintPointOnLine/de.md): Zum Festlegen eines oder mehrerer Punkte auf einer Linie in 2D or 3D.

  - <img alt="" src=images/Assembly_ConstraintPointOnCircle.svg‎‎  style="width:32px;"> [Punkt auf Kreis](Assembly3_ConstraintPointOnCircle/de.md): Zum Festlegen eines oder mehrerer Punkte auf einer durch einen Kreis definierten zylindrischen Fläche.

  -: Achtung! Es muss ein Punkt (irgendein Geometrieelement, dass einen Punkt definieren kann) ausgewählt werden und dann der Kreis (oder eine zylindrische Fläche),

  -: danach können bei Bedarf weitere Punkte hizugefügt werden.

  - <img alt="" src=images/Assembly_ConstraintPointsDistance.svg‎‎  style="width:32px;"> [Punkt zu Punkt Abstand](Assembly3_ConstraintPointsDistance/de.md): Zum Festlegen des Abstands zweier oder mehrerer Punkte zueinander.

  - <img alt="" src=images/Assembly_ConstraintPointPlaneDistance.svg‎‎  style="width:32px;"> [Punkt zu Ebene Abstand](Assembly3_ConstraintPointPlaneDistance/de.md): Zum Festlegen des Abstands eines oder mehrerer Punkte zu einer Ebene.

  - <img alt="" src=images/Assembly_ConstraintPointLineDistance.svg‎‎  style="width:32px;"> [Punkt zu Linie Abstand](Assembly3_ConstraintPointLineDistance/de.md): Zum Festlegen des Abstands eines Punktes zu einer geraden Kante in 2D oder 3D.

  - <img alt="" src=images/Assembly_ConstraintSymmetric.svg‎‎  style="width:32px;"> [Symmetrie festlegen](Assembly3_ConstraintSymmetric/de.md): Zum Festlegen der Symmetrie der (Geometrie-) Elemente zweier Teile bezüglich einer Ebene.

  -: Unterstützte Elemente sind gerade Kanten und ebene Flächen.

  - <img alt="" src=images/Assembly_ConstraintMore.svg‎‎  style="width:32px;"> [Weitere](Assembly3_ConstraintMore/de.md): Werkzeugleisten umschalten für weitere Bedingungen

  -: Nicht wirklich eine Bedingung, sondern ein Umschalter zum Anzeigen/Ausblenden der **Zusatzwerkzeugleisten für Bedingungen**.


</div>


</div>



#### Zusatzwerkzeugleisten für Bedingungen 

:   <img alt="" src=images/Assembly_ConstraintPointDistance.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintEqualAngle.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointsSymmetric.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintGeneral.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintGeneral.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintSymmetricLine.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointsHorizontal.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointsVertical.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintLineHorizontal.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintLineVertical.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintArcLineTangent.svg‎‎  style="width:28px;"> (Assembly3 Constraints2)





:   <img alt="" src=images/Assembly_ConstraintSketchPlane.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintLineLength.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintEqualLength.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintLengthRatio.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintLengthDifference.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintLengthEqualPointLineDistance.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintEqualLineArcLength.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintMidPoint.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintDiameter.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintEqualRadius.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointsProjectDistance.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintEqualPointLineDistance.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintColinear.svg‎‎  style="width:28px;"> (Assembly3 Sketch Constraints)


<div class="mw-collapsible mw-collapsed">


:   Diese kann man durch Auswählen der Schaltfläche **<img src="images/Assembly_ConstraintMore.svg" width=16px> [Weitere](Assembly3_ConstraintMore/de.md)** in der Hauptwerkzeugleiste für Bedingungen aktivieren.


<div class="mw-collapsible-content toccolours">

  - <img alt="" src=images/Assembly_ConstraintPointDistance.svg‎‎  style="width:32px;"> [Abstand zweier Punkte](Assembly3_ConstraintPointDistance/de.md): Zum Festlegen des Abstands zweier Punkte in 2D oder 3D.

  - <img alt="" src=images/Assembly_ConstraintEqualAngle.svg‎‎  style="width:32px;"> [Gleiche Winkel](Assembly3_ConstraintEqualAngle/de.md): Zum Festlegen von gleichen Winkeln zwischen (je) zwei Linien oder (Flächen-) Normalen.

  - <img alt="" src=images/Assembly_ConstraintPointsSymmetric.svg‎‎  style="width:32px;"> [Symmetrische Punkte](Assembly3_ConstraintPointsSymmetric/de.md): Zum Festlegen der symmetrischen Lage zweier Punkte bezüglich einer Ebene.

  - <img alt="" src=images/Assembly_ConstraintGeneral.svg‎‎  style="width:24px;"> () [Horizontale Symmetrie ](Assembly3_ConstraintSymmetricHorizontal/de.md): (noch nicht fertig\...)

  - <img alt="" src=images/Assembly_ConstraintGeneral.svg‎‎  style="width:24px;"> () [Vertikale Symmetrie](Assembly3_ConstraintSymmetricVertical/de.md): (noch nicht fertig\...)

  - <img alt="" src=images/Assembly_ConstraintSymmetricLine.svg‎‎  style="width:32px;"> [Achsensymmetrie](Assembly3_ConstraintSymmetricLine/de.md): Zum Festlegen der symmetrischen Lage zweier Punkte bezüglich einer Symmetrieachse.

  - <img alt="" src=images/Assembly_ConstraintPointsHorizontal.svg‎‎  style="width:32px;"> [Horizontale Punkte](Assembly3_ConstraintPointsHorizontal/de.md): Zum Festlegen einer horizontalen Ausrichtung zweier Punkte, wenn sie auf eine Ebene projiziert werden.

  - <img alt="" src=images/Assembly_ConstraintPointsVertical.svg‎‎  style="width:32px;"> [Vertikale Punkte](Assembly3_ConstraintPointsVertical/de.md): Zum Festlegen einer vertikalen Ausrichtung zweier Punkte, wenn sie auf eine Ebene projiziert werden.

  - <img alt="" src=images/Assembly_ConstraintLineHorizontal.svg‎‎  style="width:32px;"> [Horizontale Linie](Assembly3_ConstraintLineHorizontal/de.md): Zum Festlegen einer horizontalen Ausrichtung eines Liniensegments, wenn es auf eine Ebene projiziert wird.

  - <img alt="" src=images/Assembly_ConstraintLineVertical.svg‎‎  style="width:32px;"> [Vertikale Linie](Assembly3_ConstraintLineVertical/de.md): Zum Festlegen einer vertikalen Ausrichtung eines Liniensegments, wenn es auf eine Ebene projiziert wird.

  - <img alt="" src=images/Assembly_ConstraintArcLineTangent.svg‎‎  style="width:32px;"> [Bogen-Linie-Tangente](Assembly3_ConstraintArcLineTangent/de.md): Zum Festlegen eines tangentiellen Übergangs zwischen einer Linie und dem Start- oder Endpunkt eines Bogens.

  - <img alt="" src=images/Assembly_ConstraintSketchPlane.svg‎‎  style="width:32px;"> [Skizzierebene](Assembly3_ConstraintSketchPlane/de.md): Zum Festlegen einer Arbeitsebene für alle Draft-WB-Elemente innerhalb dieser Beziehung oder dieser Beziehung folgend.

  -: Eine weitere hinzufügte leere Skizzenebene löst die vorherige als Arbeitsebene ab.

  - <img alt="" src=images/Assembly_ConstraintLineLength.svg‎‎  style="width:32px;"> [Linienlänge](Assembly3_ConstraintLineLength/de.md): Zum Festlegen der Länge eines nicht unterteilten Draft-Drahtes.

  - <img alt="" src=images/Assembly_ConstraintEqualLength.svg‎‎  style="width:32px;"> [Gleiche Länge](Assembly3_ConstraintEqualLength/de.md): Zum Festlegen, dass zwei Linien gleich lang sind.

  - <img alt="" src=images/Assembly_ConstraintLengthRatio.svg‎‎  style="width:32px;"> [Längenverhältnis](Assembly3_ConstraintLengthRatio/de.md): Zum Festlegen des Verhältnisses der Längen zweier Linien.

  - <img alt="" src=images/Assembly_ConstraintLengthDifference.svg‎‎  style="width:32px;"> [Längendifferenz](Assembly3_ConstraintLengthDifference/de.md): Zum Festlegen der Differenz der Längen zweier Linien.

  - <img alt="" src=images/Assembly_ConstraintLengthEqualPointLineDistance.svg‎‎  style="width:32px;"> [Länge gleich Punkt-Linie-Abstand](Assembly3_ConstraintLengthEqualPointLineDistance/de.md): Zum Festlegen, dass der Abstand eines Punktes zu einer Linie gleich der Länge einer weiteren Linie ist.

  - <img alt="" src=images/Assembly_ConstraintGeneral.svg‎‎  style="width:24px;"> ( <img alt="" src=images/Assembly_ConstraintEqualLineArcLength.svg‎‎  style="width:32px;"> )[Linien- gleich Bogenlänge](Assembly3_ConstraintEqualLineArcLength/de.md): Zum Festlegen, dass die Länge einer Linie gleich der Länge enes Bogens ist.

  - <img alt="" src=images/Assembly_ConstraintMidPoint.svg‎‎  style="width:32px;"> [Mittelpunkt](Assembly3_ConstraintMidPoint/de.md): Zum Festlegen eines Punktes in der Mitte einer Linie.

  - <img alt="" src=images/Assembly_ConstraintDiameter.svg‎‎  style="width:32px;"> [Durchmesser](Assembly3_ConstraintDiameter/de.md): Zum Festlegen des Durchmessers eines Kreises oder Bogens.

  - <img alt="" src=images/Assembly_ConstraintEqualRadius.svg‎‎  style="width:32px;"> [Gleicher Radius](Assembly3_ConstraintEqualRadius/de.md): Zum Festlegen, dass die Radien zweier Kreise oder Bögen gleich groß sind.

  - <img alt="" src=images/Assembly_ConstraintPointsProjectDistance.svg‎‎  style="width:32px;"> [Projizierter Punktabstand](Assembly3_ConstraintPointsProjectDistance/de.md): Zum Festlegen des Abstands zweier Punkte, die auf eine Linie projiziert werden.

  - <img alt="" src=images/Assembly_ConstraintEqualPointLineDistance.svg‎‎  style="width:32px;"> [Gleicher Punkt-Linien-Abstand](Assembly3_ConstraintEqualPointLineDistance/de.md): Zum Festlegen, dass der Abstand eines Punktes zu einer Linie gleich dem Abstand eines weiteren Punktes zu einer anderen Linie ist.

  - <img alt="" src=images/Assembly_ConstraintColinear.svg‎‎  style="width:32px;"> [Kollinear](Assembly3_ConstraintColinear/de.md): Hinzufügen einer \"kollinearen\" Beschränkung um zwei Linien kollinear zu machen.


</div>


</div>


:   Die **Werkzeugleisten der Bedingungen** sind die Hauptschnittstelle für den Zusammenzubau von Einzelteilen.
:   Sie sind standardmäßig ausgegraut, werden aber aktiviert, sobald mindestens eine Fläche, eine Linie oder ein Punkt eines Teiles ausgewählt wird.
:   Normalerweise werden erst die zu verbindenden Elemente ausgewählt und danach die Art der Bedingung.
:   Die unterschiedlich gefärbten Rahmen kennzeichnen unterschiedliche Eigenschaften der Bedingungen:

    :   ob 2D / 3D oder ob mehr als 2 Elemente zusammengefügt werden können.
:   Eine ausführliche Beschreibung ist im GitHub-Wiki zu finden.



#### Navigationswerkzeugleiste

:   <img alt="" src=images/Assembly_GotoRelation.svg‎‎  style="width:28px;"> <img alt="" src=images/LinkSelect.svg‎‎  style="width:28px;"> <img alt="" src=images/LinkSelectFinal.svg‎‎  style="width:28px;">


<div class="mw-collapsible mw-collapsed">


:   Diese Funktionen sind nützlich, wenn eine Baugruppe mit einer Hierarchie von verknüpften externen Dateien bearbeitet wird.


<div class="mw-collapsible-content toccolours">

  - <img alt="" src=images/Assembly_GotoRelation.svg  style="width:32px;"> [Zur Beziehung gehen](Assembly3_GoToRelation/de.md): Zeigt die Beziehungsgruppe an (standardmäßig ausgeblendet) und wählt ein Beziehungsobjekt aus.

  - <img alt="" src=images/Std_LinkSelectLinked.svg  style="width:32px;"> [Verknüpftes Objekt auswählen](Std_LinkSelectLinked/de.md): Wählt das verknüpfte Objekt aus und wechselt zu dessen Dokument. {{Version/de|0.19}}

  - <img alt="" src=images/Std_LinkSelectLinkedFinal.svg  style="width:32px;"> [Letztes verknüpftes Objekt auswählen](Std_LinkSelectLinkedFinal/de.md): Wählt das Objekt am Ende der Verknüpfungskette aus und wechselt zu dessen Dokument. {{Version/de|0.19}}


</div>


</div>



#### Messwerkzeugleiste

:   <img alt="" src=images/Assembly_MeasurePointDistance.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_MeasurePointLineDistance.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_MeasurePointPlaneDistance.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_MeasureAngle.svg‎‎  style="width:28px;">


<div class="mw-collapsible mw-collapsed">


:   Die **Messwerkzeugleiste** fügt Funktionen zum Messen des Abstands oder des Winkels zwischen zwei Objekten hinzu


<div class="mw-collapsible-content toccolours">

  - <img alt="" src=images/Assembly_MeasurePointDistance.svg‎‎  style="width:32px;"> [Punkte messen](Assembly3_MeasurePoints/de.md): Füge ein \"Punkte messen\" hinzu, um den Abstand zwischen zwei Punkten in 2D oder 3D zu messen.

  - <img alt="" src=images/Assembly_MeasurePointLineDistance.svg‎‎  style="width:32px;"> [Punkt zu Linie messen](Assembly3_MeasurePointLine/de.md): Füge ein \"Punkt zu Linie messen\" hinzu, um den Abstand zwischen einem Punkt und einer linearen Kante in 2D oder 3D zu messen.

  - <img alt="" src=images/Assembly_MeasurePointPlaneDistance.svg‎‎  style="width:32px;"> [Punkt zu Ebene messen](Assembly3_MeasurePointPlane/de.md): Füge ein \"Punkt zu Ebene messen\" hinzu, um den Abstand zwischen einem Punkt und einer Ebene zu messen.

  - <img alt="" src=images/Assembly_MeasureAngle.svg‎‎  style="width:32px;"> [Winkel messen](Assembly3_MeasureAngle/de.md): Füge ein \"Winkel messen\" hinzu, um den Winkel von ebenen Flächen oder linearen Kanten zweier Teile zu messen.

:   Es gibt keine Funktion um einen Radius oder Durchmesser zu messen.
:   Die Messwerkzeuge überdauern Teiländerungen, z.B. den Abstand zwischen Kanten eines Würfels, wenn die die Größe des Würfels geändert wird.
:   Wie die Beschränkungen werden diese Berechnungen in Echtzeit ausgeführt und bei jeder Änderung aktualisiert. Hinter den Kulissen ist die Funktion den [Beschränkungen](#Constraints.md) sehr ähnlich. Der Abstand oder Winkel zwischen [Elemente](#Elemente.md) wird auf die gleiche Weise berechnet wie bei [Beschränkungen](#Beschränkungen.md). Die Anzeige im Baum funktioniert auf die gleiche Weise.


</div>


</div>

Wie gewohnt, kann die Werkzeugleiste geändert und einzelne Werkzeuge hinzugefügt oder entfernt werden. Im Assembly3-Menü sind weitere Funktionen vorhanden, die sich nicht in den Werkzeugleisten befinden.

[Anfang](#top.md)



### Bedingungen

Der Konstrukteur benutzt Bedingungen (auch Randbedingung, Einschränkung, Beschränkung, Zwang, Zwangsbedingung, Festlegung genannt) um zwei Teile zueinander auszurichten. Die Kunst besteht darin, die Bedingungen zu wählen, die am besten zu den jeweiligen Anforderungen passen. Jeder bestimmte Freiheitsgrad (**D**egree **O**f **F**reedom) sollte theoretisch nur einmal zwischen zwei Objekten festgelegt sein, aber in der Praxis vieler CAD-Werkzeuge erzeugen die ausgewählten Bedingungen überbestimmte Kombinationen, die oft durch komplexe Algorithmen ausgeglichen werden können, manchmal aber auch nicht. Assembly3 benutzt solche Algorithmen, um überzählige Bedingungen zu entdecken und auszugleichen, aber sie sind bisher noch nicht besonders ausgereift. Am besten vermeidet man Schwierigkeiten im Umgang mit Assembly3-Bedingungen, indem man darauf achtet, wieviele Freiheitsgrade schon bestimmt sind und welche durch weitere Bedingungen noch festzulegen sind. Kein Teil sollte durch Bedingungen so verbunden werden, dass mehr als 6 Freiheitsgrade festlegt werden.

Hinweis: Wenn der Gleichungslöser auf eine Kombination trifft, die nicht gelöst werden kann, gibt er eine Fehlermeldung aus. Es ist für den Löser sehr schwierig, die Ursache des Problems herauszufinden, sodass man normalerweise aus dem angegebenen Fehler nicht klar erkennen kann, *wo* sich das Problem befindet. Bei größeren Baugruppen kann dies zu aufwändigen Fehlersuchen führen. Leider gibt es keinen einfachen Weg, diese zu vermeiden. Allerdings hilft es, im Blick zu behalten, wie das System funktioniert (siehe z.B. [Elemente](#Elemente.md) weiter unten), eindeutige Namen für alle beteiligten Komponenten zu verwenden und nur dann weitere Bedingungen hinzuzufügen, wenn der Gleichungslöser die aktuelle Baugruppe erfolgreich berechnen kann. Sehr hilfreich, um ein Problem zu finden, ist die Funktion \"ContexMenu/Deactivate\" der jeweiligen Bedingung.

Assembly3-Bedingungen definieren, wie die Möglichkeiten der Positionierung oder Orientierung zwischen zwei [Elementen](#Elemente.md) reduziert werden. Einige Bedingungen arbeiten sogar mit mehr als zwei Elementen. Ein Element kann eine Fläche, eine Linie oder Kante oder ein Punkt eines Teils sein. Im Allgemeinen werden Bedingungen definiert, indem man erst die gewünschten Elemente und dann die Bedingung aus einer der [Werkzeugleisten](#Werkzeugleisten.md) für Bedingungen auswählt.

-   Fixiert 6 Freiheitsgrade, 0 bleiben unbestimmt:
    -   **Fixierung (Schloss)**: Die Fixiereinschränkung legt alle Freiheitsgrade einer Fläche. Sie sollte in jedem Zusammenbau zur Festlegung eines Basisteils genutzt werden. Es ist sinnvoll auch gleich die \"Bewegung ausschließen für fixierte Teile\"-Funktion (in der Werkzeugleiste) zu aktivieren, um damit ein unbeabsichtigtes Verschieben zu verhindern. In der Regel ist es egal welche Fläche, Linie oder Punkt benutzt wird um ein Teil zu fixieren. Man beachte, dass die Fixierung nur auf den aktuellen Zusammenbau wirkt, d.h. im Falle einer Unterbaugruppe braucht der übergeordnete Zusammenbau noch ein eigenes fixiertes Teil.
    -   **Anhang**: Legt die Koordinatensysteme der ausgewählten Elemente (zweier oder mehrerer Teile) deckungsgleich aufeinander. Dies ist die für die Berechnung günstigste Funktion und sollte, wo immer möglich, benutzt werden. Man beachte, dass man die Eigenschaften der Elemente nutzen kann, um Abstände und Winkel einzustellen, wenn die [Elemente](#Elements.md) nicht optimal zueinander ausgerichtet sind.
-   Fixiert 5 Freiheitsgrade, 1 bleibt unbestimmt:
    -   **Lagegleiche Ebenen**: fixes Tx,Ty,Tz, Rx,Ry. Only Rz is free. There remains the rotation around the normal passing through the ''center of the plane''.
-   Fixiert 4 Freiheitsgrade, 2 bleiben unbestimmt:
    -   **Axial Alignment**: fixes Tx,Ty, Rx,Ry. Only Tz, Rz are free. There remains the rotation around the axis of the shape and the translation along this same axis. Two *PointOnLine* constraints (if the two points are different) give the same result. The \''Colinear\'' constraint too.
    -   **PointOnLine**: This eliminates the translation and rotation along the normals to the reference line. Only the translation and rotation along the line axis is allowed.
-   Fixiert 3 Freiheitsgrade, 3 bleiben unbestimmt:
    -   **Same Orientation**: fixes Rx,Rz,Rz. All T\'s remain free.
    -   **Points Coincident**: fixes Tx,Ty,Tz. All R\'s remain free.
    -   **PointOnPoint** constraint eliminates the 3 translations.
    -   **Plane Alignment**: fixes Tz, Rx,Ry (plane motion) and Rz. This eliminates the translation along the normal to the reference plane and the two rotations around the axes of this plane.
-   Fixiert 2 Freiheitsgrade, 4 bleiben unbestimmt:
    -   **Multi Parallel**: fixes Rx,Ry. all T\'s and Rz remain. This eliminates the two rotations around the axes of the reference plane.
-   Fixiert 1 Freiheitsgrad, 5 bleiben unbestimmt:
    -   **Points in Plane**: Fixes Tz. This eliminates the translation along the normal to the reference plane.
    -   **Points Distance**: fixes the distance between the Element origins.

        :   This gives you more freedom than *Points in Plane*

Other

-   **Points on Circle**: fixes Tz and partially Tx,Ty. Freezes the point translation (or several points) on a circle or disk area. You must pick the circle second. This leaves all rotations free and gives limited translation in the circle reference plane.

\'\': Hinweis: In der folgenden Liste werden Tx,Ty,Tz und Rx,Ry,Rz benutzt, um Translations- (Verschiebe-) und Rotations- (Dreh-) Bewegungen bezogen auf die Koordinatenachsen des betreffenden Elements zu beschreiben. Dies ist nicht immer exakt oder vollständig beschrieben, wie z.B. wenn es eine Linie betrifft, ist es nicht definiert, ob sie in X-Richtung, Y-Richtung oder einem beliebigen Winkel dazwischen verläuft. Das System sorgt eher für Kürze und einfache Vergleichbarkeit, als für eine korrekte aber komplexere Definition. So ist Z normalerweise die Richtung der Flächennormalen der betroffenen Flächen.

[Zum Anfang](#top.md)



### Elemente

Elemente wird in der Arbeitsumgebung Assembly3 als besonderer Begriff benutzt, und Elemente zu verstehen ist wichtig für das Verständnis, wie Assembly3 benutzt werden sollte.

Es ist hilfreich ein Element als einen generellen Begriff für \'auswählbarer Bestandteil\' eines Teiles zu sehen wie z.B. eine Fläche , eine Kante, ein Kreis, eine Ecke oder ein Punkt. Dies sind die Elemente, die ausgewählt werden, um Teile zueinander in Beziehung zu setzen. Im Baum hat ein \'Assembly\'-Ordner drei Unterordner. Neben \'Parts\' und \'Constraints\' gibt es einen Ordner namens \'Elements\', der leer bleibt, solange keine Einschränkungen hinzugefügt werden. Wenn eine Einschränkungen hinzugefügt wird, erhält sie selbst zwei (oder mehr) Blätter, dies sind die ausgewählten Elemente. Auch werden diese Elemente dem \'Elements\'-Ordner hinzugefügt, der eine Liste aller im Zusammenbau benutzten Elemente darstellt. Es ist eine gute Idee, ihre Namen zu ändern (mit der F2-Taste), besonders in größeren Zusammenbauten.

Sehen wir uns ein Beispiel an

:   Es wird eine neue Datei erstellt und mit der Part-Arbeitsumgebung ein Würfel und ein Zylinder hinzugefügt. Es soll der Zylinder auf den Würfel gestellt werden. Zuerst wird das Basisteil fixiert, in diesem Fall der Würfel. Dazu wird die Unterseite des Würfels und danach die Fixiereinschränkung (das erste Symbol in der [Werkzeugleiste](#Toolbars.md) der Haupteinschränkungen) ausgewählt. Es werden die Oberseite des Würfels und die Oberseite des Zylinders ausgewählt. Danach wird die \'Plane Coincident\'-Einschränkung ausgewählt. Nun hat sich der Zylinder in den Würfel hinein bewegt und im Baum wurde ein neues Blatt mit zwei Kindknoten unter \'Constraints\' hinzugefügt. Zusätzlich wurden die selben zwei Kindknoten unter \'Elements\' hinzugefügt. Falls der Zylinder im Inneren des Würfels liegt, anstatt auf seiner Oberseite wird dies als nächstes korrigiert: Den Kindknoten unter \'Constraints\' auswählen, zu dem die Zylinderfläche gehört, und mit einem Rechtsklick im Kontextmenü \'Flip Part\' auswählen. Nun wurde der Zylinder auf die Würfeloberseite gestapelt.

Der wesentliche Punkt für das Verständnis ist, dass die Randbedingung mit Verknüpfungen zu Elementen in der Liste des \"Elements\"-Baumabschnitts arbeitet. Dies erlaubt, die Bindungsstruktur intakt zu halten, während die Teile geändert werden. Dies ist ohne ein Beispiel sehr schwer zu erkennen.

Zurück zum obigen Beispiel

:   Achtung: Es sollte darauf geachtet werden, dass die Fixierbedingung zum Würfel hinzugefügt wurde, andernfalls wird es merkwürdig aussehen.
:   Im CAD-Fenster wird eine weitere Fläche des Würfels ausgewählt. Ab jetzt wird nur noch in der Baumansicht gearbeitet. In der Baumansicht wird die Maus verwendet; der Würfel sollte ausgewählt sein. Der Würfel wird per \'Drag&Drop\' auf den \'Elements\'-Ordner gezogen und abgelegt. Das Ablegen sollte auf dem Namen des \'Elements\' erfolgen, nicht anderswo im Ordner - warum, sehen wir später. Es sollte erkennbar sein, dass ein weiteres Element zur \'Elements\'-Liste hinzugefügt wurde. Nun wird im \'Constraints\'-Ordner der Kindknoten der Würfelfläche in der Bedingung \'Plane Coincident\' ausgewählt und aus der Liste entfernt. Die Bedingung ist nun mit einem Ausrufezeichen gekennzeichnet, da ihr ein Element fehlt. Hierbei ist zu beachten, dass ein Element, das aus der Bedingung entfernt wurde, *nicht* auch aus der (Element-)Liste gelöscht wurde. Der Grund dafür ist, dass in der Einschränkung nur ein Verweis zum Element in der Liste abgelegt wird. Nun kann das neu zur \'Elements\'-Liste hinzugefügte Element per \'drag&drop\' auf die Bedingung \'Plane Coincident\' gezogen und abgelegt werden. Damit bewegt sich der Zylinder zu der anderen Fläche des Würfels, die vorher ausgewählt wurde. Wenn der Zylinder im Inneren des Würfels liegt, muss nochmals im Kontextmenü \'flip part\' ausgewählt werden.

Das Beispiel zeigt, dass man die zur Randbedingung gehörenden Elemente austauschen kann, ohne die Bedingung zu Löschen. Auf dieselbe Weise kann der Zylinder auch zu einem ganz anderen Teil bewegt werden. Nachdem man etwas mit diesem Beispiel herumgespielt hat, wird man noch zusätzliche Möglichkeiten entdecken, wie z.B.:

-   Wenn ein Element in der Liste umbenannt wird, wird es auch in allen Bedingungen umbenannt
-   Ein Element der Liste kann für mehrere Randbedingungen verwendet werden.
-   Das Eigenschaftenfenster eines Elements kann verwendet werden, um **Versatzangaben** (Offsets) hinzuzufügen. Z.B. kann hiermit der Zylinder auf unterschiedliche Positionen auf der gewählten Würfelfläche platziert werden.
-   Man kann die Schaltfläche \'Show Element Coordinate System\' der Hauptwerkzeugleiste benutzen, um zu sehen, wie sich \'Flip Part\' und \'Flip Element\' aus dem Kontextmenü auswirken. Nicht vergessen, die Änderungen im Eigenschaftenfenster zu beobachten.
-   Eine Randbedingung kann auch in einer ganz anderen Reihenfolge hinzugefügt werden: Zuerst werden Elemente zur \'Elements\'-Liste hinzugefügt (Eine Benennung ist hier nützlich, z.B. \"Würfel-Oberseite\" oder \"Würfel-Unterseite\"), dann wird eine Bedingung hinzugefügt, ohne etwas auszuwählen - Das ergibt eine leere Randbedingung. Dann werden Elemente aus der Liste per \'Drag&Drop\' hierher gezogen und abgelegt. Das Ergebnis ist das gleiche, wie in dem ersten Beispiel. Nach dieser Übung sollte klar sein, wie Randbedingungen und Elemente zusammenarbeiten.
-   Eine bestehende Bedingung zwischen bestehenden Elementen kann einfach ausgetauscht werden, indem man eine andere Auswahl in der \'ConstraintType\'-Eigenschaft im Eigenschaftenfenster trifft.

[Zum Anfang](#top.md)



## Kompatibilität

Assembly3 wurde vom [Assembly2](Assembly2_Workbench.md) inspiriert, ist aber nicht mit diesem kompatibel. Wenn du ältere Modelle in Assembly2 erstellt hast, solltest du bei FreeCAD 0.16 bleiben und Assembly2 dort verwenden.

Neue Modelle, die mit Assembly3 entwickelt wurden, sollten nur mit diesem Arbeitsbereich geöffnet und bearbeitet werden.

Obwohl sie möglicherweise ähnliche Werkzeuge haben, ist Assembly3 nicht kompatibel mit [A2plus](A2plus_Workbench/de.md) noch mit [Assembly4](Assembly4_Workbench/de.md). Modelle, die mit diesen Arbeitsbereichen erstellt wurden, sollten nur mit dem jeweiligen Arbeitsbereich geöffnet werden.

[Zum Anfang](#top.md)

## Installation

Der Arbeitsbereich [Assembly3](Assembly3_Workbench/de.md) ist (seit März 2022) über den [Addon-Manager](Std_AddonMgr/de.md) verfügbar. Jede Abhängigkeit von Assembly3 zu (Modulen von) Drittanbietern sollte automatisch durch den Addon_Manager verwaltet werden.



#### Alternative Installationen 

Es gibt 2 alternative Wege Assembly3 zu installieren:

-   Eine spezielle Abspaltung von FreeCAD von realthunder; siehe [hier](https://github.com/realthunder/FreeCAD/releases). Dieser Fork basiert auf einem bestimmten Commit des Master-Zweiges von FreeCAD, hat aber auch zusätzliche Funktionen, die derzeit im Master-Zweig nicht vorhanden sind. Da dieser Fork auf einem bestimmten Entwicklungs-Snapshot basiert, verfügt er nicht über die neuesten Funktionen, die täglich in den Master-Zweig eingebunden werden.
-   Das Entwicklungs-[App-Image](AppImage/de.md); dieses basiert auf dem aktuellen Master-Zweig und beinhaltet die Abhängigkeiten, die für die Arbeit mit Assembly3 benötigt werden, wie z.B. den SolveSpace Solver.

Da das App-Image nur unter Linux funktioniert, ist für Windows-Benutzer (die gerne eine alternative Assembly3-Installation hätten) die erste Option die einzige Möglichkeit, Assembly3 zu testen (realthunder\'s fork) .

[Zum Anfang](#top.md)



## GewusstWie



### Loslegen

Es gibt viele Wege einen Zusammenbau mit Assembly3 zu erstellen. Hier ist der einfachste.

:   <img alt="" src=images/Assembly3_Example-GettingStarted.jpg  style="width:600px;">
:   *Endergebnis des \'Wie man startet\'-Beispiels. In dem Bild ist die Arbeitsumgebung Assembly3 ausgewählt, sodass ihre unterschiedlichen Werkzeugleisten sichtbar sind. Beachte, dass die vertikale \'TabBar\'-Leiste links neben der Baumansicht eine zusätzliche Arbeitsumgebung ist und nicht Bestandteil von Standard-FreeCAD (aber mit dem Addon-Manager installiert werden kann).*

-   Schaltfläche **<img src="images/Std_New.svg" width=16px> [Neu](Std_New/de.md)** drücken, um eine neue FreeCAD-Datei zu erstellen
-   Zur Arbeitsumgebung <img alt="" src=images/Assembly3_workbench_icon.svg  style="width:16px;"> [Assembly3](Assembly3_Workbench/de.md) wechseln
-   Schaltfläche **<img src="images/Assembly_New_Assembly.svg‎‎" width=16px> [Baugruppe anlegen](Assembly3_CreateAssembly/de.md)** drücken
-   Zur <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Part Arbeitsumgebung](Part_Workbench/de.md) wechseln und einen <img alt="" src=images/Part_Cylinder.svg  style="width:16px;"> [Zylinder](Part_Cylinder/de.md) und einen <img alt="" src=images/Part_Box.svg  style="width:16px;"> [Würfel](Part_Box/de.md) hinzufügen
-   Die Datei unter einem selbstgewählten Dateinamen <img alt="" src=images/Std_Save.svg  style="width:16px;"> [speichern](Std_Save/de.md). Anschließend die Datei <img alt="" src=images/Std_CloseActiveWindow.svg  style="width:16px;"> [schließen](Std_CloseActiveWindow/de.md) und erneut <img alt="" src=images/Std_Open.svg  style="width:16px;"> [öffnen](Std_Open/de.md)

Die Baumansicht sollte so aussehen (0.20.pre and Link Branch):

<img alt="" src=images/Assembly3_Example-Tree-01.png  style="width:300px;"> <img alt="" src=images/Assembly3_Example-Tree-02.png  style="width:280px;">

-   Nun mit der Maus per *Drag&Drop* **Zylinder** und **Würfel** auf den **Parts**-Ordner ziehen und ablegen. Beide werden in den Ordner verschoben.

    :   Das ist der schnellste Weg und geeignet für einfache Fälle wie diesen. Ein besserer Weg geht über die Nutzung von Link-Objekten:
    :   **Würfel** sowie **Zylinder** auswählen und dann den Befehl <img alt="" src=images/Std_LinkMake.svg  style="width:16px;"> [Link erstellen](Std_LinkMake/de.md) entweder aus dem **Kontextmenü** (-\> LinkActions -\> MakeLink) oder aus der Symbolleiste **Struktur** auswählen
    :   Dies fügt zwei Link-Objekte hinzu. Diese werden dann auf den **Parts**-Ordner gezogen und abgelegt
-   Anklicken der beiden Oberseiten von Zylinder und Würfel (Strg gedrückt halten (Cmd am Mac))
-   Zur Arbeitsumgebung <img alt="" src=images/Assembly3_workbench_icon.svg  style="width:16px;"> [Assembly3](Assembly3_Workbench/de.md) wechseln.
-   Schaltfläche **<img src="images/Assembly_ConstraintCoincidence.svg‎‎" width=16px> [Deckungsgleiche Ebenen](Assembly3_ConstraintCoincidence/de.md)** aus der [Hauptwerkzeugleiste für Beschränkungen](#Main_Constraints_Toolbar/de.md) auswählen.

Jetzt sollten beide Teile miteinander verbunden sein und der Baum sollte so aussehen (0.20.pre and Link Branch):

<img alt="" src=images/Assembly3_Example-Tree-03.png  style="width:300px;"> <img alt="" src=images/Assembly3_Example-Tree-04.png  style="width:280px;">

-   Rechtsklick auf \"\_Element\" (eins der beiden) und \"Flip Part\" auswählen.

Nun sollte sich der Zylinder oben auf dem Würfel befinden. Wenn das Gebilde auf dem Kopf steht, einen Schritt zurückgehen und \"Flip Part\" auf dem anderen Element auswählen.

:   Bisher wurde ein wichtiger Schritt ausgelassen, den man besonders für größere Baugruppen nicht vergessen sollte: Das Fixieren eines Basisteils.
:   Das bedeutet ein Teil zu definieren, das nicht durch Einschränkungen bewegt werden sollte. In diesem Fall wird dafür der Würfel benutzt:
    -   Auswahl der Unterseite des **Würfels**. Nur die Unterseite, nicht der ganze **Würfel**
    -   Schaltfläche **<img src="images/Assembly_ConstraintLock.svg‎‎" width=16px> [Festsetzen](Assembly3_ConstraintLock/de.md)** aus der [Hauptwerkzeugleiste für Beschränkungen](#Main_Constraints_Toolbar/de.md) auswählen.

Fertig.

Der fertige Baugruppenbaum sollte so aussehen (0.20.pre and Link Branch):

<img alt="" src=images/Assembly3_Example-Tree-05.png  style="width:300px;"> <img alt="" src=images/Assembly3_Example-Tree-06.png  style="width:280px;">:

Wer möchte, kann die Bedingung **Festsetzen** im Baum nach oben verschieben. Dafür wird die Schaltfläche **<img src="images/Assembly_TreeItemUp.svg‎‎" width=16px> [Objekt nach oben bewegen](Assembly3_MoveItemUp/de.md)** in der [Hauptwerkzeugleiste](#Hauptwerkzeugleiste.md) verwendet.

**Hinweis:** Alle neuen externen Dateien müssen mindestens einmal **gespeichert**, **geschlossen** und erneut **geöffnet** werden, damit Assembly3 sie finden kann.

:   Andernfalls kann FreeCAD dem Arbeitsbereich Assembly3 kein Datei-Handle übergeben und dieser kann das neue Teil nicht finden.
:   Auch wenn sich alle Teile in derselben Datei befinden, sollte man diese Datei **speichern**, **schließen** und erneut **öffnen**.

[Anfang](#top.md)



### Einen Versatz hinzufügen 

Assembly3 sieht es nicht vor, mit den Bedingungen auch einen Versatz festzulegen, wie es der Arbeitsbereich [A2plus](A2plus_Workbench/de.md) oder andere CAD-Werkzeuge vorsehen. Stattdessen verwendet er ein allgemeineres und flexibleres System, um Abstände, Versätze und sogar Winkel festzulegen.

-   Einen Versatz in den Eigenschaften eines [Elements](#Elemente.md) einer [Bedingung](#Bedingungen.md) festlegen.

    :   Man kann wählen, welches der beiden man verwenden möchte.

Beispiel:

-   2 Würfel zu einer Baugruppe hinzufügen und ihre Seitenflächen auswählen.
-   Bedingung \"Deckungsgleiche Ebenen\" auswählen. Die Würfel werden ineinanderliegend zusammengefügt.
-   Ein Element und anschließend *KontextMenü/Flip part* auswählen. Die Würfel werden jetzt Seite an Seite zusammengefügt.
-   Eine Element auswählen und anschließend seine Eigenschaft Offset/Position/z und auf 5mm setzen. Die Würfel sind nun 5mm voneinander entfernt.

  - Dies testet man auch mit den anderen Koordinaten der Position oder den Eigenschaften Winkel oder Achse. Man sollte auch überprüfen, ob man das gleiche Ergebnis erhält, wenn das andere Element verwendet wird. Diese Herangehensweise gilt auch für alle anderen Bedingungen.

[Anfang](#top.md)



### Fehler des Lösers beheben 

Diese treten häufig auf, wenn Einzelteile überbestimmt sind, d.h. wenn mehr als 6 Freiheitsgrade festgelegt sind.

Der einfachste Weg das Problem zu finden, ist das Anklicken der entsprechenden Bedingung im Konstruktionsbaum und die Auswahl von *ContextMenu/Disable* mit anschließender Neuberechnung. Es hilft zu wissen, welche Bedingungen zuletzt hinzugefügt wurden, bevor die Berechnung des Gleichungslösers fehlgeschlagen ist, um diese einfach zurückzunehmen.

Achtung: Da Assembly3 hinter den Kulissen versucht überbestimmte Teile auszugleichen, kann es vorkommen, dass eine neue Bedingung scheinbar eine Fehlfunktion auslöst, die tatsächliche Ursache aber an einer anderen Stelle zu finden ist. Bevor man nun alles löscht und von vorne beginnt, sollte man daran denken, dass man Elemente wiederverwenden kann. Wenn sie benannt wurden, können die erforderlichen Elemente leicht ermittelt und die Bedingungen erneut aufgebaut werden, ohne die 3D-Ansicht zu verwenden. Siehe auch obigen Abschnitt [Elemente](#Elemente.md).

[Anfang](#top.md)



### Ein Bauteil ersetzen oder einen Dateinamen umbenennen 

Wenn ein Bauteil entfernt wird oder wenn sich ein Dateiname ändert, \"zerbricht\" die Baugruppe und kann nicht mehr berechnet werden; der Löser gibt die Meldung \"Inconsistent constraints\" (Widersprüchliche Bedingungen) aus. Der Löser kennzeichnet ungültige Elemente und Bedingungen mit einem Fragezeichen im Baum.

Ein Weg, dieses zu beheben ist, einfach alle ungültigen Bedingungen und Elemente zu löschen, das neue Bauteil zu importieren und alles erneut auzubauen. Aber es gibt einen besseren Weg:

-   Eine Datei umbenennen
    1.  Einen Dateimanager benutzen, um die Datei zu kopieren, umbenannt werden soll. Anschließend gibt man der Kopie den neuen Namen.
    2.  Öffnen der Kopie in FreeCAD. Der Zusammenbau und die alte Datei sollten auch geöffnet sein.
    3.  Das alte Objekt im Baum auswählen und per Klick die Eigenschaft \'Linked object\' ändern (sie enthält den alten Dateinamen).
    4.  Ein Dialogfenster mit einer Auflistung aller geöffneten Teile öffnet sich. Es zeigt die Dateinamen und Objekte aller Teile an. Das alte Teil und das zugehörige Objekt sind ausgewählt. Das umbenannte Teil wird im Baum abgelegt und das gleiche Objekt des neuen Teiles ausgewählt. Danach die Auswahl bestätigen.
    5.  Die alte Datei aus dem Baum entfernen. Die Datei kann jetzt auch gelöscht werden.
    6.  Die Einschränkungen und Elemente des alten Teiles sind ungültig geworden. Jetzt wird die Einschränkung oder die \'Elements\'-Liste im Baum geöffnet und anschließend nacheinander
        -   Jede Element-Fläche am neuen Teil ausgewählt. Ein Objekt im Baum wird hervorgehoben.
        -   Das Objekt per \'drag&drop\' auf das alte Element ziehen und ablegen (entweder in der \'Elements\'-Liste oder in einer der Einschränkungen, wo es benutzt wurde). Das Element sollte jetzt gültig werden.
        -   Diesen Ablauf für die übrigen Elemente wiederholen. Oft reicht ein einzelnes Element dafür aus, dass Assembly3 die übrigen Elemente des Teiles automatisch erkennen kann.
        -   Falls ein Element ausversehen einer falschen Fläche zugeordnet wurde, wird die Zuordnung einfach mit der korrekten Fläche wiederholt.
    7.  Ändern des Objektnamens in FreeCAD, falls gewünscht

-   Ein Bauteil durch ein anderes ersetzen

    :   *Eins das dem originalen Bauteil ähnlich genug ist, dass die originalen Bedingungen noch sinnvoll sind.*

    1.  Das alte Bauteil aus dem Baum entfernen. Die Datei kann jetzt auch gelöscht werden.
    2.  Die Bedingungen und Elemente des alten Teiles sind ungültig geworden. Jetzt wird die Bedingung oder die \'Elements\'-Liste im Baum geöffnet.
        -   Eine Element-Fläche am neuen Teil auswählen. Ein Objekt im Baum wird hervorgehoben.
        -   Das Objekt per \'drag&drop\' auf das alte Element ziehen und ablegen (entweder in der \'Elements\'-Liste oder in einer der Bedingungen, wo es benutzt wurde). Das Element sollte jetzt gültig werden.
        -   Diesen Ablauf für die übrigen Elemente wiederholen.
        -   Falls ein Element ausversehen einer falschen Fläche zugeordnet wurde, wird die Zuordnung einfach mit der korrekten Fläche wiederholt.
    3.  Ändern des Objektnamens in FreeCAD, falls gewünscht

\'\'Hinweise
\* Es ist nicht so kompliziert, wie es hier auf den ersten Blick aussieht. Nach 2-3 Durchläufen sollten die Abläufe in Fleisch und Blut übergehen und die Ausführung leicht von der Hand gehen.

-   Es ist nicht nur viel schneller als das Löschen und erneute Anlegen von Einschränkungen, sondern auch sicherer, da ein Element in einem übergeordneten Zusammenbau eingesetzt sein könnte. Das Original zu löschen, würde den Verweis zerstören, es neu zuzuordnen würde ihn erhalten.
-   Ferner beschleunigt und vereinfacht es diesen Ablauf, wenn Einschränkungen und Elemente benannt werden. Es gäbe kein Raten, wo die Flächen hingezogen und abgelegt werden sollten, da es aus den Namen hervorgeht (siehe auch [Tipps & Tricks](#Tipps_.26_Tricks.md)).

[Zum Anfang](#top.md)



### Tipps & Tricks 

-   Hierarchisch aufgebaute Zusammenbauten helfen dabei, Probleme des Gleichnungslösers zu vermeiden und das Modell schlank zu halten. Man kann eine Unterbaugruppe mit einem Klick einfrieren und so ohne Aufwand CPU-Resourcen einsparen (Im Kontextmenü des Baumes). Wenn ein Zusammenbau geladen wird, muss Assembly3 die externen Dateien der eingefrorenen Unterbaugruppen nicht öffnen, wodurch der Baum kompakt gehalten wird.
-   Es ist sehr hilfreich, sich anzugewöhnen, Einschränkungen und Elemente zu benennen. Im Baum lässt es sich schnell durch Benutzung der **F2**-Taste erledigen. Sehr nützlich ist auch das Werkzeug zum Sortieren des Baumes, das man in der Hauptwerkzeugleiste findet. Ein Zusammenbau mit vollständig benannten Einschränkungen und Elementen ist für andere Leute sehr einfach zu verstehen, oder auch für einen selbst, wenn man sich ältere Modelle ansieht.

    :   Beispiele für Namen von Einschränkungen für einen Tisch könnten lauten: \"Ausrichtung_Beine_vorne\", \"Ausrichtung_RahmenUnterseite-BeinOberseite\" und Elementnamen könnten sein: \"Bein1_Oberseite\", \"Tischplatte_Vorderseite\" oder \"Tischplatte_linke_Seite\".
-   Bitte beachten, dass, sobald externe Dateien durch einen Zusamenbau geöffnet werden, es nicht mehr möglich ist, diese auf einfache Weise zu schließen, ohne auch den Zusammenbau zu schließen. Da der Zusammenbau die Dateien im Hintergrund offen hält, kann der Reiter verschwinden, aber die Dateien bleiben im Baum sichtbar. Wenn man Zusammenbauten über mehrere Ebenen hat, kann es fast unmöglich sein einzelne Dateien zu schließen. Dieses Verhalten kann sich in Zukunft ändern, aber bis dahin bleibt die Möglichkeit, Die Befehle *File/Save All* und *File/Close All* zu nutzen, um den Baum aufzuräumen, bevor an einer anderen Unterbaugruppe gearbeitet wird.

    :   \'\'Beispiel: Man hat eine große CNC-Maschine mit einem Hauptzusammenbau und Unterbaugruppen für alle Module. Sobald man den Hauptzusammenbau geladen hat, wird er hunderte Dateien bis hin zur kleinsten Schraube öffnen. Bevor man nun die Baugruppe des Elektronikfachs der Maschine bearbeitet, ist es eine gute Idee, alle Dateien zu speichern und zu schließen, um einen leeren Baum zu erhalten. Dann wird nur die Unterbaugruppe des Elektronikfachs geöffnet. Sie öffnet alle benötigten Dateien, aber auch nur diese.
-   Externe Dateien zu benutzen, macht es einfacher, Teile wiederzuverwenden oder Bauteilversonierung mit Systemen wie git oder subversion zu ermöglichen. Der Arbeitsablauf in FreeCAD mit Assembly3 fühlt sich fast genauso an, wie der mit Dateien, in denen alle zusammengehörigen Teile in jeweils einer Datei enthalten sind. Letzteres bietet sich an, wenn man häufig Baugruppen mit anderen Beteiligten austauscht.
-   Mehrfach verknüpfte Dateien. Wenn man eine Dateiverknüpfung zu einem Zusammenbau hinzufügt, wird eine Eigenschaft \"Element Count\" angelegt mit Standardwert 0. Wenn man diesen auf 3 setzt, erhält man 3 Instanzen dieses Teils. Sie werden in einem Unterordner hinzugefügt und können wie vollständig unabhängige Teile verwendet werden. Diese Einstellung kann genutzt werden, um den Speicherplatzverbrauch der Datei klein zu halten, da das Teil nur einmal gespeichert wird. Die Instanzen enthalten nur die Unterschiede.
-   Einsetzen mehrfacher Teile, wie z.B. Schrauben, mit einem Klick. Siehe [Assembly3 Wiki](https://github.com/realthunder/FreeCAD_assembly3/wiki/Constraints-and-Solvers) auf der Github-Seite. Dies ist nicht nur eine erstaunliche Funktion (vielleicht ein bisschen magisch), sondern auch sehr sehr nützlich.

-   Die Benutzung des Arbeitsbereichs [TabBar](https://github.com/triplus/TabBar) beschleunigt die Arbeit mit Zusammenbauten. Es wird eine Werkzeugleiste mit je einem Knopf für jeden Arbeitsbereich hinzugefügt. Man kann die Reihenfolge ändern und man kann die Werkzeugleiste nach belieben platzieren. Viele Leute legen sie vertikal an den linken Rand direkt neben der Baumansicht. Wenn man Assembly3, Part, PartDesign und andere oft genutzte Arbeitsbereiche am oberen Ende platziert, macht es das Umschalten zwischen den Arbeitsbereichen extrem einfach.

[Zum Anfang](#top.md)



## Verweise

-   Das [App-Link](App_Link.md)-Objekt ermöglicht, dass Assembly3 funktioniert.
-   [FreeCAD_assembly3](https://github.com/realthunder/FreeCAD_assembly3) Repository und Dokumentation.
-   [Assembly3 preview](https://forum.freecadweb.org/viewtopic.php?f=20&t=25712), große Diskussionsrunde.
-   [Tutorial for Assembly 3 Workbench](http://help-freecad-jpg87.fr/02_ass_ind.php) von jpg87.
-   Anleitungen zum [kinematischen Zusammenbau](Tutorial_KinematicAssembly/de.md), [Kinematik-Skelett](Tutorial_KinematicSkeleton/de.md) und passender [Kinematiksteuerung](Tutorial_KinematicController/de.md).
-   [Current Assembly Status](https://forum.freecadweb.org/viewtopic.php?f=20&t=34583)
-   [Externe Arbeitsbereiche](External_workbenches.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > Assembly3 Workbench/de
