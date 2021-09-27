# Tasks Placement/fr
## Description

Commande pour modifier le **positionnement**. Ces options ne concernent que la position et l\'orientation de l\'objet dans l\'espace, ils n\'affectent pas les autres attributs de la forme. Le positionnement est enregistré en interne sous forme de position et une rotation (autour d\'un axe ou d\'un angle, transformé en un quaternion [1](https://fr.wikipedia.org/wiki/Quaternions_et_rotation_dans_l'espace)). Alors qu\'il existe plusieurs méthodes pour spécifier une rotation, par exemple autour d\'un centre, cela n\'affecte que les calculs de rotation et il n\'y a pas d\'enregistrement pour des opérations suivantes. De même, si un axe de rotation (1,1,1) est spécifié, il peut être normalisé lorsqu\'il est enregistré dans le quaternion et apparaît comme (0.58, 0.58, 0.58) lorsque l\'on navigue sur l\'objet par la suite.

## Utilisation

La fonction **Positionnement** peut être accessible de plusieurs façons:

-   via un [script](Python_scripting_tutorial#Vecteurs_et_Positions/fr.md) Python dans la console et son [Placement API](Placement_API/fr.md).

:   ![Placement de script en y/p/r et Matrix](images/PlacePyConv10.png )

-   ou, dans la fenêtre **Vue combinée → Propriétés → Données → Placement → **...****,

:   ![Task\_Placement](images/_Tache_Placement_fr_01.png )

-   ou par le menu **Edition → Placement \...**.

### Activer Placement dans la fenêtre Affichage 

-   Cliquez sur une forme pour la sélectionner.
-   Cliquez sur **Placement** (le titre, pas la petite flèche) et une ellipse **...** apparaît: <img alt="Tache\_Placement" src=images/Tache_Placement_01_fr_00.png  style="width:256px;">
-   Cliquez sur ce bouton et le **Dialogue de placement** est affiché:

:   ![](images/Tache_Placement_en_02.png )




### Options


{{TitreTache| Placement }}


{{TitreProprietes|Translations: }}

-    {{OngletTache| X }}: <img alt="Translation dans la direction X (Cliquez sur l\'image pour l\'agrandir)" src=images/Tache_Placement_Translation_X_fr.gif  style="width:150px;"> Déplace le système de coordonnées de l\'objet, dans la direction **X** , par rapport aux coordonnées d\'axes d\'origine **0, 0, 0**.

-    {{OngletTache| Y }}: <img alt="Translation dans la direction Y (Cliquez sur l\'image pour l\'agrandir)" src=images/Tache_Placement_Translation_Y_fr.gif  style="width:150px;"> Déplace le système de coordonnées de l\'objet, dans la direction **Y** , par rapport aux coordonnées d\'axes d\'origine **0, 0, 0**.

-    {{OngletTache| Z }}: <img alt="Translation dans la direction Z (Cliquez sur l\'image pour l\'agrandir)" src=images/Tache_Placement_Translation_Z_fr.gif  style="width:150px;"> Déplace le système de coordonnées de l\'objet, dans la direction **Z** , par rapport aux coordonnées d\'axes d\'origine **0, 0, 0**.


{{TitreProprietes|Centre : }}

-    {{OngletTache| X }}: Déplace le centre de rotation, dans la direction **X**, par rapport aux coordonnées de l\'objet sélectionné. (Défaut, **0,00**).

-    {{OngletTache| Y }}: Déplace le centre de rotation, dans la direction **Y**, par rapport aux coordonnées de l\'objet sélectionné. (Défaut, **0,00**).

-    {{OngletTache| Z }}: Déplace le centre de rotation, dans la direction **Z**, par rapport aux coordonnées de l\'objet sélectionné. (Défaut, **0,00**).

-    {{OngletTache| Défini par l'Utilisateur... }}: Permet de modifier les trois axes (**X, Y, Z**) en une seule opération <img alt="Défini par l\'utilisateur" src=images/Part_Revolve_fr_06.png  style="width:96px;">.


{{TitreProprietes|Rotation : }}

Ppur ajuster nos **paramètres de rotation**, deux moyens sont possible.

-   Première option. Sélectionner **Axe de rotation et angle**![ 256px \| Tache\_Placement Option rotation axis and angle](images/_Tache_Placement_fr_05.png ) (Par défaut)

-    {{OngletTache| Axe : X }}: La rotation se fera sur l\'axe **X**.

-    {{OngletTache| Axe : Y }}: La rotation se fera sur l\'axe **Y**.

-    {{OngletTache| Axe : Z }}: La rotation se fera sur l\'axe **Z**. (Axe par défaut).

-    {{OngletTache| Angle }}: Angle de rotation en **degrés** de **-360,00°** à **360,00°**. ( Par défaut : **0,00°**).

-   Deuxième option.Sélectionner **Angles d\'Euler** <img alt="Tache\_Placement Option Angles d\'Euler" src=images/Tache_Placement_fr_04.png  style="width:256px;">.

Cette option peut être plus facile à travailler, toutefois, même dans ce mode, il y a des choses importantes à retenir :

Les rotations positives sont dans le sens **Horaire**, en regardant depuis l\'origine le long d\'un axe positif. Ou pour le dire autrement, les rotations positives sont dans le sens \'\'\' anti-horaire \'\'\', en regardant vers l\'origine le long d\'un axe positif.

:\* [Lacet](http://fr.wikipedia.org/wiki/Lacet_(mouvement)) : Le lacet est le mouvement de rotation horizontal d\'un mobile autour d\'un axe vertical. (Le lacet est l\'angle **Psi ψ**)

:\* [Tangage](http://fr.wikipedia.org/wiki/Tangage) : Le tangage est défini comme étant un mouvement d\'oscillation d\'un bateau d\'avant en arrière. (Le tangage est l\'angle **Phi φ**).

:\* [Roulis](http://fr.wikipedia.org/wiki/Roulis) : Le roulis est un mouvement de rotation d\'un mobile autour de son axe longitudinal (axe de roulis). (Le Roulis est l\'angle **Thêta θ**).

Lacet, roulis et tangage se référent à **l\'attitude** d\'un objet dans l\'espace 3D. Ces termes sont couramment utilisés dans l\'aviation.

Les angles sont les **angles Tait-Bryan.** Si vous voulez plus d\'informations, essayez [Euler angles](http://en.wikipedia.org/wiki/Euler_angles).

![ left \| Option Euler angles](images/_Tache_Placement_fr_03.png ) 

![Left\|Lacet](images/Tache_Placement_Lacet_fr_Mini.gif )

-    {{OngletTache|Axe de lacet}}: Le **Lacet est la rotation autour de l\'axe Z**, c\'est à dire une rotation de gauche à droite. (Le lacet est l\'angle **Psi ψ**). Valeur de **-360,00°** à **360,00°** (Défaut, **0,00°**).

![Left\|Tangage](images/Tache_Placement_Tangage_fr_Mini.gif )

-    {{OngletTache|Axe de tangage}}: Le **Tangage est la rotation autour de l\'axe des Y**, c\'est à dire monter, et, descendre le nez. (Le tangage est l\'angle **Phi φ**). Valeur de **-360,00°** à **360,00°** (Défaut, **0,00°**).

![Left\|Roulis](images/Tache_Placement_Roulis_fr_Mini.gif )

-    {{OngletTache|Axe de roulis}}: Le **Roulis est la rotation autour de l\'axe X**, c\'est à dire monter et descendre les ailes. (Le Roulis est l\'angle **Thêta θ**). Valeur de **-360,00°** à **360,00°** (Défaut, **0,00°**).

-    {{OngletTache| Appliquer les modifications incrémentielles au placement de l'objet }}: Une fois cochée, cette option met **virtuellement** les paramètres à zéro, pour vous permettre d\'entrer vos valeurs sans devoir faire de calcul avec les paramètres originaux de la forme.
    Une fois que vous aurez validé avec ** OK **, les valeurs entrées s'additionneront aux valeurs de la forme.

-   Le bouton ** Réinitialiser **, remet toutes les valeurs à **0,0,0**.

## Liens et Exemple 

Un exemple pratique de l\'utilisation de cette commande est dans le tutoriel [ Avion](Aeroplane/fr.md).

Autres explications sur le [Placement](Placement/fr.md)







_

---
[documentation index](../README.md) > [Command_Reference](Category_Command_Reference.md) > Tasks Placement/fr
