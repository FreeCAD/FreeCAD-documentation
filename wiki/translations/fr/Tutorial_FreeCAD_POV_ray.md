---
- TutorialInfo   */fr
   Topic   *Rendu
   Level   *Intermediaire
   Time   *120 minutes
   Author   *[https   *//forum.freecadweb.org/memberlist.php?mode=viewprofile&u=21943 vocx]
   FCVersion   *0.18 ou ultérieure
   Files   *aucun
---

# Tutorial FreeCAD POV ray/fr




**L'[atelier Raytracing](Raytracing_Workbench/fr.md) a été remplacé par le nouvel [https   *//github.com/FreeCAD/FreeCAD-render atelier Render], qui est destiné à le remplacer. L'atelier Render peut être installé via le [Gestionnaire des extensions](Std_AddonMgr/fr.md). L'information ici est fournie parce que par défaut FreeCAD est toujours livré (à partir de 0.19-24276) avec l'atelier Raytracing et parce que le nouveau atelier devrait fondamentalement fonctionner de la même manière**

.



## Introduction

Ce tutoriel montre comment produire un rendu dans FreeCAD à l\'aide du rendu POV-Ray. Cela suppose que l\'utilisateur a déjà créé une pièce ou un assemblage dans FreeCAD ou en a importé un. Il utilise le [Module Raytracing](Raytracing_Workbench/fr.md) pour générer le fichier en vue du rendu.

Ce tutoriel est basé sur le post de forum créé par schupin [FreeCAD / pov ray tutorial](https   *//forum.freecadweb.org/viewtopic.php?f=36&t=32745) qui comprend également un fichier `.pov` nécessaire à la production du rendu.

<img alt="" src=images/Povray_before_after.png  style="width   *600px;">



*align=center|Exemple d'un modèle 3D par schupin et d'un rendu haute qualité produit avec FreeCAD et POV-Ray.*

Les fichiers utilisés dans ce tutoriel sont au post #8 [du fil en question](https   *//forum.freecadweb.org/viewtopic.php?f=36&t=32745#p305169).

## Configuration de base 

Suivez les étapes de base décrites dans la documentation du [Module Raytracing](Raytracing_Workbench/fr.md).

Pour que le rendu direct fonctionne, l\'exécutable `povray` doit être défini dans **Edition → Préférences → Raytracing → Render → Exécutable POV-Ray**. Définissez son emplacement dans votre système, par exemple `/usr/bin/povray`. D\'autres options utilisées par le renderer peuvent également être définies ici comprenant la largeur `+W` et la hauteur `+ H` de l\'image ainsi que l\'utilisation de l\'antialiasing `+ A} }.

==Mise en place du fichier .pov==

1. Créez un assemblage à l'aide de corps à partir de l'[Atelier Part](Part_Workbench/fr.md) ou [Atelier PartDesign](PartDesign_Workbench/fr.md) ou de tout autre atelier générant des objets solides par exemple [Atelier Arch](Arch_Workbench/fr.md). Attribuez des couleurs ou des matériaux aux corps individuels qui composent l'assemblage correspondant approximativement à la couleur souhaitée dans votre rendu. 

![](images/)


*align=center|Assemblage de trois corps créés dans FreeCAD avec des couleurs ou des matériaux choisis.*

2. Si votre modèle est très détaillé, assurez-vous que la valeur **Deviation** du corps est défini sur une valeur basse comprise entre {{incode|0.1` et `00.1` voire moins. Plus cette valeur est basse, plus le maillage exporté sera détaillé et donc meilleure sera la qualité du rendu.

![](images/)


*align=center|Propriété de déviation des corps créés dans FreeCAD. L'écart doit être faible pour pouvoir exporter les pièces avec une bonne résolution.*

3. Créez un projet POV-Ray en cliquant sur **<img src="images/Raytrace_New.svg" width=16px> [New](Raytracing_New/fr.md)**. Si la fenêtre d'affichage est définie sur [Vue Orthographique](Std_OrthographicCamera/fr.md) remplacez-la par [Caméra Perspective](Std_PerspectiveCamera/fr.md) car le rendu fonctionnera normalement avec une caméra avec vue en perspective. L'utilisation de la vue en perspective vous permettra de mieux voir le type de scène qui sera rendu.

4. Sélectionnez tous les objets que vous souhaitez ajouter à votre scène puis sélectionnez l'objet `PovProject` créé puis cliquez sur **<img src="images/Raytrace_NewPartSegment.svg" width=16px> [InsertPart](Raytracing_InsertPart.md)**.

**Note   *** méfiez-vous des objets qui ne sont pas actuellement visibles dans la fenêtre de visualisation 3D. S'ils sont invisibles mais inclus dans la scène, ils seront toujours restitués. D'autre part, si vous voulez vraiment omettre le rendu d'un corps, ne le sélectionnez pas pour l'inclure dans le projet POV-Ray.

**Note 2   *** tous les objets du projet POV-Ray auront un nom basé sur leur nom interne FreeCAD. Il est important de noter les noms POV-Ray car d'autres options, telles que les textures de matériau, seront affectées à ces noms POV-Ray.

5. Dans la fenêtre 3D, effectuez un zoom, un panoramique et une rotation de la vue pour configurer la scène à votre guise. Assurez-vous que les objets sont centrés dans la fenêtre puis sélectionnez l'objet `PovProject` créé et appuyez sur **<img src="images/Raytrace_ResetCamera.svg" width=16px> [ResetCamera](Raytracing_ResetCamera.md)**.

6. Le fichier POV-Ray est maintenant prêt. Il contient les objets sélectionnés et les informations de la caméra. Sélectionnez l'objet créé `PovProject` puis appuyez sur **<img src="images/Raytrace_ExportProject.svg" width=16px> [ExportProject](Raytracing_ExportProject.md)** pour enregistrer le fichier `.pov`.

7. Le fichier `.pov` créé peut maintenant être rendu directement à partir de FreeCAD. Sélectionnez l'objet `PovProject` créé puis appuyez sur **<img src="images/Raytrace_Render.svg" width=16px> [Render](Raytracing_Render.md)**. Lorsque l'image contextuelle apparaît à l'écran, cliquez dessus pour l'envoyer à FreeCAD dans son propre onglet de fenêtre.

![](images/)


*align=center|Premier rendu de l'assemblage réalisé avec POV-Ray avec le modèle standard écrit par Raytracing Workbench.*

7.1. Avec le fichier `.pov` déjà créé, il est également possible d'exécuter `povray` à partir des lignes de commande.
```python
povray assembly.pov +W800 +H600 +AM2 +A
```

Les options `+WX +HY` définissent les dimensions horizontale et verticale en pixel de l'image finale.

Les options `+ AM2` (type 2, sur-échantillonnage récursif) et `+ A` activent l'anticrénelage pour produire une image plus lisse.

8. En double-cliquant sur l'objet `PovProject`, vous pouvez voir qu'il utilise le modèle `ProjectStd.pov`. Ce modèle crée un fichier de base `.pov` qui produira une image simple et sombre.

Pour améliorer l'apparence de l'image, utilisez un meilleur modèle. Double-cliquez sur l'objet `PovProject` et choisissez le modèle `RadiosityNormal.pov`. Exportez ensuite un nouveau fichier `.pov` puis réexécutez le rendu. L'image doit être plus lumineuse et généralement meilleure.

![](images/)


*align=center|Rendu de l'assemblage réalisé avec POV-Ray avec le modèle RadiosityNormal écrit par Raytracing Workbench.*

Double-cliquez de nouveau sur l'objet `PovProject` et choisissez maintenant le modèle `RadiosityOutdoorHQ.pov`. Exportez ensuite un nouveau fichier `.pov` puis réexécutez le rendu. L'image devrait prendre plus de temps à produire mais le résultat devrait être de meilleure qualité.
![](images/)


*align=center|Rendu de l'assemblage réalisé avec POV-Ray avec le modèle RadiosityOutdoorHQ écrit par Raytracing Workbench.*

Si l'image rendue est assez bonne alors elle peut être enregistrée et il n'y a plus rien à faire. Toutefois, afin de contrôler précisément l'apparence des matériaux et d'obtenir des résultats encore meilleurs, le fichier `.pov` doit être modifié manuellement.

Dans les sections suivantes, nous modifions le fichier de base `.pov` produit avec le modèle `ProjectStd`.

==Editer le fichier .pov==

9. Le fichier `.pov` généré par FreeCAD est un simple fichier texte pouvant être ouvert avec n'importe quel éditeur. Cela ressemble vaguement à un fichier de code source C ++   * les directives commencent par un hash `#` et se terminent par un point-virgule `;`. Les accolades <code>{ }</code> sont utilisées pour limiter les blocs de section et l'indentation est un espace blanc arbitraire. Les commentaires sont indiqués par une double barre oblique `//`. Les commentaires de bloc peuvent être définis avec une paire de `/*  */` comme en C.

Le fichier peut sembler compliqué au début, mais 90% de son contenu est constitué de données de maillage ne nécessitant que peu de modifications. Ces maillages représentent la géométrie des corps à restituer.

Le fichier est structuré comme suit   *
* Includes
* Global settings   * Paramètres globaux
* Sky sphere   * Sphère du ciel
* Planes   * Plans
* Finishes and textures   * Finitions et textures
* Camera   * Caméra
* Mesh and body information   * Informations sur le maillage et le corps
* Light source   * Source de lumière

Les informations de la caméra ne seront pas touchées pas plus que la plupart des informations contenues dans les mailles. Les principales modifications seront apportées aux autres sections.

Comme les maillages ne seront pas fortement modifiés, le fichier peut être réorganisé pour que ces informations se trouvent à la fin du fichier.

<div class="toccolours mw-collapsible mw-collapsed">
Ceci est le contenu complet du fichier `.pov` mais sans les mailles.
<div class="mw-collapsible-content">
```python
// Persistence of Vision Ray Tracer Scene Description File
// for FreeCAD (http   *//www.freecadweb.org)

#version 3.6;

#include "colors.inc"
#include "metals.inc"

// 

global_settings {
    assumed_gamma 1.0
    ambient_light color rgb <1.0,1.0,1.0>
    max_trace_level 20
}  

// 


sky_sphere {
  pigment {
    gradient y
    color_map {
      [0.0 rgb <0.6,0.7,1.0>]
      [0.7 rgb <0.0,0.1,0.8>]
    }
  }
}


// 

plane {
  y, -1
  texture { pigment {rgb <0.0,0.0,0.0>} finish {ambient 0.0 reflection 0.05 specular 0.0} }
}

// Standard finish
//#declare StdFinish = F_MetalA;
//#declare StdFinish = finish { diffuse 0.7 };
//#declare StdFinish = finish { phong 0.5 };
//#declare StdFinish = finish { ambient rgb <0.5,0.5,0.5> };
//#declare StdFinish = finish { crand 0.5 phong 0.9};
#declare StdFinish = finish { ambient 0.01 diffuse 0.9 phong 1.0 phong_size 70 metallic brilliance 1.5} ;

// declares position and view direction

// Generated by FreeCAD (http   *//www.freecadweb.org/)
#declare cam_location =  <-171.753,1229.11,-2667.08>;
#declare cam_look_at  = <636.959,359.955,160.296>;
#declare cam_sky      = <0.068217,0.958943,0.275273>;
#declare cam_angle    = 45; 
camera {
  location  cam_location
  look_at   cam_look_at
  sky       cam_sky
  angle     cam_angle 
  right x*800/600
}
// Written by FreeCAD http   *//www.freecadweb.org/
// face number1 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
// ... meshes should be defined here until the end of the file ...




//default light
light_source {
  cam_location + cam_angle * 100
  color rgb <10, 10, 10>
}
```
</div>
</div>

=== Ré-organisation basique ===

10. Ouvrez le fichier `.pov` avec un éditeur de texte, allez à la fin du fichier, sélectionnez et coupez la section `light_source` puis collez-la avant la première ligne `//face number1`.

Le fichier résultant doit avoir les sections `camera` et `light_source` côte à côte, par exemple

```python
// Generated by FreeCAD (http   *//www.freecadweb.org/)
#declare cam_location =  <-171.753,1229.11,-2667.08>;
#declare cam_look_at  = <636.959,359.955,160.296>;
#declare cam_sky      = <0.068217,0.958943,0.275273>;
#declare cam_angle    = 45; 
camera {
  location  cam_location
  look_at   cam_look_at
  sky       cam_sky
  angle     cam_angle 
  right x*800/600
}

//default light
light_source {
  cam_location + cam_angle * 100
  color rgb <10, 10, 10>
}
// Written by FreeCAD http   *//www.freecadweb.org/
// face number1 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.
.
.
```

=== Modifier les lumières ===

11. Par défaut, le fichier de projet définit une lumière avec une position et une couleur.
```python
light_source {
  cam_location + cam_angle * 100
  color rgb <10, 10, 10>
}
```

La position de la lumière est définie par un vecteur `<x, y, z>`. `color` peut être établi comme un vecteur `<r, g, b>` ou il peut également être nommer par un nom tel que `White`. Si les valeurs RVB sont données, elles doivent être comprises entre `0.0` et `1.0` pour que la lumière ait une luminosité normale.

Comme d'autres objets, la lumière peut être modifiée par de nombreuses options. L'option `area_light` crée une source rectangulaire, plus réaliste dans la mesure où elle génère un éclairage diffus qui crée des ombres douces. Le mot clé `adaptive` permet de réduire le temps de calcul des trajets de lumière; plus la valeur est grande, plus le résultat sera précis. Pour éviter de longs temps de rendu, vous devez utiliser le plus petit entier donnant un résultat acceptable (`1` ou `2` sont généralement suffisants). Pour obtenir le meilleur résultat, supprimez complètement le mot clé (long rendering time   * temps de rendu long). Le mot clé `jitter` contribue à améliorer les ombres en décalant de manière aléatoire la position des lumières. Les mots-clés `circular` et `orient` transforment la lumière de la zone en source sphérique ce qui produira de meilleures ombres lorsqu'il y a des objets arrondis dans la scène. Ajouter `fade_distance` et {{incode | fade_power}} est utile pour atténuer la valeur de la lumière en fonction de la distance, tout comme cela se produit avec une source de lumière réelle.

Mettre en place une lumière venant de la droite et du haut.
```python
light_source {
    <1200, 1000, -1300>
    color White
    area_light <100, 0, 0>, <0, 0, 100>, 20, 20
    adaptive 1
    jitter
    circular orient
    fade_distance 1000 fade_power 2
}
```

Si la source de lumière est supposée être dans la scène, il peut être utile de voir une référence à l'écran à l'emplacement de cette source. Pour ce faire, créez une sphère de petit rayon et supposez que cette sphère représente la source de lumière. Positionnez la sphère où vous le souhaitez, puis déplacez la lumière très près de ces coordonnées et testez l'éclairage de la scène. Lorsque vous êtes satisfait de la position de la lumière, supprimez simplement la sphère.
```python
sphere {
    <1200, 1000, -1200>, 10
    pigment { color White }
}
```

12. La section `sky_sphere` est utilisée pour créer un fond de ciel réaliste. Elle est généralement définie par `gradient` et `color_map` d'au moins deux couleurs afin de produire une transition en douceur de la couleur de l'horizon à la couleur du zénith de la scène.

```python
sky_sphere {
    pigment {
        gradient y
        color_map {
            [0.0 color Gray50]
            [0.7 color White]
        }
    }
}
```

![](images/)


*align=center|A partir du modèle standard, rendu de la scène avec POV-Ray avec la source de lumière et sky sphere configurées.*

=== Modifier les textures des corps ===

13. Les textures de chaque corps doivent être ajustées. Il s’agit de la tâche la plus longue de ce processus.

Dans le fichier `.pov`, chaque corps est décrit de cette façon.
* Face1, Face2, Face3, Face4, ...
* Body (union de faces)
* Object

Un maillage de corps est défini par des faces. Chaque face est définie par une série d'éléments triangulaires eux-mêmes définis par des `vertex_vectors`, `normal_vectors` et `fac_indices`. Cette information n'a pas besoin d'être modifiée. Ensuite, chaque corps est défini comme l'union des faces spécifiées. Encore une fois, cette information n'a pas besoin d'être modifiée.

Enfin, chaque `object` à restituer est défini comme l'un des corps spécifiés avec une `texture` particulière elle-même définie par des propriétés telles que `pigment` et {{ incode|finish}}. 
```python
// instance to render
object {Pov_Body
 texture {
      pigment {color rgb <0.827451,0.827451,0.431373>}
      finish {StdFinish } //definition on top of the project
  }
}
```

En recherchant le mot clé `object` dans le fichier `.pov`, vous pouvez accéder directement à la partie souhaitée du fichier et modifier sa `texture` de manière appropriée.

Comme indiqué dans le commentaire, la définition de `StdFinish` figure en haut du fichier, dans ce cas avant les informations de camera. Cette valeur peut être déclarée de plusieurs manières, comme une combinaison de différentes propriétés, comme indiqué dans les lignes commentées et non commentées. 
```python
// Standard finish
//#declare StdFinish = F_MetalA;
//#declare StdFinish = finish { diffuse 0.7 };
//#declare StdFinish = finish { phong 0.5 };
//#declare StdFinish = finish { ambient rgb <0.5,0.5,0.5> };
//#declare StdFinish = finish { crand 0.5 phong 0.9};
#declare StdFinish = finish { ambient 0.01 diffuse 0.9 phong 1.0 phong_size 70 metallic brilliance 1.5} ;
```

En général, une `texture` est un conteneur qui décrit un matériau. Elle comprend des informations comme `pigment` (couleur ou graphique), `normal` (comment la couleur change avec la courbure de la surface), `finish` (interaction de la surface avec la lumière), `pattern` (agate, brique, bosses, léopard, radial, ondulations, mosaïque, vagues, bois, etc.) et d'autres propriétés. Il existe de nombreuses options qui peuvent être combinées pour produire une texture. Ce mélange n'est pas anodin, mais il existe de nombreux exemples en ligne pour obtenir l'aspect souhaité du matériau.

#### Librairies de matériaux 

14\. POV-Ray est livré avec une vaste bibliothèque de matétiaux pouvant être utilisés nommément. Par défaut, le modèle de projet rend disponibles certains matériaux en utilisant des instructions `#include` au début du fichier. Ces matériaux peuvent être encore modifiés à volonté. 
```python
#include "colors.inc"
#include "metals.inc"
```

La bibliothèque `colors.inc` définit les couleurs de base par nom, `Red`, `Green`, `Blue`, `Yellow`, `Cyan`, `Magenta`, `Clear`, `White` et `Black`. Il définit également plusieurs autres nuances ainsi que des fonctions permettant de transformer les couleurs. La bibliothèque `métaux.inc` contient des textures de cuivre, d\'argent, de chrome et de laiton et `golds.inc` contient les textures d\'or.

Les bibliothèques standard sont situées dans le répertoire d\'installation de POV-ray, par exemple 
```python
/usr/share/povray-3.7/include/
```

#### Nouvelles textures 

15\. Par exemple, pour créer une texture miroir, `finish` reçoit une valeur élevée de `reflection`. 
```python
#declare T_mirror = texture {
    finish { reflection {0.9} }
}
```

Alternativement, pour les métaux, une finition prédéfinie peut être utilisée. 
```python
#include "metals.inc"
#declare T_mirror = texture {
    finish { F_MetalE }
}
```

Ensuite, il peut être affecté à l\'objet spécifique. 
```python
object {Pov_Body002
    texture { T_mirror }
}
```

La bibliothèque `woods.inc` définit la texture `T_Wood7` (pin jaune, grain irrégulier). Il peut être utilisé comme base d'une texture plus complexe avec un redimensionnement et une traduction supplémentaires. 
```python
#include "woods.inc"
#declare T_wood = texture {
    T_Wood7
    scale 50.0
    translate x*1
    translate y*10
}
```

Ensuite, il est affecté à l\'objet spécifique. 
```python
object {Pov_Body
    texture { T_wood }
}
```

La bibliothèque `glass.inc` définit `F_Glass2` comme finition pour l'acrylique transparent. Elle définit également `I_Glass` comme un matériau intérieur qui, associé à l'option `caustics` permet de calculer aussi étroitement que possible les effets de la lumière traversant un matériau transparent. Dans ce cas, la section `material` est utilisée et contient des informations externes (`texture`) et internes (`interior`) du matériau.


```python
#declare M_vase = material {
    texture {
        pigment { color rgbf <1.0, 0.73333, 0.0, 0.75> }
        finish { F_Glass2 }
    }
    interior { I_Glass caustics 1.0 }
}
```

Ensuite, il peut être affecté à l\'objet spécifique. 
```python
object {Pov_Body001
    material { M_vase }
}
```

<img alt="" src=images/07_T04_FreeCAD_POVray_render_materials.png  style="width   *600px;">



*align=center|A partir du modèle standard, rendu de la scène avec POV-Ray avec la source de lumière et sky sphere configurées.*

### Préparation des plans 

16\. S\'ils ne sont pas fournis par le modèle 3D d\'origine, des plans peuvent être ajoutés pour simuler un sol ou une table sur laquelle les objets se tiennent. Plusieurs plans peuvent être définis pour servir de murs ou d'autres types de limites.

Par défaut, un seul plan est créé. Il est placé 1 millimètre en dessous du modèle, de sorte qu\'il apparaisse comme un sol. Une texture de base noire et légèrement réfléchissante est attribuée au plan. 
```python
plane {
  y, -1
  texture { pigment {rgb <0.0,0.0,0.0>} finish {ambient 0.0 reflection 0.05 specular 0.0} }
}
```

Notez que dans POV-Ray, l\'axe X est défini comme horizontal (gauche à droite), l\'axe Y est défini comme vertical (haut-bas) et l\'axe Z est défini en tant que profondeur (avant-arrière).

Pour un sol gris simple, c\'est à peine réfléchissant 
```python
plane {
  y, -1
  texture { pigment {rgb <0.3, 0.3, 0.3>} finish {ambient 0.0 reflection 0.01 specular 0.0} }
}
```

<img alt="" src=images/08_T04_FreeCAD_POVray_render_floor_gray.png  style="width   *600px;">



*align=center|A partir du modèle standard, le rendu de la scène avec POV-Ray, avec la source de lumière et sky sphere configurée, les matériaux affectés et un plan d'étage avec une texture de base grise.*

17\. Les plans peuvent recevoir une apparence plus complexe à l\'aide de normales et de bibliothèques de matériaux.

Définissez une carte normale qui sera utilisée pour donner au plan l\'apparence d\'un parquet.


```python
#declare Parquet_normal = normal {
    gradient z 2 slope_map { [0 <0,1>][0.05 <1,0>][0.95 <1,0>][1 <0,-1>] }
    scale 80
} ;
```

Puis définissez le plan. Comme `pigment`, utilisez un bois `color_map` défini dans `woods.inc` et modifiez-le avec `turbulence` et `scale` pour que le grain du bois apparaise aléatoire. Ajoutez ensuite la normale créée et une autre normale. Cela se traduira par une texture du parquet présentant de légères imperfections. Puis, comme `finish`, rendez-le un peu réfléchissant et brillant.


```python
#include "woods.inc"
plane {
    y, -1
    pigment {
        wood color_map { M_Wood8A }
        turbulence 0.5 scale <10, 1, 1>*20
    }
    normal {
        average normal_map {
          [1 Parquet_normal]
          [1 wood 0.5 slope_map { [0 <0,0>][0.5 <0.5,1>][1 <1,0>] }
              turbulence 0.5 scale <10, 1, 1>*20]
        }
    }
    finish { ambient 0.0 reflection 0.1 specular 0.2 }
}
```

<img alt="" src=images/09_T04_FreeCAD_POVray_render_floor_wood.png  style="width   *600px;">



*align=center|A partir du modèle standard, le rendu de la scène avec POV-Ray, avec la source de lumière et sky sphere configurée, les matériaux affectés et un plan d'étage avec une texture de parquet.*

18\. Ajoutez un deuxième plan, cette fois perpendiculaire à la direction Z, pour servir de fond. Déplacez-le un peu derrière le modèle pour éviter de couvrir le miroir. Incluez la bibliothèque `stones.inc`, ajoutez une texture de granite générique et redimensionnez-la un peu. Cela se traduira par l\'apparition d\'un simple mur sec.


```python
#include "stones.inc"
plane {
    z, 10
    texture {
        T_Grnt1   
        scale 0.02
    }
}
```

Un troisième plan peut être ajouté derrière la position de la caméra afin que le miroir reflète une zone limitée entre les deux murs.


```python
#include "stones.inc"
plane {
    z, -3700
    texture {
        T_Grnt1   
        scale 0.02
    }
}
```

<img alt="" src=images/10_T04_FreeCAD_POVray_render_floor_wood_walls.png  style="width   *600px;">



*align=center|A partir du modèle standard, le rendu de la scène avec POV-Ray, avec la source de lumière et sky sphere configurée, des matériaux assignés, un plan d'étage avec une texture de parquet et des murs arrière avec des textures de cloison sèche.*

### Préparation des paramètres globaux, de la radiosité 

19\. Les paramètres globaux définissent la lumière ambiante.


```python
global_settings {
    assumed_gamma 1.0
    ambient_light color rgb <1.0,1.0,1.0>
    max_trace_level 20
}
```

La propriété `radiosity` à l\'intérieur de `global_settings` contrôle la façon dont POV-Ray calcule les interactions de lumière diffuse entre différents objets. Il est essentiel d'ajuster cette propriété pour obtenir de bons résultats de rendu.

Comme il peut être fastidieux de tester différents paramètres `radiosity`, vous pouvez utiliser une variable `Rad_Quality` et une instruction `#switch` pour définir rapidement un rendu de qualité faible, moyenne ou élevée. Plus les paramètres de qualité sont élevés, plus le temps nécessaire au rendu d\'une image est long.


```python
#declare Rad_Quality = 1;

global_settings {
    assumed_gamma 1.0
    ambient_light color rgb <1.0,1.0,1.0>
    max_trace_level 20

#switch (Rad_Quality)
 #case (1)
    radiosity { // Settings 1 (fast)
        pretrace_start 0.08
        pretrace_end   0.02
        count 50
        error_bound 0.5
        recursion_limit 1
    }
    #break
 #case (2)
    radiosity { // Settings 2 (medium quality)
        pretrace_start 0.08
        pretrace_end   0.01
        count 120
        error_bound 0.25
        recursion_limit 1
    }
    #break
 #case (3)
    radiosity { // Settings 3 (high quality)
        pretrace_start 0.08
        pretrace_end   0.005
        count 400
        error_bound 0.1
        recursion_limit 2
    }
    #break
#end
}
```

<img alt="" src=images/11_T04_FreeCAD_POVray_render_floor_wood_walls_radiosity_1.png  style="width   *600px;">



*align=center|A partir du modèle standard, le rendu de la scène avec POV-Ray, avec la source de lumière et sky sphere configurée, des matériaux assignés, un plan d'étage avec une texture de parquet et des murs arrière avec des textures de cloison sèche.Paramètres de radiosité pour un rendu rapide.*

20\. La bibliothèque `rad_def.inc` définit une macro qui paramètrera rapidement `radiosity` pour une configuration prédéfinie. 
```python
#include "rad_def.inc"
global_settings {
    radiosity {
        Rad_Settings(Setting, Normal, Media)
    }
}
```

La valeur `Setting` peut être l\'une des constantes prédéfinies   * 
```python
Radiosity_Default
Radiosity_Debug
Radiosity_Fast
Radiosity_Normal
Radiosity_2Bounce
Radiosity_Final
Radiosity_OutdoorLQ
Radiosity_OutdoorHQ
Radiosity_OutdoorLight
Radiosity_IndoorLQ
Radiosity_IndoorHQ
```

Les valeurs `Normal` et `Media` sont soit `off` soit `on`.

Par conséquent, pour tester différents paramètres, l\'instruction `#switch` peut également être écrite comme ci-après.


```python
#declare Rad_Quality = 3;

global_settings {
    assumed_gamma 1.0
    ambient_light color rgb <1.0,1.0,1.0>
    max_trace_level 20

#switch (Rad_Quality)
 #case (1)
    radiosity { // Settings 1 (fast)
        Rad_Settings(Radiosity_Fast, off, off)
    }
    #break
 #case (2)
    radiosity { // Settings 2 (medium quality)
        Rad_Settings(Radiosity_2Bounce, on, on)
    }
    #break
 #case (3)
    radiosity{ // Settings 3 (high quality)
        Rad_Settings(Radiosity_Final, on, on)
        recursion_limit 2
    }
    #break
#end
}
```

Les valeurs exactes utilisées par ces préréglages se trouvent dans le fichier `rad_def.inc` qui se trouve dans le répertoire d\'installation de POV-Ray, par exemple   * 
```python
/usr/share/povray-3.7/include/
```

Le [Module Raytracing](Raytracing_Workbench/fr.md) a trois modèles par défaut   *

-    `ProjectStd.pov`n'utilise pas du tout `radiosity`.

-    `RadiosityNormal.pov`utilise le préréglage `Radiosity_Normal`.

-    `RadiosityOutdoorHQ.pov`utilise le préréglage `Radiosity_OutdoorHQ`.

## Rendu final 

21\. Le fichier modifié `.pov` peut être sauvegardé lorsque tous les réglages ont été effectués.

La structure finale est la suivante   *

-   Includes, avec des bibliothèques supplémentaires
-   Paramètres globaux, avec paramètres de radiosité
-   Sky sphere, avec une couleur plus claire
-   Planes, positionnés et avec des textures
-   Finitions et textures, avec des définitions personnalisées
-   Caméra, non changé
-   Source de lumière, avec des propriétés supplémentaires
-   Informations de maillage et de corps, en utilisant les textures définies précédemment


**Note   ***

les sections du fichier `.pov` peuvent être arrangées dans n\'importe quel ordre bien qu\'il soit probablement plus facile de travailler avec le fichier si les informations de maillage sont à la fin.

Le rendu final peut être effectué en cliquant sur **<img src="images/Raytrace_Render.svg" width=16px> [Render](Raytracing_Render.md)** ou en exécutant l\'exécutable à partir de la ligne de commande.


```python
povray assembly.pov +W800 +H600 +AM2 +A
```

<img alt="" src=images/12_T04_FreeCAD_POVray_render_floor_wood_walls_radiosity_final.png  style="width   *600px;">



*align=center|A partir du modèle standard, le rendu de la scène avec POV-Ray, avec la source de lumière et sky sphere configurée, des matériaux assignés, un plan d'étage avec une texture de parquet et des murs arrière avec des textures de cloison sèche.Paramètres de radiosité pour un rendu rapide   *`Radiosity_Final* et {{incode|recursion_limit 2`.}}


<div class="toccolours mw-collapsible mw-collapsed">

Ceci le contenu complet du fichier `.pov`, mais sans la dernière section, c\'est-à-dire sans les maillages.


<div class="mw-collapsible-content">


```python
// Persistence of Vision Ray Tracer Scene Description File
// for FreeCAD (http   *//www.freecadweb.org)

#version 3.6;

#include "colors.inc"
#include "metals.inc"
#include "woods.inc"
#include "glass.inc"
#include "stones.inc"
#include "rad_def.inc"

// 
#declare Rad_Quality = 3;

global_settings {
    assumed_gamma 1.0
    ambient_light color rgb <1.0,1.0,1.0>
    max_trace_level 20

#switch (Rad_Quality)
 #case (1)
    radiosity { // Settings 1 (fast)
        Rad_Settings(Radiosity_Fast, off, off)
    }
    #break
 #case (2)
    radiosity { // Settings 2 (medium quality)
        Rad_Settings(Radiosity_2Bounce, on, on)
    }
    #break
 #case (3)
    radiosity{ // Settings 3 (high quality)
        Rad_Settings(Radiosity_Final, on, on)
        recursion_limit 2
    }
    #break
#end
}

// 


sky_sphere {
    pigment {
        gradient y
        color_map {
            [0.0 color Gray50]
            [0.7 color White]
        }
    }
}


// 

#declare Parquet_normal = normal {
    gradient z 2 slope_map { [0 <0,1>][0.05 <1,0>][0.95 <1,0>][1 <0,-1>] }
    scale 80
} ;

// Floor
plane {
    y, -1
    pigment {
        wood color_map { M_Wood8A }
        turbulence 0.5 scale <10, 1, 1>*20
    }
    normal {
        average normal_map {
          [1 Parquet_normal]
          [1 wood 0.5 slope_map { [0 <0,0>][0.5 <0.5,1>][1 <1,0>] }
              turbulence 0.5 scale <10, 1, 1>*20]
        }
    }
    finish { ambient 0.0 reflection 0.1 specular 0.2 }
}

// Back wall
plane {
    z, 10
    texture {
        T_Grnt1   
        scale 0.02
    }
}

// Behind camera wall
plane {
    z, -3700
    texture {
        T_Grnt1   
        scale 0.02
    }
}

#declare T_mirror = texture {
    finish { reflection {0.9} }
//    finish { F_MetalE }
}

#declare T_wood = texture {
    T_Wood7
    scale 50.0
    translate x*1
    translate y*10
}

#declare M_vase = material {
    texture {
        pigment { color rgbf <1.0, 0.73333, 0.0, 0.75> }
        finish { F_Glass2 }
    }
    interior { I_Glass caustics 1.0 }
}
// declares position and view direction

// Generated by FreeCAD (http   *//www.freecadweb.org/)
#declare cam_location =  <-171.753,1229.11,-2667.08>;
#declare cam_look_at  = <636.959,359.955,160.296>;
#declare cam_sky      = <0.068217,0.958943,0.275273>;
#declare cam_angle    = 45; 
camera {
  location  cam_location
  look_at   cam_look_at
  sky       cam_sky
  angle     cam_angle 
  right x*800/600
}
//default light
light_source {
    <1200, 1000, -1300>
    color White
    area_light <100, 0, 0>, <0, 0, 100>, 20, 20
    adaptive 1
    jitter
    circular orient
    fade_distance 1000 fade_power 2
}
// Written by FreeCAD http   *//www.freecadweb.org/
// face number1 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
// ... meshes should be defined here until the end of the file ...
```


</div>


</div>

## Notes Finales 

POV-Ray est un logiciel relativement ancien, publié pour la première fois au début des années 90. Ses principaux avantages par rapport aux logiciels plus modernes   *

-   c\'est une solution testée qui existe depuis de nombreuses années
-   fonctionne dans de nombreux systèmes d\'exploitation
-   la scène peut être définie avec un seul fichier texte
-   nécessite des ressources informatiques simples pour produire une image de haute qualité, de sorte qu\'il fonctionne même avec du matériel relativement ancien

Il est conseillé à l\'utilisateur de lire la documentation de POV-Ray, ainsi que d\'autres tutoriels ou exemples pour définir les paramètres adaptés à ses besoins.

-   [POV-Ray for Unix version 3.7](http   *//www.povray.org/documentation/3.7.0/index.html)
-   [POV-Ray Tutorial](http   *//www.povray.org/documentation/3.7.0/t2_0.html)
-   [POV-Ray Reference](http   *//www.povray.org/documentation/3.7.0/r3_0.html)


 {{Raytracing Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [Raytracing](Category_Raytracing.md) > Tutorial FreeCAD POV ray/fr
