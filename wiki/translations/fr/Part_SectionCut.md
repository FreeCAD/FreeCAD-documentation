---
 GuiCommand:
   Name: Part SectionCut
   Name/fr: Part Coupe persistante
   MenuLocation: Affichage , Coupe persistante
   Workbenches: Tous
   Version: 0.20
   SeeAlso: Std_ToggleClipPlane/fr
---

# Part SectionCut/fr

## Description

La fonction **Coupe persistante** est disponible pour tous les ateliers, mais elle ne fonctionne que pour les objets Part et PartDesign et leurs assemblages. Elle crée une coupe persistante des objets et des assemblages. Comme le résultat de la coupe est un objet ordinaire de <img alt="" src=images/Part_Cut.svg  style="width:24px;"> [Part Soustraction](Part_Cut/fr.md), il peut être modifié ultérieurement ou, par exemple, imprimé en 3D. Voir ci-dessous les applications possibles.

<img alt="" src=images/Part_SectionCut_example.png  style="width:300px;"> 
*Un assemblage de coupe. Certaines faces coupées ont été colorées manuellement.<br>La partie jaune n'est pas coupée car elle a été volontairement déplacée d'un micron dans une autre partie.*



## Utilisation

![La fenêtre de dialogue Coupe persistante](images/Part_SectionCut_Dialog.png )

La fenêtre de dialogue **Coupe persistante** s\'ouvre via le menu **Affichage → <img src="images/Part_SectionCut.svg" width=24px> Coupe persistante**. Elle est indépendante du plan de travail actuel et du document ouvert. Elle peut être détachée de sa position d\'ouverture en appuyant sur le bouton en haut à droite de la fenêtre de dialogue.

La fonction **Coupe persistante** prend en compte tous les objets Part visibles dans le document actif. Vous pouvez donc contrôler ce qui sera coupé, en rendant une partie visible ou non. En cochant l\'une des options **Coupe** dans la fenêtre de dialogue, la fonction est activée. Vous pouvez alors soit saisir une position (en coordonnées du document), soit utiliser les curseurs pour définir la position de la coupe. Il est également possible de combiner des coupes, par exemple pour couper dans les directions X et Z. Les boutons **Inverser** permettent de retourner le côté qui est coupé.

Dès que l\'option *Coupe* est cochée dans la boîte de dialogue, vous obtenez un objet coupé dans la [vue en arborescence](Tree_view/fr.md). Son nom est par exemple *Coupe en Y* lorsqu\'il s\'agit d\'une coupe dans la direction des ordonnées.

L\'option de dialogue **Garder uniquement les coupes visibles lors de la fermeture** cache tout dans la vue en arborescence sauf l\'objet coupé lorsque le bouton **Fermer** est cliqué pour fermer le dialogue.

Pour supprimer l\'objet coupé, décochez toutes les options **Coupe**.

En décochant toutes les options **Coupe**, le bouton **Rafraîchir la vue** devient actif. Lorsqu\'il est pressé, il prend une sorte de capture d\'écran des objets Part visibles. Celle-ci sera utilisée la prochaine fois que vous vérifierez une option **Coupe**. Le rafraîchissement est nécessaire lorsque vous changez de document. Il est en outre utile pour les assemblages, où vous pouvez vouloir cacher certaines pièces ou les ajouter ultérieurement à la découpe. Dans ce cas, le rafraîchissement recalcule les valeurs min/max des curseurs et des positions de découpe en fonction des dimensions de l\'objet actuellement visible.

Si l\'option **Auto** dans la section face coupée est cochée, la couleur et la transparence des objets coupés seront prises pour la face coupée. Cela ne fonctionne que si tous les objets coupés ont la même couleur ou la même transparence.

L\'option **Couper des objets s\'intersectant** permet de couper également les objets qui se croisent. Dans les assemblages, les intersections se produisent parfois pour des objets qui sont conçus pour ne se toucher que pour des raisons de précision numérique. L\'inconvénient de cette option est que tous les objets visibles auront la même couleur. Cette couleur peut être spécifiée dans la section **Face coupée** de la fenêtre de dialogue. Si vous avez besoin d\'une découpe pour, par exemple, une belle image avec plusieurs couleurs par face, vous pouvez changer les couleurs des faces en utilisant l\'outil <img alt="" src=images/Part_ColorPerFace.svg  style="width:24px;"> [Part Couleur par face](Part_ColorPerFace/fr.md).

**Remarque :** pour les assemblages, les curseurs dans la fenêtre de dialogue sont désactivés (sauf celui de la transparence). La raison en est qu\'un mouvement de curseur entraîne de nombreuses opérations de coupe dans un court laps de temps. Pour les assemblages, cela consomme rapidement toute la puissance de l\'unité centrale et un mouvement du curseur n\'est pas utile.

Lorsque vous sélectionnez un objet coupé dans l\'arborescence et que vous ouvrez ensuite la fenêtre de dialogue Coupe persistante, les positions de la coupe seront lues dans la fenêtre de dialogue.

## Applications

-   Un cas d\'utilisation important est que Coupe persistante crée des coupes remplies, et non des coupes creuses comme la fonction <img alt="" src=images/Std_ToggleClipPlane.svg  style="width:24px;"> [Std Couper selon des plans](Std_ToggleClipPlane/fr.md).
-   Coupe persistante est utile pour les assemblages afin de visualiser, par exemple, le principe de fonctionnement d\'un appareil. Vous pouvez ainsi vouloir colorer certaines faces de coupe en utilisant l\'outil <img alt="" src=images/Part_ColorPerFace.svg  style="width:24px;"> [Part Couleur par face](Part_ColorPerFace/fr.md). Pour utiliser cet outil, passez dans l\'atelier Part ou PartDesign, cliquez avec le bouton droit de la souris sur l\'objet coupé dans la vue en arborescence et sélectionnez dans le menu contextuel **Définir les couleurs**.
-   Sans l\'option **Couper des objets s\'intersectant**, seules les parties qui ne croisent pas les autres seront coupées. Ceci peut être utilisé comme test de collision.
-   La fonction Coupe persistante peut être utilisée pour les dessins techniques pour mettre en évidence certaines zones ou pour pouvoir dessiner dans les dimensions. L\'image ci-dessous montre un exemple d\'utilisation des fonctions de [TechDraw](TechDraw_Workbench/fr.md) que sont <img alt="" src=images/TechDraw_ActiveView.svg  style="width:24px;"> [Vue active](TechDraw_ActiveView/fr.md) et <img alt="" src=images/TechDraw_View.svg  style="width:24px;"> [Vue](TechDraw_View/fr.md).

<img alt="" src=images/Part_SectionCut_TD-example.png  style="width:400px;"> 
*Un dessin technique où un résultat de Coupe persistante est utilisé. (Cliquez sur l'image pour l'agrandir.)*



## Positions spéciales de coupe 

<img alt="Une coupe oblique d\'un assemblage" src=images/Part_SectionCut_slant-cut.png  style="width:200px;">

-   Par exemple, dans la première image de cette page, seul un quart de l\'assemblage est coupé. Ceci a été réalisé en créant une coupe dans la direction X. Ensuite, dans l\'objet de coupe résultant **SectionCutX**, le [placement](Placement/fr.md) du sous-objet **SectionCutBoxX** a été modifié.
-   Pour obtenir une coupe dans n\'importe quelle direction, vous pouvez faire ceci :

1.  Créez un nouveau conteneur [Std Part](Std_Part/fr.md).
2.  Sélectionnez tous les objets que vous voulez couper dans l\'arborescence et déplacez-les dans le conteneur.
3.  Réglez maintenant le placement du conteneur sur une rotation de votre choix. Pour l\'image de gauche, le conteneur a été tourné de 45° autour des axes X et Z et la coupe de la section a été effectuée dans la direction X.




## Limitations

<img alt="Un assemblage où deux parties se croisent et qui ne sont donc pas coupées. Notez les artefacts de couleur au niveau de la face coupée." src=images/Part_SectionCut_Color-artifact.png  style="width:200px;">

-   **Important :** la fonction Coupe persistante fonctionne mal avec [OpenCASCADE](OpenCASCADE/fr.md) 7.4 et plus anciens en raison de bogues. Il est donc recommandé d\'utiliser OpenCASCADE 7.5 ou plus récent (toutes les versions de FreeCAD {{VersionPlus/fr|0.20}} l\'assurent).

-    {{VersionPlus/fr|1.0}}: l\'option **Couper des objets s\'intersectant** donne la même couleur à toutes les parties visibles. Techniquement, cela ne peut être évité. Cependant, si l\'on a besoin d\'une coupe persistante, par exemple pour une présentation, voir la méthode décrite ci-dessus pour réinitialiser la couleur manuellement.

-    {{VersionMinus/fr|0.20}}: dans les assemblages, **les pièces qui se croisent ne peuvent pas être coupées**. Normalement les objets qui se croisent ne seront pas découpés alors que les autres le seront. Cependant, parfois la découpe peut produire des résultats étranges, ce qui est un bug dans les bibliothèques OpenCASCADE.Pour obtenir une vue en coupe également pour les objets qui se croisent, vous pouvez utiliser la [Macro Cross Section](Macro_cross_section/fr.md).

-    {{VersionMinus/fr|0.20}}: en particulier lorsque vous utilisez l\'[atelier A2plus](A2plus_Workbench/fr.md), certaines pièces assemblées peuvent se chevaucher d\'un micron seulement en raison d\'erreurs d\'arrondi internes. Pour résoudre ce problème, ajoutez un micron comme espace dans les paramètres des contraintes.

-   Il peut y avoir des artefacts de couleur dans le résultat de la coupe. Si et comment cela dépend de la bibliothèque OpenCASCADE et aussi de la position de la vue. Dans de nombreux cas, les artefacts de couleur disparaissent lorsque la vue 3D est légèrement tournée.

-   Lorsque vous avez des objets coupés avec des couleurs différentes, il n\'est pas possible d\'appliquer automatiquement leur couleur aux faces coupées correspondantes. Toutes les faces coupées auront la même couleur que celle sélectionnée dans la fenêtre de dialogue.

-   Lorsque vous utilisez l\'[atelier A2plus](A2plus_Workbench/fr.md), il n\'est pas possible d\'appliquer automatiquement la couleur des pièces assemblées aux faces coupées correspondantes. Toutes les faces coupées auront la même couleur que celle sélectionnée dans la fenêtre de dialogue. La raison est que A2plus ne saisit pas les pièces [comme lien](App_Link/fr.md) mais les charge comme fichier.






## Informations contextuelles 

**Coupe persistante** s\'inspire de la macro [Cross Section](Macro_cross_section/fr.md) et fonctionne techniquement de cette manière :

Tous les objets visibles sont placés dans un <img alt="" src=images/Part_Compound.svg  style="width:24px;"> [Part Composé](Part_Compound/fr.md). Pour l\'option **Couper des objets s\'intersectant**, un <img alt="" src=images/Part_BooleanFragments.svg  style="width:24px;"> [Part Fragments booléens](Part_BooleanFragments/fr.md) est utilisé à la place. Le composé est découpé à l\'aide d\'un <img alt="" src=images/Part_Box.svg  style="width:24px;"> [Part Cube](Part_Box/fr.md). Le cube doit être aussi grand que nécessaire pour couvrir l\'ensemble du volume de tous les objets visibles. Pour ce faire, le cube englobant des objets est déterminé. Lorsque vous modifiez la vue en ajoutant/supprimant des objets ou en modifiant le document, le cube englobant doit être mis à jour. Cela se fait en cliquant sur le bouton **Rafraîchir la vue**.





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part SectionCut/fr
