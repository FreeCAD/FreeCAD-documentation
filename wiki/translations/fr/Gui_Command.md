# Gui Command/fr
 Une GuiCommand, est l\'une des fonctions les plus importantes du point de vue interaction entre l\'utilisateur et FreeCAD. Chaque fois que l\'utilisateur sélectionne un élément du menu, ou appuie sur un **bouton** de la barre d\'outils, il active une GuiCommand. Voici quelques-uns des attributs d\'une GuiCommand :

-   Définir un nom
-   Contenir une icône
-   Définir l\'action annuler/rétablir
-   Aller à une page d\'aide
-   Ouvrir et contrôler des boîtes de dialogues
-   Enregistrement de macros
-   et ainsi de suite \...

## Nommage

La GuiCommand est appelée selon un certain standard : *ModuleName\_CommandName*, par exemple [Base Open](Base_Open/fr.md) est la Gui Command Open dans le système Base. Dans certains modules, la GuiCommand a pour préfixe le nom du module, comme par exemple [Part Cylinder](Part_Cylinder/fr.md).

Si le document n\'est pas fini, utilisez le bandeau [Template:UnfinishedDocu](Template:UnfinishedDocu/fr.md)

## Pages d\'aide 

Chaque GuiCommand doit avoir une page d\'aide. La page d\'aide est hébergée sur le wiki de documentation FreeCAD. L\'article porte le même nom que la GuiCommand, par exemple [Draft ShapeString](Draft_ShapeString/fr.md).

Pour créer vos propres pages d\'aide vous pouvez utiliser le [modèle GuiCommand](GuiCommand_model/fr.md)

Exemples :

-   [Draft ShapeString](Draft_ShapeString/fr.md)
-   [Draft Line](Draft_Line/fr.md)

### Icônes

<img alt="" src=images/Tango-Palette.png  style="width:400px;">

Chaque GuiCommand doit avoir une icône. Nous utilisons le [jeu d\'icônes Tango](http://tango-project.org/Tango_Desktop_Project), et ses recommandations. Sur le côté droit, vous voyez la palette de couleurs tango.

Il est conseillé de faire toutes les icônes en format [SVG](SVG/fr.md), par exemple avec [Inkscape](http://inkscape.org/?lang=fr&css=css/base.css). Cela rend plus facile l'application des changements et des icônes dérivés dans l\'espace de la même application.

### Code des couleurs des icônes 

<img alt="" src=images/Colorchart.png  style="width:200px;">

Nous essayons autant que possible de respecter ce tableau, de sorte que la couleur des icônes soit dans la même ligne.

## Exigences de qualité 


**L'[atelier Complete](Complete_Workbench/fr.md) est obsolète, il ne contient plus chacune des commandes de FreeCAD.**

Il y a beaucoup de fonctions GuiCommands (outils) dans FreeCAD, qui sont expérimentales ou utilisées à des fins de test ou pour des nouveautés. Ces GuiCommands sont pour la plupart dans les ateliers dédiés comme [Part](Part_Workbench/fr.md), [Mesh](Mesh_Workbench/fr.md) ou Cam. Pour assurer à l\'utilisateur une utilisation facile, l\'atelier *Complete* a été créé. Cet atelier intègre toutes les commandes Gui qui répondent à certaines exigences de qualité décrites ci-après :

-   La commande ou la fonctionnalité doit être \"terminée\", c\'est-à-dire ne pas être un travail en cours.
-   Il doit définir une icône et une position de menu appropriées.
-   Il doit avoir une page d'aide, comme [Draft ShapeString](Draft_ShapeString/fr.md).
    -   Tous les champs du [Template:GuiCommand](Template:GuiCommand/fr.md) doivent être remplis
    -   Il devrait avoir une description détaillée de la commande et de tous ses paramètres et personnalisations.
    -   Il devrait avoir une image des dialogues que la commande va produire.
    -   Il devrait y avoir une description des interfaces et des classes [Python](Python/fr.md) associées avec un exemple de code.

Espérons que cela devienne vrai pour toutes les GuiCommands de la [liste des commandes](List_of_Commands/fr.md).


{{Powerdocnavi

}} 
