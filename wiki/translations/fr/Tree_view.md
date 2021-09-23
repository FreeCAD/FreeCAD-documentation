# Tree view/fr
 {{TOCright}}

## Introduction

La [vue en arborescence](Tree_view/fr.md) apparaît dans l\'onglet **Modèle** de la [Vue combinée](Combo_view/fr.md), l\'un des panneaux les plus importants de l\'[interface](Interface/fr.md). Elle montre tous les objets définis par l\'utilisateur qui font partie d\'un document FreeCAD. L\'arborescence est une représentation de la [Structure d\'un document](Document_structure/fr.md) et indique quelles informations sont enregistrées sur le disque.

Ces objets ne doivent pas nécessairement être des formes géométriques visibles dans la [Vue 3D](3D_view/fr.md) mais peuvent également prendre en charge des objets de données créés avec l\'un des [ateliers](Workbenches/fr.md).

![](images/FreeCAD_Tree_view.png )


*L'arborescence montrant divers éléments du document.*

## Travailler avec la vue en arborescence 

Par défaut, chaque fois qu\'un nouvel objet est créé, il est ajouté à la fin de la liste dans l\'arborescence. L\'arborescence permet de gérer les objets pour les garder organisés. Elle permet de créer des [groupes](Std_Group/fr.md), de déplacer des objets à l\'intérieur de groupes, de déplacer des groupes à l\'intérieur d\'autres groupes, de renommer des objets, de copier des objets, de supprimer des objets et d\'autres opérations dans le menu contextuel (clic droit) qui dépendent de l\'objet actuellement sélectionné et du plan de travail actuellement actif.

De nombreuses opérations créent des objets qui dépendent d\'un objet déjà existant. Dans ce cas, l\'arborescence montre cette relation en absorbant l\'objet plus ancien à l\'intérieur du nouvel objet. Le développement et la réduction des objets dans l\'arborescence montrent l\'historique paramétrique de cet objet. Les objets qui sont plus profondément à l\'intérieur des autres sont plus anciens, tandis que les objets qui sont à l\'extérieur sont plus récents et sont dérivés des objets plus anciens. En modifiant les objets intérieurs, les opérations paramétriques se propagent jusqu\'au sommet, générant un nouveau résultat.

<img alt="" src=images/FreeCAD_Tree_view_parametric_history_1.png  style="width:" height="304px;"> <img alt="" src=images/FreeCAD_Tree_view_parametric_history_2.png  style="width:" height="304px;">

<img alt="" src=images/FreeCAD_Tree_view_parametric_history_3.png  style="width:" height="304px;">


*L'objet au sommet est créé en effectuant des opérations paramétriques sur des objets qui ont eux-mêmes été créés par des opérations précédentes. L'élargissement de l'arbre à plusieurs niveaux révèle les éléments originaux qui ont été utilisés pour créer les solides partiels.*

## Actions


**Remarque :**

des expressions et des actions de liaison ont été ajoutées dans la version 0.19.

Étant donné que l\'arborescence répertorie les objets pouvant être visibles dans la [vue 3D](3D_view/fr.md), de nombreuses actions sont identiques à celles qui peuvent être exécutées à partir de la [vue 3D](3D_view/fr.md).

Lorsque l\'application démarre, la valeur par défaut de l\'[Atelier Start](Start_Workbench/fr.md) est active, aucun document n\'a été créé, un clic droit sur la [vue en arborescence](Tree_view/fr.md) affiche une seule commande:

-    **Expression actions**: [Copy selected](Std_Expressions.md), [Copy active document](Std_Expressions.md), [Copy all documents](Std_Expressions.md), coller. Celles-ci permettent de travailler avec divers documents mais sont désactivées si aucun document n\'est présent.

Une fois un nouveau document créé, les éléments suivants deviennent actifs:

-    **Expression actions**: [Copy active document](Std_Expressions.md), [Copy all documents](Std_Expressions.md).

De plus, les actions [Liens](Std_LinkMake/fr.md) sont disponibles.

-    **Link actions**: [Std Créer un lien](Std_LinkMake/fr.md).

    -   
        **Make Link group**
        
        : [Simple group](Std_LinkMakeGroup.md), [Group with links](Std_LinkMakeGroup.md), [Group with transform links](Std_LinkMakeGroup.md).

### Sélection du document 

Si vous sélectionnez le document actif et cliquez avec le bouton droit, en plus de **Expression actions** et **Link actions**, les commandes suivantes apparaissent :

-    **Show hidden items**: si elle est active, l\'arborescence affichera les éléments masqués.

-    **Search**: affiche un champ de saisie pour rechercher des objets à l\'intérieur du document sélectionné.

-    **Close document**: ferme le document sélectionné en appelant la méthode `closeDocument()` de l\'application.

-    **Skip recomputes**: s\'il est actif, les objets du document ne seront pas [recalculés](Std_Refresh/fr.md) automatiquement.

    -   
        **Allow partial recomputes**
        
        : s\'il est actif, le document n\'autorisera le [recalcul](Std_Refresh/fr.md) que pour certains objets.

-    **Mark to recompute**: marque tous les objets du document comme touchés et prêts pour [recalcul](Std_Refresh/fr.md).

-    **[Créer un groupe](Std_Group/fr.md)**: crée un [groupe](Std_Group/fr.md) dans le document sélectionné en utilisant la méthode `addObject()` du document.

### Sélection d\'objets 

Une fois les objets ajoutés au document, en plus des actions précédentes, un clic droit sur une partie vide de l\'arborescence affichera des commandes supplémentaires. Ceux-ci dépendent du type d\'objet et de l\'atelier actif.

Par exemple, avec [Atelier Draft](Draft_Workbench/fr.md) actif, sélectionnez d\'abord un objet, puis cliquez avec le bouton droit sur un emplacement vide dans l\'arborescence :

-    **[Basculer la visibilité](Std_ToggleVisibility/fr.md)**: rend l\'objet visible ou invisible dans la [vue 3D](3D_view/fr.md).

-    **[Afficher la sélection](Std_ShowSelection/fr.md)**: rend les objets sélectionnés visibles.

-    **[Masquer la sélection](Std_HideSelection/fr.md)**: rend les objets sélectionnés invisibles.

-    **[Basculer la sélectivité](Std_ToggleSelectability/fr.md)**: rend l\'objet non sélectionnable dans la [vue 3D](3D_view/fr.md). Utilisez à nouveau cette commande pour annuler son effet. Il définit l\'attribut `Selectable` de l\'objet sur `True` ou `False`. Modifiez la propriété en basculant {{PropertyView/fr|Selectable}} dans l\'[Éditeur de propriétés](Property_editor/fr.md).

-    **[Select all instances](Std_TreeSelectAllInstances.md)**: sélectionne toutes les instances de cet objet dans l\'arborescence.

-    **[Apparence](Std_SetAppearance/fr.md)**: ouvre la boîte de dialogue pour changer la couleur et la taille des lignes et des sommets et la couleur des faces.

-    **[Couleur aléatoire](Std_RandomColor/fr.md)**: attribue une couleur aléatoire à l\'objet. Il définit l\'attribut `ShapeColor` de l\'objet sur un tuple `(r,g,b)` avec des arborescences aléatoires entre 0 et 1. Modifiez la propriété en modifiant {{PropertyView/fr|Shape Color}} dans l\'[Éditeur de propriétés](Property_editor/fr.md).

-    **[Couper](Std_Cut.md)**: désactivé si le clic droit n\'est pas sur l\'objet.

-    **[Copier](Std_Copy.md)**: copie un objet en mémoire.

-    **[Coller](Std_Paste.md)**: pastes the copied object into the document; the copy is added to the end of the tree view.

-    **[Effacer](Std_Delete.md)**: supprime l\'objet du document et de l\'arborescence en appelant la méthode `removeObject()` du document.

-    **Utilities**: **(optionnel)** commandes contextuelles supplémentaires fournies par l\'[Atelier Draft](Draft_Workbench/fr.md).

Si un objet est sélectionné, par exemple, une [Draft Ligne](Draft_Line/fr.md) et qu\'un clic droit est effectué dans le même objet, des commandes supplémentaires peuvent être disponibles:

-    **Transform**: lance le widget de transformation pour déplacer ou faire pivoter l\'objet.

-    **Set colors**: définit les couleurs de l\'objet.

-    **Flatten this wire**: **(Draft)** commande spécifique pour une [Draft Ligne](Draft_Line/fr.md)

-    **Hide item**: si actif, l\'objet sélectionné sera défini comme masqué.

-    **Mark to recompute**: marque l\'objet sélectionné comme coché et prêt pour être [recalculer](Std_Refresh/fr.md).

-    **Recompute**: recalcule l\'objet sélectionné.

-    **Rename**: commence à modifier le nom de l\'objet sélectionné. Cela permet de modifier l\'attribut `Label` mais pas l\'attribut `Name` car ce dernier est en lecture seule.

## Icônes de superposition 

Une ou plusieurs petites icônes de superposition peuvent être affichées au-dessus de l\'icône par défaut d\'un objet dans l\'arborescence. Les icônes superposées disponibles et leur signification sont énumérées ci-dessous. {{Version/fr|0.19}}

### ![](images/FreeCAD_Tree_view_recompute.png ) Marque blanche sur fond bleu 

Cela indique que l\'objet doit être [recalculer](Std_Refresh/fr.md) en raison de modifications apportées au modèle ou parce que l\'utilisateur a marqué l\'objet dans le menu contextuel de la vue arborescente pour qu\'il soit recalculé. Dans la plupart des cas, les recalculs sont déclenchés automatiquement, mais ils sont parfois retardés pour des raisons de performance.

### ![](images/FreeCAD_Tree_view_tip.png ) Flèche blanche sur fond vert 

Ceci indique ce qu\'on appelle le [Tip](PartDesign_Body/fr#Tip_.28fonction_r.C3.A9sultante.29.md) d\'un corps. C\'est généralement la dernière caractéristique d\'un [PartDesign Corps](PartDesign_Body/fr.md) et représente le corps entier pour le monde extérieur au corps, par exemple lorsque le corps est exporté ou utilisé dans des opérations [Part booléennes](Part_Boolean/fr.md). Le Tip peut être modifié par l\'utilisateur.

### ![](images/FreeCAD_Tree_view_unattached.png ) Maillon de chaîne violet sur fond blanc 

Cela est généralement indiqué pour les [esquisses](Sketch/fr.md), les primitives géométriques, telles que la boîte, le cylindre, etc. et un [Datum](Datum/fr.md) géométrique. Elle indique que l\'objet n\'est pas attaché à quelque chose. Il n\'a pas de décalage d\'ancrage et obtient sa position et son alignement uniquement à partir de sa propriété [Placement](Placement/fr.md).

Il existe un [Tutoriel Les bases pour l\'ancrage](Basic_Attachment_Tutorial/fr.md) expliquant comment gérer ces objets.

### ![](images/FreeCAD_Tree_view_notfullyconstrained.png ) X jaune 

Ceci n\'est utilisé que pour des [esquisses](Sketch/fr.md) et indique que l\'esquisse n\'est pas entièrement contrainte. Dans l\'[atelier Sketcher](Sketcher_Workbench/fr.md), le nombre de degrés de liberté restants est indiqué dans les messages du solveur.

### ![](images/FreeCAD_Tree_view_error.png ) Point d\'exclamation blanc sur fond rouge 

Cela indique que l\'objet présente une erreur qui doit être corrigée. Après avoir recalculé l\'ensemble du document, une info-bulle décrivant l\'erreur est affichée lorsque vous passez la souris sur l\'objet dans l\'arborescence. Remarque: tous les autres objets dépendant d\'un objet dans un tel état d\'erreur ne seront pas correctement recalculés, ils peuvent donc encore présenter un ancien état.


{{Interface navi

}} {{Std Base navi}} 
