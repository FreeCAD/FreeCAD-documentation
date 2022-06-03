# <img alt="Icône de l\'atelier externe FCGear" src=images/FCGear_workbench_icon.svg  style="width   *64px;"> FCGear Workbench/fr

## Introduction


{{TOCright}}

L**\'atelier FCGear** est un [atelier externe](external_workbenches/fr.md) pour la fabrication de différents types d\'engrenages et vis sans fin dans FreeCAD. La modélisation paramétrique permet de modifier à tout moment les géométries requises. Par exemple, en modifiant quelques paramètres, l\'engrenage à développante devient soit un engrenage droit, un engrenage hélicoïdal ou un engrenage hélicoïdal double.

Pour que les résultats de FCGear soient utilisables, une certaine connaissance de base des différents types d\'engrenages est nécessaire. Module, diamètre primitif et diamètre de base sont des termes courants qui doivent donc être connus.

Parallèlement à l\'impression 3D, les utilisateurs à domicile ont désormais la possibilité de concevoir et de produire des engrenages et des vis sans fin selon leurs propres idées personnelles et, si nécessaire, de les adapter à leurs conditions de construction.

Avant de démarrer l\'[atelier FCGear](FCGear_Workbench/fr.md), il doit être installé (pour savoir comment, voir chapitre **Installation** ci-dessous). Après l\'installation, les outils sont disponibles dans la barre d\'outils.

   *   ![](images/FCGear_Drop-down-menu_example-en.png )
   *   
    
*Le menu déroulant de FCGear*
    

## Types d\'engrenages 

### Engrenage à développante 

   *   ![](images/Involute-Gear_example.png )
   *   
    
*De gauche à droite    * engrenage droit, engrenage hélicoïdal, double engrenage hélicoïdal (Voir [FCGear Engrenage à développante](FCGear_InvoluteGear/fr.md))*
    

### Engrenage à crémaillère 

   *   ![](images/Involute-Rack_example.png )
   *   
    
*De gauche à droite    * crémaillère droite, crémaillère pour engrenage hélicoïdal, crémaillère pour double engrenage hélicoïdal (voir [FCGear Engrenage à crémaillère](FCGear_InvoluteRack/fr.md))*
    

### Engrenage cycloïde 

   *   ![](images/Cycloid-Gear_example_1.png )
   *   
    
*De gauche à droite    * engrenage droit, engrenage hélicoïdal, engrenage double hélicoïdal (voir [FCGear Engrenage cycloïde](FCGear_CycloideGear/fr.md))*
    

### Engrenage conique 

   *   ![](images/Bevel-Gear_example.png )
   *   
    
*De gauche à droite    * engrenage droit, engrenage en spirale (voir [FCGear Engrenage conique](FCGear_BevelGear/fr.md))*
    

### Vis sans fin 

   *   ![](images/Worm-Gear_example.png )
   *   
    
*Ci-dessus    * engrenage à vis sans fin (voir [FCGear Vis sans fin](FCGear_WormGear/fr.md))*
    

### Engrenage couronne 

   *   ![](images/Crown-Gear_example.png )
   *   
    
*Ci-dessus    * Engrenage couronne (voir [FCGear Engrenage couronne](FCGear_CrownGear/fr.md))*
    

### Engrenage de distribution et pignon lanterne 

   *   ![](images/Timing+Latern-gear_example.png )
   *   
    
*De gauche à droite    * engrenage de distribution, engrenage de lanterne (voir [FCGear Engrenage de distribution](FCGear_TimingGear/fr.md) ou [FCGear Pignon lanterne](FCGear_LanternGear/fr.md))*
    

## Références

-   Auteur    * looooo
-   Home page    * <https   *//github.com/looooo/FCGear>
-   Code source sur Github    * <https   *//github.com/looooo/FCGear>

## Outils

### Barre d\'outils 

-   <img alt="" src=images/FCGear_InvoluteGear.svg  style="width   *32px;"> [FCGear Engrenage à développante](FCGear_InvoluteGear/fr.md) Crée un engrenage à développante
-   <img alt="" src=images/FCGear_InvoluteRack.svg  style="width   *32px;"> [FCGear Crémaillère](FCGear_InvoluteRack/fr.md) Crée une crémaillère
-   <img alt="" src=images/FCGear_CycloideGear.svg  style="width   *32px;"> [FCGear Engrenage cycloïde](FCGear_CycloideGear/fr.md) Crée un engrenage cycloïde
-   <img alt="" src=images/FCGear_BevelGear.svg  style="width   *32px;"> [FCGear Engrenage conique](FCGear_BevelGear/fr.md) Crée un engrenage conique
-   <img alt="" src=images/FCGear_WormGear.svg  style="width   *32px;"> [FCGear Vis sans fin](FCGear_WormGear/fr.md) Crée une vis sans fin
-   <img alt="" src=images/FCGear_CrownGear.svg  style="width   *32px;"> [FCGear Engrenage couronne](FCGear_CrownGear/fr.md) Crée un engrenage couronne
-   <img alt="" src=images/FCGear_TimingGear.svg  style="width   *32px;"> [FCGear Engrenage de distribution](FCGear_TimingGear/fr.md) Crée un pignon de synchronisation
-   <img alt="" src=images/FCGear_LanternGear.svg  style="width   *32px;"> [FCGear Pignon lanterne](FCGear_LanternGear/fr.md) Crée un pignon lanterne

## Installation

### Installation Automatique 

La méthode d\'installation recommandée à partir de la v0.17 est via le <img alt="" src=images/Std_AddonMgr.svg  style="width   *24px;"> [Gestionnaire d\'Addon](Std_AddonMgr/fr.md). Elle est accessible dans le menu **Outils → Gestionnaire d'Addon**.


<div class="mw-collapsible mw-collapsed toccolours" style="width   *700px">

### Installation manuelle 

S\'il est nécessaire d\'installer manuellement cet atelier, les instructions suivantes sont fournies pour ce faire    *


<div class="mw-collapsible-content">

#### Linux

-    `git clone https   *//github.com/looooo/FCGear.git`
    

-   link or copy the folder into **/freecad/Mod**

   *   

       *   
        `sudo ln -s (path_to_FCGear) (path_to_freecad)/Mod`
        

#### Windows

Testé sous (7/8/8.1/10) (d\'après GitHub)

-   téléchargez l\'archive ZIP en cliquant sur le bouton en haut à droite
-   allez dans FreeCAD-Macro-Folder (dans FreeCAD, choisissez \"Edition \> Préférences \> Général \> Macro pour voir le chemin de la macro)
-   si vous n\'avez pas modifié les paramètres standard, il doit s\'agir de \"C   *Users\\Your\_Windows\_User\_Name\\AppData\\Roaming\\FreeCAD\"
-   \\ appdata est un dossier *caché*\', vous devrez donc peut-être modifier les paramètres de l\'explorateur de fichiers pour le voir
-   créer un sous-dossier appelé \"FCGear\"
-   assurez-vous de copier les fichiers et dossiers EXACTEMENT comme indiqué ci-dessus dans le sous-dossier que vous venez de créer
-   redémarrez FreeCAD et l\'atelier devrait apparaître dans le menu déroulant
-   dans FreeCAD, vous pouvez choisir \"Outils \> Personnaliser \> Ateliers\" pour activer/désactiver les ateliers

#### MacOSX

Voir les instructions pour Linux ci-dessus


</div>


</div>

## Liens vers WB engrenage 

-   Wiki de l\'atelier    * <https   *//github.com/looooo/FCGear/wiki>
-   Wiki FreeCAD    * [Macro\_FCGear](http   *//www.freecadweb.org/wiki/index.php?title=Macro_FCGear) et [Bevel gear](http   *//forum.freecadweb.org/viewtopic.php?f=3&t=12878)
-   Forum FreeCAD    * <http   *//forum.freecadweb.org/viewtopic.php?f=21&t=12968>
-   Tutoriels    *
-   Vidéos    *
-   Fichiers    *
-   Rapports de bugs    * SVP rapportez les bugs sur <https   *//github.com/looooo/FCGear/issues>

## Autres liens intéressants 

-   <img alt="PartDesign\_InvoluteGear" src=images/PartDesign_InvoluteGear.svg  style="width   *24px;"> [PartDesign Engrenage droit à développante](PartDesign_InvoluteGear/fr.md)    * cet outil permet de créer un profil 2D d\'un engrenage à développante. Ce profil 2D est entièrement paramétrique et peut être complété avec la fonction [PartDesign Protrusion](PartDesign_Pad/fr.md).
-   [Ateliers externes](External_workbenches/fr.md)    * une liste de tous les ateliers externes actuels de FreeCAD
-   [Macros](Macros_recipes/fr.md)
-   [L\'engrenage cycloïdal (allemand)](https   *//vivat-geo.de/zykloidenverzahnung.html)
-   [Engrenage à développante (allemand)](https   *//vivat-geo.de/evolventenverzahnung.html)




[Category   *External Workbenches](Category_External_Workbenches.md) [Category   *Addons](Category_Addons.md) [Category   *FCGear](Category_FCGear.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [External Workbenches](Category_External Workbenches.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > FCGear Workbench/fr
