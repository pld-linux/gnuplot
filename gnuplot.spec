Summary:     GNU plotting package
Summary(de): GNU-Plotter-Paket
Summary(fr): Le programme de traçage de courbe de GNU.
Summary(pl): GNU program do robienia wykresów
Summary(tr): Matematiksel görselleþtirme paketi
Name:        gnuplot
Version:     3.7
Release:     1
Copyright:   GPL
Group:       Applications/Math
Group(pl):   Aplikacje/Matematyczne
Source:      ftp://ftp.gnuplot.vt.edu/pub/gnuplot/%{name}-%{version}.tar.gz
URL:         http://www.geocities.com/SiliconValley/Foothills/6647/
BuildRoot:   /tmp/%{name}-%{version}-%{release}-root

%description
This is the GNU plotting package.  It can be used to graph
data in an X window or to a file.

%description -l de
Das GNU-Plotting-Paket. Dient zur grafischen Ausgabe von Daten in 
einem X-Fenster oder in eine Datei. 

%description -l fr
Paquetage de tracé de GNU. Il peut être utilisé pour faire des graphes
de données dans une fenêtre X ou vers un fichier.

%description -l pl
GNU plot rysuje wykresy, które mo¿na drukowaæ, zapisywaæ w pliku albo
ogl±daæ w okienku X.

%description -l tr
Gnuplot, bir fonksiyonun ya da bir veri kümesinin grafiðinin elde edilmesinde
kullanýlan, çok yetenekli bir görselleþtirme aracýdýr.

%prep
%setup -q 

%build
CFLAGS="$RPM_OPT_FLAGS" \
./configure %{_target} \
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
* Sun Jan 24 1999 Artur Frysiak <wiget@usa.net>
  [3.7-1]
- changed Sources address
- changed URL address

* Sat Oct 17 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
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
