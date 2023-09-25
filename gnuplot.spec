#
# Conditional build:
%bcond_without	emacs	# Emacs for info documentation
%bcond_without	caca	# CACA driver
%bcond_with	ggi	# GGI driver
%bcond_with	ggixmi	# GGI XMI support for pm3d
%bcond_with	qt	# Qt terminal
%bcond_with	qt4	# use Qt 4 instead of Qt 5
%bcond_with	svga	# Linux SVGA console driver
%bcond_without	wxwidgets	# wxWidgets terminal
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
Version:	5.2.8
Release:	2
License:	distributable (with modifications properly marked if any)
Group:		Applications/Math
Source0:	http://downloads.sourceforge.net/gnuplot/%{name}-%{version}.tar.gz
# Source0-md5:	2df8767c7399bee57a96296d46b4d5fb
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-info.patch
URL:		http://gnuplot.sourceforge.net/
%if %{with qt}
%if %{with qt4}
BuildRequires:	QtCore-devel >= 4.5
BuildRequires:	QtGui-devel >= 4.5
BuildRequires:	QtNetwork-devel >= 4.5
BuildRequires:	QtSvg-devel >= 4.5
BuildRequires:	qt4-build >= 4.5
BuildRequires:	qt4-linguist >= 4.5
%else
BuildRequires:	Qt5Core-devel >= 5.0
BuildRequires:	Qt5Gui-devel >= 5.0
BuildRequires:	Qt5Network-devel >= 5.0
BuildRequires:	Qt5PrintSupport-devel >= 5.0
BuildRequires:	Qt5Svg-devel >= 5.0
BuildRequires:	Qt5Widgets-devel >= 5.0
BuildRequires:	qt5-build >= 5.0
BuildRequires:	qt5-linguist >= 5.0
%endif
%endif
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.10
BuildRequires:	cairo-devel >= 1.6
%if %{with emacs}
BuildRequires:	xemacs
BuildRequires:	xemacs-texinfo-pkg
%endif
BuildRequires:	gd-devel >= 2.0
BuildRequires:	glib2-devel >= 1:2.28
BuildRequires:	gtk+3-devel
%{?with_caca:BuildRequires:	libcaca-devel >= 0.99-0.beta15}
BuildRequires:	libcerf-devel
%{?with_ggi:BuildRequires:	libggi-devel}
# ???
%{?with_ggixmi:BuildRequires:	libggi-xmi-devel}
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	lua53 >= 5.3
BuildRequires:	lua53-devel >= 5.3
BuildRequires:	ncurses-devel
BuildRequires:	pango-devel > 1:1.22
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
# libvga, libvgagl, lib3dkit
%{?with_svga:BuildRequires:	svgalib-devel}
BuildRequires:	texinfo
BuildRequires:	texlive
BuildRequires:	texlive-format-pdflatex
BuildRequires:	texlive-latex
%{?with_wxwidgets:BuildRequires:	wxGTK3-unicode-devel >= 2.6}
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	zlib-devel
Requires:	cairo >= 1.6
Requires:	glib2 >= 1:2.28
%{?with_caca:Requires:	libcaca >= 0.99-0.beta15}
Requires:	pango > 1:1.22
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

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}

%configure \
	WX_CONFIG=/usr/bin/wx-gtk3-unicode-config \
	--enable-history-file \
	%{!?with_wxwidgets:--disable-wxwidgets} \
	%{?with_caca:--with-caca} \
	--with-gd \
	%{?with_ggi:--with-ggi} \
	%{?with_svga:--with-linux-vga} \
	--with-qt=%{?with_qt:%{?with_qt4:qt4}%{!?with_qt4:qt5}}%{!?with_qt:no} \
	--with-readline=gnu \
	--with-texdir=%{_datadir}/texmf-dist/tex/latex/gnuplot \
	--without-tutorial \
	--with-x \
	%{?with_ggixmi:--with-xmi}

%{__make}

%if %{with emacs}
%{__make} -C docs info
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install %{?with_emacs:install-info} \
	DESTDIR=$RPM_BUILD_ROOT \
	appdefaultdir=%{_datadir}/X11/app-defaults

install -d $RPM_BUILD_ROOT%{_mandir}/ja/man1
%{__mv} $RPM_BUILD_ROOT%{_mandir}/man1/gnuplot-ja.1 $RPM_BUILD_ROOT%{_mandir}/ja/man1/gnuplot.1

[ ! -f $RPM_BUILD_ROOT%{_desktopdir}/gnuplot.desktop ]
[ ! -f $RPM_BUILD_ROOT%{_pixmapsdir}/gnuplot.png ]
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with emacs}
%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}
%endif

%files
%defattr(644,root,root,755)
%doc BUGS ChangeLog Copyright FAQ.pdf NEWS README RELEASE_NOTES TODO docs/psdoc/ps_guide.ps
%attr(755,root,root) %{_bindir}/gnuplot
%dir %{_libexecdir}/%{name}
%dir %{_libexecdir}/%{name}/5.2
%{?with_qt:%attr(755,root,root) %{_libexecdir}/%{name}/5.2/gnuplot_qt}
%attr(755,root,root) %{_libexecdir}/%{name}/5.2/gnuplot_x11
%{_mandir}/man1/gnuplot.1*
%lang(ja) %{_mandir}/ja/man1/gnuplot.1*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/5.2
%{_datadir}/%{name}/5.2/PostScript
%{_datadir}/%{name}/5.2/js
%{_datadir}/%{name}/5.2/lua
%{_datadir}/%{name}/5.2/colors_*.gp
%{_datadir}/%{name}/5.2/gnuplot.gih
%{_datadir}/%{name}/5.2/gnuplotrc
%if %{with qt}
%dir %{_datadir}/%{name}/5.2/qt
%lang(fr) %{_datadir}/%{name}/5.2/qt/qtgnuplot_fr.qm
%lang(ja) %{_datadir}/%{name}/5.2/qt/qtgnuplot_ja.qm
%endif
%if %{with emacs}
%{_infodir}/gnuplot.info*
%endif
%{_desktopdir}/gnuplot.desktop
%{_pixmapsdir}/gnuplot.png
%{_datadir}/X11/app-defaults/Gnuplot

%files latex
%defattr(644,root,root,755)
%{_datadir}/texmf-dist/tex/latex/gnuplot
