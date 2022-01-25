# Scenegraph/fr
{{TOCright}}

## Introduction

La géométrie qui apparaît dans la [vues 3D](3D_view/fr.md) de FreeCAD est rendue par la bibliothèque [Coin3D](https://en.wikipedia.org/wiki/Coin3D). Coin3D est une implémentation de la norme [OpenInventor](https://en.wikipedia.org/wiki/Open_Inventor). Le logiciel [OpenCASCADE](https://en.wikipedia.org/wiki/Open_Cascade_Technology) fournit également la même fonctionnalité mais il a été décidé au tout début de FreeCAD de ne pas utiliser la visionneuse OpenCASCADE intégrée mais plutôt de basculer vers le logiciel Coin3D plus performant. Un bon moyen de découvrir cette bibliothèque est le livre [Open Inventor Mentor](http://www-evasion.imag.fr/Membres/Francois.Faure/doc/inventorMentor/sgi_html/).

## Description

Actuellement [OpenInventor](https://fr.wikipedia.org/wiki/Inventor_(bibliothèque_logicielle)) est un langage de description de scènes en 3 dimensions. La scène décrite dans OpenInventor est restituée en OpenGL sur votre moniteur. Coin3D prend en charge toutes ces procédures, de telle sorte que le programmeur n\'a pas besoin de traiter les appels complexes d\'OpenGL, il lui suffit simplement de fournir le code OpenInventor adéquat.

L\'un des gros travaux que FreeCAD fait pour vous est de traduire les informations de géométrie d\'OpenCASCADE en langage OpenInventor.

OpenInventor décrit une scène 3D sous la forme d\'une [Graphe de scène](https://fr.wikipedia.org/wiki/Graphe_de_scène) comme le montre l\'exemple ci dessous:

![](images/Scenegraph.gif ) 
*Image prise de [https://web.archive.org/web/20190807185912/http://www-evasion.imag.fr/~Francois.Faure/doc/inventorMentor/sgi_html/ Inventor mentor]*

Un graphe de scène openInventor décrit tout ce qui fait partie d\'une scène 3D, comme la géométrie, les couleurs, les matériaux, les lumières, etc et organise toutes ces données dans une structure pratique et claire. Tout peut être regroupé en sous-structures, ce qui vous permet d\'organiser le contenu de votre scène à peu près comme vous le souhaitez. Voici un exemple de fichier openInventor:


{{Code|lang=bash|code=
#Inventor V2.0 ascii
 
Separator { 
    RotationXYZ {   
       axis Z
       angle 0
    }
    Transform {
       translation 0 0 0.5
    }
    Separator { 
       Material {
          diffuseColor 0.05 0.05 0.05
       }
       Transform {
          rotation 1 0 0 1.5708
          scaleFactor 0.2 0.5 0.2
       }
       Cylinder {
       }
    }
}
}}

Comme vous pouvez le voir, la structure est très simple. Vous utilisez des séparateurs pour organiser vos données en blocs, un peu comme vous organiseriez vos fichiers en dossiers. Chaque instruction affecte ce qui vient ensuite, par exemple les deux premiers éléments de notre séparateur racine sont une rotation et une traduction, les deux affecteront l\'élément suivant, qui est un séparateur. Dans ce séparateur, un matériau est défini et une autre transformation. Notre cylindre sera donc affecté par les deux transformations, celle qui lui est appliquée directement et celle qui a été appliquée à son séparateur parent.

Nous avons également beaucoup d\'autres d\'éléments pour organiser notre scène (projet), tels que des groupes, des commutateurs ou des annotations.
Nous pouvons donner à nos objets des définitions très complexes, des couleurs, des textures des modes d\'ombrage et de transparence. Nous pouvons aussi définir de la lumière, des caméras et, même du mouvement.
Il est aussi possible d\'intégrer des portions de scripts dans des fichiers OpenInventor et de définir des comportements plus complexes.

Si vous souhaitez en savoir plus sur openInventor, rendez-vous directement à sa référence la plus célèbre: [Inventor mentor](http://www-evasion.imag.fr/~Francois.Faure/doc/inventorMentor/sgi_html/).

Normalement, dans FreeCAD, nous n\'avons pas besoin d\'interagir directement avec le scène de graphe OpenInventor. Dans un document FreeCAD, chaque objet maillé, forme Part ou toute autre chose, est automatiquement converti en code OpenInventor et est inséré dans le scène de graphe que vous voyez dans la [vue 3D](3D_view/fr.md). Ce graphe de scène est mis à jour en permanence lorsque vous modifiez, ajoutez ou supprimez des objets.. En fait, chaque objet (dans l\'espace App) dispose d\'un constructeur de vue (un objet correspondant dans l\'espace Gui) responsable de la création du code OpenInventor.

Mais il y a de nombreux avantages à accéder directement au scène de graphe. Par exemple, nous pouvons modifier temporairement l\'apparence d\'un objet ou nous pouvons ajouter des objets à la scène qui n\'ont aucune existence réelle dans le document FreeCAD, tels que la géométrie de construction, les aides, les conseils graphiques ou les outils telles que les manipulations ou les informations à l\'écran .

FreeCAD dispose de plusieurs outils pour voir ou modifier le code OpenInventor.
Par exemple, le code Python suivant, montre la représentation OpenInventor d\'un objet sélectionné:


```python
obj = FreeCAD.ActiveDocument.ActiveObject
viewprovider = obj.ViewObject
print viewprovider.toString()

```

Mais nous avons aussi un module Python qui permet un accès complet à toute chose gérée par Coin3D, comme, notre scène graphique FreeCAD.
Alors, lisez la suite sur la page de [pivy](Pivy/fr.md).

## Exemples de codage 

Voir les [Coin3d snippets](Coin3d_snippets/fr.md) grâce aux recherches de MariwanJ pour l\'[atelier Design456](Design456_Workbench/fr.md). Le dépôt de code de ces exemples se trouve à l\'adresse <https://github.com/MariwanJ/COIN3D_Examples>. {{Top}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Scenegraph/fr
