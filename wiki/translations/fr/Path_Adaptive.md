---
- GuiCommand:/fr
   Name:Path Adaptive
   Name/fr:Path Adaptation
   MenuLocation:Path → Adaptive
   Workbenches:[Path](Path_Workbench/fr.md)
   Shortcut:
   SeeAlso:
---


</div>

## Description

L\'outil <img alt="" src=images/Path_Adaptive.svg  style="width:24px;"> [Path Adaptation](Path_Adaptive/fr.md) utilise un algorithme adaptatif pour créer des chemins de compensation et de profilage qui gèrent l\'engagement des outils de coupe de manière à ce que l\'engagement et l\'enlèvement de matière ne dépassent jamais une valeur maximale.

## Utilisation

Les instructions d\'utilisation pour l\'opération [Adaptation](Path_Adaptive/fr.md) sont présentés ici.

#### Opération de base {#opération_de_base}

1.  Appuyez sur l\'icône **<img src="images/Path_Adaptive.svg" width=16px> [Adaptive](Path_Adaptive/fr.md)** ou sélectionnez l\'outil **Path** → **<img src="images/Path_Adaptive.svg" width=24px> [Adaptive](Path_Adaptive/fr.md)** à partir du menu **Path**.
2.  Sélectionnez le contrôleur d\'outil pour l\'opération dans la fenêtre contextuelle du contrôleur d\'outil, si vous y êtes invité.
3.  Ajustez les profondeurs d\'opération selon vos besoins dans l\'onglet Profondeurs: Début Profondeur, Fin Profondeur, Pas (respectivement Start Depth, Finish Depth, Step Down).
4.  Faites les ajustements nécessaires dans l'onglet Heights.
5.  Configurez les paramètres dans l\'onglet Opérations:
    1.  (**Voir la section Propriétés -\> Adaptative ci-dessous.**)
    2.  Définissez la valeur de dépassement en tant que pourcentage du diamètre de l\'outil.
6.  Si vous souhaitez prévisualiser le résultat avant d\'accepter les paramètres, cliquez sur **Apply**.
7.  Cliquez sur le bouton **OK** pour confirmer et générer les chemins.

##### Remarques préliminaires sur la compensation adaptative {#remarques_préliminaires_sur_la_compensation_adaptative}

-   En fonction de la taille et de la complexité de la zone pour l\'opération, il peut être préférable de ne pas recalculer l\'opération après chaque changement de propriété; considérez plutôt:
    -   Désactivez l\'opération avec l\'outil **<img src="images/Path_OpActiveToggle.svg" width=16px> [Activation de l'opération](Path_OpActiveToggle/fr.md)**, apportez vos modifications aux propriétés de l\'opération puis cliquez sur le **<img src="images/Path_OpActiveToggle.svg" width=16px> [Activation de l'opération](Path_OpActiveToggle/fr.md)** à nouveau pour réactiver l\'opération, ce qui déclenche un recalcul en interne.
-   L\'opération **<img src="images/Path_Adaptive.svg" width=16px> [Activation de l'opération](Path_Adaptive/fr.md)** peut contenir quelques bogues non encore clairement identifiés. Veuillez signaler les bogues et les problèmes sur le [FreeCAD Path/CAM Forum](https://forum.freecadweb.org/viewforum.php?f=15).
-   Toutes les formes d\'outils peuvent ne pas être respectées avec cette opération. Consultez le forum FreeCAD pour plus de détails.
-   Si vous choisissez d\'exécuter le simulateur de trajectoire dans l\'atelier Path, il utilise uniquement la fraise de bout standard pour simuler des trajectoires. Par conséquent, vous ne verrez pas l'enlèvement de matière spécifique à une forme d'outil. L\'enlèvement de matière est illustré à l\'aide de la forme de la fraise.

## Propriétés

\'\'\' *Remarque* \'\'\': les noms de certaines propriétés de cette liste diffèrent un peu des mêmes paramètres que ceux utilisés dans l\'éditeur de fenêtre de tâche.

#### Adaptive

-    {{PropertyData/fr|Force Inside-Out}}: force la pénétration dans le matériau à l\'intérieur et le nettoyage vers les bords.

-    {{PropertyData/fr|Helix Angle}}: angle d\'entrée de la rampe d\'hélice (degrés).

-    {{PropertyData/fr|Helix Cone Angle}}: Angle de l\'hélice conique (degrés).

-    {{PropertyData/fr|Helix Diameter Limit}}: limite le diamètre d\'entrée de l\'hélice, si la limite est supérieure au diamètre de l\'outil ou à 0, le diamètre de l\'outil est utilisé.

-    {{PropertyData/fr|Keep Tool Down Ratio}}: longueur maximale de l\'outil en bas par rapport à la distance directe entre les points.

-    {{PropertyData/fr|Lift Distance}}: distance de levage pour mouvements rapides.

-    {{PropertyData/fr|Operation Type}}: type d\'opération adaptative: éffacement ou profilage.

-    {{PropertyData/fr|Side}}: côté des faces sélectionnées que l\'outil doit couper: intérieur ou extérieur.

-    {{PropertyData/fr|Step Over}}: pourcentage du diamètre de la fraise à éffectuer à chaque passage.

-    {{PropertyData/fr|Stock to Leave}}: quantité de matière à laisser (c\'est-à-dire pour une opération de finition séparée).

-    {{PropertyData/fr|Tolerance}}: influence la précision et les performances.

-    {{PropertyData/fr|Use Helix Arcs}}: utilise les arcs (G2) pour la rampe hélicoïdale.

#### Base

Remarque: il est conseillé de ne pas modifier la propriété Placement des opérations de chemin. Déplacez ou faites pivoter le modèle de tâche de chemin selon vos besoins.

-    {{PropertyData/fr|Placement}}: emplacement global \[position et rotation\] de l\'objet - par rapport à l\'origine (ou à l\'origine du conteneur de l\'objet parent).

    -   
        {{PropertyData/fr|Angle}}
        
        : angle en degrés appliqué à la rotation de l\'objet autour de la valeur de la propriété Axis.

    -   
        {{PropertyData/fr|Axis}}
        
        : axe (un ou plusieurs) autour duquel faire pivoter l\'objet, défini dans les sous-propriétés: x, y, z.

        -   
            {{PropertyData/fr|X}}
            
            : valeur de l\'axe x.

        -   
            {{PropertyData/fr|Y}}
            
            : valeur de l\'axe y.

        -   
            {{PropertyData/fr|Z}}
            
            : valeur de l\'axe z.

    -   
        {{PropertyData/fr|Position}}
        
        : position de l\'objet, définie dans les sous-propriétés: x, y, z - par rapport à l\'origine (ou à l\'origine du conteneur de l\'objet parent).

        -   
            {{PropertyData/fr|X}}
            
            : valeur de distance x.

        -   
            {{PropertyData/fr|Y}}
            
            : valeur de distance y.

        -   
            {{PropertyData/fr|Z}}
            
            : valeur de distance z.

-    {{PropertyData/fr|Label}}: nom de l\'objet fourni par l\'utilisateur (UTF-8).

#### Profondeur

-    {{PropertyData/fr|Clearance Height}}: hauteur nécessaire pour supprimer les pinces et les obstructions.

-    {{PropertyData/fr|Final Depth}}: profondeur finale de l\'outil - valeur la plus basse de Z.

-    {{PropertyData/fr|Finish Depth}}: maximum de matériau retiré lors du passage final.

-    {{PropertyData/fr|Safe Height}}: seuil supérieur duquel les mouvements rapides sont autorisés.

-    {{PropertyData/fr|Start Depth}}: profondeur initiale de l\'outil - première profondeur de coupe en Z.

-    {{PropertyData/fr|Step Down}}: abaissement incrémentiel de l\'outil.

#### Tracé

-    **Active**: make False, to prevent operation from generating code

-    **Comment**: An optional comment for this Operation

-    **Tool Controller**: Defines the Tool controller used in the Operation

-    **User Label**: User assigned label


<div class="mw-translate-fuzzy">

-    {{PropertyData/fr|Active}}: rend False, pour empêcher l\'opération de générer du code

-    {{PropertyData/fr|Comment}}: commentaire facultatif pour cette opération.

-    {{PropertyData/fr|Tool Controller}}: définit le contrôleur d\'outil utilisé dans l\'opération.

-    {{PropertyData/fr|User Label}}: étiquette attribuée par l\'utilisateur


</div>

*Les descriptions de ces paramètres sont fournies dans la liste des propriétés ci-dessus.* Cette section est simplement une représentation des paramètres de l'éditeur de fenêtres pour l'opération.

#### Géométrie de base {#géométrie_de_base}

-   **Add**: ajoute les éléments sélectionnés qui doivent être la base du ou des chemins.
-   **Remove**: supprime le ou les éléments sélectionnés dans la liste emplacement de base.
-   **Edit**: efface tous les éléments de la liste d\'emplacement de base.

#### Profondeur {#profondeur_1}

-    {{PropertyData/fr|Start Depth}}
    

-    {{PropertyData/fr|Final Depth}}
    

-    {{PropertyData/fr|Finish Depth}}
    

-    {{PropertyData/fr|Step Down}}
    

#### Hauteur

-    {{PropertyData/fr|Safe Height}}
    

-    {{PropertyData/fr|Clearance Height}}
    

#### Opération

-    {{PropertyData/fr|Tool Controller}}
    

-    {{PropertyData/fr|Cut Region}}(Side)

-    {{PropertyData/fr|Operation Type}}
    

-    {{PropertyData/fr|Step Over Percent}}
    

-    {{PropertyData/fr|Accuracy vs Performance}}(Tolerance)

-    {{PropertyData/fr|Helix Ramp Angle}}
    

-    {{PropertyData/fr|Helix Cone Angle}}
    

-    {{PropertyData/fr|Helix Max Diameter}}(Helix Diameter Limit)

-    {{PropertyData/fr|Lift Distance}}
    

-    {{PropertyData/fr|Keep Tool Down Ratio}}
    

-    {{PropertyData/fr|Stock to Leave}}
    

-    {{PropertyData/fr|Force Clearing Inside-Out}}
    

-    {{PropertyData/fr|Stop}}
    

## Ressources

-   Page GitHub de l\'auteur pour le projet d\'origine: [kreso-t/FreeCAD\_Mod\_Adaptive\_Path](https://github.com/kreso-t/FreeCAD_Mod_Adaptive_Path).
-   Sujet actif dans les forums FreeCAD pour l\'opération Adaptive de chemin: [Adaptive Path/CAM Operation](https://forum.freecadweb.org/viewtopic.php?f=15&t=30127).


<div class="mw-translate-fuzzy">





</div>


{{Path_Tools_navi

}} 
