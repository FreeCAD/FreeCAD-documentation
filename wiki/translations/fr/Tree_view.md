# Tree view/fr
{{TOCright}}

## Introduction

La [vue en arborescence](Tree_view/fr.md) apparaît dans l\'onglet **Modèle** de la [vue combinée](Combo_view/fr.md), l\'un des panneaux les plus importants de l\'[interface](Interface/fr.md). Elle montre tous les objets définis par l\'utilisateur qui font partie d\'un document FreeCAD. L\'arborescence est une représentation de la [structure d\'un document](Document_structure/fr.md) et indique quelles informations sont enregistrées sur le disque.

Ces objets ne doivent pas nécessairement être des formes géométriques visibles dans la [Vue 3D](3D_view/fr.md) mais peuvent également prendre en charge des objets de données créés avec l\'un des [ateliers](Workbenches/fr.md).

![](images/FreeCAD_Tree_view.png )



*La vue en arborescence montrant divers éléments du document.*



## Travailler avec la vue en arborescence 

Par défaut, chaque fois qu\'un nouvel objet est créé, il est ajouté à la fin de la liste dans l\'arborescence. L\'arborescence permet de gérer les objets pour les garder organisés. Elle permet de créer des [groupes](Std_Group/fr.md), de déplacer des objets à l\'intérieur de groupes, de déplacer des groupes à l\'intérieur d\'autres groupes, de renommer des objets, de copier des objets, de supprimer des objets et d\'autres opérations dans le menu contextuel (clic droit) qui dépendent de l\'objet actuellement sélectionné et du plan de travail actuellement actif.

De nombreuses opérations créent des objets qui dépendent d\'un objet déjà existant. Dans ce cas, l\'arborescence montre cette relation en absorbant l\'objet plus ancien à l\'intérieur du nouvel objet. Le développement et la réduction des objets dans l\'arborescence montrent l\'historique paramétrique de cet objet. Les objets qui sont plus profondément à l\'intérieur des autres sont plus anciens, tandis que les objets qui sont à l\'extérieur sont plus récents et sont dérivés des objets plus anciens. En modifiant les objets intérieurs, les opérations paramétriques se propagent jusqu\'au sommet, générant un nouveau résultat.

<img alt="" src=images/FreeCAD_Tree_view_parametric_history_1.png  style="width:" height="304px;"> <img alt="" src=images/FreeCAD_Tree_view_parametric_history_2.png  style="width:" height="304px;">

<img alt="" src=images/FreeCAD_Tree_view_parametric_history_3.png  style="width:" height="304px;">



*L'objet au sommet est créé en effectuant des opérations paramétriques sur des objets qui ont eux-mêmes été créés par des opérations précédentes. L'élargissement de l'arbre à plusieurs niveaux révèle les éléments originaux qui ont été utilisés pour créer les solides partiels.*

## Actions

Étant donné que l\'arborescence répertorie les objets pouvant être visibles dans la [vue 3D](3D_view/fr.md), de nombreuses actions sont identiques comme celles qui peuvent être exécutées à partir de la [vue 3D](3D_view/fr.md).

Lorsque l\'application démarre, l\'[atelier Start](Start_Workbench/fr.md) par défaut est actif et aucun document n\'a été créé, un clic droit sur la [vue en arborescence](Tree_view/fr.md) affiche un sous-menu avec quatre commandes :

-    **Actions sur les expressions**:

    -   [Copier la sélection](Std_Expressions/fr.md)
    -   [Copier le document actif](Std_Expressions/fr.md)
    -   [Copier tous les documents](Std_Expressions/fr.md)
    -   [Coller](Std_Paste/fr.md)

Elles permettent de travailler avec divers documents, mais sont désactivées si aucun document n\'est présent.

Une fois un nouveau document créé, les éléments suivants deviennent actifs :

-    **Actions sur les expressions**:

    -   [Copier le document actif](Std_Expressions/fr.md)
    -   [Copier tous les documents](Std_Expressions/fr.md)

De plus, les actions [Liens](Std_LinkMake/fr.md) sont disponibles.

-    **Actions sur les liens**:

    -   
        **Créer un groupe de liens**
        
        :

        -   [Groupe simple](Std_LinkMakeGroup/fr.md)
        -   [Groupe avec des liens](Std_LinkMakeGroup/fr.md)
        -   [Groupe avec des liens transformés](Std_LinkMakeGroup/fr.md)

    -   [Créer un lien](Std_LinkMake/fr.md)



### Sélection du document 

Si vous sélectionnez le document actif et cliquez avec le bouton droit, en plus de **Actions sur les expressions** et **Actions de liens**, les commandes suivantes apparaissent :

-    **Montrer les objets cachés**: si elle est active, l\'arborescence affichera les éléments masqués.

-    **Rechercher...**: affiche un champ de saisie pour rechercher des objets à l\'intérieur du document sélectionné.

-    **Fermer le document**: ferme le document sélectionné.

-    **Abandonner le recalcul**: si actif, les objets du document ne seront pas [recalculés](Std_Refresh/fr.md) automatiquement.

    -   
        **Permettre un recalcul partiel**
        
        : si actif, le document n\'autorisera le [recalcul](Std_Refresh/fr.md) que pour certains objets.

-    **Marquer pour recalculer**: marque tous les objets du document comme touchés et prêts pour [recalcul](Std_Refresh/fr.md).

-    **[Créer un groupe...](Std_Group/fr.md)**: crée un [groupe](Std_Group/fr.md) dans le document sélectionné.



### Sélection d\'objets 

Une fois que les objets ont été ajoutés au document, un clic droit sur ceux-ci fait apparaître des commandes supplémentaires. Celles-ci dépendent du nombre d\'objets sélectionnés, de leur type et également du plan de travail actif. Dans la plupart des cas et avec la plupart des ateliers (sauf l\'[atelier Start](Start_Workbench/fr.md)), les commandes suivantes sont alors disponibles :

-    **[Apparence](Std_SetAppearance/fr.md)**: lance une boîte de dialogue permettant de modifier les propriétés visuelles de l\'objet entier.

-    **[Couleur aléatoire](Std_RandomColor/fr.md)**: attribue une couleur aléatoire à l\'objet.

-    **[Couper](Std_Cut/fr.md)**: désactivé.

-    **[Copier](Std_Copy/fr.md)**: copie un objet en mémoire.

-    **[Coller](Std_Paste/fr.md)**: colle l\'objet copié dans le document ; la copie est ajoutée à la fin de l\'arborescence.

-    **[Supprimer](Std_Delete/fr.md)**: supprime l\'objet du document.

-    **[Cacher l'élément](#Symbole_de_l'oeil.md)**: si cette case est cochée, l\'objet sera masqué dans l\'arborescence.

-    **Ajouter des objets dépendants à la sélection**: tous les objets dépendants seront ajoutés à la sélection. De cette façon, vous pouvez voir les dépendances et, par exemple, supprimer tous les objets dépendants en une seule fois. {{Version/fr|0.20}}

-    **Marquer pour recalculer**: marque l\'objet sélectionné comme pris en compte, et prêt pour le [recalcul](Std_Refresh/fr.md).

-    **Recalculer l'objet**: recalcule l\'objet sélectionné.

-    **Renommer**: lance l\'édition de l\'étiquette de l\'objet sélectionné, et non du nom qui est en lecture seule. Cette option n\'est disponible que si un seul objet est sélectionné.

Comme exemple d\'extension du menu contextuel, si un [Part Cube](Part_Box/fr.md) est cliqué du bouton droit de la souris alors que l\'[atelier Part](Part_Workbench/fr.md) est actif, les commandes supplémentaires suivantes sont disponibles :

-    **[Modifier](Std_Edit/fr.md)**: active le mode d\'édition de l\'objet.

-    **[Transformer](Std_TransformManip/fr.md)**: lance le widget de transformation pour déplacer ou faire tourner l\'objet.

-    **[Editeur de pièces jointes](Part_EditAttachment/fr.md)**: lance une boîte de dialogue pour attacher l\'objet à un ou plusieurs autres objets.

-    **[Définir les couleurs...](Part_FaceColors/fr.md)**: définit la couleur des faces sélectionnées de l\'objet.

-    **[Basculer la visibilité](Std_ToggleVisibility/fr.md)**: rend l\'objet visible ou invisible dans la [Vue 3D](3D_view/fr.md).

-    **[Afficher la selection](Std_ShowSelection/fr.md)**: rend visible l\'objet sélectionné.

-    **[Masquer la selection](Std_HideSelection/fr.md)**: rend l\'objet sélectionné invisible.

-    **[Basculer la selectivité](Std_ToggleSelectability/fr.md)**: fait basculer la sélection de l\'objet dans la [Vue 3D](3D_view/fr.md).

-    **[Sélectionner tous les cas](Std_TreeSelectAllInstances/fr.md)**: sélectionne toutes les instances de cet objet dans l\'arborescence.

-    **[Envoyer la console Python](Std_SendToPythonConsole/fr.md)**: crée une variable dans la [console Python](Python_console/fr.md) faisant référence à l\'objet



### Actions du clavier 

Les actions clavier suivantes sont disponibles lorsque le curseur est sur l\'arborescence :

-    **Ctrl**\+**F** : ouvre une boîte de recherche au bas de l\'arbre, permettant de rechercher et d\'atteindre des objets en utilisant leurs noms ou leurs étiquettes.

-   Actions d\'expansion et de réduction à l\'aide des combinaisons **Alt**+**Flèche** : {{Version/fr|0.20}}
    -   
        **Alt**
        
        \+**Flèche gauche** : réduit le(s) élément(s) sélectionné(s).

    -   
        **Alt**
        
        \+**Flèche droit** : développe le(s) élément(s) sélectionné(s).

    -   
        **Alt**
        
        \+**Flèche haut** : développe le ou les éléments sélectionnés avec tous leurs enfants de niveau 1 réduits (les enfants plus profonds restent inchangés).

    -   
        **Alt**
        
        \+**Flèche bas** : développe le ou les éléments sélectionnés avec tous leurs enfants de niveau 1 également développés (les enfants plus profonds restent inchangés).



## Icônes de superposition 

Une ou plusieurs petites icônes de superposition peuvent être affichées au-dessus de l\'icône par défaut d\'un objet dans l\'arborescence. Les icônes superposées disponibles et leur signification sont énumérées ci-dessous. {{Version/fr|0.19}}



### ![](images/FreeCAD_Tree_view_recompute.png ) Marque blanche sur fond bleu 

Cela indique que l\'objet doit être [recalculé](Std_Refresh/fr.md) en raison de modifications apportées au modèle ou parce que l\'utilisateur a marqué l\'objet dans le menu contextuel de la vue arborescente pour qu\'il soit recalculé. Dans la plupart des cas, les recalculs sont déclenchés automatiquement, mais ils sont parfois retardés pour des raisons de performance.



### ![](images/FreeCAD_Tree_view_tip.png ) Flèche blanche sur fond vert 

Ceci indique ce qu\'on appelle le [Tip](PartDesign_Body/fr#Tip_.28fonction_r.C3.A9sultante.29.md) d\'un corps. C\'est généralement la dernière fonction d\'un [PartDesign Corps](PartDesign_Body/fr.md) et représente le corps entier pour le monde extérieur au corps, par exemple lorsque le corps est exporté ou utilisé dans des [Part opérations booléennes](Part_Boolean/fr.md). Le Tip peut être modifié par l\'utilisateur.



### ![](images/FreeCAD_Tree_view_unattached.png ) Maillon de chaîne violet sur fond blanc 

Cela est généralement indiqué pour les [esquisses](Sketch/fr.md), les primitives géométriques, telles que la boîte, le cylindre, etc. et un [Datum](Datum/fr.md) géométrique. Elle indique que l\'objet n\'est pas attaché à quelque chose. Il n\'a pas de décalage d\'ancrage et obtient sa position et son alignement uniquement à partir de sa propriété [Placement](Placement/fr.md).

Il existe un [Tutoriel Les bases pour l\'ancrage](Basic_Attachment_Tutorial/fr.md) expliquant comment gérer ces objets.



### ![](images/FreeCAD_Tree_view_notfullyconstrained.png ) X jaune 

Ceci n\'est utilisé que pour des [esquisses](Sketch/fr.md) et indique que l\'esquisse n\'est pas entièrement contrainte. Dans l\'[atelier Sketcher](Sketcher_Workbench/fr.md), le nombre de degrés de liberté restants est indiqué dans les messages du solveur.



### ![](images/FreeCAD_Tree_view_error.png ) Point d\'exclamation blanc sur fond rouge 

Cela indique que l\'objet présente une erreur qui doit être corrigée. Après avoir recalculé l\'ensemble du document, une info-bulle décrivant l\'erreur est affichée lorsque vous passez la souris sur l\'objet dans l\'arborescence. Remarque: tous les autres objets dépendant d\'un objet dans un tel état d\'erreur ne seront pas correctement recalculés, ils peuvent donc encore présenter un ancien état.



### ![](images/FreeCAD_Tree_view_hidden.png ) Symbole de l\'oeil 

Cela indique que l\'objet sera masqué dans la vue en arborescence parce que son option **Cacher l'élément** du menu contextuel est cochée. Cocher puis décocher l\'option **Montrer les éléments cachés** du menu contextuel du document, ou reouvrir le document, permet de mettre à jour la vue en arborescence.


{{Interface navi

}} {{Std Base navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Tree view/fr
