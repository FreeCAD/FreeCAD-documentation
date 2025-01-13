---
 GuiCommand:
   Name: CAM Adaptive
   Name/fr: CAM Adaptatif
   MenuLocation: CAM , Détourer/contourner de manière adaptative
   Workbenches: CAM_Workbench/fr
---

# CAM Adaptive/fr

## Description

L\'algorithme de l\'opération <img alt="" src=images/CAM_Adaptive.svg  style="width:24px;"> [Adaptatif](CAM_Adaptive/fr.md) crée des parcours de détourage et de contournage. L\'opération fait varier l\'engagement de la fraise de manière à ce que l\'enlèvement de matière ne dépasse jamais une valeur maximale.



## Utilisation

Les instructions d\'utilisation pour l\'opération [Adaptatif](CAM_Adaptive/fr.md) sont présentés ici.



### Opération de base 

1.  Appuyez sur l\'icône **<img src="images/CAM_Adaptive.svg" width=16px> [Détourer/contourner de manière adaptative](CAM_Adaptive/fr.md)** ou faites **CAM** → **<img src="images/CAM_Adaptive.svg" width=24px> [Détourer/contourner de manière adaptative](CAM_Adaptive/fr.md)** à partir du menu.
2.  Sélectionnez le contrôleur d\'outil pour l\'opération dans la fenêtre contextuelle du contrôleur d\'outil, si vous y êtes invité.
3.  Ajustez les profondeurs d\'opération selon vos besoins dans l\'onglet Profondeurs : Profondeur de départ, Profondeur de fin, Pas de descente.
4.  Faites les ajustements nécessaires dans l'onglet Hauteurs.
5.  Configurez les paramètres dans l\'onglet Opérations :
    1.  (**Voir la section ci-dessous [Propriétés](#Propriétés.md) → Adaptive.**)
    2.  Définissez la valeur de dépassement en tant que pourcentage du diamètre de l\'outil.
6.  Si vous souhaitez prévisualiser le résultat avant d\'accepter les paramètres, cliquez sur **Appliquer**.
7.  Cliquez sur le bouton **OK** pour confirmer et générer les trajectoires.



### Remarques préliminaires sur le détourage adaptatif 

-   En fonction de la taille et de la complexité de la zone pour l\'opération, il peut être préférable de ne pas recalculer l\'opération après chaque changement de propriété. Considérez plutôt :
    -   Désactivez l\'opération avec l\'outil **<img src="images/CAM_OpActiveToggle.svg" width=16px> [Activer une opération](CAM_OpActiveToggle/fr.md)**, apportez vos modifications aux propriétés de l\'opération puis cliquez sur le **<img src="images/CAM_OpActiveToggle.svg" width=16px> [Activer une opération](CAM_OpActiveToggle/fr.md)** à nouveau pour réactiver l\'opération, ce qui déclenche un recalcul en interne.
-   L\'opération **<img src="images/CAM_Adaptive.svg" width=16px> [Activer une opération](CAM_Adaptive/fr.md)** peut contenir encore quelques bogues. Veuillez signaler les bogues et les problèmes sur le [FreeCAD CAM/CAM Forum](https://forum.freecadweb.org/viewforum.php?f=15).
-   Toutes les formes d\'outils peuvent ne pas être respectées avec cette opération. Consultez le forum FreeCAD pour plus de détails.
-   Si vous choisissez d\'exécuter le simulateur de parcours dans l\'atelier CAM, il utilise uniquement la fraise de bout standard pour simuler des parcours. Par conséquent, vous ne verrez pas l'enlèvement de matière spécifique à une forme d'outil. L\'enlèvement de matière est illustré à l\'aide de la forme de la fraise.



## Propriétés

***Remarque***: les noms de certaines propriétés de cette liste diffèrent un peu des mêmes paramètres que ceux utilisés dans l\'éditeur de fenêtre de tâche.


{{TitleProperty|Adaptive}}

-    **Force Inside-Out**: force la pénétration dans le matériau à l\'intérieur et le détourage vers les bords.

-    **Helix Angle**: angle d\'entrée de la rampe hélicoïdale (degrés).

-    **Helix Cone Angle**: angle du cone hélicoïdal (degrés).

-    **Helix Diameter Limit**: limite le diamètre d\'entrée de l\'hélicoïde, si la limite est supérieure au diamètre de l\'outil ou à 0, le diamètre de l\'outil est utilisé.

-    **Keep Tool Down Ratio**: longueur maximale de la descente de l\'outil par rapport à la distance directe entre les points.

-    **Lift Distance**: distance de levage pour les mouvements rapides.

-    **Operation Type**: type d\'opération adaptative : détourage ou contournage.

-    **Side**: côté des faces sélectionnées que l\'outil doit couper : intérieur ou extérieur.

-    **Step Over**: pourcentage du diamètre de la fraise à effectuer à chaque passage.

-    **Stock to Leave**: quantité de matière à laisser (c\'est-à-dire pour une opération de finition séparée).

-    **Tolerance**: influence la précision et les performances.

-    **Use Helix Arcs**: utilise les arcs (G2) pour la rampe hélicoïdale.


{{TitleProperty|Base}}

Remarque : il est conseillé de ne pas modifier la propriété Placement des opérations de parcours. Il convient plutôt de déplacer ou de faire pivoter le modèle CAM Tâche selon les besoins.

-    **Placement**: emplacement global \[position et rotation\] de l\'objet, par rapport à l\'origine (ou à l\'origine du conteneur de l\'objet parent).

    -   
        **Angle**
        
        : angle en degrés appliqué à la rotation de l\'objet autour de la valeur de la propriété Axis.

    -   
        **Axis**
        
        : axe (un ou plusieurs) autour duquel faire pivoter l\'objet, défini dans les sous-propriétés : X, Y, Z.

        -   
            **X**
            
            : valeur de l\'axe X.

        -   
            **Y**
            
            : valeur de l\'axe Y.

        -   
            **Z**
            
            : valeur de l\'axe Z.

    -   
        **Position**
        
        : position de l\'objet, définie dans les sous-propriétés : X, Y, Z - par rapport à l\'origine (ou à l\'origine du conteneur de l\'objet parent).

        -   
            **X**
            
            : valeur de distance X.

        -   
            **Y**
            
            : valeur de distance Y.

        -   
            **Z**
            
            : valeur de distance Z.

-    **Label**: nom de l\'objet fourni par l\'utilisateur (UTF-8).


{{TitleProperty|Depth}}

-    **Clearance Height**: hauteur nécessaire pour éviter les brides et autres obstacles.

-    **Final Depth**: profondeur finale de l\'outil, valeur la plus basse en Z.

-    **Finish Depth**: maximum de matériau a retirer lors de la passe final.

-    **Safe Height**: seuil supérieur à partir duquel les mouvements rapides sont autorisés.

-    **Start Depth**: profondeur initiale de l\'outil, première profondeur de coupe en Z.

-    **Step Down**: pas de descente incrémentale de l\'outil.


{{TitleProperty|Path}}

-    **Active**: mis à False, pour empêcher l\'opération de générer du code.

-    **Comment**: commentaire facultatif pour cette opération.

-    **Tool Controller**: définit le contrôleur d\'outil utilisé dans l\'opération.

-    **User Label**: étiquette attribuée par l\'utilisateur.



## Disposition de l\'éditeur de la fenêtre des tâches 

*Les descriptions des paramètres sont fournies dans la liste des propriétés ci-dessus.*

Cette section est simplement une représentation des paramètres de l'éditeur de fenêtres pour l'opération.



### Géométrie de base 

-   **Ajouter** : ajoute le(s) élément(s) sélectionné(s) qui doit(vent) être la(les) base(s) pour le(s) parcours.
-   **Enlever** : supprime le ou les éléments sélectionnés dans la liste de la géométrie de base.
-   **Réinitialiser** : efface tous les éléments de la liste de la géométrie de base.



### Profondeurs

-    **Start Depth**
    

-    **Final Depth**
    

-    **Finish Depth**
    

-    **Step Down**
    



### Hauteurs

-    **Safe Height**
    

-    **Clearance Height**
    



### Opération

-    **Tool Controller**
    

-    **Cut Region**(Côté)

-    **Operation Type**
    

-    **Step Over Percent**
    

-    **Accuracy vs Performance**(Tolérance)

-    **Helix Ramp Angle**
    

-    **Helix Cone Angle**
    

-    **Helix Max Diameter**(Limite du diamètre de l\'hélice)

-    **Lift Distance**
    

-    **Keep Tool Down Ratio**
    

-    **Stock to Leave**
    

-    **Force Clearing Inside-Out**
    

-    **Stop**
    



## Problèmes connus 

Si CAM Adaptatif crée des parcours indésirables, essayez avec **Stock to Leave** réglée à {{Value|0.001 mm}} ou plus. Vous pouvez réduire le diamètre de l\'outil en doublant cette valeur pour conserver des parcours exactes.

Une proposition de correction de bogue est disponible (mais personne ne travaille à son intégration) :

<https://github.com/FreeCAD/FreeCAD/pull/5276>



## Ressources

-   Page GitHub de l\'auteur pour le projet d\'origine : [kreso-t/FreeCAD_Mod_Adaptive_Path](https://github.com/kreso-t/FreeCAD_Mod_Adaptive_Path).
-   Sujet actif dans les forums FreeCAD pour l\'opération Adaptive de parcours : [Adaptive Path/CAM Operation](https://forum.freecadweb.org/viewtopic.php?f=15&t=30127).





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM Adaptive/fr
