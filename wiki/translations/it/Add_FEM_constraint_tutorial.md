# Add FEM constraint tutorial/it
<div class="mw-translate-fuzzy">


{{TutorialInfo/it
|Topic=Aggiungere vincoli FEM 
|Level= 
|Time= 
|Author=_
|FCVersion=
|Files=
}}


</div>

## Introduction

In questo tutorial aggiungeremo a FreeCAD il vincolo di velocità del flusso e implementeremo il supporto per il risolutore Elmer. Prima di leggere questo tutorial è necessario aver letto e compreso il tutorial [ Estendere il modulo FEM](Extend_FEM_Module/it.md).

This tutorial only covers how to implement constraints in python. In contrast to solver and equations constraints follow the classic FEM module structure. That is, all modules of a constraint have there place in either the {{Incode|femobjects}} or {{Incode|femviewprovider}} package.

## Sommario

1.  **Create document object:** The document object that resides inside the analysis and though which the constraint can be parametrized and attached to boundaries.
2.  **Create GUI command:** Add a command to the FEM workbench that adds a flow constraint to the active analysis.
3.  **Create a task panel:** The task panel is necessary to allow the user to set the boundaries at which he wants to set the velocity constraint. It also makes entering the parameters a little more user friendly.
4.  **Extend elmers writer:** Add support for the new constraint to Elmer by extending its sif file exporter.

## Create document object 

In this step we are going to modify the following files:

-    {{FileName|src/Mod/Fem/CMakeLists.txt}}
    

-    {{FileName|src/Mod/Fem/App/CMakeLists.txt}}
    

-    {{FileName|src/Mod/Fem/ObjectsFem.py}}
    

And add the following files:

-    {{FileName|src/Mod/Fem/femobjects/constraint_flowvelocity.py}}
    

-    {{FileName|src/Mod/Fem/femviewprovider/view_constraint_flowvelocity.py}}
    

A document proxy and a view proxy are required for the new constraint. Those reside in separate modules. The document proxy in femobjects and the view proxy in femviewprovider. Just copy the modules from an existing constraint e.g.:

-    {{FileName|femobjects/constraint_selfweight.py}}
    

-    {{FileName|femviewprovider/view_constraint_selfweight.py}}
    

Adjust the Type variable and the properties to your needs. The document proxy of the flow constraint looks like the following:


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

The module containing the view proxy might look a little more complicated. But for now just adjust the icon path. We are going to come back to this file in later steps of the tutorial.


```python
class ViewProxy(FemConstraint.ViewProxy):
    def getIcon(self):
        return ":/icons/fem-constraint-flow-velocity.svg"
```

Add the two new modules to the build system like described in [Extend FEM Module](https://www.freecadweb.org/wiki/Extend_FEM_Module). Locate the correct list by searching for constraint modules.

As all objects of the FEM workbench the velocity constraint must be registered in {{Incode|ObjectsFem.py}}. The following method adds a velocity constraint to the active document. This method will be used by the GUI command to add the constraint. It must be inserted somewhere in {{Incode|ObjectsFem.py}}.


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

## Create GUI command 

In this step we are going to modify the following files:

-    {{FileName|src/Mod/Fem/CMakeLists.txt}}
    

-    {{FileName|src/Mod/Fem/App/CMakeLists.txt}}
    

-    {{FileName|src/Mod/Fem/Gui/Workbench.cpp}}
    

And add the following new file:

-    {{FileName|src/Mod/Fem/femobjects/constraint_flowvelocity.py}}
    

The command allows the user to actually add the constraint to the active analysis. Just copy a command from an existing constraint. Commands reside in the {{Incode|femviewprovider}} package. Adjust the resources attribute and the make method called in Activated to your needs. Also use a different command id in the addCommand call on the bottom of the module. The following class is the command class of the velocity constraint.


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

Add the new command file to the build system as decripted in [Extend FEM Module](https://www.freecadweb.org/wiki/Extend_FEM_Module). Locate the correct list be searching for existing command modules.

Put the command into Gui/Workbench.cpp to add it to the toolbar and menu. Search for an existing constraint of the same category as the new one (e.g. Flow) copy-paste it and adjust the command id. This should be done two times. Once for the menu and again for the toolbar.

## Create a task panel 

In this step we are going to modify the following file:

-    {{FileName|src/Mod/Fem/femviewprovider/view_constraint_flowvelocity.py}}
    

In FreeCAD constraint objects benefit greatly from task panels. Task panels can make use of more powerful input widgets which expose the unit of entered values directely to the user. The velocity constraint even requires the use of a task panel since a task panel is the only way of specifieing the face(s) on which the constraint shall be applied.

The location of the module in which task panels are implemented is not strictely defined. For the velocity constraint we are just going to put the task panel in the same module we put the view proxy. The task panel is quite complicated. It makes use of the FemSolectionWidgets.BoundarySelector(). Thats a qt widget which allows the user to select the boundaries on which the constraint shall be applied. In addition to this widget it generates another one by loading a ui file specifically created for the velocity constraint. Via this widget the velocity vector can be specified.

Most of the time is should be sufficient to just copy this class, use a suitable ui file (instead of TaskPanelFemFlowVelocity.ui) and adjust \_initParamWidget() as well as \_applyWidgetChanges(). If the new constraint requires bodies as references instead of boundaries just replace the BoundarySelector object with the SolidSelector.


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

The view proxy must be extended to support the task panel we just implemented. The following extended view proxy opens the task panel when the user makes a double click on the constraint object in the tree view.


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

## Extend Elmer\'s writer 

In this step we are going to modify the following file:

-    {{FileName|src/Mod/Fem/femsolver/elmer/writer.py}}
    

The writer module contains methods for all equation types. Depending on the type of the constraint, boundary condition, initial condition or body force one has to modify different methods. For our flow velocity we have to adjust {{Incode|_handleFlowBndConditions(...)}}.


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
[documentation index](../README.md) > [FEM](Category_FEM.md) > Add FEM constraint tutorial/it
