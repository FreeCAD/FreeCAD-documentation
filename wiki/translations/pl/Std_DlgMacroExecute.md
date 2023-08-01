---
- GuiCommand:
   Name:Std DlgMacroExecute
   Name/pl:Std: Okno dialogowe Makrodefinicje
   MenuLocation:Makrodefinicje → Makrodefinicje ...
   Workbenches:wszystkie
   SeeAlso:[Wykonaj makrodefinicję w trakcie edycji](Std_DlgMacroExecuteDirect/pl.md)
---

# Std DlgMacroExecute/pl



## Opis

Polecenie **Makrodefinicje \...** otwiera okno dialogowe Wykonaj makro. W tym oknie dialogowym można wykonywać makra, edytować je i zarządzać nimi.

![](images/Std_DlgMacroExecute_dialog.png ) 
*The Execute macro dialog box*



## Użycie

1.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Std_DlgMacroExecute.svg" width=16px> [Makrodefinicje ...](Std_DlgMacroExecute/pl.md)**.
    -   Wybierz opcję z menu **Makrodefinicje → <img src="images/Std_DlgMacroExecute.svg" width=16px> Makrodefinicje ...**.
2.  Zostanie otwarte okno dialogowe Wykonaj makro. Zobacz dostępne [Opcje](#Opcje.md).



## Opcje



### Makrodefinicje użytkownika 

1.  Zakładka **Makrodefinicje użytkownika** zawiera listę dostępnych makrodefinicji w **lokalizacji makrodefinicji użytkownika**.
2.  Kliknij makro, aby je wybrać.
3.  Nazwa wybranej makrodefinicji zostanie wyświetlona w polu **Nazwa makrodefinicji**.



### Makrodefinicje systemowe 

:   Karta **Makrodefinicje systemowe** nie jest obecnie używana.



### Lokalizacja makrodefinicji użytkownika 

1.  Naciśnij przycisk **...**, aby zmienić lokalizację pliku makroinstrukcji użytkownika.
2.  Przejdź do innego folderu i wybierz go.



### Wykonaj

1.  Aby wykonać dowolną makrodefinicję, należy postępować w jeden z następujących sposobów:
    -   Zaznacz odpowiednia pozycję na liście i naciśnij przycisk **Wykonaj**.
    -   Kliknij dwukrotnie makrodefinicję z listy.
2.  Okno dialogowe zostanie zamknięte.
3.  Makrodefinicja zostanie wykonana.



### Zamknij

1.  Naciśnij **Esc** lub przycisk **Zamknij**, aby zamknąć okno dialogowe.



### Utwórz

1.  Naciśnij przycisk **Utwórz**, aby utworzyć nowy plik makrodefinicji.
2.  Wpisz nazwę w oknie dialogowym, które się pojawi. Nie musisz dołączać rozszerzenia **.FCMacro**.
3.  Naciśnij klawisz **Enter** lub przycisk **OK**.
4.  Oba okna dialogowe zostaną zamknięte.
5.  Nowy plik zostanie otwarty w edytorze makr.



### Usuń

1.  Zaznacz na liście makro, które chcesz usunąć.
2.  Naciśnij przycisk **Usuń**.
3.  Naciśnij przycisk **Tak** w oknie dialogowym potwierdzenia, które się pojawi.



### Edycja

1.  Wybierz z listy makrodefinicję, która ma zostać poddana edycji.
2.  Naciśnij przycisk **Edycja**.
3.  Okno dialogowe zostanie zamknięte.
4.  Wybrany plik zostanie otwarty w edytorze makroinstrukcji.



### Zmień nazwę 

1.  Zaznacz na liście pozycję, której nazwę chcesz zmienić.
2.  Naciśnij przycisk **Zmień nazwę**.
3.  Wpisz nową nazwę w oknie dialogowym, które się pojawi. Nie musisz dołączać rozszerzenia **.FCMacro**.
4.  Naciśnij klawisz **Enter** lub przycisk **OK**.



### Duplikuj

1.  Zaznacz na liście wybrane makropolecenie, które chcesz powielić.
2.  Naciśnij przycisk **Duplikuj**.
3.  Wpisz nową nazwę w oknie dialogowym, które się pojawi. Nie musisz dołączać rozszerzenia **.FCMacro**.
4.  Naciśnij klawisz **Enter** lub przycisk **OK**.



### Pasek narzędzi 

1.  Wybierz z listy wybrane makropolecenie, które chcesz dodać do niestandardowego paska narzędzi.
2.  Naciśnij przycisk **Pasek narzędzi**.
3.  Dwa okna dialogowe \"opis postępowania\" poprowadzą Cię przez wymagane kroki. Więcej informacji na ten temat można znaleźć w opisie [Dostosowywanie interfejsu użytkownika do własnych potrzeb](Interface_Customization/pl.md).



### Pobieranie

1.  Naciśnij przycisk **Pobierz**, aby uruchomić [Menadżer dodatków](Std_AddonMgr/pl.md).



## Uwagi

-   Aby dowiedzieć się więcej o makropoleceniach, zobacz stronę [Makrodefinicje](Macros/pl.md).



## Ustawienia

Lokalizację plików makroinstrukcji użytkownika można również zmienić w preferencjach: **Edycja → Preferencje ... → Python → Makropolecenia → Ścieżka do plików makrodefinicji**. Więcej informacji na ten temat można znaleźć również w [Edytorze ustawień](Preferences_Editor/pl#Makropolecenia.md).





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std DlgMacroExecute/pl
