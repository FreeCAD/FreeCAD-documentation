# Tasks Placement/fr
## Description

Commande pour modifier le **positionnement**. Ces options ne concernent que la position et l\'orientation de l\'objet dans l\'espace, ils n\'affectent pas les autres attributs de la forme. Le positionnement est enregistré en interne sous forme de position et une rotation (autour d\'un axe ou d\'un angle, transformé en un [quaternion](https   *//fr.wikipedia.org/wiki/Quaternions_et_rotation_dans_l'espace)). Alors qu\'il existe plusieurs méthodes pour spécifier une rotation, par exemple autour d\'un centre, cela n\'affecte que les calculs de rotation et il n\'y a pas d\'enregistrement pour des opérations suivantes. De même, si un axe de rotation (1,1,1) est spécifié, il peut être normalisé lorsqu\'il est enregistré dans le quaternion et apparaît comme (0.58, 0.58, 0.58) lorsque l\'on navigue sur l\'objet par la suite.

## Utilisation

La fonction **Positionnement** peut être accessible de plusieurs façons   *

-   via un [script](Python_scripting_tutorial#Vecteurs_et_Positions/fr.md) Python dans la console et son [API](Placement_API/fr.md).

   *   ![Placement de script en y/p/r et Matrix](images/PlacePyConv10.png )

-   ou, dans la fenêtre **Vue combinée → Propriétés → Données → Placement → **...****,

   *   ![Task\_Placement](images/Tache_Placement_fr_01.png )

-   ou par le menu **Edition → Placement\...**.

### Activer Placement dans la fenêtre Affichage 

-   Cliquez sur une forme pour la sélectionner.
-   Cliquez sur **Placement** (le titre, pas la petite flèche) et une ellipse **...** apparaît   * <img alt="Tache\_Placement" src=images/Tache_Placement_01_fr_00.png  style="width   *256px;">
-   Cliquez sur l\'ellipse et le **Boîte de dialogue de Placement** est affiché   *

   *   ![](images/Tache_Placement_en_02.png )

### Options


{{TitleProperty|Translation}}


{{TitleProperty|Translations   * }}

-    {{TasksTag|X}}<img alt="Translation dans la direction X (Cliquez sur l\'image pour l\'agrandir)" src=images/Tache_Placement_Translation_X_fr.gif  style="width   *150px;"> Déplace le système de coordonnées de l\'objet, dans la direction **X** , par rapport aux coordonnées d\'axes d\'origine 0, 0, 0.

-    {{TasksTag|Y}}<img alt="Translation dans la direction Y (Cliquez sur l\'image pour l\'agrandir)" src=images/Tache_Placement_Translation_Y_fr.gif  style="width   *150px;"> Déplace le système de coordonnées de l\'objet, dans la direction **Y** , par rapport aux coordonnées d\'axes d\'origine 0, 0, 0.

-    {{TasksTag|Z}}<img alt="Translation dans la direction Z (Cliquez sur l\'image pour l\'agrandir)" src=images/Tache_Placement_Translation_Z_fr.gif  style="width   *150px;"> Déplace le système de coordonnées de l\'objet, dans la direction **Z** , par rapport aux coordonnées d\'axes d\'origine 0, 0, 0.


{{TitleProperty|Center}}

-    {{TasksTag|X}}   * Déplace le centre de rotation, dans la direction **X**, par rapport aux coordonnées de l\'objet sélectionné. (Défaut   * 0,0,0).

-    {{TasksTag|Y}}   * Déplace le centre de rotation, dans la direction **Y**, par rapport aux coordonnées de l\'objet sélectionné. (Défaut   * 0,0,0).

-    {{TasksTag|Z}}   * Déplace le centre de rotation, dans la direction **Z**, par rapport aux coordonnées de l\'objet sélectionné. (Défaut   * 0,0,0).

-    {{TasksTag|Défini par l'utilisateur...}}   * Permet de modifier les trois axes (**X, Y, Z**) en une seule opération <img alt="Défini par l\'utilisateur" src=images/Part_Revolve_fr_06.png  style="width   *96px;">.


{{TitleProperty|Rotation}}

Pour ajuster nos **paramètres de rotation**, deux moyens sont possibles.

-   Première option. Sélectionner **Axe de rotation et angle** <img alt="Tache\_Placement Option Axe de rotation et angle" src=images/Tache_Placement_fr_05.png  style="width   *256px;"> (Par défaut)
    -   
        {{TasksTag|Axis   * X}}
        
           * La rotation se fera sur l\'axe **X**.

    -   
        {{TasksTag|Axis   * Y}}
        
           * La rotation se fera sur l\'axe **Y**.

    -   
        {{TasksTag|Axis   * Z}}
        
           * La rotation se fera sur l\'axe **Z**. (Axe par défaut).

    -   
        {{TasksTag|Angle   *}}
        
           * Angle de rotation en **degrés** de **-360,00°** à **360,00°**. ( Par défaut    * **0,00°**).

-   Deuxième option. Sélectionnez **Angles d\'Euler** <img alt="Tache\_Placement Option Angles d\'Euler" src=images/Tache_Placement_fr_04.png  style="width   *256px;">.

Cette option peut être plus facile à travailler, toutefois, même dans ce mode, il y a des choses importantes à retenir    * les rotations positives sont dans le sens **Horaire**, en regardant depuis l\'origine le long d\'un axe positif. Ou pour le dire autrement, les rotations positives sont dans le sens \'\'\' anti-horaire \'\'\', en regardant vers l\'origine le long d\'un axe positif.

   **


<div id="Yaw">


</div>

**[Lacet](https   *//fr.wikipedia.org/wiki/Lacet_(mouvement))**    * Le lacet est le mouvement de rotation horizontal d\'un mobile autour d\'un axe vertical. (Le lacet est l\'angle **Psi ψ**)

   **


<div id="Pitch">


</div>

**[Tangage](https   *//fr.wikipedia.org/wiki/Tangage)**    * Le tangage est défini comme étant un mouvement d\'oscillation d\'un bateau d\'avant en arrière. (Le tangage est l\'angle **Phi φ**).

   **


<div id="Roll">


</div>

**[Roulis](https   *//fr.wikipedia.org/wiki/Roulis)**    * Le roulis est un mouvement de rotation d\'un mobile autour de son axe longitudinal (axe de roulis). (Le Roulis est l\'angle **Thêta θ**).

Lacet, roulis et tangage se référent à l**\'attitude** d\'un objet dans l\'espace 3D. Ces termes sont couramment utilisés dans l\'aviation. Les angles sont les **angles Tait-Bryan.** Si vous voulez plus d\'informations, lire [angles d\'Euler](https   *//fr.wikipedia.org/wiki/Angles_d%27Euler).

![None\|Options Angles d\'Euler](images/Tache_Placement_en_03.png )

![None\|Lacet](images/Tache_Placement_Lacet_fr_Mini.gif )

-    {{TasksTag|axe de lacet}}**Le lacet est la rotation autour de l\'axe Z**, c\'est à dire une rotation de gauche à droite. (L\'angle de lacet est le **Psi ψ**). Valeur **-360.00°** à **360, 00°** (Par défaut, **0.00°**).

![None\|Tangage](images/Tache_Placement_Tangage_fr_Mini.gif )

-    {{TasksTag|axe de tangage}}**Le pitch est la rotation autour de l\'axe Y**, c\'est-à-dire le cabré et le piqué. (L\'angle de tangage est le **Phi φ**). Valeur **-360.00°** à **360, 00°** (Par défaut, **0.00°**).

![None\|Roulis](images/Tache_Placement_Roulis_fr_Mini.gif )

-    {{TasksTag|axe de roulis}}**Le roulis est une rotation autour de l\'axe X**, c\'est à dire l\'aile en haut et en bas. (L\'angle de roulis est le **Thêta θ**). Valeur **-360.00°** à **360, 00°**(Par défaut, **0.00°**).

-    {{TasksTag|Appliquer les changements incrémentiels}}au placement de l\'objet    * Une fois sélectionnée, cette option met **virtuellement** tous les paramètres à zéro, pour vous permettre d\'entrer vos valeurs sans avoir à calculer avec les paramètres originaux du formulaire. Une fois que vous aurez confirmé avec **OK**, les valeurs saisies seront ajoutées aux valeurs du formulaire.

-    **Réinitialiser**ramène toutes les valeurs à **0,0,0**.

## Liens et Exemple 

Un exemple pratique de l\'utilisation de cette commande est dans le tutoriel [Avion](Aeroplane/fr.md).

Autres explications sur le [Placement](Placement/fr.md).




[Category   *Command\_Reference](Category_Command_Reference.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Command_Reference](Category_Command_Reference.md) > Tasks Placement/fr
