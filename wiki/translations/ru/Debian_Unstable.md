# Debian Unstable/ru
[Debian Unstable](https://wiki.debian.org/DebianUnstable) is a rolling distribution used for [Debian development](Debian_development.md) and recommended for advanced users in FreeCAD development and packaging. New packages are ready as soon as they are uploaded and built, unless the uploader has marked them for [Debian Experimental](https://wiki.debian.org/DebianExperimental) which requires explicit installation (after some setup to enable the extra distribution) via .

Часто люди, использующие тестирование Debian, на самом деле должны использовать нестабильный Debian; Тестирование Debian следует рассматривать только как \"QA release pocket\", поскольку, хотя оно может показаться более стабильным, чем нестабильным, на самом деле есть недостаток. Новые пакеты загружаются в нестабильный Debian и через некоторое время переходят на тестирование, поэтому исправления безопасности и важные изменения в упаковке могут быть ненадлежащим образом отложены.

There are two key things to a good user experience in Unstable. The first is to never blindly run sudo apt full-upgrade or its equivalents without first checking the results of the operation. If it\'s saying you\'ll free up hundreds of MB of space, there\'s a package transition underway which will remove a good portion of your system. Instead, one can safely run sudo apt upgrade and get new packages. Sometimes, this will result in packages being held back, which means it may be appropriate to run full-upgrade as package uninstallation may actually be necessary.

The second key is to embrace that you\'re taking part in Debian development, and use the appropriate tools and methods. For example, that may mean installing packages like apt-listbugs or apt-listchanges or subscribing to Debian mailing lists like [debian-devel-announce@lists.debian.org](https://lists.debian.org/debian-devel-announce/).

While Debian Unstable is perfectly suitable as a long-term daily driver, it\'s also very easy to run in a virtual machine, where breakages won\'t be such a big deal. Simply download a Debian Testing ISO, install it into a VM and update it, and then edit /etc/apt/sources.list to contain something like:

deb [http://ftp.us.debian.org/debian/](http://ftp.us.debian.org/debian/) testing main contrib non-free
# deb-src [http://ftp.us.debian.org/debian/](http://ftp.us.debian.org/debian/) testing main contrib non-free
deb [http://security.debian.org/debian-security](http://security.debian.org/debian-security) testing/updates main contrib non-free
# deb-src [http://security.debian.org/debian-security](http://security.debian.org/debian-security) testing/updates main contrib non-free
deb [http://ftp.us.debian.org/debian/](http://ftp.us.debian.org/debian/) unstable main contrib non-free
# deb-src [http://ftp.us.debian.org/debian/](http://ftp.us.debian.org/debian/) unstable main contrib non-free

If you want to enable packages from Experimental, put this into /etc/apt/sources.list.d/experimental.list:

deb [http://deb.debian.org/debian](http://deb.debian.org/debian) experimental main contrib non-free
# deb-src [http://deb.debian.org/debian](http://deb.debian.org/debian) experimental main contrib non-free



---
![](images/Button_right.svg) [documentation index](../README.md) > [Packaging](Category_Packaging.md) > [Developer Documentation](Category_Developer Documentation.md) > Debian Unstable/ru
