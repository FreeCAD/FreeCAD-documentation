# Flatpak
{{TOCright}}

### Stable


{{code|
# add flathub repo just to be sure as it might not be enabled if it is your first time using flatpak
flatpak remote-add --if-not-exists flathub https   *//flathub.org/repo/flathub.flatpakrepo
flatpak install flathub org.freecadweb.FreeCAD
}}

### Beta


{{code|
# flathub-beta repo is not enabled by default
flatpak remote-add --if-not-exists flathub-beta https   *//flathub.org/beta-repo/flathub-beta.flatpakrepo
flatpak install flathub-beta org.freecadweb.FreeCAD
}}

Note   * They can be installed in parallel. To choose which one to run use the `--branch` flag   *


{{code|
flatpak run --branch=beta org.freecadweb.FreeCAD
}}

### Repository

-   <https   *//github.com/flathub/org.freecadweb.FreeCAD>

### Maintainer(s)

-   [hfiguiere](https   *//github.com/hfiguiere)

### Related

-   [AppImage](AppImage.md) packages
-   [Snap](Snap.md) panckages



[Category   *Packaging](Category_Packaging.md) [Category   *Developer Documentation](Category_Developer_Documentation.md) [Category   *Testing](Category_Testing.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Packaging](Category_Packaging.md) > [Developer Documentation](Category_Developer Documentation.md) > [Testing](Category_Testing.md) > Flatpak
