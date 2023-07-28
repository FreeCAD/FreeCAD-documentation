---
- GuiCommand:/fr
   Name:Path Job
   Name/fr:Path Tâche
   MenuLocation:Path → Tâche
   Workbenches:[Path](Path_Workbench/fr.md)
   Shortcut:**P** **J**
   SeeAlso:[Path Post-traitement](Path_Post/fr.md), [Path Personnalisation du post-processeur](Path_Postprocessor_Customization/fr.md)
---

# Path Job/fr

## Description

L\'outil <img alt="" src=images/Path_Job.svg  style="width:16px;"> [Tâche](Path_Job/fr.md) crée un nouvel objet Tâche dans le document actif. L\'objet Tâche contient les informations suivantes :

1.  Une liste de définitions des paramètres des outils, spécifiant la géométrie, les paramètres de coupe et les vitesses pour les outils des opérations de Path.
2.  Une liste séquentielle d\'opérations de travail des opérations de Path.
3.  Un corps de base : un clone utilisé pour le décalage.
4.  Un brut représentant la matière première qui sera usinée dans l\'atelier Path.
5.  Une feuille de calcul, contenant les entrées utilisées par les opérations de Path, comprenant des valeurs statiques et des formules.
6.  Des paramètres de configuration spécifiant la trajectoire prévue de la tâche de sortie en G-code, le nom de fichier et l\'extension, ainsi que le [post-processeur](Path_Post/fr.md) (utilisé pour générer le langage approprié pour le contrôleur CNC cible et personnaliser les unités, les changements d\'outil, le stationnement, etc.).

## Usage

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Path_Job.svg" width=16px> [Tâche](Path_Job/fr.md)**.
    -   Sélectionnez l\'option **Path → <img src="images/Path_Job.svg" width=16px> Tâche** dans le menu.
    -   Utilisez le raccourci clavier : **P** puis **J**.

La boîte de dialogue GUI de la Tâche comporte cinq onglets alignés horizontalement : **Général**, **Sortie**, **Installation**, **Outils** et **Plan de travail**. L\'utilisateur peut à tout moment utiliser les options **OK** ou **Annuler** dans la boîte de dialogue.



## Général

![](images/Job_1.jpg )

-   **Étiquette** : l\'étiquette de la tâche affichée dans la vue en arborescence.
-   **Modèle** : l\'objet de base qui définit par sa forme les parcours d\'usinage. S\'il s\'agit d\'un objet Part Design, c\'est généralement le corps que vous sélectionnez ici. Si vous avez sélectionné un élément dans la vue en arborescence *avant* de cliquer sur l\'icône \"Ajouter une tâche\", cet élément est déjà saisi ici. Vous pouvez le modifier en sélectionnant un autre élément dans le menu déroulant.
-   **Description** : vous pouvez ajouter quelques notes à la tâche ici. Les notes sont seulement pour votre information et n\'ont aucun effet sur le parcours.



## Sortie

![](images/Job_2.jpg )

-   **Fichier de sortie** : définit le nom, l\'extension et le chemin du fichier de sortie G-code. Vous pouvez utiliser les espaces réservés suivants :
    -   **%D** répertoire du document actif
    -   **%d** nom du document actif (sans extension)
    -   **%M** répertoire de la macro de l\'utilisateur
    -   **%j** nom de la tâche

-   **Processeur** : sélectionne le [post-processeur](Path_Post/fr.md) pour votre machine.
-   **Arguments** : ajoute des arguments pour le [post-processeur](Path_Post/fr.md) si nécessaire.



## Installation

![](images/Job_3.jpg )

-   **Brut** : définit la taille et la forme de la matière première.
-   **Orientation**: le bord ou la face sélectionné est utilisé pour orienter la base ou le brut en conséquence.
-   **Alignement** : sélectionne un sommet pour définir l\'origine ou déplacer une base ou un brut



## Outils

![](images/Job_4.jpg )

Ajoutez le(s) outil(s) de votre [Gestionnaire d\'outils](Path_ToolLibraryEdit/fr.md) dont vous avez besoin pour les opérations de ce travail.

Après avoir ajouté un outil, vous pouvez définir/modifier l\'avance et la vitesse de broche si vous avez besoin d\'une vitesse d\'avance différente dans cette tâche. Une modification ici ne modifie pas les paramètres stockés dans le gestionnaire d\'outils.

L\'outil par défaut que vous pouvez supprimer si vous avez ajouté un outil personnel.



## Plan de travail 

![](images/Job_5.jpg )

Si vous avez une tâche qui implique plus d\'une opération d\'usinage, vous pouvez déterminer dans quel ordre les opérations doivent être effectuées. Pour réorganiser, sélectionnez une opération et appuyez sur le bouton haut ou bas.





{{Path_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Job/fr
