---
- GuiCommand:/fr
   Name:PartDesign AdditiveLoft
   Name/fr:PartDesign Lissage additif
   MenuLocation:Conception de pièces → Créer une fonction additive → Lissage additif
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
   Version:0.17
   SeeAlso:[PartDesign Balayage additif](PartDesign_AdditivePipe/fr.md), [PartDesign Lissage soustractif](PartDesign_SubtractiveLoft/fr.md)
---

# PartDesign AdditiveLoft/fr

## Description

Le **Lissage additif** crée un solide dans le Corps actif en faisant une transition entre deux ou plusieurs esquisses (également appelées sections transversales). Si le corps contient déjà des éléments, le lissage additif sera fusionné avec eux.

![](images/PartDesign_AddLoft_example.png ) 
*A gauche: sections (A), (B) et (C); à droite, résultat du Lissage additif.*

## Utilisation

### Processus de travail basé sur la boîte de dialogue 

1.  Cliquez sur le bouton **[<img src=images/PartDesign_AdditiveLoft.svg style="width:24px"> [Lissage additif](PartDesign_AdditiveLoft/fr.md)**.
2.  Dans la boîte de dialogue **Sélectionner une fonction**, sélectionnez une esquisse à utiliser comme objet de profil de base et cliquez sur **OK**.
    -   Vous pouvez également sélectionner une seule esquisse ou la face d\'un objet 3D ({{Version/fr|0.20}}) avant d\'appuyer sur le bouton Lissage additif.
3.  Dans **Paramètres de lissage**, cliquez sur **Ajouter une section**.
4.  Sélectionnez l\'esquisse suivante dans la [Vue 3D](3D_view/fr.md). Répétez la sélection pour les autres esquisses dans l'ordre dans lequel vous souhaitez qu'elles soient lissées. (Vous pouvez modifier l\'ordre des sections à tout moment ultérieurement dans la boîte de dialogue de lissage en faisant glisser les sections de la liste vers la position souhaitée. {{Version/fr|0.19}})
5.  Définissez des options si nécessaire puis cliquez sur **OK**.

### Processus de travail basé sur la sélection 


{{Version/fr|0.19}}

1.  Sélectionnez plusieurs esquisses. L\'ordre dans lequel vous les sélectionnez est important:
    -   L\'esquisse sélectionnée au départ deviendra l\'objet de profil de base à l\'étape suivante
    -   Les esquisses sélectionnées après la première deviendront les sections du lissage. Ici aussi, l\'ordre de sélection est important: la deuxième esquisse sélectionnée deviendra la première section de lissage, celle sélectionnée comme troisième deviendra la deuxième section et ainsi de suite. (Vous pouvez modifier l\'ordre des sections à tout moment ultérieurement dans la boîte de dialogue de lissage en faisant glisser les sections de la liste vers la position souhaitée. {{Version/fr|0.19}})
    -   La première ou la dernière sélection peut aussi être une face d\'un objet 3D ({{Version/fr|0.20}}).
2.  Appuyez sur le bouton **[<img src=images/PartDesign_AdditiveLoft.svg style="width:24px"> [Lissage additif](PartDesign_AdditiveLoft/fr.md)**.
3.  Définissez les options si nécessaire et cliquez sur **OK**.

## Options

-   **Surface réglée** : effectue des transitions droites entre les sections. Ne s\'applique pas à un lissage avec deux sections transversales. Si cette case n\'est pas cochée, les transitions seront lisses.
-   **Fermé** : effectue une transition de la dernière section à la première, en créant une boucle.

## Propriétés

-    **Label**: nom donné à l\'opération, ce nom peut être changé à la convenance.

-    **Sections**: liste les sections utilisées.

-    **Ruled**: voir [Options](#Options.md).

-    **Closed**: voir [Options](#Options.md).

-    **Refine**: true ou false. Si la valeur est true, nettoie le solide des arêtes résiduelles laissées par les fonctions. Voir [Part Affiner la forme](Part_RefineShape/fr.md) pour plus de détails.

-    **Profile**: l\'objet de profil de base voir du lissage.

-    **Midplane**: non applicable.

-    **Inversé**: non applicable.

-    **Up To Face**: non applicable.

-    **Allow Multi Face**: non applicable.

## Remarques

-   Pour mieux contrôler la forme du lissage, il est recommandé que toutes les sections transversales aient le même nombre de segments. Par exemple, pour un lissage entre un rectangle et un cercle, le cercle doit être décomposé en 4 arcs connectés.
-   Vous pouvez effectuer un lissage depuis ou vers un seul [vertex (ou Point)](Glossary/fr#V.md) d\'une esquisse ou du corps. {{Version/fr|0.20}}
-   Les [Vertices](Glossary/fr#V.md) ne peuvent être que le début ou la fin d\'un lissage. Sinon, le corps du lissage serait constitué de deux solides reliés en un seul point. Cela violerait la définition d\'un objet 3D du noyau de CAO.
-   Une section transversale ne peut pas se trouver sur le même plan que celle qui la précède immédiatement.
-   Si l\'esquisse a une géométrie interne, c\'est-à-dire que le lissage est censé avoir des trous, l\'ordre dans lequel la géométrie de l\'esquisse est créée doit être le même pour toutes les sections : Soit vous commencez toutes les sections par la géométrie intérieure, soit vous les commencez toutes par la géométrie extérieure. Sinon, un lissage invalide peut être créé là où les parois intérieurs et extérieurs se croisent.
-   Il n\'est pas possible de lisser des boucles disjointes ou croisées.
-   Certains modes de défaillance rendent la pièce noire.

## Liens

-   [Part Détails techniques du lissage](Part_Loft_Technical_Details/fr.md) explique comment un [Part Lissage](Part_Loft/fr.md) est créé, une grande partie de son contenu est pertinente pour le Lissage additif de PartDesign.





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveLoft/fr
