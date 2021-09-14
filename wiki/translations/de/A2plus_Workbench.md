# A2plus Workbench/de

 <img alt="A2plus Arbeitsbereichssymbol" src=images/A2p_workbench.svg  style="width:128px;">

## Einführung


{{TOCright}}

Der A2plus Arbeitsbereich ist ein [externer Arbeitsbereich](External_workbenches/de.md), zum [Zusammenbau](Assembly/de.md) verschiedener Teile in FreeCAD.

Diese Dokumentation beschreibt die A2plus Version **0.4.47 oder neuer**.

## Einrichtung

Der A2plus Arbeitsbereich ist eine Erweiterung zu FreeCAD. Er kann einfach mit Hilfe des FreeCAD <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Erweiterungsverwalters](Std_AddonMgr/de.md) aus dem **Werkzeuge → Erweiterungsverwalter** Menü installiert werden. A2plus wird aktiv weiterentwickelt und erhält häufig neue Funktionen. Deshalb solltest Du ihn regelmäßig aktualisieren, ebenfalls mittels des Menüs **Werkzeuge → [Erweiterungsverwalter](Std_AddonMgr/de.md)**. Der A2plus Code wird bereitgestellt und weiterentwickelt [auf GitHub](https://github.com/kbwbe/A2plus) und kann auch manuell durch kopieren in das FreeCAD {{FileName|Mod}} Verzeichnis installiert werden.

## Einstieg

Wechsle zuerst in die A2plus Werkzeugleiste in FreeCAD. Um eine Baugruppe zu erstellen, erzeuge eine neue Datei in FreeCAD an. Diese Datei muss zuerst gespeichert werden. Es wird empfohlen (aber nicht notwendig), sie im gleichen Ordner zu speichern wie die Teile, die du zusammenbauen willst.

Jetzt können Teile durch Verwendung der Werkzeugleisten Schaltfläche <img alt="" src=images/A2p_ImportPart.svg  style="width:24px;"> oder <img alt="" src=images/A2p_ShapeReference.svg  style="width:24px;"> zur Baugruppe hinzugefügt werden. Die Schaltfläche <img alt="" src=images/A2p_ImportPart.svg  style="width:24px;"> fügt alle Körper in der ausgewählten Datei als ein einzelnes Teil ein. Wenn Du die Schaltfläche <img alt="" src=images/A2p_ShapeReference.svg  style="width:24px;"> benutzt, kannst Du wählen, welches Teil aus einer Datei zum Teil importiert werden soll. Auf diese Weise kann man z.B. nur eine Skizze importieren, um weitere Teile zu montieren, indem man die Skizze zur Bestimmung der Teilepositionen verwendet.

Das zuerst hinzugefügte Teil bekommt standardmäßig eine fixe Position. (Du kannst dies später über die Teil Eigenschaft **fixed Position** ändern.)

Teile, die sich bereits in der Baugruppe befinden, können mit der Schaltfläche <img alt="" src=images/A2p_DuplicatePart.svg  style="width:24px;"> in der Werkzeugleiste geklont werden.

Um ein Teil aus der Baugruppe zu bearbeiten, wähle es im Modellbaum aus und verwende die Werkzeugleistenschaltfläche <img alt="" src=images/A2p_EditPart.svg  style="width:24px;">. Dies öffnet das Bauteil in einem neuen Reiter in FreeCAD oder wechselt zu seinem Reiter, wenn die Datei bereits geöffnet ist.

Zum Aktualisieren veränderter Teile klicke auf die Schaltfläche <img alt="" src=images/A2p_ImportPart_Update.svg  style="width:24px;">. Die Schaltfläche <img alt="" src=images/A2p_RecursiveUpdate.svg  style="width:24px;"> importiert Teile ebenfalls, jedoch rekursiv über mögliche [Subassemblies](#Subassemblies.md). Wenn Du eines oder mehrere Teile in FreeCAD\'s Modellbaum auswählst, dann wird A2plus nachfragen, nur die ausgewählten Teile zu aktualisieren.

Importierte Teile behalten ihre externen Abhängigkeiten und können bearbeitet werden. Für genau definierte Teile wie Schrauben ist es hingegen nützlich, dass ihre Form nicht verändert werden kann. Dies kann erreicht werden mit der Schaltfläche <img alt="" src=images/A2p_ConvertPart.svg  style="width:24px;">, welche das ausgewählte Teil in eine statische Kopie des Originals konvertiert.

Um das Assembly zu speichern und danach zu schließen kann die Schaltfläche <img alt="" src=images/A2p_Save_and_exit.svg  style="width:24px;"> verwendet werden.

## Der Zusammenbau 

Der Zusammenbau von Teilen erfolgt durch Hinzufügen von Beschränkungen zwischen den Teilen. Nach einer Beschränkung wird A2plus die Teile nach Möglichkeit entsprechend der Beschränkung verschieben.

Um eine Beschränkung zwischen Teilen zu erstellen, halte die **Strg** Taste gedrückt und wähle jeweils eine Kante oder Fläche von zwei Teilen aus. Klicke dann auf die Werkzeugleisten Schaltfläche der gewünschten Beschränkung. Ein Dialogfeld wird aufgeklappt, das in Abschnitt [Beschränkungen](#Beschränkungen.md) beschrieben wird. Die Beschränkung wird in den Modellbaum eingefügt, der an die betroffenen Teile angehängt ist.

Bei komplexen Beschränkungen zwischen Teilen kann A2plus die Beschränkungen möglicherweise nicht lösen. Schau dir daher auch Abschnitt [Fehlerbehebung](#Troubleshooting.md) für Strategien zur Lösung solcher Fälle an.

### Den Überblick behalten 

Je mehr Teile du hinzufügst, desto wichtiger ist es, den Überblick zu behalten. A2plus bietet daher diese Werkzeuge zum Verschieben und Anzeigen von Teilen:

-   Um ein Teil in der Baugruppe zu verschieben, wähle es im Modellbaum aus und verwende die Werkzeugleistenschaltfläche <img alt="" src=images/A2p_MovePart.svg  style="width:24px;">. Wenn du das Teil dort platziert hast, wo es dir gefällt, links-klicke mit der Maustaste. Wenn das verschobene Teil bereits Beschränkungen aufweist, wird es durch Drücken der Werkzeugleistenschaltfläche <img alt="" src=images/A2p_solver.svg  style="width:24px;"> entsprechend platziert, da dies die Auflösung aller Beschränkungen der Baugruppe auslöst.
-   Um eine Beschränkung anzuzeigen, wähle sie im Modellbaum aus und verwende die Werkzeugleistenschaltfläche <img alt="" src=images/A2p_ViewConnection.svg  style="width:24px;">. Dadurch wird die gesamte Baugruppe transparent und die beiden Objekte, die über die Beschränkung verbunden sind, werden hervorgehoben. Um zur Normalansicht zurückzukehren, links-klicke in die Baugruppe.
-   Um nur bestimmte Teile in der Baugruppe anzuzeigen, wähle diese Teile im Modellbaum aus und verwende die Werkzeugleistenschaltfläche <img alt="" src=images/A2p_Isolate_Element.svg  style="width:24px;">. Alternativ kannst du ein bestimmtes Teil ausblenden, indem du es im Modellbaum markierst und **Space** drückst, um seine Sichtbarkeit umzuschalten.
-   Um die Transparenzansicht der gesamten Baugruppe umzuschalten, kannst du die Werkzeugleistenschaltfläche <img alt="" src=images/A2p_ToggleTransparency.svg  style="width:24px;"> verwenden.
-   Jedes Teil kann mit der normalen FreeCAD Bearbeitung transparent gemacht werden. Manchmal geht jedoch die Transparenzeinstellung für Teile beim erneuten Öffnen der Baugruppe aufgrund eines Fehlers in FreeCAD verloren. Als Ausweichlösung kannst du den Werkzeugleistenknopf <img alt="" src=images/A2p_Restore_Transparency.svg  style="width:24px;"> verwenden, um die Transparenzeinstellungen wiederherzustellen.

### Beschränkungen

Bei der Erstellung einer Beschränkung wird ein solches Dialogfeld angezeigt, nachdem du eine Schaltfläche in der Beschränkungswerkzeugleiste gedrückt hast:

![](images/A2p_ConstraintPropertiesDialog.png ) *Oben: Der A2plus Beschränkungseigenschaftsdialog*

Bei bestimmten Beschränkungen erlaubt es dir, die Richtung der Beschränkung zu ändern. Mit der Schaltfläche **<img src="images/A2p_solver.svg" width=24px> Solve** kannst du vorab prüfen, ob diese neue Randbedingung von A2plus gelöst werden kann. Falls nicht, wirf einen Blick auf Abschnitt [Fehlerbehebung](#Troubleshooting/de.md).

Beschränkungen können durch Ändern der [Sichtbarkeit](Std_ToggleVisibility/de.md) deaktiviert werden. Wähle dazu die Beschränkung in der Baumansicht aus und drücke **Space**. Dadurch wird die Eigenschaft **Suppressed** umgeschaltet. Eine unterdrückte Beschränkung wird bei der Lösung der Baugruppe nicht berücksichtigt.

A2plus bietet die folgenden Beschränkungen:

#### Punkt auf Punkt 

Wähle entweder einen [Knoten](Glossary/de#Vertex.md) (Punkt), Kreis oder Kugel auf jedem Teil. Wenn ein Kreis oder eine Kugel ausgewählt wurde, wird dessen Mittelpunkt für die Beschränkung verwendet. Die Werkzeugleistenschaltfläche <img alt="" src=images/A2p_PointIdentity.svg  style="width:24px;"> fügt die Beschränkung {{Variable|pointIdentity}} hinzu, die die Knoten deckungsgleich werden lässt.

#### Punkt auf Linie 

Wähle einen [Knoten](Glossary/de#Vertex.md) (Punkt), oder kreisförmig [Kante](Glossary/de#Edge.md) (wählt seinen Mittelpunkt aus), oder eine sphärische [Fläche](Glossary/de#Face.md) (wählt auch seinen Mittelpunkt) auf der einen Seite und ein [Kante](Glossary/de#Edge.md) auf dem anderen Teil. Die Werkzeugleistenschaltfläche <img alt="" src=images/A2p_PointOnLineConstraint.svg  style="width:24px;"> fügt die Beschränkung {{Variable|pointOnLine}} hinzu. Dadurch wird der Knoten auf die Kante gesetzt.

#### Punkt auf Ebene 

Wähle einen [Knoten](Glossary/de#Vertex.md) (Punkt), oder kreisförmige [Kante](Glossary/de#Edge.md) (wählt seinen Mittelpunkt aus), oder eine sphärische [Fläche](Glossary/de#Face.md) (wählt auch seinen Mittelpunkt) auf einem Teil und eine Ebene auf dem anderen Teil. Die Werkzeugleistenschaltfläche <img alt="" src=images/A2p_PointOnPlaneConstraint.svg  style="width:24px;"> fügt die Beschränkung {{Variable|pointOnPlane}} hinzu. Im Dialogfeld Beschränkung kannst du einen Versatz zwischen dem Punkt und der Ebene angeben. Dieser Versatz kann auch zwischen beiden Seiten der Ebene umgedreht werden. Wenn der Versatz gleich Null ist, setzt die Beschränkung den Knoten auf die Ebene.

#### Kugel auf Kugel 

Wähle entweder eine kugelförmige [Fläche](Glossary/de#Face.md) oder einen [Knoten](Glossary/de#Vertex.md) (Punkt) auf beiden Teilen. Die Werkzeugleistenschaltfläche <img alt="" src=images/A2p_SphericalSurfaceConstraint.svg  style="width:24px;"> fügt die Beschränkung {{Variable|KugelMitteIdent}} hinzu. Sie bewirkt, dass entweder das Zentrum der Kugeln, das Zentrum der Kugel und der Knoten oder die Knoten deckungsgleich werden.

#### Kreiskante auf Kreiskante 

Wähle eine kreisförmige [Kante](Glossary/de#Edge.md) bei beiden Teilen aus. Die Schaltfläche <img alt="" src=images/A2p_CircularEdgeConstraint.svg  style="width:24px;"> fügt die Beschränkung {{Variable|circularEdge}} hinzu. Der Beschränkungs-Dialog erlaubt Dir einen Versatz zwischen beiden Kanten anzugeben. Der Versatz kann auch umgedreht werden. Du kannst außerdem die Richtung der Beschränkung bestimmen und die Verdrehung der Teile sperren. Wenn der Versatz gleich Null ist, wird die Beschränkung die Kanten konzentrisch in derselben Ebene anordnen.

#### Achsdeckungsgleich

Wähle entweder eine zylindrische [Fläche](Glossar/de#Face.md) oder eine lineare [Kante](Glossar/de#Edge.md) auf beiden Teilen. Die Werkzeugleistenschaltfläche <img alt="" src=images/A2p_AxialConstraint.svg  style="width:24px;"> fügt die Beschränkung {{Variable|AchseDeckungsgleich}} hinzu. Der Dialog Beschränkung erlaubt dir die Achsenrichtung anzugeben. Der Dialog ermöglicht es dir außerdem, die Drehung der Teile zu sperren. Durch die Beschränkung werden die Achsen oder Linien deckungsgleich.

#### Achsparallel

Wähle bei beiden Teilen jeweils entweder eine zylindrische [Fläche](Glossary/de#Face.md) oder eine lineare [Kante](Glossary/de#Edge.md) aus. Die Schaltfläche <img alt="" src=images/A2p_AxisParallelConstraint.svg  style="width:24px;"> fügt die Beschränkung {{Variable|Achsparallel}} hinzu. Der Dialog dieser Beschränkung erlaubt Dir die Achsrichtung anzugeben. Die Beschränkung setzt die Achsen oder Linien zueinander parallel.

#### Achse auf Ebene parallel 

Wähle entweder ein zylindrisches [Fläche](Glossar/de#Face.md) oder eine lineare [Kante](Glossar/de#edge.md) auf einem Teil und eine Ebene auf dem anderen Teil. Die Werkzeugleistenschaltfläche <img alt="" src=images/A2p_AxisPlaneParallelConstraint.svg  style="width:24px;"> fügt die Beschränkung {{Variable/de|AchseEbeneParallel}} hinzu. Die Beschränkung macht die Achse oder Linie parallel zur Ebene.

#### Achse normal auf Ebene 

Wähle entweder ein zylindrisches [Fläche](Glossar/de#Face.md) oder eine lineare [Kante](Glossar/de#edge.md) auf einem Teil und eine Ebene auf dem anderen Teil. Die Werkzeugleistenschaltfläche <img alt="" src=images/A2p_AxisPlaneNormalConstraint.svg  style="width:24px;"> fügt die Beschränkung {{Variable/de|AchseEbeneNormal}} hinzu. Durch die Beschränkung wird die Achse oder Linie normal zur Ebene gemacht.

#### Achse im Winkel zu Ebene 

Wähle entweder eine zylindrische [Fläche](Glossar/de#Face.md) oder eine lineare [Kante](Glossar/de#edge.md) auf einem Teil und eine Ebene auf dem anderen Teil.Mit der Werkzeugleistenschaltfläche <img alt="" src=images/A2p_AxisPlaneAngleConstraint.svg  style="width:24px;"> wird die Beschränkung {{Variable/de|AchseEbeneWinkel}} hinzugefügt. Die Beschränkung macht die Achse zunächst parallel zur Ebene. Dann kannst du den Winkel für die Achse im erscheinenden Dialogfeld für die Beschränkungseinstellungen anpassen.

#### Ebene parallel 

Wähle eine Ebene auf beiden Teilen aus. Die Werkzeugleistenschaltfläche <img alt="" src=images/A2p_PlanesParallelConstraint.svg  style="width:24px;"> fügt die Beschränkung {{Variable/de|EbenenParallel}} hinzu. Im Dialogfeld Beschränkung kannst du die Richtung der Beschränkung angeben. Durch die Beschränkung werden die Ebenen parallel gemacht.

#### Ebene auf Ebene 

Wähle eine Ebene auf beiden Teilen aus. Die Werkzeugleistenschaltfläche <img alt="" src=images/A2p_PlaneCoincidentConstraint.svg  style="width:24px;"> fügt die Beschränkung {{Variable/de|EbeneDeckungsgleich}} hinzu. Im Dialogfeld Beschränkung kannst du eine Beschränkungsrichtung und einen Versatz zwischen den Ebenen angeben. Dieser Versatz kann auch umgedreht werden. Wenn der Versatz gleich Null ist, bewirkt die Beschränkung, dass die Ebenen zusammenfallen.

#### Ebene Winklig 

Wähle eine Ebene auf beiden Teilen aus. Die Werkzeugleistenschaltfläche <img alt="" src=images/A2p_AngleConstraint.svg  style="width:24px;"> fügt die Beschränkung {{Variable/de|winkligeEbenen}} hinzu. Im Dialogfeld Beschränkung kannst du einen Winkel zwischen den Ebenen angeben. Durch die Beschränkung werden die Ebenen zunächst parallel, und der angegebene Winkel wird festgelegt.

#### Deckungsgleichheit im Massenschwerpunkt 

Wähle entweder eine geschlossene [Kante](Glossar/de#Edge.md) oder eine Ebene auf beiden Teilen. Die Werkzeugleistenschaltfläche <img alt="" src=images/A2p_CenterOfMassConstraint.svg  style="width:24px;"> fügt die Beschränkung {{Variable/de|Massenschwerpunkt}} hinzu. Im Dialogfeld Beschränkung kannst du einen Versatz zwischen den Kanten oder Ebenen angeben. Dieser Versatz kann auch umgedreht werden. Außerdem kannst du die Beschränkungsrichtung festlegen und die Drehung der Teile sperren. Wenn der Versatz gleich Null ist, setzt die Beschränkung die Kanten oder Ebenen auf dieselbe Ebene.

### Unterbaugruppen

Eine Baugruppe kann andere Baugruppen enthalten. Sie werden wie Teile hinzugefügt, durch drücken der Werkzeugleistenschaltfläche <img alt="" src=images/A2p_ImportPart.svg  style="width:24px;"> und Wahl einer {{FileName|*.FCStd}} Datei, die eine Baugruppe enthält. Solche Unterbaugruppen können auch wie Teile bearbeitet werden, indem die Werkzeugleisteschaltfläche <img alt="" src=images/A2p_EditPart.svg  style="width:24px;"> verwendet wird. Bitte stelle bei höheren Baugruppenstufen sicher, dass du die Baugruppe rekursiv über die Werkzeugleistenschaltfläche <img alt="" src=images/A2p_RecursiveUpdate.svg  style="width:24px;"> aktualisierst, wenn es Änderungen gab.

## Handhabung von Beschränkungen 

Mögliche Beschränkungen für eine Auswahl werden in der Werkzeugleiste und im Dialogfeld *Beschränkungswerkzeuge* angezeigt, durch aktivieren der entsprechenden Schaltflächen. Der *Beschränkungswerkzeuge* Dialog wird über die Werkzeugleistenschaltfläche <img alt="" src=images/A2p_DefineConstraints.svg  style="width:24px;"> geöffnet. Es ist beabsichtigt, offen zu bleiben, um der Baugruppe schnell mehrere Beschränkungen hinzufügen zu können.

Vorhandene Beschränkungen können bearbeitet werden, indem sie im Modellbaum ausgewählt und dann entweder doppelt angeklickt oder mit der Werkzeugleistenschaltfläche <img alt="" src=images/A2p_EditConstraint.svg  style="width:24px;"> bearbeitet werden. Dadurch wird das Dialogfeld *Beschränkungseigenschaften* geöffnet.

Beschränkungen können vorübergehend unterdrückt werden, indem man sie im Modellbaum auswählt und die Baumelementeigenschaft {{PropertyData/de|Unterdrückt}} ändert.

Beschränkungen können entweder durch Auswahl im Modellbaum und Drücken von **Entf** oder durch Auswahl eines Teils mit Beschränkungen im Modellbaum und Verwendung der Werkzeugleistenschaltfläche <img alt="" src=images/A2p_DeleteConnections.svg  style="width:24px;"> gelöscht werden.

Alle Beschränkungen können jederzeit mit der Werkzeugleistenschaltfläche <img alt="" src=images/A2p_solver.svg  style="width:24px;"> aufgelöst werden. Wenn die Werkzeugleistenschaltfläche <img alt="" src=images/A2p_ToggleAutoSolve.svg  style="width:24px;"> aktiviert ist, wird nach jeder Bearbeitung einer Beschränkung automatisch eine Auflösung durchgeführt.

Die Werkzeugleistenschaltfläche <img alt="" src=images/A2p_FlipConstraint.svg  style="width:24px;"> wirkt sich auf die zuletzt hinzugefügte Beschränkung aus. Sie kehrt die Richtung der Beschränkung um.

## Stücklisten

Um Stücklisten von Baugruppen zu erstellen, müssen die verschiedenen Teile der Baugruppe Teilinformationen erhalten, die von A2plus gelesen werden können. Dies geschieht durch Bearbeiten des Teils mit Hilfe der Werkzeugleistenschaltfläche <img alt="" src=images/A2p_EditPart.svg  style="width:24px;">. Drücke im geöffneten Teil die Werkzeugleistenschaltfläche <img alt="" src=images/A2p_PartsInfo.svg  style="width:24px;"> und ein [Tabellenblatt](Spreadsheet_Workbench.md) mit dem Namen *\#PARTINFO\#* wird erstellt.

Die Struktur des Tabellenblatts ist wie folgt:

![](images/A2p_PartinfoTable.png )

Fülle die grauen Felder mit den Informationen aus, die du hast und in der endgültigen Stückliste haben möchtest.

Verwende in der Baugruppe oder Unterbaugruppe die Werkzeugleistenschaltfläche <img alt="" src=images/A2p_PartsList.svg  style="width:24px;">. Du wirst gefragt, ob du rekursiv über alle Unterbaugruppen iterieren möchtest. Klicke auf *Ja*. Dadurch wird ein neues Arbeitsblatt mit dem Namen *\#PARTSLIST\#* erstellt. Sie enthält die Informationen aus den verschiedenen *\#PARTSINFO\#*-Tabellenblättern der Teile in einer Liste wie dieser:

![](images/A2p_PartslistTable.png )

The position (POS) is automatically set according to the appearance of the parts in the model tree. The top level part will get POS 1.

The quantity (QTY) is automatically calculated from the assembly. If a parts is twice in the assembly it will get QTY 2.

If you have updated a part info you can refresh the parts list by pressing the toolbar button <img alt="" src=images/A2p_PartsList.svg  style="width:24px;"> again.

For subassemblies you can also create an info spreadsheet using the toolbar button <img alt="" src=images/A2p_PartsInfo.svg  style="width:24px;">. When you create or update the parts list of the main assembly this info will be used if you click on *No* for the question if you want to iterate recursively over all subassemblies. Then the different parts are not in the parts list but only the subassemblies.

## Sonderfunktionen

### Zusammenbaustruktur

The toolbar button <img alt="" src=images/A2p_Treeview.svg  style="width:24px;"> creates an HTML file with the structure of your assembly. The file will by default be created in the folder of your assembly file. The structure looks like this:

:   ![](images/A2p_Dependency-Tree.jpg )

### Freiheitsgrade

The button <img alt="" src=images/A2p_DOFs.svg  style="width:24px;"> labels every part of the assembly with its degrees of freedom. Furthermore it outputs a list with all parts and their dependencies. The list is output into FreeCAD\'s widget *Report view*. If this widget is currently not visible, it can either be shown by right-clicking into an empty part of the FreeCAD toolbar area and then choosing it in the appearing context menu or with the menu **View → Panels → [Report view](Report_view.md)**.

The degrees of freedom labels can be removed by clicking the button <img alt="" src=images/A2p_DOFs.svg  style="width:24px;"> again.

### Teilkennzeichnungen

The button <img alt="" src=images/A2p_PartLabel.svg  style="width:24px;"> labels every part of the assembly in the 3D view with its name. The part labels can be removed by clicking the button <img alt="" src=images/A2p_PartLabel.svg  style="width:24px;"> again

### Form der gesamten Baugruppe 

Sometimes it is necessary to have the whole assembly combined as one shape. This shape can then for example be used for 3D printing in the [Mesh workbench](Mesh_Workbench.md) or for drawings in the [TechDraw workbench](TechDraw_Workbench.md). It is created using the toolbar button <img alt="" src=images/A2p_SimpleAssemblyShape.svg  style="width:24px;">. The shape is by default not made visible. Use the same toolbar button to update the shape in case of changes in the assembly.

### Absolute Pfade in relative Pfade umwandeln 

With the menu **A2plus → Misc → <img src=images/A2p_SetRelativePathes.svg style="width:24px"> Convert absolute paths of imported parts to relative ones** you can convert absolute paths of imported parts to relative ones.

## Einstellungen

The a2plus preferences can be accessed via FreeCAD\'s menu **Edit → [Preferences](Preferences_Editor.md)** and there in the section *A2plus*. You can set the following options:

### Standardlösungsmethode

Use solving of partial systems : The solver begins with a part that has the property **fixed Position** set to *true* and a part constrained to it. All other parts are not calculated. If a solution could be found, the next constrained part is added to the calculation and so on.
Use \"magnetic\" solver, solving all parts at once : The solver tries to move all parts at once in direction to a part that has the property **fixed Position** set to *true*. Note that this will in most cases take more time for the calculation of a solution.
Force fixed position : This sets the property **fixed Position** to *true* for all parts in the assembly. Then no calculation is actually performed since all parts will always be fixed to the positions where they were created.

### Standardlöserverhalten

Solve automatically if a constraint property is changed : The solver will automatically be started. The same as turning on the toolbar button <img alt="" src=images/A2p_ToggleAutoSolve.svg  style="width:24px;">.

### Verhalten beim Aktualisieren importierter Teile 

Recalculate imported parts before updating them : All parts of the assembly, including subassemblies, will be opened in FreeCAD to be reconstructed using values from spreadsheets.
This feature is designed to construct fully parametrically. **Note:** This feature is very experimental and not recommended for important projects.
Known problems:

-   The assembly can be destroyed because of wrong references to topological names in parts
-   Master spreadsheets can get broken when they are edited while a referenced part file is already closed. This can crash FreeCAD.

Enable recursive update of imported parts : Opens all subassemblies recursively to update them.





Use experimental topological naming : While importing parts to the assembly an algorithm generates topological names for each subelement of the imported shape. The topological names are written into the **mux Info**. When an imported part needs to be updated, these topological names are used to update the subelements of the constraints. So assemblies get more robust against volatile subelement numbers of FreeCAD.
**Note:** This increases file sizes and calculation time during import of parts. If topological naming should be used it has to be activated before the assembly is created.





Inherit per face transparency from parts and subassemblies : Use colour and transparency settings from imported parts.
**Note:** This feature is very experimental and not recommended for important projects.





Do not import invisible shapes : This will hide invisible datum/construction shapes. **Note:** No constraints must be connected to datum/construction shapes in higher or other subassemblies. Otherwise you can break the assembly.





Use solid union for importing parts and subassemblies : All imported parts will directly be put together as union.
This feature is useful for [FEM](FEM_Workbench.md) simulations or [3D-printing](Manual:Preparing_models_for_3D_printing.md) if only one solid is allowed. The alternative is to create a [shape of the whole assembly](#Shape_of_whole_Assembly.md) later on.

### Benutzeroberflächeneinstellungen

Show constraints in toolbar : If this option is not used, the toolbar buttons for the different constraints are not visible to save space in the toolbar. New constraints can still be set using the *Constraint Tools* dialog (toolbar button <img alt="" src=images/A2p_DefineConstraints.svg  style="width:24px;">).
Use native file manager of your OS : If this option is used, you get the file dialog of your OS when selecting files for assemblies.

### Speicherung von Dateien 

Use relative paths for imported parts : Uses relative file paths to the part files.
Use absolute paths for imported parts : Uses absolute file paths to the part files.
All files are in this project folder : All project files have to be in the specified folder. It doesn\'t matter if they are in subfolders of this folder. **Note:** No file is allowed to exist several times in the folder (e.g. in different subfolders).
This option is helpful to work on different machines because then one only has to copy the project folder.

## Problembehebung

Sooner or later you will get the problem that A2plus cannot solve the constraints you set. To overcome this, there are different strategies:

### Verwendung des Konfliktfinderwerkzeugs 

This is the safest method when you have several constraints because this tool attempts to solve one constraint after another until it finds the conflicting constraint. Then you can go on with the other strategies to resolve the identified constraint. The tool is called using the toolbar button <img alt="" src=images/A2p_SearchConstraintConflicts.svg  style="width:24px;">.

### Überprüfung der Beschränkungsrichtung 

Sometimes constraints seem to be consistently defined but they can nevertheless not be solved. An example: Assume you have a {{Variable|[planesParallel](#Plane_Parallel.md)}} constraint set for two planes. Now you want to set for the same planes the {{Variable|[planeCoincident](#Plane_on_Plane.md)}} constraint and A2plus cannot solve this. Then the constraint directions of {{Variable|planesParallel}} and {{Variable|planeCoincident}} are different. Use the same direction for both constraints to fix this.

A2plus offers to automatically check the right direction for **all** constraints of the assembly using the toolbar button <img alt="" src=images/A2p_ReAdjustConstraints.svg  style="width:24px;">.

### Löschen von Beschränkungen 

Most cases of unsolvable constraints occur directly when adding a new constraint. The solution is then to delete the constraint you added last. A2plus will propose this, too.

Sometimes the deletion strategy is the only one, for example when you edited a part in FreeCAD so that faces or edges connected to constraints are missing. You should then delete one constraint that is connected to the changed part at a time. Use the toolbar button <img alt="" src=images/A2p_solver.svg  style="width:24px;"> after every deletion to see if you reached a solvable state.

When you got an assembly that can be solved, add step by step the constraints you need.

### Bewegliche Teile 

In some cases the solver only needs better start values to solve the constraints. Take for example the case that you have an axle part and a wheel part. You add a {{Variable|axisCoincident }} constraint and get no info that the solver failed but the parts are not moved accordingly and in the *Report view* widget of FreeCAD you see \"*REACHED POS-ACCURACY :0.0*\". A solution for this is to move the parts closer to that position you like to get by the constraint.

**Note:** Assure that at least one part of the constraint has the property **fixed Position** set to *false*.

### Festlegen der Eigenschaft Spitze 

If you miss some features of your part after the import to an A2plus assembly, check the property **[Tip](PartDesign_MoveTip.md)**.

A2plus imports bodies of parts with all their features up to the tip feature. This is sensible because setting the tip to a certain feature means that all features behind the tip should not appear in the final part. So if you miss a part feature in A2plus, open the part via the toolbar button <img alt="" src=images/A2p_EditPart.svg  style="width:24px;">, then select a body and look at its property **Tip**. If the tip is not at the feature where you want it, right-click on the feature where the tip should be and choose **<img src=images/PartDesign_MoveTip.svg style="width:24px"> Set tip**. Finally save the part and reload the assembly using the toolbar button <img alt="" src=images/A2p_ImportPart_Update.svg  style="width:24px;">.

### Baugruppenbaum reparieren 

If you cannot see a clear reason why some constraints cannot be resolved, you can try to use the toolbar button <img alt="" src=images/A2p_RepairTree.svg  style="width:24px;">. This will resolve all constraints and re-group then again under the different parts.

### Migration alter A2plus Baugruppen 

Assemblies created with A2plus older than March 2019 do not show the correct icons for imported parts and have obsolete properties. These assemblies can be migrated to A2plus version 0.4.35 and newer using the menu **A2plus → Misc → <img src=images/A2p_Upgrade.svg style="width:24px"> Migrate proxies of imported parts**. After doing this, you must save and reopen your assembly file.

### Vermeidung von Sonderzeichen 

**Diese Strategie ist für Windows nicht erforderlich.**

On some operating systems you can get problems if the file names or the file paths of parts or the assembly contain accented characters. Therefore avoid such characters and also special characters in general.

### Festlegen der Position 

**This strategy is no longer necessary for assemblies created with A2plus 0.3.11 or newer because A2plus issues now a warning for missing fixed positions.**

When you set a constraint between two parts and no part has the property **fixed Position** set to *true* or is connected by a constraint to a part with **fixed Position** set to *true*, the constraint cannot be solved. The same happens if both parts of the constraint have **fixed Position** set to *true*.

Then A2plus outputs the info about the failed solution, but sometimes you only see that the parts are not moved accordingly and in the *Report view* widget of FreeCAD you see \"*REACHED POS-ACCURACY :0.0*\". This means the solver finished without errors but it could actually not solve the constraints.

Therefore check that at least one of your parts in the assembly has **fixed Position** set to *true*. Then assure that you only set constraints to a part which is somehow connected to the fixed part. To visualise these dependencies, see section [Assembly Structure](#Assembly_Structure.md).

### Drehende Teile 

**This strategy is no longer necessary for assemblies created with A2plus 0.4.0 or newer because A2plus rotates the parts now automatically a bit in the background to get a sufficient start angle for the solver.**

The solver often fails for the constraint {{Variable|angledPlanes}} if the two selected planes have currently an angle of 0° or 180°. (The parts are not moved accordingly and in the *Report view* widget of FreeCAD you see \"*REACHED POS-ACCURACY :0.0*\".) A solution for this is to rotate one part by a few degrees using FreeCAD\'s transform feature (right-click on the part in the model tree and select in the context menu **Transform**).

**Note:** Assure that at least one part of the constraint has the property **fixed Position** set to *false*.

## Animation

A2plus offers animations via dragging and via Python scripts.

### Ziehen

Dragging animations are interactive since you trigger it by dragging a part of the assembly. To get these kind of animations:

1.  Fully constrain the part whose movement or rotation should be animated
2.  Click on the toolbar button <img alt="" src=images/A2p_MovePartUnderConstraints.svg  style="width:24px;">. This enables the dragging mode.
3.  Click on the desired part in the assembly.
4.  Now you can move the mouse and the part will follow the movement of the mouse within the defined constraints.
5.  To end the dragging mode, left click in the assembly or press ESC.

Here is an example assembly to try out the dragging animation: [A2p\_example-for-dragging-animation.FCStd](https://forum.freecadweb.org/download/file.php?id=99204)

![](images/A2p_dragging-animation-result.gif )


*Above: The dragging animation using the example assembly*

### Skripten

Despite the dragging mode offers nice interactive animations, they are sometimes not precise enough for screencasts or videos. Scripted animations have the advantage that they animate movements and rotations in a defined way. You can for example rotate a part by exactly 10° back and forth. The following examples use an assembly where a part should be rotated. If you try to animate this using the dragging mode, you will see how hard it is to get a back and forth rotation that you can e.g. show your boss in a presentation. With the interactive example script, however, this is an easy task.

A scripted animation works usually this way:

1.  The assembly is fully constrained
2.  The script changes a parameter, for example the position or rotation angle of a part
3.  After the parameter change, the assembly constraints are solved
4.  Step 2. and 3. are repeated to get the animation

It is also possible to change instead of a placement parameter a constraint, for example the distance between 2 planes.

#### Einfaches Skriptbeispiel 

The simplest way to script an animation is a non-interactive animation that follows a defined movement. Here is an example: First download this assembly file: [A2p\_animated-example.FCStd](https://forum.freecadweb.org/download/file.php?id=97554) and also this Python script: [A2p\_animation-example-script.py](https://forum.freecadweb.org/download/file.php?id=97981).


<div class="mw-collapsible mw-collapsed toccolours">

This is the content of the script and the lines beginning with a \'\#\' describe what the different script lines do:


<div class="mw-collapsible-content">


```python
# import libraries
import time, math, PySide
import A2plus.a2p_solversystem as a2p_solver

# we use steps of 1 degree
step = 1
# wait 1 ms between every step
timeout = 0.001
# initial angle is 0 degree
angle = 0
# we take the currently opened document
document = FreeCAD.activeDocument()
# we want later change the rotation angle of the part "star_wheel_001"
starWheel = document.getObject("star_wheel_001")
# define a progress dialog running from 0 to 360
progressDialog = PySide.QtGui.QProgressDialog(u"Animation progress", u"Stop", 0, 360)

# the while block is the main loop to change the angle and solve
# the assembly constraints subsequently
while angle < 360: # run this loop until we have one full turn (360 degrees)
    # increase the rotation angle
    angle += step
    # set the new angle to the progress dialog
    progressDialog.setValue(angle)
    # change the rotation angle of the part "star_wheel_001"
    starWheel.Placement.Rotation.Angle = math.radians(angle)
    # solve the constraints 
    a2p_solver.solveConstraints(document, useTransaction=True)
    # update the view after the solving ('Gui' stands for 'graphical user interface')
    FreeCADGui.updateGui()
    # bring the progress dialog to front
    PySide.QtGui.QWidget.raise_(progressDialog)
    # if 'Stop' was pressed in the dialog, exit the loop
    if progressDialog.wasCanceled():
        angle = 360
    # wait some time before performing the next step
    time.sleep(timeout)
```


</div>


</div>

To use the script to perform the animation, we must

1.  Open the assembly file in FreeCAD.
2.  Open the script file in FreeCAD.
3.  Click on the toolbar button <img alt="" src=images/Menu_Std_DlgMacroExecute_fr_02.png  style="width:24px;"> to execute the script (also called macro).
4.  Change to the tab of the assembly to see the rotation.

To practice, just change something in the script and execute it afterwards. For example increase *step* to *5*.

This is the result of the example animation:

![](images/A2p_animated-example-result.gif )

#### Interaktives Skriptbeispiel 

The first script example demonstrated how to create an animation without any user feedback. For most applications you need to interact with the animation. For example the interesting issue in the example is to see how the driving pins cross the center groove of the wheel. To have a closer look you might present this detail to your colleagues or boss. Therefore you need an interactive solution.

This can be done by using a custom animation dialog with a slider. By moving the slider you can set the rotation angle and therefore rotate back and forth at interesting position.

We use the same assembly file: [A2p\_animated-example.FCStd](https://forum.freecadweb.org/download/file.php?id=97554) and this Python script: [A2p\_animation-example-script.py](https://forum.freecadweb.org/download/file.php?id=97982).


<div class="mw-collapsible mw-collapsed toccolours">

This is the content of the script to get the interactive animation dialog:


<div class="mw-collapsible-content">


```python
# import libraries
import time, math, PySide, sys
import FreeCAD.A2plus.a2p_solversystem as a2p_solver
from FreeCAD import Units
from PySide import QtCore, QtGui

# wait 1 ms after every calculation
timeout = 0.001
# we take the currently opened document
document = FreeCAD.activeDocument()
# we want later change the rotation angle of the part "star_wheel_001"
starWheel = document.getObject("star_wheel_001")

class AnimationDlg(QtGui.QWidget): # the animation dialog

    def __init__(self): # to initialize the dialog
        super(AnimationDlg, self).__init__()
        self.initUI()

    def initUI(self): # the definition of the dialog components
        self.setMinimumSize(self.minimumSizeHint()) # set the minimal dialog size to minimum
        self.setWindowTitle('Animation Dialog')
        # use a grid layout for the whole form
        self.mainLayout = QtGui.QGridLayout()
        self.lineNo = 0 # first dialog grid line
        # add description label
        DescriptionLabel = QtGui.QLabel(self)
        DescriptionLabel.setText("Change slider to change rotation angle")
        self.mainLayout.addWidget(DescriptionLabel,self.lineNo,0,1,4)
         # next dialog grid line
        self.lineNo += 1
        # add a label; there is no need for the "self." prefix because we don't want to change the label later
        LabelMin = QtGui.QLabel(self)
        LabelMin.setText("Min")
        LabelMin.setFixedHeight(32)
        self.mainLayout.addWidget(LabelMin,self.lineNo,0)
        # add a spin edit to define the slider minimum
        self.MinEdit = QtGui.QSpinBox(self)
        # get the angle unit as string
        self.MinEdit.setSuffix(" " + str(FreeCAD.Units.Quantity(1, FreeCAD.Units.Angle))[2:])
        self.MinEdit.setMaximum(999)
        self.MinEdit.setMinimum(0)
        self.MinEdit.setSingleStep(10)
        self.MinEdit.setValue(0)
        self.MinEdit.setFixedHeight(32)
        self.MinEdit.setToolTip("Minimal angle for the slider")
        QtCore.QObject.connect(self.MinEdit, QtCore.SIGNAL("valueChanged(int)"), self.setMinEdit)
        self.mainLayout.addWidget(self.MinEdit,self.lineNo,1)
        # add the slider
        self.slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        self.slider.setRange(0, 360)
        self.slider.setValue(0)
        self.slider.setFixedHeight(32)
        self.slider.setToolTip("Move the slider to change the rotation angle")
        QtCore.QObject.connect(self.slider, QtCore.SIGNAL("sliderMoved(int)"), self.handleSliderValue)
        self.mainLayout.addWidget(self.slider,self.lineNo,2)
        # add a label
        LabelMax = QtGui.QLabel(self)
        LabelMax.setText("Max")
        LabelMax.setFixedHeight(32)
        self.mainLayout.addWidget(LabelMax,self.lineNo,3)
        # add a spin edit to define the slider maximum
        self.MaxEdit = QtGui.QSpinBox(self)
        # get the angle unit as string
        self.MaxEdit.setSuffix(" " + str(FreeCAD.Units.Quantity(1, FreeCAD.Units.Angle))[2:])
        self.MaxEdit.setMaximum(999)
        self.MaxEdit.setMinimum(1)
        self.MaxEdit.setSingleStep(10)
        self.MaxEdit.setValue(360)
        self.MaxEdit.setFixedHeight(32)
        self.MaxEdit.setToolTip("Maximal angle for the slider")
        QtCore.QObject.connect(self.MaxEdit, QtCore.SIGNAL("valueChanged(int)"), self.setMaxEdit)
        self.mainLayout.addWidget(self.MaxEdit,self.lineNo,4)
         # next dialog grid line
        self.lineNo += 1
        # add a spacer
        self.mainLayout.addItem(QtGui.QSpacerItem(10,10), 0, 0)
        # add a label
        LabelCurrent = QtGui.QLabel(self)
        LabelCurrent.setText("Current angle:")
        LabelCurrent.setFixedHeight(32)
        self.mainLayout.addWidget(LabelCurrent,self.lineNo,1)
        # output the current angle
        self.CurrentAngle = QtGui.QLineEdit(self)
        self.CurrentAngle.setText(str(0))
        self.CurrentAngle.setFixedHeight(32)
        self.CurrentAngle.setToolTip("Current rotation angle")
        self.CurrentAngle.isReadOnly()
        self.mainLayout.addWidget(self.CurrentAngle,self.lineNo,2)
        # add label for the unit
        LabelUnit = QtGui.QLabel(self)
        LabelUnit.setText("deg")
        LabelUnit.setFixedHeight(32)
        self.mainLayout.addWidget(LabelUnit,self.lineNo,3)
        # button to close the dialog
        self.Close = QtGui.QPushButton(self)
        self.Close.setText("Close")
        self.Close.setFixedHeight(32)
        self.Close.setToolTip("Closes the dialog")
        QtCore.QObject.connect(self.Close, QtCore.SIGNAL("clicked()"), self.CloseClicked)
        self.mainLayout.addWidget(self.Close,self.lineNo,4)
        # place the defined grid layout to the dialog
        self.setLayout(self.mainLayout)
        self.update()

    def handleSliderValue(self):
        # set slider value as angle
        starWheel.Placement.Rotation.Angle = math.radians(self.slider.value())
        # output current angle
        self.CurrentAngle.setText(str(self.slider.value()))
        # solve the constraints 
        a2p_solver.solveConstraints(document)
        # update the view after the solving ('Gui' stands for 'graphical user interface')
        FreeCADGui.updateGui()
        # wait some time, important to give time to perform calculations
        time.sleep(timeout)

    def setMinEdit(self):
        # assure that the minimum is samller than the maximum
        if self.MinEdit.value() >=  self.MaxEdit.value():
            self.MaxEdit.setValue(self.MinEdit.value() + 1)
        self.slider.setRange(self.MinEdit.value(), self.MaxEdit.value())

    def setMaxEdit(self):
        # assure that the minimum is samller than the maximum
        if self.MinEdit.value() >=  self.MaxEdit.value():
            self.MinEdit.setValue(self.MaxEdit.value() - 1)
        self.slider.setRange(self.MinEdit.value(), self.MaxEdit.value())

    def CloseClicked(self):
        AnimationDialog.close()

# create and show the defined dialog
AnimationDialog = AnimationDlg()
AnimationDialog.show()

# run this loop when the dialog is visible
while AnimationDialog.isVisible():
    # update the view; important to give the OS feedback the dialog is alive
    FreeCADGui.updateGui()
    # bring the dialog to front, so that the dialog is always visible
    QtGui.QWidget.raise_(AnimationDialog)
    # output slider value here too because during the calculation the slider might have been moved
    AnimationDialog.CurrentAngle.setText(str(AnimationDialog.slider.value()))
```


</div>


</div>

The dialog defined in the script looks like this:

![](images/A2p_AnimationDialog.png )

### Skriptbefehle

To understand the script syntax better, here is some command info: 
```python starWheel.Placement.Rotation.Angle = math.radians(angle)```

Here we change the placement property `Rotation.Angle` of the part get got previously as `starWheel`. This property gets the angle as [radian](https://en.wikipedia.org/wiki/Radian). The function `radians()` from the library `math` converts the angle from degree to radian.

The property `Rotation.Angle` uses the current placement axis of the part (in our example the X-axis). To rotate the part e.g. around the Z-axis one can set the rotation axis (before calling the rotation command) using the command: 
```python starWheel.Placement.Rotation.Axis = FreeCAD.Vector(0,0,1)``` Instead of rotating, parts can also be moved. To change for example the placement in Y-direction of the wheel, the command would be: 
```python starWheel.Placement.Base.y = PositionShift``` In this case we would not define the variable `angle` but `PositionShift` that we change on every loop run.

There are different ways to set the placement of a part. Some are [ documented here](Placement.md). Unfortunately there is no list (yet) with all possible placement commands. 
```pythona2p_solver.solveConstraints(document, useTransaction=False/True)```

This is an A2plus-specific command. It solves the assembly constraints of the assembly we previously got as `document`. The option `useTransaction` specifies if FreeCAD should store every change in the undo/redo stack. For large animations you might therefore set it to `False`.




[Category:Addons](Category:Addons.md) [Category:External Workbenches](Category:External_Workbenches.md)
