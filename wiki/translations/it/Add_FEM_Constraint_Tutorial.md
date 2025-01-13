---
 TutorialInfo:t
   Topic: Aggiungere vincoli FEM 
   Level:  
   Time:  
   Author: User:M42kus
   FCVersion: 
   Files: 
---

# Add FEM Constraint Tutorial/it







## Introduzione

In questo tutorial, aggiungeremo a FreeCAD il vincolo di velocità del flusso e implementeremo il supporto per il risolutore Elmer. Prima di leggere questo tutorial è necessario aver letto e compreso il tutorial [ Estendere il modulo FEM](Extend_FEM_Module/it.md).

Questo tutorial riguarda solo come implementare i vincoli in Python. A differenza del solutore e delle equazioni, i vincoli seguono la classica struttura del modulo FEM. Cioè, tutti i moduli di un vincolo hanno il loro posto nel pacchetto {{Incode|femobjects}} o {{Incode|femviewprovider}}.



## Sommario

1.  **Creare un oggetto documento:** L\'oggetto documento che risiede all\'interno dell\'analisi e attraverso il quale il vincolo può essere parametrizzato e collegato ai confini.
2.  **Creare un comando GUI:** Aggiungere un comando al workbench FEM che aggiunge un vincolo di flusso all\'analisi attiva.
3.  **Creare un pannello delle attività:** Il pannello delle attività è necessario per consentire all\'utente di impostare i limiti entro i quali deve stare il vincolo di velocità. Inoltre, l\'immissione dei parametri risulta un po\' più facile da attuare.
4.  **Estendere il writer di Elmer:** Aggiungere il supporto per il nuovo vincolo a Elmer estendendo il suo esportatore di file sif.



## Creare un oggetto documento 

In questo passaggio modificheremo i seguenti file:

-    **src/Mod/Fem/CMakeLists.txt**
    

-    **src/Mod/Fem/App/CMakeLists.txt**
    

-    **src/Mod/Fem/ObjectsFem.py**
    

E aggiungeremo i seguenti file:

-    **src/Mod/Fem/femobjects/constraint_flowvelocity.py**
    

-    **src/Mod/Fem/femviewprovider/view_constraint_flowvelocity.py**
    

Per il nuovo vincolo sono necessari un proxy di documento e un proxy di vista. Questi risiedono in moduli separati. Il proxy del documento in femobjects e il proxy della vista in femviewprovider. Basta copiare i moduli da un vincolo esistente, ad esempio:

-    **femobjects/constraint_selfweight.py**
    

-    **femviewprovider/view_constraint_selfweight.py**
    

Adattare la variabile Type e le proprietà alle proprie esigenze. Il documento proxy del vincolo di flusso è simile al seguente:


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

Il modulo contenente il proxy di visualizzazione potrebbe sembrare un po\' più complicato. Ma per ora impostare semplicemente il path dell\'icona. Si tornerà su questo file nei passaggi successivi del tutorial.


```python
class ViewProxy(FemConstraint.ViewProxy):
    def getIcon(self):
        return ":/icons/fem-constraint-flow-velocity.svg"
```

Aggiungere i due nuovi moduli al sistema di built come descritto in [ Estendere il modulo FEM](Extend_FEM_Module/it.md). Individuare l\'elenco corretto cercando i moduli dei vincoli.

Come per tutti gli oggetti dell\'ambiente FEM, il vincolo di velocità deve essere registrato in {{Incode|ObjectsFem.py}}. Il seguente metodo aggiunge un vincolo di velocità al documento attivo. Questo metodo verrà utilizzato dal comando GUI per aggiungere il vincolo. Deve essere inserito da qualche parte in {{Incode|ObjectsFem.py}}.


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



## Creare un comando GUI 

In questo passaggio modificheremo i seguenti file:

-    **src/Mod/Fem/CMakeLists.txt**
    

-    **src/Mod/Fem/App/CMakeLists.txt**
    

-    **src/Mod/Fem/Gui/Workbench.cpp**
    

E aggiungeremo il seguente nuovo file:

-    **src/Mod/Fem/femobjects/constraint_flowvelocity.py**
    

Il comando consente all\'utente di aggiungere effettivamente il vincolo all\'analisi attiva. Basta copiare un comando da un vincolo esistente. I comandi risiedono nel pacchetto {{Incode|femviewprovider}}. Adattare l\'attributo resources e il metodo make chiamato in Activated alle proprie esigenze. Utilizzare anche un ID comando diverso nella chiamata addCommand nella parte inferiore del modulo. La classe seguente è la classe per il comando del vincolo di velocità.


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

Aggiungere il nuovo file di comando al sistema di compilazione come descritto in [ Estendere il modulo FEM](Extend_FEM_Module/it.md). Individuare l\'elenco corretto da cercare per i moduli di comando esistenti.

Inserire il comando in Gui/Workbench.cpp per aggiungerlo alla barra degli strumenti e al menu. Cercare un vincolo esistente della stessa categoria di quello nuovo (ad esempio Flow), copiarlo e incollarlo e modificare l\'ID del comando. Questo dovrebbe essere fatto per due volte. Una volta per il menu e un\'altra per la barra degli strumenti.



## Creare un pannello delle attività 

In questo passaggio modificheremo i seguenti file:

-    **src/Mod/Fem/femviewprovider/view_constraint_flowvelocity.py**
    

In FreeCAD, gli oggetti vincolo traggono grandi vantaggi dai pannelli attività. I pannelli attività possono utilizzare widget di input più potenti che espongono l\'unità dei valori immessi direttamente all\'utente. Il vincolo di velocità richiede anche l\'uso di un pannello delle attività poiché un pannello delle attività è l\'unico modo per specificare la faccia o le facce su cui deve essere applicato il vincolo.

La posizione del modulo in cui sono implementati i pannelli attività non è definita in modo rigoroso. Per il vincolo di velocità, inseriremo semplicemente il pannello delle attività nello stesso modulo in cui inseriamo il proxy di visualizzazione. Il pannello delle attività è piuttosto complicato. Fa uso di FemSolectionWidgets.BoundarySelector(). Si tratta di un widget qt che consente all\'utente di selezionare i confini su cui applicare il vincolo. Oltre a questo widget, ne genera un altro caricando un file UI creato appositamente per il vincolo di velocità. Tramite questo widget è possibile specificare il vettore velocità.

Nella maggior parte dei casi dovrebbe essere sufficiente copiare semplicemente questa classe, utilizzare un file UI adatto (invece di TaskPanelFemFlowVelocity.ui) e regolare \_initParamWidget() e \_applyWidgetChanges(). Se il nuovo vincolo richiede corpi come riferimenti anziché confini, basta sostituire l\'oggetto BoundarySelector con SolidSelector.


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

Il proxy di visualizzazione deve essere esteso per supportare il pannello delle attività appena implementato. Il seguente proxy di visualizzazione estesa apre il pannello delle attività quando l\'utente fa doppio clic sull\'oggetto vincolo nella visualizzazione ad albero.


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



## Estendere il writer di Elmer 

In questo passaggio modificheremo i seguenti file:

-    **src/Mod/Fem/femsolver/elmer/writer.py**
    

Il modulo writer contiene metodi per tutti i tipi di equazioni. A seconda del tipo di vincolo, condizione al contorno, condizione iniziale o forza del corpo è necessario modificare metodi diversi. Per la nostra velocità del flusso dobbiamo impostare {{Incode|_handleFlowBndConditions(...)}}.


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



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > Add FEM Constraint Tutorial/it
