# Add FEM constraint tutorial/ro



<div class="mw-translate-fuzzy">


{{TutorialInfo/ro
|Topic= 
|Level= 
|Time= 
|Author=[M42kus](User:M42kus.md)
|FCVersion=
|Files=
}}


</div>

## Introduction

În acest tutorial vom adăuga constrângerea vitezei fluxului la FreeCAD și vom implementa suportul pentru elmer solver. Asigurați-vă că ați citit și ați înțeles [Extend FEM Module](Extend_FEM_Module.md) înainte de a citi acest tutorial.


<div class="mw-translate-fuzzy">

Acest tutorial acoperă doar modul de implementare a constrângerilor în Python. Spre deosebire de constrângerile solver și ecuații, urmați structura modulului FEM clasic. Adică toate modulele unei constrângeri au loc în pachetul PyObjects sau PyGui.


</div>

## Sumar

1.  **Create document object:** Obiectul documentului care se află în analiză și în care constrângerea poate fi parametrizată și legată de limite.
2.  **Create GUI command:** Adăugați o comandă la atelierul FEM care adaugă o constrângere a fluxului la analiza activă.
3.  **Create a task panel:** Panoul de sarcini este necesar pentru a permite utilizatorului să definească limitele la care dorește să definească constrângerea de viteză. Acest lucru face ca intrarea parametrilor să fie mai ușor de utilizat.
4.  **Extend elmers writer:** Adăugați suport pentru noua constrângere modulul Elmer FEM solver prin dezactivarea exportatorului de fișiere sif.


<div class="mw-translate-fuzzy">

## Crearea Documentului Obiect 


</div>

În acest pas vom modifica următoarele fișiere:

-    {{FileName|src/Mod/Fem/CMakeLists.txt}}
    

-    {{FileName|src/Mod/Fem/App/CMakeLists.txt}}
    

-    {{FileName|src/Mod/Fem/ObjectsFem.py}}
    


<div class="mw-translate-fuzzy">

și adăugați următoarele fișiere:


</div>

-    {{FileName|src/Mod/Fem/femobjects/constraint_flowvelocity.py}}
    

-    {{FileName|src/Mod/Fem/femviewprovider/view_constraint_flowvelocity.py}}
    


<div class="mw-translate-fuzzy">

Un document proxy și o vedere proxy sunt necesare pentru noua constrângere. Acestea se află în module separate. Proxy documentul în PyObjects și vederea proxy în PyGui. Trebuie doar să copiați modulele dintr-o constrângere existentă, de ex.


</div>

-    {{FileName|femobjects/constraint_selfweight.py}}
    

-    {{FileName|femviewprovider/view_constraint_selfweight.py}}
    

Reglați tipul de variabilă și proprietățile la nevoile dvs. Proxy-ul documentului al constrângerii fluxului arată după cum urmează:


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

Modulul care conține proxy-ul ar putea părea puțin mai complicat. Dar pentru moment ajustați calea pictogramelor. Vom reveni la acest dosar.


```python
class ViewProxy(FemConstraint.ViewProxy):
    def getIcon(self):
        return ":/icons/fem-constraint-flow-velocity.svg"
```

Adăugați cele două module noi la construirea sistemului descrisă în [Extend FEM Module](https://www.freecadweb.org/wiki/Extend_FEM_Module). Găsiți lista de căutare corectă pentru modulele de constrângere.


<div class="mw-translate-fuzzy">

Ca toate obiectele din bancul de lucru FEM, constrângerile de viteză trebuie să fie înregistrate ObjectsFem.py. Următoarea metodă adaugă viteza documentului activ. Această metodă va fi utilizată de comanda GUI pentru a adăuga constrângerea. Trebuie să fie inserat undeva în ObjectsFem.py.


</div>


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

## Creează o camandă GUI 

În acest pas vom modifica următoarele fișiere:

-    {{FileName|src/Mod/Fem/CMakeLists.txt}}
    

-    {{FileName|src/Mod/Fem/App/CMakeLists.txt}}
    

-    {{FileName|src/Mod/Fem/Gui/Workbench.cpp}}
    


<div class="mw-translate-fuzzy">

și adăugați următorul fișier nou:


</div>

-    {{FileName|src/Mod/Fem/femobjects/constraint_flowvelocity.py}}
    


<div class="mw-translate-fuzzy">

Comanda permite utilizatorului să adauge constrângerea la analiza activă. Trebuie doar să copiați o comandă dintr-o constrângere existentă. Commands reside in the PyGui package. Ajustați resursele și efectuați metoda numită Activat la nevoile dvs. Utilizați, de asemenea, o comandă diferită id in the addCommand apel în partea de jos a modulului. Următoarea clasă este clasa constrângerii vitezei.


</div>


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

Adăugați noua comandă în sistem așa cum este încorporată [Extend FEM Module](https://www.freecadweb.org/wiki/Extend_FEM_Module). Identificați lista corectă pentru a căuta modulele de comandă existente.

Puneți o comandă în Gui/Workbench.cpp pentru a o adăuga în bara de instrumente și în meniu. Căutați o constrângere existentă din aceeași categorie ca cea nouă (de exemplu, Flow) copiați-o și adaptați id-ul comenzii. Acest lucru ar trebui făcut de două ori. Odată pentru meniu și din nou pentru bara de instrumente.


<div class="mw-translate-fuzzy">

## Creara Task Panel 


</div>

În acest pas vom modifica următorul fișier:

-    {{FileName|src/Mod/Fem/femviewprovider/view_constraint_flowvelocity.py}}
    

În obiectele de constrângere FreeCAD beneficiați foarte mult de panourile de sarcini. Tsolicită panourile pot utiliza mai multe widget-uri de intrare mai puternice care expun unitatea de valori introduse direct către utilizator. Constrângerea de viteză presupune chiar utilizarea unui task panel(panou de sarcini), deoarece un panou de sarcini este singura modalitate de a specifica fața pe care trebuie aplicată constrângerea.

Localizarea modulului în care sunt implementate panourile de sarcini nu este strict definită. Pentru constrângerea de viteză, vom pune doar panoul de sarcini în același modul pe care îl punem proxy-ul de vizualizare. Panoul de sarcini este destul de complicat. Folosește FemSolectionWidgets.BoundarySelector(). Acesta este modul în care widget-ul permite utilizatorului să selecteze limitele pe care va fi aplicată constrângerea. În plus față de acest widget, acesta generează un altul prin încărcarea unui fișier ui specific creat pentru constrângerea de viteză. Prin intermediul acestui widget se poate specifica vectorul de viteză.

Majoritatea timpului ar trebui să fie suficient, trebuie doar să utilizați acest fișier (în schimbul TaskPanelFemFlowVelocity.ui) și adjust \_initParamWidget() la fel ca \_applyWidgetChanges(). Dacă noua constrângere necesită ca referințe corpuri în loc de limite, pur și simplu înlocuiți obeictul BoundarySelector cu SolidSelector.


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

Proxy-ul de vizualizare trebuie extins pentru a sprijini panoul de sarcini pe care tocmai l-am implementat. Următoarea vizualizare extinsă deschide panoul de sarcini atunci când utilizatorul face dublu clic pe obiectul constrângere din vizualizarea arborescentă.


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


<div class="mw-translate-fuzzy">

## Extensia Elmer FEM solver Writer 


</div>

În acest pas vom modifica următorul fișier:

-    {{FileName|src/Mod/Fem/femsolver/elmer/writer.py}}
    


<div class="mw-translate-fuzzy">

Modulul de scriere conține metode pentru toate tipurile de ecuații. În funcție de tipul de restricție, de condiția de limită, de starea inițială sau de forța corpului, trebuie modificate diferite metode. Pentru viteza fluxului nostru trebuie să ne ajustăm \_handleFlowBndConditions(\...).


</div>


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

[Category:FEM](Category:FEM.md)
