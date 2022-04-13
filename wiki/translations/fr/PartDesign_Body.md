---
- GuiCommand:/fr
   Name:PartDesign Body
   Name/fr:PartDesign Corps
   MenuLocation:Part Design → Créer un corps
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
   Version:0.17
   SeeAlso:[Std Part](Std_Part/fr.md), [Édition de fonctions](Feature_editing/fr.md)
---

# PartDesign Body/fr

## Description

Un [PartDesign Corps (Body)](PartDesign_Body/fr.md) est l\'élément de base pour créer des formes solides avec l\'[atelier PartDesign](PartDesign_Workbench/fr.md). Il peut contenir des [esquisses](Sketch/fr.md), des [objets Datum](Datum/fr.md) et des [PartDesign Fonctions (Features)](PartDesign_Feature/fr.md) afin de produire un [simple solide contigu](PartDesign_Body/fr#Solide_contigu_unique.md).

Le Corps fournit un objet **Origine** qui comprend les axes X, Y, Z, et les plans standards. Ces éléments peuvent être utilisés comme références pour ancrer des [esquisses](Sketch/fr.md) et des [objets primitifs](PartDesign_CompPrimitiveAdditive/fr.md).

Ne pas confondre le <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [PartDesign Corps (Body)](PartDesign_Body/fr.md) avec le <img alt="" src=images/Std_Part.svg  style="width:24px;"> [Std Part](Std_Part/fr.md). Le premier est un objet spécifique utilisé dans l\'<img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Atelier PartDesign](PartDesign_Workbench/fr.md), destiné à modéliser un [simple solide contigu](PartDesign_Body/fr#Solide_contigu_unique.md) au moyen de [PartDesign Fonctionnalités](PartDesign_Feature/fr.md). [Std Part](Std_Part/fr.md) est un objet de regroupement destiné à créer des [assemblages](assembly/fr.md). Il n\'est pas utilisé pour la modélisation, juste pour organiser différents objets dans l\'espace. Plusieurs corps et d\'autres [Std Parts](Std_Part/fr.md) peuvent être placés à l\'intérieur d\'un seul [Std Part](Std_Part/fr.md) pour créer un assemblage complexe.

![](images/PartDesign_Body_tree.png ) ![](images/PartDesign_Body_example.png ) 
*A gauche: l'arborescence montrant les entités qui produisent séquentiellement la forme finale de l'objet. A droite: l'objet définitif visible dans la [Vue 3D](3D_view/fr.md).*

## Utilisation

Si aucun solide précédent n\'est sélectionné:

1.  Appuyez sur le bouton **<img src="images/PartDesign_Body.svg" width=16px> [Créer un corps](PartDesign_Body/fr.md)**. Le nouveau corps est créé et devient automatiquement **[actif](PartDesign_Body/fr#Statut_actif.md)**.
2.  Vous pouvez maintenant appuyer sur **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [PartDesign Créer une esquisse ](PartDesign_NewSketch/fr.md)** pour créer une [esquisse](Sketch/fr.md) dans le corps qui peut être utilisée avec **[<img src=images/_PartDesign_Pad.svg style="width:16px"> [PartDesign Protusion](PartDesign_Pad/fr.md)**.
3.  Alternativement, vous pouvez ajouter une [PartDesign Fonction](PartDesign_Feature/fr.md), par exemple un **[<img src=images/_PartDesign_AdditiveBox.svg style="width:16px"> [PartDesign Cube additif](PartDesign_AdditiveBox/fr.md)**.

Si un objet solide est sélectionné:

1.  Appuyez sur le bouton **<img src="images/PartDesign_Body.svg" width=16px> [Créer un corps](PartDesign_Body/fr.md)**. Un nouveau corps est créé contenant une seule **Base Feature**. Cet élément Fonction de base (Base Feature) est une simple référence à un autre objet précédemment créé ou importé dans le document. Voir [Fonction de base](PartDesign_Body/fr#Fonction_de_base.md) pour plus d\'informations. Un Corps existant ou une [PartDesign Fonction](PartDesign_Feature/fr.md) ne peut pas être sélectionné lorsque vous appuyez sur le **<img src="images/PartDesign_Body.svg" width=16px> [Créer un corps](PartDesign_Body/fr.md)**.

### Remarques

-   Si aucun corps n\'existe au moment où une **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [PartDesign Esquisse](PartDesign_NewSketch/fr.md)** est sélectionnée, un nouveau Corps sera automatiquement créé. Si un corps existe déjà, il doit être rendu actif avant d\'utiliser **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [PartDesign Créer une esquisse](PartDesign_NewSketch/fr.md)**.
-   Double-cliquez sur le Corps dans la [Vue en arborescence](Tree_view/fr.md) du modèle ou ouvrez le menu contextuel (clic droit) et sélectionnez **Toggle active body** pour activer ou désactiver le Corps. Si un autre Corps est déjà actif, il sera automatiquement désactivé. Voir [statut actif](PartDesign_Body/fr#Statut_actif.md) pour plus d\'informations.

## Propriétés

Un [PartDesign Corps](PartDesign_Body/fr.md) (classe `PartDesign::Body`) est dérivé d\'une [Part Fonctionnalité](Part_Feature/fr.md) (classe `Part::Feature`), par conséquent il partage toutes les propriétés de ce dernier.

Outre les propriétés décrites dans [Part Fonctionnalité](Part_Feature/fr.md), le PartDesign Corps a les propriétés suivantes dans l\'[Éditeur de propriétés](Property_editor/fr.md).

### Données


{{TitleProperty|Base}}

-    **Tip|Link**: [PartDesign Fonction](PartDesign_Feature/fr.md) définie sur \"Tip\" est généralement la dernière fonction créée dans le Corps. Tip indique la forme finale du Corps qui est affichée dans la [Vue 3D](3D_view/fr.md) lorsque **Display Mode Body** est défini sur `Tip`. Voir [Tip](PartDesign_Body/fr#Tip.md) pour plus d\'informations.

-    **Base Feature|Link**: forme externe utilisée comme première [PartDesign Fonction](PartDesign_Feature/fr.md) dans le Corps. Il est généralement défini lorsque vous faites glisser un objet solide dans un Corps vide. Si aucun solide n\'est importé de cette manière, cette propriété sera vide. Voir [Base Feature](PartDesign_Body/fr#Base_Feature.md) pour plus d\'informations.

-    **Placement|Placement**: position de l\'objet dans la [Vue 3D](3D_view/fr.md). Le placement est défini par un point `Base` (vecteur) et une `Rotation` (axe et angle). Voir [Positionnement](Placement/fr.md).

-    **Group|LinkList**: une liste avec les [PartDesign Fonctions](PartDesign_Feature/fr.md) dans le Corps.

##### Propriétés cachées de Données 

-    **Origin|Link**: l\'objet [App Origin](App_Origin/fr.md) est la référence de position pour tous les éléments répertoriés dans **Group**.

-    **_ Group Touched|Bool**: si le groupe est coché ou non.

Aussi les propriétés cachées décrites dans [Part Fonction](Part_Feature/fr.md).

### Vue


{{TitleProperty|Base}}

-    **Display Mode Body|Enumeration**: définit le mode d\'affichage spécifiquement pour le Corps avec l\'un des deux types.

    -   
        `Through`
        
        (à travers) valeur par défaut, affiche tous les objets à l\'intérieur du Corps, c\'est-à-dire les [esquisses](Sketch/fr.md), [PartDesign Fonctions](PartDesign_Feature/fr.md), les objets de référence (datum), etc\... Ce mode permet de visualiser les opérations partielles effectuées à l\'intérieur du Corps et c\'est donc le mode recommandé lors de l\'ajout et de la modification de fonctions. Sélectionnez la fonction spécifique et définissez **Visibility** sur `True` ou appuyez sur la **Barre d'espace** du clavier.

    -   
        `Tip`
        
        affiche uniquement la forme finale du corps, qui est définie par la propriété **Tip**. Tout le reste, y compris les [esquisses](Sketch/fr.md), les [PartDesign Fonctions](PartDesign_Feature/fr.md), les références, etc\... ne sont pas affichées même s\'elles sont visibles dans la [Vue en arborescence](Tree_view/fr.md). Ce mode est recommandé lorsque le Corps n\'a pas besoin d\'être modifié davantage, aussi une forme fixe est affichée. Ce mode est également recommandé lorsque vous souhaitez sélectionner les sous-éléments (sommets, arêtes et faces) de la forme finale à utiliser avec d\'autres outils d\'ateliers.

## Conception du Corps 

### Solide contigu unique 

Un PartDesign Corps est destiné à modéliser un solide contigu unique. Le sens de \"contigu\" est un élément fait d\'une seule pièce, sans pièces mobiles ou solides déconnectés. Des exemples de solides contigus sont ceux qui sont fabriqués à partir d\'une seule pièce de matière première par un procédé de coulée, de découpe ou de fraisage. Par exemple, un écrou, une rondelle et un boulon se compose chacun d\'une seule pièce solide en métal, sans pièces mobiles, de sorte que chacun peut être modélisé par un PartDesign Corps. Les objets créés en soudant deux pièces peuvent également être modélisés par un seul Corps tant que le joint de soudure est solide et non destiné à être cassé.

Une fois que ces solides contigus sont rassemblés dans un certain type d\'arrangement, ils deviennent alors un \"assemblage\". Dans un assemblage, les objets ne sont pas fusionnés, mais simplement \"empilés\" ou placés côte à côte et restent des objets individuels.

<img alt="" src=images/PartDesign_Body_contiguous_separate.png  style="width:" height="200px;"> <img alt="" src=images/PartDesign_Body_contiguous_assembly.png  style="width:" height="200px;"> 
*À gauche: trois solides contigus individuels, chacun modélisé par un PartDesign Corps. À droite: les différents Corps (Body) réunis en un assemblage.*

### Modification des fonctionnalités 

Un PartDesign Corps est conçu pour fonctionner en créant un solide initial, soit à partir d\'une [esquisse](Sketch/fr.md) soit à partir d\'une forme [primitive](PartDesign_CompPrimitiveAdditive/fr.md), puis en la modifiant par le biais de [\"fonctions\"](PartDesign_Feature/fr.md) pour ajouter ou enlever de la matière de la forme précédente. Pour une explication complète, voir [Édition de fonctions](feature_editing/fr.md).

Un PartDesign Corps effectuera une [union](Part_Fuse/fr.md) automatique des éléments solides à l\'intérieur de celui-ci. Cela signifie que (1) les solides partiels doivent être en contact et (2) que les solides déconnectés ne sont pas autorisés.

<img alt="" src=images/PartDesign_Body_two_intersection.png  style="width:" height="200px;"> <img alt="" src=images/PartDesign_Body_two_fusion.png  style="width:" height="200px;"> 
*À gauche: deux solides individuels qui se coupent. À droite: un PartDesign Corps unique avec deux [fonctions additives](PartDesign_Feature/fr.md). Elles sont automatiquement fusionnées ensemble, donc au lieu de se recouper, elles forment un solide contigu unique.*

![](images/PartDesign_Body_non-contiguous.png ) 
*À gauche: deux solides déconnectés. Ce n'est pas un PartDesign Corps valide. À droite: deux solides se touchant. Cela se traduit par un PartDesign Corps valide. La nouvelle [fonction](PartDesign_Feature/fr.md) doit toujours entrer en contact avec la fonction précédente ou l'intersecter afin qu'elle lui soit fusionnée et devienne un solide contigu unique.*


**Remarque:**

d\'autres programmes de CAO comme Catia autorisent les solides non contigus dans le même \"Corps\". Jusqu\'à la v0.19, FreeCAD ne le permet toujours pas. Il y a eu des discussions sur le [FreeCAD forum](https://forum.freecadweb.org/index.php) sur la levée de cette restriction, mais aucune décision concrète n\'a été prise. Si vous souhaitez en savoir plus ou présenter différents points de vue, veuillez en discuter dans le [forum](https://forum.freecadweb.org/index.php).

## Explication détaillée des propriétés 

### Statut actif 

Un document ouvert peut contenir plusieurs Corps. Pour ajouter une nouvelle fonctionnalité à un Corps spécifique, il doit être rendu **actif**. Un Corps actif sera affiché dans la [Vue en arborescence](Tree_view/fr.md) avec la couleur d\'arrière-plan spécifiée par la valeur **Active container** dans l\'[éditeur de préférences](Preferences_Editor/fr#Couleurs.md) (par défaut, bleu clair). le Corps actif sera également affiché en gras.

Pour activer ou désactiver un Corps:

-   Double-cliquez dessus dans la [Vue en arborescence](Tree_view/fr.md) ou
-   Ouvrez le menu contextuel (clic droit) et sélectionnez **Toggle active body** (Activer/Désactiver le corps).

L\'activation d\'un Corps bascule automatiquement vers l\'[atelier PartDesign](PartDesign_Workbench/fr.md). Un seul Corps ne peut être actif à la fois.

![](images/PartDesign_Body_active.png )



*Document avec deux PartDesign Corps dont le second est actif.*

### Origine

L\'Origine se compose des trois axes standard (X, Y, Z) et de trois plans standard (XY, XZ et YZ). Des [esquisses](Sketch/fr.md) et autres objets peuvent être attachés à ces éléments lors de leur création.

1.  Créez le Corps.
2.  Si le Corps (Body) est sélectionné dans la [Vue en arborescence](Tree_view/fr.md) lorsque le **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [Créer une esquisse](PartDesign_NewSketch/fr.md)** est enfoncé, le [Panneau des tâches](Task_panel/fr.md) s\'ouvrira pour permettre de sélectionner un des plans.
3.  Si le Corps n\'est pas sélectionné, sélectionnez l\'origine à la place et rendez-le visible dans la [Vue 3D](3D_view/fr.md) en appuyant sur la barre **Espace** du clavier. Développez également l\'objet Origin pour voir les axes et les plans.
4.  Sélectionnez un des plans, soit dans la [Vue en arborescence](Tree_view/fr.md) soit dans la [Vue 3D](3D_view/fr.md), puis appuyez sur **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [Créer une esquisse](PartDesign_NewSketch/fr.md)**. L\'esquisse sera créée sur le plan choisi.

Le même processus peut être utilisé lors de la création d\'une géométrie de référence auxiliaire comme des [PartDesign Lignes](PartDesign_Line/fr.md), [PartDesign Plans](PartDesign_Plane/fr.md) et [PartDesign Systèmes de coordonnées](PartDesign_CoordinateSystem/fr.md).


**Remarque:**

L\'Origine est un objet [App Origin](App_Origin/fr.md) (classe `App::Origin`) tandis que les axes et les plans sont respectivement des objets de type `App::Line` et `App::Plane`. Chacun de ces éléments peut être masqué et non masqué individuellement avec la barre **Espace**. Cela est utile pour choisir la référence correcte lors de la création d\'autres objets.


**Remarque 2:**

tous les éléments à l\'intérieur du Corps sont référencés à l\'Origine du Corps, ce qui signifie que le Corps peut être déplacé et tourné en référence au système de coordonnées global sans affecter le placement des éléments à l\'intérieur.

<img alt="" src=images/PartDesign_Body_Origin_tree.png ) ![](images/PartDesign_Body_Origin_view.png  style="width:" height="400px;">



*A gauche: PartDesign Origin du Corps dans la [Vue en arborescence](Tree_view/fr.md) et telle qu'elle apparaît affichée dans la [Vue 3D](3D_view/fr.md). A droite: représentation des éléments Origin dans la [Vue 3D](3D_view/fr.md).*

### Base Feature 

La Base Feature (fonction de base) est la première [PartDesign Fonction](PartDesign_Feature/fr.md) dans le Corps quand le Corps est basé sur une autre forme solide. Ce solide peut être créé par n\'importe quel atelier ou importé à partir d\'un fichier externe, par exemple un fichier STEP.

![](images/PartDesign_Body_BaseFeature_tree.png ) 
*Deux PartDesign Corps, chacun avec une seule Base Feature qui est prises des solides créés précédemment.*

Pour créer la fonction de base:

1.  sélectionner une forme solide externe à n\'importe quel Corps et
2.  appuyez sur **[<img src=images/PartDesign_Body.svg style="width:16px"> [Créer un Corps](PartDesign_Body/fr.md)**. Cela créera un nouveau Corps avec une seule Base Feature.


**Remarque:**

vous ne pouvez pas sélectionner un Corps existant ou l\'une de ses [fonctions](PartDesign_Feature/fr.md) lorsque vous appuyez sur **[<img src=images/PartDesign_Body.svg style="width:16px"> [Créer un corps](PartDesign_Body/fr.md)**.

Si vous avez déjà un Corps, vous pouvez créer la fonction de base de cette manière :

-   dans la [Vue en arborescence](Tree_view/fr.md), choisissez un objet et faites-le glisser à l\'intérieur du Corps, ou
-   dans l\'[Éditeur de propriétés](Property_editor/fr.md), modifiez la valeur de la **Base Feature** en appuyant sur la touche points de suspension **...** et en choisissant un objet dans la liste. Dans ce cas, vous pouvez choisir un Corps existant pour être la Base Feature.


**Remarque :**

le glisser-déposer ne fonctionne que pour les Corps qui n\'ont pas encore de fonction de base (Base Feature).


**Remarque 2 :**

si le Corps possède déjà plusieurs fonctions, lorsque vous faites glisser et déposez le solide externe, la fonction de base sera créée au début de la liste des fonctions, c\'est-à-dire qu\'elle sera ajoutée au début de la propriété **Group**.

La fonction de base (Base Feature) est entièrement facultative. Elle n\'est présente que lors de l\'inclusion d\'un objet extérieur au Corps. Si aucun solide externe n\'est inclus, vous pouvez toujours créer votre forme à l\'aide d\'[Esquisses](Sketch/fr.md), de [Protrusions](PartDesign_Pad/fr.md), de [Primitives additives](PartDesign_CompPrimitiveAdditive/fr.md) et d\'autres [PartDesign Fonctions](PartDesign_Feature/fr.md). Dans ce cas, la propriété **Base Feature** reste vide.

![](images/PartDesign_Body_BaseFeature_Tip.svg )



*A gauche:un PartDesign Corps avec une fonction de base issue d'un objet solide externe et de nombreuses [PartDesign Fonctions](PartDesign_Feature/fr.md) ultérieures en haut. A droite: un Corps qui n'a pas de fonction de base explicite (Base Feature).*


**Remarque :**

Si un autre PartDesign Corps est sélectionné comme BaseFeature, il doit avoir une forme. S\'il est vide (pas de caractéristiques, pas de BaseFeature, \...), il en résultera une erreur.

### Tip (fonction résultante) 

Le Tip (fonction résultante) est une [PartDesign Fonction](PartDesign_Feature/fr.md) qui est exposée à l\'extérieur du Corps, c\'est-à-dire que si un autre outil de n\'importe quel atelier (par exemple, **[<img src=images/Part_SimpleCopy.svg style="width:16px"> [Part Copie simple](Part_SimpleCopy/fr.md)** ou **[<img src=images/Part_Cut.svg style="width:16px"> [Part Soustraction](Part_Cut/fr.md)**) doit utiliser la forme du Corps, il utilisera la forme du Tip. Autrement dit, le Tip est la représentation finale du Corps comme si l\'historique paramétrique n\'existait pas.

![](images/PartDesign_Body_Tip_final.svg )



*A gauche: un PartDesign Corps avec l'historique paramétrique complet incluant les fonctions intermédiaires. À droite: le Tip est la forme finale qui peut être exportée à partir du Corps, tout en omettant l'historique du modèle.*

Le Tip est automatiquement définie sur la dernière fonction créée dans le Corps. Néanmoins, il peut également être défini sur l\'une des fonctionnalités intermédiaires en ouvrant le menu contextuel de la [Vue en arborescence](Tree_view/fr.md) (clic droit) et en choisissant **[<img src=images/PartDesign_MoveTip.svg style="width:16px"> [Désigner comme fonction résultante](PartDesign_MoveTip/fr.md)** ou en modifiant la valeur **Tip** du Corps dans l\'[Éditeur de propriétés](Property_editor/fr.md).

Le fait de modifier le Tip permet en effet de revenir en arrière et d\'ajouter des fonctionnalités qui auraient dû être ajoutées plus tôt. Cela expose également une forme différente aux outils externes.

Dans la [Vue en arborescence](Tree_view/fr.md), le Tip du Corps est reconnue par la [PartDesign Fonction](PartDesign_Feature/fr.md) qui a une superposition d\'icônes consistant en une flèche blanche à l\'intérieur d\'un cercle vert.

![](images/PartDesign_Body_Tip_tree.png ) 
*Deux PartDesign Corps, chacun avec des [PartDesign Fonctions](PartDesign_Feature/fr.md). Le Tip est la dernière fonction de celles-ci et est marqué par un symbole de superposition.*

### Interaction avec d\'autres ateliers 

Par défaut, des [PartDesign Fonctions](PartDesign_Feature/fr.md) à l\'intérieur d\'un Corps sont sélectionnables dans le but de modifier et d\'ajouter d\'autres fonctions avec les outils de l\'[atelier PartDesign](PartDesign_Workbench/fr.md). Néanmoins, il n\'est pas conseillé de sélectionner les fonctions individuelles pour les utiliser avec des outils d\'autres ateliers, tels que l\'[atelier Part](Part_Workbench/fr.md) et l\'[atelier Draft](Draft_Workbench/fr.md), des résultats inattendus peuvent apparaitre. Si cela est fait, dans la [Vue rapport](Report_view/fr.md), un message d\'erreur peut apparaître, **Links go out of the allowed scope** (Les liens sortent du champ d\'application autorisé).

Par conséquent, pour les interactions avec d\'autres ateliers, seul le Corps lui-même doit être sélectionné dans la [Vue en arborescence](Tree_view/fr.md). Dans les cas où il est nécessaire de sélectionner des sous-éléments spécifiques du Corps (sommets, arêtes et faces), la propriété **Display Mode Body** du Corps doit être basculée sur `Tip`. Lorsque ce mode est activé, l\'accès aux objets sous le Corps ([PartDesign Fonctions](PartDesign_Feature/fr.md), les références (datum), [esquisses](Sketch/fr.md)) sont désactivées et tout sauf le [Tip](PartDesign_Body/fr#Tip_.28fonction_r.C3.A9sultante.29.md) du Corps sera caché dans la [Vue 3D](3D_view/fr.md).

Une fois que les sous-éléments ont été utilisés avec d\'autres ateliers, la **Display Mode Body** peut être redéfinie sur `Through`.

![](images/PartDesign_Body_Tip_Display_mode.svg )



*A gauche: lorsque "Display Mode Body" est réglé sur `Through*, il est possible de sélectionner et d'effectuer des opérations avec la [PartDesign Fonction](PartDesign_Feature/fr.md); en général, ce n'est pas recommandé. A droite: lorsque "Display Mode Body" est réglé sur {{incode|Tip` toutes les sélections et opérations effectuées sur le Corps seront effectuées sur le Tip, en s'assurant que seule la forme finale du Corps est exposée.}}

### Gestion de la visibilité 

La visibilité du Corps remplace la visibilité de tout objet qu\'il contient. Si le Corps est masqué, les objets qu\'il contient seront également masqués, même si leur propriété individuelle **Visibility** est définie sur `True`.

Plusieurs [Esquisses](Sketch/fr.md) peuvent être visibles à la fois mais une seule [PartDesign Fonction](PartDesign_Feature/fr.md) (résultat solide) peut être visible à la fois. Sélectionner une fonction cachée et appuyer sur la barre **Espace** du clavier la rendra visible et masquera automatiquement la fonction précédemment visible.

![](images/PartDesign_Body_Visibility.png ) 
*PartDesign Corps: plusieurs [Esquisses](Sketch/fr.md) peuvent être visibles simultanément, mais une seule [PartDesign Fonction](PartDesign_Feature/fr.md) peut être visible à la fois, que ce soit le Tip ou non.*

### Ancrage

Les [PartDesign Fonctions](PartDesign_Feature.md), tout comme les [objets planaires](Part_Part2DObject/fr.md), peuvent être ancrées à différents plans, généralement les plans standard définis par l\'[Origine](PartDesign_Body/fr#Origine.md) du Corps ou à des [PartDesign Plans de référence](PartDesign_Plane/fr.md) personnalisés.

Les [esquisses](Sketch/fr.md) sont normalement ancrées à un plan lors de leur création. De la même manière, les [PartDesign Primitives additives](PartDesign_CompPrimitiveAdditive/fr.md) peuvent également être ancrées. Ancrer ces objets à un plan permet de les déplacer dans le Corps en modifiant leur propriété **Attachment Offset**. Pour plus d\'informations sur les modes d\'ancrage, voir [Part Ancrage](Part_EditAttachment/fr.md).

Une [PartDesign Fonction](PartDesign_Feature/fr.md) qui n\'est pas ancrée sera affichée avec un symbole de superposition rouge à côté de son icône dans la [Vue en arborescence](Tree_view/fr.md).

![](images/PartDesign_Body_Feature_attachment.png ) 
*PartDesign Corps: les [PartDesign Fonctions](PartDesign_Feature/fr.md) qui ne sont pas ancrées à un plan ou à un système de coordonnées seront affichées avec un symbole de superposition à côté de leur icône dans la [Vue en arborescence](Tree_view/fr.md).*

### Héritage

Un [PartDesign Corps](PartDesign_Body/fr.md) est formellement une instance de la classe `PartDesign::Body`, dont le parent est une [Part Fonction](Part_Feature/fr.md) (classe `Part::Feature`) via la classe intermédiaire `Part::BodyBase` et est complétée par une extension Origin.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Diagramme simplifié des relations entre les objets centraux du programme. L'objet `PartDesign::Body* est destiné à construire des solides 3D paramétriques et est donc dérivé de l'objet de base {{incode|Part::Feature`. Il possède une Origine pour contrôler le placement des fonctionnalités utilisées à l'intérieur.}}

## Script


**Voir aussi:**

[Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md) et [Objets créés par script](scripted_objects/fr.md).

Voir [Part Fonction](Part_Feature/fr.md) pour plus d\'informations à propos de l\'ajout d\'objets au document.

Un PartDesign Corps (Body) est créé avec la méthode `addObject()` du document. Une fois qu\'un Corps existe, des [PartDesign Fonctions](PartDesign_Feature/fr.md), comme les primitives additives et soustractives, peuvent être ajoutées et attachées à ce Corps avec les méthodes `addObject()` ou `addObjects()` de ce Corps.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("PartDesign::Body", "Body")
obj.Label = "Custom label"

feat1 = App.ActiveDocument.addObject("PartDesign::AdditiveBox", "Box")
feat2 = App.ActiveDocument.addObject("PartDesign::AdditiveCylinder", "Cylinder")

obj.addObjects([feat1, feat2])
App.ActiveDocument.recompute()
```

Dans un document contenant plusieurs Corps, le [Corps actif](PartDesign_Body/fr#Statut_actif.md) peut être défini par la méthode `setActiveObject` de la `ActiveView`. Le premier argument est la chaîne fixe `"pdbody"` et le deuxième argument est l\'objet Corps (Body) qui doit être activé. 
```python
import FreeCAD as App
import FreeCADGui as Gui

doc = App.newDocument()
obj1 = App.ActiveDocument.addObject("PartDesign::Body", "Body")
obj2 = App.ActiveDocument.addObject("PartDesign::Body", "Body")

Gui.ActiveDocument.ActiveView.setActiveObject("pdbody", obj1)
App.ActiveDocument.recompute()
```





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Body/fr
