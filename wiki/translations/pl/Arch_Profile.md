---
 GuiCommand:
   Name: Arch Profile
   Name/pl: BIM: Profil
   MenuLocation: 3D/BIM , Narzędzia ogólne 3D , Profil
   Workbenches: BIM_Workbench/pl
   Version: 0.19
---

# Arch Profile/pl



## Opis

Narzędzie **Profil** tworzy parametryczny obiekt profilu 2D. Obiekt ten może być następnie użyty jako podstawa w innych narzędziach, które wykonują wyciągnięcia, takich jak [Rama](Arch_Frame/pl.md), [Ściana kurtynowa](Arch_CurtainWall/pl.md) lub [Część: Wyciągnij](Part_Extrude/pl.md).

Patrz [lista dostępnych ustawień wstępnych](https://github.com/FreeCAD/FreeCAD/blob/main/src/Mod/BIM/Presets/profiles.csv).

Narzędzie profilu jest również zintegrowane z narzędziem [Konstrukcja](Arch_Structure/pl.md), wszystkie wstępnie ustawione profile są tam również dostępne.



## Użycie

1.  Naciśnij przycisk **<img src="images/Arch_Profile.svg" width=16px> '''Profil'''**.
2.  Wybierz ustawienie wstępne w panelu zadań narzędzia.
3.  Kliknij punkt w widoku 3D, aby umieścić profil.



## Właściwości



### Dane

-    **Wysokość**: Całkowita wysokość profilu.

-    **Szerokość**: Całkowita szerokość profilu.

-    **Średnica**: Średnica profilu *(tylko profile okrągłe)*.

-    **Grubość**: Grubość ścianki rury *(tylko okrągłe i prostokątne puste profile)*.

-    **Web Thickness**: Grubość środnika profilu *(tylko profile H i I)*.

-    **Grubość kołnierza**: Grubość kołnierza profilu *(tylko profile H i I)*.



## Dodawanie profili niestandardowych 

Użytkownik może utworzyć dodatkowy plik CSV zawierający niestandardowe definicje profili. Musi on mieć nazwę `profiles.csv` i być umieszczony w folderze:


{{Code|lang=bash|code=
$FREECAD_USER_DIR/BIM/
}}

lokalizację `$FREECAD_USER_DIR` można uzyskać z [konsoli Python](Python_console.md):


{{Code|lang=bash|code=
FreeCAD.getUserAppDataDir()
}}

Zawartość pliku niestandardowego profilu `profiles.csv` musi być wzorowana na tych samych zasadach, co plik [profiles.csv](https://github.com/FreeCAD/FreeCAD/blob/main/src/Mod/BIM/Presets/profiles.csv) w kodzie źródłowym.

Plik CSV musi zawierać jeden wiersz dla każdego dostępnego profilu, sformatowany w następujący sposób:

-   Dla profili C: Kategoria, Nazwa, Klasa profilu, Średnica, Grubość.
-   Dla profili H, U i T: Kategoria, Nazwa, Klasa profilu, Szerokość, Wysokość, Grubość środnika, Grubość kołnierza.
-   Dla profili L: Kategoria, Nazwa, Klasa profilu, Szerokość, Wysokość, Grubość.
-   Dla profili R: Kategoria, Nazwa, Klasa profilu, Szerokość, Wysokość.
-   Dla profili RH: Kategoria, Nazwa, Klasa profilu, Szerokość, Wysokość, Grubość.

Wszystkie pomiary muszą być podane w milimetrach. Możliwe klasy profili to:

-   C: Rura okrągła,
-   H: [Profil H lub I](https://en.wikipedia.org/wiki/I-beam),
-   R: Prostokątny,
-   RH: Prostokątny wydrążony,
-   U: Profil U,
-   L: Profil L,
-   T: Profil T.

Można utworzyć dodatkowe typy profili, ale najpierw należy zdefiniować odpowiednią klasę w [ArchProfile.py](https://github.com/FreeCAD/FreeCAD/blob/main/src/Mod/BIM/ArchProfile.py).



## Tworzenie skryptów 

Narzędzie **Profil** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następującej funkcji:


```python
profile = makeProfile(profile_list)
```

Gdzie `profile_list` zawiera różne elementy listy w pliku CSV.

Przykład:


```python
import Arch
Arch.makeProfile([0, 'REC', 'REC100x100', 'R', 100, 100])
```

Gdzie pierwszym elementem listy jest numer porządkowy, który nie został jeszcze użyty.



---
⏵ [documentation index](../README.md) > Arch Profile/pl
