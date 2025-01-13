---
 GuiCommand:
   Name: Assembly CreateJointGears
   Name/pl: Złożenie Utwórz połączenie kół zębatych
   MenuLocation: Złożenie , Utwórz połączenie przekładni zębatej / pasowej , Utwórz połączenie kół zębatych
   Workbenches: Assembly_Workbench/pl
   Shortcut: 
   Version: 1.0
   SeeAlso: 
---

# Assembly CreateJointGears/pl



## Opis

Narzędzie <img alt="" src=images/Assembly_CreateJointGears.svg  style="width:24px;"> [Utwórz połączenie kół zębatych](Assembly_CreateJointGears/pl.md) tworzy połączenie kół zębatych wiążące obrót dwóch części z dwoma różnymi połączeniami typu Obrotowe. Razem z innymi istniejącymi połączeniami pozwala zasymulować koła walcowe, stożkowe, przekładnie cierne i inne.



## Użycie

1.  Opcjonalnie wybierz dwa obiekty geometryczne należące do dwóch różnych części, które zostały wcześniej użyte do zdefiniowania dwóch połączeń typu Obrotowe.
2.  Jest kilka sposobów na wywołanie tego polecenia:
    -   Wciśnij przycisk **<img src="images/Assembly_CreateJointGears.svg" width=16px> '''Utwórz połączenie koła zębatego / pasa'''**.
    -   Wybierz opcję **Złożenie → <img src="images/Assembly_CreateJointGears.svg" width=16px> Utwórz połączenie koła zębatego / pasa** z menu.
3.  Okno dialogowe **Utwórz połączenie** zostanie otwarte w [panelu zadań](Task_panel/pl.md), wymieniając wcześniej wskazane obiekty.
4.  Dla dalszych kroków zobacz [Utwórz połączenie stałe](Assembly_CreateJointFixed/pl#Użycie.md).



## Uwagi

-   Promień1 i Promień2 odnoszą się do okręgów podziałowych kół zębatych lub zewnętrznych średnic w przypadku przekładni ciernej. Ich wartości są przechowywane we właściwościach **Distance** oraz **Distance2** i definiują stosunek między obrotami.
-   Ponieważ wartości obu promieni nie mają wpływu na odległość między osiami obrotu i jednostki i tak są anulowane, możesz rozważyć wprowadzenie wartości średnic lub liczby zębów (nie trzeba wtedy szukać średnicy podziałowej kół stożkowych) dla obu promieni.
-   Użyj tej samej wartości dla obu promieni aby połączyć końce wału giętkiego (jeśli obroty nie pasują, odwróć jedno połączenie Obrotowe lub użyj połączenia Pasowego zamiast tego).



## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Obiekt **Gears** wywodzi się z obiektu [App: Właściwości Python](App_FeaturePython/pl.md) i dziedziczy wszystkie jego właściwości. Zobacz [Utwórz połączenie stałe](Assembly_CreateJointFixed/pl#Właściwości.md) aby znaleźć dodatkowe właściwości.





{{Assembly_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Assembly](Assembly_Workbench.md) > Assembly CreateJointGears/pl
