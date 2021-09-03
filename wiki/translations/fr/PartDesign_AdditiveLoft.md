---
- GuiCommand:/fr
   Name:PartDesign AdditiveLoft
   Name/fr:PartDesign Lissage additif
   MenuLocation:Conception de pièces → Créer une fonction additive → Lissage additif
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
   Version:0.17
   SeeAlso:[PartDesign Balayage additif](PartDesign_AdditivePipe/fr.md), [PartDesign Lissage soustractif](PartDesign_SubtractiveLoft/fr.md)
---

## Description

Le **Lissage additif** crée un solide dans le Corps actif en faisant une transition entre deux ou plusieurs esquisses (également appelées sections transversales). Si le corps contient déjà des éléments, le lissage additif sera fusionné avec eux.

![](images/PartDesign_AddLoft_example.png ) *A gauche: sections (A), (B) et (C); à droite, résultat du Lissage additif.*

## Utilisation

### Déroulement du travail basé sur la boîte de dialogue {#déroulement_du_travail_basé_sur_la_boîte_de_dialogue}

1.  Cliquez sur le bouton **<img src=images/PartDesign_AdditiveLoft.svg style="width:24px"> [Lisser un profil sélectionné...](PartDesign_AdditiveLoft/fr.md)**.
2.  Dans la boîte de dialogue **Sélectionner une fonction**, sélectionnez une esquisse à utiliser comme objet de profil de base et cliquez sur **OK**.
    -   Autre possibilité: présélectionnez une esquisse avant de cliquer sur <img alt="" src=images/PartDesign_AdditiveLoft.png  style="width:24px;">.
3.  Dans **Paramètres de lissage**, cliquez sur **Ajouter une section**.
4.  Sélectionnez l\'esquisse suivante dans la [Vue 3D](3D_view/fr.md). Répétez la sélection pour les autres esquisses dans l'ordre dans lequel vous souhaitez qu'elles soient lissées. (Vous pouvez modifier l\'ordre des sections à tout moment ultérieurement dans la boîte de dialogue de lissage en faisant glisser les sections de la liste vers la position souhaitée. {{Version/fr|0.19}})
5.  Définissez des options si nécessaire puis cliquez sur **OK**.

### Déroulement du travail basé sur la sélection {#déroulement_du_travail_basé_sur_la_sélection}


{{Version/fr|0.19}}

1.  Sélectionnez plusieurs esquisses. L\'ordre dans lequel vous les sélectionnez est important:
    -   L\'esquisse sélectionnée au départ deviendra l\'objet de profil de base à l\'étape suivante
    -   Les esquisses sélectionnées après la première deviendront les sections du lissage. Ici aussi, l\'ordre de sélection est important: la deuxième esquisse sélectionnée deviendra la première section de lissage, celle sélectionnée comme troisième deviendra la deuxième section et ainsi de suite. (Vous pouvez modifier l\'ordre des sections à tout moment ultérieurement dans la boîte de dialogue de lissage en faisant glisser les sections de la liste vers la position souhaitée. {{Version/fr|0.19}})
2.  Appuyez sur le bouton **<img src=images/PartDesign_AdditiveLoft.svg style="width:24px"> [Lisser un profil sélectionné...](PartDesign_AdditiveLoft/fr.md)**.
3.  Définissez les options si nécessaire et cliquez sur **OK**.

## Options

-   **Surface réglée** : effectue des transitions droites entre les sections. Ne s\'applique pas à un lissage avec deux sections transversales. Si cette case n\'est pas cochée, les transitions seront lisses.
-   **Fermé** : effectue une transition de la dernière section à la première, en créant une boucle.

## Propriétés

-    {{PropertyData/fr|Label}}: nom donné à l\'opération, ce nom peut être changé à la convenance.

-    {{PropertyData/fr|Sections}}: liste les sections utilisées.

-    {{PropertyData/fr|Ruled}}: voir [Options](#Options.md).

-    {{PropertyData/fr|Closed}}: voir [Options](#Options.md).

-    {{PropertyData/fr|Refine}}: true ou false. Si la valeur est true, nettoie le solide des arêtes résiduelles laissées par les fonctions. Voir [Part Affiner la forme](Part_RefineShape/fr.md) pour plus de détails.

-    {{PropertyData/fr|Profile}}: l\'objet de profil de base voir du lissage.

-    {{PropertyData/fr|Midplane}}: non applicable.

-    {{PropertyData/fr|Inversé}}: non applicable.

-    {{PropertyData/fr|Up To Face}}: non applicable.

-    {{PropertyData/fr|Allow Multi Face}}: non applicable.

## Limitations

-   Les esquisses doivent former des profils fermées.
-   Il n\'est pas possible de faire un lissage avec un sommet.
-   Une section ne peut pas se trouver sur le même plan que celui qui la précède immédiatement.
-   Pour mieux contrôler la forme du lissage, il est recommandé que toutes les sections transversales aient le même nombre de segments. Par exemple, pour un lissage entre un rectangle et un cercle, le cercle peut être décomposé en 4 arcs connectés.
-   Le lissage sera créé dans l\'ordre dans lequel les coupes transversales ont été ajoutées.
-   Si l\'esquisse a une géométrie intérieure, c\'est-à-dire que le lissage est censé avoir des trous, alors l\'ordre dans lequel la géométrie de l\'esquisse est créée doit être le même pour toutes les sections: commencez soit avec toutes les sections avec la géométrie intérieure, ou commencez-les toutes avec la géométrie extérieure . Sinon, un lissage non valide peut être créé à la croisée des murs intérieurs et extérieurs.

## Problèmes connus {#problèmes_connus}

-   Certains modes d\'échec vont transformer la pièce en noir

## Liens

-   [Part Détails techniques du lissage](Part_Loft_Technical_Details/fr.md) explique comment un [Part Lissage](Part_Loft/fr.md) est créé, une grande partie de son contenu est pertinente pour le Lissage additif de PartDesign.





{{PartDesign Tools navi

}} 
