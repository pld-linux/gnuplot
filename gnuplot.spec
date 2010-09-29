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
Version:	4.4.2
Release:	1
License:	distributable (with modifications properly marked if any)
Group:		Applications/Math
Source0:	http://downloads.sourceforge.net/gnuplot/%{name}-%{version}.tar.gz
# Source0-md5:	a4f0dd89f9b9334890464f687ddd9f50
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-info.patch
Patch1:		%{name}-info_install.patch
Patch2:		%{name}-lua.patch
Patch3:		%{name}-wx-config.patch
Patch4:		%{name}-4.4.1-mp.patch
URL:		http://gnuplot.sourceforge.net/
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	cairo-devel
BuildRequires:	gd-devel
BuildRequires:	glib2-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libtool
BuildRequires:	lua51-devel
BuildRequires:	ncurses-devel
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	texinfo
BuildRequires:	texlive
BuildRequires:	texlive-format-pdflatex
BuildRequires:	texlive-latex
BuildRequires:	wxGTK2-unicode-devel
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
Summary:	LaTeX files
Group:		Applications/Publishing/TeX

%description latex
LaTeX files.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p0
%patch4 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}

%configure \
	--with-readline=gnu \
	--enable-history-file \
	--with-png \
	--with-gd \
	--with-x \
	--without-lisp-files \
	--without-linux-vga \
	%{!?with_pdf:--without-pdf} \
	--without-tutorial

# The source tarball incorrectly includes a file that should not be there.
rm -f src/getcolor_x11.*

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

mv $RPM_BUILD_ROOT%{_datadir}/texmf{,-dist}

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
