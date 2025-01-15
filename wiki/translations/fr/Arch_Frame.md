---
 GuiCommand:
   Name: Arch Frame
   Name/fr: Arch Ossature
   MenuLocation: 3D/BIM , Ossature
   Workbenches: BIM_Workbench/fr
   Shortcut: **F** **R**
   SeeAlso: 
---

# Arch Frame/fr

## Description

L\'outil **Arch Ossature** sert à construire toutes sortes d\'objets structurels basés sur un profil et un schéma d\'agencement. Le profil est extrudé sur les bords du modèle, qui peut être n\'importe quel objet 2D comme une [esquisse](Sketcher_Workbench/fr.md) ou un [objet Draft](Draft_Workbench/fr.md). Il est particulièrement utile pour créer des rampes ou des murs. Les objets Ossature peuvent alors facilement être transformés en [murs](Arch_Wall/fr.md) ou en objets [structurels](Arch_Structure/fr.md).

<img alt="" src=images/Arch_Frame_example.jpg  style="width:640px;"> 
*Ici l'objet Frame (structure) est créé à partir d'un [Draft Réseau orthogonal](Draft_OrthoArray/fr.md) d'une [Draft Ligne](Draft_Line/fr.md) en utilisant un [Draft Cercle](Draft_Circle/fr.md) comme profil.*



## Utilisation

1.  Créez un schéma ou un objet modèle et un objet profil, par exemple avec l\'[atelier Draft](Draft_Workbench/fr.md) ou l\'[atelier Sketcher](Sketcher_Workbench/fr.md).
2.  Sélectionnez en premier l\'objet modèle, puis, maintenez la touche **Ctrl** enfoncée et sélectionnez l\'objet profil.
3.  Cliquez sur le bouton **<img src="images/Arch_Frame.svg" width=16px> [Ossature](Arch_Frame/fr.md)** ou appuyez sur **F** puis **R**.

## Options

-   Les ossatures partagent les propriétés et comportements communs de tous les objets [Arch Composants](Arch_Component/fr.md)
-   L\'objet ossature peut être placé à une certaine distance de l\'objet modèle, en définissant sa propriété Offset
-   Le profil sera copié à la base de chaque côté de l\'objet modèle, puis extrudé sur lui. Vous pouvez contrôler la façon dont le profil est placé à la base de chaque arête avec les propriétés Align et Rotation.



## Propriétés



### Données


{{TitleProperty|Component}}

-    **Base|Link**: la forme qui sert de base à l\'ossature.

Pour les autres propriétés du groupe, voir [Arch Composant](Arch_Component/fr#Propriétés.md).


{{TitleProperty|Frame}}

-    **Align|Bool**: spécifie si le profil doit être tourné pour que son axe normal soit aligné sur chaque arête.

-    **Base Point|Integer**: indice basé sur zéro indiquant le point de croisement de la trajectoire sur le profil :

    -   
        {{Value|0}}
        
        : la **Base** du **Placement** du profil. Ce point est également utilisé en cas d\'indice invalide.

    -   
        {{Value|1}}
        
        : le milieu de la première arête du profil.

    -   
        {{Value|2}}
        
        : l\'extrémité de la première arête du profil.

    -   
        {{Value|3}}
        
        : le milieu de la deuxième arête du profil.

    -   
        {{Value|4}}
        
        : l\'extrémité de la deuxième arête du profil.

    -   \...

    -   
        {{Value|n*2-1}}
        
        : le milieu de la nième arête du profil.

    -   
        {{Value|n*2}}
        
        : l\'extrémité de la nième arête du profil.

-    **Edges|Enumeration**: le type d\'arêtes à prendre en compte. Les options sont les suivantes :

    -   
        {{Value|All edges}}
        

    -   
        {{Value|Vertical edges}}
        

    -   
        {{Value|Horizontal edges}}
        

    -   
        {{Value|Bottom horizontal edges}}
        
        : basé sur la coordonnée globale Z du centre de masse de l\'arête.

    -   
        {{Value|Top horizontal edges}}
        
        : idem.

-    **Fuse|Bool**: si true, les solides qui se chevauchent sont fusionnés.

-    **Offset|VectorDistance**: distance facultative entre l\'objet de base et l\'objet ossature.

-    **Profile|Link**: profil sur lequel l\'ossature est basée.

-    **Profile Placement|Placement**: placement supplémentaire facultatif à ajouter au profil avant de l\'extruder. Seule la **Rotation** du **Placement** est utilisée. Ignoré si **Align** est `True`.

-    **Rotation|Angle**: rotation du profil autour de son axe d\'extrusion.



## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

L\'outil Frame peut être utilisé dans une [macro](Macros/fr.md) et dans la console [Python](Python/fr.md) en utilisant la fonction suivante :


```python
Frame = makeFrame(baseobj, profile)
```

-   Crée un objet `Frame` d\'un `baseobj` et `profile` donnés.
    -   
        `baseobj`
        
        est n\'importe quel objet contenant des filaires comme des [Draft Polylignes](Draft_Wire/fr.md) ou un [Draft Réseau orthogonal](Draft_OrthoArray/fr.md) et leur combinaison.

    -   
        `profile`
        
        est un objet 2D extrudable contenant des faces et des fils fermés.

Exemple :


```python
import Draft, Arch

Line = Draft.makeLine(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(0, 0, 2000))
baseobj = Draft.makeArray(Line, FreeCAD.Vector(1000, 0, 0), FreeCAD.Vector(0, 1, 0), 6, 1)

profile = Draft.makeCircle(200)
Frame = Arch.makeFrame(baseobj, profile)
FreeCAD.ActiveDocument.recompute()
```



---
⏵ [documentation index](../README.md) > Arch Frame/fr
