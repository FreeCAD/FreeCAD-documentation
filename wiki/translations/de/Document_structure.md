# Document structure/de
{{TOCright}}

![](images/Screenshot_treeview.jpg ) Ein FreeCAD Dokument enthält alle Objekte deiner Arbeitsumgebung. Es kann Gruppen und Objekte enthalten, die Sie mit den Arbeitsbereichen erstellt haben. Daher kannst du zwischen Arbeitsbereichen wechseln und immer noch im selben Dokument arbeiten. Es ist das Dokument, das gespeichert wird, wenn du deine Arbeit auf Datenträger speichern. Du kannst sowohl mehrere Dokumente gleichzeitig in FreeCAD öffnen, als auch mehrere Ansichten im selben Dokument.

Innerhalb des Dokuments können die Objekte in Gruppen geschoben werden und haben einen eindeutigen Namen. Das Verwalten von Gruppen, Objekten und Objektnamen wird vor allem in der [Baumansicht](Tree_view/de.md) erledigt. **Hinweis:** Es kann natürlich auch, wie alles in FreeCAD, über den [Python](Python/de.md)-Interpreter geschehen. In der [Baumansicht](Tree_view/de.md) können durch einen Rechtsklick in der [Baumansicht](Tree_view/de.md) <img alt="" src=images/Std_Group.svg  style="width:16px;"> [Gruppen](Std_Group/de.md) erstellt, Objekte in Gruppen eingefügt, Objekte oder Gruppen gelöscht, oder bei einem Objekt durch einen Doppelklick auf dessen Namen, dieses umbenannt oder eventuell andere Operationen durchgeführt werden, abhängig vom aktiven Arbeitsbereich.

Die Objekte innerhalb eines FreeCAD Dokuments können unterschiedlichen Typs sein. Jeder Arbeitsbereich kann seinen eigenen Typ von Objekten erstellen, zum Beispiel schafft der <img alt="" src=images/Workbench_Mesh.svg  style="width:16px;">[Netz Arbeitsbereich](Mesh_Workbench/de.md) Polygonnetzobjekte, der <img alt="" src=images/Workbench_Part.svg  style="width:16px;">[Part Arbeitsbereich](Part_Workbench/de.md) erstellt Teil Objekte, der <img alt="" src=images/Workbench_Draft.svg  style="width:16px;">[Entwurf Arbeitsbereich](Draft_Workbench/de.md) erstellt auch Teil Objekte, usw.

Wenn mindestens ein Dokument in FreeCAD geöffnet ist, gibt es immer **ein** und **nur ein** aktives Dokument. Das ist das Dokument, das in der aktuellen 3D-Ansicht angezeigt wird, das Dokument, an welchem Sie derzeit arbeiten.

## Anwendungs- und Benutzeroberfläche 

Wie fast alles andere in FreeCAD ist der Teil der grafischen Benutzeroberfläche (GUI) vom Teil der Basisanwendung (App) getrennt. Dies gilt auch für Dokumente. Die Dokumente bestehen ebenfalls aus zwei Teilen: dem Anwendungsdokument, das unsere Objekte enthält, und dem Ansichtsdokument, das die Darstellung unserer Objekte auf dem Bildschirm enthält.

Stelle es dir als zwei Räume vor, in denen die Objekte definiert werden. Ihre konstruktiven Parameter (ist es ein Würfel? ein Kegel? welche Grösse?) werden im Anwendungsdokument gespeichert, während ihre graphische Darstellung (wird sie mit schwarzen Linien gezeichnet? mit blauen Flächen?) im View Dokument gespeichert wird. Warum ist das so? Weil FreeCAD auch mit {{emphasis|ohne}} graphischer Oberfläche z.B. in anderen Programmen verwendet werden kann, und wir müssen unsere Objekte immer noch verändern können, auch wenn nichts auf dem Bildschirm gezeichnet wird.

Eine andere Sache, die innerhalb des Ansichtsdokuments enthalten ist, sind 3D Ansichten. In einem Dokument können mehrere Ansichten geöffnet sein, so dass Sie Ihr Dokument aus mehreren Blickwinkeln gleichzeitig betrachten können. Vielleicht möchten Sie eine Draufsicht und eine Frontansicht Ihre Arbeit gleichzeitig sehen? Dann haben Sie zwei Ansichten des gleichen Dokuments, beide in nur einem Ansichts-Dokument gespeichert. Das Erstellen neuer Ansichten oder das Schließen von Ansichten kann über das Menü Ansicht oder durch Rechtsklicken auf einen Ansichtsreiter erfolgen.

## Skripten

Dokumente können mit dem [Python](Python/de.md) Interpreter einfach erstellt, aufgerufen und geändert werden. Zum Beispiel: 
```python
FreeCAD.ActiveDocument
``` Gibt das aktuelle (aktive) Dokument zurück 
```python
FreeCAD.ActiveDocument.Blob
``` Greift auf das Objekt namens \"Blob\" innerhalb Ihres Dokuments zu 
```python
FreeCADGui.ActiveDocument
``` Geht zurück zum Ansichts-Dokument, das mit dem aktuellen Dokument verbunden ist. 
```python
FreeCADGui.ActiveDocument.Blob
``` Greift zu auf den grafischen Darstellungsteil(view) Ihres Blob-Objekts 
```python
FreeCADGui.ActiveDocument.ActiveView
``` Gibt die aktuelle Ansicht zurück



---
![](images/Button_right.svg) [documentation index](../README.md) > Document structure/de
