%define name wmdf
%define version 0.1.6
%define release  9

Summary:	An app to monitor disk IO and available space on partitions
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Graphical desktop/WindowMaker
Source0:	%{name}-%{version}.tar.bz2
Source10:	%{name}-16x16.png
Source11:	%{name}-32x32.png
Source12:	%{name}-48x48.png
URL:		https://www.dockapps.com/file.php/id/175
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(xext)


%description
An app to monitor disk usage,the app makes use of the OS filesystem info
and partition info functions so is very low on the CPU usage scale. It
allows you to toggle the mount point with scrolling information about the
disk usage and free space etc.

%prep
%setup -q

%build
%configure
%make

%install
[ -d %buildroot ] && rm -rf %buildroot

%makeinstall

install -m 755 -d %buildroot%{_miconsdir}
install -m 755 -d %buildroot%{_iconsdir}
install -m 755 -d %buildroot%{_liconsdir}
install -m 644 %SOURCE10 %buildroot%{_miconsdir}/%{name}.png
install -m 644 %SOURCE11 %buildroot%{_iconsdir}/%{name}.png
install -m 644 %SOURCE12 %buildroot%{_liconsdir}/%{name}.png


install -m 755 -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=WmDf
Comment=An app to monitor disk IO and available space on partitions
Exec=%{_bindir}/%{name} -at 99 -bl
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-System-Monitoring;System;Monitor;
EOF


# This is commented as we don't need it
#mv %buildroot/usr/bin/i586-mandrake-linux-gnu-wmdf    %buildroot%prefix/bin/wmdf
#mv %buildroot//usr/share/man/man1/i586-mandrake-linux-gnu-wmdf.1 %buildroot%_mandir/man1/wmdf.1

%clean
[ -z %buildroot ] || {
    rm -rf %buildroot
}


%if %mdkversion < 200900
%post
%{update_menus}
%endif


%if %mdkversion < 200900
%postun
%{clean_menus}
%endif


%files
%defattr (-,root,root)
%doc AUTHORS COPYING README THANKS TODO ChangeLog
%{_bindir}/*
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop
%{_mandir}/man1/*




%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.1.6-7mdv2010.0
+ Revision: 434814
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.1.6-6mdv2009.0
+ Revision: 262032
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.1.6-5mdv2009.0
+ Revision: 256134
- rebuild
- drop old menu

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.1.6-3mdv2008.1
+ Revision: 129395
- kill re-definition of %%buildroot on Pixel's request
- kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'


* Tue Feb 06 2007 Gustavo De Nardin <gustavodn@mandriva.com> 0.1.6-3mdv2007.0
+ Revision: 116916
- fixed .desktop file Comment
- fixed and trimmed dependencies
- spec cleanup
- fixed old menu section
- xdg menu migration for great compliance

* Sat Jul 23 2005 Nicolas L�cureuil <neoclust@mandriva.org> 0.1.6-1mdk
- New release 0.1.6

* Fri Jun 03 2005 Nicolas L�cureuil <neoclust@mandriva.org> 0.1.5-3mdk
- Rebuild

