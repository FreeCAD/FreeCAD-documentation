# TechDraw Templates/fr
{{TOCright}}

## Vue d\'ensemble 

Chaque page TechDraw est basée sur un objet Modèle. Le modèle contrôle la taille du papier et contient des graphiques et du texte fixes, par exemple un cadre de page ou une bordure.

Le modèle peut également contenir des champs de texte modifiables pour des attributs tels que *Titre*, *Sous-titre*, *Auteur*, *Date*, *Échelle*, *Poids*, *Numéro du dessin* et *Feuille*.

Les modèles sont des fichiers [SVG](SVG/fr.md) qui peuvent être créés et modifiés en dehors de FreeCAD, avec une application telle que [Inkscape](https   *//fr.wikipedia.org/wiki/Inkscape).

## Propriétés

-    **Orientation**   * Portrait ou Paysage.

-    **Width**   * Largeur du papier en mm.

-    **Height**   * Hauteur du papier en mm

-    **Page Result**   * Une copie du fichier modèle original incluant toutes les modifications apportées aux textes modifiables. Cela permet aux utilisateurs qui ne possèdent pas une copie du fichier modèle de voir la page comme prévu. Pas typiquement utile pour les utilisateurs finaux.

-    **Template**   * a) Un pointeur vers la copie du fichier modèle original incorporé dans ce fichier \*.FCStd, ou b) un chemin de fichier vers un modèle accessible sur la machine actuelle. Utilisez le bouton de sélection de fichier (\...) pour changer de modèle.

## Sélectionner un autre fichier modèle 

Pour sélectionner un modèle différent pour un dessin    *

1.  Localisez l\'objet Page souhaité dans la [Vue par arborescence](Tree_view/fr.md).
2.  Développez le nœud Page si nécessaire.
3.  Sélectionnez l\'objet Modèle.
4.  Dans l\'[Éditeur de propriétés](Property_editor/fr.md), cliquez dans le champ de propriété **Template**.
5.  Appuyez sur le bouton **...** (point de suspension) qui apparaît.
6.  Un dialogue de fichier ouvre le dossier dans lequel se trouve le modèle en cours. Si la page a été créée dans la session FreeCAD en cours, il s\'agit du dossier de modèle par défaut (tel que défini dans les [TechDraw Préférences](TechDraw_Preferences/fr#Fichiers.md)).
7.  Vous pouvez aussi naviguer vers un autre dossier.
8.  Sélectionnez un autre fichier modèle.
9.  Appuyez sur le bouton **OK**.

Si vous avez modifié un fichier modèle et que vous souhaitez mettre à jour une page créée dans la session FreeCAD en cours qui utilise ce modèle, sélectionnez d\'abord temporairement un fichier différent, puis sélectionnez à nouveau le fichier modifié.

## Modèles personnalisés 

Un nombre limité de modèles pré-formatés dans différentes tailles de page sont inclus avec FreeCAD. Ils se trouvent dans


```python
$INSTALL_DIR/Mod/TechDraw/Templates/
```

Où `$INSTALL_DIR` est le répertoire où FreeCAD a été installé, par exemple


```python
/usr/share/freecad/Mod/TechDraw/Templates/
```

Les modèles personnalisés peuvent également être spécifiés par défaut dans [TechDraw Préférences](TechDraw_Preferences/fr.md).

Voir aussi [Comment créer un modèle TechDraw personnalisé](TechDraw_TemplateHowTo/fr.md)

## Remarques

-   Les modèles TechDraw ne sont pas entièrement interchangeables avec les [Drawing Modèles](Drawing_templates/fr.md). En général, les modèles de Drawing fonctionneront dans TechDraw, mais il peut y avoir des problèmes avec le texte modifiable.

-   Les clauses de transformation Svg **causeront des problèmes** dans les modèles personnalisés. Voir une discussion sur Stackoverflow à l\'adresse [supprimer les clauses de transformation dans les fichiers SVG](https   *//stackoverflow.com/questions/13329125/removing-transforms-in-svg-files).

-   La clause **xml   *space=\"preserve\"** pose parfois des problèmes de taille et de positionnement du texte. Il est préférable d\'éviter/de supprimer cette clause du code SVG de votre modèle personnalisé.

-   Les modèles fonctionnent mieux lorsqu\'ils ne contiennent aucun code SVG superflu (appelé par certains \"SVG garbage\"). Il y a un bon article sur [supprimer les déchets des SVG ici](https   *//freecad-gost.ru/news/gost-templates-techdraw-09-01-2020/). L\'article est en russe.





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Templates/fr
