---
 GuiCommand:
   Name: Mesh Evaluation
   Name/fr: Mesh Évaluation
   MenuLocation: Maillages , Analyser , Évaluer et réparer un maillage...
   Workbenches: Mesh_Workbench/fr
---

# Mesh Evaluation/fr

## Description

La commande **Évaluation** évalue et répare un objet maillé.

<img alt="" src=images/Mesh_Evaluation_dialog.png  style="width:300px;"> 
*La fenêtre de dialogue Évaluer et réparer un maillage avec l'option ''Recherche de plis sur une surface'' activée*



## Utilisation

1.  Sélectionnez un seul objet maillé.
2.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Mesh_Evaluation.svg" width=16px> [Évaluer et réparer un maillage...](Mesh_Evaluation/fr.md)
**
    -   Sélectionnez l\'option **Maillages → Analyser → <img src="images/Mesh_Evaluation.svg" width=16px> Évaluer et réparer un maillage...** du menu.
3.  La fenêtre de dialogue **Évaluer et réparer un maillage** s\'ouvre.
4.  Appuyez sur le bouton **Paramètres...** pour modifier les paramètres suivants :
    -   
        **Rechercher des points non-manifolds**
        

    -   
        **Activer la recherche de plis sur une surface**
        

    -   
        **Ne considérer que les faces de surface nulle comme dégénérées**
        
5.  Si vous n\'avez pas encore sélectionné d\'objet maillé : sélectionnez-en un dans la liste déroulante en haut de la fenêtre de dialogue.
6.  La fenêtre de dialogue contient 7 ou 8 options de test (si l\'option **Plis sur la surface** est activée).
7.  N\'utilisez pas les cases à cocher, elles seront vérifiées automatiquement si des erreurs sont trouvées.
8.  Appuyez sur l\'un des boutons **Analyser** pour démarrer un test.
9.  Ou utilisez le bouton **Analyser** de l\'option **Tous les tests ci-dessus combinés** pour exécuter les 7 ou 8 tests ensemble.
10. Les erreurs seront indiquées dans la fenêtre de dialogue, ainsi que, avec des marqueurs jaunes et rouges, dans la [vue 3D](3D_view/fr.md).
11. Vous pouvez appuyer sur un ou plusieurs boutons **Réparer** pour réparer les erreurs trouvées.
12. Vous pouvez appuyer sur le bouton **Réinitialiser** pour réinitialiser tous les résultats de test. Cela réinitialisera la fenêtre de dialogue et supprimera les marqueurs colorés de la vue 3D. Si vous souhaitez répéter le même test ou exécuter tous les tests ensemble, il n\'est pas nécessaire de le faire.
13. Sélectionnez un autre objet de maillage dans la liste déroulante pour continuer les tests et la réparation.
14. Appuyez sur le bouton **Fermer** pour fermer la fenêtre de dialogue et terminer la commande.
15. Le bouton **Actualiser** ne fonctionne pas correctement pour le moment.



## Remarques

-   La réparation d\'un maillage peut signifier que les éléments problématiques sont supprimés du maillage, ce qui entraîne des trous. Les trous peuvent être fermés avec les commandes [Mesh Remplir les trous](Mesh_FillupHoles/fr.md), [Mesh Boucher un trou](Mesh_FillInteractiveHole/fr.md) et [Mesh Ajouter une facette](Mesh_AddFacet/fr.md).
-   Voir [ce fil du forum](https://forum.freecadweb.org/viewtopic.php?f=3&p=533252#p533252) pour une explication de la structure de données du maillage. Ces informations peuvent aider à comprendre pourquoi un maillage a des problèmes.



## Préférences

-   Le paramètre **Rechercher des points non-manifolds** est enregistré : **Outils → Éditer les paramètres... → BaseApp → Preferences → Mod → Mesh → Evaluation → CheckNonManifoldPoints**.
-   Le paramètre **Activer la recherche de plis sur une surface** est enregistré : **Outils → Éditer les paramètres... → BaseApp → Preferences → Mod → Mesh → Evaluation → EnableFoldsCheck**.
-   Le paramètre **Ne considérer que les faces de surface nulle comme dégénérées** est enregistré : **Outils → Éditer les paramètres... → BaseApp → Preferences → Mod → Mesh → Evaluation → StrictlyDegenerated**.





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh Evaluation/fr
