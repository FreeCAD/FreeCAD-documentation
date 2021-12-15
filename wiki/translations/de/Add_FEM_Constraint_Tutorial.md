# Add FEM Constraint Tutorial/de
{{TutorialInfo/de
|Topic= FEM Beschränkung hinzufügen
|Level= 
|Time= 
|Author=_
|FCVersion=
|Files=
}}

## Einführung

In diesem Tutorium werden wir die Fließgeschwindigkeitsbeschränkung zu FreeCAD hinzufügen und Unterstützung für den Elmer Löser implementieren. Bitte stelle sicher, dass du [FEM Modul erweitern](Extend_FEM_Module/de.md) gelesen und verstanden hast, bevor du dieses Tutorial liest.

Dieses Tutorium umfasst nur die Implementierung von Beschränkungen in Python. Im Gegensatz zu Löser und Gleichungsbeschränkungen folge der klassischen FEM Modulstruktur. Das heißt, alle Module einer Beschränkung haben dort entweder im `femobjects` oder `femviewprovider` Paket Platz.

## Zusammenfassung

1.  **Erstelle Dokumentobjekt:** Das Dokumentobjekt, das sich innerhalb der Analyse befindet und durch das die Beschränkung parametrisiert und an Grenzen angehängt werden kann.
2.  **Erstelle GUI Befehl:** Füge dem FEM Arbeitsbereich einen Befehl hinzu, der der aktiven Analyse eine Durchflussbeschränkung hinzufügt.
3.  **Erstelle ein Aufgabenpaneel:** Das Aufgabenpaneel ist erforderlich, um dem Anwender die Möglichkeit zu gewähren, die Grenzen festzulegen, an denen er die Geschwindigkeitsbeschränkung festlegen möchte. Es macht auch die Eingabe der Parameter etwas benutzerfreundlicher.
4.  **Erweitere Elmers Schreiber:** Füge Unterstützung für die neue Beschränkung Elmer hinzu, durch erweitern seines sif Datei Exportierers.

## Dokument-Objekt erstellen 

In diesem Schritt werden wir die folgenden Dateien modifizieren:

-    {{FileName|src/Mod/Fem/CMakeLists.txt}}
    

-    {{FileName|src/Mod/Fem/App/CMakeLists.txt}}
    

-    {{FileName|src/Mod/Fem/ObjectsFem.py}}
    

Und füge die folgenden Dateien hinzu:

-    {{FileName|src/Mod/Fem/femobjects/constraint_flowvelocity.py}}
    

-    {{FileName|src/Mod/Fem/femviewprovider/view_constraint_flowvelocity.py}}
    

Für die neue Beschränkung sind ein Dokument-Proxy und ein Ansicht-Proxy erforderlich. Diese liegen in separaten Modulen vor. Der Dokument-Proxy in femobjects und der Ansicht-Proxy in femviewprovider. Kopiere einfach die Module aus einer bestehenden Beschränkung, z.B.:

-    {{FileName|femobjects/constraint_selfweight.py}}
    

-    {{FileName|femviewprovider/view_constraint_selfweight.py}}
    

Passe die Typvariable und die Eigenschaften an deine Bedürfnisse an. Der Dokumentproxy der Fließbeschränkung sieht wie folgt aus:


```python
class Proxy(FemConstraint.Proxy):
    Type = "Fem::ConstraintFlowVelocity"
    def __init__(self, obj):
        super(Proxy, self).__init__(obj)
        obj.addProperty(
            "App::PropertyFloat", "VelocityX",
            "Parameter", "Body heat flux")
        obj.addProperty(
            "App::PropertyBool", "VelocityXEnabled",
            "Parameter", "Body heat flux")
        obj.addProperty(
            "App::PropertyFloat", "VelocityY",
            "Parameter", "Body heat flux")
        obj.addProperty(
            "App::PropertyBool", "VelocityYEnabled",
            "Parameter", "Body heat flux")
        obj.addProperty(
            "App::PropertyFloat", "VelocityZ",
            "Parameter", "Body heat flux")
        obj.addProperty(
            "App::PropertyBool", "VelocityZEnabled",
            "Parameter", "Body heat flux")
        obj.addProperty(
            "App::PropertyBool", "NormalToBoundary",
            "Parameter", "Body heat flux")
```

Das Modul, das den Ansichtproxy enthält, könnte etwas komplizierter aussehen. Aber für den Moment passe einfach den Symbolpfad an. Wir werden in späteren Schritten des Tutoriums auf diese Datei zurückkommen.


```python
class ViewProxy(FemConstraint.ViewProxy):
    def getIcon(self):
        return ":/icons/fem-constraint-flow-velocity.svg"
```

Füge die beiden neuen Module zum Bausystem hinzu, wie in [FEM Modul erweitern](https://www.freecadweb.org/wiki/Extend_FEM_Module) beschrieben. Suche die richtige Liste auf, durch Suchen nach Beschränkungsmodulen.

Wie alle Objekte des FEM-Arbeitsbereiches muss die Geschwindigkeitsbeschränkung in `ObjectsFem.py` registriert werden. Die folgende Methode fügt dem aktiven Dokument eine Geschwindigkeitsbeschränkung hinzu. Diese Methode wird vom GUI-Befehl verwendet, um die Beschränkung hinzuzufügen. Sie muss irgendwo in `ObjectsFem.py` eingefügt werden.


```python
def makeConstraintFlowVelocity(name="FlowVelocity"):
    obj = FreeCAD.ActiveDocument.addObject("Fem::ConstraintPython", name)
    import femobjects.constraint_flowvelocity
    femobjects.constraint_flowvelocity.Proxy(obj)
    if FreeCAD.GuiUp:
        import femviewprovider.view_constraint_flowvelocity
        femviewprovider.view_constraint_flowvelocity.ViewProxy(obj.ViewObject)
    return obj
```

## GUI Befehl erstellen 

In diesem Schritt werden wir die folgenden Dateien modifizieren:

-    {{FileName|src/Mod/Fem/CMakeLists.txt}}
    

-    {{FileName|src/Mod/Fem/App/CMakeLists.txt}}
    

-    {{FileName|src/Mod/Fem/Gui/Workbench.cpp}}
    

Und die folgende neue Datei hinzufügen:

-    {{FileName|src/Mod/Fem/femobjects/constraint_flowvelocity.py}}
    

Der Befehl ermöglicht es dem Anwender, die Beschränkung tatsächlich zur aktiven Analyse hinzuzufügen. Kopiere einfach einen Befehl aus einer vorhandenen Beschränkung. Die Befehle befinden sich im Paket `femviewprovider`. Passe das Attribut resources und die in Activated aufgerufene make-Methode deinen Bedürfnissen an. Verwende auch eine andere Befehls-ID im addCommand-Aufruf am unteren Ende des Moduls. Die folgende Klasse ist die Befehlsklasse der Geschwindigkeitsbeschränkung.


```python
class Command(FemCommands.FemCommands):

    def __init__(self):
        super(Command, self).__init__()
        self.resources = {
            'Pixmap': 'fem-constraint-flow-velocity',
            'MenuText': QtCore.QT_TRANSLATE_NOOP(
                "FEM_ConstraintFlowVelocity",
                "Constraint Velocity"),
            'ToolTip': QtCore.QT_TRANSLATE_NOOP(
                "FEM_ConstraintFlowVelocity",
                "Creates a FEM constraint body heat flux")}
        self.is_active = 'with_analysis'

    def Activated(self):
        App.ActiveDocument.openTransaction(
            "Create FemConstraintFlowVelocity")
        Gui.addModule("ObjectsFem")
        Gui.doCommand(
            "FemGui.getActiveAnalysis().Member += "
            "[ObjectsFem.makeConstraintFlowVelocity()]")

Gui.addCommand('FEM_AddConstraintFlowVelocity', Command())
```

Füge die neue Befehlsdatei zum Bausystem hinzu, wie in [FEM Modul erweitern](https://www.freecadweb.org/wiki/Extend_FEM_Module) beschrieben. Ermittle die richtige Liste, durch Suchen nach vorhandenen Befehlsmodulen.

Gib den Befehl in Gui/Workbench.cpp ein, um ihn der Symbolleiste und dem Menü hinzuzufügen. Suche nach einer vorhandenen Beschränkung der gleichen Kategorie wie die neue (z.B. Flow), kopiere und füge sie ein und passe die Befehls ID an. Dies sollte zweimal durchgeführt werden. Einmal für das Menü und noch einmal für die Werkzeugleiste.

## Erstelle ein Aufgabenpaneel 

In diesem Schritt werden wir die folgenden Dateien modifizieren:

-    {{FileName|src/Mod/Fem/femviewprovider/view_constraint_flowvelocity.py}}
    

In FreeCAD profitieren Beschränkungsobjekte stark von Aufgabenpaneels. Aufgabenpaneels können leistungsfähigere Eingabebedienelemente verwenden, die dem Benutzer die Einheit der eingegebenen Werte direkt anzeigen. Die Geschwindigkeitsbeschränkung erfordert sogar die Verwendung eines Aufgabenpaneels, da ein Aufgabenpaneel die einzige Möglichkeit ist, die Fläche(n) zu spezifizieren, auf die die Beschränkung angewendet werden soll.

Der Standort des Moduls, in dem die Aufgabenpanels implementiert werden, ist nicht streng definiert. Für die Geschwindigkeitsbeschränkung werden wir das Aufgabenpaneel einfach in dasselbe Modul setzen, in das wir den Ansichtsproxy setzen. Das Aufgabenpaneel ist ziemlich kompliziert. Es verwendet die Funktion FemSolectionWidgets.BoundarySelector(). Dabei handelt es sich um ein qt Bedienelement, mit dem der Benutzer die Grenzen auswählen kann, auf die die Beschränkung angewendet werden soll. Zusätzlich zu diesem Bedienelement erzeugt es ein weiteres, indem es eine speziell für die Geschwindigkeitsbeschränkung erstellte ui Datei lädt. Über dieses Bedienelement kann der Geschwindigkeitsvektor spezifiziert werden.

Die meiste Zeit sollte ausreichen, diese Klasse einfach zu kopieren, eine geeignete ui Datei zu verwenden (anstelle von TaskPanelFemFlowVelocity.ui) und \_initParamWidget() sowie \_applyWidgetChanges() anzupassen. Wenn die neue Beschränkung Körper als Referenzen anstelle von Begrenzungen erfordert, ersetze einfach das BoundarySelector Objekt durch das SolidSelector Objekt.


```python
class _TaskPanel(object):

    def __init__(self, obj):
        self._obj = obj
        self._refWidget = FemSelectionWidgets.BoundarySelector()
        # self._refWidget = FemSelectionWidgets.SolidSelector()
        self._refWidget.setReferences(obj.References)
        self._paramWidget = Gui.PySideUic.loadUi(
            App.getHomePath() + "Mod/Fem/femviewprovider/TaskPanelFemFlowVelocity.ui")
        self._initParamWidget()
        self.form = [self._refWidget, self._paramWidget]
        analysis = FemMisc.findAnalysisOfMember(obj)
        self._mesh = FemMisc.getSingleMember(analysis, "Fem::FemMeshObject")
        self._part = self._mesh.Part if self._mesh is not None else None
        self._partVisible = None
        self._meshVisible = None

    def open(self):
        if self._mesh is not None and self._part is not None:
            self._meshVisible = self._mesh.ViewObject.isVisible()
            self._partVisible = self._part.ViewObject.isVisible()
            self._mesh.ViewObject.hide()
            self._part.ViewObject.show()

    def reject(self):
        self._restoreVisibility()
        return True

    def accept(self):
        if self._obj.References != self._refWidget.references():
            self._obj.References = self._refWidget.references()
        self._applyWidgetChanges()
        self._obj.Document.recompute()
        self._restoreVisibility()
        return True

    def _restoreVisibility(self):
        if self._mesh is not None and self._part is not None:
            if self._meshVisible:
                self._mesh.ViewObject.show()
            else:
                self._mesh.ViewObject.hide()
            if self._partVisible:
                self._part.ViewObject.show()
            else:
                self._part.ViewObject.hide()

    def _initParamWidget(self):
        unit = "m/s"
        self._paramWidget.velocityXTxt.setText(
            str(self._obj.VelocityX) + unit)
        self._paramWidget.velocityYTxt.setText(
            str(self._obj.VelocityY) + unit)
        self._paramWidget.velocityZTxt.setText(
            str(self._obj.VelocityZ) + unit)
        self._paramWidget.velocityXBox.setChecked(
            not self._obj.VelocityXEnabled)
        self._paramWidget.velocityYBox.setChecked(
            not self._obj.VelocityYEnabled)
        self._paramWidget.velocityZBox.setChecked(
            not self._obj.VelocityZEnabled)
        self._paramWidget.normalBox.setChecked(
            self._obj.NormalToBoundary)

    def _applyWidgetChanges(self):
        unit = "m/s"
        self._obj.VelocityXEnabled = \
            not self._paramWidget.velocityXBox.isChecked()
        if self._obj.VelocityXEnabled:
            quantity = Units.Quantity(self._paramWidget.velocityXTxt.text())
            self._obj.VelocityX = float(quantity.getValueAs(unit))
        self._obj.VelocityYEnabled = \
            not self._paramWidget.velocityYBox.isChecked()
        if self._obj.VelocityYEnabled:
            quantity = Units.Quantity(self._paramWidget.velocityYTxt.text())
            self._obj.VelocityY = float(quantity.getValueAs(unit))
        self._obj.VelocityZEnabled = \
            not self._paramWidget.velocityZBox.isChecked()
        if self._obj.VelocityZEnabled:
            quantity = Units.Quantity(self._paramWidget.velocityZTxt.text())
            self._obj.VelocityZ = float(quantity.getValueAs(unit))
        self._obj.NormalToBoundary = self._paramWidget.normalBox.isChecked()
```

Der Ansichtproxy muss erweitert werden, um das Aufgabenpaneel zu unterstützen, das wir gerade implementiert haben. Der folgende erweiterte Ansichtproxy öffnet das Aufgabenpaneel, wenn der Anwender einen Doppelklick auf das Beschränkungsobjekt in der Baumansicht macht.


```python
class ViewProxy(FemConstraint.ViewProxy):

    def getIcon(self):
        return ":/icons/fem-constraint-flow-velocity.svg"

    def setEdit(self, vobj, mode=0):
        task = _TaskPanel(vobj.Object)
        Gui.Control.showDialog(task)

    def unsetEdit(self, vobj, mode=0):
        Gui.Control.closeDialog()

    def doubleClicked(self, vobj):
        if Gui.Control.activeDialog():
            Gui.Control.closeDialog()
        Gui.ActiveDocument.setEdit(vobj.Object.Name)
        return True
```

## Elmers Schreiber erweitern 

In diesem Schritt werden wir die folgenden Dateien modifizieren:

-    {{FileName|src/Mod/Fem/femsolver/elmer/writer.py}}
    

Das Schreiber Modul enthält Methoden für alle Gleichungstypen. Je nach Art der Beschränkung, Randbedingung, Anfangsbedingung oder Körperkraft muss man unterschiedliche Methoden modifizieren. Für unsere Strömungsgeschwindigkeit müssen wir `_handleFlowBndConditions(...)` anpassen.


```python
def _handleFlowBndConditions(self):
    for obj in self._getMember("Fem::ConstraintFlowVelocity"):
        if obj.References:
            for name in obj.References[0][1]:
                if obj.VelocityXEnabled:
                    velocity = getFromUi(obj.VelocityX, "m/s", "L/T")
                    self._boundary(name, "Velocity 1", velocity)
                if obj.VelocityYEnabled:
                    velocity = getFromUi(obj.VelocityY, "m/s", "L/T")
                    self._boundary(name, "Velocity 2", velocity)
                if obj.VelocityZEnabled:
                    velocity = getFromUi(obj.VelocityZ, "m/s", "L/T")
                    self._boundary(name, "Velocity 3", velocity)
                if obj.NormalToBoundary:
                    self._boundary(name, "Normal-Tangential Velocity", True)
            self._handled(obj)
```

_

---
[documentation index](../README.md) > [FEM](Category_FEM.md) > Add FEM Constraint Tutorial/de
