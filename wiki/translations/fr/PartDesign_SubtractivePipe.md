---
- GuiCommand:/fr
   Name:PartDesign SubtractivePipe
   Name/fr:PartDesign Balayage soustractif
   MenuLocation:Conception de pièces → Créer une fonction soustractive → Enlèvement de matière par balayage
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
   Version:0.17
   SeeAlso:[PartDesign Balayage additif](PartDesign_AdditivePipe/fr.md), [PartDesign Lissage soustractif](PartDesign_SubtractiveLoft/fr.md)
---

## Description

Le **Balayage soustractif** crée un solide soustractif dans le corps actif en balayant une ou plusieurs esquisses (également appelées coupes transversales) le long d\'un chemin ouvert ou fermé. Sa forme est ensuite soustraite du solide existant. Le balayage soustractif est souvent utilisé avec l\'[Part Hélice](Part_Helix/fr.md) et la [Part Forme liée](PartDesign_ShapeBinder/fr.md) pour créer un filetage. Voir le [Tutoriel Création de vis](Thread_for_Screw_Tutorial/fr.md) pour plus de détails.

## Utilisation

1.  Appuyer sur le bouton **<img src="images/_PartDesign_SubtractivePipe.svg" width=24px> '''Balayer une esquisse sélectionnée...'''**.
2.  Dans la boîte de dialogue **Sélectionner la fonction**, sélectionner une esquisse à utiliser comme première section et cliquer sur **OK**.
3.  \* Vous pouvez également sélectionner une seule esquisse avant d\'appuyer sur le bouton Balayage soustractif.
4.  Dans **Paramètres du balayage** sous **Profil**, appuyer sur le bouton **Objet**.
5.  Sélectionner l\'esquisse à utiliser comme chemin dans la vue 3D:
6.  \* Vous pouvez également sélectionner les arêtes du corps en appuyant sur **Ajouter une arête** et en sélectionnant les arêtes dans la vue 3D.
7.  Pour utiliser plus d\'une section, sous **Transformation de section**, régler le mode Transformation sur *Sections multiples*, appuyer sur **Ajouter une section**, puis sélectionner une esquisse dans la vue 3D. Répéter l\'opération pour chaque section supplémentaire.
8.  Définir les options si nécessaire et cliquer sur **OK**.

## Options


<div class="mw-translate-fuzzy">

**Transformation de section** :

-   Sélectionnez **Constant** pour utiliser un seul profil.
-   Sélectionnez **Sections multiples** pour utiliser plusieurs profils.

**Orientation de section** :

-   Standard
    -   Cela permet de garder la forme de la section transversale perpendiculaire à la trajectoire. Il s\'agit du paramètre par défaut.
-   Fixe
    -   Orientation définie par le premier profil et constante tout au long du parcours. Ceci désactive l\'alignement sur le vecteur normal de la trajectoire. Cela signifie que la forme de la section transversale ne tournera pas avec la trajectoire. Balayez le long d\'un cercle pour voir l\'effet.
-   Frenet
    -   Crée une torsion minimale possible du profil. Pour plus d\'informations, voir [Formules de Frenet-Serret](https://fr.wikipedia.org/wiki/Rep%C3%A8re_de_Frenet).
-   Auxiliaire
    -   Spécifiez le chemin secondaire pour guider le tuyau.
    -   Pour chaque point **P** le long du chemin de balayage, il y aura un point correspondant **Q** sur le chemin auxiliaire.
    -   Au fur et à mesure du balayage, le profil sera transformé de telle sorte que la ligne **PQ** soit la normale au chemin de balayage.
    -   Si **Equivalence curviligne** est défini, les points **Q** sont mis à l\'échelle proportionnellement le long du chemin de balayage, quelle que soit sa longueur.
-   Binormal
    -   Spécifiez le vecteur binormal en X, Y et Z.

**Transition de coin**

-   Transformé
-   Coin droite
-   Coin arrondi


</div>

## Propriétés

-    {{PropertyData/fr|Label}}: nom donné à l\'opération, ce nom peut être changé à la convenance.

-    {{PropertyData/fr|Refine}}: true (vrai) ou false (faux). Si la valeur est \"true\", nettoie le solide des bords résiduels laissés par les entités. Voir [Affiner la forme](Part_RefineShape/fr.md) pour plus de détails.

-    {{PropertyData/fr|Sections}}: liste les sections utilisées.

-    {{PropertyData/fr|Spine Tangent}}: true (vrai) ou false (faux) (par défaut). \"True\" étend le chemin pour inclure les bords tangents.

-    {{PropertyData/fr|Auxiliary Spine Tangent}}: true (vrai) ou false (faux) (par défaut). \"True\" étend le chemin auxiliaire pour inclure les bords tangents.

-    {{PropertyData/fr|Auxiliary Curvelinear}}: true (vrai) ou false (faux) (par défaut). \"True\" calcule la normale entre les points équidistants sur les deux dorsales.

-    {{PropertyData/fr|Mode}}: mode profil. Voir [ Options](#Options.md).

-    {{PropertyData/fr|Binormal}}: vecteur de la binormale pour le mode d\'orientation correspondant.

-    {{PropertyData/fr|Transition}}: mode de transition. Les options sont *Transformé*, *Coin Droit* ou \'\' Coin rond\'\'.

-    {{PropertyData/fr|Transformation}}: *Constant* utilise une section unique. *Multisection* utilise deux ou plusieurs sections transversales. *Linear*, *S-shape* et *Interpolation* ne sont actuellement pas fonctionnels.

## Limites

-   Les esquisses utilisées pour les sections transversales doivent former des profils fermés.
-   Il n\'est pas possible d\'utiliser un sommet comme section.
-   Une section transversale ne peut pas se trouver sur le même plan que celui qui la précède immédiatement.
-   Pour mieux contrôler la forme du balayage, il est recommandé que toutes les sections aient le même nombre de segments. Par exemple, pour un balayage entre un rectangle et un cercle, le cercle peut être divisé en 4 arcs connectés.





{{PartDesign Tools navi

}} 
