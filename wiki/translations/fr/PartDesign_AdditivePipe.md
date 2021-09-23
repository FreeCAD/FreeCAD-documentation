---
- GuiCommand:/fr
   Name:PartDesign AdditivePipe
   Name/fr:PartDesign Balayage additif
   MenuLocation:Conception de pièces → Créer une fonction additive → Balayage additif
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
   Version:0.17
   SeeAlso:[PartDesign Lissage additif](PartDesign_AdditiveLoft/fr.md), [PartDesign Balayage soustractif](PartDesign_SubtractivePipe/fr.md)
---

## Description

Insère un **Balayage additif** dans un Corps actif par balayage d\'une ou plusieurs esquisses (également appelées sections transversales) le long d\'un chemin ouvert ou fermé. Si le Corps contient déjà un solide, le balayage additif sera fusionné avec lui.

![](images/PartDesign_AdditivePipe_example.svg ) *À gauche les sections (A) et (B) seront balayées le long du chemin (C), le résultat est visible à droite.*

## Utilisation

L\'exemple d\'image ci-dessus montre deux formes de section transversale différentes. Le texte ci-dessous décrit la procédure avec une seule forme. Cela permettra d\'obtenir une pièce avec la même section transversale le long de la trajectoire.

1.  Créez deux esquisses distinctes.
    -   une pour le chemin, par exemple deux lignes reliées par une courbe comme dans l\'image ci-dessus
    -   une pour la forme de la section, par ex. un cercle comme première forme dans l\'image ci-dessus
2.  **Arrangez** les deux formes en 3D correctement. Il est recommandé de placer l\'origine de la section transversale sur la ligne du chemin. Les deux esquisses doivent dans la plupart des cas être **orthogonales**. Cela peut être fait avec la fonction \'Map Mode\' (permet de rendre les deux esquisses visibles avec **Espace**. Sélectionnez l\'esquisse en coupe. Sélectionnez Properties/DataTab/MapMode. Cliquez le bouton droit **...** .Dans la boîte de dialogue des pièces jointes, sélectionnez un sommet de la esquisse du chemin et sélectionnez le mode correct pour aligner correctement les deux esquisses).
3.  Presser le bouton **<img src="images/PartDesign_AdditivePipe.svg" width=24px> [Balayer une esquisse sélectionnée...](PartDesign_AdditivePipe/fr.md)**.
4.  Dans la boite de dialogue **Select feature** comme section de départ et cliquer**OK**.
    -   Alternative, l\'esquisse de section peut être sélectionnée avant d\'appuyer sur le bouton Balayer une esquisse sélectionnée\... Dans ce cas, vous n\'aurez pas de boîte de dialogue \"Sélectionner une fonction\".
5.  Dans les **Paramètres de balayage** sous **Chemin le long duquel efectuer le balayge**, cliquez sur le bouton **Objet**.
6.  Sélectionnez l\'esquisse à utiliser comme chemin dans la vue 3D. Dans ce cas, l\'esquisse entière sera utilisée comme chemin.
    -   Alternative, vous pouvez également sélectionner des arêtes uniques de l\'esquisse en appuyant sur **Ajouter une arête** et en sélectionnant des arêtes dans la vue 3D. Notez que vous devez appuyer à nouveau sur **Ajouter une arête** pour chaque bord. Vous devez sélectionner une ligne continue sans branches.
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
    -   Crée le minimum de torsion possible du profil. Pour plus d\'informations, voir [Frenet-Serret](https://fr.wikipedia.org/wiki/Rep%C3%A8re_de_Frenet#Formules_de_Frenet)
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

-    {{PropertyData/fr|Label}}: Donne le nom de l\'opération, changer si nécessaire.

-    {{PropertyData/fr|Refine}}: Vrai ou faux. Si \"Vrai\", les arêtes résiduelles sont lissées. Voir [Affiner la forme](Part_RefineShape/fr.md) pour plus de détails.

-    {{PropertyData/fr|Sections}}: liste les esquisses de section utilisées.

-    {{PropertyData/fr|Spine Tangent}}: Vrai ou faux (défaut). \"Vrai\" étend le chemin aux arêtes tangentes.

-    {{PropertyData/fr|Auxiliary Spine Tangent}}: Vrai ou faux (défaut). \"Vrai\" étend le chemin aux arêtes tangentes auxiliaires.

-    {{PropertyData/fr|Auxiliary Curvelinear}}: Vrai ou faux (défaut). \"Vrai\" calcule la normale entre les points équidistants sur les deux courbes dorsales.

-    {{PropertyData/fr|Mode}}: mode profil. Voir [Options](#Options.md).

-    {{PropertyData/fr|Binormal}}: vecteur de la binormale pour le mode d\'orientation correspondant.

-    {{PropertyData/fr|Transition}}: mode de transition. Les options sont \"Transformé\", \"Coin droit\" ou \"Coin arrondi\".

-    {{PropertyData/fr|Transformation}}: \"Constant \" utilise une section unique. \"Sections multiples\" utilise deux ou plusieurs sections transversales. \"Linear\", \"S-shape\" et \"Interpolation\" ne sont actuellement pas fonctionnels.

## Limites

-   Les esquisses utilisées pour les sections transversales doivent être toutes fermées.
-   Le parcours ne peut provenir que d\'une seule esquisse, fonction ou d\'une forme liée. Si vous souhaitez balayer plusieurs arêtes à partir de différentes esquisses, utilisez une **<img src=images/PartDesign_SubShapeBinder.svg style="width:16px"> [PartDesign Sous-forme liée](PartDesign_SubShapeBinder/fr.md)**.
-   Le chemin ne doit pas contenir de branches ou de jonctions en T, etc. Les boucles sont autorisées.
-   Il n\'est pas possible d\'utiliser un sommet comme section transversale.
-   Cela peut entraîner des problèmes si la section transversale n\'est pas perpendiculaire au tracé en 3D (certains autres systèmes de CAO considèrent l\'origine de la section transversale comme le chemin et ne nécessitent pas de placer cette esquisse explicitement).
-   Une section ne peut pas être sur le même plan que celle qui la précède.
-   Pour un meilleur résultat sur le lissage, il est recommandé que toutes les sections aient le même nombres de segments. Par exemple, pour un balayage entre un rectangle et un cercle, le cercle peut être divisé en 4 arcs connectés.





{{PartDesign Tools navi

}} 
