---
- GuiCommand:/fr
   Name:Part_Fillet
   Name/fr:Part Congé
   MenuLocation:Pièce → Congé
   Workbenches:[Part](Part_Workbench/fr.md)
   SeeAlso:[Part Chanfrein](Part_Chamfer/fr.md)
---


</div>

## Description

Cet outil crée un congé (arrondi) sur les arêtes sélectionnées d\'un objet. Une boîte de dialogue vous permet de choisir les objets et les arêtes à utiliser.

## Utilisation

-   Lancez l\'outil à partir de la barre d\'outils de la pièce ou du menu. Vous pouvez sélectionner l\'objet avant ou après le démarrage de l\'outil.
-   Si la forme n\'a pas été sélectionnée avant de démarrer l\'outil, sélectionnez-la dans la liste déroulante du [Panneau des tâches](Task_panel/fr.md).
-   Sélectionnez le type de congé, soit un rayon constant (par défaut) ou un rayon variable.
-   Sélectionnez les arêtes soit dans la [vue 3D](3D_view/fr.md) ou en les cochant dans la liste des arêtes dans le [Panneau des tâches](Task_panel/fr.md).
-   Définissez la valeur du rayon.
-   Cliquez sur **OK** pour valider.

![](images/Dialog-fillet.png )

## Comparaison PartDesign Congé et Part Congé 

Il existe un autre outil de congé dans l\'<img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [atelier PartDesign](PartDesign_Workbench/fr.md). Veuillez noter que leur fonctionnement est assez différent. Consultez la page de référence <img alt="" src=images/PartDesign_Fillet.svg  style="width:24px;"> [PartDesign Congé](PartDesign_Fillet/fr.md) pour plus de détails sur leurs différences.

## Remarques pour l\'application de Part Congés 

Le congé de pièce peut ne rien faire si le résultat touche ou traverse le prochain bord adjacent. Donc, si vous n\'obtenez pas le résultat attendu, essayez avec une valeur inférieure. C\'est la même chose pour <img alt="" src=images/Part_Chamfer.svg  style="width:24px;"> [Part Chanfrein](Part_Chamfer/fr.md).

L\'outil Congé échoue parfois lors de la tentative de congé sur des objets complexes. Une cause commune peut être que la forme recevant le congé n\'est pas géométriquement correcte. Cela peut être dû au fait que les lignes/plans ne sont pas supprimés après les opérations précédentes utilisées pour construire la forme (par exemple, Cut/Intersection/Fusion). Un certain nombre d\'étapes peuvent être utilisées pour minimiser les problèmes:

-   Si possible, attendez pour la création des congés d\'une pièce que la pièce soit complètement générée. Cela minimisera l\'interaction des congés avec les opérations booléennes suivantes;
-   Utilisez la commande **Pièce → Vérifier la géométrie** pour rechercher d\'éventuelles erreurs dans la géométrie de la forme et les corriger.
-   Utilisez **Pièce → Affiner la forme** pour supprimer les artefacts introduits par les opérations booléennes précédentes avant le congé (et dans certains cas, entre les opérations de congé en séquence);
-   Envisagez d\'utiliser **Édition → Préférences → PartDesign** pour activer la vérification automatique et le raffinage du modèle après des opérations booléennes et basées sur des esquisses (les performances peuvent être affectées si ces options sont laissées activées).

Notez également que la fonction de congé de pièce est affectée par le [Problème de dénomination topologique](Topological_naming_problem/fr.md) lorsque toute modification est apportée à une étape de modélisation plus tôt dans la chaîne qui affecte le nombre de facettes ou de sommets. Cela pourrait entraîner des résultats imprévisibles. En attendant que cela soit résolu (éventuellement avec la V0.19), il est conseillé d'appliquer les opérations Chanfrein et [Congé](Part_Fillet/fr.md) aux dernières étapes de la chaîne.


<div class="mw-translate-fuzzy">





</div>


  
