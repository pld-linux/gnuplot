Summary:     	GNU plotting package
Summary(de): 	GNU-Plotter-Paket
Summary(fr): 	Le programme de tra�age de courbe de GNU.
Summary(pl): 	GNU program do robienia wykres�w
Summary(tr): 	Matematiksel g�rselle�tirme paketi
Name:        	gnuplot
Version:     	3.7.0.8
Release:     	1
Copyright:   	GPL
Group:       	Applications/Math
Group(pl):   	Aplikacje/Matematyczne
Source:      	ftp://ftp.gnuplot.vt.edu/pub/gnuplot/beta/%{name}-%{version}.tar.gz
Patch0:		gnuplot-DESTDIR.patch
Patch1:		gnuplot-png.patch
URL:         	http://www.geocities.com/SiliconValley/Foothills/6647/
BuildRequires:	readline-devel
BuildRequires:	libpng-devel
BuildRequires:	XFree86-devel
BuildRequires:	gd-devel
BuildRequires:	svgalib-devel
BuildRequires:	zlib-devel
BuildRequires:	ncurses-devel
#BuildRequires:	xemacs-lisp-programming
#or --without-lisp-files
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_datadir	%{_prefix}/share/misc

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
%setup -q 
%patch0 -p1
%patch1 -p1

%build
automake
LDFLAGS="-s"; export LDFLAGS
%configure \
	--with-gnu-readline \
	--with-png \
	--with-gd \
	--with-x \
	--without-lisp-files \
	--without-tutorial

make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

gzip -9fn $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/gnuplot.gih
