---
 TutorialInfo:l
   Topic:  Dodawanie cech analiz MES
   Level: 
   Time: 
   Author: User:M42kus
   FCVersion: 
   Files: 
---

# Add FEM Constraint Tutorial/pl







## Wprowadzenie

W tym poradniku dodamy warunek brzegowy prędkości przepływu do FreeCAD i zaimplementujemy wsparcie dla solvera Elmer. Upewnij się, że przeczytałeś i zrozumiałeś stronę [Rozszerzenie modułu MES](Extend_FEM_Module/pl.md) przed przejściem do tego poradnika.

Ten poradnik omawia tylko implementację cech analizy w Python. W przeciwieństwie do solvera i równań, cechy analizy są zgodne z klasyczną strukturą środowiska pracy MES. Oznacza to, że wszystkie moduły cechy analizy mają swoje miejsce w paczce {{Incode|femobjects}} lub {{Incode|femviewprovider}}.



## Podsumowanie

1.  **Utwórz obiekt dokumentu:** Obiekt dokumentu, który znajduje się wewnątrz analizy i poprzez który cecha analizy może być sparametryzowana i zadana na brzegach.
2.  **Utwórz polecenie w GUI:** Dodaj do środowiska pracy MES polecenie, które wstawia warunek brzegowy przepływu do aktywnej analizy.
3.  **Utwórz panel zadań:** Panel zadań jest konieczny aby umożliwić użytkownikowi ustawianie brzegów, na których warunek brzegowy ma być zadany. Ułatwia również nieco wprowadzanie parametrów.
4.  **Rozszerz kod zapisujący pliki dla solvera Elmer:** Dodaj wsparcie dla nowej cechy analizy do Elmera poprzez rozszerzenie jego eksportera plików sif.



## Utwórz obiekt dokumentu 

W tym kroku zmodyfikujemy następujące pliki:

-    **src/Mod/Fem/CMakeLists.txt**
    

-    **src/Mod/Fem/App/CMakeLists.txt**
    

-    **src/Mod/Fem/ObjectsFem.py**
    

I dodamy te pliki:

-    **src/Mod/Fem/femobjects/constraint_flowvelocity.py**
    

-    **src/Mod/Fem/femviewprovider/view_constraint_flowvelocity.py**
    

Proxy dokumentu i proxy widoku są wymagane dla nowej cechy analizy. Znajdują się one w osobnych modułach. Proxy dokumentu jest w femobjects a proxy widoku w femviewprovider. Po prostu skopiuj moduły z istniejącej cechy analizy, np.:

-    **femobjects/constraint_selfweight.py**
    

-    **femviewprovider/view_constraint_selfweight.py**
    

Popraw zmienną Type i właściwości tak jak potrzebujesz. Proxy dokumentu warunku brzegowego przepływu wygląda następująco:


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

Moduł zawierający proxy widoku może wydawać się nieco bardziej skomplikowany. Ale póki co po prostu dodaj ścieżkę ikony. Wrócimy do tego pliku w dalszych krokach poradnika.


```python
class ViewProxy(FemConstraint.ViewProxy):
    def getIcon(self):
        return ":/icons/fem-constraint-flow-velocity.svg"
```

Dodaj dwa nowe moduły do systemu budowania, tak jak to opisano na stronie [Rozszerzenie modułu MES](https://www.freecadweb.org/wiki/Extend_FEM_Module/pl). Zlokalizuj poprawną listę poprzez poszukanie modułów cech analizy.

Jak wszystkie obiekty środowiska pracy MES, warunek brzegowy prędkości musi być zarejestrowany {{Incode|ObjectsFem.py}}. Następująca metoda dodaje ten warunek brzegowy do aktywnego dokumentu. Ta metoda będzie używana przez polecenie w GUI do dodawania warunku brzegowego. Musi być wprowadzona gdzieś w {{Incode|ObjectsFem.py}}.


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



## Utwórz polecenie w GUI 

W tym kroku zmodyfikujemy następujące pliki:

-    **src/Mod/Fem/CMakeLists.txt**
    

-    **src/Mod/Fem/App/CMakeLists.txt**
    

-    **src/Mod/Fem/Gui/Workbench.cpp**
    

I dodamy ten nowy plik:

-    **src/Mod/Fem/femobjects/constraint_flowvelocity.py**
    

To polecenie pozwala użytkownikowi faktycznie dodać cechę do aktywnej analizy. Po prostu skopiuj polecenie z istniejącej cechy. Polecenia są w paczce {{Incode|femviewprovider}}. Dostosuj cechy resources i make method wywoływane w Activated do swoich potrzeb. Użyj też innego id polecenia w addCommand call na dole modułu. Następująca klasa jest klasą polecenia warunku brzegowego prędkości przepływu.


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

Dodaj plik nowego polecenia do systemu budowania zgodnie z opisem na stronie [Rozszerzenie modułu MES](https://www.freecadweb.org/wiki/Extend_FEM_Module/pl). Zlokalizuj poprawną listę poprzez poszukanie modułów istniejących poleceń.

Umieść polecenie w Gui/Workbench.cpp aby dodać je do paska narzędzi i menu. Poszukaj istniejących cech analizy tej samej kategorii jak nowa (np. Przepływ), skopiuj i wklej a następnie dostosuj id polecenia. Należy to zrobić dwukrotnie. Raz dla menu i raz dla paska narzędzi.



## Utwórz pasek zadań 

W tym kroku zmodyfikujemy następujący plik:

-    **src/Mod/Fem/femviewprovider/view_constraint_flowvelocity.py**
    

Obiekty cech analizy we FreeCAD zyskują znacznie na panelach zadań. Panele te mogą korzystać z lepszych widgetów danych wejściowych, które eksponują jednostkę wprowadzanych wartości. Warunek brzegowy prędkości przepływu nawet wymaga użycia panelu zadań, ponieważ jest to jedyny sposób wskazania ścian, na które warunek ma być nałożony.

Lokalizacja modułu, w którym zaimplementowane są panele zadań nie jest jednoznaczna. Dla warunku brzegowego prędkości przepływu po prostu umieścimy panel zadań w tym samym module co proxy widoku. Panel zadań jest dosyć złożony. Korzysta z FemSolectionWidgets.BoundarySelector(). To widget qt, który pozwala użytkownikowi wybrać brzegi, na które cecha analizy ma być nałożona. Oprócz tego widgetu, generuje też inny poprzez załadowanie pliku ui specjalnie utworzonego dla warunku brzegowego prędkości przepływu. Ten widget pozwala określić wektor prędkości przepływu.

W większości przypadków powinno wystarczyć po prostu skopiowanie tej klasy, użycie odpowiedniego pliku ui (zamiast TaskPanelFemFlowVelocity.ui) i dostosowanie \_initParamWidget() oraz \_applyWidgetChanges(). Jeśli nowa cecha analizy wymaga brył zamiast brzegów jako odniesień to po prostu zamień obiekt BoundarySelector na SolidSelector.


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

Proxy widoku musi być rozszerzone aby wspierać panel zadań, który właśnie zaimplementowaliśmy. Następujące rozszerzone proxy widoku otwiera panel zadań gdy użytkownik kliknie dwukrotnie na obiekcie cechy analizy w widoku drzewa.


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



## Rozszerz kod zapisujący pliki dla solvera Elmer 

W tym kroku zmodyfikujemy następujący plik:

-    **src/Mod/Fem/femsolver/elmer/writer.py**
    

Moduł zapisujący zawiera metody dla wszystkich typów równań. W zależności od typu cechy analizy, należy zmodyfikować inne metody. Dla naszej prędkości przepływu musimy zmienić {{Incode|_handleFlowBndConditions(...)}}.


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
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > Add FEM Constraint Tutorial/pl
