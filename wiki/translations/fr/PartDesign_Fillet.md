---
- GuiCommand:/fr
   Name:PartDesign Fillet
   Name/fr:PartDesign Congé 
   MenuLocation:Conception de pièces → Appliquer une fonction d'habillage → Congé
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
   SeeAlso:[PartDesign Chanfrein](PartDesign_Chamfer/fr.md), [Part Congé](Part_Fillet/fr.md)
---

# PartDesign Fillet/fr

## Description

Cet outil crée des congés (arrondis) sur les bords sélectionnés d\'un objet. Une nouvelle entrée de congé séparée (suivie d\'un numéro séquentiel s\'il existe déjà des congés dans le document) est créée dans l\'arborescence du projet.

## Utilisation

-   Sélectionnez une ou plusieurs arêtes ou une face sur un objet, puis lancez l\'outil en cliquant sur son icône ou en allant dans le menu. Si vous avez sélectionné une face ou un objet 3D ({{Version/fr|0.20}}), toutes ses arêtes sont prises en compte pour le congé.
-   Dans le [Panneau des tâches](Task_Panel/fr.md) qui apparaît, réglez le rayon du congé soit en entrant la valeur, soit en cliquant sur les flèches haut/bas.
-   Après avoir cliqué sur le bouton **Ajouter**, vous pouvez ajouter toutes les arêtes de l\'objet en faisant un clic droit et en sélectionnant **Ajouter tous les bords** dans le menu contextuel. {{Version/fr|0.20}}
-   Si vous voulez ajouter plus d\'arêtes ou de faces, cliquez sur le bouton **Ajouter** et sélectionnez les arêtes et/ou les faces.
-   Si vous voulez supprimer des arêtes ou des faces
    -   sélectionnez l\'arête/la face dans la liste du dialogue et appuyez sur la touche **Suppr**. *Remarque* : puisqu\'il doit y avoir au moins une arête pour la fonction, la dernière arête ou face restante dans la liste ne peut pas être supprimée.
    -   ou cliquez sur le bouton **Suppression**. Toutes les arêtes et faces précédemment sélectionnées sont surlignées en violet. Sélectionnez l\'arête ou la face à supprimer.
    -   Assurez-vous que la case **Utiliser tous les bords** n\'est pas cochée, sinon certains widgets de la boîte de dialogue seront désactivés. {{Version/fr|0.20}}
-   Cliquez sur **OK** pour valider.
-   Pour une chaîne d\'arêtes tangentes les unes aux autres, une seule arête peut être sélectionnée. Le congé se propagera le long de la chaîne.
-   Pour éditer le filet après la validation de la fonction, double-cliquez sur l\'étiquette du filet dans l\'arbre du projet ou cliquez dessus avec le bouton droit de la souris et sélectionnez **Modifier le congé**.

## Remarques

-   Le PartDesign Congé ne doit pas être confondu avec le [Part Congé](Part_Fillet/fr.md). À moins que vous ne sachiez ce que vous faites, [Part Congé](Part_Fillet/fr.md) ne doit pas être utilisé sur un corps PartDesign. Voir [Part et PartDesign](Part_and_PartDesign/fr.md).

## Problèmes connus 

Les congés, chanfreins et autres fonctionnalités opérant sur les corps solides dépendent du noyau OpenCASCADE Technology (OCCT) sous-jacent utilisé par FreeCAD. Le noyau OCCT a parfois du mal à gérer les arêtes vives qui coïncident, là où deux faces se rencontrent. Si tel est le cas, FreeCAD peut se bloquer sans explication.

Si FreeCAD est exécuté depuis le terminal, FreeCAD peut produire un fichier de logs comme celui-ci après le crash :


{{code|code=
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

Ce dernier fait référence à des fonctions situées dans `libTKBRep.so`, `libTKFillet.so`, etc. qui sont des bibliothèques OCCT. Si ce type de plantage se produit, le problème doit être signalé et résolu dans OCCT plutôt que dans FreeCAD.

Voir les discussions du forum pour plus d\'informations :

-   [Bug Chamfer bigger than 2mm crashes freecad](https://forum.freecadweb.org/viewtopic.php?p=263818#p263818)
-   [Segfault when using part design fillet](https://forum.freecadweb.org/viewtopic.php?p=264827#p264827)

L\'utilisateur est également responsable de l\'intégrité de son propre modèle. Selon le modèle, il peut être impossible d\'effectuer un congé ou un chanfrein si le corps n\'est pas assez grand pour supporter cette opération. Par exemple, il ne serait pas possible de créer un congé de 10 mm si un bord n\'est séparé que de 5 mm de la surface suivante. Dans ce cas, le rayon maximal pour un congé serait de 5 mm ; essayer d\'utiliser une valeur plus grande peut entraîner une forme qui ne calcule pas, voire un crash. Si l\'utilisation de la limite exacte de 5 mm ne fonctionne pas, il est possible d\'utiliser une approximation très proche, telle que 4,9999 mm, pour obtenir le même résultat visible.

### Dénomination topologique 

La numérotation des arêtes n\'est pas complètement stable. Il est donc conseillé de terminer la conception principale de votre corps solide avant d\'appliquer des fonctions telles que les congés et les chanfreins, sans quoi les arêtes risquent de changer de nom et les arêtes recevant un congé risquent de devenir invalides. Lorsque la propriété **Use All Edges** ({{Version/fr|0.20}}) est cochée à `True`, il existe une certaine protection contre ce problème. En effet, dans ce cas, toutes les arêtes de l\'objet de base sont utilisées et il n\'y a aucune dépendance vis-à-vis des noms des arêtes individuelles.

Voir la page [Problème de dénomination topologique](Topological_naming_problem/fr.md) pour en savoir plus.

## Script

L\'outil **[16px|text-top=Congé|link=PartDesign_Fillet/fr](File:PartDesign_Fillet.svg.md) [Congés](PartDesign_Fillet/fr.md)** peut être utilisé dans une macro et à partir de la console Python en utilisant la fonction suivante :


```python
Box = Box.makeFillet(3,[Box.Edges[0]]) # 1 Fillet
Box = Box.makeFillet(3,[Box.Edges[1],Box.Edges[2],Box.Edges[3],Box.Edges[4]]) # for several Fillets
```

-   3 = rayon du congé
-   Box.Edges\[2\] = bord avec son numéro

Exemple :


```python
import PartDesign
from FreeCAD import Base

Box = Part.makeBox(10,10,10)
Box = Box.makeFillet(3,[Box.Edges[0]]) # pour 1 Fillet
Box = Box.makeFillet(3,[Box.Edges[1],Box.Edges[2],Box.Edges[3],Box.Edges[4]]) # for several Fillets
Part.show(Box)
```





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Fillet/fr
