# Debian Unstable/pl
[Debian Unstable](https://wiki.debian.org/DebianUnstable) jest dystrybucją rozwijaną, używaną dla [rozwoju dystrybucji Debian](Debian_development/pl.md) i zalecaną dla zaawansowanych użytkowników w rozwijaniu i pakietowaniu programów FreeCAD. Nowe pakiety są gotowe jak tylko zostaną przesłane i zbudowane, chyba, że przesyłający oznaczył je jako [Debian Experimental](https://wiki.debian.org/DebianExperimental), co wymaga wyraźnej instalacji *(po pewnych ustawieniach, aby włączyć dodatkową dystrybucję)* poprzez .

Często osoby używające dystrybucji Debiana Testing powinny używać Debiana Unstable. Debian Testing powinien być traktowany tylko jako \"kieszeń wydania QA\", ponieważ, choć może się wydawać bardziej stabilny niż Unstable, to w rzeczywistości ma pewną wadę. Nowe pakiety są wysyłane do Debian Unstable i migrują do Testing po pewnym czasie, więc poprawki bezpieczeństwa i ważne zmiany w pakietach mogą być niepotrzebnie opóźnione.

Istnieją dwie kluczowe rzeczy dla uzyskania dobrego doświadczenia użytkownika w systemie Unstable. Pierwszą z nich jest to, aby nigdy nie uruchamiać sudo apt full-upgrade lub jego odpowiedników bez uprzedniego sprawdzenia wyników operacji. Jeśli jest napisane, że zwolnisz setki MB miejsca, to znaczy, że trwa zmiana pakietów, która usunie sporą część twojego systemu. Zamiast tego, można bezpiecznie uruchomić sudo apt upgrade i pobrać nowe pakiety. Czasami spowoduje to, że pakiety będą wstrzymane, co oznacza, że może być właściwe uruchomienie full-upgrade, ponieważ deinstalacja pakietów może być rzeczywiście konieczna.

Drugim kluczem jest zrozumienie, że bierzesz udział w rozwoju Debiana i używanie odpowiednich narzędzi i metod. Na przykład, może to oznaczać instalację pakietów takich jak apt-listbugs lub apt-listchanges lub zapisanie się na listy dyskusyjne Debiana, takie jak [debian-devel-announce\@lists.debian.org](https://lists.debian.org/debian-devel-announce/).

Debian Unstable doskonale nadaje się do codziennego użytku przez dłuższy czas, ale można go też łatwo uruchomić w maszynie wirtualnej, gdzie awarie nie będą aż tak wielkim problemem. Wystarczy pobrać ISO testowego Debiana, zainstalować go w maszynie wirtualnej i zaktualizować, a następnie edytować /etc/apt/sources.list, aby zawierał coś takiego:

deb [http://ftp.us.debian.org/debian/](http://ftp.us.debian.org/debian/) testing main contrib non-free
# deb-src [http://ftp.us.debian.org/debian/](http://ftp.us.debian.org/debian/) testing main contrib non-free
deb [http://security.debian.org/debian-security](http://security.debian.org/debian-security) testing/updates main contrib non-free
# deb-src [http://security.debian.org/debian-security](http://security.debian.org/debian-security) testing/updates main contrib non-free
deb [http://ftp.us.debian.org/debian/](http://ftp.us.debian.org/debian/) unstable main contrib non-free
# deb-src [http://ftp.us.debian.org/debian/](http://ftp.us.debian.org/debian/) unstable main contrib non-free

Jeśli chcesz włączyć pakiety z wersji Experimental, umieść poniższe linie w pliku konfiguracyjnym /etc/apt/sources.list.d/experimental.list:

deb [http://deb.debian.org/debian](http://deb.debian.org/debian) experimental main contrib non-free
# deb-src [http://deb.debian.org/debian](http://deb.debian.org/debian) experimental main contrib non-free




[Category:Packaging](Category:Packaging.md) [Category:Developer Documentation](Category:Developer_Documentation.md)

---
[documentation index](../README.md) > [Packaging](Category:Packaging.md) > Debian Unstable/pl
