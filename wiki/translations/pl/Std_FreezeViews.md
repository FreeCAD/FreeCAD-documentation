---
- GuiCommand:
   Name: Std FreezeViews
   Name/pl: Std: Zamroź widok
   MenuLocation: Widok -> Zamroź widok -> ...
   Workbenches: Wszystkie
   SeeAlso: Std_StoreWorkingView/pl, Std_RecallWorkingView/pl,Std_ViewIvIssueCamPos/pl
---

# Std FreezeViews/pl



## Wprowadzenie

FreeCAD może przechowywać ujęcia widoku maksymalnie w 50 \"zamrożonych widokach\". Opcje menu, które dotyczą zamrożonych widoków, można znaleźć w menu podrzędnym **Widok → Zamroź widok**. Zamrożone widoki nie są zapisywane w dokumencie i, jeśli nie zostaną zapisane za pomocą opcji **[Zapisz widoki \...](#Zapisz_widok.md)**, zostaną utracone po zamknięciu aplikacji FreeCAD.



## Zapisz widok 



### Opis

Opcja menu **Zapisz widoki\...** zapisuje wszystkie istniejące zamrożone widoki w pliku z rozszerzeniem \*.cam.



### Użycie

1.  Aby użyć tej opcji musi istnieć jeden lub więcej zamrożonych widoków. Widok zamrożony tworzy się za pomocą opcji menu **[Zamroź widok](#Zamro.C5.BA_widok.md)**.
2.  Wybierz z menu opcję **Widok → Zamroź widok → Zapisz widoki ...**.
3.  Wprowadź nazwę pliku w oknie dialogowym.
4.  Naciśnij przycisk **Zapisz**.



### Opcje

-   Naciśnij przycisk **Esc** lub przycisk **Anuluj** aby przerwać wykonywanie polecenia.



## Wczytaj widok 



### Opis 

Opcja menu **Załaduj widoki\...** wczytuje zamrożone widoki z pliku z rozszerzeniem \*.cam. Wszystkie istniejące zamrożone widoki zostaną usunięte.



### Użycie 

1.  Wybierz z menu opcję **Widok → Zamroź widok → Załaduj widoki ...**.
2.  Naciśnij przycisk **Tak** w oknie dialogowym Przywróć widoki, aby potwierdzić, że chcesz usunąć wszystkie istniejące zamrożone widoki.
3.  Wybierz plik.
4.  Naciśnij przycisk **Otwórz**.



### Opcje 

-   Jeśli zostanie wyświetlone okno dialogowe Przywróć widoki: naciśnij klawisz **Esc** lub przycisk **Nie**, aby przerwać wykonywanie polecenia.
-   Jeśli zostanie wyświetlone okno dialogowe Plik: naciśnij przycisk klawisz **Esc** lub przycisk **Anuluj**, aby przerwać polecenie.



## Zamroź widok 



### Opis 

Opcja menu **Zamroź widok** zapisuje bieżące ustawienia ujęcia widoku *(kierunek, zoom itp.)* w oknie [widoku 3D](3D_view/pl.md) na nowej pozycji listy zamrożonych widoków. Lista zamrożonych widoków może zawierać do 50 pozycji.



### Użycie 

1.  Istnieje kilka sposobów na wywołanie tej opcji:
    -   Wybierz z menu opcję **Widok → Zamroź widok → Zamroź widok**.
    -   Użyj skrótu klawiaturowego: **Shift**+**F**.
2.  Nowy zamrożony widok można wybrać w podmenu **Widok → Zamroź widok**.



## Wyczyść widoki 



### Opis 

Opcja menu **Wyczyść widoki** usuwa wszystkie istniejące zamrożone widoki.



### Użycie 

1.  Wybierz z menu opcję **Widok → Zamroź widok → Wyczyść widoki**.



## Odtwórz widok 



### Opis 

Dla każdego zamrożonego widoku dodana jest opcja **Przywróć widok**, za pomocą której można go przywrócić. Opcje są ponumerowane od: **Przywróć widok 1** do **Przywróć widok 50**.



### Użycie 

1.  Istnieje kilka sposobów na wywołanie tej opcji:
    -   Wybierz z menu właściwą opcję **Widok → Zamroź widok → Załąduj widoki ...**.
    -   Dla pierwszych 9 zamrożonych widoków: użyj skrótu klawiaturowego: **Ctrl**+**1** - **Ctrl**+**9**.





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std FreezeViews/pl
