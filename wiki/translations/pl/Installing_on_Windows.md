# Installing on Windows/pl



{{docnav/pl
|[Funkcjonalność programu](Feature_list/pl.md)
|[Instalacja w systemie Linux](Installing_on_Linux/pl.md)
}}

Możesz zainstalować FreeCAD w systemie Windows pobierając jeden z poniższych instalatorów:


{{DownloadWindowsStable}}

Po pobraniu pliku .exe *(Instalator NSIS)*, kliknij jego ikonę dwukrotnie, aby uruchomić proces instalacji.

Poniżej znajduje się więcej informacji na temat opcji technicznych. Większość użytkowników Windows nie będzie potrzebowała nic więcej niż powyższy plik .exe, aby zainstalować FreeCAD. Gdy zakończysz instalacje przejdź do poradnika [Jak zacząć](Getting_started/pl.md).

## Łatwa instalacja instalatorem NSIS 

Najprostszym sposobem na **zainstalowanie programu FreeCAD w systemie Windows** jest skorzystanie z powyższego pakietu instalatora, przygotowanego do pobrania. Ta strona opisuje użycie i funkcje *Instalatora NSIS*, aby umożliwić przeprowadzenie instalacji z większą ilością opcji.

Jeśli chcesz pobrać wersję rozwojową (która może być niestabilna), odwiedź stronę [Download](Download/pl.md).

## Chocolatey

W celu przeprowadzenia aktualizacji oprogramowania zaleca się jednak używanie menedżera pakietów, takiego jak **Chocolatey**.
Możesz zainstalować Chocolatey, postępując zgodnie z [instrukcjami](https://chocolatey.org/install), a następnie otworzyć terminal PowerShell jako administrator i uruchomić proces aktualizacji:


```python
choco install freecad
```

raz na jakiś czas można zaktualizować oprogramowanie poprzez


```python
choco upgrade freecad
```

aby uzyskać najnowszą wersję dostępną w repozytorium Chocolatey. W przypadku wystąpienia jakichkolwiek problemów z pakietem Chocolatey, możesz skontaktować się z opiekunami na stronie [o tutaj](https://chocolatey.org/packages/freecad).

## Instalacja z użyciem wiersza poleceń 

Za pomocą narzędzia wiersza poleceń *msiexec.exe* dostępne są dodatkowe funkcje, takie jak nieinteraktywna instalacja i instalacja administratora. Zobacz przykłady poniżej.

### Instalacja nieinteraktywna 

Z wiersza poleceń


```python
msiexec /i FreeCAD<version>.msi
```

Instalacja może być inicjowana przez system programowo. Dodatkowe parametry mogą być przekazywane na końcu linii poleceń, np.


```python
msiexec /i FreeCAD-2.5.msi TARGETDIR=R:\FreeCAD25
```

### Kontrola interfejsu użytkownika 

Zakres kontroli użytkownika dozwolony przez instalatora może być określony za pomocą opcji /q:

-   /qn - Brak interfejsu.

/qb - Podstawowy interfejs - wyświetlane jest tylko okno postępu, z przyciskiem Anuluj

-   /qb! - Jak /qb, ale ukryto przycisk Anuluj.

/qr - Zredukowany interfejs - wyświetla wszystkie okna dialogowe, które nie wymagają interakcji z użytkownikiem *(nie wymaga odpowiedzi uzytkownika)*.

-   /qn+ - Jak /qn, ale na końcu wyświetl okno dialogowe \"Zakończone\".

### Katalog docelowy 

Parametr TARGETDIR określa główny katalog instalacji FreeCAD. Np. inny dysk instalacji może być określony przez


```python
TARGETDIR=R:\FreeCAD25
```

Domyślna wartość TARGETDIR to \[WindowsVolume\\Programm Files\\\]FreeCAD.

### Instalacja dla wszystkich użytkowników 

Dodanie


```python
ALLUSERS=1
```

powoduje, że instalacja jest wykonana dla wszystkich użytkowników. Domyślnie instalacja nie-interaktywna **/i** sprawia, że pakiet może być używany tylko przez aktualnego użytkownika *(tego, który wykonuje instalację)*. Instalacja interaktywna przedstawia okno dialogowe, które domyślnie jest dostępne dla \"wszystkich użytkowników\", jeśli użytkownik wykonujący instalację ma wystarczające uprawnienia.

### Wybór właściwości 

Szereg parametrów umożliwia wybór funkcji, które mają być zainstalowane, ponownie zainstalowane lub usunięte. Zestaw parametrów dla instalatora FreeCAD zawiera:

-   DefaultFeature - zainstaluj aplikację i podstawowe biblioteki.
-   Documentation - zainstaluj dokumentację.
-   Source code - zainstaluj pliki źródłowe.
-   \... Do zrobienia.

Dodatkowo, ALL zaznacza wszystkie właściwości. Wszystkie funkcje zależą od **DefaultFeature**, więc instalacja jakiejkolwiek z nich automatycznie instaluje również funkcję podstawową. Następujące funkcje kontroli właściwości regulują instalowanie lub usuwanie składników:

-   ADDLOCAL - lista funkcji, które należy zainstalować lokalnie.
-   REMOVE - lista składników, do usunięcia lokalnie.
-   ADDDEFAULT - lista funkcji dodanych w domyślnej konfiguracji *(lokalna dla wszystkich funkcji FreeCAD)*.
-   REINSTALL - lista składników, które mają być ponownie zainstalowane/naprawione.
-   ADVERTISE - lista funkcji, dla których należy wykonać instalację z informacją reklamową.

Dostępnych jest kilka dodatkowych właściwości; szczegółowe informacje znajdują się w dokumentacji MSDN.

Dzięki tym opcjom, dodając


```python
ADDLOCAL=Extensions
```

wykonana będzie instalacja samego interpretera i rejestracja rozszerzeń, ale nie spowoduje to instalacji niczego innego.

## Deinstalacja

Poprzez:


```python
msiexec /x FreeCAD<version>.msi
```

FreeCAD może zostać odinstalowany. Nie jest konieczne posiadanie pliku MSI dostępnego do odinstalowania. Opcjonalnie można również podać kod pakietu lub produktu. Kod produktu można znaleźć, przeglądając właściwości skrótu do odinstalowania, który FreeCAD instaluje w Menu Start.

## Instalacja Sieciowa 

Poprzez:


```python
msiexec /a FreeCAD<version>.msi
```

można rozpocząć instalację sieciową. Pliki zostaną rozpakowywane do katalogu docelowego *(który powinien być katalogiem sieciowym)*, ale żadne inne modyfikacje nie będą dokonywane w systemie lokalnym. Ponadto w katalogu docelowym generowany jest kolejny *(mniejszy)* plik msi, który klienci mogą wykorzystać do wykonania instalacji lokalnej *(przyszłe wersje mogą również oferować zachowanie niektórych funkcji na dysku sieciowym)*.

Aktualnie nie ma interfejsu użytkownika dla instalacji sieciowej, więc katalog docelowy musi być określony za pośrednictwem wiersza poleceń.

Nie opracowano specjalnej procedury odinstalowywania dla instalacji sieciowej. Wystarczy usunąć katalog docelowy, jeśli żaden klient nie korzysta już z niego.

## Promowanie

Poprzez:


```python
msiexec /jm FreeCAD<version>.msi
```

w zasadzie możliwe byłoby promowanie FreeCAD na maszynie *(za pomocą **/ju** dla każdego użytkownika)*. Spowoduje to, że ikony pojawią się w menu startowym, a rozszerzenia zostaną zarejestrowane, bez faktycznego zainstalowania oprogramowania. Pierwsze użycie składnika spowodowałoby zainstalowanie tej funkcji.

Instalator FreeCAD obsługuje obecnie tylko promowanie wpisów w menu startowym, ale nie obsługuje promowania skrótów.

## Automatyczna instalacja w grupie maszyn 

Dzięki Windows Group Policy, możliwa jest automatyczna instalacja programu FreeCAD na grupie maszyn. Aby to zrobić, wykonaj następujące kroki:

1.  Zaloguj się do kontrolera domeny.
2.  Skopiuj plik MSI do folderu współdzielonego z dostępem przyznanym wszystkim komputerom docelowym.
3.  Otwórz przystawkę MMC **Użytkownicy i komputery usługi Active Directory**.
4.  Przejdź do grupy komputerów, które potrzebują FreeCAD.
5.  Otwórz właściwości.
6.  Otwórz zasady grupy.
7.  Dodaj nową zasadę i edytuj ją.
8.  Konfiguracja n komputerów / Instalacja oprogramowania, wybierz Nowy / Pakiet.
9.  Wybierz plik MSI poprzez ścieżkę sieciową.
10. Opcjonalnie wybierz, że chcesz, aby FreeCAD został odinstalowany, jeśli komputer pozostanie poza zakresem zasad.

Wdrożenie polityki grupowej zazwyczaj jest czasochłonne - aby niezawodnie wdrożyć pakiet, wszystkie maszyny powinny zostać zrestartowane.

## Instalacja pod Linuksem przy użyciu Crossover Office 

FreeCAD w wersji dla systemu Windows można zainstalować na systemie Linux za pomocą **CXOffice 5.0.1**. W tym celu należy uruchomić *msiexec* z wiersza poleceń CXOffice. Zakładając, że pakiet instalacyjny znajduje się w katalogu \"software\" na dysku \"Y:\":


```python
msiexec /i Y:\\software\\FreeCAD<version>.msi
```

FreeCAD został uruchomiony, lecz zgłoszono, że nie działa system OpenGL, tak jak w przypadku innych programów działających w środowisku [Wine](wikipedia:Wine_(software).md), na przykład Google [SketchUp](wikipedia:SketchUp.md).


{{docnav/pl
|[Funkcjonalność programu](Feature_list/pl.md)
|[Instalacja w systemie Linux](Installing_on_Linux/pl.md)
}}



