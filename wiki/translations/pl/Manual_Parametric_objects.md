# Manual:Parametric objects/pl
{{Manual:TOC}}

FreeCAD stosuje podejście projektowania parametrycznego, w którym geometria obiektów jest sterowana przez zasady i parametry, a nie dowolnie modelowana. Oznacza to, że wymiary i cechy każdego komponentu są definiowane przez parametry, które instruują program, jak generować geometrię. Na przykład, aby stworzyć cylinder, określa się takie parametry jak promień i wysokość. Na podstawie tych wartości FreeCAD generuje precyzyjny kształt geometryczny.

We FreeCAD obiekty parametryczne są zasadniczo małymi, programowalnymi skryptami, które wykonują się po każdej zmianie parametru. Parametry te mogą się znacznie różnić, obejmując liczby całkowite i zmiennoprzecinkowe, wartości wymiarowe z rzeczywistego świata, takie jak milimetry, metry czy stopy, współrzędne (wyrażone jako x, y, z), ciągi tekstowe, a nawet odwołania do innych obiektów. Taka wszechstronność parametrów umożliwia tworzenie skomplikowanych modeli poprzez serię powiązanych operacji, w których każdy nowy obiekt czerpie swoje cechy z poprzedniego, wprowadzając jednocześnie dodatkowe atrybuty.

Na przykład, rozważmy tworzenie obiektu sześciennego za pomocą modelowania parametrycznego. Zaczynasz od podstawowego kształtu 2D w postaci prostokąta o długości l i szerokości w, nazwanego \'płytą\'. Ten szkic definiuje podstawę obiektu sześciennego. Następnie definiujesz operację \'Wyciągnięcia\', określając odległość, na jaką należy wypchnąć lub wciągnąć szkic, aby stworzyć obiekt 3D. W rezultacie powstaje sześcienny obiekt bazujący na kształcie szkicu oraz określonej odległości wyciągnięcia.

![](images/FreeCAD_022_PArametricDesignPlate.png )

Na górnej powierzchni płyty rysujesz okrąg o określonej średnicy d. Następnie używasz tego okręgu do stworzenia kieszeni (usunięcia materiału) z oryginalnej płyty.

![](images/FreeCAD_022_ParametricDesignPocket.png )

Jeśli zdecydujesz się zmienić którykolwiek z wymiarów płyty lub okręgu, ostateczny obiekt również zostanie zmodyfikowany. Dzięki zastosowaniu podejścia parametrycznego nie ma potrzeby tworzenia obiektu od nowa.

1.  Przeliczanie nie zawsze odbywa się automatycznie. Ciężkie operacje, które mogą zmodyfikować dużą część dokumentu, a zatem zająć trochę czasu, nie są wykonywane automatycznie. Zamiast tego obiekt *(i wszystkie obiekty, które od niego zależą)* zostaną oznaczone do ponownego obliczenia *(w widoku drzewa pojawi się na nich mała niebieska ikona)*. Następnie należy nacisnąć przycisk ponownego obliczania *(lub **Edycja->Odśwież**)*, aby ponownie przeliczyć wszystkie zaznaczone obiekty.
2.  Drzewo zależności musi zawsze płynąć w tym samym kierunku. Pętle są zabronione. *(Zobacz [DAG](Glossary#Directed_Acyclic_Graph.md) i [Widok DAG](DAG_view/pl.md))* Możesz mieć obiekt A, który zależy od obiektu B, który zależy od obiektu C. Ale nie możesz mieć obiektu A, który zależy od obiektu B, który zależy od obiektu A. To byłaby zależność kołowa. Można jednak mieć wiele obiektów, które zależą od tego samego obiektu, na przykład obiekty B i C zależą od A. Menu **Przybory -> Graf zależności** pokazuje diagram zależności, jak na powyższym obrazku. Może on być przydatny do wykrywania problemów.

W procesie modelowania parametrycznego w FreeCAD, analiza drzewa zależności obiektu daje wyraźny wgląd w sekwencyjną budowę i powiązania w obrębie modelu. U podstaw struktury w powyższym przykładzie znajduje się \'Szkic Płyty\', który stanowi podstawę początkowej formy modelu. Następnie stosowana jest operacja \'Wyciągnięcia\', która dodaje materiał do tego podstawowego szkicu, skutkując stworzeniem struktury trójwymiarowej z dwuwymiarowej bazy.

Następnie na nowo utworzonej powierzchni tworzony jest \'Szkic Koła\'. To koło stanowi podstawę dla kolejnej operacji \'Kieszeni\'. Operacja kieszeni strategicznie usuwa materiał ze struktury, zasadniczo wycinając fragment na podstawie szkicu koła. Proces ten, polegający na dodawaniu i następnie usuwaniu materiału, pozwala na bezproblemowe wprowadzanie skomplikowanych geometrii i cech do podstawowego modelu.

Przez ten ciąg operacji --- zaczynając od szkicu bazowego, dodając objętość za pomocą wyciągnięcia, a następnie tworząc szczegółowe cechy z dodatkowymi szkicami i kieszeniami --- ostateczny obiekt nabiera kształtu. Każdy krok w tym łańcuchu zależy od swojego poprzednika, co ilustruje wzajemnie powiązany charakter projektowania parametrycznego we FreeCAD.

![](images/FreeCAD_022_ParametricDesignDependGraph.png )

Nie wszystkie obiekty są parametryczne w FreeCAD. Często geometria importowana z innych plików nie zawiera żadnych parametrów i będzie prostymi, nieparametrycznymi obiektami. Jednak często można je wykorzystać jako bazę lub punkt wyjścia dla nowo utworzonych obiektów parametrycznych, w zależności oczywiście od tego, czego wymaga obiekt parametryczny i jakości zaimportowanej geometrii.

Wszystkie obiekty, parametryczne lub nie, będą jednak miały kilka podstawowych parametrów, takich jak Nazwa, która jest unikalna w dokumencie i nie może być edytowana, Etykieta, która jest nazwą zdefiniowaną przez użytkownika, którą można edytować, oraz [umiejscowienie](Placement/pl.md), które określa jego pozycję w przestrzeni 3D.

Na koniec warto zauważyć, że niestandardowe obiekty parametryczne są obiektami [łatwymi do zaprogramowania w środowisku Python](Scripted_objects/pl.md).

**Więcej informacji:**

-   [Edytor własciwości](Property_editor/pl.md)
-   [Obiekty tworzone skryptami](Scripted_objects/pl.md)
-   [Umiejscowienie](Placement/pl.md)
-   [Graf zależności](Std_DependencyGraph/pl.md)



---
⏵ [documentation index](../README.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > [Tutorials](Category_Tutorials.md) > Manual:Parametric objects/pl
