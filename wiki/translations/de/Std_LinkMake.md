---
- GuiCommand:
   Name: Std LinkMake
   Name/de: Std VerknüpfungErstellen
   MenuLocation: Keine
   Workbenches: Alle
   Version: 0.19
   SeeAlso: [Standard Teil](Std_Part/de.md), [Std Gruppe](Std_Group/de.md), [PartDesign Körper](PartDesign_Body/de.md)
---

# Std LinkMake/de



## Beschreibung


**[<img src=images/Std_LinkMake.svg style="width:16px"> [Verknüpfung erstellen](Std_LinkMake/de.md)**

erstellt ein [App Link](App_Link.md)-Objekt (`App::Link` class), das auf ein anderes Objekt innerhalb desselben Dokuments oder in einem anderen Dokument verweist oder eine Verknüpfung zu ihm erzeugt. Es ist speziell dafür entwickelt worden einzelne Objekte effizient zu vervielfältigen, was bei der Erstellung komplexer [Baugruppen](assembly/de.md) aus kleineren Unterbaugruppen und vielen Wiederholteilen wie Schrauben, Muttern und ähnlichen Befestigungselementen hilft.

Das [App-Link](App_Link/de.md)-Object wurde mit der Version 0.19 neu eingeführt; in der Vergangenheit wurde das einfache Duplizieren von Objekten durch **[<img src=images/Draft_Clone.svg style="width:16px"> [Draft Klonen](Draft_Clone/de.md)** erreicht, aber das ist eine weniger effiziente Lösung, da sie entsprechend ihrer Implementierung zwingend eine Kopie der internen [Form](Part_TopoShape/de.md) des Quellobjekts erzeugt. Dagegen referenziert ein App-Link direkt auf die originale Form und ist dadurch speichereffizienter.

Das [App-Link](App_Link.md)-Objekt allein kann schon wie ein Array genutzt werden um das Basisobjekt zu vervielfältigen; das kann erreicht werden, durch das Ändern der {{PropertyData/de|Element Count}} auf {{Value|1}} oder größer. Dieses \"[Link-Array](#Link_Array.md)\"-Object kann auch mit den verschiedenen Array-Werkzeugen des <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft-Arbeitsbereichs](Draft_Workbench/de.md) erzeugt werden, z.B. **[<img src=images/Draft_OrthoArray.svg style="width:16px"> [Draft Rechtwinklige Anordnung](Draft_OrthoArray/de.md)**, **[<img src=images/Draft_PolarArray.svg style="width:16px"> [Draft Polare Anordnung](Draft_PolarArray/de.md)**, and **[<img src=images/Draft_CircularArray.svg style="width:16px"> [Draft Kreisanordnung](Draft_CircularArray/de.md)**.

Im <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md) sind Verknüpfungen zur Verwendung mit 
**[<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Körper](PartDesign_Body/de.md)** vorgesehen. Es empfiehlt sich daher **Display Mode Body** auf {{Value|Tip}} zu setzen, um Eigenschaften des gesamten Körpers und nicht einzelner Eigenschaften auszuwählen. Um Muster interner [PartDesign Formelemente](PartDesign_Feature/de.md) zu erstellen, verwendet man **[<img src=images/PartDesign_LinearPattern.svg style="width:16px"> [PartDesign Lineares Muster](PartDesign_LinearPattern/de.md)**, **[<img src=images/PartDesign_PolarPattern.svg style="width:16px"> [PartDesign Polares Muster](PartDesign_PolarPattern/de.md)**, and **[<img src=images/PartDesign_MultiTransform.svg style="width:16px"> [PartDesign MultiTransform](PartDesign_MultiTransform.md)**


**[<img src=images/Std_LinkMake.svg style="width:16px"> [Std LinkMake](Std_LinkMake/de.md)**

ist nicht für einen speziellen Arbeitsbereich vorgesehen, sondern für das grundlegende System. Deshalb kann es aus der **Strukturellen Werkzeugleiste** verwendet werden, die in allen [Arbeitsbereichen](Workbenches/de.md) enthalten ist. Das Verknüpfungsobjekt (link object) zusammen mit **[<img src=images/Std_Part.svg style="width:16px"> [Std Teil](Std_Part/de.md)** zur Gruppierung verschiedener Objekte, stellt die Grundlage der <img alt="" src=images/Assembly3_workbench_icon.svg  style="width:24px;"> [Arbeitsbereich Assembly3](Assembly3_Workbench/de.md) und <img alt="" src=images/Assembly4_workbench_icon.svg  style="width:24px;"> [Arbeitsbereich Assembly4](Assembly4_Workbench/de.md) Arbeitsbereiche dar.



## Anwendung

Mit Auswahl:

1.  Ein Objekt in der [Baumansicht](tree_view/de.md) oder der [3D-Ansicht](3D_view/de.md) auswählen, für das eine Verknüpfung erstellt werden soll.
2.  Die Schaltfläche **[<img src=images/Std_LinkMake.svg style="width:16px"> [Verknüpfung erstellen](Std_LinkMake/de.md)** drücken. Das erzeugte Objekt hat dasselbe Symbol wie das Originalobjekt, ist jedoch mit einem Pfeil überlagert, der darauf hinweist, dass es sich um eine Verknüpfung handelt.

Ohne Auswahl:

1.  Wenn kein Objekt ausgewählt wurde, wird durch das Drücken der Schaltfläche **[<img src=images/Std_LinkMake.svg style="width:16px"> [Verknüpfung erstellen](Std_LinkMake/de.md)** eine leere <img alt="" src=images/Link.svg  style="width:24px;"> Verknüpfung erstellt.
2.  Zum [Eigenschafteneditor](property_editor/de.md) wechseln, dann auf die {{PropertyData/de|Linked Object}} klicken, um den Dialog Link zu öffnen (siehe [Auswahlmethoden](Selection_methods/de.md)) und ein Objekt auszuwählen, anschließend **OK** drücken.
3.  Anstatt ein komplettes Objekt in der [Baumansicht](tree_view/de.md) auszuwählen, kann man auch Unterelemente (Knoten, Kanten oder Flächen) eines einzigen Objekts in der [3D-Ansicht](3D_view/de.md) auswählen. In diesem Falle dupliziert die Verknüpfung nur diese Unterelemente und der überlagerte Pfeil sieht anders aus. Dies kann auch mit **[<img src=images/Std_LinkMakeRelative.svg style="width:16px"> [Unterverknüpfung erstellen](Std_LinkMakeRelative/de.md)** erreicht werden.

![](images/Std_Link_tree_example.png ) ![](images/Std_Link_example.png )



*(1) Ein Objekt, (2) eine leere Verknüpfung, (3) eine vollständige Verknüpfung zum ersten Objekt (mit überlagerndem Material) und (4) eine Verknüpfung nur mit einzelnen Unterelementen des Objektes. Die leere Verknüpfung ist nicht an das reale Objekt gebunden und wird daher nicht in der [3D Ansicht](3D_view/de.md) angezeigt.*



## Verwendung externer Dokumente 

1.  Wir beginnen mit einem Dokument, das mindestens ein Objekt enthält, das die Quelle der Verknüpfung darstellt.
2.  Wir öffnen ein neues oder bereits existierendes Dokument. Zur Vereinfachung nutzen wir die Schaltfläche **[<img src=images/Std_TreeMultiDocument.svg style="width:16px"> [Std BaumMehrfachdokument](Std_TreeMultiDocument/de.md)**, um beide Dokumente in der [Baumansicht](tree_view/de.md) anzuzeigen. Wir [Speichern](Std_Save/de.md) beide Dokumente, bevor wir weitergehen. Das Verknüpfungswerkzeug kann seine Quelle und sein Ziel nicht finden, wenn die Dokumente nicht gespeichert wurden.
3.  Im ersten Dokument wählen wir das Objekt, das wir verknüpfen wollen. Dann wählen wir den Reiter im [Hauptansichtsbereich](main_view_area/de.md), um zum zweiten Dokument zu wechseln.
4.  Nun die Schaltfläche **[<img src=images/Std_LinkMake.svg style="width:16px"> [Std VerknüpfungErstellen](Std_LinkMake/de.md)** anklicken. Das erstellte Ojekt hat dasselbe Icon, wie das Originalobjekt, hat aber einen zusätzlichen, überlagernden Pfeil, der es als Verknüpfung aus einem externen Dokument anzeigt.


**Hinweise:**

-   Wenn das Dokument mit der Verknüpfung gespeichert wird, wird ebenfalls gebeten, das Quelldokument mit dem Originalobjekt zu [Std Speichern](Std_Save/de.md).
-   Um das Originalobjekt in das Dokument mit der Verknüpfung einzufügen, betätigen wir die Schaltfläche **[<img src=images/Std_LinkImport.svg style="width:16px"> [Std VerknüpfungImportieren](Std_LinkImport/de.md)** oder **[<img src=images/Std_LinkImportAll.svg style="width:16px"> [Std AlleVerknüpfungenImportieren](Std_LinkImportAll/de.md)**.
-   Die Schaltfläche **[<img src=images/Std_LinkMake.svg style="width:16px"> [Std VerknüpfungErstellen](Std_LinkMake/de.md)** kann auf eine existierende Verknüpfung angewendet werden, um eine Verknüpfung auf eine Verknüpfung zu erstellen, die sich letztendlich in eine Verknüpfung auf das Originalobjekt im Quelldokument auflöst. Das kann auch mit der Schaltfläche **[<img src=images/Std_LinkMakeRelative.svg style="width:16px"> [Std UnterverknüpfungErstellen](Std_LinkMakeRelative.md)** verwendet werden, um nur einzelne Unterelemente zu verknüpfen.

![](images/Std_Link_tree_documents_example.png ) ![](images/Std_Link_documents_example.png )



*(1, 2) Zwei Objekte eines Quelldokumentes verknüpft mit einem Zieldokument, (3) eine Verknüpfung auf eine zweite Verknüpfung (mit überlagerndem Material) und (4) eine Verknüpfung zu einem Unterelement der zweiten Verknüpfung.*



### Ziehen und Loslassen (dragging and dropping) 

Anstatt zwischen den Dokumentenreitern hin und her zu schalten, können Verknüpfungen auch durch Ziehen und Loslassen in der [Baumansicht](Tree_view/de.md) erstellt werden: das Quellobjekt des ersten Dokumentes wählen, die **Alt**-Taste gedrückt halten, ziehen und auf dem Namen des zweiten Dokumentes loslassen.

Abhängig von der gedrückten Zusatztaste werden unterschiedliche Aktionen beim Ziehen und Loslassen aufgerufen.

-   Ohne die Zusatztaste wird das Objekt von einem Dokument in das andere nur verschoben. Dabei wird ein geneigter Pfeil im Cursor gezeigt.
-   Mit der gedrückten **strg**-Taste wird das Objekt kopiert. Dabei wird ein Pluszeichen im Cursor gezeigt.
-   Mit der gedrückten **Alt**-Taste wird eine Verknüpfung erstellt. Zwei Kettenglieder werden im Cursor angeigt.

Ziehen und Loslassen mit den Zusatztasten **Ctrl** und **Alt** kann auch in einem einzelnen Dokument gearbeitet werden. Ziehen und Loslassen im selben Dokument erstellen damit mehrere Kopien oder mehrere Verknüpfungen.



## Gruppen


**[<img src=images/Std_LinkMake.svg style="width:16px"> [Std VerknüpfungErstellen](Std_LinkMake/de.md)**

kann auf **[<img src=images/Std_Part.svg style="width:16px"> [Standard Teil](Std_Part/de.md)** angewendet werden, um schnell Objektgruppen im Raum zu vervielfältigen, wie z.B. [Zusammenbauten](assembly.md).

![](images/Std_Link_tree_Std_Part_example.png )



*Eine Verknüpfung, die aus einem [Standard Teil](Std_Part/de.md) erstellt wurde. Die Objekte wurden nicht kopiert, sondern sie werden unter der Originalgruppierung und unter der verknüpften Gruppierung angezeigt.*

Ein normale **[<img src=images/Std_Group.svg style="width:16px"> [Std Gruppe](Std_Group/de.md)** besitzt keine **Positionierungs**-Eigenschaft. Daher kann es die Position der Objekte darin nicht steuern. Wenn jedoch **[<img src=images/Std_LinkMake.svg style="width:16px"> [Std VerknüpfungErstellen](Std_LinkMake/de.md)** mit **[<img src=images/Std_Group.svg style="width:16px"> [Std Gruppe](Std_Group/de.md)** verwendet wird, verhält sich die daraus entstandene Verknüpfung wie ein **[<img src=images/Std_Part.svg style="width:16px"> [Standard Teil](Std_Part/de.md)** und kann ebenso im Raum bewegt werden.

![](images/Std_Link_tree_Std_Group_example.png ) ![](images/Std_Link_Std_Group_example.png )



*Eine Verknüpfung, erstellt aus [Std Grupppe](Std_Group/de.md); die Objekte sind nicht vervielfältigt, werden aber sowohl im Ursprungsbehälter als auch im verknüpften Behälter angezeigt. Die Verknüpfung (mit überlagerndem Material) kann im Raum bewegt werden, ebenso wie [Standardd Teil](Std_Part/de.md).*

Eine Verknüpfung auf ein **[<img src=images/Std_Part.svg style="width:16px"> [Standard Teil](Std_Part/de.md)** hält die Sichtbarkeit der Objekte synchron zum Originalteil. Wird also ein Objekt in einer Verknüpfung verborgen, so wird es in allen dazugehörigen Verknüpfungen und dem Originalteil verborgen. Dem gegenüber erlaubt eine Verknüpfung auf eine **[<img src=images/Std_Group.svg style="width:16px"> [Std Gruppe](Std_Group/de.md)** unabhängige Kontrolle auf die Sichtbarkeit.

![](images/Std_Link_tree_Std_Part_visibility.png ) ![](images/Std_Link_tree_Std_Group_visibility.png )



*Links: ein [Standard Teil](Std_Part/de.md) mit zwei Objekten und zwei Verknüpfungen auf das Teil; die Sichtbarkeit der Objekte ist synchron. Rechts: [Std Gruppe](Std_Group/de.md) mit zwei Objekten und zwei Verknüpfungen auf die Gruppe; die Sichtbarkeit der Objekte ist unabhängig in jeder Gruppe einstellbar.*



## Darstellung der Überlagerung 

Wenn eine Verknüpfung erstellt wird, ist die Eigenschaft **Override Material** mit `False` voreingestellt. Daher wird die Verknüpfung genauso aussehen, wie das originale **Linked Object**.

Wenn die Eigenschaft **Override Material** auf `True` gesetzt ist, wird die Eigenschaft **Shape Material** nun das Erscheinungsbild der Verknüpfung steuern.

Unabhängig vom Status der Eigenschaft **Override Material** ist es möglich, das Erscheinungsbild der Unterelemente, wie Punkte, Kanten oder Oberflächen einer Verknüpfung individuell zu bestimmen.

1.  Die Verknüpfung in der [Baumansicht](tree_view/de.md) wählen. Das Kontextmenü mit einem Rechtsklick öffnen und **Override colors** wählen.
2.  Nun die einzelnen Unterelemente in der [3D Ansicht](3D_view/de.md) wählen, die Schaltfläche **Edit** anklicken und die Eigenschaften einschließlich der Transparenz ändern.
3.  Um geänderte Attribute wieder zu entfernen, werden die Elemente in der Liste gewählt und die Schaltfläche **Remove** angeklickt.
4.  Mit dem Betätigen der Schaltfläche **OK** wird der Vorgang abgeschlossen.


**Hinweis:**

da in Version v0.19 die Färbung der Unterelemente Teil des [Topologisches Benennungsproblems](topological_naming_problem/de.md) ist, sollte dies der letzte Schritt der Gestaltung des Models sein, wenn nichts mehr am Modell geändert werden soll.

<img alt="" src=images/Std_Link_override_color_example.png  style="width:500px;">



*(1) das Original, (2) eine Verknüpfung mit überlagerndem Material und (3) eine weitere Verknüpfung mit individuell angepaßten Unterelementen.*



## Muster aus Verknüpfungen 


**Siehe auch:**

[Draft RechtwinkligeAnordnung](Draft_OrthoArray/de.md).

Wenn eine Verknüpfung erstellt wird, ist seine Eigenschaft **Element Count** mit {{Value|0}} voreingestellt. Daher wird nur eine Verknüpfung in der [Baumansicht](tree_view/de.md) angezeigt.

Wenn, wie voreingestellt die Eigenschaft **Show Element** `True` ist und der Wert der Eigenschaft **Element Count** auf {{Value|1}} oder mehr gesetzt ist, werden automatisch mehrere Verknüpfungen unter der ersten erstellt. Jede neue Verknüpfung kann in die gewünschte Position über ihre eigene Eigenschaft **Placement** verschoben werden.

In gleicher Weise kann die Erscheinung jedes Elementes des Musters verändert werden, entweder über die Eigenschaften **Override Material** und **Shape Material** oder über das Menü **Override colors** auf das ganze Muster und anschließender Wahl einzelner Oberflächen. Das ist in [Darstellung der Überlagerung](#Overriding_appearance.md) beschrieben.

<img alt="" src=images/Std_Link_tree_array_example.png ) ![](images/Std_Link_array_example.png  style="width:500px;">



*(1) das Original und (2, 3, 4) ein Muster mit drei Verknüpfungen als deren Elemente, jede in einer anderen Position. Die erste Verknüpfung hat ein überlagerndes Material und transparente Oberflächen. Die beiden anderen haben selbst geänderte Oberflächenfarben.*

Wenn Position und Eigenschaften der Verküpfungen im Muster passen, kann die Eigenschaft **Show Element** auf `False` gesetzt werden, um die einzelnen Verknüpfungen in der [Baumansicht](tree_view/de.md) auszublenden. Dadurch reagiert das System schneller, vor allem, wenn es viele Objekte im Dokument gibt.

Bei diesem Muster mit Verknüpfungen muß jedes Element manuell positioniert werden. Soll aber ein spezielles Muster der Verknüpfungen entstehen, können die Werkzeuge des <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Arbeitsbereiches Draft](Draft_Workbench/de.md), wie **[<img src=images/Draft_OrthoArray.svg style="width:16px"> [Draft RechtwinkligeAnordnung](Draft_OrthoArray/de.md)**, **[<img src=images/Draft_PolarArray.svg style="width:16px"> [Draft PolareAnordnung](Draft_PolarArray/de.md)** und **[<img src=images/Draft_CircularArray.svg style="width:16px"> [Draft KreisAnordnung](Draft_CircularArray/de.md)** verwendet werden. Diese Anweisungen erstellen normale Kopien oder Kopien der Verknüpfungen, abhängig von den eingestellten Optionen während der Erstellung.



## Sichtbarkeit

Wenn die Eigenschaft **Show Element** `True` ist und einzelne Elemente eines [Musters aus Verknüpfungen](#Link_Array.md) in der [Baumansicht](Tree_view/de.md) angezeigt werden, kann jede Verknüpfung durch die **Leertaste** gezeigt oder verborgen werden.

Ein anderer Weg einzelne Elemente zu verbergen ist die Verwendung des **Override colors**-Menüs.

1.  Das Muster wählen und mit einem Rechtsklick das **Override colors**-Menü öffnen.
2.  In der [3D Ansicht](3D_view/de.md) ein Unterelement einer Verknüpfung im Musters anklicken.
3.  Die Schaltfläche **Hide** klicken. Ein Icon eines Auges <img alt="" src=images/Invisible.svg  style="width:24px;"> erscheint und zeigt an, daß dieses Element in der [3D Ansicht](3D_view/de.md) verborgen ist. Das Element wird kurz angezeigt, wenn der Cursor über das Icon <img alt="" src=images/Invisible.svg  style="width:24px;"> gezogen wird.
4.  Mit einem Klick auf die Schaltfläche **OK** wird die Ausführung bestätigt und der Vorgang verlassen. Die Verknüpfung bleibt verborgen, auch wenn sie in der [Baumansicht](tree_view/de.md) als sichtbar angezeigt wird.

![](images/Std_Link_array_visibility_example.png )



*Die Elementenfarbwahl zeigt sich beim Öffnen des Kontextmenüs zu einer Verknüpfung in der Baumansicht.*

Soll die Sichtbarkeit des Elementes in einem Muster wiederhergestellt werden, dann muß das Kontextmenü wieder geöffnet werden und das Augenicon angeklickt werden. Danach auf die Schaltfläche **Remove** klicken, um das Verbergen abzuschalten, und auf die Schaltfläche **OK** klicken, um den Vorgang zu bestätigen und zu abzuschließen. Das Element zeigt sich in der [3D Anischt](3D_view/de.md) wieder.

Weist die Verknüpfung auf ein **[<img src=images/Std_Part.svg style="width:16px"> [Standard Teil](Std_Part/de.md)** oder eine **[<img src=images/Std_Group.svg style="width:16px"> [Std Gruppe](Std_Group/de.md)**, verhält sich das **Override colors**-Menü ähnlich zu den Mustern. Es ermöglicht die Einstellung einer Oberflächenfarbe, der Farbe des ganzen Objektes und die Sichtbarkeit des Objektes in der Gruppe.

![](images/Std_Link_Std_Part_visibility_example.png ) ![](images/Std_Link_Std_Part_visibility_example_3D.png )



*Ein [Standard Teil](Std_Part/de.md) enthält drei Objekte und eine Verknüpfung zu diesem Teil. In der Verknüpfung (1) ist das erste Objekt unsichtbar. (2) das zweite Objekt hat einige Unterelemente mit unterschiedlichen Farben. (3) das ganze dritte Objekt hat unterschiedliche Farben und einen gewissen Grad an Transparenz.*



## Eigenschaften

Eine [Anwendung Verknüpfung](App_Link/de.md) (`App::Link` Klasse) ist aus der zugrunde liegenden [App DocumentObject](App_DocumentObject/de.md) (`App::DocumentObject` Klasse) abgeleitet. Deshalb hat es die grundlegenden Eigenschaften, wie **Label** und **Label2**.

Das Folgende sind die speziellen Eigenschaften, die im [Eigenschafteneditor](Property_editor/de.md) eingestellt werden können. Verborgene Eigenschaften können mit der Anweisung **Show all** aus dem Kontextmenü im [Eigenschafteneditor](Property_editor/de.md) eingestellt werden.



### Daten


{{TitleProperty| Link}}

-    **Linked Object|XLink**: it indicates the source object of the [App Link](App_Link.md); this can be an entire object, or a subelement of it (vertex, edge, or face).

-    **Link Transform|Bool**: it defaults to `False`, in which case the Link will override the **Linked Object**\'s own placement. If it is set to `True`, the Link will be placed in the same position as the **Linked Object**, and its placement will be relative to the **Linked Object**\'s placement. This can also be achieved with **[<img src=images/Std_LinkMakeRelative.svg style="width:16px"> [Std LinkMakeRelative](Std_LinkMakeRelative.md)**.

-    **Placement|Placement**: the placement of the Link in absolute coordinates.

-    **Link Placement|Placement|Hidden**: it is an offset applied on top of the **Placement** of the **Linked Object**. This property is normally hidden but appears if **Link Transform** is set to `True`; in this case, **Placement** now becomes hidden.

-    **Show Element|Bool**: it defaults to `True`, in which case the [tree view](tree_view.md) will show the individual Link copies, as long as **Element Count** is {{Value|1}} or larger.

-    **Element Count|IntegerConstraint**: it defaults to {{Value|0}}. If it is {{Value|1}} or larger, the [App Link](App_Link.md) will behave like an array, and will duplicate the same **Linked Object** many times. If **Show Elements** is `True`, each element in the array will be displayed in the [tree view](tree_view.md), and each can have its own **Placement** modified. Each Link copy will have a name based on the Link\'s [Name](Object_name.md), augmented by `_iN`, where `N` is a number starting from `0`. For example, with a single `Link`, the copies will be named `Link_i0`, `Link_i1`, `Link_i2`, etc.

-    **Link Execute|String**: name of the execute function that will run for this particular Link object. It defaults to {{Value|'appLinkExecute'}}. Set it to {{Value|'None'}} to disable it.

-    **Colored Elements|LinkSubHidden|Hidden**: list of Link elements that have had their color overriden.

-    **Scale|Float**: it defaults to {{Value|1.0}}. It is a factor for uniform scaling in each direction `X`, `Y`, and `Z`. For example, a cube of {{Value|2 mm}} x {{Value|2 mm}} x {{Value|2 mm}}, that is scaled by {{Value|2.0}}, will result in a shape with dimensions {{Value|4 mm}} x {{Value|4 mm}} x {{Value|4 mm}}.

-    **Scale Vector|Vector|Hidden**: the scale factor for each component `(X, Y, Z)` for all Link elements when **Element Count** is {{Value|1}} or larger. If **Scale** is other than {{Value|1.0}}, this same value will be used in the three components.

-    **Scale List|VectorList**: the scale factor for each Link element.

-    **Visibility List|BoolList|Hidden**: {{emphasis|(read-only)}} the visibility state of each Link element, either `True` or `False`.

-    **Placement List|PlacementList|Hidden**: {{emphasis|(read-only)}} the placement for each Link element.

-    **Element List|LinkList|Hidden**: the list of Link elements.

-    **_LinkTouched|Bool|Hidden**:

-    **_ChildCache|LinkList|Hidden**:


{{TitleProperty|Base}}

-    **Proxy|PythonObject|Hidden**: a custom class associated with this object. This only exists for the [Python](Python.md) version. See [Scripting](Std_LinkMake#Scripting.md).

The [App Link](App_Link.md) object will additionally show the properties of the original **Linked Object**, so the [property editor](property_editor.md) may have groups of properties like {{TitleProperty|Attachment}}, {{TitleProperty|Box}}, {{TitleProperty|Draft}}, etc.



### Ansicht


{{TitleProperty| Link}}

-    **Draw Style|Enumeration**: it defaults to {{Value|None}}; it can be {{value|Solid}}, {{value|Dashed}}, {{value|Dotted}}, {{value|Dashdot}}; defines the style of the edges in the [3D view](3D_view.md).

-    **Line Width|FloatConstraint**: a float that determines the width in pixels of the edges in the [3D view](3D_view.md). It defaults to {{value|2.0}}.

-    **Override Material|Bool**: it defaults to `False`; if set to `True` it will override the **Linked Object**\'s material, and it will display the colors defined in **Shape Material**.

-    **Point Size|FloatConstraint**: similar to **Line Width**, defines the size of the vertices.

-    **Selectable|Bool**: if it is `True`, the object can be picked with the pointer in the [3D view](3D_view.md). Otherwise, the object cannot be selected until this option is set to `True`.

-    **Shape Material|Material**: this property includes sub-properties that describe the appearance of the object.

    -   
        **Diffuse Color**
        
        , it defaults to  light blue .

    -   
        **Ambient Color**
        
        , it defaults to  dark gray .

    -   
        **Specular Color**
        
        , it defaults to  black .

    -   
        **Emissive Color**
        
        , it defaults to  black .

    -   
        **Shininess**
        
        , it defaults to {{Value|0.2}}

    -   
        **Transparency**
        
        , it defaults to {{Value|0.0}}.


{{TitleProperty|Base}}

-    **Child View Provider|PersistentObject|Hidden**:

-    **Material List|MaterialList|Hidden**: **(read-only)** if individual materials have been added, they will be listed here.

-    **Override Color List|ColorList|Hidden**: **(read-only)** if the individual faces or edges of the link have been overridden they will be listed here.

-    **Override Material List|BoolList|Hidden**: **(read-only)** if the individual materials of the link have been overridden they will be listed here.


{{TitleProperty|Display Options}}

-    **Display Mode|Enumeration**: {{Value|'Link'}} or {{Value|'ChildView'}}.

-    **Show In Tree|Bool**: see the information in [App FeaturePython](App_FeaturePython.md).

-    **Visibility|Bool**: see the information in [App FeaturePython](App_FeaturePython.md).


{{TitleProperty|Selection}}

-    **On Top When Selected|Enumeration**: see the information in [App FeaturePython](App_FeaturePython.md).

-    **Selection Style|Enumeration**: see the information in [App FeaturePython](App_FeaturePython.md).

It will additionally show the view properties of the original **Linked Object**.



## Vererbung

An [App Link](App_Link.md) is formally an instance of the class `App::Link`, whose parent is the basic [App DocumentObject](App_DocumentObject.md) (`App::DocumentObject` class). It is a very low level object, which can be used with most other document objects.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Simplified diagram of the relationships between the core objects in the program. The `App::Link* object is a core component of the system, it does not depend on any workbench, but it can be used with most objects created in all workbenches.`



## Skripten


**Siehe auch:**

[Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md) und [Skriptgenerierte Objekte](scripted_objects/de.md).

Für allgemeine Informationen, siehe [Part Formelement](Part_Feature/de.md).

An App Link is created with the `addObject()` method of the document. It can define its **Linked Object** by overriding its `LinkedObject` attribute, or by using its `setLink` method. 
```python
import FreeCAD as App

doc = App.newDocument()
bod1 = App.ActiveDocument.addObject("Part::Box", "Box")
bod2 = App.ActiveDocument.addObject("Part::Cylinder", "Cylinder")
bod1.Placement.Base = App.Vector(10, 0, 0)
bod2.Placement.Base = App.Vector(0, 10, 0)

obj1 = App.ActiveDocument.addObject("App::Link", "Link")
obj2 = App.ActiveDocument.addObject("App::Link", "Link")

obj1.LinkedObject = bod1
obj2.setLink(bod2)
obj1.Placement.Base = App.Vector(-10, -10, 0)
obj2.Placement.Base = App.Vector(10, -10, 0)
obj1.ViewObject.OverrideMaterial = True
App.ActiveDocument.recompute()
```

The basic `App::Link` doesn\'t have a Proxy object so it can\'t be fully used for sub-classing.

Therefore, for [Python](Python.md) subclassing, you should create the `App::LinkPython` object.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::LinkPython", "Link")
obj.Label = "Custom label"
```



## Weiterführende Literatur 

Das Objekt [Anwendung Verknüpfung](App_Link/de.md) wurde nach 2 Jahren Entwicklung und Prototypenfertigung eingeführt. Diese Komponente wurde fast im Alleingang vom Benutzer **realthunder** ausgedacht und entwickelt. Die Motivationen und Entwurfsimplementierungen hinter diesem Projekt sind in seiner GitHub Seite [Link](https://github.com/realthunder/FreeCAD_assembly3/wiki/Link) beschrieben. Um dieses Feature zu erreichen, wurden einige Kernänderungen an FreeCAD vorgenommen; diese wurden auch ausführlich dokumentiert in [Core-Changes](https://github.com/realthunder/FreeCAD_assembly3/wiki/Core-Changes).

The App Link project started after the redesign of the [PartDesign Workbench](PartDesign_Workbench.md) was complete in v0.17. The history of App Link can be traced to some essential forum threads:

-   [Why an object can only be inside one App::Part?](https://forum.freecadweb.org/viewtopic.php?f=19&t=21505) (March 2017)
-   [Introducing App::Link/XLink](https://forum.freecadweb.org/viewtopic.php?f=10&t=21586) (March 2017)
-   [Links](https://forum.freecadweb.org/viewtopic.php?f=20&t=22216) (May 2017)
-   [Realthunder Link implementation: Architecture discussion](https://forum.freecadweb.org/viewtopic.php?f=20&t=23015) (June 2017)
-   [PR #876: Link, stage one, context aware selection](https://forum.freecadweb.org/viewtopic.php?f=17&t=23419) (July 2017)
-   [Preview: Link, stage two, API groundwork](https://forum.freecadweb.org/viewtopic.php?f=17&t=23626) (July 2017)
-   [Assembly3 preview](https://forum.freecadweb.org/viewtopic.php?f=20&t=25712) (December 2017)
-   [Merging of my Link branch](https://forum.freecadweb.org/viewtopic.php?f=10&t=29542) (June 2018)

Finally, the pull request and merge happened:

-   [App::Link: the big merge](https://forum.freecadweb.org/viewtopic.php?f=27&t=38621), old thread (July 2019), [pull request #2350](https://github.com/FreeCAD/FreeCAD/pull/2350) (the BIG merge), [LinkMerge branch](https://github.com/realthunder/FreeCAD/tree/LinkMerge).
-   [App::Link: the big merge](https://forum.freecadweb.org/viewtopic.php?f=8&t=37757), main thread (July 2019)
-   [A simple path description of Link, 019, Link stage, Asm3, merge?](https://forum.freecadweb.org/viewtopic.php?p=329054#p329054) (August 2019)
-   [PR#2559: expose link and navigation actions](https://forum.freecadweb.org/viewtopic.php?f=17&t=39672), an introduction to the Link feature in 0.19 (September 2019).

Other miscellaneous \"links\" about Link include:

-   [Dynamic linked object](Dynamic_linked_object.md) - A pattern with Link and assemblies that aims to reduce duplication of assembly related logic such as orientation, positioning, or number of instances.





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std LinkMake/de
