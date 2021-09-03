---
- GuiCommand:/fr
   Name:PartDesign Chamfer
   Name/fr:PartDesign Chanfrein
   MenuLocation:Conception de pièces → Appliquer une fonction d'habillage → Chanfrein
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
   SeeAlso:[PartDesign Congé](PartDesign_Fillet/fr.md), [Part Chanfrein](Part_Chamfer/fr.md)
---

## Description

Cet outil crée des chanfreins sur les arêtes sélectionnées d\'un objet. Une nouvelle entrée distincte de chanfrein (suivie d\'un numéro consécutif s\'il existe déjà des chanfreins dans le document) est créée dans l\'arborescence du projet.

## Utilisation

-   Sélectionnez une seule arête, plusieurs arêtes ou une face sur un objet, puis démarrez l\'outil en cliquant sur le **<img src="images/PartDesign_Chamfer.svg" width=24px> '''Chanfreiner les arêtes...'''** ou par le menu **Part Design → Apply a dress-up feature → Chanfrein**. Si vous avez sélectionné une face, toutes ses arêtes sont respectées pour le chanfreinage.
-   Dans le [Panneau des tâches](Task_Panel/fr.md) qui apparaît, vous pouvez définir la chambre de 3 manières :
    -   **Equal distance** : les chanfreins sont également distants du bord du corps.
    -   **Two distances** : Les distances du bord de chanfrein au bord du corps sont spécifiées. La direction de la distance peut être inversée. {{Version/fr|0.19}}
    -   **Distance and angle** : Une distance du bord de chanfrein au bord du corps est spécifiée. Le deuxième bord de chanfrein est défini par l\'angle du chanfrein. La direction de la distance peut être inversée. {{Version/fr|0.19}}
-   Si vous souhaitez ajouter plus d\'arêtes ou de faces, cliquez sur le bouton **Ajouter** et sélectionnez les arêtes et/ou les faces.
-   Si vous souhaitez supprimer des arêtes ou des faces
    -   Sélectionnez l\'arête/la face dans la liste de la boîte de dialogue et appuyez sur la touche **Suppr**. *Remarque* : puisqu\'il doit y avoir au moins une arête pour la fonction, la dernière arête ou face restante dans la liste ne peut pas être supprimée.
    -   ou cliquez sur le bouton **Supprimer**. Toutes les arêtes et faces sélectionnées précédemment sont surlignées en violet. Sélectionnez l\'arête ou la face à supprimer.
-   Cliquez sur **OK** pour valider.
-   Pour une chaîne d\'arêtes tangentes les unes aux autres, une seule arête peut être sélectionnée ; le chanfrein se propage le long de la chaîne.
-   Pour modifier le chanfrein après la validation de la fonction, double-cliquez sur l\'étiquette du chanfrein dans l\'arborescence du projet, ou faites un clic droit dessus et sélectionnez **Modifier chanfrein**.

## PartDesign Chanfrein versus Part Chanfrein 

**Le PartDesign Chanfrein ne doit pas être confondu avec le [Part Chanfrein](Part_Chamfer/fr.md)**. Bien qu\'ils partagent la même icône, ils ne sont pas identiques et ne sont pas utilisés de la même manière. La principale différence est que le PartDesign Chanfrein crée une entrée de chanfrein distincte (suivie d\'un numéro séquentiel s\'il existe déjà des chanfreins) dans l\'arborescence du projet pour le corps en cours. Le Part Chanfrein devient le parent de l\'objet auquel il a été appliqué.





{{PartDesign Tools navi

}} 
