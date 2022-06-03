---
- GuiCommand   */fr
   Name   *PartDesign Fillet
   Name/fr   *PartDesign Congé 
   MenuLocation   *Part Design → Appliquer une fonction d'habillage → Congé
   Workbenches   *[PartDesign](PartDesign_Workbench/fr.md)
   SeeAlso   *[PartDesign Chanfrein](PartDesign_Chamfer/fr.md)
---

# PartDesign Fillet/fr

## Description


<div class="mw-translate-fuzzy">

Cet outil crée des congés (arrondis) sur les bords sélectionnés d\'un objet. Une nouvelle entrée de congé séparée (suivie d\'un numéro séquentiel s\'il existe déjà des congés dans le document) est créée dans l\'arborescence du projet.


</div>

## Utilisation

### Add a fillet 


<div class="mw-translate-fuzzy">

-   Sélectionnez une ou plusieurs arêtes ou une face sur un objet, puis lancez l\'outil en cliquant sur son icône ou en allant dans le menu. Si vous avez sélectionné une face ou un objet 3D ({{Version/fr|0.20}}), toutes ses arêtes sont prises en compte pour le congé.
-   Dans le [Panneau des tâches](Task_Panel/fr.md) qui apparaît, réglez le rayon du congé soit en entrant la valeur, soit en cliquant sur les flèches haut/bas.
-   Après avoir cliqué sur le bouton **Ajouter**, vous pouvez ajouter toutes les arêtes de l\'objet en faisant un clic droit et en sélectionnant **Ajouter tous les bords** dans le menu contextuel. {{Version/fr|0.20}}
-   Si vous voulez ajouter plus d\'arêtes ou de faces, cliquez sur le bouton **Ajouter** et sélectionnez les arêtes et/ou les faces.
-   Si vous voulez supprimer des arêtes ou des faces
    -   sélectionnez l\'arête/la face dans la liste du dialogue et appuyez sur la touche **Suppr**. *Remarque*    * puisqu\'il doit y avoir au moins une arête pour la fonction, la dernière arête ou face restante dans la liste ne peut pas être supprimée.
    -   ou cliquez sur le bouton **Suppression**. Toutes les arêtes et faces précédemment sélectionnées sont surlignées en violet. Sélectionnez l\'arête ou la face à supprimer.
    -   Assurez-vous que la case **Utiliser tous les bords** n\'est pas cochée, sinon certains widgets de la boîte de dialogue seront désactivés. {{Version/fr|0.20}}
-   Cliquez sur **OK** pour valider.
-   Pour une chaîne d\'arêtes tangentes les unes aux autres, une seule arête peut être sélectionnée. Le congé se propagera le long de la chaîne.
-   Pour éditer le filet après la validation de la fonction, double-cliquez sur l\'étiquette du filet dans l\'arbre du projet ou cliquez dessus avec le bouton droit de la souris et sélectionnez **Modifier le congé**.


</div>

### Edit a fillet 

1.  Do one of the following   *
    -   Double-click the Fillet object in the [Tree view](Tree_view.md)
    -   Right-click the Fillet object in the [Tree view](Tree_view.md) and select **Edit Fillet** from the context menu.
2.  The **Fillet parameters** [task panel](Task_panel.md) opens.See [Options](#Options.md) for more information.
3.  Press the **OK** button to finish.

## Options

-   To add edges do one of the following   *
    -   Press the **Add** button to start selecting edges and/or faces in the [3D view](3D_view.md).
    -   To select all remaining edges do the following   *
        1.  If required press the **Add** button.
        2.  Use the **Ctrl**+**Shift**+**A** keyboard shortcut, or right-click the list and select **Add all edges** from the context menu. <small>(v0.20)</small> 
-   To remove edges do one of the following   *
    -   Press the **Remove** button to start deselecting edges and/or faces in the [3D view](3D_view.md). Selected elements are highlighted in purple.
    -   Select one or more elements in the list and press the **Del** key, or right-click the list and select **Remove** from the context menu.
-   Set the **Radius** of the fillet.
-   Check the **Use all edges** checkbox to select all edges of the previous feature. This deactivates the selection list and the related buttons. <small>(v0.20)</small> 

## Remarques

-   Le PartDesign Congé ne doit pas être confondu avec le [Part Congé](Part_Fillet/fr.md). À moins que vous ne sachiez ce que vous faites, [Part Congé](Part_Fillet/fr.md) ne doit pas être utilisé sur un corps PartDesign. Voir [Part et PartDesign](Part_and_PartDesign/fr.md).
-   Les Congés ne peuvent pas entièrement épouser les faces adjacentes.

## Properties

See also   * [Property editor](Property_editor.md).

A PartDesign Fillet object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties   *

### Data


{{Properties_Title|Base}}

-    **Base|LinkSub**   * Link to the selected edges and faces of the parent feature. Can be a link to only the parent feature if **Use All Edges** is `True`.

-    **Support Transform|Bool**   * If `True` the filleted shape of the additive/subtractive parent feature will be used when the fillet object is included in a [pattern](PartDesign_Workbench#Transformation_tools.md), else only the shape of the fillet itself will be used. The default is `False`.

-    **Add Sub Shape|PartShape|hidden**
    

-    **Base Feature|Link|hidden**   * Link to the parent feature.

-    **_ Body|LinkHidden|hidden**   * Link to the parent body.


{{Properties_Title|Fillet}}

-    **Radius|QuantityConstraint**   * The fillet radius. The default is {{value|1 mm}}.

-    **Use All Edges|Bool**   * If `True` all edges of the feature are filleted, and the edges specified by **Base** are ignored. The default is `False`.


{{Properties_Title|Part Design}}

-    **Refine|Bool**   * If `True` redundant edges are removed from the result of the operation. The default value is determined by the **Automatically refine model after sketch-based operation** preference. See [PartDesign Preferences](PartDesign_Preferences#General.md).

## Problèmes connus 


<div class="mw-translate-fuzzy">

Les congés, chanfreins et autres fonctionnalités opérant sur les corps solides dépendent du noyau OpenCASCADE Technology (OCCT) sous-jacent utilisé par FreeCAD. Le noyau OCCT a parfois du mal à gérer les arêtes vives qui coïncident, là où deux faces se rencontrent. Si tel est le cas, FreeCAD peut se bloquer sans explication.


</div>


<div class="mw-translate-fuzzy">

Si FreeCAD est exécuté depuis le terminal, FreeCAD peut produire un fichier de logs comme celui-ci après le crash    *


</div>


{{code|lang=text|code=
#1  0x7fff63d660ba in BRep_Tool   *   *Curve(TopoDS_Edge const&, TopLoc_Location&, double&, double&) from /usr/lib/x86_64-linux-gnu/libTKBRep.so.7+0x2a
#2  0x7fff63d69546 in BRep_Tool   *   *Curve(TopoDS_Edge const&, double&, double&) from /usr/lib/x86_64-linux-gnu/libTKBRep.so.7+0x46
#3  0x7fff71f4fef5 in ChFi3d_Builder   *   *PerformIntersectionAtEnd(int) from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x3b05
#4  0x7fff71f58307 in ChFi3d_Builder   *   *PerformOneCorner(int, bool) from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x1097
#5  0x7fff71ef6218 in ChFi3d_Builder   *   *PerformFilletOnVertex(int) from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x4e8
#6  0x7fff71ef71d1 in ChFi3d_Builder   *   *Compute() from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0xe31
#7  0x7fff720ad7c3 in BRepFilletAPI_MakeChamfer   *   *Build() from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x33
#8  0x7fff723be48e in PartDesign   *   *Chamfer   *   *execute() from /usr/lib/freecad-daily/lib/_PartDesign.so+0x60e
...
}}


<div class="mw-translate-fuzzy">

Ce dernier fait référence à des fonctions situées dans `libTKBRep.so`, `libTKFillet.so`, etc. qui sont des bibliothèques OCCT. Si ce type de plantage se produit, le problème doit être signalé et résolu dans OCCT plutôt que dans FreeCAD.


</div>

Voir les discussions du forum pour plus d\'informations    *

-   [Bug Chamfer bigger than 2mm crashes freecad](https   *//forum.freecadweb.org/viewtopic.php?p=263818#p263818)
-   [Segfault when using part design fillet](https   *//forum.freecadweb.org/viewtopic.php?p=264827#p264827)

### Dénomination topologique 


<div class="mw-translate-fuzzy">

La numérotation des arêtes n\'est pas complètement stable. Il est donc conseillé de terminer la conception principale de votre corps solide avant d\'appliquer des fonctions telles que les congés et les chanfreins, sans quoi les arêtes risquent de changer de nom et les arêtes recevant un congé risquent de devenir invalides. Lorsque la propriété **Use All Edges** ({{Version/fr|0.20}}) est cochée à `True`, il existe une certaine protection contre ce problème. En effet, dans ce cas, toutes les arêtes de l\'objet de base sont utilisées et il n\'y a aucune dépendance vis-à-vis des noms des arêtes individuelles.


</div>

Voir la page [Problème de dénomination topologique](Topological_naming_problem/fr.md) pour en savoir plus.





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Fillet/fr
