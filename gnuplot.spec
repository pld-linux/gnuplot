Summary:	A program for plotting mathematical expressions and data
Summary(de):	GNU-Plotter-Paket
Summary(es):	Paquete para trazar grАficos
Summary(fr):	Le programme de traГage de courbe de GNU
Summary(pl):	Program GNU do robienia wykresСw
Summary(pt_BR):	Pacote para traГar grАficos
Summary(ru):	Программа для построения графиков математических выражений и данных
Summary(tr):	Matematiksel gЖrselleЧtirme paketi
Summary(uk):	Програма для побудови граф╕к╕в математичних вираз╕в та даних
Name:		gnuplot
Version:	3.7.2
Release:	4
License:	GPL
Group:		Applications/Math
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/gnuplot/%{name}-%{version}.tar.gz
Patch0:		%{name}-info.patch
Patch1:		%{name}-acfix.patch
Patch2:		%{name}-round.patch
URL:		http://gnuplot.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpng >= 1.0.8
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRequires:	zlib-devel
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
Este es el paquete GNU de ploteado. Se puede usar para crear grАficos
en X Window o para archivo.

%description -l fr
Paquetage de tracИ de GNU. Il peut Йtre utilisИ pour faire des graphes
de donnИes dans une fenЙtre X ou vers un fichier.

%description -l pl
GNU plot rysuje wykresy, ktСre mo©na drukowaФ, zapisywaФ w pliku albo
ogl╠daФ w okienku X.

%description -l pt_BR
Este И o pacote GNU de plotagem. Pode ser usado para gerar grАficos em
X Window ou para arquivo.

%description -l ru
Gnuplot - это интерактивная программа построения графиков, управляемая
с командной строки. Gnuplot особенно хорошо подходит для презентации
научных данных и может применяться для отображения функций и данных в
2-х и 3-х измерениях и во многих различных форматах.

%description -l tr
Gnuplot, bir fonksiyonun ya da bir veri kЭmesinin grafiПinin elde
edilmesinde kullanЩlan, Гok yetenekli bir gЖrselleЧtirme aracЩdЩr.

%description -l uk
Gnuplot - це ╕нтерактивна програма побудови граф╕к╕в, яка керу╓ться з
командного рядка. Gnuplot особливо гарно п╕дходить для презентац╕╖
наукових даних та може застосовуватись для в╕дображення функц╕й та
даних в 2-х та 3-х вим╕рах та в багатьох р╕зних форматах.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}

%configure \
	--with-readline=gnu \
	--with-png \
	--without-gd \
	--with-x \
	--without-lisp-files \
	--without-linux-vga \
	--without-tutorial

%{__make}
cd docs
makeinfo gnuplot.texi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_infodir}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

rm -r $RPM_BUILD_ROOT%{_infodir}/dir*

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
