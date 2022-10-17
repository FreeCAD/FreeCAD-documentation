# Macro Megaminx/fr
{{Macro/fr
|Name=Macro_Megaminx
|Name/fr=Macro_Megaminx
|Icon=Macro_Megaminx.png
|Description=Cette macro crée un [https   *//fr.wikipedia.org/wiki/Megaminx Megaminx] virtuel.
|Author=aleph0
|SeeAlso=[Macro Rubik Cube](Macro_Rubik_Cube/fr.md)
|Date=2019-02-17
|FCVersion=0.18 et plus
|Download=[https   *//www.freecadweb.org/wiki/images/4/43/Macro_Megaminx.png Icône de la barre d'outils]
}}

## Description

Cette macro crée un document FreeCAD contenant un [Megaminx](https   *//fr.wikipedia.org/wiki/Megaminx) virtuel et vous permet de manipulez-le. Il affiche six vues du Megaminx, y compris chacune des douze faces au moins une fois. Il y a différentes flèches (chaque avec une infobulle qui sera affichée aussi longtemps que vous survolez la souris dessus). En cliquant sur les flèches, vous pouvez faire pivoter les faces du Megaminx, faites pivoter l'ensemble du Megaminx ou faites pivoter ou reflétez l'historique qu'il maintient des rotations que vous avez faites jusqu'à présent. Là est également un menu Megaminx qui est affiché à droite de la barre de menus tant que vous avez au moins un document Megaminx ouvert. Du menu, vous pouvez afficher un texte d'aide, réinitialiser le Megaminx à son initial (résolu), annulez la dernière rotation (et retirez-la de l'historique), copiez l'historique dans le presse-papiers, parcourez les l\'historique, randomiser le Megaminx, et activer ou désactiver l\'écho de rotations à la vue de rapport. Toutes ces fonctions peuvent également être invoqué en tapant des commandes appropriées dans la fenêtre de la console Python.

Un historique sauvegardé dans le presse-papier peut être collé dans la fenêtre de la console Python ou copié dans un fichier qui peut être appelé dans une macro et effectué dans le document Megaminx actif. Vous pouvez avoir plus d\'un document Megaminx ouvert à la fois, même si un seul peut être actif.

## Script

Icône de la barre d\'outils <img alt="" src=images/Macro_Megaminx.png  style="width   *64px;">


{{Codeextralink|https   *//raw.githubusercontent.com/rparkins999/Megaminx/master/Megaminx.FCMacro}}

**Macro_Megaminx.FCMacro**

![](images/Macro_Megaminx.png )




## Utilisation

Téléchargez le code de <https   *//github.com/rparkins999/Megaminx> dans votre macro annuaire. Exécutez la macro pour créer un document Megaminx. Ensuite, vous pouvez jouer avec. Les fonctions d\'historique peuvent être utilisées construire et sauvegarder des opérateurs (alias algorithmes) qui effectuent des transformations utiles sur le Megaminx. Un ensemble approprié de ceux-ci vous donnera une solution complète. Le step_history Cette fonction peut être utilisée pour vous aider à reproduire un opérateur sur un vrai Megaminx.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Megaminx/fr
