---
 GuiCommand:
   Name: Assembly CreateSimulation
   Name/fr: Assembly Simulation
   MenuLocation: Assemblage , Créer une simulation
   Workbenches: Assembly_Workbench/fr
   Shortcut: **S**
   Version: 1.1
   SeeAlso: 
---

# Assembly CreateSimulation/fr

## Description

L\'outil <img alt="" src=images/Assembly_CreateSimulation.svg  style="width:32px;"> [Assembly Simulation](Assembly_CreateSimulation/fr.md) crée une simulation de l\'assemblage en cours.



## Utilisation

1.  Assurez-vous qu\'un assemblage est actif.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/Assembly_CreateSimulation.svg" width=16px> [Créer une simulation](Assembly_CreateSimulation/fr.md)**.
    -   Sélectionnez l\'option **Assemblage → <img src="images/Assembly_CreateSimulation.svg" width=16px> Créer une simulation** du menu.
    -   Utilisez le raccourci clavier : **S**.
3.  Si aucun objet Simulations ne préexiste : un conteneur Simulations est ajouté à l\'assemblage actif.
4.  Un objet Simulation est ajouté au conteneur Simulations.
5.  Le [panneau des tâches](Task_panel/fr.md) **Créer une simulation** s\'ouvre.
6.  Appuyez sur le bouton vert plus pour ouvrir une fenêtre de dialogue.
    -   Sélectionnez une liaison dans la liste.
    -   Si nécessaire, sélectionnez un type de mouvement.
    -   Vous pouvez éditer la formule.
    -   Appuyez sur le bouton **OK** pour fermer la fenêtre de dialogue.
7.  Vous pouvez ajuster les paramètres de simulation.
8.  Cliquez sur le bouton **Générer**.
9.  Une section **Lecteur de l\'animation** est ajoutée au panneau des tâches.
    -   Utilisez les widgets du lecteur pour animer l\'assemblage.
10. Cliquez sur le bouton **OK** pour arrêter l\'outil et fermer le panneau des tâches.



## Remarques

-   La fenêtre de dialogue sans nom permet de définir un opérateur :
    1.  Sélectionnez la liaison souhaitée dans la liste des **Liaisons**.
    2.  S\'il y a plus d\'une transformation disponible avec la liaison sélectionnée, sélectionnez-en une dans la liste **Type de mouvement**.
    3.  Modifiez la formule qui décrit la relation entre le temps de fonctionnement et l\'angle ou la distance parcourue.
    4.  Si vous le souhaitez, vous pouvez appuyer sur le bouton Aide pour voir des exemples de descriptions de **Formule**.
-   Dans la formule, **time** semble représenter 1 rad par seconde, et avec 360° = 6,283 rad pour une rotation complète, nous pouvons faire l\'une ou l\'autre chose :
    -   Saisir {{Value|6.283 * time}} dans le champ Formule et définir une durée (Valeur finale - Valeur de départ) d\'une seconde sous Paramètres de simulation dans le panneau des tâches.
    -   Saisir {{Value|1 * time}} dans le champ Formule et fixer une durée (Valeur finale - Valeur de départ) de 6,283 secondes sous Paramètres de simulation dans le panneau des tâches.



## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)



### Simulations

Un conteneur **Simulations** est un objet {{Incode|Assembly::SimulationGroup}} dérivé d\'un objet [App DocumentObjectGroup](App_DocumentObjectGroup/fr.md) et héritant de toutes ses propriétés. Il n\'a pas de propriétés supplémentaires.



### Simulation

Un objet **Simulation** est dérivé d\'un [App FeaturePython](App_FeaturePython/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :



### Données


{{Properties_Title|Base}}

-    **Group|LinkList**: objets de mouvement de l\'objet.

-    **_ Group Touched|Bool|Hidden**:


{{Properties_Title|Simulation}}

-    **a Time Start|Time**: par défaut {{value|0.0 s}}. Début de la simulation.

-    **b Time End|Time**: par défaut {{value|4.0 s}}. Fin de simulation.

-    **c Time Step Output|Time**: par défaut {{value|0.01 s}}. Pas du temps de la simulation.

-    **f Global Error Tolerance|Float**: par défaut {{value|1e-06}}. Tolérance d\'erreur globale de l\'intégration.

-    **j Frames par seconde|Integer**: par défaut {{value|30}}. Nombre d\'images par seconde.



### Vue


{{Properties_Title|Space}}

-    **Decimals|Integer**: par défaut {{value|9}}. Nombre de décimales à utiliser pour les textes calculés.



### Mouvement

Un objet **Motion** est dérivé d\'un [App FeaturePython](App_FeaturePython/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :



### Données 


{{Properties_Title|Motion}}

-    **Formula|String**: formule du mouvement. Par exemple {{Value|1.0*time}}.

-    **Joint|XLinkSubHidden**: liaison déplacée par le mouvement.

-    **Motion Type|Enumeration**: type de mouvement. Les options sont les suivantes : {{Value|Angular}} et {{Value|Linear}}.





{{Assembly_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Assembly](Assembly_Workbench.md) > Assembly CreateSimulation/fr
