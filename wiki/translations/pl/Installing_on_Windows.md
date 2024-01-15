# Installing on Windows/pl
{{docnav/pl
|[Funkcjonalność programu](Feature_list/pl.md)
|[Instalacja w systemie Linux](Installing_on_Linux/pl.md)
}}






## Instalacja standardowa 

Najprostszym sposobem na zainstalowanie najnowszej stabilnej wersji FreeCAD jest użycie instalatora, zobacz stronę [Pobieranie](Download/pl.md).

Jeśli chcesz pobrać wersję rozwojową, która może być niestabilna, zobacz stronę [Pobieranie kompilacji tygodniowych](https://github.com/FreeCAD/FreeCAD-Bundle/releases/tag/weekly-builds).

Po pobraniu pliku .exe Instalatora, kliknij jego ikonę dwukrotnie, aby uruchomić proces instalacji.

Poniżej znajduje się więcej informacji na temat opcji technicznych. Większość użytkowników Windows nie będzie potrzebowała nic więcej niż instalator. Gdy zakończysz instalację przejdź do poradnika [Jak zacząć](Getting_started/pl.md).



## Instalacja dla wszystkich użytkowników systemu Windows 

Domyślnie program FreeCAD zostanie zainstalowany dla użytkownika, który uruchomi instalator. Jeśli użytkownik ten posiada jedynie uprawnienia użytkownika, domyślną ścieżką instalacji jest:

:   
    **C:\\Users\<username\\AppData\Local\Programy\FreeCAD X.YY**
    

Jeśli instalator jest uruchamiany przez użytkownika z uprawnieniami administratora lub ty uruchamiasz go jako administrator, możesz wybrać, czy FreeCAD ma być zainstalowany dla wszystkich użytkowników systemu, czy tylko dla Ciebie. Domyślnie instalator jest uruchamiany dla wszystkich użytkowników systemu.

W przypadku instalacji dla wszystkich użytkowników, domyślna ścieżka instalacji to:

:   
    **C:\Program Files\FreeCAD X.YY**
    



## Cicha instalacja 

Aby zainstalować program FreeCAD po cichu, można uruchomić instalator z wiersza poleceń:


{{Code|lang=text|code=
FreeCAD-~.exe /S
}}

Dla wszystkich opcji zostaną zastosowane ustawienia domyślne. W ten sposób można określić niestandardową ścieżkę instalacji:


{{Code|lang=text|code=
FreeCAD-~.exe /S /D=A path to FreeCAD with spaces
}}

Domyślnie, nawet w przypadku cichej instalacji, podczas sprawdzania instalatora pod kątem uszkodzeń zostanie wyświetlone krótkotrwałe okno dialogowe. To tak zwane cykliczne sprawdzanie poprawności trwa najwyżej kilka sekund. Aby wyłączyć sprawdzanie poprawności:


{{Code|lang=text|code=
FreeCAD-~.exe /S /NCRC
}}

Uwaga: ta flaga {{Incode|/NCRC}} jest **niezalecana**, ponieważ sprawdzanie poprawności zapewnia, że instalator został np. całkowicie pobrany.



## Chocolatey

W celu przeprowadzenia aktualizacji oprogramowania zaleca się jednak używanie menedżera pakietów, takiego jak **Chocolatey**.
Możesz zainstalować Chocolatey, postępując zgodnie z [instrukcjami](https://chocolatey.org/install), a następnie otworzyć terminal PowerShell jako administrator i uruchomić proces aktualizacji:


{{Code|lang=text|code=
choco install freecad
}}

Raz na jakiś czas można zaktualizować oprogramowanie poprzez:


{{Code|lang=text|code=
choco upgrade freecad
}}

Aby uzyskać najnowszą wersję dostępną w repozytorium Chocolatey. W przypadku wystąpienia jakichkolwiek problemów z pakietem Chocolatey, możesz skontaktować się z opiekunami na stronie [o tutaj](https://chocolatey.org/packages/freecad).



## Deinstalacja

Aby odinstalować program FreeCAD, najlepiej jest użyć narzędzi Windows do odinstalowywania oprogramowania. Można też bezpośrednio uruchomić dezinstalator. To jest ten plik:

:   
    **Uninstall-FreeCAD.exe**
    

Można go znaleźć w folderze, w którym zainstalowany jest program FreeCAD.

Odinstalowanie programu można także wykonać za pomocą wiersza poleceń:


{{Code|lang=text|code=
Uninstall-FreeCAD.exe /S}}

Należy pamiętać, że *(cicha)* deinstalacja nie powiedzie się, jeśli istnieje działająca instancja programu FreeCAD, nawet jeśli nie jest to wersja, która jest odinstalowywana.


{{docnav/pl
|[Funkcjonalność programu](Feature_list/pl.md)
|[Instalacja w systemie Linux](Installing_on_Linux/pl.md)
}}



---
⏵ [documentation index](../README.md) > Installing on Windows/pl
