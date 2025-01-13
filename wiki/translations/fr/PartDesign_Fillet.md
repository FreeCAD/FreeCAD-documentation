---
 GuiCommand:
   Name: PartDesign Fillet
   Name/fr: PartDesign Congé 
   MenuLocation: PartDesign , Appliquer une fonction d'habillage , Congé
   Workbenches: PartDesign_Workbench/fr
   SeeAlso: PartDesign_Chamfer/fr
---

# PartDesign Fillet/fr

## Description

L\'outil <img alt="" src=images/PartDesign_Fillet.svg  style="width:24px;"> **PartDesign Congé** crée des filets (arrondis) sur les arêtes sélectionnées d\'un objet. Il ajoute un objet **Fillet** au document avec sa représentation correspondante dans la [vue en arborescence](Tree_view/fr.md).



## Utilisation



### Ajouter un congé 

1.  Vous pouvez [activer](PartDesign_Body/fr#Statut_actif.md) le corps recevant les congés.
2.  Il existe plusieurs façons de sélectionner les arêtes recevant le congé :
    -   Sélectionnez une ou plusieurs arêtes du corps individuellement.
    -   Sélectionnez une ou plusieurs faces du corps pour sélectionner toutes leurs arêtes.
    -   Sélectionnez un élément (généralement le dernier élément) du corps pour sélectionner toutes ses arêtes.
3.  Pour une chaîne d\'arêtes connectées tangentiellement, une seule arête doit être sélectionnée, le congé se propage le long de la chaîne.
4.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/PartDesign_Fillet.svg" width=16px> [Congé](PartDesign_Fillet/fr.md)**.
    -   Sélectionnez l\'option **PartDesign → Appliquer une fonction d'habillage → <img src="images/PartDesign_Fillet.svg" width=16px> Congé** du menu.
5.  S\'il n\'y a pas de corps actif, et qu\'il y a deux corps ou plus dans le document, la fenêtre de dialogue **Corps actif requis** s\'ouvrira et vous invitera à en activer un. S\'il n\'y a qu\'un seul corps, il sera activé automatiquement.
6.  Le [panneau des tâches](Task_panel/fr.md) **Paramètres du congé** s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
7.  Appuyez sur le bouton **OK** pour terminer.



### Modifier un congé 

1.  Effectuez l\'une des opérations suivantes :
    -   Double-cliquez sur l\'objet Fillet dans la [vue en arborescence](Tree_view/fr.md).
    -   Cliquez avec le bouton droit de la souris sur l\'objet Fillet dans la [vue en arborescence](Tree_view/fr.md) et sélectionnez **Modifier le congé** dans le menu contextuel.
2.  Le [panneau des tâches](Task_panel/fr.md) **Paramètres du congé** s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
3.  Appuyez sur le bouton **OK** pour terminer.

## Options

-   Pour ajouter des arêtes, effectuez l\'une des opérations suivantes :
    -   Appuyez sur le bouton **Ajouter** pour commencer à sélectionner des arêtes et/ou des faces dans la [vue 3D](3D_view/fr.md).
    -   Pour sélectionner toutes les arêtes restantes, procédez comme suit :
        1.  Si nécessaire, appuyez sur le bouton **Ajouter**.
        2.  Utilisez le raccourci clavier **Ctrl**+**Shift**+**A**, ou cliquez avec le bouton droit de la souris sur la liste et sélectionnez **Ajouter toutes les arêtes** dans le menu contextuel.
-   Pour supprimer des arêtes, effectuez l\'une des opérations suivantes :
    -   Appuyez sur le bouton **Supprimer** pour commencer à désélectionner les arêtes et/ou les faces dans la [vue 3D](3D_view/fr.md). Les éléments sélectionnés sont surlignés en violet.
    -   Sélectionnez un ou plusieurs éléments dans la liste et appuyez sur la touche **Suppr**, ou cliquez avec le bouton droit de la souris sur la liste et sélectionnez **Supprimer** dans le menu contextuel.
-   Définissez le **Rayon** du congé.
-   Cochez la case **Ajouter toutes les arêtes** pour sélectionner tous les arêtes de l\'élément précédent. Cela désactive la liste de sélection et les boutons associés.



## Remarques

-   Le PartDesign Congé ne doit pas être confondu avec le [Part Congé](Part_Fillet/fr.md). À moins que vous ne sachiez ce que vous faites, [Part Congé](Part_Fillet/fr.md) ne doit pas être utilisé sur un corps de PartDesign. Voir [Part et PartDesign](Part_and_PartDesign/fr.md).
-   Les congés ne peuvent pas entièrement épouser les faces adjacentes.



## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet PartDesign Fillet est dérivé d\'un [Part Feature](Part_Feature/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :



### Données


{{Properties_Title|Base}}

-    **Base|LinkSub**: lien vers les arêtes et les faces sélectionnées de l\'élément parent. Peut être un lien vers l\'élément parent uniquement si **Use All Edges** est `True`.

-    **Support Transform|Bool**: si `True`, la forme du congé de l\'élément parent additif/soustractif sera utilisée lorsque l\'objet congé est inclus dans un [motif](PartDesign_Workbench/fr#Outils_de_transformation.md), sinon seule la forme du congé sera utilisée. La valeur par défaut est `False`.

-    **Add Sub Shape|PartShape|hidden**
    

-    **Base Feature|Link|hidden**: lien vers l\'élément parent.

-    **_ Body|LinkHidden|hidden**: lien vers le corps du parent.


{{Properties_Title|Fillet}}

-    **Radius|QuantityConstraint**: rayon du congé. La valeur par défaut est {{value|1 mm}}.

-    **Use All Edges|Bool**: si `True`, toutes les arêtes de l\'élément sont pourvus de congés et les arêtes spécifiées par **Base** sont ignorées. La valeur par défaut est `False`.


{{Properties_Title|Part Design}}

-    **Refine|Bool**: si `True`, les arêtes redondantes sont supprimées du résultat de l\'opération. La valeur par défaut est déterminée par la préférence **Affiner les modèles automatiquement après une opération sur une esquisse**. Voir [PartDesign Préférences](PartDesign_Preferences/fr#G.C3.A9n.C3.A9ral.md).



## Problèmes connus 

Les congés, chanfreins et autres fonctionnalités opérant sur les corps solides dépendent du noyau [OpenCASCADE](OpenCASCADE/fr.md) Technology (OCCT) sous-jacent utilisé par FreeCAD. Le noyau OCCT a parfois du mal à gérer les arêtes vives qui coïncident, là où deux faces se rencontrent. Si tel est le cas, FreeCAD peut se bloquer sans explication.

S\'il est exécuté depuis le terminal, FreeCAD peut produire un fichier de logs comme celui-ci après un crash :


{{code|lang=text|code=
#1  0x7fff63d660ba in BRep_Tool::Curve(TopoDS_Edge const&, TopLoc_Location&, double&, double&) from /usr/lib/x86_64-linux-gnu/libTKBRep.so.7+0x2a
#2  0x7fff63d69546 in BRep_Tool::Curve(TopoDS_Edge const&, double&, double&) from /usr/lib/x86_64-linux-gnu/libTKBRep.so.7+0x46
#3  0x7fff71f4fef5 in ChFi3d_Builder::PerformIntersectionAtEnd(int) from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x3b05
#4  0x7fff71f58307 in ChFi3d_Builder::PerformOneCorner(int, bool) from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x1097
#5  0x7fff71ef6218 in ChFi3d_Builder::PerformFilletOnVertex(int) from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x4e8
#6  0x7fff71ef71d1 in ChFi3d_Builder::Compute() from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0xe31
#7  0x7fff720ad7c3 in BRepFilletAPI_MakeChamfer::Build() from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x33
#8  0x7fff723be48e in PartDesign::Chamfer::execute() from /usr/lib/freecad-daily/lib/_PartDesign.so+0x60e
...
}}

Cette sortie fait référence à des fonctions des bibliothèques OCCT. Si ce type de crash se produit, le problème doit être signalé et résolu dans OCCT plutôt que dans FreeCAD.

Voir les discussions du forum pour plus d\'informations :

-   [Bug Chamfer bigger than 2mm crashes freecad](https://forum.freecadweb.org/viewtopic.php?p=263818#p263818)
-   [Segfault when using PartDesign Fillet](https://forum.freecadweb.org/viewtopic.php?p=264827#p264827)



### Dénomination topologique 

La numérotation des arêtes n\'est pas complètement stable. Il est donc conseillé de terminer la conception principale de votre corps solide avant d\'appliquer des fonctions telles que les congés et les chanfreins, sans quoi les arêtes risquent de changer de nom et les arêtes recevant un congé risquent de devenir invalides. Lorsque la propriété **Use All Edges** est cochée à `True`, il existe une certaine protection contre ce problème. En effet, dans ce cas, toutes les arêtes de l\'objet de base sont utilisées et il n\'y a pas de dépendance à l\'égard des noms de chaque arête.

Voir la page [Problème de dénomination topologique](Topological_naming_problem/fr.md) pour en savoir plus.





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Fillet/fr
