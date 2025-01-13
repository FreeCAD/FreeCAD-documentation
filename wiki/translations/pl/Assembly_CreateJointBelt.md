---
 GuiCommand:
   Name: Assembly CreateJointBelt
   Name/pl: Złożenie Utwórz połączenie pasowe
   MenuLocation: Złożenie , Utwórz połączenie przekładni zębatej/pasowej , Utwórz połączenie pasowe
   Workbenches: Assembly_Workbench/pl
   Shortcut: 
   Version: 1.0
   SeeAlso: 
---

# Assembly CreateJointBelt/pl



## Opis

Narzędzie <img alt="" src=images/Assembly_CreateJointBelt.svg  style="width:24px;"> **Utwórz połączenie pasowe** tworzy połączenie przekładni pasowej, które wiąże obrót dwóch części z dwoma różnymi połączeniami typu Obrotowe. Razem z innymi istniejącymi połączeniami pozwala zasymulować napędy pasowe, paski rozrządu itd.



## Użycie

1.  Opcjonalnie wybierz dwa obiekty geometryczne należące do dwóch różnych części, które zostały wcześniej użyte do zdefiniowania dwóch połączeń typu Obrotowe.
2.  Jest kilka sposobów na wywołanie tej komendy:
    -   Wciśnij przycisk **<img src="images/Assembly_CreateJointBelt.svg" width=16px> [Utwórz połączenie pasowe](Assembly_CreateJointBelt/pl.md)**.
    -   Wybierz opcję **Złożenie → Utwórz połączenie przekładni zębatej / pasowej → <img src="images/Assembly_CreateJointBelt.svg" width=16px> Utwórz połączenie pasowe** z menu.
3.  Okno dialogowe **Utwórz połączenie** zostanie otwarte w [panelu zadań](Task_panel/pl.md), wymieniając wcześniej wskazane obiekty.
4.  Dla dalszych kroków zobacz [Utwórz połączenie stałe](Assembly_CreateJointFixed/pl#Użycie.md).



## Uwagi

-   Promień 1 i Promień2 odnoszą się do okręgów podziałowych kół rozrządu lub zewnętrznej średnicy kół pasowych. Ich wartości są przechowywane we właściwościach **Distance** oraz **Distance2** i definiują stosunek między obrotami.
-   Użyj tej samej wartości dla obu promieni żeby połączyć końce wału giętkiego *(jeśli obroty się nie zgadzają, odwróć jedno z połączeń typu [Obrotowe](Assembly_CreateJointRevolute/pl.md) lub użyj połączenia typu [Koła zębate](Assembly_CreateJointGears/pl.md) zamiast tego)*.



## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Obiekt **Bell** wywodzi się z obiektu [App: Właściwości Python](App_FeaturePython/pl.md) i dziedziczy wszystkie jego właściwości. Zobacz [Utwórz połączenie stałe](Assembly_CreateJointFixed/pl#Właściwości.md) aby znaleźć dodatkowe właściwości.





{{Assembly_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Assembly](Assembly_Workbench.md) > Assembly CreateJointBelt/pl
