---
- GuiCommand:
   Name: PartDesign AdditivePipe
   Name/fr: PartDesign Balayage additif
   MenuLocation: Part Design - Créer une fonction additive - Balayage additif
   Workbenches: [PartDesign](PartDesign_Workbench/fr.md)
   Version: 0.17
   SeeAlso: [PartDesign Lissage additif](PartDesign_AdditiveLoft/fr.md), [PartDesign Balayage soustractif](PartDesign_SubtractivePipe/fr.md)
---

# PartDesign AdditivePipe/fr

## Description

**Balayage additif** crée un solide dans le corps actif en balayant une ou plusieurs esquisses (également appelées sections transversales) le long d\'un chemin ouvert ou fermé. Si le corps contient déjà des éléments, le tuyau additif sera fusionné avec eux.

![](images/PartDesign_AdditivePipe_example.svg ) 
*À gauche les sections (A) et (B) seront balayées le long du chemin (C), le résultat est visible à droite.*

## Utilisation

L\'exemple d\'image ci-dessus montre deux formes de section transversale différentes. Le texte ci-dessous décrit la procédure avec une seule forme. Cela permettra d\'obtenir une pièce avec la même section transversale le long de la trajectoire.

1.  Créez deux esquisses séparées ;
    -   une pour la trajectoire, par exemple deux lignes reliées par une courbe comme dans l\'image ci-dessus,
    -   une pour la forme de la section transversale, par exemple un cercle comme la première forme dans l\'image ci-dessus. Au lieu d\'une esquisse, on peut aussi utiliser la face d\'un objet 3D. ({{Version/fr|0.20}})
2.  **Arrangez** les deux formes en 3D correctement. Il est recommandé de placer l\'origine de la section transversale sur la ligne de la trajectoire. Les deux esquisses devraient dans la plupart des cas être **orthogonales**. Ceci peut être fait avec la fonction \'Map Mode\' (rendez les deux esquisses visibles avec **Espace**. Sélectionnez l\'esquisse de coupe transversale. Sélectionnez Properties/DataTab/MapMode. Cliquez sur le bouton **...** qui apparaît sur le côté droit. Dans la boîte de dialogue d\'attachement, sélectionnez un sommet de l\'esquisse de trajectoire et sélectionnez le mode correct pour que les deux esquisses soient correctement alignées).
3.  Appuyez sur le bouton **<img src="images/PartDesign_AdditivePipe.svg" width=24px> [Balayage additif](PartDesign_AdditivePipe/fr.md)**.
4.  Dans la boîte de dialogue **Sélectionner un élément**, sélectionnez une section d\'esquisse à utiliser et cliquez sur **OK**.
    -   Vous pouvez également sélectionner une esquisse ou une face d\'un objet 3D ({{Version/fr|0.20}}) avant d\'appuyer sur le bouton Additive pipe. Dans ce cas, vous n\'obtiendrez pas de boîte de dialogue \"Select feature\".
5.  Dans les **Paramètres de balayage**, sous **Chemin le long duquel effectuer le balayage**, appuyez sur le bouton **Objet**.
6.  Sélectionnez l\'esquisse à utiliser comme trajectoire dans la vue 3D. Dans ce cas, l\'esquisse entière sera utilisée comme trajectoire.
    -   Vous pouvez également sélectionner des arêtes individuelles de l\'esquisse en appuyant sur **Ajouter une arête** et en sélectionnant des arêtes dans la vue 3D. Notez que vous devez appuyer à nouveau sur **Ajouter une arête** pour chaque arête. Vous devez sélectionner une ligne continue, sans branches.
7.  Les autres paramètres devraient fonctionner avec les paramètres par défaut dans la plupart des cas.
8.  Cliquez sur **OK**.

Pour utiliser plusieurs sections, commencez par la section comme décrit ci-dessus. Ensuite, sous **Transformation de section**, définissez le mode de transformation sur *Sections multiples*, appuyez sur **Ajouter une section** puis sélectionnez une esquisse dans la [Vue 3D](3D_view/fr.md). Répétez l\'opération pour chaque section supplémentaire.

## Options

**Transformation de section**:

-   Sélectionner **Constant** pour utiliser un seul profil
-   Sélectionner **Sections multiples** pour utiliser plusieurs profils

**Orientation de la section**:

-   Standard

    :   Cela maintient la forme de la section perpendiculaire au chemin. Ce sont les paramètres par défauts.
-   Fixé
    -   Orientation définie par le premier profil et constante tout au long. Cela désactive l\'alignement sur le vecteur normal de trajectoire. Cela signifie que la forme de la section transversale ne tournera pas avec le chemin. Balayez le long d\'un cercle pour voir l\'effet.
-   Frenet
    -   Crée le minimum de torsion possible du profil. Pour plus d\'informations, voir les [formules de Frenet-Serret](https://fr.wikipedia.org/wiki/Rep%C3%A8re_de_Frenet#Formules_de_Frenet)
-   Auxiliaire
    -   Spécifie le chemin secondaire pour guider le balayage.
    -   Pour chaque point **P** le long du chemin de balayage, il y aura un point correspondant **Q** sur le chemin auxiliaire.
    -   Au fur et à mesure que le profil est balayé, il sera transformé de telle sorte que la ligne **PQ** soit la normale du chemin de balayage.
    -   Si **Equivalence curviligne** est choisie, les points **Q** sont mis à l\'échelle proportionnellement le long du chemin de balayage, quelle que soit sa longueur.
-   Binormal
    -   Spécifie le vecteur de la binormale en X, Y et Z

**Transition de coin**

-   Transformé
-   Coin droit
-   Coin arrondi

## Propriétés

-    **Label**: Donne le nom de l\'opération, changer si nécessaire.

-    **Refine**: Vrai ou faux. Si \"Vrai\", les arêtes résiduelles sont lissées. Voir [Affiner la forme](Part_RefineShape/fr.md) pour plus de détails.

-    **Sections**: liste les esquisses de section utilisées.

-    **Spine Tangent**: Vrai ou faux (défaut). \"Vrai\" étend le chemin aux arêtes tangentes.

-    **Auxiliary Spine Tangent**: Vrai ou faux (défaut). \"Vrai\" étend le chemin aux arêtes tangentes auxiliaires.

-    **Auxiliary Curvelinear**: Vrai ou faux (défaut). \"Vrai\" calcule la normale entre les points équidistants sur les deux courbes dorsales.

-    **Mode**: mode profil. Voir [Options](#Options.md).

-    **Binormal**: vecteur de la binormale pour le mode d\'orientation correspondant.

-    **Transition**: mode de transition. Les options sont \"Transformé\", \"Coin droit\" ou \"Coin arrondi\".

-    **Transformation**: \"Constant \" utilise une section unique. \"Sections multiples\" utilise deux ou plusieurs sections transversales. \"Linear\", \"S-shape\" et \"Interpolation\" ne sont actuellement pas fonctionnels.

## Remarques

-   Pour mieux contrôler la forme du tuyau, il est recommandé que toutes les sections transversales aient le même nombre de segments. Par exemple, pour un tuyau entre un rectangle et un cercle, le cercle doit être décomposé en 4 arcs connectés.
-   Vous pouvez créer un tuyau à partir ou en direction d\'un seul [vertex (ou point)](Glossary/fr#V.md) d\'une esquisse ou du corps. {{Version/fr|0.20}}
-   Lorsque vous sélectionnez un [vertex](Glossary/fr#V.md) comme section, il doit s\'agir de la dernière section du tuyau. Sinon, le corps du tuyau serait constitué de deux solides reliés en un seul point. Cela violerait la définition d\'un objet 3D du noyau de CAO. Vous pouvez modifier l\'ordre des sections en les faisant glisser dans la liste.
-   La trajectoire ne peut provenir que d\'une seule esquisse, d\'une seule caractéristique ou d\'un seul ShapeBinder. Si vous souhaitez balayer plusieurs arêtes provenant de différentes esquisses, utilisez un **[<img src=images/PartDesign_SubShapeBinder.svg style="width:16px"> [PartDesign Sous-forme liée](PartDesign_SubShapeBinder/fr.md)**.
-   La trajectoire ne doit pas contenir de branches ou de jonctions en T, etc. Les boucles sont autorisées.
-   Il peut y avoir des problèmes si la section transversale n\'est pas perpendiculaire à la trajectoire en 3D.
-   Une section transversale ne peut pas se trouver sur le même plan que celle qui la précède immédiatement.
-   Les sections transversales ne doivent pas contenir de boucles disjointes ou croisées.





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditivePipe/fr
