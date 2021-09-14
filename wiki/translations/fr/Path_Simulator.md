---
- GuiCommand:/fr
   Name:Path Simulator
   Name/fr:Path Simulateur d'usinage
   MenuLocation:Path → Simulateur FAO
   Workbenches:[Path](Path_Workbench/fr.md)
   Shortcut:**P** **M**
   SeeAlso:[Path Inspecteur de G-code](Path_Inspect/fr.md)
---

## Description

Cet outil permet de simuler la tâche Path en balayant les modèles 3D des outils utilisés dans chaque opération, le long des trajectoires du G-code, en soustrayant le matériau du stock, là où le stock et l\'outil se chevauchent, ce qui permet de visualiser le travail. Cela permet de détecter et d\'isoler les erreurs avant d\'exécuter le travail sur une fraiseuse.

![](images/Path-Simulation.gif )

## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Path_Simulator.svg" width=16px> [Simulateur FAO](Path_Simulator/fr.md)**.
    -   Sélectionnez l\'option **Path → <img src="images/Path_Simulator.svg" width=16px> Simulateur FAO** dans le menu.
    -   Utilisez le raccourci clavier : **P** puis **M**.
2.  Désélectionnez toutes les **Operations** qui ne doivent pas être simulées.
3.  Réglez les paramètres de **Speed** et **Accuracy**.
4.  Sélectionnez la tâche **Job** à simuler dans le menu déroulant.
5.  Utilisez la barre d\'outils **Simulateur de trajets** pour invoquer différentes actions :
    -   Appuyez sur le bouton <img alt="" src=images/Path_BPlay.svg  style="width:24px;"> (Play) pour lire ou reproduire une animation des opérations.
    -   Appuyez sur le bouton <img alt="" src=images/Path_BFastForward.svg  style="width:24px;"> (Fast Forward) pour augmenter sensiblement la vitesse (afin de revoir rapidement des chemins compliqués).
    -   Appuyez sur le bouton <img alt="" src=images/Path_BPause.svg  style="width:24px;"> (Pause) pour mettre l\'animation en pause à des fins de dépannage.
    -   Appuyez sur le bouton <img alt="" src=images/Path_BStep.svg  style="width:24px;"> (Single-Step) pour ralentir l\'animation, cette fonctionnalité permet de dépanner et de résoudre des coupes et/ou des mouvements spécifiques.
    -   Appuyez sur le bouton <img alt="" src=images/Path_BStop.svg  style="width:24px;"> (Stop) pour arrêter l\'animation.
    -   Appuyez sur le bouton **Annuler** pour supprimer le stock créé pour la simulation. Si vous appuyez sur **OK**, cet objet sera conservé dans votre travail.

## Propriétés

-    {{PropertyData/fr|Playback Speed}}: La vitesse de lecture de la simulation, en lignes G-code/seconde

-    {{PropertyData/fr|Accuracy}}: La précision de la simulation exprimée en pourcentage indiquant l\'écart des simulations par rapport à la taĉhe. Pour la simulation interactive, réduire la précision à 0.3 fonctionne beaucoup plus rapidement.

-    {{PropertyData/fr|Job}}: La taĉhe utilisé comme base de la simulation.

-    {{PropertyData/fr|Operation List}}: La liste des opérations sélectionnées à inclure dans la simulation.





{{Path_Tools_navi

}} 
