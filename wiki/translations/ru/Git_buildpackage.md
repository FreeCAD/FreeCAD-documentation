# Git buildpackage/ru



Modern Debian development workflows involve [packaging with Git](https://wiki.debian.org/PackagingWithGit) and the primary tool for doing that is [git-buildpackage](http://honk.sigxcpu.org/projects/git-buildpackage/manual-html/gbp.html). git-buildpackage provides a gbp command with several options similar to the git command itself. Many of these commands are themselves just a wrapper of lower-level Debian tools, so the complexity to learning packaging can be quite high.

To get around that, here are the short & simple steps to getting started with git-buildpackage. This should work on nearly any Debian-based distribution, but I recommend working on this in a clean and separate environment a [Debian Unstable](Debian_Unstable.md) virtual machine.

1.  Install it with sudo apt install git-buildpackage
2.  Grab the dotfiles at the end of this page. You\'ll need: ~/.gbp.conf, ~/.pbuilderrc, and ~/.quiltrc
3.  The package build will occur in a clean environment. Create it with sudo git-pbuilder create
4.  Find the URL of a package you want to build on <https://salsa.debian.org>, the Debian project\'s self-hosted GitLab instance
5.  Create a clone of it with 
6.  Enter the cloned repo\'s directory with cd
7.  Run the build with gbp buildpackage -us -uc
8.  When it\'s finished, your packages will be at ../build-area/.

##### gbp.conf

Расположение: ~/.gbp.conf

<https://gitlab.com/kkremitzki/dotfiles/blob/master/.gbp.conf>

##### pbuilderrc

Расположение: ~/.pbuilderrc

<https://gitlab.com/kkremitzki/dotfiles/blob/master/.pbuilderrc>

##### quiltrc

Расположение: ~/.quiltrc

<https://gitlab.com/kkremitzki/dotfiles/blob/master/.quiltrc>


 

[Category:Packaging](Category:Packaging.md) [Category:Developer Documentation](Category:Developer_Documentation.md)
