---
- GuiCommand:/pl
   Name:Plot Axes
   Name/pl:Wykres: Konfiguruj osie
   MenuLocation:Wykres → Konfiguruj osie
   Workbenches:[Wykres](Plot_Workbench/pl.md)
---

# Plot Axes/pl

## Opis

Standardowy moduł wykresów dostarcza już elementarne narzędzie do kontroli osi wykresów <img alt="" src=images/Matplotlib_edit_subplot.png  style="width:24px;">. Jednak narzędzie to jest niewystarczające, gdy trzeba obsługiwać wieloosiowe wykresy, jak to ma miejsce w _ używając [Menadżera dodatków](Std_AddonMgr/pl.md), dzięki czemu będzie dostępne bardziej kompletne narzędzie do edycji osi wykresu.

<img alt="" src=images/Plot_MultiAxes_Example.png  style="width:600px;">

## Użycie

Wybierz kartę wykresu, którą chcesz edytować, i uruchom to narzędzie.

Zalecane jest rozpoczęcie skalowania całej powierzchni, aby mieć pewność, że zmieści się ona w dostępnej przestrzeni. W tym celu należy włączyć opcję **Zastosuj do wszystkich osi**.

![Apply to all axes](images/Apply_To_All_Axes.png ) 
*Zastosuj do wszystkich selektorów osi*

Następnie możesz przeskalować cały wykres, aby zmieścić go w widocznym obszarze, używając czterech suwaków.

![Plot area controlling sliders](images/Plot_Axes_Sliders.png ) 
*Suwaki do skalowania wykresu*

Kiedy jesteś zadowolony z ogólnego rozmiaru wykresu, możesz odznaczyć **Zastosuj do wszystkich osi** i dostroić każdy zestaw osi niezależnie. Po prostu wybierz zestaw osi, które chcesz edytować na górze.

![Plot axes selector](images/Plot_Axes_Active.png ) 
*Selektor dla zestawu osi do edycji*

Ponownie możesz użyć suwaków, aby kontrolować obszar objęty przez dany wykres cząstkowy. Możesz również kontrolować, gdzie umieszczane są zaznaczenia i napisy zarówno dla osi X jak i Y.

![Plot axes position editor](images/Plot_Axes_Position.png ) 
*Edytor pozycji dla wybranych osi*

Dokładniej, można ustawić, czy oś X jest wyświetlana poniżej czy powyżej wykresu, jak również czy oś Y jest wyświetlana po lewej czy po prawej stronie wykresu. Można nawet ustawić przesunięcie obu osi względem linii bazowej wykresu.

Na koniec można ustawić minimalne i maksymalne wartości uwzględniane dla każdego zestawu osi, tzw. przybliżenie.

![Plot zoom editor](images/Plot_Axes_Zoom.png ) 
*Edytor rozważanych wartości minimalnych i maksymalnych*





{{Plot_Tools_navi

}} 

_ _

---
[documentation index](../README.md) > [External_Workbenches](Category_External_Workbenches.md) > Plot Axes/pl
