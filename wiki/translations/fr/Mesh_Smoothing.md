---
- GuiCommand:/fr
   Name:Mesh Smoothing
   Name/fr:Mesh Lissage
   MenuLocation:Maillages → Lisser...
   Workbenches:[Mesh](Mesh_Workbench/fr.md)
---

# Mesh Smoothing/fr

## Description

La commande **Mesh Lissage** lisse les objets maillés en modifiant la position de leurs sommets.

![](images/Meshes_Smooth.jpg ) 
*Le panneau des tâches de lissage après avoir choisi l'option de Seulement la sélection*

## Utilisation

1.  Si vous prévoyez de lisser uniquement certaines zones, notez que la commande utilise la couleur rouge pour marquer les faces sélectionnées pour cette option. Pour les voir correctement:
    -   Le {{PropertyView/fr|Display Mode}} des objets maillés devrait idéalement être {{Value|Flat lines}}, mais devrait au moins montrer des faces. Si nécessaire, utilisez la commande [Std Style de représentation](Std_DrawStyle/fr.md) pour remplacer cette propriété.
    -   La {{PropertyView/fr|Shape Color}} des objets maillés ne doit pas être rouge.
2.  Sélectionnez un ou plusieurs objets maillés.
3.  Il existe plusieurs façons d\'appeler la commande:
    -   Appuyez sur le bouton **<img src="images/Mesh_Smoothing.svg" width=16px> [Lisse les maillages sélectionnés](Mesh_Smoothing/fr.md)
**
    -   Sélectionnez l\'option **Maillages → <img src="images/Mesh_Smoothing.svg" width=16px> Lisser...** dans le menu.
4.  Le panneau des tâches **Smoothing** s\'ouvre.
5.  Si vous souhaitez uniquement lisser les zones sélectionnées: choisissez l\'option **Only selection**:
    -   Le panneau **Selection** est ajouté au panneau des tâches.
    -   Spécifiez les options de région:
        -   
            **Respect only visible triangles**
            

        -   
            **Respect only triangles with normals facing screen**
            
    -   Appuyez sur le bouton **Add** et tout en maintenant le bouton gauche de la souris enfoncé, dessinez une région, une spline fermée, dans la [vue 3D](3D_view/fr.md). Les faces qui correspondent aux options de région et tombent (partiellement) à l\'intérieur de la région seront sélectionnées.
    -   Si vous le souhaitez, appuyez sur le bouton **Clear** pour effacer la sélection.
6.  Sélectionnez le lissage **Method**:
    -   
        **Taubin**
        

    -   
        **Laplace**
        
7.  Spécifiez le **Parameters**:
    -   
        **Iterations**
        
        : plus ce nombre est élevé, plus le résultat final est lisse. La valeur a également un impact sur le temps de traitement total de la commande. Évitez les valeurs élevées si les objets maillés ont de nombreux points.

    -   
        **λ**
        
        : la valeur doit être comprise dans la plage {{Value|0}} - {{Value|1}}.

    -   
        **μ**
        
        : la valeur doit être comprise dans la plage {{Value|0}} - {{Value|1}}.
8.  Appuyez sur le bouton **OK** pour terminer la commande.





{{Mesh Tools navi

}}

---
[documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh Smoothing/fr
