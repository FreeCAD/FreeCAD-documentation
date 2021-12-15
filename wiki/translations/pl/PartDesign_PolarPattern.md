---
- GuiCommand:/pl
   Name:PartDesign PolarPattern
   Name/pl:Projekt Części: Szyk kołowy
   MenuLocation:Part Design → Zastosuj szyk → Szyk kołowy
   Workbenches:[Projekt Części](PartDesign_Workbench/pl.md)
---

# PartDesign PolarPattern/pl

## Opis

Narzędzie wzorca kołowego przyjmuje wybrany element i tworzy zestaw kopii obróconych wokół wybranej osi. {{Version/pl|0.17}} Listę cech można modelować.

![](images/PartDesign_PolarPattern_example.png )

\'\'Powyżej: kieszeń w kształcie szczeliny (B) wykonana na bazie bryły (A, zwana również podstawą) jest używana do tworzenia wzoru biegunowego. Wynik (C) jest pokazany po prawej stronie\".

## Użycie

#### Aby stworzyć wzorzec 

1.  Wybierz element *({{Version/pl|0.19}} lub kilka elementów)*, które mają być układane we wzór.
2.  Naciśnij przycisk **<img src="images/PartDesign_PolarPattern.svg" width=24px> '''Szyk kołowy'''**.
3.  \* Jeśli początkowo nie wybrałeś żadnych elementów, będziesz mógł wybrać „jeden" bazowy.
4.  Zdefiniuj **Oś**. Patrz [Opcje](#Opcje.md).
5.  Określ **Kąt** pomiędzy ostatnim skopiowanym wystąpieniem a oryginalnym elementem.
6.  Ustaw liczbę **Wystąpień**.
7.  Jeśli masz kilka elementów we wzorcu, ich kolejność może być ważna, zobacz obrazek poniżej.
8.  Naciśnij przycisk **OK**.

#### Cechy szczególne 

![](images/PartDesign_feature-order.gif ) 
*Efekty kolejności występowania elementów*


{{Version/pl|0.19}}

Możesz zmienić kolejność, przeciągając element na liście, a rezultat pojawi się natychmiast w podglądzie.

#### Dodawanie elementów 

###### v0.18

1.  Naciśnij przycisk **Dodaj element**, aby dodać element, który ma być wzorcem. Element musi być widoczny w oknie [widoku 3D](3D_view/pl.md):
2.  Przejdź do widoku drzewa modelu,
3.  Wybierz w drzewie element, który ma zostać dodany i naciśnij klawisz **Spacja**, aby wybrany element był widoczny w oknie [widoku 3D](3D_view/pl.md),
4.  Przejdź z powrotem do panelu zadań,
5.  Wybierz element w oknie [widoku 3D](3D_view/pl.md), zostanie on dodany do listy,
6.  Powtórz czynność, aby dodać inne elementy.

###### v0.19

1.  Naciśnij przycisk **Dodaj element**, aby dodać element, który ma być wzorcem.
2.  Przejdź do widoku drzewa modelu,
3.  Wybierz w drzewie element, który ma zostać dodany.
4.  Powtórz czynność, aby dodać inne elementy.

#### Usuwanie elementów 

-   Kliknij prawym przyciskiem myszy element na liście i wybierz **Usuń**.

lub

###### v0.18 

1.  Naciśnij przycisk **Usuń element**, aby usunąć element z listy. Element musi być widoczny w oknie [widoku 3D](3D_view/pl.md):
2.  Przejdź do widoku drzewa modelu,
3.  Wybierz w drzewie element, który ma zostać usunięty i naciśnij klawisz **Spacja**, aby wybrany element był widoczny w oknie [widoku 3D](3D_view/pl.md),
4.  Przejdź z powrotem do panelu zadań,
5.  Wybierz element w oknie [widoku 3D](3D_view/pl.md), zostanie on skasowany z listy,
6.  Powtórz czynność, aby usunąć inne elementy.

###### v0.19 

1.  Naciśnij przycisk **Usuń element**, aby usunąć element z listy.
2.  Przejdź do widoku drzewa modelu,
3.  Wybierz w drzewie element, który ma zostać usunięty.
4.  Powtórz czynność, aby usunąć inne elementy.

## Opcje

![](images/Polarpattern_parameters.png )

### Oś

Podczas tworzenia cech szyku kołowego, dialog \"Szyk kołowy parametry\" oferuje różne sposoby określania osi obrotu dla szyku.

#### Oś normalna szkicu 

Oś, która jest prostopadła do szkicu i rozpoczyna się od początku szkicu wykorzystywanego obiektu, jest brana jako oś dla wzorca kołowego.
Kierunek wzoru można odwrócić, zaznaczając opcję **Odwróć kierunek**.

#### Pozioma oś szkicu 

Używa poziomej osi szkicu jako osi dla wzorca.

#### Pionowa oś szkicu 

Używa pionowej osi szkicu jako osi dla wzorca.

#### Niestandardowa oś szkicu 

Jeżeli szkic definiujący element, który ma być użyty jako wzór, zawiera również linię *(lub linie)* konstrukcyjną, to lista rozwijana będzie zawierać jedną niestandardową oś szkicu dla każdej linii konstrukcyjnej. Pierwsza linia konstrukcyjna będzie oznaczona etykietą *Oś szkicu 0*.

#### Oś bazowa *(X / Y / Z)* 


{{VersionPlus/pl|0.17}}

Wybierz jedną ze standardowych osi odniesienia bryły *(X, Y lub Z)* jako oś dla wzorca.

#### Wybierz odniesienie\... 

Umożliwia wybranie linii odniesienia lub krawędzi obiektu lub linii szkicu do użycia jako osi dla wzorca.

### Kąt i wystąpienia 

Określa kąt, który ma zostać ujęty we wzorcu, oraz całkowitą liczbę kształtów wzoru *(łącznie z elementem oryginalnym)*. Na przykład, cztery wystąpienia pod kątem 180° dają odstęp 60° między wzorcami. Jest jeden wyjątek: Jeśli kąt wynosi 360°, ponieważ pierwsze i ostatnie wystąpienie są identyczne, cztery wystąpienia będą od siebie oddalone o 90 stopni.

## Ograniczenia

-   Zapoznaj się z tematem [ograniczenia cech wzorca liniowego](PartDesign_LinearPattern/pl#Ograniczenia.md).





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign PolarPattern/pl
