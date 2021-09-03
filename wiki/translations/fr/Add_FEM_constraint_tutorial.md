


{{TutorialInfo/fr
|Topic=Ajouter des contraintes FEM
|Level=
|Time=
|Author=[M42kus](User:M42kus.md)
|FCVersion=
|Files=
}}

Dans ce tutoriel, nous allons ajouter la contrainte de vitesse d\'écoulement à FreeCAD et implémenter le support pour le solveur Elmer. Assurez-vous d\'avoir lu et compris [Module d\'extension FEM](Extend_FEM_Module/fr.md) avant de lire ce tutoriel.

Ce tutoriel explique uniquement comment implémenter des contraintes en Python. Contrairement aux solveurs et aux équations, les contraintes suivent la structure classique du module FEM. C\'est-à-dire que tous les modules d\'une contrainte ont leur place soit dans le paquet {{Incode|femobjects}} ou le paquet {{Incode|femviewprovider}}.

## Résumé

1.  **Créer un objet document:** l\'objet document soumis à l\'analyse et où la contrainte peut être paramétrée et liée.
2.  **Créer une commande graphique:** ajoute une commande à l\'atelier FEM laquelle permet d\'ajouter une contrainte de flux à l\'analyse active.
3.  **Créer un panneau de tâches:** le panneau de tâches est nécessaire pour permettre à l\'utilisateur de définir les limites de la contrainte de vélocité. Cela rend également la saisie des paramètres un peu plus conviviale.
4.  **Extension du fichier writer du solveur Elmer:** ajoute le support pour la nouvelle contrainte au solveur Elmer en développant son exportateur de fichier sif.

## Créer un objet document 

Dans cette étape, nous allons modifier les fichiers suivants:

-    {{FileName|src/Mod/Fem/CMakeLists.txt}}
    

-    {{FileName|src/Mod/Fem/App/CMakeLists.txt}}
    

-    {{FileName|src/Mod/Fem/ObjectsFem.py}}
    

Et ajouter les fichiers suivants:

-    {{FileName|src/Mod/Fem/femobjects/constraint_flowvelocity.py}}
    

-    {{FileName|src/Mod/Fem/femviewprovider/view_constraint_flowvelocity.py}}
    

Un document proxy et une vue proxy sont nécessaires pour la nouvelle contrainte. Ceux-ci sont dans des modules séparés. Le document proxy est dans femobjects et la vue proxy dans femviewprovider. Copiez simplement les modules à partir d\'une contrainte existante, par exemple:

-    {{FileName|femobjects/constraint_selfweight.py}}
    

-    {{FileName|femviewprovider/view_constraint_selfweight.py}}
    

Ajustez la variable Type et les propriétés à vos besoins. Le document proxy de la contrainte de flux a l\'aspect suivant:


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

Le module contenant la vue proxy peut paraître un peu plus compliqué. Mais pour l\'instant, ajustez simplement le chemin de l\'icône. Nous allons revenir à ce fichier dans les prochaines étapes du tutoriel.


```python
class ViewProxy(FemConstraint.ViewProxy):
    def getIcon(self):
        return ":/icons/fem-constraint-flow-velocity.svg"
```

Ajoutez les deux nouveaux modules au système de construction comme décrit dans [Module d\'extension FEM](https://www.freecadweb.org/wiki/Extend_FEM_Module/fr). Localisez la bonne liste en recherchant les modules de contraintes.

Comme tous les objets de l\'espace de travail FEM, la contrainte de vélocité doit être enregistrée dans {{Incode|ObjectsFem.py}}. La méthode suivante ajoute une contrainte de vélocité au document actif. Cette méthode sera utilisée par la commande GUI pour ajouter la contrainte. Elle doit être insérée quelque part dans {{Incode|ObjectsFem.py}}.


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

## Création d\'une commande graphique 

Dans cette étape, nous allons modifier les fichiers suivants:

-    {{FileName|src/Mod/Fem/CMakeLists.txt}}
    

-    {{FileName|src/Mod/Fem/App/CMakeLists.txt}}
    

-    {{FileName|src/Mod/Fem/Gui/Workbench.cpp}}
    

Et ajoutez le nouveau fichier suivant:

-    {{FileName|src/Mod/Fem/femobjects/constraint_flowvelocity.py}}
    

La commande permet à l\'utilisateur d\'ajouter la contrainte à l\'analyse active. Copiez simplement une commande à partir d\'une contrainte existante. Les commandes sont dans le package {{Incode|femviewprovider}}. Ajustez l'attribut des ressources et la méthode de compilation appelée dans Activated selon vos besoins. Utilisez également un ID de commande différent dans l\'appel addCommand au bas du module. La classe suivante est la classe de commande de la contrainte de vélocité.


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

Ajoutez le nouveau fichier de commande au système de build comme décrit dans [Module d\'extension FEM](https://www.freecadweb.org/wiki/Extend_FEM_Module/fr). Recherchez la liste appropriée en recherchant les modules de commande existants.

Placez la commande dans Gui/Workbench.cpp pour l'ajouter à la barre d'outils et au menu. Recherchez une contrainte existante de la même catégorie que la nouvelle (par exemple, Flow), faites copier/coller et ajustez l\'ID de la commande. Cela devrait être fait deux fois, une fois pour le menu et une pour la barre d\'outils.

## Créer un panneau de tâches 

Dans cette étape, nous allons modifier le fichier suivant:

-    {{FileName|src/Mod/Fem/femviewprovider/view_constraint_flowvelocity.py}}
    

Dans FreeCAD, les objets de contrainte bénéficient des panneaux de tâches. Les panneaux de tâches peuvent utiliser des widgets de saisie puissants donnant directement l'unité de valeurs entrées à l'utilisateur. La contrainte de vélocité nécessite l\'utilisation d\'un panneau de tâches. C\'est le seul moyen de spécifier la ou les faces sur lesquels la contrainte doit être appliquée.

L\'emplacement du module dans lequel les panneaux de tâches sont implémentés n\'est pas strictement défini. Pour la contrainte de vitesse, nous allons simplement placer le panneau de tâches dans le même module que la vue proxy. Le panneau de tâches est assez compliqué. Il utilise le FemSolectionWidgets.BoundarySelector(). C\'est un widget QT qui permet à l\'utilisateur de sélectionner les limites sur lesquelles la contrainte doit être appliquée. En plus de ce widget, il en génère un autre en chargeant un fichier d\'interface utilisateur créé spécifiquement pour la contrainte de vélocité. Via ce widget, le vecteur de vitesse peut être spécifié.

La plupart du temps, cela devrait suffire pour copier cette classe. Utilisez un fichier d\'interface utilisateur approprié (au lieu de TaskPanelFemFlowVelocity.ui) et ajustez \_initParamWidget() ainsi que \_applyWidgetChanges(). Si la nouvelle contrainte nécessite des bodies pour référence plutôt que des limites, remplacez simplement l\'objet BoundarySelector par SolidSelector.


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

La vue proxy doit être étendue pour prendre en charge le panneau de tâches que nous venons d\'implémenter. La vue proxy étendue ouvre le panneau de tâches lorsque l\'utilisateur clique deux fois sur l\'objet de contrainte dans la vue arborescente.


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

## Extension du fichier writer du solveur Elmer 

Dans cette étape, nous allons modifier le fichier suivant:

-    {{FileName|src/Mod/Fem/femsolver/elmer/writer.py}}
    

Le module writer contient des méthodes de calcul pour tout type d\'équations. En fonction du type de contraintes, de la condition limite, de la condition initiale ou de la force body, il est nécessaire de modifier ces différentes méthodes. Pour notre vitesse d\'écoulement, nous devons ajuster {{Incode|_handleFlowBndConditions(...)}}.


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

[Category:FEM/fr](Category:FEM/fr.md) [Category:FEM{{\#translation:}}](Category:FEM.md)
