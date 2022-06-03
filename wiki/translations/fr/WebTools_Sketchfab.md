---
- GuiCommand   */fr
   Name   *WebTools Sketchfab
   Name/fr   *WebTools Sketchfab
   MenuLocation   *Web Tools → Sketchfab
|
   Workbenches   *[WebTools](WebTools_Workbench/fr.md)
   Shortcut   *
   SeeAlso   *
---

# WebTools Sketchfab/fr

## Description

Cet outil permet l\'exportation et le téléchargement d\'objets vers votre compte [SketchFab](http   *//www.sketchfab.com). {{Version/fr|0.17}}

![](images/Sketchfab_exporter.jpg )

## Utilisation

1.  Enregistrez-vous un compte sur [SketchFab](http   *//www.sketchfab.com) si vous n\'en avez pas déjà un. Les comptes gratuits sont suffisants, les comptes payants ajoutent plus de fonctionnalités, comme la possibilité de rendre des modèles privés, ainsi que d\'avoir des tailles de téléchargement maximales plus importantes.
2.  Préparez un modèle que vous voulez télécharger.
3.  Cliquez sur <img alt="" src=images/WebTools_Sketchfab.svg  style="width   *32px;"> depuis la barre de menu de l\'[atelier WebTools](WebTools_Workbench/fr.md)
4.  Remplissez les champs. Les champs *Name* (nom) et *Clé API Sketchfab* sont obligatoires.
5.  Cliquez sur le bouton \"Upload\".

## Options

-   Vous avez besoin d\'une clé API Sketchfab pour que cet exportateur puisse se connecter à votre compte sketchfab. En appuyant sur le bouton \"Obtenir\", vous serez dirigé vers votre page de paramètres Sketchfab, où cette clé d\'API (unique pour votre compte) est donnée. Copiez la clé et collez-la dans le champ \"Clé API\" de l\'exportateur. Cette valeur sera stockée par FreeCAD, vous n\'avez donc qu\'à le faire une fois.
-   Le champ du nom est obligatoire, les autres peuvent rester vides.
-   L\'exportateur propose plusieurs formats d\'exportation différents. Le meilleur pour vous dépend du type de modèle et du résultat que vous souhaitez obtenir, il est recommandé de tester ce qui vous convient le mieux. En règle générale, OBJ + MTL vous donnera un meilleur contrôle des matériaux, tandis qu\'IV (OpenInventor) donnera un résultat plus proche de ce que vous voyez dans la vue 3D de FreeCAD.
-   Une fois votre modèle chargé, Sketchfab offre une interface assez avancée permettant de configurer davantage les matériaux, l'éclairage et l'environnement.
-   Lorsque vous appuyez sur le bouton \"Télécharger\", une fois le téléchargement terminé, si tout s\'est bien passé, le bouton se transforme en bouton \"Afficher votre modèle en ligne\". Ce bouton vous permet d\'accéder directement à la page du modèle de Sketchfab.
-   Certains formats, comme OBJ, sont interprétés différemment par Sketchfab et FreeCAD. FreeCAD considère que l\'axe Z est dirigé vers le haut, tandis que Sketchfab considère qu\'il pointe vers la personne derrière l\'écran. Pour remédier à cela, une fois le téléchargement terminé, l\'exportateur utilisera l\'API Sketchfab pour faire pivoter le modèle à sa position correcte. Si cette opération échoue, vous en serez averti, mais votre modèle sera toujours correctement téléchargé. Vous pouvez le faire pivoter manuellement dans l\'interface Sketchfab en appuyant sur la flèche à droite de l\'axe \"X\" dans l\'onglet d\'orientation du modèle.



---
![](images/Right_arrow.png) [documentation index](../README.md) > WebTools Sketchfab/fr
