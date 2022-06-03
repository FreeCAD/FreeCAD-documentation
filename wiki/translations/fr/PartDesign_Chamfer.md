---
- GuiCommand   */fr
   Name   *PartDesign Chamfer
   Name/fr   *PartDesign Chanfrein
   MenuLocation   *Part Design → Appliquer une fonction d'habillage → Chanfrein
   Workbenches   *[PartDesign](PartDesign_Workbench/fr.md)
   SeeAlso   *[PartDesign Congé](PartDesign_Fillet/fr.md)
---

# PartDesign Chamfer/fr

## Description


<div class="mw-translate-fuzzy">

Cet outil crée des chanfreins sur les arêtes sélectionnées d\'un objet. Une nouvelle entrée distincte de chanfrein (suivie d\'un numéro consécutif s\'il existe déjà des chanfreins dans le document) est créée dans l\'arborescence du projet.


</div>

## Utilisation

### Add a chamfer 


<div class="mw-translate-fuzzy">

-   Sélectionnez une seule arête, plusieurs arêtes ou une face sur un objet, puis lancez l\'outil en cliquant sur le **<img src="images/PartDesign_Chamfer.svg" width=24px> '''Chanfrein'''** ou par le menu **Part Design → Appliquer une fonction d'habillage → Chanfrein**. Si vous avez sélectionné une face ou un objet 3D ({{Version/fr|0.20}}), toutes ses arêtes sont prises en compte pour le chanfreinage.
-   Dans le [Panneau des tâches](Task_Panel/fr.md) qui apparaît, vous pouvez définir le chanfrein de 3 manières    *
    -   
        **Cote égale**
        
           * les chanfreins sont également distants du bord du corps.

    -   
        **Deux cotes**
        
           * les distances du bord de chanfrein au bord du corps sont spécifiées. La direction de la distance peut être inversée. {{Version/fr|0.19}}

    -   
        **Cote et angle**
        
           * une distance du bord de chanfrein au bord du corps est spécifiée. Le deuxième bord de chanfrein est défini par l\'angle du chanfrein. La direction de la distance peut être inversée. {{Version/fr|0.19}}
-   Si vous souhaitez ajouter plus d\'arêtes ou de faces, cliquez sur le bouton **Ajouter** et sélectionnez les arêtes et/ou les faces.
-   Après avoir cliqué sur le bouton **Ajouter**, vous pouvez ajouter toutes les arêtes de l\'objet en faisant un clic droit et en sélectionnant **Ajouter tous les bords** dans le menu contextuel. {{Version/fr|0.20}}
-   Si vous souhaitez supprimer des arêtes ou des faces   *
    -   Sélectionnez l\'arête/la face dans la liste de la boîte de dialogue et appuyez sur la touche **Suppr**. *Remarque*    * puisqu\'il doit y avoir au moins une arête pour la fonction, la dernière arête ou face restante dans la liste ne peut pas être supprimée.
    -   ou cliquez sur le bouton **Supprimer**. Toutes les arêtes et faces sélectionnées précédemment sont surlignées en violet. Sélectionnez l\'arête ou la face à supprimer.
    -   Assurez-vous que la case **Utiliser tous les bords** n\'est pas cochée, sinon certains widgets de la boîte de dialogue seront désactivés. {{Version/fr|0.20}}
-   Cliquez sur **OK** pour valider.
-   Pour une chaîne d\'arêtes tangentes les unes aux autres, une seule arête peut être sélectionnée ; le chanfrein se propage le long de la chaîne.
-   Pour modifier le chanfrein après la validation de la fonction, double-cliquez sur l\'étiquette du chanfrein dans l\'arborescence du projet, ou faites un clic droit dessus et sélectionnez **Modifier le chanfrein**.


</div>

### Edit a chamfer 

1.  Do one of the following   *
    -   Double-click the Chamfer object in the [Tree view](Tree_view.md)
    -   Right-click the Chamfer object in the [Tree view](Tree_view.md) and select **Edit Chamfer** from the context menu.
2.  The **Chamfer parameters** [task panel](Task_panel.md) opens. See [Options](#Options.md) for more information.
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
-   Specify a chamfer **Type**   *
    -   
        **Equal distance**
        
           * One distance is used to place both chamfer edges.

    -   
        **Two distances**
        
           * Two distances are used to place the chamfer edges. <small>(v0.19)</small> 

    -   
        **Distance and angle**
        
           * A distance is used to place one chamfer edge, the placement of the other chamfer edge is defined by the angle of the chamfer. <small>(v0.19)</small> 
-   Press the **<img src="images/PartDesign_Flip_Direction.svg" width=16px> Flip direction** button to flip the direction of the chamfer (deactivated for **Equal distance**). <small>(v0.19)</small> 
-   Set the **Size** of the chamfer.
-   Set the **Size2** of the chamfer (only available if **Two distances** is selected).
-   Set the **Angle** of the chamfer (only available if **Distance and angle** is selected).
-   Check the **Use all edges** checkbox to select all edges of the previous feature. This deactivates the selection list and the related buttons. <small>(v0.20)</small> 

## Remarques

-   Le PartDesign Chanfrein ne doit pas être confondu avec le [Part Chanfrein](Part_Chamfer/fr.md). À moins que vous ne sachiez ce que vous faites, [Part Chanfrein](Part_Chamfer/fr.md) ne doit pas être utilisé sur un corps PartDesign. Voir [Part et PartDesign](Part_and_PartDesign/fr.md).
-   Les chanfreins ne peuvent pas entièrement épouser les faces adjacentes.

## Properties

See also   * [Property editor](Property_editor.md).

A PartDesign Chamfer object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties   *

### Data


{{Properties_Title|Base}}

-    **Base|LinkSub**   * Link to the selected edges and faces of the parent feature. Can be a link to only the parent feature if **Use All Edges** is `True`.

-    **Support Transform|Bool**   * If `True` the chamfered shape of the additive/subtractive parent feature will be used when the chamfer object is included in a [pattern](PartDesign_Workbench#Transformation_tools.md), else only the shape of the chamfer itself will be used. The default is `False`.

-    **Add Sub Shape|PartShape|hidden**
    

-    **Base Feature|Link|hidden**   * Link to the parent feature.

-    **_ Body|LinkHidden|hidden**   * Link to the parent body.


{{Properties_Title|Chamfer}}

-    **Camfer Type|Enumeration**   * The chamfer type   * {{value|Equal distance}} (default), {{value|Two distances}} or {{value|Distance and Angle}}.

-    **Size|QuantityConstraint**   * The first chamfer distance. The default is {{value|1 mm}}.

-    **Size2|QuantityConstraint**   * The second chamfer distance. Only used if **Camfer Type** is {{Value|Two distances}}. The default is {{value|1 mm}}.

-    **Angle|Angle**   * The chamfer angle. Only used if **Camfer Type** is {{Value|Distance and Angle}}. The default is {{value|45 °}}.

-    **Flip Direction|Bool**   * If `True` the direction of the chamfer is flipped. Not used if **Camfer Type** is {{Value|Equal distance}}. The default is `False`.

-    **Use All Edges|Bool**   * If `True` all edges of the feature are chamfered, and the edges specified by **Base** are ignored. The default is `False`.


{{Properties_Title|Part Design}}

-    **Refine|Bool**   * If `True` redundant edges are removed from the result of the operation. The default value is determined by the **Automatically refine model after sketch-based operation** preference. See [PartDesign Preferences](PartDesign_Preferences#General.md).

## Problèmes connus 

Voir [PartDesign Congé](PartDesign_Fillet/fr#Probl.C3.A8mes_connus.md).





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Chamfer/fr
