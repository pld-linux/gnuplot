#
# Conditional build:
%bcond_with	ggi	# GGI driver
%bcond_with	ggixmi	# GGI XMI support for pm3d
%bcond_with	pdf	# PDF terminal (based on PDFLib)
%bcond_with	qt	# build Qt terminal
%bcond_with	svga	# Linux SVGA console driver
#
Summary:	A program for plotting mathematical expressions and data
Summary(de.UTF-8):	GNU-Plotter-Paket
Summary(es.UTF-8):	Paquete para trazar gráficos
Summary(fr.UTF-8):	Le programme de traçage de courbe de GNU
Summary(hu.UTF-8):	Matematikai függvények és adatok ábrázolása
Summary(pl.UTF-8):	Program GNU do robienia wykresów
Summary(pt_BR.UTF-8):	Pacote para traçar gráficos
Summary(ru.UTF-8):	Программа для построения графиков математических выражений и данных
Summary(tr.UTF-8):	Matematiksel görselleştirme paketi
Summary(uk.UTF-8):	Програма для побудови графіків математичних виразів та даних
Name:		gnuplot
Version:	4.6.3
Release:	2
License:	distributable (with modifications properly marked if any)
Group:		Applications/Math
Source0:	http://downloads.sourceforge.net/gnuplot/%{name}-%{version}.tar.gz
# Source0-md5:	db7a73d2dddec0149dcec35e30561aa3
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-info.patch
Patch1:		%{name}-info_install.patch
Patch2:		%{name}-lua.patch
Patch3:		%{name}-wx-config.patch
URL:		http://gnuplot.sourceforge.net/
%if %{with qt}
BuildRequires:	QtCore-devel >= 4.5
BuildRequires:	QtGui-devel >= 4.5
BuildRequires:	QtNetwork-devel >= 4.5
BuildRequires:	QtSvg-devel >= 4.5
BuildRequires:	qt4-build >= 4.5
BuildRequires:	qt4-linguist >= 4.5
%endif
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.7.9
BuildRequires:	cairo-devel >= 1.6
BuildRequires:	gd-devel >= 2.0
BuildRequires:	glib2-devel
BuildRequires:	gtk+2-devel >= 2:2.8.0
%{?with_ggi:BuildRequires:	libggi-devel}
# ???
%{?with_ggixmi:BuildRequires:	libggi-xmi-devel}
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libtool
BuildRequires:	lua51-devel
BuildRequires:	ncurses-devel
BuildRequires:	pango-devel > 1:1.10.2
# which version? it needs PDF_create_gstate,PDF_set_gstate symbols
%{?with_pdf:BuildRequires:	pdflib-devel > 4.0.2}
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
# libvga, libvgagl, lib3dkit
%{?with_svga:BuildRequires:	svgalib-devel}
BuildRequires:	texinfo
BuildRequires:	texlive
BuildRequires:	texlive-format-pdflatex
BuildRequires:	texlive-latex
BuildRequires:	wxGTK2-unicode-devel >= 2.6
#BuildRequires:	xemacs-lisp-programming
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	zlib-devel
#or --without-lisp-files
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnuplot is a command-line driven, interactive function plotting
program especially suited for scientific data representation. Gnuplot
can be used to plot functions and data points in both two and three
dimensions and in many different formats.

%description -l de.UTF-8
Das GNU-Plotting-Paket. Dient zur grafischen Ausgabe von Daten in
einem X-Fenster oder in eine Datei.

%description -l es.UTF-8
Este es el paquete GNU de ploteado. Se puede usar para crear gráficos
en X Window o para archivo.

%description -l fr.UTF-8
Paquetage de tracé de GNU. Il peut être utilisé pour faire des graphes
de données dans une fenêtre X ou vers un fichier.

%description -l hu.UTF-8
Gnuplot egy parancssor-vezérelt, interaktív függvényábrázoló program,
amely különösen alkalmas tudományos adatok megjelenítésére. A Gnuplot
alkalmas függvények és adathalmazok ábrázolására, kettő és három
dimenzióban, különféle formátumokban.

%description -l pl.UTF-8
GNU plot rysuje wykresy, które można drukować, zapisywać w pliku albo
oglądać w okienku X.

%description -l pt_BR.UTF-8
Este é o pacote GNU de plotagem. Pode ser usado para gerar gráficos em
X Window ou para arquivo.

%description -l ru.UTF-8
Gnuplot - это интерактивная программа построения графиков, управляемая
с командной строки. Gnuplot особенно хорошо подходит для презентации
научных данных и может применяться для отображения функций и данных в
2-х и 3-х измерениях и во многих различных форматах.

%description -l tr.UTF-8
Gnuplot, bir fonksiyonun ya da bir veri kümesinin grafiğinin elde
edilmesinde kullanılan, çok yetenekli bir görselleştirme aracıdır.

%description -l uk.UTF-8
Gnuplot - це інтерактивна програма побудови графіків, яка керується з
командного рядка. Gnuplot особливо гарно підходить для презентації
наукових даних та може застосовуватись для відображення функцій та
даних в 2-х та 3-х вимірах та в багатьох різних форматах.

%package latex
Summary:	gnuplot support for LaTeX
Summary(pl.UTF-8):	Obsługa gnuplota dla LaTeXa
Group:		Applications/Publishing/TeX
# which subpackages? required tex packages: tikz,xxcolor,ifpdf,ifxetex
Requires:	texlive

%description latex
gnuplot support for LaTeX.

%description latex -l pl.UTF-8
Obsługa gnuplota dla LaTeXa.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p0

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}

%configure \
	--enable-history-file \
	%{?with_qt:--enable-qt} \
	%{?with_ggi:--with-ggi} \
	%{?with_svga:--with-linux-vga} \
	--with-readline=gnu \
	--with-png \
	--with-gd \
	--with-x \
	%{?with_ggixmi:--with-xmi} \
	--without-lisp-files \
	--without-linux-vga \
	%{!?with_pdf:--without-pdf} \
	--without-tutorial \
	--with-texdir=%{_datadir}/texmf-dist/tex/latex/gnuplot

%{__make}
cd docs
makeinfo gnuplot.texi
cd ..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_infodir},%{_desktopdir},%{_pixmapsdir}}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	appdefaultdir=%{_datadir}/X11/app-defaults

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc docs/psdoc/ps_guide.ps
%attr(755,root,root) %{_bindir}/gnuplot
%attr(755,root,root) %{_libdir}/%{name}
%{_mandir}/man1/gnuplot.1*
%{_datadir}/%{name}
%{_infodir}/gnuplot.info*
%{_desktopdir}/gnuplot.desktop
%{_pixmapsdir}/gnuplot.png
%{_datadir}/X11/app-defaults/Gnuplot

%files latex
%defattr(644,root,root,755)
%{_datadir}/texmf-dist/tex/latex/gnuplot
