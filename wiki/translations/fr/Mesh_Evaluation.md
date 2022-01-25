---
- GuiCommand:/fr
   Name:Mesh Evaluation
   Name/fr:Mesh Evaluation
   MenuLocation:Maillages → Analyser → Évaluer et réparer le maillage...
   Workbenches:[Mesh](Mesh_Workbench/fr.md)
---

# Mesh Evaluation/fr

## Description

La commande **Mesh Evaluation** évalue et répare un objet maillé.

![](images/Mesh_Evaluation_dialog.png ) 
*La boîte de dialogue Evaluer et réparer le maillage avec l'option Folds (plis) active sur la surface activée*

## Utilisation

1.  Sélectionnez éventuellement un seul objet maillé.
2.  Il existe plusieurs façons d\'appeler la commande:
    -   Appuyez sur le bouton **<img src="images/Mesh_Evaluation.svg" width=16px> [Ouvre une fenêtre permettant d'analyser et de réparer un maillage](Mesh_Evaluation/fr.md)
**
    -   Sélectionnez l\'option **Maillages → Analyser → <img src="images/Mesh_Evaluation.svg" width=16px> Évaluer et réparer le maillage...** dans le menu.
3.  La boîte de dialogue **Évaluer et réparer un maillage** s\'ouvre.
4.  Appuyez éventuellement sur le bouton **Paramètres...** pour modifier les paramètres suivants:
    -   
        **Recherche de points libres "non-manifolds"**
        

    -   
        **Active la recherche de plis sur une surface**
        

    -   
        **Considère uniquement les faces de surface nulle comme dégénérées**
        
5.  Si vous n\'avez pas encore sélectionné d\'objet maillé: sélectionnez-en un dans la liste déroulante en haut de la boîte de dialogue.
6.  La boîte de dialogue contient 7 ou 8 options de test (si l\'option **Se replie sur la surface** est activée).
7.  N\'utilisez pas les cases à cocher, elles seront vérifiées automatiquement si des erreurs sont trouvées.
8.  Appuyez sur l\'un des boutons **Analyser** pour démarrer un test.
9.  Ou utilisez le bouton **Analyser** de l\'option **Tous les tests ensembles** pour exécuter les 7 ou 8 tests ensemble.
10. Les erreurs seront indiquées dans la boîte de dialogue, ainsi que, avec des marqueurs jaunes et rouges, dans la [vue 3D](3D_view/fr.md).
11. Appuyez éventuellement sur un ou plusieurs boutons **Réparer** pour réparer les erreurs trouvées.
12. Appuyez éventuellement sur le bouton **Réinitialiser** pour réinitialiser tous les résultats de test. Cela réinitialisera la boîte de dialogue et supprimera les marqueurs colorés de la vue 3D. Si vous souhaitez répéter le même test ou exécuter tous les tests ensemble, il n\'est pas nécessaire de le faire.
13. Sélectionnez éventuellement un autre objet de maillage dans la liste déroulante pour continuer les tests et la réparation.
14. Appuyez sur le bouton **Fermer** pour fermer la boîte de dialogue et terminer la commande.
15. Le bouton **Actualiser** ne fonctionne pas correctement pour le moment.

## Remarques

-   La réparation d\'un maillage peut signifier que les éléments problématiques sont supprimés du maillage, ce qui entraîne des trous. Les trous peuvent être fermés avec les commandes [Mesh Remplir les trous](Mesh_FillupHoles/fr.md), [Mesh Boucher un trou](Mesh_FillInteractiveHole/fr.md) et [Mesh Ajouter un facette](Mesh_AddFacet/fr.md).
-   Voir [ce fil du forum](https://forum.freecadweb.org/viewtopic.php?f=3&p=533252#p533252) pour une explication de la structure de données du maillage. Ces informations peuvent aider à comprendre pourquoi un maillage a des problèmes.

## Préférences

-   Le paramètre **Rechercher de points libres non-manifolds** est stocké: **Outils → Editer les paramètres... → BaseApp → Preferences → Mod → Mesh → Evaluation → CheckNonManifoldPoints**.
-   Le paramètre **Active la recherche de plis sur une surface** est stocké: **Outils → Editer les paramètres... → BaseApp → Preferences → Mod → Mesh → Evaluation → EnableFoldsCheck**.
-   Le paramètre **Considère uniquement les faces de surface nulle comme dégénérées** est stocké: **Outils → Editer les paramètres... → BaseApp → Preferences → Mod → Mesh → Evaluation → StrictlyDegenerated**.





{{Mesh Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh Evaluation/fr
