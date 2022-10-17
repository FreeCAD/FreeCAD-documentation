---
- GuiCommand   */fr
   Name   *PartDesign SubtractivePipe
   Name/fr   *PartDesign Balayage soustractif
   MenuLocation   *Part Design → Créer une fonction soustractive → Enlèvement de matière par balayage
   Workbenches   *[PartDesign](PartDesign_Workbench/fr.md)
   Version   *0.17
   SeeAlso   *[PartDesign Balayage additif](PartDesign_AdditivePipe/fr.md), [PartDesign Lissage soustractif](PartDesign_SubtractiveLoft/fr.md)
---

# PartDesign SubtractivePipe/fr

## Description

Le **Balayage soustractif** crée un solide soustractif dans le corps actif en balayant une ou plusieurs esquisses (également appelées coupes transversales) le long d\'un chemin ouvert ou fermé. Sa forme est ensuite soustraite du solide existant. Le balayage soustractif est souvent utilisé avec [Part Hélice](Part_Helix/fr.md) et [Part Forme liée](PartDesign_ShapeBinder/fr.md) pour créer un filetage. Voir le [Tutoriel Création de vis](Thread_for_Screw_Tutorial/fr.md) pour plus de détails.

## Utilisation

1.  Appuyer sur le bouton **<img src="images/_PartDesign_SubtractivePipe.svg" width=24px> '''Enlèvement de matière par balayage'''**.
2.  Dans la boîte de dialogue **Sélectionner la fonction**, sélectionner une esquisse à utiliser comme première section et cliquer sur **OK**.

#\* Il est également possible de sélectionner une esquisse ou une face d\'un objet 3D ({{Version/fr|0.20}}) avant d\'appuyer sur le bouton Balayage soustractif.

1.  Dans **Paramètres du balayage** sous **Profil**, appuyer sur le bouton **Objet**.
2.  Sélectionner l\'esquisse à utiliser comme chemin dans la vue 3D   *
3.  \* Vous pouvez également sélectionner les arêtes du corps en appuyant sur **Ajouter une arête** et en sélectionnant les arêtes dans la vue 3D.
4.  Pour utiliser plus d\'une section, sous **Transformation de section**, régler le mode Transformation sur *Sections multiples*, appuyer sur **Ajouter une section**, puis sélectionner une esquisse dans la vue 3D. Répéter l\'opération pour chaque section supplémentaire.
5.  Définir les options si nécessaire et cliquer sur **OK**.

## Options

**Transformation de section**    *

-   Sélectionnez **Constant** pour utiliser un seul profil.
-   Sélectionnez **Sections multiples** pour utiliser plusieurs profils.

**Orientation de section**    *

-   Standard
    -   Cela permet de garder la forme de la section transversale perpendiculaire à la trajectoire. Il s\'agit du paramètre par défaut.
-   Fixe
    -   Orientation définie par le premier profil et constante tout au long du parcours. Ceci désactive l\'alignement sur le vecteur normal de la trajectoire. Cela signifie que la forme de la section transversale ne tournera pas avec la trajectoire. Balayez le long d\'un cercle pour voir l\'effet.
-   Frenet
    -   Crée une torsion minimale possible du profil. Pour plus d\'informations, voir [Formules de Frenet-Serret](https   *//fr.wikipedia.org/wiki/Rep%C3%A8re_de_Frenet).
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

-    **Label**   * nom donné à l\'opération, ce nom peut être changé à la convenance.

-    **Refine**   * true (vrai) ou false (faux). Si la valeur est \"true\", nettoie le solide des bords résiduels laissés par les entités. Voir [Affiner la forme](Part_RefineShape/fr.md) pour plus de détails.

-    **Sections**   * liste les sections utilisées.

-    **Spine Tangent**   * true (vrai) ou false (faux) (par défaut). \"True\" étend le chemin pour inclure les bords tangents.

-    **Auxiliary Spine Tangent**   * true (vrai) ou false (faux) (par défaut). \"True\" étend le chemin auxiliaire pour inclure les bords tangents.

-    **Auxiliary Curvelinear**   * true (vrai) ou false (faux) (par défaut). \"True\" calcule la normale entre les points équidistants sur les deux dorsales.

-    **Mode**   * mode profil. Voir [Options](#Options.md).

-    **Binormal**   * vecteur de la binormale pour le mode d\'orientation correspondant.

-    **Transition**   * mode de transition. Les options sont *Transformé*, *Coin Droit* ou *Coin rond*.

-    **Transformation**   * *Constant* utilise une section unique. *Multisection* utilise deux ou plusieurs sections transversales. *Linear*, *S-shape* et *Interpolation* ne sont actuellement pas fonctionnels.

## Remarques

-   Pour mieux contrôler la forme du tuyau, il est recommandé que toutes les sections transversales aient le même nombre de segments. Par exemple, pour un tuyau entre un rectangle et un cercle, le cercle doit être décomposé en 4 arcs connectés.
-   Vous pouvez créer un tuyau à partir ou en direction d\'un seul [vertex (ou point)](Glossary/fr#V.md) d\'une esquisse ou du corps. {{Version/fr|0.20}}
-   Lorsque vous sélectionnez un [vertex](Glossary/fr#V.md) comme section, il doit dans la plupart des cas être la dernière section du tuyau. Vous pouvez modifier l\'ordre des sections en les faisant glisser dans la liste.
-   La trajectoire ne peut provenir que d\'une seule esquisse, d\'une seule caractéristique ou d\'un seul ShapeBinder. Si vous souhaitez balayer plusieurs arêtes à partir de différentes esquisses, utilisez une **[<img src=images/PartDesign_SubShapeBinder.svg style="width   *16px">[PartDesign Sous forme liée](PartDesign_SubShapeBinder/fr.md)**.
-   La trajectoire ne doit pas contenir de branches ou de jonctions en T, etc. Les boucles sont autorisées.
-   Il peut y avoir des problèmes si la section transversale n\'est pas perpendiculaire à la trajectoire en 3D.
-   Une section transversale ne peut pas se trouver sur le même plan que celle qui la précède immédiatement.
-   Les sections transversales ne doivent pas contenir de boucles disjointes ou croisées.





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractivePipe/fr
