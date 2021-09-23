---
- GuiCommand:/fr
   Name:Part Builder
   Name/fr:Part Générateur de forme
   MenuLocation:Pièce → Générateur de forme
   Workbenches:[Part](Part_Workbench/fr.md)
   SeeAlso:[Part Primitives](Part_Primitives/fr.md)
---

# Part Builder/fr

## Description

Outil pour créer des formes plus complexes à partir de diverses primitives géométriques paramétriques.

## Utilisation

Cet outil peut créer les objets suivants :

### Arête à partir de deux sommets 

1.  Sélectionnez deux sommets
2.  Cliquez sur **Créer**

![](images/Edge_from_verts-1.gif )

### Polyligne à partir d\'arêtes 

1.  Sélectionnez un ensemble d\'arêtes adjacentes dans la [vue 3D](3D_view/fr.md).
2.  Cliquez sur **Créer**

![](images/Wire_from_edges-1.gif )

### Face à partir de sommets 

1.  Sélectionner les sommets délimitant la face dans la [vue 3D](3D_view/fr.md).
2.  Sélectionnez si la face doit être planaire
3.  Cliquez sur **Créer**.
4.  L\'objet sera créé dans la [vue 3D](3D_view/fr.md) et sera répertorié dans la [Vue en arborescence](Tree_view/fr.md).

![](images/Face_from_verts.gif )

### Face à partir d\'arêtes 

1.  Sélectionner un ensemble fermé d\'arêtes délimitant la face dans la [Vue 3D](3D_view/fr.md).
2.  Sélectionnez si la face doit être planaire.
3.  Cliquez sur **Créer**.
4.  L\'objet sera créé dans la [Vue 3D](3D_view/fr.md) et sera répertorié dans la [Vue en arborescence](Tree_view/fr.md).

![](images/Face_from_edges.gif )

### Coque à partir de faces 

1.  Sélectionner les faces dans la [Vue 3D](3D_view/fr.md).
2.  Sélectionner si la forme doit être raffinée
3.  Sélectionnez si toutes les faces doivent être incluses dans la coque
4.  Cliquez sur **Créer**.
5.  L\'objet sera créé dans la [Vue 3D](3D_view/fr.md) et sera répertorié dans la [Vue en arborescence](Tree_view/fr.md).

### Solide à partir de coque 

1.  Sélectionnez si la forme doit être raffinée.
2.  Cliquez sur **Créer**.
3.  L\'objet sera créé dans la [Vue 3D](3D_view/fr.md) et sera répertorié dans la [Vue en arborescence](Tree_view/fr.md).

## Remarques

Un flux de travail possible pourrait être:

-   Dessiner un modèle filaire de votre forme à l\'aide des outils de l\'<img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [atelier Draft](Draft_Workbench/fr.md) (par exemple, ligne et fil).
-   Créer toutes les faces avec \"face à partir des bords\"
-   Créer une \"coque à partir de faces\"
-   Créer un \"solide à partir d\'une coque\"

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Builder/fr
