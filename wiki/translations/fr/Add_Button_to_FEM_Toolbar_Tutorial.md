# Add Button to FEM Toolbar Tutorial/fr
{{Page_in_progress}}




{{TutorialInfo
|Topic=FEM
|Level=Avancé
|Time=60 min
|Author=_
|FCVersion=0.19
}}

## Introduction

L\'atelier FEM dispose de barres d\'outils et de menus. Ce tutoriel montre comment ajouter un bouton de test à une barre d\'outils. Il montre également comment ajouter un élément de menu à un menu.

La tâche peut être divisée en quatre parties :

-   **Créer un nouveau fichier d\'icône**.
-   **Enregistrer le nouveau fichier d\'icône**. Modification nécessaire dans 
-   **Créer une nouvelle classe de commande**. Modification nécessaire dans 
-   **Ajout d\'une nouvelle commande à l\'atelier**. Modification nécessaire dans .

## Créer un nouveau fichier d\'icône 

Pour le bouton, nous avons besoin d\'un fichier d\'icône. Vous pouvez utiliser n\'importe lequel de vos outils préférés pour le créer, mais il doit être au format SVG. Nous utiliserons ici le fichier {{FileName|FEM_testButton.svg}} comme exemple.

Il doit être placé dans : `src/Mod/Fem/Gui/Resources/icons/`.

## Enregistrer le nouveau fichier d\'icône 

Le nouveau fichier icône SVG doit être enregistré pour le bouton GUI en l\'insérant dans `src/Mod/Fem/Gui/Resources/Fem.qrc` :


{{code|code=
     <file>icons/FEM_testButton.svg</file>
}}

## Créer une nouvelle classe de commande 

Une nouvelle classe de commande doit être ajoutée au module `src/Mod/Fem/femcommands/commands.py`.

Il suffit de copier/coller une commande existante, puis d\'ajuster l\'icône, le texte du menu et l\'info-bulle dans `__init__(self)` :


{{code|code=
class _testButton(CommandManager):
    "The FEM_testButton command definition"

    def __init__(self):
        super(_testButton, self).__init__()
        self.menuetext = "test Button"
        self.tooltip = "This is a test button"
        self.is_active = "always"
        #self.do_activated = "add_obj_on_gui_selobj_noset_edit"
}}

N\'oubliez pas d\'enregistrer la commande au bas du fichier du module avec la méthode `addCommand(...)` :


{{code|code=
FreeCADGui.addCommand(
    "FEM_testButton",
    _testButton()
)
}}

**Remarque** : veuillez consulter ce [fil de discussion](https://forum.freecadweb.org/viewtopic.php?f=18&t=46693&start=10#p402004) dans le forum si des icônes sont impliquées.

## Ajouter une nouvelle commande à l\'atelier 

Nous allons ajouter la nouvelle commande à la fois à la barre d\'outils *solve* et au menu *solve*.

Recherchez le bout de code suivant dans `/Gui/Workbench.cpp` et ajoutez la nouvelle commande :


{{code|code= 
     Gui::ToolBarItem* solve = new Gui::ToolBarItem(root);
     solve->setCommand("Solve");
     *solve << "FEM_SolverCalculixCxxtools"
            << "FEM_SolverCalculiX"
            << "FEM_SolverElmer"
+           << "FEM_testButton"
            << "Separator"
}}

Pour ajouter la commande au menu **solve** de l\'atelier FEM, recherchez le bout de code suivant dans `Workbench.cpp` :


{{code|code= 
    Gui::MenuItem* solve = new Gui::MenuItem;
    root->insertItem(item, solve);
    solve->setCommand("&Solve");
    *solve << "FEM_SolverCalculixCxxtools"
           << "FEM_SolverCalculiX"
           << "FEM_SolverElmer"
           << "FEM_SolverZ88"
+          << "FEM_testButton"
           << "Separator"
}}

**Résultat** : vous devriez avoir ajouté avec succès un bouton de test à la barre d\'outils et au menu d\'un atelier FEM. Maintenant, vous pouvez [compiler FreeCAD](Compiling/fr.md) et tester votre nouveau bouton.

## En relation 

-   [Tutoriel FEM Module d\'extension](Extend_FEM_Module/fr.md)
-   [Page pour développeurs FEM](Onboarding_FEM_Devs/fr.md)

_ _

---
[documentation index](../README.md) > [FEM](Category_FEM.md) > Add Button to FEM Toolbar Tutorial/fr
