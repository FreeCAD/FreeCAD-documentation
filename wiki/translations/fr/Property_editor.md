# Property editor/fr
## Description

L\'[éditeur de propriétés](Property_editor/fr.md) apparaît dans la partie inférieure du panneau **Modèle** (si la [vue combinée](Combo_view/fr.md) est active) ou sous la forme d\'un panneau autonome appelé **Vue des propriétés**.

En règle générale, l\'éditeur de propriétés est destiné à traiter un seul objet à la fois. Les valeurs affichées dans l\'éditeur de propriétés appartiennent à l\'objet sélectionné. Néanmoins, certaines propriétés, comme les couleurs, peuvent être définies pour plusieurs objets sélectionnés. Si aucun élément n\'est sélectionné, l\'éditeur de propriétés est vide.

Toutes les propriétés ne peuvent pas être modifiées, certaines sont en lecture seule.

<img alt="" src=images/FreeCAD_Property_editor_Data.png  style="width:300px;"> 
*Les propriétés de données d'un [Part Cube](Part_Box/fr.md)*



## Types de propriétés 

Une propriété est une information comme un numéro ou une chaîne de texte qui est rattachée à un document Freecad ou à un objet dans le document. De nombreux types de propriétés sont disponibles. Parmi les plus courants :


{{Code|lang=text|code=
App::PropertyAngle
App::PropertyBool
App::PropertyDistance
App::PropertyFloat
App::PropertyInteger
App::PropertyLength
App::PropertyPlacement
App::PropertyString
App::PropertyVector
}}



## Propriétés Vue et Données 

L\'éditeur de propriétés comporte deux onglets donnant accès à deux classes de propriétés :

-   les propriétés **Données**, liées aux paramètres *physiques* de l\'objet. Les propriétés **Données** définissent les caractéristiques essentielles de l\'objet. Elles existent à tout moment, même lorsque FreeCAD est utilisé en mode console, ou en tant que bibliothèque. Cela signifie que si vous chargez un document en mode console, vous pouvez éditer le rayon d\'un cercle ou la longueur d\'une ligne, même si vous ne voyez pas le résultat à l\'écran.
-   Les propriétés **Vue**, liées à l\'aspect *visuel* de l\'objet. Les propriétés **Vue** sont liées au `ViewObject` de l\'objet, et ne sont accessibles que lorsque l\'interface graphique est chargée. Elles ne sont pas accessibles lorsque FreeCAD est utilisé en mode console ou en tant que bibliothèque headless. Par défaut, les modifications apportées aux propriétés de la vue ne sont pas ajoutées à la stack d\'annulation et ne peuvent pas être annulées et refaites avec [Std Annuler](Std_Undo/fr.md) et [Std Rétablir](Std_Redo/fr.md). Mais il est possible de changer cela en réglant le paramètre de [réglage fin](Fine-tuning/fr.md) **AutoTransactionView** à `True`.



## Propriétés de base 

Des objets différents peuvent avoir des propriétés différentes. Cependant, de nombreux objets ont les mêmes propriétés parce qu\'ils sont dérivés de la même classe interne.

La plupart des objets géométriques qui peuvent être créés et affichés dans la [vue 3D](3D_view/fr.md) sont dérivés d\'un `Part::Feature`. Voir [Part Feature](Part_Feature/fr.md) pour connaître les propriétés élémentaires de ces objets.

Pour la géométrie 2D, la plupart des objets sont dérivés de `Part::Part2DObject` (lui-même dérivé de `Part::Feature`) qui est la base des [esquisses](Sketch/fr.md) et de la pluspart des [Draft éléments](Draft_Workbench/fr.md). Voir [Part Part2DObject](Part_Part2DObject/fr.md) pour les propriétés élémentaires de ces objets.



## Menu contextuel 

Pour afficher le menu contextuel de l\'éditeur de propriétés, cliquez avec le bouton droit de la souris sur l\'arrière-plan de l\'éditeur ou sur une propriété.

En cliquant avec le bouton droit de la souris sur l\'arrière-plan, trois options s\'offrent à vous :

-    **Ajouter une propriété**: ajoute une propriété dynamique à l\'objet.

-    **Afficher les propriétés cachées**: si elle est active, les propriétés Données et Vue cachées sont affichées dans l\'éditeur.

-    **Expansion automatique**: si elle est active, tous les nœuds de l\'éditeur sont développés lorsqu\'un objet est sélectionné.

En cliquant avec le bouton droit de la souris sur une propriété, les options supplémentaires suivantes sont disponibles :

-    **Renommer le groupe de propriétés**: renomme le groupe de propriétés sélectionné. Disponible uniquement pour les propriétés dynamiques. Les propriétés dynamiques sont celles ajoutées par l\'utilisateur, ainsi que celles ajoutées par le code Python.

-    **Supprimer la propriété**: supprime les propriétés sélectionnées. Disponible uniquement pour les propriétés dynamiques.

-    **Expression...**: affiche l\'éditeur d\'expressions qui permet d\'utiliser des [expressions](Expressions/fr.md) dans la valeur de la propriété.

-    **État**:

:   Si une valeur d\'état est suivie d\'un astérisque (*****), elle est statique et ne peut être modifiée.

  - **Propriétés cachées** : si elle est active, elle définit la propriété comme étant cachée, ce qui signifie qu\'elle ne sera affichée dans l\'éditeur de propriétés que si **Afficher les propriétés cachées** est active.

  - **Sortie** : si elle est active, elle définit la propriété comme sortie.

  - **Pas de recalcul** : si elle est active, la modification de la propriété ne touche pas son conteneur pour le recalcul.

  - **Lecture seule** : si elle est active, définit la propriété comme étant en lecture seule. La propriété ne sera pas modifiable dans l\'éditeur de propriétés et l\'option **Expression...** n\'est plus disponible. Il peut cependant encore être possible de modifier la propriété par le biais d\'une fenêtre de dialogue.

  - **Transitoire** : si active, définit la propriété comme transitoire. La valeur d\'une propriété transitoire n\'est pas enregistrée dans un fichier. Lors de l\'ouverture d\'un fichier, elle est instanciée avec sa valeur par défaut.

  - **Détecté** : s\'il est actif, l\'objet est détecté et prêt à être recalculé.

  - **Évalué lors de la restauration** : si elle est active, la propriété est évaluée lorsque le document est restauré.

  - **Copie lors du changement** : si elle est active, la propriété est copiée lorsqu\'elle est modifiée dans un lien. La propriété **Link Copy on Change** du lien doit être définie sur {{Value|Tracking}} ou {{Value|Enabled}} pour que cela fonctionne. Ceci est lié aux [liens variants](https://forum.freecad.org/viewtopic.php?p=738833#p738833).



## Script

Voir [Propriétés personnalisées de FeaturePython](FeaturePython_Custom_Properties/fr.md).



## Préférences

Voir [Vue combinée](Combo_view/fr#Préférences.md).





{{Interface_navi

}} {{Std_Base_navi}}



---
⏵ [documentation index](../README.md) > Property editor/fr
