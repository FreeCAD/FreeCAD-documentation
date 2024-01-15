# Tree view/fr
## Introduction

La [vue en arborescence](Tree_view/fr.md) apparaît dans l\'onglet **Modèle** de la [vue combinée](Combo_view/fr.md), l\'un des panneaux les plus importants de l\'[interface](Interface/fr.md). Elle montre tous les objets définis par l\'utilisateur qui font partie d\'un document FreeCAD. L\'arborescence est une représentation de la [structure d\'un document](Document_structure/fr.md) et indique quelles informations sont enregistrées sur le disque.

Ces objets ne doivent pas nécessairement être des formes géométriques visibles dans la [Vue 3D](3D_view/fr.md) mais peuvent également prendre en charge des objets de données créés avec l\'un des [ateliers](Workbenches/fr.md).

![](images/FreeCAD_Tree_view.png )



*La vue en arborescence montrant divers éléments du document.*



## Travailler avec la vue en arborescence 

Par défaut, chaque fois qu\'un nouvel objet est créé, il est ajouté à la fin de la liste dans l\'arborescence. L\'arborescence permet de gérer les objets pour les garder organisés. Elle permet de créer des [groupes](Std_Group/fr.md), de déplacer des objets à l\'intérieur de groupes, de déplacer des groupes à l\'intérieur d\'autres groupes, de réétiqueter des objets, de copier des objets, de supprimer des objets et d\'autres opérations dans le menu contextuel (clic droit) qui dépendent de l\'objet actuellement sélectionné et du plan de travail actuellement actif.

De nombreuses opérations créent des objets qui dépendent d\'un objet déjà existant. Dans ce cas, l\'arborescence montre cette relation en absorbant l\'objet plus ancien à l\'intérieur du nouvel objet. Le développement et la réduction des objets dans l\'arborescence montrent l\'historique paramétrique de cet objet. Les objets qui sont plus profondément à l\'intérieur des autres sont plus anciens, tandis que les objets qui sont à l\'extérieur sont plus récents et sont dérivés des objets plus anciens. En modifiant les objets intérieurs, les opérations paramétriques se propagent jusqu\'au sommet, générant un nouveau résultat.

<img alt="" src=images/FreeCAD_Tree_view_parametric_history.png  style="width:" height="300px;">



*L'objet au sommet est créé en effectuant des opérations paramétriques sur des objets qui ont eux-mêmes été créés par des opérations précédentes.<br>
L'expansion complète de l'arboresence révèle les éléments d'origine qui ont été utilisés pour créer les solides partiels.*



### Colonnes de la vue en arborescence 

Par défaut, la vue en arborescence n\'affiche qu\'une seule colonne avec les étiquettes et les icônes des objets. Une deuxième colonne avec des descriptions peut être affichée en option, et des en-têtes de colonne sont également ajoutés.

Pour activer la colonne de description, cliquez avec le bouton droit de la souris sur la vue en arborescence et sélectionnez dans le menu contextuel :
**Paramètres de la vue en arborescence → Afficher la colonne de description** {{Version/fr|0.21}}



### Modifier l\'étiquette de l\'objet 

Sélectionnez un objet dans la première colonne et appuyez sur **F2** (sous Windows et Linux) ou **Entrée** (sous macOS) pour modifier sa propriété **Label**. Cette propriété peut également être modifiée via l\'action du menu contextuel décrite ci-dessous ou dans l\'[éditeur de propriétés](Property_editor/fr.md).



### Modifier la description de l\'objet 

Un objet peut éventuellement être accompagné d\'une description. Cette information est enregistrée dans sa propriété **Label2**. Si la colonne de description est affichée, vous pouvez modifier cette propriété en sélectionnant un objet dans cette colonne et en appuyant sur **F2** (sous Windows et Linux) ou **Entrée** (sous macOS). La propriété peut également être modifiée dans l\'[éditeur de propriétés](Property_editor/fr.md).

## Actions

Étant donné que la vue en arborescence répertorie les objets pouvant être visibles dans la [vue 3D](3D_view/fr.md), de nombreuses actions sont identiques comme celles qui peuvent être exécutées à partir de la [vue 3D](3D_view/fr.md).



### Lancement de l\'application 

Lorsque l\'application démarre, que l\'[atelier Start](Start_Workbench/fr.md) par défaut est actif et qu\'aucun document n\'a été créé, le menu contextuel de la [vue en arborescence](Tree_view/fr.md) ne comporte qu\'une seule entrée :

-    **Actions sur les expressions**. Lorsque le curseur est déplacé sur cette entrée, un sous-menu contenant quatre commandes s\'ouvre :

    -   [Copier la sélection](Std_Expressions/fr.md)
    -   [Copier le document actif](Std_Expressions/fr.md)
    -   [Copier tous les documents](Std_Expressions/fr.md)
    -   [Coller](Std_Paste/fr.md)

Elles permettent de travailler avec divers documents, mais sont désactivées si aucun document n\'est présent.



### Nouveau document 

Une fois qu\'un nouveau document a été créé, un clic droit sur l\'arrière-plan ouvre le menu contextuel qui contient désormais deux entrées :

-    **Actions sur les expressions**comme ci-dessus mais avec ces deux entrées activées :

    -   [Copier le document actif](Std_Expressions/fr.md)
    -   [Copier tous les documents](Std_Expressions/fr.md)

-    **Actions sur les liens**\- un sous-menu avec deux entrées :

    -   
        **Faire un groupe de liens**
        
        \- un autre sous-menu contenant trois commandes :

        -   [Groupe simple](Std_LinkMakeGroup/fr.md)
        -   [Groupe avec liens](Std_LinkMakeGroup/fr.md)
        -   [Groupe avec liens de transformation](Std_LinkMakeGroup/fr.md)

    -   [Créer un lien](Std_LinkMake/fr.md)



### Sélection du document 

Si vous sélectionnez le document et cliquez avec le bouton droit, en plus de **Actions sur les expressions** et **Actions sur les liens**, le menu contextuel contient les commandes suivantes :

-    **Afficher les éléments masqués dans la vue en arborescence**: si elle est active, la vue en arborescence affichera les éléments masqués.

-    **Rechercher...**: affiche un champ de saisie pour rechercher des objets à l\'intérieur du document sélectionné.

-    **Fermer le document**: ferme le document sélectionné.

-    **Ajouter tous les objets dépendants à la sélection**: tous les objets dépendants seront ajoutés à la sélection. De cette manière, il est possible de voir les dépendances et, par exemple, de supprimer tous les objets dépendants en une seule fois. Disponible uniquement pour les objets avec des liens et pour les documents.

-    **Sauter les recalculs**: si actif, les objets du document ne seront pas [recalculés](Std_Refresh/fr.md) automatiquement.

-    **Permettre un recalcul partiel**: si actif, le document n\'autorisera le [recalcul](Std_Refresh/fr.md) que pour certains objets. Uniquement disponible si **Sauter les recalculs** est activé.

-    **Marquer pour recalculer**: marque tous les objets du document comme touchés et prêts pour [recalcul](Std_Refresh/fr.md).

-    **[Créer un groupe...](Std_Group/fr.md)**: crée un [groupe](Std_Group/fr.md) dans le document sélectionné.



### Sélection d\'objets 

Une fois que les objets ont été ajoutés au document, un clic droit sur ceux-ci fait apparaître des commandes supplémentaires. Celles-ci dépendent du nombre d\'objets sélectionnés, de leur type et également du plan de travail actif. Dans la plupart des cas et avec la plupart des ateliers (sauf l\'[atelier Start](Start_Workbench/fr.md)), les commandes suivantes sont alors disponibles :

-    **[Apparence](Std_SetAppearance/fr.md)**: lance une boîte de dialogue permettant de modifier les propriétés visuelles de l\'objet entier.

-    **[Couleur aléatoire](Std_RandomColor/fr.md)**: attribue une couleur aléatoire à l\'objet.

-    **[Couper](Std_Cut/fr.md)**: désactivé.

-    **[Copier](Std_Copy/fr.md)**: copie un objet en mémoire.

-    **[Coller](Std_Paste/fr.md)**: colle l\'objet copié dans le document. La copie est ajoutée à la fin de l\'arborescence.

-    **[Supprimer](Std_Delete/fr.md)**: supprime l\'objet du document.

-    **[Activer/désactiver la visibilité dans l'arborescence](#Symbole_de_l'oeil.md)**: permet d\'activer la visibilité des objets dans l\'arborescence.

-    **Marquer pour recalculer**: marque l\'objet sélectionné comme pris en compte, et prêt pour le [recalcul](Std_Refresh/fr.md).

-    **Recalculer l'objet**: recalcule l\'objet sélectionné.

-    **Renommer**: lance l\'édition de l\'étiquette de l\'objet sélectionné, et non du nom qui est en lecture seule. Cette option n\'est disponible que si un seul objet est sélectionné.

Comme exemple d\'extension du menu contextuel, si un [Part Cube](Part_Box/fr.md) est cliqué du bouton droit de la souris alors que l\'[atelier Part](Part_Workbench/fr.md) est actif, les commandes supplémentaires suivantes sont disponibles :

-    **[Modifier](Std_Edit/fr.md)**: active le mode d\'édition de l\'objet.

-    **[Transformer](Std_TransformManip/fr.md)**: lance le widget de transformation pour déplacer ou faire tourner l\'objet.

-    **[Éditeur de pièces ancrées](Part_EditAttachment/fr.md)**: lance une boîte de dialogue pour ancrer l\'objet à un ou plusieurs autres objets.

-    **[Définir les couleurs...](Part_FaceColors/fr.md)**: définit la couleur des faces sélectionnées de l\'objet.

-    **[Basculer la visibilité](Std_ToggleVisibility/fr.md)**: rend l\'objet visible ou invisible dans la [Vue 3D](3D_view/fr.md).

-    **[Afficher la selection](Std_ShowSelection/fr.md)**: rend visible l\'objet sélectionné.

-    **[Masquer la selection](Std_HideSelection/fr.md)**: rend l\'objet sélectionné invisible.

-    **[Basculer la selectivité](Std_ToggleSelectability/fr.md)**: fait basculer la sélection de l\'objet dans la [Vue 3D](3D_view/fr.md).

-    **[Sélectionner tous les cas](Std_TreeSelectAllInstances/fr.md)**: sélectionne toutes les instances de cet objet dans l\'arborescence.

-    **[Envoyer vers la console Python](Std_SendToPythonConsole/fr.md)**: crée une variable dans la [console Python](Python_console/fr.md) faisant référence à l\'objet.



### Actions du clavier 

Les actions clavier suivantes sont disponibles lorsque le curseur est sur la vue en arborescence :

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

Une ou plusieurs petites icônes de superposition peuvent être affichées au-dessus de l\'icône par défaut d\'un objet dans l\'arborescence. Les icônes superposées disponibles et leur signification sont énumérées ci-dessous.



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

Ceci indique que l\'objet sera caché dans la vue en arborescence si l\'option du menu contextuel **Afficher les éléments masqués dans la vue en arborescence** n\'est pas cochée.


{{Interface navi

}} {{Std Base navi}}



---
⏵ [documentation index](../README.md) > Tree view/fr
