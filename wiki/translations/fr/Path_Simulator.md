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

Cet outil permet de simuler le Travail Path en balayant les modèles 3D avec les outils utilisés dans chaque opération, le long des parcours G-Code, en enlevant la matière du brut, où le brut et l\'outil se chevauchent, fournissant une visualisation du Travail. Cela permet de détecter et d\'isoler les erreurs avant d\'exécuter le travail sur une fraiseuse.

![](images/Path-Simulation.gif )

## Usage


<div class="mw-translate-fuzzy">

## Utilisation

1.  Appuyez sur le bouton **<img src="images/Path_Simulator.svg" width=16px> [Simuler le chemin G-Code...](Path_Simulator/fr.md)
**
2.  Désélectionnez toutes les opérations qui ne doivent pas être simulées
3.  Réglez les paramètres de vitesse et de précision.
4.  Sélectionnez le travail à simuler dans le menu déroulant.
5.  Utilisez la barre d\'outils du simulateur de chemin pour appeler différentes actions:
    -   Appuyez sur le bouton <img alt="" src=images/Path_BPlay.svg  style="width:24px;"> (Lecture) pour lire ou lire une animation des opérations.
    -   Appuyez sur le bouton <img alt="" src=images/Path_BFastForward.svg  style="width:24px;"> (Avance rapide) pour augmenter considérablement la vitesse (afin de passer rapidement en revue les chemins compliqués).
    -   Appuyez sur le bouton <img alt="" src=images/Path_BPause.svg  style="width:24px;"> (Pause) pour suspendre l\'animation à des fins de dépannage
    -   Appuyez sur le bouton <img alt="" src=images/Path_BStep.svg  style="width:24px;"> (Single-Step) pour ralentir l\'animation, cette fonctionnalité permet de dépanner et de résoudre des coupes et / ou des mouvements spécifiques.
    -   Appuyez sur le bouton <img alt="" src=images/Path_BStop.svg  style="width:24px;"> (Stop) pour arrêter l\'animation.
6.  Cliquer sur le bouton **Cancel** supprimera le stock créé pour la simulation. Si vous cliquez sur **OK**, cet objet sera conservé dans votre travail.


</div>


<div class="mw-translate-fuzzy">

## Propriétés

1.  nécessite des utilisations


</div>

-    {{PropertyData/fr|Vitesse de lecture}}: La vitesse de lecture de la simulation, en lignes G-Code / seconde

-    {{PropertyData/fr|Précision de la simulation}}: La précision de la simulation exprimée en pourcentage indiquant l\'écart des simulations par rapport au Travail. Pour la simulation interactive, réduire la précision à 0,3 fonctionne beaucoup plus rapidement.

-    {{PropertyData/fr|Travail}}: Le Travail utilisé comme base de la simulation

-    {{PropertyData/fr|Liste des opérations}}: La liste des opérations sélectionnées à inclure dans la simulation.


<div class="mw-translate-fuzzy">





</div>


{{Path_Tools_navi

}} 
