# OSE Piping Workbench/fr
## Introduction


{{TOCright}}

L\'atelier OSE Piping crée des tuyaux et des raccords. Il fait partie de [Open Source Ecology](https://www.opensourceecology.org/) et [Open Source Ecology Germany](https://www.ose-germany.de/). Pour utiliser toutes ses fonctionnalités, installez l\'atelier Dodo.

![ 512px](images/OSE_Piping_workbench_screenshot.png )

# Personnalisation

OSE Piping stocke les dimensions dans des fichiers CSV dans le répertoire *table* du répertoire de l\'atelier. Modifiez ces fichiers CSV si vous souhaitez en ajouter ou modifier les dimensions du raccord.

# Tuyau

Un tuyau est décrit par son diamètre extérieur *OD*, son épaisseur de paroi *Thk* et sa hauteur *H*.

Pour créer un tuyau, cliquez sur ![](images/OSE_Piping_create_pipe_icon.svg ) dans l\'atelier OSE Piping. Sélectionnez les dimensions de la tuyauterie et cliquez sur \"OK\".

![ 512px](images/OSE_Pining_create_pipe_screenshot.png )

Pour ajouter de nouvelles dimensions, ajustez le fichier CSV **pipe.csv**.

Wikipédia sur la taille nominale des tuyaux (NPS) [1](https://en.wikipedia.org/wiki/Nominal_Pipe_Size).

# Coude

Un coude est décrit par un angle alpha, le diamètre extérieur du tuyau **POD**, le diamètre intérieur du tuyau **PID**, **H**, **J** et **M**.

Pour créer un coude, cliquez sur ![](images/OSE_Piping_create_elbow_icon.svg ).

<img alt="" src=images/OSE_Piping_create_elbow_screenshot.png  style="width:512px;"> ![](images/OSE_Piping_elbow_CAD_screenshot.png )  Pour ajouter de nouveaux coudes, ajustez le fichier **elbow.csv**.

# Coude de balayage 

Un sweep elbow est un coude spécial dont le rayon de courbure est plus grand. Il est décrit par le diamètre extérieur du tube POD, l\'épaisseur du tube **PThk**, **G**, **H** et **M**. Pour créer un coude de balayage, cliquez sur ![](images/OSE_Piping_create_sweep_elbow_icon.svg ).

<img alt="" src=images/OSE_Piping_create_sweep_elbow_screenshot.png  style="width:512px;"> ![](images/OSE_Piping_sweep_elbow_CAD_screenshot.png )  Pour ajouter de nouveaux coudes, ajustez le fichier **sweep-elbow.csv**.



[<img src="images/Property.png" style="width:16px"> User Documentation](Category_User_Documentation.md) [<img src="images/Property.png" style="width:16px"> Addons](Category_Addons.md) [<img src="images/Property.png" style="width:16px"> External Workbenches](Category_External_Workbenches.md)

---
[documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > OSE Piping Workbench/fr
