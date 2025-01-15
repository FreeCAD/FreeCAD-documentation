# Flatpak/de
## Installing

### Stable

If you want to install at the user level or don\'t have sudo privileges add the `--user` flag to the following commands.


{{code|lang=bash|code=
# add flathub repo just to be sure as it might not be enabled if it is your first time using flatpak
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
flatpak install flathub org.freecad.FreeCAD
}}

### Development versions 

If you want to install at the user level or don\'t have sudo privileges add the `--user` flag to the following commands.


{{code|lang=bash|code=
# flathub-beta repo is not enabled by default
flatpak remote-add --if-not-exists flathub-beta https://flathub.org/beta-repo/flathub-beta.flatpakrepo
flatpak install flathub-beta org.freecad.FreeCAD
}}

## Running

You may start the flatpak using the desktop file or using the following command:


{{code|lang=bash|code=
flatpak run org.freecad.FreeCAD
}}

The different branches can be installed in parallel. To choose which one to run use the `--branch` flag:


{{code|lang=bash|code=
flatpak run --branch=beta org.freecad.FreeCAD
}}

To run a specific executable (for example `FreeCADCmd` to run without GUI) from the flatpak use the `--command` flag:


{{code|lang=bash|code=
flatpak run --command=FreeCADCmd org.freecad.FreeCAD
}}

## Repository

-   <https://github.com/flathub/org.freecad.FreeCAD>

### Maintainer(s)

-   [adrianinsaval](https://github.com/adrianinsaval)
-   [hfiguiere](https://github.com/hfiguiere)

## Related

-   [AppImage](AppImage.md) packages
-   [Snap](Snap.md) packages



---
⏵ [documentation index](../README.md) > [Packaging](Category_Packaging.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Testing](Category_Testing.md) > Flatpak/de
