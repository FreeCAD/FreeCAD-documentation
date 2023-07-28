---
- GuiCommand:/fr
   Name:Part_Fillet
   Name/fr:Part Congé
   MenuLocation:Part → Congé...
   Workbenches:[Part](Part_Workbench/fr.md)
   SeeAlso:[Part Chanfrein](Part_Chamfer/fr.md)
---

# Part Fillet/fr

## Description

Cet outil crée des congés (arrondis) sur les bords sélectionnés d\'une forme. Une boîte de dialogue permet de choisir la forme et les bords sur lesquels travailler.



## Utilisation

-   Lancez l\'outil à partir de la barre d\'outils Part ou du menu **Part → Congé...**. Vous pouvez sélectionner la forme avant de lancer l\'outil.
-   Si la forme n\'a pas été sélectionnée avant de lancer l\'outil, sélectionnez-la dans la liste déroulante du [panneau des tâches](Task_panel/fr.md).
-   Sélectionnez le type de congé, soit un rayon constant (par défaut) soit un rayon variable.
-   Sélectionnez les arêtes soit dans la [vue 3D](3D_view/fr.md) ou en les cochant dans la liste des arêtes dans le [panneau des tâches](Task_panel/fr.md).
-   Définissez la valeur du rayon.
-   Cliquez sur **OK** pour valider.

![](images/Dialog-fillet.png )

## Comparaison PartDesign Congé et Part Congé 

Il existe un autre outil de congé dans l\'<img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [atelier PartDesign](PartDesign_Workbench/fr.md). Veuillez noter que leur fonctionnement est assez différent. Consultez la page de référence <img alt="" src=images/PartDesign_Fillet.svg  style="width:24px;"> [PartDesign Congé](PartDesign_Fillet/fr.md) pour plus de détails sur leurs différences.

## Remarques pour l\'application de Part Congé 

Part Congé peut ne rien faire si le résultat touche ou traverse le bord adjacent suivant. Par conséquent, si vous n\'obtenez pas le résultat escompté, essayez avec une valeur de **Rayon** plus petite. Il en est de même pour <img alt="" src=images/Part_Chamfer.svg  style="width:24px;"> [Part Chanfrein](Part_Chamfer/fr.md).

L\'outil Congé échoue parfois lorsqu\'il tente de faire des congés sur des formes complexes. Une cause fréquente de cet échec est que la forme recevant le congé n\'est géométriquement pas correcte. Cela peut être le résultat de lignes/plans, etc. qui n\'ont pas été supprimés après les précédentes opérations utilisées pour construire la forme (par exemple, coupe/intersection/union). Un certain nombre d\'étapes peuvent être utilisées pour minimiser les problèmes :

-   Dans la mesure du possible, laissez le congé d\'une pièce jusqu\'à ce que la pièce soit complètement générée. Cela minimisera l\'interaction des congés avec les opérations booléennes suivantes ;
-   Utilisez la **Part → Vérifier la géométrie** pour vérifier les erreurs éventuelles dans la géométrie de la forme et les corriger ;
-   Utilisez **Part → Créer une copie → Affiner la forme** pour supprimer tout artefact introduit par les opérations booléennes précédentes avant le congé (et dans certains cas entre les opérations de congé en séquence) ;
-   Envisagez d\'utiliser **Édition → Préférences → PartDesign** pour activer la vérification et l\'affinage automatiques du modèle après les opérations booléennes et basées sur des esquisses (les performances peuvent être affectées si ces options restent activées).

L\'outil Congé est sensible au [Problème de dénomination topologique](Topological_naming_problem/fr.md) lors d\'une modification d\'une étape de modélisation antérieure dans la chaîne qui affecte le nombre de faces ou de sommets. Cela pourrait entraîner des résultats imprévisibles. Jusqu\'à ce que ce problème soit résolu, il est conseillé d\'appliquer les opérations de chanfrein et de congé comme dernières étapes de la chaîne de modélisation.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Fillet/fr
