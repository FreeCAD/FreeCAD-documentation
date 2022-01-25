# Macro Manage Navigational Style2/fr
{{Macro/fr
|Name=Macro Manage Navigational Styles2
|Icon=Macro_Manage_Navigational_Styles2.png
|Description=Cette macro vous permet de modifier le style de navigation Inventor lors de l'utilisation de l'esquisse. <br/> Lors de l'utilisation de l'esquisse, le menu du bouton droit est redéfini pour contenir les options pertinentes pour l'esquisse. Par conséquent, l'option permettant de modifier le style de navigation, qui est disponible en dehors de l'esquisse, n'est pas disponible dans l'esquisse.
|Author=PiffPoof
|Version=1.0
|Date=2015-01-17
|FCVersion=Toutes
|Download=[https://www.freecadweb.org/wiki/images/1/1c/Macro_Manage_Navigational_Styles2.png ToolBar icon]
|SeeAlso=[Macro Manage Navigational Style1](Macro_Manage_Navigational_Style.md)
}}

## Description

Lorsque vous utilisez le Sketcher, le menu du bouton droit de la souris est redéfini pour contenir les options pertinentes relatives au Sketcher. Par conséquent, l\'option de modification du Style de navigation, qui est disponible en dehors du Sketcher, n\'est pas disponible lorsque vous êtes dans le Sketcher.

## Installation

Il existe deux extraits de code, chaque code est une macro distincte. L\'installation consiste à copier les deux mocros dans le répertoire Macro approprié et à les invoquer dans le menu Macro. Il est préférable de les ajouter à la barre d\'outils afin d\'être facilement disponible lors de l\'utilisation du Sketcher.

-   voir [Comment installer des macros](How_to_install_macros/fr.md) pour plus d\'informations sur l\'installation de ce code de macro
-   voir [Personnaliser les barres d\'outils](Customize_Toolbars/fr.md) pour savoir comment installer un bouton sur une barre d\'outils

## Utilisation

Cliquez sur le bouton de la barre d\'outils associée ou appelez-le dans le menu Macro. Il n\'y a aucune confirmation visible de leur exécution, à part que le style de navigation va changer.

## Interface Utilisateur 

Il n\'y a vraiment aucune interface utilisateur, même pas la confirmation que le style de navigation a été modifié. La confirmation sera visible lors de la prochaine manipulation de la vue, les mouvements de votre souris seront interprétés dans le style de navigation que vous aurez sélectionné.

## Scripts

-   icône et macro pour changerle style de navigation \'Inventor\'

![](images/Macro_Manage_Navigational_Styles2.png )

**Macro\_Manage\_Navigational\_Styles2\_Inventor.FCMacro**


{{MacroCode|code=
# change to Inventor Navigational Style
p=App.ParamGet("User parameter:BaseApp/Preferences/View")
p.SetString("NavigationStyle","Gui::InventorNavigationStyle")
}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Manage Navigational Style2/fr
