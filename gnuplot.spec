Summary:	A program for plotting mathematical expressions and data
Summary(de):	GNU-Plotter-Paket
Summary(es):	Paquete para trazar gráficos
Summary(fr):	Le programme de traçage de courbe de GNU
Summary(pl):	Program GNU do robienia wykresów
Summary(pt_BR):	Pacote para traçar gráficos
Summary(tr):	Matematiksel görselleþtirme paketi
Name:		gnuplot
Version:	3.7.1
Release:	15
License:	GPL
Group:		Applications/Math
Group(de):	Applikationen/Mathematik
Group(pl):	Aplikacje/Matematyczne
Source0:	http://prdownloads.sourceforge.net/gnuplot/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-info.patch
Patch2:		%{name}-acfix.patch
URL:		http://gnuplot.sourceforge.net/
BuildRequires:	readline-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	XFree86-devel
BuildRequires:	zlib-devel
BuildRequires:	ncurses-devel
BuildRequires:	autoconf
BuildRequires:	automake
#BuildRequires:	xemacs-lisp-programming
#or --without-lisp-files
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_datadir	%{_prefix}/share/misc

%description
Gnuplot is a command-line driven, interactive function plotting
program especially suited for scientific data representation. Gnuplot
can be used to plot functions and data points in both two and three
dimensions and in many different formats.

%description -l de
Das GNU-Plotting-Paket. Dient zur grafischen Ausgabe von Daten in
einem X-Fenster oder in eine Datei.

%description -l es
Este es el paquete GNU de ploteado. Se puede usar para crear gráficos
en X Window o para archivo.

%description -l fr
Paquetage de tracé de GNU. Il peut être utilisé pour faire des graphes
de données dans une fenêtre X ou vers un fichier.

%description -l pl
GNU plot rysuje wykresy, które mo¿na drukowaæ, zapisywaæ w pliku albo
ogl±daæ w okienku X.

%description -l pt_BR
Este é o pacote GNU de plotagem. Pode ser usado para gerar gráficos em
X Window ou para arquivo.

%description -l tr
Gnuplot, bir fonksiyonun ya da bir veri kümesinin grafiðinin elde
edilmesinde kullanýlan, çok yetenekli bir görselleþtirme aracýdýr.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
aclocal -I m4
autoconf
autoheader

%configure \
	--with-readline=gnu \
	--with-png \
	--without-gd \
	--with-x \
	--without-lisp-files \
	--without-linux-vga \
	--without-tutorial

%{__make}
(cd docs; makeinfo gnuplot.texi)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_infodir}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install docs/gnuplot.info* $RPM_BUILD_ROOT%{_infodir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/gnuplot.gih
%{_infodir}/gnuplot*
