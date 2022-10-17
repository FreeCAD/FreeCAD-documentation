# Flatpak/pl
{{TOCright}}

## Instalacja

### Wersja stabilna 

Jeśli chcesz przeprowadzić instalację na poziomie użytkownika lub nie masz uprawnień sudo, dodaj flagę `--user` do następujących poleceń   *


{{code|lang=bash|code=
# add flathub repo just to be sure as it might not be enabled if it is your first time using flatpak
flatpak remote-add --if-not-exists flathub https   *//flathub.org/repo/flathub.flatpakrepo
flatpak install flathub org.freecadweb.FreeCAD
}}

### Wersja rozwojowa 

Jeśli chcesz przeprowadzić instalację na poziomie użytkownika lub nie masz uprawnień sudo, dodaj flagę `--user` do następujących poleceń   *


{{code|lang=bash|code=
# flathub-beta repo is not enabled by default
flatpak remote-add --if-not-exists flathub-beta https   *//flathub.org/beta-repo/flathub-beta.flatpakrepo
flatpak install flathub-beta org.freecadweb.FreeCAD
}}

## Uruchomienie

Możesz uruchomić flatpak za pomocą ikonki pulpitu lub za pomocą następującego polecenia   *


{{code|lang=bash|code=
flatpak run org.freecadweb.FreeCAD
}}

Różne gałęzie mogą być instalowane równolegle. Aby wybrać, która z nich ma być uruchomiona, użyj flagi `--branch`   *


{{code|lang=bash|code=
flatpak run --branch=beta org.freecadweb.FreeCAD
}}

Aby uruchomić konkretny plik wykonywalny *(na przykład `FreeCADCmd`, aby uruchomić bez GUI)* flatpaka użyj flagi `--command`   *


{{code|lang=bash|code=
flatpak run --command=FreeCADCmd org.freecadweb.FreeCAD
}}

## Repozytorium

-   <https   *//github.com/flathub/org.freecadweb.FreeCAD>

### Opiekunowie

-   [hfiguiere](https   *//github.com/hfiguiere)

## Powiązane

-   paczki [AppImage](AppImage/pl.md)
-   paczki [Snap](Ubuntu_Snap/pl.md)

[Category   *Packaging](Category_Packaging.md) [Category   *Developer Documentation](Category_Developer_Documentation.md) [Category   *Testing](Category_Testing.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Packaging](Category_Packaging.md) > [Developer Documentation](Category_Developer Documentation.md) > [Testing](Category_Testing.md) > Flatpak/pl
