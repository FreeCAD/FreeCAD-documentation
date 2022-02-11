---
- GuiCommand:/fr
   Name:PartDesign Chamfer
   Name/fr:PartDesign Chanfrein
   MenuLocation:Conception de pièces → Appliquer une fonction d'habillage → Chanfrein
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
   SeeAlso:[PartDesign Congé](PartDesign_Fillet/fr.md), [Part Chanfrein](Part_Chamfer/fr.md)
---

# PartDesign Chamfer/fr

## Description

Cet outil crée des chanfreins sur les arêtes sélectionnées d\'un objet. Une nouvelle entrée distincte de chanfrein (suivie d\'un numéro consécutif s\'il existe déjà des chanfreins dans le document) est créée dans l\'arborescence du projet.

## Utilisation

-   Sélectionnez une seule arête, plusieurs arêtes ou une face sur un objet, puis lancez l\'outil en cliquant sur le **<img src="images/PartDesign_Chamfer.svg" width=24px> '''Chanfrein'''** ou par le menu **Conception de pièces → Appliquer une fonction d'habillage → Chanfrein**. Si vous avez sélectionné une face ou un objet 3D ({{Version/fr|0.20}}), toutes ses arêtes sont prises en compte pour le chanfreinage.
-   Dans le [Panneau des tâches](Task_Panel/fr.md) qui apparaît, vous pouvez définir le chanfrein de 3 manières :
    -   
        **Cote égale**
        
        : les chanfreins sont également distants du bord du corps.

    -   
        **Deux cotes**
        
        : les distances du bord de chanfrein au bord du corps sont spécifiées. La direction de la distance peut être inversée. {{Version/fr|0.19}}

    -   
        **Cote et angle**
        
        : une distance du bord de chanfrein au bord du corps est spécifiée. Le deuxième bord de chanfrein est défini par l\'angle du chanfrein. La direction de la distance peut être inversée. {{Version/fr|0.19}}
-   Si vous souhaitez ajouter plus d\'arêtes ou de faces, cliquez sur le bouton **Ajouter** et sélectionnez les arêtes et/ou les faces.
-   Après avoir cliqué sur le bouton **Ajouter**, vous pouvez ajouter toutes les arêtes de l\'objet en faisant un clic droit et en sélectionnant **Ajouter tous les bords** dans le menu contextuel. {{Version/fr|0.20}}
-   Si vous souhaitez supprimer des arêtes ou des faces:
    -   Sélectionnez l\'arête/la face dans la liste de la boîte de dialogue et appuyez sur la touche **Suppr**. *Remarque* : puisqu\'il doit y avoir au moins une arête pour la fonction, la dernière arête ou face restante dans la liste ne peut pas être supprimée.
    -   ou cliquez sur le bouton **Supprimer**. Toutes les arêtes et faces sélectionnées précédemment sont surlignées en violet. Sélectionnez l\'arête ou la face à supprimer.
    -   Assurez-vous que la case **Utiliser tous les bords** n\'est pas cochée, sinon certains widgets de la boîte de dialogue seront désactivés. {{Version/fr|0.20}}
-   Cliquez sur **OK** pour valider.
-   Pour une chaîne d\'arêtes tangentes les unes aux autres, une seule arête peut être sélectionnée ; le chanfrein se propage le long de la chaîne.
-   Pour modifier le chanfrein après la validation de la fonction, double-cliquez sur l\'étiquette du chanfrein dans l\'arborescence du projet, ou faites un clic droit dessus et sélectionnez **Modifier le chanfrein**.

## Remarques

-   Le PartDesign Chanfrein ne doit pas être confondu avec le [Part Chanfrein](Part_Chamfer/fr.md). À moins que vous ne sachiez ce que vous faites, [Part Chanfrein](Part_Chamfer/fr.md) ne doit pas être utilisé sur un corps PartDesign. Voir [Part et PartDesign](Part_and_PartDesign/fr.md).

## Problèmes connus 

Voir [PartDesign Congé](PartDesign_Fillet/fr#Probl.C3.A8mes_connus.md).





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Chamfer/fr
