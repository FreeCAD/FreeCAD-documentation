# Gui Command/fr
{{TOCright}}

La GuiCommand est l\'une des fonctions les plus importantes du point de vue interaction entre l\'utilisateur et FreeCAD. Chaque fois que l\'utilisateur sélectionne un élément du menu ou appuie sur un bouton de la barre d\'outils, il active une GuiCommand. Certains des attributs d\'une GuiCommand sont :

-   Définir un nom
-   Contenir une icône
-   Définir l\'action annuler/rétablir
-   Aller à une page d\'aide
-   Ouvrir et contrôler des boîtes de dialogues
-   Enregistrer une macro
-   et ainsi de suite \...



## Nommage

La GuiCommand est appelée selon un certain standard : *ModuleName_CommandName*, par exemple \"[Base Open](Base_Open/fr.md)\" est la Gui Command Open dans le système Base. Dans certains modules, la GuiCommand a pour préfixe le nom du module, comme par exemple \"[Part_Cylinder](Part_Cylinder.md)\".

Si le document n\'est pas fini, utilisez le bandeau [Template:UnfinishedDocu](Template_UnfinishedDocu.md).



## Pages d\'aide 

Chaque GuiCommand doit avoir une page d\'aide. La page d\'aide est hébergée sur le wiki de documentation FreeCAD. L\'article porte le même nom que la GuiCommand, par exemple [Draft ShapeString](Draft_ShapeString/fr.md).

Pour créer vos propres pages d\'aide vous pouvez utiliser le [modèle GuiCommand](GuiCommand_model/fr.md).

Exemples :

-   [Draft Formes à partir de texte](Draft_ShapeString/fr.md)
-   [Draft Ligne](Draft_Line/fr.md)



## Icônes

<img alt="" src=images/Tango-Palette.png  style="width:400px;">

Chaque GuiCommand doit avoir une icône. Nous utilisons le [jeu d\'icônes Tango](http://tango-project.org/Tango_Desktop_Project), et ses recommandations. Sur le côté droit, vous voyez la palette de couleurs tango.

Il est conseillé de faire toutes les icônes au format [SVG](SVG/fr.md), par exemple avec [Inkscape](http://inkscape.org/?lang=fr&css=css/base.css). Cela rend plus facile l'application des changements et des icônes dérivés dans l\'espace de la même application.



### Code des couleurs des icônes 

<img alt="" src=images/Colorchart.png  style="width:200px;">

Nous essayons autant que possible de respecter ce tableau, la couleur des icônes a donc une signification directe.



---
![](images/Button_right.svg) [documentation index](../README.md) > Gui Command/fr
