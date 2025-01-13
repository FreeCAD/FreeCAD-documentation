---
 GuiCommand:
   Name: PartDesign SubShapeBinder
   Name/fr: PartDesign Sous forme liée
   MenuLocation: PartDesign , Créer une forme liée du/des sous-objet
   Workbenches: PartDesign_Workbench/fr
   Version: 0.19
   SeeAlso: PartDesign_Clone/fr
---

# PartDesign SubShapeBinder/fr

## Description

L\'outil **PartDesign Sous forme liée** crée un liant de forme référençant la géométrie d\'un ou plusieurs objets parents. Une Sous forme liée est généralement utilisée à l\'intérieur d\'un [PartDesign Corps](PartDesign_Body/fr.md) pour référencer une géométrie extérieure au corps. L\'utilisation d\'une géométrie externe directement dans un corps n\'est pas autorisée et entraînera des erreurs hors champ. Mais une Sous forme liée peut également être utilisé sans être imbriqué dans un corps.

Une Sous forme liée suivra le placement relatif de la géométrie référencée, ce qui est utile dans le contexte de la création d\'un [assemblage](Assembly/fr.md), mais en plus de cela, elle a aussi son propre placement.

La géométrie référencée peut être constituée d\'un ou de plusieurs éléments. Chaque élément peut être un objet individuel (par exemple un [PartDesign Corps](PartDesign_Body/fr.md)), un sous-objet (par exemple une [Part Cube](Part_Box/fr.md) à l\'intérieur d\'une [Std Part](Std_Part/fr.md), ou une [esquisse](PartDesign_NewSketch/fr.md) ou [fonction](PartDesign_Feature/fr.md) à l\'intérieur d\'un corps), ou un sous-élément (une face, un bord ou un sommet). Le choix de la géométrie à sélectionner dépend de l\'utilisation prévue d\'une Sous forme liée. Pour une opération booléenne, vous devrez sélectionner un solide. Pour une opération de [Protrusion](PartDesign_Pad/fr.md), on peut utiliser une face, une esquisse ou un fil plan. Et pour la [géométrie externe](Sketcher_External/fr.md) dans une esquisse, ou pour attacher une esquisse, toute combinaison de sous-éléments peut être appropriée. Les éléments peuvent appartenir à différents objets parents, et peuvent même appartenir au corps dans lequel la Sous forme liée est imbriqué. Étant donné qu\'une Sous forme liée est [basée sur les liens](Std_LinkMake/fr.md), la géométrie référencée peut également appartenir à un document externe.

<img alt="" src=images/PartDesign_SubShapeBinder_example_1.png  style="width:" height="300px;"> <img alt="" src=images/PartDesign_SubShapeBinder_example_2.png  style="width:" height="300px;"> 
*À gauche, deux solides créés dans deux [Corps](PartDesign_Body/fr.md) distincts.<br> A droite deux Sous formes liées référençant la géométrie du premier Corps, imbriqués dans le second corps, et déplacés à une position différente.*

<img alt="" src=images/PartDesign_SubShapeBinder_example_3.png  style="width:" height="300px;"> 
*Les deux Sous formes liées sont utilisées pour créer une [soustraction booléenne](PartDesign_Boolean/fr.md) et une [protrusion](PartDesign_Pad/fr.md) dans le deuxième corps.*



## Utilisation



### Même document 

1.  S\'il y a plusieurs corps dans le document : vous pouvez [activer le corps](PartDesign_Body/fr#Statut_actif.md) dans lequel la Sous forme liée doit être imbriquée.
2.  Sélectionnez la géométrie requise. Les sous-éléments ne peuvent être sélectionnés que dans la [vue 3D](3D_view/fr.md).
3.  Il existe plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/PartDesign_SubShapeBinder.svg" width=16px> [Créer une forme liée du/des sous-objet(s)](PartDesign_SubShapeBinder/fr.md)**.
    -   Sélectionnez l\'option **PartDesign → <img src="images/PartDesign_SubShapeBinder.svg" width=16px> Créer une forme liée du/des sous-objet(s)** du menu.
4.  La Sous forme liée est créée.
5.  S\'il n\'y a qu\'un seul corps dans le document, la Sous forme liée est automatiquement ajoutée à celui-ci et le corps est activé. Si c\'est le cas et que la Sous forme liée ne doit pas être imbriquée, elle peut être glissée hors du corps et déposée sur le nœud du document <img alt="" src=images/Document.svg  style="width:16px;"> dans la [vue en arborescence](Tree_view/fr.md).



### Document externe 

1.  Si nécessaire, ouvrez le document source (le document externe) et le document cible. Les deux documents doivent avoir été enregistrés au moins une fois.
2.  S\'il y a plusieurs corps dans le document cible : vous pouvez activer le corps dans lequel la Sous forme liée doit être imbriquée.
3.  Sélectionnez la géométrie requise dans le document source. Les sous-éléments ne peuvent être sélectionnés que dans la [vue 3D](3D_view/fr.md).
4.  Passez au document cible en cliquant sur son onglet dans la [zone de vue principale](Main_view_area/fr.md).
5.  Lancez l\'outil comme décrit ci-dessus.



### Commencer avec une Sous forme liée vide 

1.  Suivez les instructions décrites dans [Même document](#M.C3.AAme_document.md) ci-dessus mais sans sélectionner de géométrie.
2.  Une Sous forme liée vide est créée.
3.  Sélectionnez la géométrie requise. Les sous-éléments ne peuvent être sélectionnés que dans la [vue 3D](3D_view/fr.md).
4.  Dans la [vue en arborescence](Tree_view/fr.md), faites glisser et déposez la sélection sur la Sous forme liée. Si vous avez sélectionné des sous-éléments, leurs objets parents sont mis en surbrillance dans la [vue en arborescence](Tree_view/fr.md), indiquant les objets à faire glisser.
5.  Vous pouvez ajouter d\'autres éléments géométriques de la même manière.
6.  Pour remplacer une géométrie déjà référencée, maintenez la touche **Ctrl** enfoncée pendant l\'opération de glisser-déposer.



## Remarques

-   Le décalage 2D est pris en charge pour certains types de formes, notamment les faces planes, les arêtes et les fils. Comme le décalage est une opération difficile pour le logiciel, il ne réussit pas toujours.
-   Une Sous forme liée qui n\'est pas imbriquée dans un corps peut être utilisé comme une [Base Feature](PartDesign_Body/fr#Base_Feature.md) pour un nouveau corps.
-   La propriété **Support** contient les liens vers la géométrie référencée. Par défaut, cette propriété est en lecture seule, mais elle peut être modifiée en suivant les instructions décrites dans la section [Commencer avec une Sous forme liée vide](#Commencer_avec_une_Sous_forme_li.C3.A9e_vide.md).
-   Une Sous forme liée créée à partir d\'une esquisse peut avoir une \" direction d\'outil \" opposée. Par exemple, une [protrusion](PartDesign_Pad/fr.md) créée à partir de l\'esquisse peut s\'étendre dans la direction +Y, tandis qu\'une [protrusion](PartDesign_Pad/fr.md), avec les mêmes propriétés, créée à partir d\'une Sous forme liée s\'étend dans la direction -Y. Le basculement de la propriété **Reversed** (ou de la case à cocher) résoudra ce problème.



## PartDesign Sous forme liée vs. PartDesign Forme liée 

Voir [PartDesign Forme liée](PartDesign_ShapeBinder/fr#PartDesign_Sous_forme_liée_vs._PartDesign_Forme_liée.md).



## Propriétés

Un objet PartDesign Sous forme liée est dérivé d\'un objet [Part Feature](Part_Feature/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :



### Données


{{TitleProperty|Base}}

-    **Support|XLinkSubList|hidden**: support de la géométrie.

-    **Fuse|Bool**: si `True`, fusionne les formes liées solides.

-    **Make Face|Bool**: si `True`, crée une face pour les polylignes liées.

-    **Claim Children|PropertyBool**: si `True`, les objets liés seront déclarés en tant qu\'enfants dans la [vue en arborescence](Tree_view/fr.md).

-    **Relative|Bool**: si `True`, permet d\'établir des liens relatifs entre les sous-objets.

-    **Bind Mode|Enumeration**: mode de liaison, {{value|Synchronized}}, {{Value|Frozen}}, {{Value|Detached}}.

-    **Partial Load|Bool**: si `True`, permet le chargement partiel des objets.

-    **Context|XLink|hidden**: objet conteneur de cet objet liant.

-    **Bind Copy On Change|Enumeration**
    

-    **Refine|Bool**: si `True`, les arêtes redondantes seront supprimées (par exemple après une opération booléenne).

-    **_ Version|Integer|hidden**: version de ce type d\'objet.

-    **_ Lien copié|XLinkSub|hidden**: version de ce type d\'objet.


{{TitleProperty|Cache}}

-    **Body|Matrix|hidden**: matrice d\'unité (propriété distincte pour chaque objet dans **Support**).


{{TitleProperty|Offsetting}}

-    **Offset**: décalage 2D à appliquer. Si Offset = 0, alors aucun décalage n\'est appliqué. Si Offset \< 0, alors le décalage est appliqué vers l\'intérieur.

-    **Offset Join Type**: méthode de jointure permettant de décaler les joints non tangents. La méthode peut être {{Value|Arcs}}, {{Value|Tangente}} ou {{Value|Intersection}}.

-    **Offset Fill|Bool**: si `True`, une face est créée entre la nouvelle polyligne et la polyligne d\'origine. Voir aussi la propriété **Make Face**.

-    **Offset Open Result|Bool**: affecte la façon dont les polylignes ouvertes sont traitées. Si `False`, une polyligne ouverte est réalisée. Si `True`, une polyligne fermée est créé à partir d\'un décalage de double face, avec des ronds autour des sommets ouverts.

-    **Offset Intersection|Bool**: affecte la façon dont les composés sont traités. Si `False`, tous les enfants sont traités indépendamment. Si `True`, et que les enfants sont des arêtes et des polylignes, les enfants sont décalés de manière collective.



### Vue


{{TitleProperty|Base}}

-    **Use Binder Style|Bool**: si mis à `True`, les couleurs de l\'objet liant dépendent du paramètre **DefaultDatumColor** du [réglage fin](Fine-tuning/fr#Atelier_PartDesign.md). si mis à `False`, les couleurs normales de la forme sont appliquées.



## Liens

-   Explication de l\'utilisation avec une vidéo [New Sublink Link Feature](https://forum.freecadweb.org/viewtopic.php?t=41450).





{{PartDesign_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubShapeBinder/fr
