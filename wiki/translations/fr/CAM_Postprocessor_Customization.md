# CAM Postprocessor Customization/fr
}









## Introduction

FreeCAD utilise comme représentation interne pour les trajectoires générées, ce que l\'on appelle des G-codes. Ils peuvent décrire des choses telles que : la vitesse et l\'avance, l\'arrêt du moteur etc\... Mais la chose la plus importante est les mouvements qu\'ils décrivent. Ces mouvements sont assez simples : il peut s\'agir de lignes droites ou d\'arcs de cercle. Des courbes plus sophistiquées comme les B-splines sont déjà approximées par l\'<img alt="" src=images/Workbench_CAM.svg  style="width:24px;"> [atelier CAM](CAM_Workbench/fr.md) de FreeCAD.



## Ce que le post-processeur peut faire pour vous 

De nombreuses fraiseuses utilisent également des G-codes pour contrôler le processus de fraisage. Ils peuvent ressembler presque aux codes internes mais il peut y avoir quelques différences:

-   la machine peut avoir une séquence de démarrage spéciale
-   il peut avoir une séquence d\'arrêt spéciale
-   les arcs peuvent être définis avec un centre relatif ou absolu
-   il peut nécessiter des numéros de ligne dans un certain format
-   il peut utiliser ce que l\'on appelle des cycles fixes pour des sous-processus prédéfinis tels que le forage
-   vous pouvez préférer la sortie de votre G-code en unités métriques ou impériales.
-   il peut être utile d\'effectuer un ensemble de mouvements avant d\'appeler pour un changement d\'outil afin de faciliter l\'action pour l\'opérateur
-   vous souhaiterez peut-être inclure des commentaires pour plus de lisibilité ou les supprimer pour garder le programme petit
-   vous souhaiterez peut-être inclure un en-tête personnalisé pour identifier ou documenter le programme pour référence future.
-   \...

En outre, il existe d\'autres langages pour contrôler une fraiseuse comme le HPGL, le DXF ou d\'autres.

Le postprocesseur est un programme qui traduit les codes internes en un fichier complet qui peut être téléchargé sur votre machine.



## Préparation pour écrire votre propre post-processeur 

Vous pouvez commencer avec un modèle très simple montrant comment votre machine lit les lignes droites et les arcs. Préparez-le avec n\'importe quel programme adapté à votre machine.

Un fichier pour ces chemins commençant à (0,0,0) et allant vers Y serait utile. Assurez-vous que c\'est l\'outil lui-même qui se déplace le long de ce chemin, c\'est-à-dire qu\'aucune compensation de rayon d\'outil ne doit être appliquée.

![](images/Path_PostProcessorSketch.png )

Le chemin dans FreeCAD ressemblerait à ceci. Veuillez noter la petite flèche bleue, elle indique la direction de départ. Pour un tout premier essai, vous ne pouvez fournir qu\'un seul niveau dans le plan XY.

![](images/Path_PostProcessorModel.png )

Vous pouvez ensuite consulter le fichier et le comparer à la sortie des postprocesseurs existants tels que **linux_cnc_post.py** ou **grbl_post.py** et essayez de les adapter vous-même ou de les télécharger sur le [forum Path/CAM](https://forum.freecadweb.org/viewforum.php?f=15) pour obtenir de l\'aide.



## Convention de dénomination 

Le postprocesseur peut être installé dans votre répertoire de macros FreeCAD. Pour un préfixe **<filename>**, le postprocesseur doit avoir le nom **<filename>_post.py**. Veuillez noter que le postfixe et l\'extension, **_post.py**, doivent être en minuscules.

Le nouveau nom doit être repris en tête de la liste des arguments de l\'analyseur syntaxique dans le fichier **<filename>_post.py**, par exemple :


{{Code|lang=text|code=
parser = argparse.ArgumentParser(prog="grbl", add_help=False)
}}

Si vous testez, placez-le dans votre répertoire de macros. S\'il fonctionne bien, veuillez envisager de le fournir pour que d\'autres en profitent (postez-le sur le forum Path/CAM de FreeCAD) afin qu\'il puisse être inclus dans la distribution de FreeCAD à l\'avenir.



## Autres post-processeurs existants 

A titre de comparaison, vous pouvez regarder les post-processeurs qui sont fournis avec votre installation de FreeCAD. Ils sont situés dans le répertoire /Mod/CAM/Path/Post/scripts. Les postprocesseurs [linuxcnc](http://linuxcnc.org/) et [grbl](https://github.com/grbl/grbl) sont très utilisés. L\'étude de leur code peut donner des indications utiles.



## Programmer votre propre post-processeur 

Ce paragraphe traite de certains éléments internes des postprocesseurs linuxcnc. La même structure est également utilisée dans d\'autres postprocesseurs.

En regardant le fichier linux_cnc_post.py, vous verrez la fonction d\'exportation (à partir de la 0.19.20514, elle se trouve à la ligne 156)


```python
def export(objectslist, filename, argstring):
    # pylint: disable=global-statement
    ...
    gcode = ""
    ...
    ...
```

Elle collecte étape par étape dans la variable \"gcode\" les G-codes traités et gère l\'exportation globale des objets post-traités (opérations, outils, travaux, etc\...).
L\'exportation gère les éléments de haut niveau comme les commentaires et le liquide de refroidissement mais tous les objets qui ont plusieurs commandes de CAM (changements d\'outils et opérations) sont délégués à la fonction d\'analyse (à partir du 0.19.20514, elle est à la ligne 288).


```python
def parse(pathobj):
    ...
    out = ""
    lastcommand = None
    ...
    ...
```

De même que la fonction \"export\" collecte les G-codes dans la variable \"out\". Dans la variable \"command\", les commandes telles que vues dans la fonction \"inspect G-code\" de l\'atelier CAM sont stockées et peuvent être examinées pour un traitement ultérieur.


```python
        for c in pathobj.Path.Commands:

            command = c.Name
```

Il reconnaît les différents codes G, M, F, S et autres codes G. En se souvenant de la dernière commande de la variable \"lastcommand\", elle peut supprimer les répétitions ultérieures de commandes modales.

L\'analyse et l\'exportation consistent simplement à formater des chaînes de caractères et à les concaténer ensemble pour obtenir le résultat final.

Vous verrez que les deux fonctions appellent également la fonction \"linenumber()\". Si l\'utilisateur veut des numéros de ligne, la fonction linenumber renvoie la chaîne à coller à l\'endroit approprié, sinon elle renvoie une chaîne vide pour que rien ne soit ajouté.



## En relation 

-   <img alt="" src=images/CAM_Post.svg  style="width:24px;"> [CAM Post-traitement](CAM_Post/fr.md)





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM Postprocessor Customization/fr
