# Flatpak/fr
## Installation



### Version stable 

Si vous voulez installer au niveau de l\'utilisateur ou si vous n\'avez pas les privilèges sudo, ajoutez le drapeau `--user` aux commandes suivantes.


{{code|lang=bash|code=
# add flathub repo just to be sure as it might not be enabled if it is your first time using flatpak
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
flatpak install flathub org.freecad.FreeCAD
}}



### Versions en cours de développement 

Si vous voulez installer au niveau de l\'utilisateur ou si vous n\'avez pas les privilèges sudo, ajoutez le drapeau `--user` aux commandes suivantes.


{{code|lang=bash|code=
# flathub-beta repo is not enabled by default
flatpak remote-add --if-not-exists flathub-beta https://flathub.org/beta-repo/flathub-beta.flatpakrepo
flatpak install flathub-beta org.freecad.FreeCAD
}}



## Lancement

Vous pouvez démarrer le flatpak en utilisant le fichier du bureau ou en utilisant la commande suivante :


{{code|lang=bash|code=
flatpak run org.freecad.FreeCAD
}}

Les différentes branches peuvent être installées en parallèle. Pour choisir laquelle exécuter, utilisez le drapeau `--branch` :


{{code|lang=bash|code=
flatpak run --branch=beta org.freecad.FreeCAD
}}

Pour exécuter un exécutable spécifique (par exemple `FreeCADCmd` pour l\'exécuter sans interface graphique) à partir du flatpak, utilisez l\'indicateur `--command` :


{{code|lang=bash|code=
flatpak run --command=FreeCADCmd org.freecad.FreeCAD
}}



## Dépôt

-   <https://github.com/flathub/org.freecad.FreeCAD>



### Mainteneur(s)

-   [adrianinsaval](https://github.com/adrianinsaval)
-   [hfiguiere](https://github.com/hfiguiere)



## En relation 

-   Paquets [AppImage](AppImage/fr.md)
-   Paquets [Snap](Snap/fr.md)



---
⏵ [documentation index](../README.md) > [Packaging](Category_Packaging.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Testing](Category_Testing.md) > Flatpak/fr
