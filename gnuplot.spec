Summary:	A program for plotting mathematical expressions and data
Summary(de):	GNU-Plotter-Paket
Summary(fr):	Le programme de traçage de courbe de GNU.
Summary(pl):	GNU program do robienia wykresów
Summary(tr):	Matematiksel görselleþtirme paketi
Name:		gnuplot
Version:	3.7.1
Release:	1
Copyright:	GPL
Group:		Applications/Math
Group(pl):	Aplikacje/Matematyczne
Source:		ftp://ftp.gnuplot.vt.edu/pub/gnuplot/%{name}-%{version}.tar.gz
Patch0:		gnuplot-DESTDIR.patch
Patch1:		gnuplot-info.patch
URL:		http://www.geocities.com/SiliconValley/Foothills/6647/
BuildRequires:	readline-devel
BuildRequires:	libpng-devel
BuildRequires:	XFree86-devel
BuildRequires:	zlib-devel
BuildRequires:	ncurses-devel
#BuildRequires:	xemacs-lisp-programming
#or --without-lisp-files
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr
%define		_datadir	%{_prefix}/share/misc

%description
Gnuplot is a command-line driven, interactive function plotting program
especially suited for scientific data representation. Gnuplot can be used
to plot functions and data points in both two and three dimensions and in
many different formats.

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
%patch0 -p1
%patch1 -p1

%build
aclocal -I m4
autoconf
autoheader

LDFLAGS="-s"; export LDFLAGS
%configure \
	--with-gnu-readline \
	--with-png \
	--without-gd \
	--with-x \
	--without-lisp-files \
	--without-linux-vga \
	--without-tutorial

make
(cd docs; makeinfo gnuplot.texi)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_infodir}

make install DESTDIR=$RPM_BUILD_ROOT

install docs/gnuplot.info* $RPM_BUILD_ROOT%{_infodir}

gzip -9fn $RPM_BUILD_ROOT{%{_mandir}/man1/*,%{_infodir}/*}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ -x /usr/sbin/fix-info-dir ] && /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ -x /usr/sbin/fix-info-dir ] && /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/gnuplot.gih
%{_infodir}/gnuplot*
