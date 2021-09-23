---
- GuiCommand:/fr
   Name:PartDesign SubtractiveLoft
   Name/fr:PartDesign Lissage soustractif
   MenuLocation:Conception de pièces → Créer une fonction soustractive → Enlèvement de matière par lissage
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
   Version:0.17
   SeeAlso:[PartDesign Lissage additif](PartDesign_AdditiveLoft/fr.md), [PartDesign Balayage soustractif](PartDesign_SubtractivePipe/fr.md)
---

# PartDesign SubtractiveLoft/fr

## Description

Le **Lissage soustractif** crée un solide soustractif dans le corps actif en effectuant une transition entre deux esquisses ou plus (également appelés coupes transversales). Sa forme est ensuite soustraite du solide existant.

## Utilisation

### Déroulement du travail basé sur la boîte de dialogue 

1.  Appuyez sur le bouton **<img src=images/PartDesign_SubtractiveLoft.svg style="width:24px"> [Lisser un profil sélectionné...](PartDesign_SubtractiveLoft/fr.md)**.
2.  Dans la boîte de dialogue **Sélectionner une fonction**, sélectionnez une esquisse à utiliser comme objet de profil de base et cliquez sur **OK**.
    -   Alternativement, une seule esquisse peut être sélectionnée avant d\'appuyer sur le bouton de lissage soustractif.
3.  Dans **Paramètres de lissage**, appuyez sur le bouton **Ajouter une section**.
4.  Sélectionnez l\'esquisse suivante dans la [vue 3D](3D_view/fr.md). Répétez pour sélectionner d\'autres esquisses dans l\'ordre dans lequel vous voulez qu\'elles soient lissées. (Vous pouvez modifier l\'ordre des sections à tout moment ultérieurement dans la boîte de dialogue de lissage en faisant glisser les sections de la liste vers la position souhaitée. {{Version/fr|0.19}})
5.  Définissez les options si nécessaire et cliquez sur **OK**.

### Déroulement du travail basé sur la sélection 


{{Version/fr|0.19}}

1.  Sélectionnez plusieurs esquisses. L\'ordre dans lequel vous les sélectionnez est important:
    -   L\'esquisse sélectionnée au départ deviendra l\'objet de profil de base à l\'étape suivante.
    -   Les esquisses sélectionnées après la première deviendront les sections du lissage. Ici aussi, l\'ordre de sélection est important: la deuxième esquisse sélectionnée deviendra la première section de lissage, celle sélectionnée comme troisième deviendra la deuxième section et ainsi de suite. (Vous pouvez modifier l\'ordre des sections à tout moment ultérieurement dans la boîte de dialogue de lissage en faisant glisser les sections de la liste vers la position souhaitée. {{Version/fr|0.19}})
2.  Appuyez sur le bouton **<img src=images/_PartDesign_SubtractiveLoft.svg style="width:24px"> [Lisser un profil sélectionné...](PartDesign_SubtractiveLoft/fr.md)**.
3.  Définissez les options si nécessaire et cliquez sur **OK**.

## Options

-   **Surface réglée** : effectue des transitions droites entre les sections. Ne s\'applique pas à un lissage avec deux sections transversales. Si cette case n\'est pas cochée, les transitions seront lisses.
-   **Fermé** : effectue une transition de la dernière section à la première, en créant une boucle.

## Propriétés

-    {{PropertyData/fr|Label}}: nom donné à l\'opération, ce nom peut être changé à la convenance.

-    {{PropertyData/fr|Sections}}: liste les sections utilisées.

-    {{PropertyData/fr|Ruled}}: voir [Options](#Options.md).

-    {{PropertyData/fr|Closed}}: voir [Options](#Options.md).

-    {{PropertyData/fr|Midplane}}: N/A

-    {{PropertyData/fr|Reversed}}: N/A

-    {{PropertyData/fr|Refine}}: vrai ou faux. Si la valeur est \"true\" (vrai), nettoie le solide des bords résiduels laissés par les entités. Voir [Affiner la forme](Part_RefineShape/fr.md) pour plus de détails.

## Limites

-   Les esquisses doivent être toutes fermées.
-   Il n\'est pas possible de faire un lissage avec un sommet.
-   Une section ne peut pas être sur le même plan que celle qui la précède.
-   Pour un meilleur résultat sur le lissage, il est recommandé que toutes les sections aient le même nombre de segments. Par exemple, pour un lissage entre un rectangle et un cercle, le cercle peut être décomposé en 4 arcs connectés.

## Liens

-   [Part Détails techniques du lissage](Part_Loft_Technical_Details/fr.md) explique comment un [Lissage](Part_Loft/fr.md) est créé, une grande partie de son contenu est pertinente pour le Lissage soustractif de PartDesign.





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveLoft/fr
