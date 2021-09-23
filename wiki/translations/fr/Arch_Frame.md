---
- GuiCommand:/fr
   Name:Arch Frame
   Name/fr:Arch Ossature
   MenuLocation:Arch → Ossature
   Workbenches:[Atelier Arch](Arch_Workbench/fr.md)
   Shortcut:**F** **R**
   SeeAlso:[Arch Mur](Arch_Wall/fr.md), [Arch Structure](Arch_Structure/fr.md)
---

# Arch Frame/fr

## Description

L\'outil **<img src="images/Arch_Frame.svg" width=16px> [Arch Ossature](Arch_Frame/fr.md)** sert à construire toutes sortes d\'objets structurels basés sur un profil et un schéma d\'agencement. Le profil est extrudé sur les bords du modèle, qui peut être n\'importe quel objet 2D comme une [esquisse](Sketcher_Workbench/fr.md) ou un [objet Draft](Draft_Workbench/fr.md). Il est particulièrement utile pour créer des rampes ou des murs. Les objets Ossature peuvent alors facilement être transformés en [murs](Arch_Wall/fr.md) ou en objets [structurels](Arch_Structure/fr.md).

<img alt="" src=images/Arch_Frame_example.jpg  style="width:640px;"> 
*Ici l'objet Frame (structure) est créé à partir d'un [Draft Réseau orthogonal](Draft_OrthoArray/fr.md) d'une [Draft Ligne](Draft_Line/fr.md) en utilisant un [Draft Cercle](Draft_Circle/fr.md) comme profil.*

## Utilisation

1.  Créer un schéma ou modèle d\'objet et le profil d\'un objet, par exemple avec l\'[atelier Draft](Draft_Workbench/fr.md) ou l\'[atelier Sketcher](Sketcher_Workbench/fr.md).
2.  Sélectionnez en premier l\'objet modèle, puis, maintenez la touche **Ctrl** enfoncée, et sélectionnez l\'objet à profiler.
3.  Cliquez sur le bouton **<img src="images/Arch_Frame.svg" width=16px> [Créer un objet forme...](Arch_Frame/fr.md)** ou appuyez sur **F** puis **R**.

## Options

-   Les ossatures partagent les propriétés et comportements communs de tous les objets [Arch Composants](Arch_Component/fr.md)
-   L\'objet ossature peut être placé à une certaine distance de l\'objet modèle, en définissant sa propriété Offset
-   Le profil sera copié à la base de chaque côté de l\'objet modèle, puis extrudé sur lui. Vous pouvez contrôler la façon dont le profil est placé à la base de chaque arête avec les propriétés Align et Rotation.

## Propriétés

-    {{PropertyData/fr|Base}}: Le modèle ou motif sur lequel cette structure est basée.

-    {{PropertyData/fr|Profile}}: Le profil sur lequel cette structure est basée.

-    {{PropertyData/fr|Align}}: Spécifie si le profil doit être tourné pour que son axe normal soit aligné avec chaque arête.

-    {{PropertyData/fr|Offset}}: Une option de distance entre l\'objet layout (modèle ou motif) et l\'objet frame (structure).

-    {{PropertyData/fr|Rotation}}: La rotation du profil autour de son axe d\'extrusion.

## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md) et [FreeCAD Scripts de Base](FreeCAD_Scripting_Basics/fr.md).

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
[documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Frame/fr
