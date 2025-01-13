---
 GuiCommand:
   Name: CAM Simulator
   Name/fr: CAM Simulateur de parcours
   MenuLocation: CAM , Simuler le parcours
   Workbenches: CAM_Workbench/fr
   Shortcut: **P** **M**
   SeeAlso: CAM_Inspect/fr
---

# CAM Simulator/fr

## Description

L\'outil <img alt="" src=images/CAM_Simulator.svg  style="width:24px;"> [Simulateur de parcours](CAM_Simulator/fr.md) permet de simuler la tâche de CAM en balayant les modèles 3D des outils utilisés pour chaque opération, le long des parcours du G-code, en soustrayant le matériau du brut, là où le brut et l\'outil se chevauchent, ce qui permet de visualiser la tâche. Cela permet de détecter et d\'isoler les erreurs avant d\'exécuter la tâche à la fraiseuse.

![](images/Path-Simulation.gif )



## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/CAM_Simulator.svg" width=16px> [Simuler le parcours](CAM_Simulator/fr.md)**.
    -   Sélectionnez l\'option **CAM → <img src="images/CAM_Simulator.svg" width=16px> Simuler le parcours** du menu.
    -   Utilisez le raccourci clavier : **P** puis **M**.
2.  Désélectionnez toutes les **Opérations** qui ne doivent pas être simulées.
3.  Réglez les paramètres de **Vitesse** et **Précision**.
4.  Sélectionnez la tâche **Tâche** à simuler dans le menu déroulant.
5.  Utilisez la barre d\'outils **Simulateur de parcours** pour lancer les différentes actions :
    -   Appuyez sur le bouton <img alt="" src=images/CAM_BPlay.svg  style="width:24px;"> pour lire ou reproduire une animation des opérations.
    -   Appuyez sur le bouton <img alt="" src=images/CAM_BFastForward.svg  style="width:24px;"> pour augmenter sensiblement la vitesse (afin de revoir rapidement des chemins compliqués).
    -   Appuyez sur le bouton <img alt="" src=images/CAM_BPause.svg  style="width:24px;"> pour mettre l\'animation en pause à des fins de dépannage.
    -   Appuyez sur le bouton <img alt="" src=images/CAM_BStep.svg  style="width:24px;"> pour ralentir l\'animation, cette fonctionnalité permet de dépanner et de résoudre des coupes et/ou des mouvements spécifiques.
    -   Appuyez sur le bouton <img alt="" src=images/CAM_BStop.svg  style="width:24px;"> pour arrêter l\'animation.
    -   Appuyez sur le bouton **Annuler** pour supprimer le brut créé pour la simulation. Si vous appuyez sur **OK**, cet objet sera conservé dans votre travail.



## Propriétés

-    **Playback Speed**: vitesse de lecture de la simulation, en lignes G-code/seconde

-    **Accuracy**: précision de la simulation exprimée en pourcentage indiquant l\'écart des simulations par rapport à la taĉhe. Pour la simulation interactive, réduire la précision à 0.3 fonctionne beaucoup plus rapidement.

-    **Job**: taĉhe utilisée comme base de la simulation.

-    **Operation List**: liste des opérations sélectionnées à inclure dans la simulation.





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM Simulator/fr
