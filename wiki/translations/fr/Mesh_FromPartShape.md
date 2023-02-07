---
- GuiCommand:/fr
   Name:Mesh FromPartShape‏‎
   Name/fr:Mesh Créer un maillage
‏‎   MenuLocation:Maillages → Créer un maillage à partir d'une forme...
   Workbenches:[Mesh](Mesh_Workbench/fr.md)
---

# Mesh FromPartShape/fr

## Description

La commande **Créer un maillage** crée des objets [maillés](mesh/fr.md) non paramétriques, [Mesh Features](Mesh_Feature/fr.md), à partir de la [forme](shape/fr.md) d\'objets ([Part Features](Part_Feature/fr.md)).

L\'opération inverse est [Part Forme à partir du maillage](Part_ShapeFromMesh/fr.md) depuis l\'<img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [atelier Part](Part_Workbench/fr.md).



## Utilisation

1.  Sélectionnez éventuellement un ou plusieurs objets.
2.  Il existe plusieurs manières de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/_Mesh_FromPartShape.svg" width=16px> [Créer un maillage à partir d'une forme...](Mesh_FromPartShape/fr.md)**.
    -   Sélectionnez l\'option **Maillages → <img src="images/_Mesh_FromPartShape.svg" width=16px> Créer un maillage à partir d'une forme...** du menu.
3.  Le panneau des tâches **Tessellation** s\'ouvre.
4.  Lorsque le panneau des tâches est ouvert, vous pouvez créer une nouvelle sélection ou modifier une sélection existante.
5.  Sélectionnez l\'onglet du mailleur que vous souhaitez utiliser.
6.  Spécifiez les paramètres requis. Voir [Mailleurs](#Mailleurs.md).
7.  Appuyez sur le bouton **OK** pour fermer le panneau des tâches et terminer la commande.



## Mailleurs

Voici les mailleurs disponibles et leurs paramètres :



### Mailleur standard 

-    **Déviation de surface**: la [déviation linéaire](https://www.opencascade.com/doc/occt-7.3.0/overview/html/occt_user_guides__modeling_algos.html#occt_modalg_11_2) maximale d\'une section de maillage par rapport à la surface de l\'objet.

-    **Déviation angulaire**: la [déviation angulaire](https://www.opencascade.com/doc/occt-7.3.0/overview/html/occt_user_guides__modeling_algos.html#occt_modalg_11_2) maximale d\'une section de maillage à la suivante . Ce paramètre est utilisé lors du maillage de surfaces courbes.

-    **Écart relatif de surface**: si cochée, la déviation linéaire maximale d\'un segment de maillage sera **Déviation de surface** multipliée par la longueur du segment de maillage courant (bord).

-    **Appliquer les couleurs des faces au maillage**: si coché, le maillage obtiendra les couleurs de face de l\'objet.

-    **Définir les segments par les couleurs des faces**: si coché, les segments de maillage seront regroupés en fonction des couleurs des faces de l\'objet. Ces groupes seront exportés pour les formats de sortie de maillage prenant en charge cette fonctionnalité (le format [OBJ](https://fr.wikipedia.org/wiki/Objet_3D_(format_de_fichier)) par exemple).



### Mailleur Mefisto 

-    **Longueur maximale d'arêtes**: la longueur maximale du bord du maillage. Une valeur plus petite donne un maillage plus fin. Si vous spécifiez {{Value|0}} ou décochez la case, vous obtenez un maillage très grossier.

    -   Si vous appuyez sur le bouton **Estimation**, le mailleur entrera une valeur estimée pour **Longueur maximale d'arêtes**. Cette valeur n\'est pas très fiable si plusieurs objets ont été sélectionnés.



### Mailleur Netgen 

-    **Finesse**: sélectionnez une option pour la finesse du maillage:

    -   
        **Trés grossier**
        

    -   
        **Grossier**
        

    -   
        **Moyen**
        

    -   
        **Fin**
        

    -   
        **Trés fin**
        

    -   
        **Défini par l'utilisateur**
        
        : pour cette option, les paramètres suivants peuvent être spécifiés:

        -   
            **Classement des tailles de maillages**
            
            : une valeur plus petite donne un maillage plus fin. La valeur doit être comprise dans la plage {{Value|0.1}} - {{Value|1.0}}.

        -   
            **Élément par arête**
            
            : une valeur plus grande donne un maillage plus fin. La valeur doit être comprise dans la plage {{Value|0.2}} - {{Value|10.0}}.

        -   
            **Élément par rayon de courbure**
            
            : une valeur plus grande donne un maillage plus fin. La valeur doit être comprise dans la plage {{Value|0.2}} - {{Value|10}}.

-    **Optimiser la surface**: si coché, la forme de la surface sera optimisée.

-    **Éléments de second ordre**: si coché, les éléments du second ordre seront générés résultant en un maillage plus fin.

-    **Principalement des quadrilatères**: si coché, le maillage utilisera de préférence des [faces de quadrilatères](https://en.wikipedia.org/wiki/Types_of_mesh#Two-dimensional).



### Mailleur Gmsh 


{{Version/fr|0.19}}

Pour les utilisateurs Linux : le module externe [Gmsh](https://gmsh.info/) est requis.

-    **Maillage**: sélectionnez une option de maillage :

    -   
        **Automatique**
        

    -   
        **Adaptif**
        

    -   
        **Delaunay**
        

    -   
        **Frontal**
        

    -   
        **BAMG**
        

    -   
        **Quadrangle frontal**
        

    -   
        **Parallélogrammes**
        

-    **Taille maximale de l'élément**: une valeur plus petite donne un maillage plus fin. Spécifiez {{Value|0}} pour que cette taille soit automatiquement déterminée.

-    **Taille minimale de l'élément**: une valeur plus petite donne un maillage plus fin. La valeur doit être inférieure à **Taille maximale de l'élément**. Spécifiez {{Value|0}} pour que cette taille soit automatiquement déterminée.

-    **Angle**: semble ne pas être pris en charge pour le moment.

-    **Chemin**: appuyez sur le bouton **...** et allez jusqu\'au chemin **gmsh.exe**.

-   Si le processus de maillage prend trop de temps, vous pouvez appuyer sur le bouton **Arrêter** pour l\'abandonner.

-   Appuyez sur le bouton **Effacer** pour supprimer les informations de la zone de texte.



## Remarques

-   Cette commande n\'est pas limitée aux objets créés avec l\'[atelier Part](Part_Workbench/fr.md). Il peut créer un maillage à partir de n\'importe quel objet qui a une forme, y compris des objets créés avec l\'[atelier Part](PartDesign_Workbench/fr.md).
-   La commande [Std Exporter](Std_Export/fr.md) peut exporter des objets de forme directement vers un format de maillage.
-   Voir aussi : Tutoriel [Exportation de fichier STL ou OBJ](Export_to_STL_or_OBJ/fr.md).



## Préférences



### Mailleur standard 

-   Le paramètre **Déviation de surface** est enregistré : **Outils → Editer les de paramètres... → BaseApp → Preferences → Mod → Mesh → Meshing → Standard → LinearDeflection**.
-   Le paramètre **Déviation angulaire** est enregistré : **Outils → Editer les paramètres... → BaseApp → Preferences → Mod → Mesh → Meshing → Standard → AngularDeflection**.
-   Le paramètre **Écart relatif de surface** est enregistré : **Outils → Editer les paramètres... → BaseApp → Preferences → Mod → Mesh → Meshing → Standard → RelativeLinearDeflection**.



### Mailleur Gmsh 

-    **Chemin**est enregistré : **Outils → Editer les paramètres... → BaseApp → Preferences → Mod → Mesh → Meshing → gmshExe**.



## Propriétés

Voir : [Mesh Feature](Mesh_Feature/fr.md).



## Script

Voir aussi : [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

Pour créer un objet maillé à partir d\'un objet forme, utilisez la méthode `meshFromShape` du module MeshPart. Cette méthode a plusieurs signatures. La signature détermine le mailleur qui sera utilisé. L\'exemple ci-dessous utilise la signature de maillage Mefisto.


```python
import FreeCAD, Part, Mesh, MeshPart

cyl = FreeCAD.ActiveDocument.addObject("Part::Cylinder","Cylinder")
FreeCAD.ActiveDocument.recompute()

msh = FreeCAD.ActiveDocument.addObject("Mesh::Feature", "Mesh")
msh.Mesh = MeshPart.meshFromShape(Shape=cyl.Shape, MaxLength=1)
msh.ViewObject.DisplayMode = "Flat Lines"
```





{{Mesh Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh FromPartShape/fr
