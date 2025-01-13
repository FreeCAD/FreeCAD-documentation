---
 GuiCommand:
   Name: CAM Simulateur GL
   MenuLocation: CAM , Simuler le parcours 
   Workbenches: CAM_Workbench/fr
   Shortcut: **P** **N**
   Version: 1.0
   SeeAlso: CAM_Simulator/fr
---

# CAM SimulatorGL/fr

## Description

L\'outil <img alt="" src=images/CAM_SimulatorGL.svg  style="width:24px;"> [Simulateur GL](CAM_SimulatorGL/fr.md) est une nouvelle alternative au [Simulateur de parcours](CAM_Simulator/fr.md). Il est basé sur des fonctions OpenGL de bas niveau. Pour éliminer les interférences avec la vue 3D de FreeCAD, il fonctionne dans une fenêtre séparée avec un contexte OpenGL séparé. Il est censé être plus rapide et plus précis que l\'ancien simulateur.

<img alt="" src=images/CAM_new_simulator.PNG  style="width:600px;">



## Utilisation

1.  Il y a plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/CAM_SimulatorGL.svg" width=16px> [Simuler le parcours (nouvelle version)](CAM_SimulatorGL/fr.md)**.
    -   Sélectionnez l\'option **CAM → <img src="images/CAM_Simulator.svg" width=16px> Simuler le parcours (nouvelle version)** du menu.
    -   Utilisez le raccourci clavier : **P** puis **N**.
2.  Désélectionnez toutes les **Opérations** qui ne doivent pas être simulées.
3.  Réglez le paramètre **Précision**.
4.  Sélectionnez la **Tâche** à simuler dans le menu déroulant.
5.  Appuyez sur le bouton <img alt="" src=images/CAM_BPlay.svg  style="width:24px;"> (Activer/reprendre la simulation).
    -   Une fenêtre séparée avec le simulateur s\'ouvre.
    -   Utilisez les boutons de gauche : Exécuter, Pas à pas et Avance rapide et le curseur pour contrôler l\'animation.
    -   Utilisez les boutons de droite pour : Afficher/masquer la superposition du modèle de base, Orbiter le modèle, Afficher la trajectoire et Activer/désactiver l\'occlusion ambiante.
    -   Contrôlez la vue 3D avec les commandes de souris en cours dans FreeCAD.



## Propriétés

-    **Accuracy**: précision de la simulation, exprimée en pourcentage, indique l\'écart de la simulation par rapport à la tâche. Pour les simulations interactives, la réduction de la précision à 0.3 est beaucoup plus rapide.

-    **Job**: tâche utilisée comme base de la simulation

-    **Operation List**: liste des opérations sélectionnées pour être incluses dans la simulation.





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM SimulatorGL/fr
