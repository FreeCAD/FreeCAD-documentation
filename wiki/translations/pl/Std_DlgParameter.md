---
- GuiCommand:/pl
   Name:Std DlgParameter
   Name/pl:Edytor parametrów
   MenuLocation:Narzędzia → Edytor parametrów ...
   Workbenches:Wszystkie
   SeeAlso:[Edytor preferencji](Preferences_Editor/pl.md)
---

## Opis

Polecenie **Std DlgParameter** otwiera Edytor Parametrów. W Edytorze parametrów można sprawdzać parametry sterujące zachowaniem programu FreeCAD i jego stanowisk pracy oraz opcjonalnie je usunąć, dodać lub zmienić. Parametry są przechowywane w pliku o nazwie {{FileName|user.cfg}}, lokalizacja tego pliku zależy od systemu operacyjnego.

Praca z edytorem parametrów wymaga pewnego doświadczenia. Dla najpopularniejszych parametrów można również skorzystać z wygodniejszego [Edytora preferencji](Preferences_Editor/pl.md).

![](images/Std_DlgParameter_dialog.png ) *Okno dialogowe Edytor parametrów*

## Użycie

Przejdź do menu {{MenuCommand|Tools → <img src="images/Std_DlgParameter.svg" width=16px> Edycja parametrów}}.

1.  Otwiera się okno dialogowe Edytor parametrów. Więcej informacji można znaleźć w sekcji [Opcje](#Opcje.md).
2.  Opcjonalnie wciśnij przycisk **Zapisz na dysku**, aby natychmiast zaktualizować plik {{FileName|user.cfg}}. Nie jest to wymagane, ponieważ FreeCAD automatycznie zaktualizuje ten plik po zamknięciu aplikacji.
3.  Naciśnij przycisk **Zamknij**, aby zamknąć Edytor Parametrów.

## Opcje

### Panel lewy {#panel_lewy}

W lewym panelu wyświetlane jest drzewo z grupami parametrów oraz podgrupami.

\"W menu kontekstowym panelu dostępne są następujące opcje:\"

#### Rozwiń / Zwiń {#rozwiń_zwiń}

1.  Jeśli wybrana grupa posiada jedną lub więcej podgrup, można ją rozszerzyć lub zwinąć wybierając tę opcję z menu kontekstowego. Ale możesz również rozwinąć i zwinąć drzewo w zwykły sposób.

#### Dodaj grupę podrzędną {#dodaj_grupę_podrzędną}

1.  Wybierz grupę.
2.  Wybierz opcję {{MenuCommand|Dodaj podgrupę}}z menu kontekstowego.
3.  Wprowadź nazwę nowej grupy podrzędnej w otwartym oknie dialogowym.
4.  Wciśnij przycisk **OK**.

#### Usuń grupę {#usuń_grupę}

1.  Wybierz grupę.
2.  Wybierz z menu kontekstowego opcję {{MenuCommand|Usuń grupę}}.
3.  W otwartym oknie dialogowym naciśnij przycisk **Tak**, aby potwierdzić, że chcesz usunąć tą grupę *(łącznie ze wszystkimi jej podgrupami, oraz wszystkimi parametrami w grupie i jej podgrupach)*.

#### Zmień nazwę grupy {#zmień_nazwę_grupy}

1.  Wybierz grupę.
2.  Wybierz opcję {{MenuCommand|Zmień nazwę grupy}} z menu kontekstowego.
3.  Wprowadź nową nazwę.
4.  Nazwę grupy można też zmienić klikając w nią dwukrotnie.

#### Eksportuj parametr {#eksportuj_parametr}

1.  Wybierz grupę.
2.  Wybierz opcję {{MenuCommand|Eksportuj parametr}} z menu kontekstowego.
3.  Wprowadź nazwę pliku w oknie dialogowym.
4.  Wciśnij przycisk **Zapisz**.

#### Importuj parametr {#importuj_parametr}

1.  Wybierz grupę, która nie zawiera żadnych podgrup lub usuń je w pierwszej kolejności. Wszystkie istniejące parametry w grupie zostaną usunięte.
2.  Wybierz opcję {{MenuCommand|Importuj parametr}} z menu kontekstowego.
3.  Wybierz plik typu \*.FCParam w oknie dialogowym.
4.  Wciśnij przycisk **Otwórz**.

### Panel prawy {#panel_prawy}

Prawy panel pokazuje parametry wybranej grupy w lewym panelu. Jeśli ta grupa zawiera tylko podgrupy, prawy panel będzie pusty.

\"W menu kontekstowym panelu dostępne są następujące opcje:\"

#### Zmień wartość {#zmień_wartość}

1.  Wybierz parametr.
2.  Wybierz z menu kontekstowego opcję {{MenuCommand|Zmień wartość}}.
3.  Wprowadź nową wartość w otwartym oknie dialogowym.
4.  Naciśnij przycisk **OK**.
5.  Wartość parametru można również zmienić, klikając dwukrotnie jego pole o nazwie **Typ** lub **Wartość**.

#### Usuń element z wartością {#usuń_element_z_wartością}

1.  Wybierz parametr.
2.  Wybierz z menu kontekstowego opcję {{MenuCommand|Usuń element z wartością}}.

#### Zmień nazwę wartości {#zmień_nazwę_wartości}

1.  Wybierz parametr.
2.  Wybierz z menu kontekstowego opcję {{MenuCommand|Zmień nazwę wartości}}.
3.  Wprowadź nową nazwę.
4.  Nazwę parametru można również zmienić klikając dwukrotnie na jego pole \"Nazwa\".

#### Nowy element tekstowy {#nowy_element_tekstowy}

1.  Wybierz z menu kontekstowego opcję {{MenuCommand|Nowy element tekstowy}} lub {{MenuCommand|Nowy → Nowy element tekstowy}}.
2.  Wprowadź nazwę w otwartym oknie dialogowym.
3.  Naciśnij przycisk **OK**.
4.  Wprowadź wartość w następnym oknie dialogowym.
5.  Naciśnij przycisk **OK**.

#### Nowy element z liczbą zmiennoprzecinkową {#nowy_element_z_liczbą_zmiennoprzecinkową}

1.  Wybierz z menu kontekstowego opcję {{MenuCommand|Nowy element z liczbą zmiennoprzecinkową}} lub {{MenuCommand|Nowy → Nowy element z liczbą zmiennoprzecinkową}}.
2.  Kolejne kroki są podobne do tych dla [Nowy element tekstowy](#Nowy_element_tekstowy.md)

#### Nowy element z liczbą całkowitą {#nowy_element_z_liczbą_całkowitą}

1.  Wybierz z menu kontekstowego opcję {{MenuCommand|Nowy element z liczbą całkowitą}} lub {{MenuCommand|Nowy → Nowy element z liczbą całkowitą}}.
2.  Kolejne kroki są podobne do tych dla [Nowy element tekstowy](#Nowy_element_tekstowy.md)

#### Nowy element bez typu {#nowy_element_bez_typu}

1.  Wybierz z menu kontekstowego opcję {{MenuCommand|Nowy element bez typu}} lub {{MenuCommand|Nowy → Nowy element bez typu}}.
2.  Kolejne kroki są podobne do tych dla [Nowy element tekstowy](#Nowy_element_tekstowy.md)

#### Nowy element z wartością logiczną {#nowy_element_z_wartością_logiczną}

1.  Wybierz z menu kontekstowego opcję {{MenuCommand|Nowy element z wartością logiczną}} lub {{MenuCommand|Nowy → Nowy element z wartością logiczną}}.
2.  Kolejne kroki są podobne do tych dla [Nowy element tekstowy](#Nowy_element_tekstowy.md)

### Sortowanie

Domyślnie, grupy lewego panelu na każdym poziomie drzewa są sortowane alfabetycznie, a parametry w prawym panelu również sortowane są alfabetycznie. Kolejność wyświetlania w każdym panelu można odwrócić, klikając odpowiednio nagłówek **Grupa** lub **Nazwa**.

### Szybkie wyszukiwanie {#szybkie_wyszukiwanie}

Wpisanie ciągu znaków *(nawet kilku znaków)* w tym polu wprowadzania danych, spowoduje pełne rozwinięcie drzewa lewego panela i podświetlenie wszystkich grup o nazwach odpowiadających wprowadzonej wartości. Jeśli nie zostaną znalezione żadne dopasowania, tło pola wejściowego zmieni kolor na czerwony.

### Znajdź

1.  W lewym panelu wybierz grupę, w której chcesz rozpocząć wyszukiwanie. Kierunek wyszukiwania będzie przebiegał w dół. Wyszukiwanie nie jest ograniczone do grupy i jej podgrup, ale raczej do wybranej grupy i wszystkiego, co znajduje się pod nią w drzewie.
2.  Naciśnij przycisk **Znajdź...**
3.  Wprowadź ciąg znaków w polu wprowadzania **Znajdź to**. W wyszukiwaniu nie uwzględnia się wielkości liter.
4.  Zaznacz jedno lub więcej pól wyboru {{CheckBox|TRUE|Grupy}}, {{CheckBox|TRUE|Nazwy}} i {{CheckBox|TRUE|Wartości}}. Należy pamiętać, że przeszukiwane będą tylko wartości ciągów znaków.
5.  Opcjonalnie *(odznacz)*zaznacz pole wyboru {{CheckBox|TRUE|Dopasuj tylko cały ciąg}}.
6.  Naciśnij przycisk **Znajdź następny**, aby odnaleźć pierwszą grupę z dopasowaniem. Pasujące parametry nie są wyróżniane indywidualnie. Opcjonalnie można tąc zynność powtarzać aż do momentu, gdy nie będzie można znaleźć kolejnych dopasowań.
7.  Możliwe jest rozpoczęcie nowego wyszukiwania bez zamykania okna dialogowego. Ponowne wybranie grupy, od której należy rozpocząć wyszukiwanie, jest wtedy zazwyczaj wymagane.
8.  Użyj przycisku **Anuluj**, aby zamknąć okno dialogowe.

## Uwagi

-   Na stronie [Dostrajanie parametrów](Fine-tuning/pl.md) wymieniono szereg parametrów, które mogą być interesujące.

## Tworzenie skryptów {#tworzenie_skryptów}


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics.md).

Aby zapoznać się z przykładem tworzenia skryptu, zobacz [Std: SelBoundingBox](Std_SelBoundingBox.md).





{{Std Base navi

}}  
