---
 GuiCommand:
   Name: PartDesign SubtractivePipe
   Name/fr: PartDesign Balayage soustractif
   MenuLocation: PartDesign , Créer une fonction soustractive , Enlèvement de matière par balayage
   Workbenches: PartDesign_Workbench/fr
   Version: 0.17
   SeeAlso: PartDesign_AdditivePipe/fr, PartDesign_SubtractiveLoft/fr
---

# PartDesign SubtractivePipe/fr

## Description

Le **Balayage soustractif** crée un solide soustractif dans le corps actif en balayant une ou plusieurs esquisses (également appelées coupes transversales) le long d\'un chemin ouvert ou fermé. Sa forme est ensuite soustraite du solide existant. Le balayage soustractif est souvent utilisé avec [Part Hélice](Part_Helix/fr.md) et [Part Forme liée](PartDesign_ShapeBinder/fr.md) pour créer un filetage. Voir le [Tutoriel Création de vis](Thread_for_Screw_Tutorial/fr.md) pour plus de détails.



## Utilisation

1.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyer sur le bouton **<img src="images/PartDesign_SubtractivePipe.svg" width=16px> [Enlèvement de matière par balayage](PartDesign_SubtractivePipe/fr.md)**.
    -   Sélectionner l\'option **PartDesign → Créer une fonction soustractive → <img src="images/PartDesign_SubtractivePipe.svg" width=16px> Enlèvement de matière par balayage** du menu.
2.  Dans **Paramètres du balayage**, sélectionner une esquisse à utiliser comme première section transversale et cliquer sur **OK**.
    -   Vous pouvez sélectionner une esquisse ou une face d\'un objet 3D ({{Version/fr|0.20}}) avant de lancer l\'outil. Dans ce cas, vous n\'aurez pas cette fenêtre de dialogue.
3.  Dans **Paramètres du balayage** sous **Profil**, appuyer sur le bouton **Objet**.
4.  Sélectionner l\'esquisse à utiliser comme trajectoire dans la vue 3D :
    -   Vous pouvez sélectionner les arêtes du corps en appuyant sur le bouton **Ajouter une arête** et en sélectionnant les arêtes dans la vue 3D.
5.  Pour utiliser plus d\'une section transversale, sous *Transformation de la section*, régler le mode Transformation sur *Sections multiples*, appuyer sur le bouton **Ajouter une section** puis sélectionner une esquisse dans la vue 3D. Répéter l\'opération pour chaque section supplémentaire.
6.  Définir les options si nécessaire et cliquez sur **OK**.

## Options

**Transformation de section** :

-   Sélectionnez **Constant** pour utiliser un seul profil.
-   Sélectionnez **Sections multiples** pour utiliser plusieurs profils.

**Orientation de section** :

-   Standard
    -   Cela permet de garder la forme de la section transversale perpendiculaire à la trajectoire. Il s\'agit du paramètre par défaut.
-   Constante
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



## Propriétés

-    **Label**: nom donné à l\'opération, ce nom peut être changé à la convenance.

-    **Refine**: true (vrai) ou false (faux). Si la valeur est \"true\", nettoie le solide des bords résiduels laissés par les éléments. Voir [Part Affiner la forme](Part_RefineShape/fr.md) pour plus de détails.

-    **Sections**: liste les sections utilisées.

-    **Spine Tangent**: true (vrai) ou false (faux) (par défaut). \"True\" étend le chemin pour inclure les bords tangents.

-    **Auxiliary Spine Tangent**: true (vrai) ou false (faux) (par défaut). \"True\" étend le chemin auxiliaire pour inclure les bords tangents.

-    **Auxiliary Curvelinear**: true (vrai) ou false (faux) (par défaut). \"True\" calcule la normale entre les points équidistants sur les deux chemins.

-    **Mode**: mode profil. Voir [Options](#Options.md).

-    **Binormal**: vecteur de la binormale pour le mode d\'orientation correspondant.

-    **Transition**: mode de transition. Les options sont *Transformed*, *Right Corner* ou *Round Corner*.

-    **Transformation**: *Constant* utilise une section unique. *Multisection* utilise deux ou plusieurs sections transversales. *Linear*, *S-shape* et *Interpolation* ne sont actuellement pas fonctionnels.



## Remarques

-   Pour mieux contrôler la forme du balayage, il est recommandé que toutes les sections transversales aient le même nombre de segments. Par exemple, pour un balayage entre un rectangle et un cercle, le cercle doit être décomposé en 4 arcs connectés.
-   Vous pouvez créer un balayage à partir ou en direction d\'un seul [vertex (ou point)](Glossary/fr#V.md) d\'une esquisse ou du corps. {{Version/fr|0.20}}
-   Lorsque vous sélectionnez un [vertex](Glossary/fr#V.md) comme section, il doit dans la plupart des cas être la dernière section du balayage. Vous pouvez modifier l\'ordre des sections en les faisant glisser dans la liste.
-   La trajectoire ne peut provenir que d\'une seule esquisse, d\'une seule caractéristique ou d\'un seul ShapeBinder. Si vous souhaitez balayer plusieurs arêtes à partir de différentes esquisses, utilisez une [PartDesign Sous forme liée](PartDesign_SubShapeBinder/fr.md).
-   La trajectoire ne doit pas avoir ni embranchements ni jonctions en T, etc. Les boucles sont autorisées.
-   Il peut y avoir des problèmes si la section transversale n\'est pas perpendiculaire à la trajectoire en 3D.
-   Une section transversale ne peut pas se trouver sur le même plan que celle qui la précède immédiatement.
-   Les sections transversales ne doivent pas contenir de boucles disjointes ou croisées.
-   Si l\'esquisse possède une géométrie intérieure, l\'ordre dans lequel la géométrie de l\'esquisse est créée doit être le même pour toutes les sections. Commencez toutes les sections par la géométrie intérieure, ou commencez-les toutes par la géométrie extérieure. Sinon, un tuyau non valide sera créé à l\'endroit où les murs intérieurs et extérieurs se croisent.





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractivePipe/fr
