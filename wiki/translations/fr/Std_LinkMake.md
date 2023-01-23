---
- GuiCommand:/fr
   Name:Std LinkMake
   Name/fr:Std Créer un lien
   MenuLocation:
   Workbenches:Tous
   Version:0.19
   SeeAlso:[Std Part](Std_Part/fr.md), [Std Groupe](Std_Group/fr.md), [PartDesign Corps](PartDesign_Body/fr.md)
---

# Std LinkMake/fr

## Description


**[<img src=images/Std_LinkMake.svg style="width:16px"> [Std Créer un lien](Std_LinkMake/fr.md)**

crée une classe [App Link](App_Link/fr.md) (`App::Link`), un type d\'objet faisant référence ou lié à un autre objet, dans le même document ou dans un autre document. Il est spécialement conçu pour dupliquer efficacement un seul objet plusieurs fois, ce qui permet de créer des [assemblages](assembly/fr.md) complexes à partir de sous-assemblages plus petits et de plusieurs composants réutilisables tels que des vis, des écrous et des éléments de fixation similaires.

L\'objet [App Link](App_Link/fr.md) a été nouvellement introduit dans la v0.19. Auparavant, une simple duplication d\'objets pouvait être réalisée avec **[<img src=images/Draft_Clone.svg style="width:16px"> [Draft Cloner](Draft_Clone/fr.md)**, mais c\'est une solution moins efficace en raison de son implémentation qui crée essentiellement une copie de la [forme](Part_TopoShape/fr.md) interne de l\'objet source. D\'un autre côté, un lien fait directement référence à la forme d\'origine, donc plus efficace en mémoire.

En lui-même, l\'objet [Link](App_Link/fr.md) peut se comporter comme un tableau dupliquant son objet de base plusieurs fois. Cela peut être fait en définissant sa propriété {{PropertyData/fr|Element Count}} sur {{Value|1}} ou plus. Cet objet \"[Réseau lien](Std_LinkMake/fr#R.C3.A9seau_lien.md)\" peut également être créé avec les différents outils de tableau de l\'<img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [atelier Draft](Draft_Workbench/fr.md), par exemple **[<img src=images/Draft_OrthoArray.svg style="width:16px"> [Draft Réseau orthogonal](Draft_OrthoArray/fr.md)**, **[<img src=images/Draft_PolarArray.svg style="width:16px"> [Draft Réseau polaire](Draft_PolarArray/fr.md)**, et **[<img src=images/Draft_CircularArray.svg style="width:16px"> [Draft Réseau circulaire](Draft_CircularArray/fr.md)**.

Lorsqu\'ils sont utilisés avec l\'<img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [atelier PartDesign](PartDesign_Workbench/fr.md), les liens sont destinés à être utilisés avec **[<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Corps](PartDesign_Body/fr.md)**. Il est donc recommandé de définir {{PropertyView/fr|Display Mode Body}} sur {{Value|Tip}} pour sélectionner les caractéristiques du corps entier et non les fonctions individuelles. Pour créer des tableaux des [PartDesign Features](PartDesign_Feature/fr.md) internes, utilisez **[<img src=images/PartDesign_LinearPattern.svg style="width:16px"> [PartDesign Répétition linéaire](PartDesign_LinearPattern/fr.md)**, **[<img src=images/PartDesign_PolarPattern.svg style="width:16px"> [PartDesign Répétition circulaire](PartDesign_PolarPattern/fr.md)** et **[<img src=images/PartDesign_MultiTransform.svg style="width:16px"> [PartDesign Transformation multiple](PartDesign_MultiTransform/fr.md)**.

L\'outil **[<img src=images/Std_LinkMake.svg style="width:16px"> [Std Créer un lien](Std_LinkMake/fr.md)** n\'est pas défini par un atelier particulier mais par le système de base. De ce fait il se trouve donc dans **Barre d'outils Structure** qui est disponible dans tous les [ateliers](Workbenches/fr.md). L\'objet Link, utilisé en conjonction avec **[<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part/fr.md)** pour regrouper divers objets, constitue la base des ateliers <img alt="" src=images/Assembly3_workbench_icon.svg  style="width:24px;"> [Assembly3](Assembly3_Workbench/fr.md) et <img alt="" src=images/Assembly4_workbench_icon.svg  style="width:24px;"> [Assembly4](Assembly4_Workbench/fr.md).



## Utilisation

Avec sélection :

1.  Sélectionnez un objet dans la [Vue en arborescence](Tree_view/fr.md) ou la [vue 3D](3D_view/fr.md) pour lequel vous souhaitez créer un lien.
2.  Appuyez sur le bouton **[<img src=images/Std_LinkMake.svg style="width:16px"> [Std Créer un lien](Std_LinkMake/fr.md)**. L\'objet crée a la même icône que l\'objet d\'origine mais a une flèche superposée indiquant qu\'il s\'agit d\'un lien.

Sans sélection :

1.  Si aucun objet n\'est sélectionné, appuyez sur le bouton **[<img src=images/Std_LinkMake.svg style="width:16px"> [Std Créer un lien](Std_LinkMake/fr.md)** pour créer un lien vide <img alt="" src=images/Link.svg  style="width:24px;">.
2.  Allez dans l\'[Éditeur de propriétés](Property_editor/fr.md), puis cliquez sur la propriété {{PropertyData/fr|Linked Object}} pour ouvrir la [Dialogue de sélection des liens](Selection_methods.md) pour choisir un objet, puis appuyez sur **OK **.
3.  Au lieu de choisir un objet entier dans la [Vue en arborescence](Tree_view/fr.md), vous pouvez également choisir des sous-éléments (sommets, arêtes ou faces) d\'un seul objet dans la [Vue 3D](3D_view/fr.md). Dans ce cas, le lien dupliquera uniquement ces sous-éléments et la superposition de flèches sera différente. Cela peut également être fait avec **[<img src=images/Std_LinkMakeRelative.svg style="width:16px"> [Std Créer un sous-lien](Std_LinkMakeRelative/fr.md)**.

![](images/Std_Link_tree_example.png ) ![](images/Std_Link_example.png )



*(1) Un objet, (2) un lien vide, (3) un lien complet vers le premier objet (avec un matériau de remplacement), et (4) un lien vers seulement quelques sous-éléments de l'objet. Le lien vide n'est pas lié à l'objet réel et n'est donc pas affiché dans la [vue 3D](3D_view/fr.md).*



## Utilisation : documents externes 

1.  Commencez par un document contenant au moins un objet qui sera la source du lien.
2.  Ouvrez un nouveau document ou un document existant. Pour une manipulation plus facile, utilisez **[<img src=images/Std_TreeMultiDocument.svg style="width:16px"> [Std Arborescence plusieurs documents](Std_TreeMultiDocument/fr.md)** pour afficher les deux documents dans la [Vue en arborescence](Tree_view/fr.md). Avant de continuer, [sauvegarder](Std_Save/fr.md) les deux documents. Le lien ne pourra pas trouver sa source et sa cible à moins que les deux documents ne soient enregistrés sur le disque.
3.  Dans le premier document, sélectionnez l\'objet que vous souhaitez lier, puis changez d\'onglet dans la [Zone de vue principale](main_view_area/fr.md) pour passer au deuxième document.
4.  Appuyez sur **[<img src=images/Std_LinkMake.svg style="width:16px"> [Std Créer un lien](Std_LinkMake/fr.md)**. L\'objet produit a la même icône que l\'objet d\'origine mais a une flèche superposée indique qu\'il s\'agit d\'un lien provenant d\'un document externe.


**Remarques :**

-   Lors de l\'enregistrement du document avec le lien, il sera demandé également de [sauvegarder](Std_Save/fr.md) le document source qui contient l\'objet d\'origine.

-   Pour inclure l\'objet d\'origine dans le document avec le lien, utilisez **[<img src=images/Std_LinkImport.svg style="width:16px"> [Std Importer des liens](Std_LinkImport/fr.md)** ou **[<img src=images/Std_LinkImportAll.svg style="width:16px"> [Std Importer tous les liens](Std_LinkImportAll/fr.md)**.

-    **[<img src=images/Std_LinkMake.svg style="width:16px"> [Std Créer un lien](Std_LinkMake/fr.md)**peut être utilisé sur un objet Link existant afin de créer un lien vers un lien qui résout finalement l\'objet original dans le document source. Cela peut être réalisé avec **[<img src=images/Std_LinkMakeRelative.svg style="width:16px"> [Std Créer un sous-lien](Std_LinkMakeRelative/fr.md)** pour ne sélectionner que certains sous-éléments également.

![](images/Std_Link_tree_documents_example.png ) ![](images/Std_Link_documents_example.png )



*(1, 2) Deux objets d'un document source liés à un document cible, (3) un lien vers le deuxième lien (avec un matériau de remplacement) et (4) un lien vers les sous-éléments du deuxième lien.*



### Glisser-déposer 

Au lieu de changer d\'onglet de document, vous pouvez créer des liens en effectuant une opération de glisser-déposer dans la [Vue en arborescence](Tree_view/fr.md): sélectionnez l\'objet source dans le premier document, faites-le glisser, puis déposez-le dans le nom du second document tout en maintenant la touche **Alt** du clavier.

Le glisser-déposer entraîne différentes actions en fonction de la touche de modification enfoncée.

-   Sans touche de modification, il déplace simplement l\'objet d\'un document à l\'autre; une flèche inclinée s\'affiche dans le curseur.
-   Maintenir la touche **Ctrl** copie l\'objet ; un signe plus est affiché dans le curseur.
-   Maintenir la touche **Alt** crée un lien ; une paire de maillons de chaîne est affichée dans le curseur.

Pour les modificateurs **Ctrl** et **Alt**, le glisser-déposer peut également être effectué avec un seul document. Autrement dit, faire glisser un objet et le déposer dans le même nom de document peut être utilisé pour créer plusieurs copies ou plusieurs liens vers celui-ci.



## Groupes


**[<img src=images/Std_LinkMake.svg style="width:16px"> [Std Créer un lien](Std_LinkMake/fr.md)**

peut être utilisé avec des objets **[<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part/fr.md)** afin de dupliquer rapidement des groupes d\'objets positionnés dans l\'espace, c\'est-à-dire [assemblages](assembly/fr.md).

![](images/Std_Link_tree_Std_Part_example.png )



*Lien créé à partir d'une [Std Part](Std_Part/fr.md) ; les objets ne sont pas dupliqués mais ils sont répertoriés sous le conteneur d'origine et sous le conteneur Lien.*

Un **[<img src=images/Std_Group.svg style="width:16px"> [Std Groupe](Std_Group/fr.md)** ne possède pas de propriété {{PropertyData/fr|Placement}}, il ne peut donc pas contrôler la position des objets à l\'intérieur de celui-ci. Cependant, lorsque **[<img src=images/Std_LinkMake.svg style="width:16px"> [Std Créer un lien](Std_LinkMake/fr.md)** est utilisé avec **[<img src=images/Std_Group.svg style="width:16px"> [Std Groupe](Std_Group/fr.md)**, le lien résultant se comporte essentiellement comme un **[<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part/fr.md)** et peut également être déplacé dans l\'espace.

![](images/Std_Link_tree_Std_Group_example.png ) ![](images/Std_Link_Std_Group_example.png )



*Lien créé à partir d'un [Std Groupe](Std_Group/fr.md) ; les objets ne sont pas dupliqués mais ils sont répertoriés sous le conteneur d'origine et sous le conteneur Lien. Le lien (avec le matériau de remplacement) peut être déplacé dans l'espace, tout comme un [Std Part](Std_Part/fr.md).*

Un lien vers un **[<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part/fr.md)** gardera la visibilité des objets synchronisée avec la Part d\'origine. Donc si vous masquez un objet dans un lien, il sera masqué dans tous les liens et dans l\'objet d\'origine. D\'un autre côté, un lien vers un **[<img src=images/_Std_Group.svg style="width:16px"> [Std Groupe](Std_Group/fr.md)** permettra un contrôle indépendant des visibilités.

![](images/Std_Link_tree_Std_Part_visibility.png ) ![](images/Std_Link_tree_Std_Group_visibility.png )



*À gauche : [Std Part](Std_Part/fr.md) avec deux objets et deux liens vers la pièce; la visibilité des objets est synchronisée. À droite : [Std Group](Std_Group/fr.md) avec deux objets et deux liens vers le groupe. La visibilité des objets est contrôlée indépendamment dans chaque groupe.*



## Apparence de remplacement 

Lorsqu\'un lien est créé, par défaut {{PropertyView/fr|Override Material}} est `False`, donc le lien aura la même apparence que l\'original {{PropertyData/fr|Linked Object}}.

Lorsque {{PropertyView/fr|Override Material}} est défini sur `True`, la propriété {{PropertyView/fr|Shape Material}} contrôlera désormais l\'apparence du lien.

Quel que soit l\'état de {{PropertyView/fr|Override Material}}, il est possible de définir individuellement l\'apparence des sous-éléments (sommets, arêtes, faces) d\'un lien.

1.  Sélectionnez le lien dans la [Vue en arborescence](Tree_view/fr.md). Ouvrez le menu contextuel (clic droit) et choisissez **Override colors**.
2.  Choisissez maintenant les sous-éléments individuels que vous voulez dans la [Vue 3D](3D_view/fr.md), appuyez sur **Edit** et modifiez les propriétés, y compris la transparence.
3.  Pour supprimer les attributs personnalisés, sélectionnez les éléments dans la liste et appuyez sur **Remove**.
4.  Lorsque vous êtes satisfait du résultat, appuyez sur **OK** pour fermer la boîte de dialogue.


**Remarque :**

à partir de la v0.19, la coloration des sous-éléments est soumise au [Problème de dénomination topologique](topological_naming_problem/fr.md). Elle doit être effectuée comme dernière étape de modélisation lorsque le modèle n\'est plus sensé être modifié.

<img alt="" src=images/Std_Link_override_color_example.png  style="width:500px;">



*(1) Un objet original, (2) un lien avec un matériau de remplacement et (3) un deuxième lien avec des sous-éléments modifiés individuels.*



## Réseau lien 


**Voir aussi :**

[Draft Réseau orthogonal](Draft_OrthoArray/fr.md).

Lorsqu\'un lien est créé, par défaut, son {{PropertyData/fr|Element Count}} est {{Value|0}}, donc un seul objet Link sera visible dans la [Vue en arborescence](Tree_view/fr.md).

Étant donné que {{PropertyData/fr|Show Element}} est `True` par défaut, lorsque {{PropertyData/fr|Element Count}} est défini sur {{Value|1}} ou plus, automatiquement plus de liens seront créés sous le premier. Chaque nouveau lien peut être placé à la position souhaitée en modifiant sa propre propriété {{PropertyData/fr|Placement}}.

De la même manière, chaque élément du réseau peut avoir sa propre apparence modifiée, soit par les propriétés {{PropertyView/fr|Override Material}} et {{PropertyView/fr|Shape Material}}, soit en utilisant le menu **Override colors** sur l\'ensemble du réseau puis en sélectionnant des faces une par une. Ceci est décrit dans [Apparence de remplacement](#Apparence_de_remplacement.md).

<img alt="" src=images/Std_Link_tree_array_example.png ) ![](images/Std_Link_array_example.png  style="width:500px;">



*(1) Objet d'origine, et (2, 3, 4) un réseau Lien avec trois éléments, chacun dans une position différente. Le premier lien a un matériau de remplacement et des faces transparentes, les deux autres ont des couleurs de face personnalisées.*

Une fois que vous êtes satisfait de l\'emplacement et des propriétés des éléments Liens dans le réseau, vous pouvez changer {{PropertyData/fr|Show Element}} en `False` afin de masquer les liens individuels dans la [Vue en arborescence](Tree_view/fr.md). Cela présente l\'avantage de rendre le système plus réactif, en particulier si vous avez de nombreux objets dans le document.

Lors de la création de ce type de réseau de liens, vous devez placer chacun des éléments manuellement. Cependant, si vous souhaitez utiliser des modèles spécifiques pour placer les copies, vous pouvez utiliser les outils de réseau de l\'<img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [atelier Draft](Draft_Workbench/fr.md), comme **[16px](_File:Draft_OrthoArray.svg.md) [Draft Réseau orthogonal](Draft_OrthoArray/fr.md)**, **[<img src=images/Draft_PolarArray.svg style="width:16px"> [Draft Réseau polaire](Draft_PolarArray/fr.md)** et **[<img src=images/Draft_CircularArray.svg style="width:16px"> [Draft Réseau circulaire](Draft_CircularArray/fr.md)**; ces commandes peuvent créer des copies normales ou des copies de lien selon les options au moment de la création.



## Visibilité

Lorsque {{PropertyData/fr|Show Element}} est `True` et que des éléments individuels sont répertoriés dans la [Vue en arborescence](Tree_view/fr.md) dans un [Réseau lien](#R.C3.A9seau_lien.md), chaque lien peut être affiché ou masqué par en appuyant sur la barre **Espace** du clavier.

Une autre façon de masquer les éléments individuels consiste à utiliser le menu **Override colors**.

1.  Sélectionnez le tableau, ouvrez le menu **Override colors** (clic droit).
2.  Dans la [Vue 3D](3D_view/fr.md), choisissez n\'importe quel sous-élément à partir de n\'importe quel lien du réseau.
3.  Appuyez sur **Hide**. Une icône représentant un œil <img alt="" src=images/Invisible.svg  style="width:24px;"> devrait apparaître, indiquant que cet élément a été masqué de la [Vue 3D](3D_view/fr.md). L\'objet s\'affichera temporairement lorsque le curseur survolera l\'icône <img alt="" src=images/Invisible.svg  style="width:24px;">.
4.  Vous pouvez cliquer sur **OK** pour confirmer l\'opération et fermer la boîte de dialogue. Le lien restera caché même s\'il est affiché comme visible dans la [Vue en arborescence](Tree_view/fr.md).

![](images/Std_Link_array_visibility_example.png )



*Boîte de dialogue des couleurs des éléments disponibles lors de l'ouverture du menu contextuel d'un objet Lien dans l'arborescence.*

Si vous souhaitez restaurer la visibilité de cet élément du réseau, entrez à nouveau dans la boîte de dialogue, choisissez l\'icône en forme d\'œil, puis cliquez sur **Remove** pour supprimer l\'état caché et cliquez sur **OK** pour confirmer et fermez la boîte de dialogue. L\'élément sera à nouveau visible dans [Vue 3D](3D_view/fr.md).

Lorsque le lien est pour un **[<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part/fr.md)** ou un **[<img src=images/Std_Group.svg style="width:16px"> [Std Groupe](_Std_Part/fr.md)**, le menu **Override colors** fonctionne de la même manière qu\'avec les réseaux. Il permet de contrôler la couleur de la face, la couleur de l\'objet entier et la visibilité des objets du groupe.

![](images/Std_Link_Std_Part_visibility_example.png ) ![](images/Std_Link_Std_Part_visibility_example_3D.png )



*Un [Std Part](Std_Part/fr.md) contenant trois objets et un lien vers cette pièce; dans le lien, (1) le premier objet est rendu invisible, (2) le deuxième objet a des sous-éléments avec des couleurs différentes, (3) le troisième objet entier a une couleur et un niveau de transparence différents.*



## Propriétés

Un [App Link](App_Link/fr.md) (classe `App::Link`) est dérivé de [App DocumentObject](App_DocumentObject/fr.md) (classe `App::DocumentObject`). Il a donc les propriétés de base de ce dernier comme {{PropertyData/fr|Label}} et {{PropertyData/fr|Label2}}.

Voici les propriétés spécifiques disponibles dans l\'[Éditeur de propriétés](Property_editor/fr.md). Les propriétés masquées peuvent être affichées en utilisant la commande **Afficher tout** dans le menu contextuel de l\'[Éditeur de propriétés](Property_editor/fr.md).



### Données


{{TitleProperty|Link}}

-    {{PropertyData/fr|Linked Object|XLink}}: il indique l\'objet source de [App Link](App_Link/fr.md); il peut s\'agir d\'un objet entier ou d\'un sous-élément de celui-ci (sommet, arête ou face).

-    {{PropertyData/fr|Link Transform|Bool}}: la valeur par défaut est `False`, auquel cas le lien remplacera le propre emplacement de {{PropertyData/fr|Linked Object}}. S\'il est défini sur `True`, le lien sera placé à la même position que {{PropertyData/fr|Linked Object}}, et son placement sera relatif à l\'emplacement de {{PropertyData/fr|Linked Object}}. Ceci peut également être réalisé avec **[<img src=images/Std_LinkMakeRelative.svg style="width:16px"> [Std Créer un sous-lien](Std_LinkMakeRelative/fr.md)**.

-    {{PropertyData/fr|Placement|Placement}}: le placement du lien en coordonnées absolues.

-    {{PropertyData/fr|Link Placement|Placement|Hidden}}: il s\'agit d\'un décalage appliqué au-dessus du {{PropertyData/fr|Placement}} du {{PropertyData/fr|Linked Object}}. Cette propriété est normalement masquée mais apparaît si {{PropertyData/fr|Link Transform}} est défini sur `True` ; dans ce cas, {{PropertyData/fr|Placement}} devient désormais masqué.

-    {{PropertyData/fr|Show Element|Bool}}: la valeur par défaut est `True`, auquel cas la [Vue en arborescence](Tree_view/fr.md) affichera les copies de lien individuelles, tant que {{PropertyData/fr|Element Count}} est {{Value|1}} ou plus grand.

-    {{PropertyData/fr|Element Count|IntegerConstraint}}: la valeur par défaut est {{Value|0}}. S\'il est {{Value|1}} ou plus grand, le [App Link](App_Link.md) se comportera comme un réseau et dupliquera le même {{PropertyData/fr|Linked Object}} plusieurs fois. Si {{PropertyData/fr|Show Elements}} est `True`, chaque élément du tableau sera affiché dans la [Vue en arborescence](Tree_view/fr.md) et chacun pourra avoir son propre {{PropertyData/fr|Placement}} modifié. Chaque copie de lien aura un nom basé sur le [nom (Name)](Object_name/fr.md) du lien, augmenté de `_iN`, où `N` est un nombre commençant par `0`. Par exemple, avec un seul `Link`, les copies seront nommées `Link_i0`, `Link_i1`, `Link_i2`, etc.

-    {{PropertyData/fr|Link Execute|String}}: nom de la fonction d\'exécution qui s\'exécutera pour cet objet Link particulier. La valeur par défaut est {{Value|'appLinkExecute'}}. Réglez-le sur {{Value|'None'}} pour le désactiver.

-    {{PropertyData/fr|Colored Elements|LinkSubHidden|Hidden}}: liste des éléments Link dont la couleur a été remplacée.

-    {{PropertyData/fr|Scale|Float}}: la valeur par défaut est {{Value|1.0}}. C\'est un facteur de mise à l\'échelle uniforme dans chaque direction `X`, `Y` et `Z`. Par exemple, un cube de {{Value|2 mm}} x {{Value|2 mm}} x {{Value|2 mm}}, qui est mis à l\'échelle par {{Value|2.0}}, donnera une forme aux dimensions {{Value|4 mm}} x {{Value|4 mm}} x {{Value|4 mm}}.

-    {{PropertyData/fr|Scale Vector|Vector|Hidden}}: le facteur d\'échelle pour chaque composant `(X, Y, Z)` pour tous les éléments Link lorsque {{PropertyData/fr|Element Count}} est {{Value|1}} ou plus. Si {{PropertyData/fr|Scale}} est différent de {{Value|1.0}}, cette même valeur sera utilisée dans les trois composants.

-    {{PropertyData/fr|Scale List|VectorList}}: le facteur d\'échelle pour chaque élément Link.

-    {{PropertyData/fr|Visibility List|BoolList|Hidden}}: {{emphasis|(lecture seule)}} l\'état de visibilité de chaque élément Link, soit `True` ou `False`.

-    {{PropertyData/fr|Placement List|PlacementList|Hidden}}: {{emphasis|(lecture seule)}} l\'emplacement de chaque élément Link.

-    {{PropertyData/fr|Element List|LinkList|Hidden}}: la liste des éléments Link.

-    {{PropertyData/fr|_LinkTouched|Bool|Hidden}}:

-    {{PropertyData/fr|_ChildCache|LinkList|Hidden}}:


{{TitleProperty|Base}}

-    {{PropertyData/fr|Proxy|PythonObject|Hidden}}: classe personnalisée associée à cet objet. Cela n\'existe que pour la version [Python](Python/fr.md). Voir [Script](Std_LinkMake/fr#Script.md).

L\'objet [App Link](App_Link/fr.md) affichera en plus les propriétés de **Linked Object** d\'origine, ainsi l\'[Éditeur de propriétés](Property_editor/fr.md) peut avoir des groupes de propriétés comme {{TitleProperty|Attachment}}, {{TitleProperty|Box}}, {{TitleProperty|Draft}}, etc.



### Vues


{{TitleProperty|Link}}

-    {{PropertyView/fr|Draw Style|Enumeration}}: il vaut par défaut {{Value|None}}; il peut s\'agir de {{value|Solid}}, {{value|Dashed}}, {{value|Dotted}}, {{value|Dashdot}}; définit le style des arêtes dans la [Vue 3D](3D_view/fr.md).

-    {{PropertyView/fr|Line Width|FloatConstraint}}: un flotteur qui détermine la largeur en pixels des bords dans la [Vue 3D](3D_view/fr.md). La valeur par défaut est {{value|2.0}}.

-    {{PropertyView/fr|Override Material|Bool}}: la valeur par défaut est `False`; s\'il est défini sur `True`, il remplacera le matériau de **Linked Object** et affichera les couleurs définies dans {{PropertyView/fr|Shape Material}}.

-    {{PropertyView/fr|Point Size|FloatConstraint}}: similaire à {{PropertyView/fr|Line Width}}, définit la taille des sommets.

-    {{PropertyView/fr|Selectable|Bool}}: s\'il est `True`, l\'objet peut être sélectionné avec le pointeur dans la [Vue 3D](3D_view/fr.md). Sinon, l\'objet ne peut pas être sélectionné tant que cette option n\'est pas définie sur `True`.

-    {{PropertyView/fr|Shape Material|Material}}: cette propriété comprend des sous-propriétés qui décrivent l\'apparence de l\'objet.

    -   
        {{PropertyView/fr|Diffuse Color}}
        
        , la valeur par défaut est  light blue ..

    -   
        {{PropertyView/fr|Ambient Color}}
        
        , la valeur par défaut est  dark gray .

    -   
        {{PropertyView/fr|Specular Color}}
        
        , la valeur par défaut est  black .

    -   
        {{PropertyView/fr|Emissive Color}}
        
        , la valeur par défaut est  black .

    -   
        {{PropertyView/fr|Shininess}}
        
        , la valeur par défaut est {{Value|0.2}}

    -   
        {{PropertyView/fr|Transparency}}
        
        , la valeur par défaut est {{Value|0.0}}.


{{TitleProperty|Base}}

-    {{PropertyView/fr|Child View Provider|PersistentObject|Hidden}}:

-    {{PropertyView/fr|Material List|MaterialList|Hidden}}: **(lecture seulement)** si des matériaux individuels ont été ajoutés, ils seront listés ici.

-    {{PropertyView/fr|Override Color List|ColorList|Hidden}}: **(lecture seulement)** si les faces ou arêtes individuelles du lien ont été remplacées, elles seront listées ici.

-    {{PropertyView/fr|Override Material List|BoolList|Hidden}}: **(lecture seulement)** si les différents matériaux du lien ont été remplacés, ils seront listés ici.


{{TitleProperty|Options d'affichage}}

-    {{PropertyView/fr|Display Mode|Enumeration}}: {{Value|'Link'}} ou {{Value|'ChildView'}}.

-    {{PropertyView/fr|Show In Tree|Bool}}: voir les informations dans [App FeaturePython](App_FeaturePython/fr.md).

-    {{PropertyView/fr|Visibility|Bool}}: voir les informations dans [App FeaturePython](App_FeaturePython/fr.md).


{{TitleProperty|Selection}}

-    {{PropertyView/fr|On Top When Selected|Enumeration}}: voir les informations dans [App FeaturePython](App_FeaturePython/fr.md).

-    {{PropertyView/fr|Selection Style|Enumeration}}: voir les informations dans [App FeaturePython](App_FeaturePython/fr.md).

Il montrera en outre les propriétés de vue de l\'original **Linked Object**.



## Héritage

Un [App Link](App_Link/fr.md) est formellement une instance de la classe `App::Link`, dont le parent est le [App DocumentObject](App_DocumentObject/fr.md) (classe `App::DocumentObject`). C\'est un objet de très bas niveau, qui peut être utilisé avec la plupart des autres objets de document.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Schéma simplifié des relations entre les objets principaux du programme. L'objet `App::Link* est un composant central du système, il ne dépend d'aucun atelier, mais il peut être utilisé avec la plupart des objets créés dans tous les ateliers.`



## Script


**Voir aussi :**

[Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md) et [Objets créés par script](Scripted_objects/fr.md).

Voir [Part Feature](Part_Feature/fr.md) pour plus d\'informations.

Un lien d\'application est créé avec la méthode `addObject()` du document. Il peut définir son {{PropertyData/fr|Linked Object}} en remplaçant son attribut `LinkedObject`, ou en utilisant sa méthode `setLink`. 
```python
import FreeCAD as App

doc = App.newDocument()
bod1 = App.ActiveDocument.addObject("Part::Box", "Box")
bod2 = App.ActiveDocument.addObject("Part::Cylinder", "Cylinder")
bod1.Placement.Base = App.Vector(10, 0, 0)
bod2.Placement.Base = App.Vector(0, 10, 0)

obj1 = App.ActiveDocument.addObject("App::Link", "Link")
obj2 = App.ActiveDocument.addObject("App::Link", "Link")

obj1.LinkedObject = bod1
obj2.setLink(bod2)
obj1.Placement.Base = App.Vector(-10, -10, 0)
obj2.Placement.Base = App.Vector(10, -10, 0)
obj1.ViewObject.OverrideMaterial = True
App.ActiveDocument.recompute()
```

Le `App::Link` de base n\'a pas d\'objet Proxy, il ne peut donc pas être entièrement utilisé pour la sous-classification.

Par conséquent, pour la sous-classification [Python](Python/fr.md), vous devez créer l\'objet `App::LinkPython`.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::LinkPython", "Link")
obj.Label = "Custom label"
```



## Lecture complémentaire 

L\'objet [App Link](App_Link/fr.md) a été introduit après 2 ans de développement et de prototypage. Ce composant a été pensé et développé presque seul par l\'utilisateur **realthunder**. Les motivations et les implémentations de conception derrière ce projet sont décrites dans sa page GitHub, [Link](https://github.com/realthunder/FreeCAD_assembly3/wiki/Link). Afin d\'accomplir cette fonctionnalité, plusieurs modifications fondamentales de FreeCAD ont été apportées; ceux-ci ont également été largement documentés dans [Core-Changes](https://github.com/realthunder/FreeCAD_assembly3/wiki/Core-Changes).

Le projet App Link a démarré après que la refonte de l\'[atelier PartDesign](PartDesign_Workbench/fr.md) s\'est terminée dans la v0.17. L\'histoire d\'App Link peut être retracée à certains fils de discussion essentiels du forum :

-   [Pourquoi un objet ne peut être que dans un seul App::Part?](https://forum.freecadweb.org/viewtopic.php?f=19&t=21505) (mars 2017)
-   [Présentation de App::Link/XLink](https://forum.freecadweb.org/viewtopic.php?f=10&t=21586) (mars 2017)
-   [Liens](https://forum.freecadweb.org/viewtopic.php?f=20&t=22216) (mai 2017)
-   [Implémentation de Realthunder Link: discussion sur l\'architecture](https://forum.freecadweb.org/viewtopic.php?f=20&t=23015) (juin 2017)
-   [PR \# 876: Lien, première étape, sélection sensible au contexte](https://forum.freecadweb.org/viewtopic.php?f=17&t=23419) (juillet 2017)
-   [Preview: Link, stage two, API groundwork](https://forum.freecadweb.org/viewtopic.php?f=17&t=23626) (juillet 2017)
-   [Aperçu Assembly3](https://forum.freecadweb.org/viewtopic.php?f=20&t=25712) (décembre 2017)
-   [Fusion de ma branche Link](https://forum.freecadweb.org/viewtopic.php?f=10&t=29542) (juin 2018)

Enfin, le pull request et le merge ont eu lieu :

-   [App::Link: the big merge](https://forum.freecadweb.org/viewtopic.php?f=27&t=38621), ancien fil de discussion (juillet 2019), [pull request #2350](https://github.com/FreeCAD/FreeCAD/pull/2350) (the BIG merge), [LinkMerge branch](https://github.com/realthunder/FreeCAD/tree/LinkMerge).
-   [App::Link: the big merge](https://forum.freecadweb.org/viewtopic.php?f=8&t=37757), fil de discussion principal (juillet 2019)
-   [A simple path description of Link, 019, Link stage, Asm3, merge?](https://forum.freecadweb.org/viewtopic.php?p=329054#p329054) (août 2019)
-   [PR#2559: expose link and navigation actions](https://forum.freecadweb.org/viewtopic.php?f=17&t=39672), une introduction à la fonctionnalité Lien dans la version 0.19 (septembre 2019).

D\'autres \"liens\" divers à propos de Link incluent :

-   [Dynamic linked object](Dynamic_linked_object.md) - Un schéma avec Link et assemblys qui vise à réduire la duplication de la logique associée à l\'assemblage telle que l\'orientation, le positionnement ou le nombre d\'instances.





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std LinkMake/fr
