# Macros/pl
{{TOCright}}

## Wprowadzenie

[Makra](Macros/pl.md) to wygodny sposób na odtworzenie złożonych działań w programie FreeCAD. Po prostu nagrywasz działania tak, jak je wykonujesz, a następnie zapisujesz je pod nazwą i odtwarzasz, kiedy tylko chcesz. Ponieważ makra są w rzeczywistości listą poleceń [Python](Python.md), możesz je również edytować i tworzyć bardzo złożone skrypty.

Podczas gdy skrypty Pythona zwykle mają rozszerzenie `.py`, makra FreeCAD powinny mieć rozszerzenie `.FCMacro`. Zbiór makr napisanych przez doświadczonych użytkowników znajduje się na stronie [przepisy na makra](macros_recipes.md).

Zobacz [Centrum Power użytkownika](Power_users_hub/pl.md), aby dowiedzieć się więcej o języku programowania [Python](Python.md) oraz o pisaniu makr. W szczególności powinieneś zacząć od tych stron:

-   [Wprowadzenie do środowiska Python](Introduction_to_Python/pl.md)
-   [Poradnik: Tworzenie skryptów Python](Python_scripting_tutorial/pl.md)
-   [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md)

## Jak to działa 

Włącz obsługę wyjścia konsoli w menu **Edcja → Preferencje → Ogólne → Makro → Pokaż polecenia skryptów w konsoli python**. Zobaczysz, że w programie FreeCAD każda wykonywana czynność, taka jak naciśnięcie przycisku, wysyła polecenie Pythona. To właśnie te polecenia mogą być nagrywane w makrze. Głównym narzędziem do tworzenia makr jest pasek narzędzi makr: ![](images/Macros_toolbar.jpg ). Na nim znajdują się 4 przyciski: Rejestrowanie makr, Zatrzymaj nagrywanie makra, Wykonaj makro.

Jest to bardzo łatwe w użyciu:
Naciśnij przycisk {{button|Rejestrowanie makr}}, zostaniesz poproszony o podanie nazwy dla swojego makra, a następnie wykonaj kilka czynności. Kiedy skończysz, kliknij przycisk **Zatrzymaj nagrywanie makra**, a Twoje działania zostaną zapisane. Teraz możesz uzyskać dostęp do okna dialogowego makra za pomocą przycisku {{button|Edycja}}.

![](images/Macros.png ) 
*Okno dialogowe Makro, zawierające listę makrodefinicji dostępnych w systemie.*

W tym miejscu możesz zarządzać swoimi makrami, usuwać, edytować, powielać, instalować lub tworzyć nowe od podstaw. Jeśli edytujesz makro, zostanie ono otwarte w oknie edytora, w którym możesz dokonać zmian w jego kodzie. Nowe makra można zainstalować za pomocą przycisku {{button|Dodatki...}}, który prowadzi do [Addon Manager](AddonManager.md).

## Przykład

Naciśnij przycisk nagrywania, podaj nazwę, powiedzmy \"cylinder 10x10\", a następnie w środowisku [Część](Part_Workbench/pl.md) utwórz walec o promieniu=10 i wysokości=10. Następnie naciśnij przycisk {{button|Zatrzymaj}}. W oknie dialogowym edycji makr możesz zobaczyć kod Pythona, który został nagrany i, jeśli chcesz, wprowadź do niego zmiany. Aby wykonać makro, wystarczy nacisnąć przycisk wykonania na pasku narzędzi, gdy makro znajduje się w edytorze. Twoje makro jest zawsze zapisywane na dysku, więc każda wprowadzona zmiana lub każde nowe makro, które stworzysz, będzie zawsze dostępne przy następnym uruchomieniu programu FreeCAD.

## Dostosowywanie

Oczywiście nie jest praktyczne ładowanie makra w edytorze, aby móc z niego korzystać. FreeCAD zapewnia znacznie lepsze sposoby korzystania z makra, takie jak przypisanie do niego skrótu klawiaturowego lub umieszczenie jego pozycji w menu. Po utworzeniu makra, wszystko to można zrobić poprzez menu **Narzędzia → Dostosuj**.

![](images/Macros_config.jpg )

W ten sposób możesz sprawić, że Twoje makro stanie się prawdziwym narzędziem, tak jak każde standardowe narzędzie FreeCAD. Jest to dodatek do mocy skryptów Python w FreeCAD, który umożliwia łatwe i przyjemne tworzenie własnych narzędzi w interfejsie.

Aby uzyskać bardziej szczegółowy opis, zobacz artykuł [dostosowanie pasków narzędzi](Customize_Toolbars.md).

## Tworzenie makr bez nagrywania 

Możesz również bezpośrednio skopiować/wkleić kod pytona do makra, bez nagrywania akcji w GUI. Po prostu utwórz nowe makro, edytuj je i wklej swój kod. Następnie możesz zapisać swoje makro w ten sam sposób, w jaki zapisujesz dokument FreeCAD. Następnym razem, gdy uruchomisz FreeCAD, makro pojawi się pod pozycją **Zainstalowane makra** w menu Makro.

Zobacz prezentacje [jak zainstalować makrodefinicje](How_to_install_macros/pl.md), aby uzyskać bardziej szczegółowy opis.

## Repozytorium makrodefinicji 

Istnieją dwa główne miejsca, w których można znaleźć makra. Pierwszym z nich jest oficjalne repozytorium makrodefinicji na _, z której możesz wybrać kilka użytecznych makrodefinicji do dodania do swojej instalacji FreeCAD. Makrodefinicje z obu repozytoriów mogą być instalowane poprzez [Menadżer dodatków](Std_AddonMgr/pl.md) bezpośrednio z programu FreeCAD.

## Informacje dodatkowe 

-   [Automatyczne uruchamianie makra podczas startu programu](Macro_at_Startup.md)
-   [Instalacja dodatkowych Środowisk pracy](Installing_more_workbenches.md).

## Poradniki

Możesz ręcznie instalować rozszerzenia, jednak znacznie prostsze jest użycie narzędzia [Menadżer dodatków](Std_AddonMgr/pl.md).

-   [Jak zainstalowac makro](How_to_install_macros/pl.md)
-   [Jak zainstalować dodatkowe Środowiska pracy](How_to_install_additional_workbenches/pl.md)


{{Powerdocnavi

}} 

_ _ _

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Macros/pl
