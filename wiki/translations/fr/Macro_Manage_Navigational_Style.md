 {{Macro/fr
|Name=Macro Manage Navigational Styles
|Description=Cette paire de macros vous permet de modifier le style de navigation tout restant le sketcher.
|Author=PiffPoof
|Version=1.0
|Date=2015-01-17
|FCVersion=Toutes
|Download=[https://www.freecadweb.org/wiki/images/9/92/Macro_Manage_Navigational_Styles1.png ToolBar icon]
|SeeAlso=[Macro Manage Navigational Style2](Macro_Manage_Navigational_Style2/fr.md)
}}

## Description

Lorsque vous utilisez le Sketcher, le menu du bouton droit de la souris est redéfini pour contenir les options pertinentes relatives au Sketcher. Par conséquent, l\'option de modification du Style de navigation, qui est disponible en dehors du Sketcher, n\'est pas disponible lorsque vous êtes dans le Sketcher.

## Installation

Il existe deux extraits de code, chaque code est une macro distincte. L\'installation consiste à copier les deux mocros dans le répertoire Macro approprié et à les invoquer dans le menu Macro. Il est préférable de les ajouter à la barre d\'outils afin d\'être facilement disponible lors de l\'utilisation du Sketcher.

-   voir [Comment installer des macros](How_to_install_macros/fr.md) pour plus d\'informations sur l\'installation de ce code de macro
-   voir [Personnaliser les barres d\'outils](Customize_Toolbars/fr.md) pour savoir comment installer un bouton sur une barre d\'outils

## Utilisation

Cliquez sur le bouton de la barre d\'outils associée ou appelez-le dans le menu Macro. Il n\'y a aucune confirmation visible de leur exécution, à part que le style de navigation va changer.

## Interface utilisateur 

Il n\'y a vraiment aucune interface utilisateur, même pas la confirmation que le style de navigation a été modifié. La confirmation sera visible lors de la prochaine manipulation de la vue, les mouvements de votre souris seront interprétés dans le style de navigation que vous aurez sélectionné.

## Scripts

Il existe deux scripts, un pour chacun des styles de navigation \'Cad\' et \'Inventor\'. Il y a aussi 2 icônes, une pour chaque Macro:

-   icône et code de la macro pour changer le style de navigation en «CAD»

![](images/Macro_Manage_Navigational_Styles1.png )

**Macro\_Manage\_Navigational\_Styles1\_CAD.FCMacro**


{{MacroCode|code=
# change to CAD Navigational Style
p=App.ParamGet("User parameter:BaseApp/Preferences/View")
p.SetString("NavigationStyle","Gui::CADNavigationStyle")
}}




