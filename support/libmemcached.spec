Summary: memcached C library and command line tools
Name: libmemcached
Version: 0.6
Release: 1
License: BSD
Group: System Environment/Libraries
URL: http://tangent.org/552/libmemcached.html

Packager: Jeff Fisher <guppy@techmonkeys.org>

Source: http://download.tangent.org/libmemcached-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
libmemcached is a C client library to the memcached server
(http://danga.com/memcached). It has been designed to be light on memory
usage, and provide full access to server side methods.

It also implements several command line tools:

memcat - Copy the value of a key to standard output
memflush - Flush the contents of your servers.
memrm - Remove a key(s) from the serrver.
memstat - Dump the stats of your servers to standard output
memslap - Generate testing loads on a memcached cluster

%prep
%setup -q

%configure

%build
%{__make} %{_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install  DESTDIR="%{buildroot}" AM_INSTALL_PROGRAM_FLAGS=""

%clean
%{__rm} -rf %{buildroot}

%files
%{_bindir}/memcat
%{_bindir}/memcp
%{_bindir}/memflush
%{_bindir}/memrm
%{_bindir}/memstat
%{_bindir}/memslap
%{_includedir}/libmemcached/memcached.h
%{_libdir}/libmemcached.a
%{_libdir}/libmemcached.la
%{_libdir}/libmemcached.so
%{_libdir}/libmemcached.so.0
%{_libdir}/libmemcached.so.0.0.0
%{_mandir}/man1/memcat.1.gz
%{_mandir}/man1/memcp.1.gz
%{_mandir}/man1/memflush.1.gz
%{_mandir}/man1/memrm.1.gz
%{_mandir}/man1/memslap.1.gz
%{_mandir}/man1/memstat.1.gz
%{_mandir}/man3/libmemcached.3.gz
%{_mandir}/man3/libmemcached_examples.3.gz
%{_mandir}/man3/memcached_add.3.gz
%{_mandir}/man3/memcached_behavior_get.3.gz
%{_mandir}/man3/memcached_behavior_set.3.gz
%{_mandir}/man3/memcached_create.3.gz
%{_mandir}/man3/memcached_decrement.3.gz
%{_mandir}/man3/memcached_delete.3.gz
%{_mandir}/man3/memcached_fetch.3.gz
%{_mandir}/man3/memcached_free.3.gz
%{_mandir}/man3/memcached_get.3.gz
%{_mandir}/man3/memcached_increment.3.gz
%{_mandir}/man3/memcached_mget.3.gz
%{_mandir}/man3/memcached_quit.3.gz
%{_mandir}/man3/memcached_replace.3.gz
%{_mandir}/man3/memcached_server_add.3.gz
%{_mandir}/man3/memcached_server_count.3.gz
%{_mandir}/man3/memcached_server_list.3.gz
%{_mandir}/man3/memcached_server_list_append.3.gz
%{_mandir}/man3/memcached_server_list_count.3.gz
%{_mandir}/man3/memcached_server_list_free.3.gz
%{_mandir}/man3/memcached_server_push.3.gz
%{_mandir}/man3/memcached_servers_parse.3.gz
%{_mandir}/man3/memcached_set.3.gz
%{_mandir}/man3/memcached_stat.3.gz
%{_mandir}/man3/memcached_stat_get_keys.3.gz
%{_mandir}/man3/memcached_stat_get_value.3.gz
%{_mandir}/man3/memcached_stat_servername.3.gz
%{_mandir}/man3/memcached_strerror.3.gz
%{_mandir}/man3/memcached_verbosity.3.gz

%changelog
* Wed Oct  3 2007 Brian Aker <brian@tangent.org> - 0.4-1
- See Changelog

* Mon Oct  1 2007 Brian Aker <brian@tangent.org> - 0.3-1
- Added memslap

* Fri Sep 28 2007 Jeff Fisher <guppy@techmonkeys.org> - 0.2-1
- Initial package
