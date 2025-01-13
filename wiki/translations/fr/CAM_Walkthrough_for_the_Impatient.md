---
 TutorialInfo:r
   Topic: Atelier CAM
   Level: Débutant/modéré
   Time: 15 minutes
   Author: Chrisb
   FCVersion: 0.19
---

# CAM Walkthrough for the Impatient/fr







## Objectif

Démonstration de la création d\'une tâche de l\'<img alt="" src=images/Workbench_CAM.svg  style="width:32px;"> [atelier CAM](CAM_Workbench/fr.md) dérivé d\'un modèle 3D, puis création du G-Code pour dialoguer avec une fraiseuse CNC cible.



## Le modèle 3D 

1\. Le projet commence par un simple modèle FreeCAD conçu dans <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> [PartDesign](PartDesign_Workbench/fr.md), un cube avec une poche rectangulaire,

:   ![](images/Path-SquarePocketModel.png )



*Au dessus: créé dans l'<img src="images/Workbench_PartDesign.svg" width=24px> [atelier PartDesign](PartDesign_Workbench/fr.md) incluant un Corps, une boîte avec une cavité, basée sur une esquisse orientée dans le 
**![](images/)*_plan_XY.**

2\. Une fois le modèle 3D terminé, passez à l\'<img alt="" src=images/Workbench_CAM.svg  style="width:32px;"> [atelier CAM](CAM_Workbench/fr.md) via le [sélecteur d\'atelier](Std_Workbench/fr.md) (menu déroulant)



## La tâche 

3\. Maintenant, nous créons une [CAM Tâche](CAM_Job/fr.md) par l\'une des méthodes suivantes :

-   Appuyez sur le bouton **![](images/)_[Tâche](CAM_Job/fr.md)** dans la barre d\'outils.
-   Utilisation du raccourci clavier **P** puis **J**.
-   En utilisant l\'entrée **CAM → Tâche** du menu supérieur.

![](images/Path-JobCreationDialog.png )

:   

    :   
        
*Ci-dessus: la fenêtre de dialogue de création de [CAM Tâche](CAM_Job/fr.md)*
        

4\. Cela ouvre une fenêtre de dialogue de création de tâche. Dans cette fenêtre de dialogue, cliquez sur **OK** pour accepter le corps comme modèle de base, sans modèle.



### Configuration de la tâche 

5\. La fenêtre de dialogue de la tâche s\'ouvre dans la fenêtre Tâche et la fenêtre de vue du modèle affiche le brut sous la forme de cube en filaire entourant le corps de base. L\'onglet Configuration est sélectionné.



### Sortie de la tâche 

6\. L\'onglet Sortie définit le chemin du fichier de sortie, le nom, l\'extension et le postprocesseur. Pour les utilisateurs avancés, les arguments du post-processeur peuvent être personnalisés (passez la souris pour afficher les info-bulles des arguments courants).

:   ![](images/Path-JobOutput.png )

:   
    
*Ci-dessus : la fenêtre de dialogue Modifier de [CAM Tâche](CAM_Job/fr.md) avec l'onglet Sortie sélectionné*
    



### Outils

:   ![](images/Path-JobTools.png )

:   
    
*Ci-dessus : la fenêtre de dialogue Modifier de [CAM Tâche](CAM_Job/fr.md) avec l'onglet Outils sélectionné*
    

7\. Modifier l\'outil Par défaut en le sélectionnant et en cliquant sur le bouton **Edit**. Cela ouvre la fenêtre d\'édition du contrôleur d\'outil.

:   ![](images/Path-ToolConfig.gif )

:   
    
*Ci-dessus : la fenêtre de dialogue d'édition de [CAM Tâche](CAM_Job/fr.md) du sous-panneau du contrôleur d'outil*
    

8\. Le nom donné à l\'outil et le numéro d\'outil correspondent au numéro d\'outil de la machine. Dans la fenêtre de dialogue (voir ci-dessus), c\'est Tool Nr. 4. Le contrôleur d\'outil est configuré pour des vitesses d\'avance horizontale et verticale de `2mm/s` et une vitesse de fraise de `2000 rpm`.

9\. Sélectionnez le sous-panneau Tool du contrôleur d\'outil. Définissez le diamètre (et si vous souhaitez utiliser l\'outil <img alt="" src=images/CAM_Simulator.svg  style="width:24px;"> [CAM Simulateur de parcours](CAM_Simulator/fr.md) plus tard : ajoutez un angle de tranchant et une hauteur de tranchant).

:   ![](images/Path-ToolAdd.gif )

:   
    
*Ci-dessus : la fenêtre de dialogue de [CAM Tâche](CAM_Job/fr.md) du sous-panneau "Outil" du contrôleur d'outil*
    

10\. Les valeurs seront confirmées avec **OK**.

Remarque : pour un accès facile, tous les outils peuvent être prédéfinis et sélectionnés dans le <img alt="" src=images/CAM_ToolLibraryEdit.svg  style="width:24px;">[Gestionnaire d\'outils](CAM_ToolLibraryEdit/fr.md).



### Plan de travail 

L\'onglet Plan de travail est initialement affiché comme vide. Il est ensuite rempli par la séquence des opérations de tâche, des commandes particulières et des finitions de CAM. L\'ordre de ces éléments est ordonné ici.

Cette arborescence apparaît après la configuration de la tâche une fois celui-ci déplié :

:   ![](images/Path-TreeWithJob.png )



## Les opérations d\'usinage 

11\. Deux opérations seront ajoutées pour générer des parcours de fraisage pour cette tâche. L\'opération [Profilage](CAM_Profile/fr.md) crée un parcours d\'usinage autour de la boîte et l\'opération [Poche](CAM_Pocket_Shape/fr.md) crée un parcours pour la poche intérieure.

12\. Pour l\'instant, nous allons garder les choses simples. Le bouton <img alt="" src=images/CAM_Profile.svg  style="width:32px;"> [Profilage](CAM_Profile/fr.md) ouvre le panneau Profilage. Après avoir confirmé avec **OK** en utilisant les valeurs par défaut, le parcours d\'usinage autour de l\'objet est visible en vert.

13\. Sélectionner le bas de la poche puis le bouton <img alt="" src=images/CAM_Pocket_Shape.svg  style="width:32px;"> [Poche](CAM_Pocket_Shape/fr.md) ouvre la fenêtre Forme de la poche. Les valeurs par défaut de la géométrie de base, des profondeurs et des hauteurs sont utilisées, le sous-panneau Opération est sélectionné et le pourcentage de dépassement est défini sur 50.

:   ![](images/Path-PocketOperation.gif )

:   
    
*Ci-dessus: la fenêtre de dialogue Forme de poche avec le sous-panneau Operation sélectionné*
    

14\. Le motif est changé en \"Offset\" et l\'opération de tâche est confirmée pour la configuration de la poche avec **OK**.

Le résultat est un modèle avec deux parcours d\'usinage:

:   ![](images/Path-WalkThroughResult.gif )

:   
    
*Ci-dessus: le résultat avec un modèle à deux trajectoires*
    



## Vérification des parcours d\'usinage 

Il existe deux manières de vérifier les parcours d\'usinage créés. Le G-code peut être inspecté, notamment en mettant en évidence les segments de parcours d\'usinage correspondants. Le processus de fraisage de la tâche d\'usinage peut également être simulé pour illustrer les parcours d'outil optimisés, nécessaires aux géométries d'outil pour fraiser le brut.

Pour inspecter le G-code, utilisez l\'outil <img alt="" src=images/CAM_Inspect.svg  style="width:32px;"> [CAM Inspecter des commandes](CAM_Inspect/fr.md). La sélection des lignes de G-code correspondantes dans la fenêtre Inspection du G-code met en surbrillance des segments de parcours d\'usinage individuels.

:   ![](images/Path-InspectWindow.gif )

:   
    
*Ci-dessus: L'outil [CAM Inspecter des commandes](CAM_Inspect/fr.md) ouvre la fenêtre de dialogue Inspection G-Code*
    

Démarrer la simulation en utilisant l\'outil <img alt="" src=images/CAM_Simulator.svg  style="width:32px;"> [CAM Simulateur de parcours](CAM_Simulator/fr.md) .

Réglez la vitesse et la précision et lancez la simulation avec le bouton de lecture <img alt="" src=images/CAM_BPlay.svg  style="width:24px;">.

:   ![](images/Path-Simulation.gif )

:   
    
*Ci-dessus : [Simulateur de parcours](CAM_Simulator/fr.md) en cours*
    

Si vous souhaitez mettre fin à la simulation, cliquez sur le bouton **Annuler** pour supprimer le brut créé pour la simulation. Si vous cliquez sur **OK**, cet objet sera conservé dans votre travail.



## Post-traiter la tâche 

La dernière étape pour générer le G-code pour la fraiseuse cible consiste à post-traiter la tâche. Cela envoie les G-codes dans un fichier pouvant être chargé sur le contrôleur de machine CNC cible. Pour appeler le post-processeur:

-   Sélectionnez l\'objet Tâche dans la [vue en arborescence](Tree_view/fr.md)
-   Sélectionnez l\'outil <img alt="" src=images/CAM_Post.svg  style="width:32px;"> [CAM Post-traitement](CAM_Post/fr.md) pour post-traiter le fichier. Cela ouvre une fenêtre de G-code permettant d\'inspecter le fichier de sortie final avant son enregistrement.

:   ![](images/Path-PostOutput.gif )

:   
    
*Ci-dessus: la fenêtre G-Code permettant l'inspection du fichier de sortie final*
    


{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM Walkthrough for the Impatient/fr
