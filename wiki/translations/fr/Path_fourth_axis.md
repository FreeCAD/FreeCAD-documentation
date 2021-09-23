# Path fourth axis/fr
{{TOCright}}

## Description

Ces fonctionnalités expérimentales permettent le fraisage de quatre axes [faces](https://forum.freecadweb.org/viewtopic.php?f=15&t=36773) et [35867 poches](https://forum.freecadweb.org/viewtopic.php?f=15&t=)

Ces fonctionnalités sont en cours de développement. Des bogues peuvent exister. Merci pour vos commentaires et tests.

## Installation

Idéalement, passez à la version 0.19.16502 ou supérieure.

Téléchargez ces scripts:

-   PathProfileFaces.py [disponible ici](https://forum.freecadweb.org/viewtopic.php?f=15&t=36773) et
-   PathAreaOp.py [ici](https://forum.freecadweb.org/viewtopic.php?f=15&t=35867)
-   PathPocketShape.py from [ici aussi](https://forum.freecadweb.org/viewtopic.php?f=15&t=35867) (pour des opérations de poches)

Placez-les dans votre répertoire FreeCAD/Mod/Path/PathScripts, \* après \* renommer vos originaux pour les conserver en toute sécurité. Renommez les nouveaux scripts aux noms de script d\'origine. Redémarrez FreeCAD et amusez-vous.

À utiliser à vos risques et périls.

## Limitations

Les opérations actuelles du 4ème axe ne gèrent pas les rotations complexes/composées: celles impliquant X et Y simultanément.

Il n\'y a actuellement aucune intégration GUI des paramètres de rotation du 4ème axe dans la branche de publication. Tous les paramètres associés se trouvent dans l\'onglet Données de la section Affichage des propriétés pour chaque opération individuelle prise en charge.

## Utilisation

### Surfaces des profiles 

-   Sélectionnez la(les) surface(s) pour l\'opération comme d\'habitude
-   Cliquez sur l\'icône Path Profile Faces pour démarrer l\'opération
-   Modifiez vos paramètres comme vous le souhaitez
-   Cliquez sur OK pour exécuter l\'opération
-   Dans la liste des propriétés de la nouvelle opération, modifiez le paramètre \"Enable Rotation\" selon les besoins pour les faces
-   Recalculez l\'opération
-   Ajustez les profondeurs de début/fin selon les besoins. La profondeur finale est codée pour NE PAS dépasser la face sélectionnée utilisée pour le profil.

### Forme de la poche 

-   Cliquez sur l\'icône Path Pocket Shape pour démarrer l\'opération.
-   Cliquez sur OK pour créer l\'opération - aucune face sélectionnée
-   Sélectionnez la nouvelle opération Pocket\_Shape dans la fenêtre des tâches
-   Dans la liste Propriétés de l\'opération, faites défiler jusqu\'à la section Path et modifiez la propriété \"Enable Rotation\" sur le paramètre de 4ème axe souhaité.
-   Recalculez l\'opération
-   Double-cliquez sur la même opération, pour modifier les paramètres dans la fenêtre des tâches.
-   Ouvrez l\'onglet \'Base Geometry\'. Sélectionnez une face (préférée pour le moment) et cliquez sur le bouton \'Add\' en plaçant cette face dans la liste Géométrie de base.
-   Modifiez les autres paramètres de fonctionnement comme vous le souhaitez.
-   Cliquez sur OK pour enregistrer et appliquer les modifications.

## Dépannage

-   Il existe une propriété \"Inverse Angle\". Vous devrez peut-être basculer cette option pour obtenir des chemins corrects pour certains de vos visages.
-   Réglez \"Enable Rotation\" sur autre chose que \'Off\' pour profiler les faces perpendiculairement qui ne sont pas normales à l\'axe Z.
-   Basculez la propriété \"Reverse Direction\" si le chemin semble être désactivé de 180 degrés.





{{Path_Tools_navi

}}

---
[documentation index](../README.md) > [Path](Path_Workbench.md) > Path fourth axis/fr
