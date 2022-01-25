# TechDraw Templates/fr
{{TOCright}}

## Vue d\'ensemble 

Chaque page TechDraw est basée sur un objet Modèle. Le modèle contrôle la taille du papier et contient des graphiques et du texte fixes, par exemple un cadre de page ou une bordure.

Le modèle peut également contenir des champs de texte modifiables pour des attributs tels que *Titre*, *Sous-titre*, *Auteur*, *Date*, *Échelle*, *Poids*, *Numéro du dessin* et *Feuille*.

Les modèles sont des fichiers [SVG](SVG.md) qui peuvent être créés et modifiés en dehors de FreeCAD, avec une application telle que [Inkscape](https://en.wikipedia.org/wiki/Inkscape).

## Propriétés

-    {{PropertyData/fr|Orientation}}: Portrait ou Paysage.

-    {{PropertyData/fr|Width}}: Largeur du papier en mm.

-    {{PropertyData/fr|Height}}: Hauteur du papier en mm

-    {{PropertyData/fr|Page Result}}: Une copie du fichier modèle original incluant toutes les modifications apportées aux textes modifiables. Cela permet aux utilisateurs qui ne possèdent pas une copie du fichier modèle de voir la page comme prévu. Pas typiquement utile pour les utilisateurs finaux.

-    {{PropertyData/fr|Template}}: a) Un pointeur vers la copie du fichier modèle original incorporé dans ce fichier \*.FCSTD, ou b) un chemin de fichier vers un modèle accessible sur la machine actuelle. Utilisez le bouton de sélection de fichier (\...) pour changer de modèle.

## Modification du fichier de modèle 

Pour modifier le gabarit d\'un dessin

1.  cliquez sur la page souhaitée dans l\'arborescence
2.  s\'il n\'est pas déjà ouvert, l\'arbre doit ouvrir un petit sous-arbre avec plusieurs feuilles
3.  sélectionnez la feuille modèle
4.  dans le panneau de propriétés/onglet Données/Modèle est le chemin d\'accès au fichier modèle. Pour changer de fichier, appuyez sur le bouton points de suspension (\'\...\'). Cela ouvrira votre dossier de modèles par défaut (tel que défini dans Préférences/TechDraw).
5.  sélectionnez un autre fichier modèle.

Le nouveau fichier sera ouvert directement.

Lorsque vous souhaitez mettre à jour un fichier de modèle modifié, notez que vous devez charger un autre fichier avant de pouvoir sélectionner à nouveau le même fichier. En effet, la sélection du même fichier est ignorée.

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

## Notes

-   Les modèles TechDraw ne sont pas entièrement interchangeables avec les [Drawing Modèles](Drawing_templates/fr.md). En général, les modèles de Drawing fonctionneront dans TechDraw, mais il peut y avoir des problèmes avec le texte modifiable.

-   Les clauses de transformation Svg **causeront des problèmes** dans les modèles personnalisés. Voir une discussion sur Stackoverflow à l\'adresse [en supprimant les clauses de transformation dans les fichiers SVG](https://stackoverflow.com/questions/13329125/removing-transforms-in-svg-files).

-   La clause **xml:space=\"preserve\"** pose parfois des problèmes de taille et de positionnement du texte. Il est préférable d\'éviter/de supprimer cette clause du code SVG de votre modèle personnalisé.

-   Les modèles fonctionnent mieux lorsqu\'ils ne contiennent aucun code SVG superflu (appelé par certains \"SVG garbage\"). Il y a un bon article sur [removing garbage from SVG here](https://freecad-gost.ru/news/gost-templates-techdraw-09-01-2020/). L\'article est en russe.





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Templates/fr
