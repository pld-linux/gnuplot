Summary:     GNU plotting package
Summary(de): GNU-Plotter-Paket
Summary(fr): Le programme de tra�age de courbe de GNU.
Summary(pl): GNU program do robienia wykres�w
Summary(tr): Matematiksel g�rselle�tirme paketi
Name:        gnuplot
%define vermain	3.6
%define versub	beta347
Version:     %{vermain}%{versub}
Release:     1
Copyright:   GPL
Group:       Applications/Math
Source:      ftp://cmpc1.phys.soton.ac.uk/pub/%{name}-%{versub}.tar.gz
URL:         http://www.nas.nasa.gov/~woo/gnuplot/beta/
BuildRoot:   /tmp/%{name}-%{version}-root

%description
This is the GNU plotting package.  It can be used to graph
data in an X window or to a file.

%description -l de
Das GNU-Plotting-Paket. Dient zur grafischen Ausgabe von Daten in 
einem X-Fenster oder in eine Datei. 

%description -l fr
Paquetage de trac� de GNU. Il peut �tre utilis� pour faire des graphes
de donn�es dans une fen�tre X ou vers un fichier.

%description -l pl
GNU plot rysuje wykresy, kt�re mo�na drukowa�, zapisywa� w pliku albo
ogl�da� w okienku X.

%description -l tr
Gnuplot, bir fonksiyonun ya da bir veri k�mesinin grafi�inin elde edilmesinde
kullan�lan, �ok yetenekli bir g�rselle�tirme arac�d�r.

%prep
%setup -q -n %{name}

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure \
	--prefix=/usr \
	--with-gnu-readline \
	--with-png
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{bin,share,man/man1}

install -s gnuplot gnuplot_x11 $RPM_BUILD_ROOT/usr/bin
install docs/gnuplot.1 $RPM_BUILD_ROOT/usr/man/man1
install docs/gnuplot.gih $RPM_BUILD_ROOT/usr/share

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%attr(755, root, root) /usr/bin/*
%attr(644, root,  man) /usr/man/man1/*
/usr/share/gnuplot.gih

%changelog
* Sat Oct 17 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.6beta347-2]
- changed way pass $RPM_OPT_FLAGS (as a configure eviroment variable).

* Mon Sep 28 1998 Marcin 'Qrczak' Kowalczyk <qrczak@knm.org.pl>
  [3.6beta347-1]
- changed Version / Release numbering scheme,
- use %{name} and %{version} macros,
- `mkdir -p' replaced with more standard `install -d',
- added full %attr description in %files,
- removed unnecessary empty /usr/share/gnuplot directory,
- added pl translation,
- fixed using $RPM_OPT_FLAGS.

* Fri Sep 11 1998 Jeff Johnson <jbj@redhat.com>
- update to 2.6beta347

* Sat Aug 15 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Oct 20 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
