# <img alt="Icône de l\'atelier externe Render" src=images/Render_workbench_icon.svg  style="width:64px;"> Render Workbench/fr




## Introduction

L\'atelier Render vous permet de produire des images de haute qualité à partir de modèles FreeCAD, en utilisant des moteurs open source de rendu externes.

Image:Pabellon_de_Barcelona.png\|Pavillon Barcelone
Capture d\'écran Image:Pabellon_de_Barcelona_Pov_large.png\|Pavillon Barcelone
Rendu de Povray Image:Pabellon_de_Barcelona_Cycles.png\|Pavillon Barcelone
Rendu de Cycles Image:Asm_V4.png\|Asm V4
Capture d\'écran Image:Asm_V4_lux.png\|Asm V4
Rendu de LuxCore Image:Asm_V4_ospray2.png\|Asm V4
Rendu de Ospray Image:Church_of_the_light.png\|Église de la lumière
Capture d\'écran Image:Church_of_the_light_lux2.png\|Église de la lumière
Rendu de LuxCore Image:Church_of_the_light_cycles.png\|Église de la lumière
Rendu de Cycles Image:Car.png\|Voiture
Capture d\'écran Image:Car_ospray.png\|Voiture
Rendu de Ospray Image:Car_lux.png\|Voiture
Rendu de LuxCore Image:Brick_assembly.png\|Assemblage de briques
Capture d\'écran Image:Brick_assembly_appleseed.png\|Assemblage de briques
Rendu de Appleseed Image:Brick_assembly_luxcore.png\|Assemblage de briques
Rendu de Luxcore Image:VillaSavoye.png\|Villa Savoye
Capture d\'écran Image:VillaSavoye appleseed.png\|Villa Savoye
Rendu de Appleseed Image:VillaSavoye Cycles.png\|Villa Savoye
Rendu de Cycles

Atelier en Python, Render est parfaitement intégré à FreeCAD : toute la scène de rendu - objets, éclairage, matériaux, caméra, etc. - peut être décrite avec des objets FreeCAD, pour être exportée vers des moteurs de rendu externes.

Par rapport à d\'autres approches basées sur des applications d\'infographie tierces, Render vise à :

-   éviter à l\'utilisateur d\'apprendre un autre logiciel d\'infographie 3D : tout ce que vous devez savoir se trouve dans FreeCAD.
-   simplifier le flux de travail du rendu et soulager l\'utilisateur de toute manipulation de fichier intermédiaire - comme l\'importation, l\'exportation, la retouche de la scène, etc.
-   rendre la configuration de la scène persistante et surtout éviter de retravailler dans un outil externe à chaque fois que le modèle a été modifié.



## Moteurs de rendu pris en charge 

Actuellement, six moteurs de rendu sont pris en charge :

-   LuxCoreRender
-   Appleseed
-   Cycles (version autonome)
-   Pov-Ray
-   Intel Ospray Studio
-   Pbrt-v4 (expérimental)



## Utilisation

En mode démarrage rapide, après que l\'installation de l\'atelier a été correctement effectuée, le rendu d\'un modèle FreeCAD se fait en 4 étapes :

1.  **Créer un projet de rendu :** appuyer sur le bouton de la barre d\'outils correspondant à votre moteur de rendu et sélectionner un modèle adapté à votre moteur de rendu (vous pouvez commencer par une variante \'studio\', comme **appleseed_studio_light.appleseed**, **cycles_studio_light.xml**, **luxcore_studio_light.cfg**, **povray_studio_light.pov** etc.).
2.  **Ajouter des vues de vos objets à votre projet de rendu :** sélectionner à la fois les objets et le projet, et appuyer sur le bouton **Add view**.
3.  **Définir votre point de vue :** [naviguer dans la vue 3D](Manual:Navigating_in_the_3D_view/fr.md) à la position désirée et basculer en mode [perspective](Std_PerspectiveCamera/fr.md).
4.  **Rendu :** sélectionner votre projet et appuyez sur le bouton **Render** dans la barre d\'outils (également disponible dans le menu contextuel du projet).

**Et vous devriez obtenir un premier rendu de votre modèle.**

Vous trouverez plus d\'instructions dans le [dépôt GitHub](https://github.com/FreeCAD/FreeCAD-render) ou dans l\'aide en ligne.



## Fonctions

Les fonctions incluent, mais ne sont pas limitées à :

-   Éclairage : lumières ponctuelles, lumières surfaces, modèle soleil-ciel et modèles d\'éclairage prédéfinis.
-   Caméras.
-   Gestion des matériaux (à l\'aide des nuanceurs habituels : mat, brillant, verre, transparent, etc.) y compris les textures.
-   Mode lot / mode interface utilisateur.
-   Suppression de bruit.
-   Condition d\'arrêt (échantillon par pixel).
-   Contrôle du maillage : déflexions angulaires et linéaires, lissage automatique.



## Liens

Plus d\'informations ? Suivez le lien : <https://github.com/FreeCAD/FreeCAD-render>



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > [External Workbenches](Category_External Workbenches.md) > Render Workbench/fr
