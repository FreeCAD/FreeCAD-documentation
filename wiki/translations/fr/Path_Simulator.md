---
- GuiCommand:
   Name:Path Simulator
   Name/fr:Path Simulateur FAO
   MenuLocation:Path - Simulateur FAO
   Workbenches:[Path](Path_Workbench/fr.md)
   Shortcut:**P** **M**
   SeeAlso:[Path Inspecter des commandes](Path_Inspect/fr.md)
---

# Path Simulator/fr

## Description

L\'outil <img alt="" src=images/Path_Simulator.svg  style="width:24px;"> [Simulateur FAO](Path_Simulator/fr.md) permet de simuler la tâche de Path en balayant les modèles 3D des outils utilisés pour chaque opération, le long des parcours du G-code, en soustrayant le matériau du brut, là où le brut et l\'outil se chevauchent, ce qui permet de visualiser la tâche. Cela permet de détecter et d\'isoler les erreurs avant d\'exécuter la tâche à la fraiseuse.

![](images/Path-Simulation.gif )



## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Path_Simulator.svg" width=16px> [Simulateur FAO](Path_Simulator/fr.md)**.
    -   Sélectionnez l\'option **Path → <img src="images/Path_Simulator.svg" width=16px> Simulateur FAO** dans le menu.
    -   Utilisez le raccourci clavier : **P** puis **M**.
2.  Désélectionnez toutes les **Opérations** qui ne doivent pas être simulées.
3.  Réglez les paramètres de **Vitesse** et **Précision**.
4.  Sélectionnez la tâche **Job** à simuler dans le menu déroulant.
5.  Utilisez la barre d\'outils **Path Simulateur** pour lancer les différentes actions :
    -   Appuyez sur le bouton <img alt="" src=images/Path_BPlay.svg  style="width:24px;"> pour lire ou reproduire une animation des opérations.
    -   Appuyez sur le bouton <img alt="" src=images/Path_BFastForward.svg  style="width:24px;"> pour augmenter sensiblement la vitesse (afin de revoir rapidement des chemins compliqués).
    -   Appuyez sur le bouton <img alt="" src=images/Path_BPause.svg  style="width:24px;"> pour mettre l\'animation en pause à des fins de dépannage.
    -   Appuyez sur le bouton <img alt="" src=images/Path_BStep.svg  style="width:24px;"> pour ralentir l\'animation, cette fonctionnalité permet de dépanner et de résoudre des coupes et/ou des mouvements spécifiques.
    -   Appuyez sur le bouton <img alt="" src=images/Path_BStop.svg  style="width:24px;"> pour arrêter l\'animation.
    -   Appuyez sur le bouton **Annuler** pour supprimer le brut créé pour la simulation. Si vous appuyez sur **OK**, cet objet sera conservé dans votre travail.



## Propriétés

-    **Playback Speed**: vitesse de lecture de la simulation, en lignes G-code/seconde

-    **Accuracy**: précision de la simulation exprimée en pourcentage indiquant l\'écart des simulations par rapport à la taĉhe. Pour la simulation interactive, réduire la précision à 0.3 fonctionne beaucoup plus rapidement.

-    **Job**: taĉhe utilisée comme base de la simulation.

-    **Operation List**: liste des opérations sélectionnées à inclure dans la simulation.





{{Path_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Simulator/fr
