Summary:	A program for plotting mathematical expressions and data
Summary(de):	GNU-Plotter-Paket
Summary(es):	Paquete para trazar gr�ficos
Summary(fr):	Le programme de tra�age de courbe de GNU
Summary(pl):	Program GNU do robienia wykres�w
Summary(pt_BR):	Pacote para tra�ar gr�ficos
Summary(ru):	��������� ��� ���������� �������� �������������� ��������� � ������
Summary(tr):	Matematiksel g�rselle�tirme paketi
Summary(uk):	�������� ��� �������� ���Ʀ˦� ������������ ����ڦ� �� �����
Name:		gnuplot
Version:	3.8j.0
Release:	2
License:	GPL
Group:		Applications/Math
Source0:	http://dl.sourceforge.net/gnuplot/%{name}-%{version}.tar.gz
# Source0-md5:	929e210e2d6585d34b029fa59d39915f
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-info.patch
Patch1:		%{name}-info_install.patch
Patch2:		%{name}-no_lisp.patch
URL:		http://gnuplot.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libtool
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
Este es el paquete GNU de ploteado. Se puede usar para crear gr�ficos
en X Window o para archivo.

%description -l fr
Paquetage de trac� de GNU. Il peut �tre utilis� pour faire des graphes
de donn�es dans une fen�tre X ou vers un fichier.

%description -l pl
GNU plot rysuje wykresy, kt�re mo�na drukowa�, zapisywa� w pliku albo
ogl�da� w okienku X.

%description -l pt_BR
Este � o pacote GNU de plotagem. Pode ser usado para gerar gr�ficos em
X Window ou para arquivo.

%description -l ru
Gnuplot - ��� ������������� ��������� ���������� ��������, �����������
� ��������� ������. Gnuplot �������� ������ �������� ��� �����������
������� ������ � ����� ����������� ��� ����������� ������� � ������ �
2-� � 3-� ���������� � �� ������ ��������� ��������.

%description -l tr
Gnuplot, bir fonksiyonun ya da bir veri k�mesinin grafi�inin elde
edilmesinde kullan�lan, �ok yetenekli bir g�rselle�tirme arac�d�r.

%description -l uk
Gnuplot - �� ������������ �������� �������� ���Ʀ˦�, ��� ���դ���� �
���������� �����. Gnuplot �������� ����� Ц������� ��� ��������æ�
�������� ����� �� ���� ��������������� ��� צ���������� ����æ� ��
����� � 2-� �� 3-� ��ͦ��� �� � �������� Ҧ���� ��������.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}

%configure \
	--with-readline=gnu \
	--with-png \
	--without-gd \
	--with-x \
	--without-lisp-files \
	--without-linux-vga \
	--without-tutorial

# The source tarball incorrectly includes a file that should not be there.
rm -f src/getcolor_x11.*

%{__make}
cd docs
makeinfo gnuplot.texi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_infodir},%{_applnkdir}/Scientific/Plotting} \
	$RPM_BUILD_ROOT%{_pixmapsdir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Scientific/Plotting
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/%{name}
%{_mandir}/man1/*
%{_datadir}/%{name}
%{_infodir}/gnuplot*
%{_applnkdir}/Scientific/Plotting/*
%{_pixmapsdir}/*
