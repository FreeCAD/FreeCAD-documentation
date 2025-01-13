---
 GuiCommand:
   Name: Part Boolean
   Name/fr: Part Opération booléenne
   MenuLocation: Part , Opération booléenne , Opération booléenne...
   Workbenches: Part_Workbench/fr
   SeeAlso: Part_Cut, Part_Fuse/fr, Part_Common/fr, Part_Section/fr
---

# Part Boolean/fr

## Description


**[<img src=images/Part_Boolean.svg style="width:16px"> [Part Opération booléenne](Part_Boolean/fr.md)**

est un outil booléen générique tout-en-un. Il vous permet de spécifier les objets et l\'opération à effectuer via une seule boîte de dialogue.

Pour des opérations booléennes plus rapides, voir aussi **[<img src=images/Part_Cut.svg style="width:16px"> [Part Soustraction](Part_Cut/fr.md)**, **[<img src=images/Part_Fuse.svg style="width:16px"> [Part Union](Part_Fuse/fr.md)**, **[<img src=images/Part_Common.svg style="width:16px"> [Part Intersection](Part_Common/fr.md)** et **[<img src=images/Part_Section.svg style="width:16px"> [Part Section](Part_Section/fr.md)**.

![PartBooleansDialog](images/PartBooleansDialog.png )



*Fenêtre de dialogue pour sélectionner des objets et effectuer des opérations booléennes avec eux*



## Utilisation

Voir les commandes individuelles :

-    **<img src="images/Part_Cut.svg" width=16px> [Part Soustraction](Part_Cut/fr.md)
**
    

-    **<img src="images/Part_Fuse.svg" width=16px> [Part Union](Part_Fuse/fr.md)
**
    

-    **<img src="images/Part_Common.svg" width=16px> [Part Intersection](Part_Common/fr.md)
**
    

-    **<img src="images/Part_Section.svg" width=16px> [Part Section](Part_Section/fr.md)
**
    



## Problèmes coplanaires 

Les opérations booléennes sont effectuées par le noyau de géométrie interne, [OpenCASCADE Technology](OpenCASCADE/fr.md) (OCCT). Cette bibliothèque a parfois des problèmes pour produire des résultats booléens lorsque les objets d\'entrée partagent une arête ou une face. Pour être sûr que l\'opération booléenne est réussie, la recommandation est que les formes se croisent clairement. Cela signifie que dans la plupart des cas, une forme doit dépasser ou être plus grande que l\'autre forme.

En cas de coplanarité, même si la première opération booléenne réussit, les opérations booléennes suivantes peuvent échouer. Dans ce cas, le problème peut ne pas être lié à la dernière opération effectuée, mais aux anciennes, c\'est-à-dire aux opérations imbriquées, comme indiqué dans la [Vue en arborescence](Tree_view/fr.md). Pour résoudre ces problèmes, il est recommandé d\'utiliser l\'outil **[<img src=images/Part_CheckGeometry.svg style="width:16px"> [Part Vérifier la géométrie](Part_CheckGeometry/fr.md)** pour inspecter tous les objets à la recherche de problèmes.

<img alt="" src=images/Part_Boolean_cut_coplanar_1.png  style="width:500px;">

<img alt="" src=images/Part_Boolean_cut_coplanar_2.png  style="width:500px;">



*À gauche : formes qui partagent une face, une soustraction booléenne peut produire des résultats incorrects. À droite : les formes qui s'entrecroisent clairement, la soustraction booléenne réussira dans la plupart des cas.*

<img alt="" src=images/Part_Boolean_fusion_coplanar_1.png  style="width:500px;">

<img alt="" src=images/Part_Boolean_fusion_coplanar_2.png  style="width:500px;">



*À gauche : formes qui partagent un visage, une union booléenne peut produire des résultats incorrects. À droite : des formes qui se croisent clairement, l'union booléenne réussira dans la plupart des cas.*





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Boolean/fr
