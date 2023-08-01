---
- GuiCommand:
   Name:Arch Equipment
   Name/fr:Arch Équipement
   MenuLocation:Arch → Équipement
   Workbenches:[Arch](Arch_Workbench/fr.md)
   Shortcut:**E** **Q**
   SeeAlso:[Arch 3 vues depuis maillage](Arch_3Views/fr.md)
---

# Arch Equipment/fr

## Description

L\'outil Équipement vous offre un moyen simple et pratique d\'insérer des éléments autonomes, non structurels tels que des meubles, des équipements sanitaire ou appareils électriques à vos projets. Les équipements sont basés sur des [objets Part](Part_Workbench/fr.md), ce qui leur permet de bénéficier de la solidité et des possibilités de la géométrie BRep et de générer de jolies vues lors du rendu en vue en plan et en coupe.

![](images/Arch_equipment_example.jpg ) 
*Objets d'ameublement dans un objet [Arch Équipement](Arch_Equipment/fr.md). Les projections à plat peuvent être obtenues par l'outil [Draft Vue 2D d'une forme](Draft_Shape2DView/fr.md)*

A partir de la version 0.17, les objets d\'équipement ont aussi une propriété **HiRes** où un objet [Mesh](Mesh_Workbench/fr.md) peut être attaché. Les objets équipement peuvent ensuite être créés pour afficher ce maillage dans la vue 3D au lieu de leur forme, ce qui permet d\'utiliser des objets maillés haute résolution tels que des meubles détaillés que l\'on trouve généralement sur les sites Web.

![](images/Arch_equipment_mesh.jpg ) 
*Objets d'ameublement dans un objet [Arch Équipement](Arch_Equipment/fr.md) avec un maillage haute résolution*

Lors de l\'utilisation de l\'exportateur Arch OBJ, tous les équipements en mode d\'affichage Mesh seront exportés en tant que maillage au lieu d\'objet forme.



## Utilisation

1.  Sélectionnez une forme [Part](Part_Workbench/fr.md), et optionnellement un objet [Mesh](Mesh_Workbench/fr.md).
2.  Appuyez sur le bouton **<img src="images/Arch_Equipment.png" width=16px> [Équipement](Arch_Equipment/fr.md)** ou appuyez la touche **E** puis **Q**.

## Options

-   Les équipements partagent les propriétés communes et les comportements de tous les [Arch Composants](Arch_Component/fr.md)



## Propriétés

-    **Model**: Une description du modèle de cet équipement.

-    **Url**: Une URL de la page du produit, où plus d\'informations sur cet équipement peut être trouvée.

-    **Mesh**: Représentation de cet équipement en objet [Mesh](Mesh_Workbench.md). Lorsqu\'il est défini, le mode d\'affichage **Maillage** devient disponible.



## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

L\'outil Équipement peut-être utilisé dans des [macros](Macros/fr.md) et depuis la console [Python](Python/fr.md) en utilisant la fonction suivante : 
```python
Equipment = makeEquipment(baseobj=None, placement=None, name="Equipment")
```

-   Crée un objet `Equipment` à partir d\'un `baseobj` ou un objet `Part` ou `Mesh`
-   Si `placement` est donné, il sera utilisé.
-   Retourne `None` si l\'opération échoue.

Exemple : 
```python
import FreeCAD, Arch

Box = FreeCAD.ActiveDocument.addObject("Part::Box", "Box")
Box.Length = 500
Box.Width = 2000
Box.Height = 600

Equip = Arch.makeEquipment(Box)
FreeCAD.ActiveDocument.recompute()
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Equipment/fr
