# $Id: smeserver-userpanel.spec,v 1.6 2013/12/15 18:09:43 unnilennium Exp $
# Authority: dungog
# Name: Stephen Noble

Summary: Provide a user panel to let users to change delegated server settings.
%define name smeserver-userpanel
Name: %{name}
%define version 1.1
%define release 1
Version: %{version}
Release: %{release}%{?dist}
License: GPL
URL: http://wiki.contribs.org
Group: SMEserver/addon
Source: %{name}-%{version}.tar.gz
BuildArchitectures: noarch
BuildRoot: /var/tmp/%{name}-%{version}
Requires: e-smith-release >= 9
BuildRequires: e-smith-devtools
Obsoletes: e-smith-userpanel
AutoReqProv: no

%description
SME Server enhancement to create a user manager panel where users can
authenticate with their own username/password and change selected
server settings as allowed by admin.
Selected User settings can be altered after installing additional
userpanels available in seperate rpms.
Panels can be delegated at user, group or global levels

%changelog
* Mon Jun 23 2014 stephane de Labrusse <stephdl@de-labrusse.fr> 1.1-1.sme
- Initial release to sme9

* Sun Dec 15 2013 JP Pialasse <tests@pialasse.com>  0.9-16.sme
- move post to an action event [SME: 8032]

* Mon Dec 2 2013  JP Pialasse <tests@pialasse.com>  0.9-13.sme
- reverting language links creation in post as temp fix. see Bugs 8032 and 8022
- final fix will depends on 8032 int he future

* Thu Nov 28 2013 JP Pialasse <tests@pialasse.com>  0.9-12.sme
- NFR: logout button  [SME: 8022]
- NFR: show username [SME: 8025]
- should fix 500 error by adding action in most events [SME: 7667]
- spec file tidying

* Sun Feb 17 2008 Stephen Noble <support@dungog.net> 0.9-11
- remove pleasewait hack [SME: 126] 

* Mon Feb 5 2007 Stephen Noble <support@dungog.net> 0.9-10
- redirect to https [sme 1879]
- Adjust to work on sme 7.1.1 [sme 2419]
- thanks John Bennett

* Mon Oct 30 2006  Stephen Noble <support@dungog.net> 0.9-9
- shorten /user-manager to /user
- delegate rights with a group [sme 1748]

* Sun Oct 29 2006  Stephen Noble <support@dungog.net> 0.9-8
- bugfix for navigation frame

* Sat Oct 28 2006  Stephen Noble <support@dungog.net>
- i18n support for navigation frame [sme 2009]
- [0.9-7]

* Thu Oct 26 2006  Stephen Noble <support@dungog.net>
- german and italian language support [sme 2008]
- [0.9-6]

* Mon Feb 13 2006  Stephen Noble <support@dungog.net>
- remove Provides e-smith-userpanel, for sme7 pre release 2
- [0.9-5]

* Wed Sep 21 2005  Stephen Noble <support@dungog.net>
- for sme7 beta
- [0.9-4]

* Sun Aug 21 2005 Stephen Noble <support@dungog.net>
- perl-Unicode-String dependancy removed
- [0.9-3]

* Wed Aug 10 2005  Stephen Noble <support@dungog.net>
- removed all userpanels, these are in smeserver-userpanel-*
- /home/e-smith/db/accounts relocated
- for sme7 alpha
- [0.9-2]

* Sat Jun 18 2005  Stephen Noble <support@dungog.net>
- renamed rpm smeserver-userpanel
- user admin can be delegated hidden panels in userpanelaccess
- option to use maildrop instead of procmail
- new setting to enable procmail and/or mailfilter
-  db set accounts USER procmail|mailfilter enabled [individually]
-  db set configuration MailFilter service procmail|mailfilter enabled [global[if above unset]]
- [0.9-1]

* Sat Jun 18 2005  Stephen Noble <support@dungog.net>
- Allows for: e-smith-release >= 7.0
- sme7 RequireSSL -> SSLRequireSSL [Gordon Rowell]
- passwords can be stricter [Lorenzo Fascì]
-  sme6 /sbin/e-smith/db configuration setprop passwordstrength User none|normal|strong
-  sme7 /sbin/e-smith/db configuration setprop passwordstrength Users none|normal|strong
- merged dungog-useraccounts, new function userpanel-useraccounts
-  http://www.dungog.net/sme/changelog/useraccounts.txt
-  delegated user account creation with limits
- sme5 manager.css added
- 26autoreply altered to leave autoreplied email in the inbox
- sme7 IMAP changed from /;junkmail to /.junkmail, check all your procmail rules !!
- perl-Unicode-IMAPUtf7 dependancy/support removed
- [1.6.5-3]

* Thu May 26 2005 Stephen Noble <support@dungog.net>
- vacation if enabled is run first
- test for invalid forwarding addresses
- [1.6.5-2]

* Fri Feb 11 2005 Stephen Noble <support@dungog.net>
- change rpm scripts from httpd-* graceful to restart
-  to allow rpm to install on both SME 6.0 + 6.5
- added alias, /user is same as /user-manager
- allow remote access to /user, with alt IP range from /server-manager access
-  /sbin/e-smith/db configuration set httpd-user 188.122.45.122
-  /sbin/e-smith/expand-template /etc/httpd/conf/httpd.conf
-  /etc/rc.d/init.d/httpd-e-smith restart
-  see also /sbin/e-smith/db configuration show httpd-admin for format
-  bad things happen if you enter an invalid ip ie>256
- remove displayed mitel references and old images
- [1.6.5-1]

* Thu Dec 23 2004 Stephen Noble <support@dungog.net>
- cosmetic vacation msg fix re. Dos/Unix new line
- [1.6.0-4]

* Sat Mar 6 2004 Stephen Noble <support@dungog.net>
- procmail forward to user fixed
- procmail says folder not in correct format fixed
- procmail can use 2nd value for closer matching
- geek mode hidden, you can set manually with
- /sbin/e-smith/db processmail setprop stephen mode geek
- [1.6.0-3]

* Fri Dec 5 2003 Stephen Noble <support@dungog.net>
- procmail, supports folders starting with new, cur, tmp
  thanks Shad Lords
- displays sme6 panels correctly
  thanks Robert Mc Donald
- [1.6.0-2]

* Fri Aug 15 2003 Stephen Noble <support@dungog.net>
- SME 6.0 support, this version requires it
- supports servermanager navigation & shows tables correctly
- procmail writes to dovecoat imap store eg. ~/Maildir/;junkmail
- many other changes
- [1.6.0-1]

* Thu May 21 2003 Stephen Noble <support@dungog.net>
- Fix 90e-smithAccess30user, httpd failed with 500?+ users
- [1.0-11]

* Thu Mar 6 2003 Stephen Noble <support@dungog.net>
- Fix 23autoreply, wasn't stopping looping to self
- [1.0-10]

* Mon Dec 16 2002 Stephen Noble <support@dungog.net>
- Fix /usr.../vacation, saved in dos not unix
- [1.0-9]

* Thu Dec 12 2002 Stephen Noble <support@dungog.net>
- mkdir -p user/cgi-bin in spec for new installs
- [1.0-8]

* Tue Dec 10 2002 Stephen Noble <support@dungog.net>
- Fix actions, saved in dos not unix
- userpanel-backup changed default file save as name to username
- [1.0-7]

* Fri Nov 29 2002 Stephen Noble <support@dungog.net>
- userpanel-forwarding modified to allow empty fwd address
- [1.0-6]

* Thu Nov 28 2002 Shad Lords <slords@mail.com>
- changed directive for externalSSLAccess to strip /255.255.255.255
- [1.0-5]

* Thu Oct 03 2002 Shad Lords <slords@mail.com>
- fixed ordering of panels a little more to make them alphabetical
- [1.0-4]

* Thu Oct 03 2002 Shad Lords <slords@mail.com>
- Cleaned up .procmailrc header
- [1.0-3]

* Wed Oct 02 2002 Shad Lords <slords@mail.com>
- Updated requires to include the Unicode packages for imap folders
- [1.0-2]

* Tue Oct 01 2002 Shad Lords <slords@mail.com>
- Combined all user-manager panels into 1 package
- Fixed user-manager.jpg to show on all panels (except pleasewait)
- updated userpanel-forward to check for procmail enabled
- updated userpanel-autoreply to check for procmail enabled
- [1.0-1]

* Mon Sep 30 2002 Shad Lords <slords@mail.com>
- Fixed another bug with global panels (needed AdminPanels)
- added externalSSLAccess to allow from for external access
- added RequireSSL on to the user-manager directive
- fixed user-manager.jpg to correct version
- [0.3-6]

* Mon Sep 23 2002 Stephen Noble <support@dungog.net>
- userpanel-forwarding tests if procmail fragments are installed
- renumbered navigation in userpanels to display alphabetically and match initial
- [0.3-5]

* Sun Sep 22 2002 Shad Lords <slords@mail.com>
- added userpanel- panels into list to choose from
- added default globalUP panels to all userpanel- panels
- added indication in user panels to which global panels are active
- added routine to display desc and longdesc to userpanel-initial
- [0.3-4]

* Sat Sep 21 2002 Shad Lords <slords@mail.com>
- helps if you actually include your changes (userpanelaccess) ;)
- excluded a few more web functions per Darrell May.
- [0.3-3]

* Sat Sep 21 2002 Shad Lords <slords@mail.com>
- fixed permission for global user panels
- added userpanel-* back into navigation
- fixed userpanel-noframes to use globals
- fixed userpanelaccess to look in functions for panels
- fixed conf-userpanelsymlinks to only create needed panels
- cleaned up some of the userpanel- titles for consistency
- fixed userpanel-initial to look for userpanel-procmail instead of dungog-procmail
- removed ^M from admin-conf templates
- added devinfo-mitel-userpanel-autoreply to obsoletes
- [0.3-2]

* Sat Sep 21 2002 Stephen Noble <support@dungog.net>
- only gives users access after admin assigns panel
- admin can assign a panel to all users via userpanelaccess
- merged updated userpanels for userpanelaccess, e-smith-userpanel-vacation,
  e-smith-userpanel-config, dungog-autoreply and dungog-userbackup
- updated userpanel-password,forward,navigation,inital)
- added usermanager.jpg
- [0.3-1]

* Mon Jan 07 2002 Daniel van Raay <danielvr@caa.org.au>
- fixed bug in 90e-smithAccess30user while maintaining '<Files>' directives
  for security purposes
- [0.2-5]

* Sun Jan 06 2002 Darrell May <dmay@netsourced.com>
- fixed bug in 90e-smithAccess30user
- [0.2-4]

* Sun Jan 06 2002 Daniel van Raay <danielvr@caa.org.au>
- [0.2-3]
- added all the panels to the default AvailablePanels setting
- modified the default navigation heading weights

* Sun Jan 06 2002 Daniel van Raay <danielvr@caa.org.au>
- [0.2-2]
- fixed bug in conf-userpanel event

* Sat Jan 05 2002 Daniel van Raay <danielvr@caa.org.au>
- [0.2-1]
- tidy up /etc/e-smith/templates/etc/httpd/admin-conf/httpd.conf/90e-smithAccess30user
- added initial support for additional 'AdminPanels' for users that need access to
  one or a few of the server-manager panels only
- changed 'Email' and 'Password' to 'Your Email' and 'Your Password'

* Wed Jan 02 2002 Daniel van Raay <danielvr@caa.org.au>
- [0.1-12]
- added manual redirect httpd.conf fragment for user-manager under e-smith 4.1.2
- stopped templates from adding ProxyPass directives under e-smith 4.1.2
  so that the redirects will work properly

* Tue Jan 01 2002 Darrell May <dmay@netsourced.com>
- [0.1-11]
- edit initial.html to support name change of userpanel-procmail to userpanel-processmail

* Sun Dec 30 2001 Daniel van Raay <danielvr@caa.org.au>
- [0.1-10]
- improved (cosmetic) compatibility with e-smith 4.1.2, SME 5.0, SME 5.1
- rolled in Darrell's cosmetic changes to initial page with checks to
  see if e-smith-procmail and/or e-smith-vacation are installed

* Tue Dec 25 2001 Darrell May <dmay@netsourced.com>
- [0.1-9]
- updated initial.html

* Mon Dec 24 2001 Darrell May <dmay@netsourced.com>
- [0.1-8]
- minor cosmetic changes to the password panel for SME5.1B3

* Sat Oct 20 2001 Daniel van Raay <danielvr@caa.org.au>
- [0.1-7]
- minor cosmetic changes to the password panel

* Fri Oct 19 2001 Daniel van Raay <danielvr@caa.org.au>
- [0.1-6]
- actually build the RPM properly to include [0.1-6] changes ;)

* Thu Oct 11 2001 Daniel van Raay <danielvr@caa.org.au>
- [0.1-5]
- added alias for access via http://servername/user-manager/
- cosmetic changes to refer to the panels as 'User Manager' instead of 'e-smith user'

* Sat Sep 22 2001 Daniel van Raay <danielvr@caa.org.au>
- [0.1-4]
- fixed minor cosmetic problem with front page when accessed through ProxyPass

* Fri Sep 21 2001 Daniel van Raay <danielvr@caa.org.au>
- [0.1-3]
- updated for compatibility with SME Sever V5

* Wed Sep 19 2001 Daniel van Raay <danielvr@caa.org.au>
- [0.1-2]
- added post (un)install scripts to expand/reload the relevant templates/services

* Mon Sep 04 2001 Daniel van Raay <danielvr@caa.org.au>
- [0.1-1]
- initial release

%prep
%setup


%build
perl createlinks

mkdir -p root/etc/e-smith/web/panels/user/cgi-bin

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
|grep -v 'logout-user'> %{name}-%{version}-filelist
echo "%doc COPYING"  >> %{name}-%{version}-filelist
echo '%attr(0755,root,admin) /etc/e-smith/web/common/cgi-bin/logout-user'>> %{name}-%{version}-filelist

%clean
#cd ..
#rm -rf %{name}-%{version}

%pre
%preun

%post

#/sbin/e-smith/expand-template /etc/httpd/admin-conf/httpd.conf
#/sbin/e-smith/expand-template /etc/httpd/conf/httpd.conf
#/usr/local/bin/svc -h /service/httpd-admin
#/usr/local/bin/svc -h /service/httpd-e-smith

#needs script to find existing languages
#upgrades (and new installs) should be in new but existing users may miss some lexicons
#should have in build not post
# or better move as action in events, this way we could update any languages.
#for lang in en-us fr es it de sv pt sl nl #el id
#do
#/bin/mkdir -p /etc/e-smith/locale/$lang/etc/e-smith/web/panels/user
#/bin/ln -sf /etc/e-smith/locale/$lang/etc/e-smith/web/functions /etc/e-smith/locale/$lang/etc/e-smith/web/panels/user/cgi-bin
#done

#/sbin/e-smith/signal-event conf-userpanel

%postun
#uninstall
#if [ $1 = 0 ] ; then
# /sbin/e-smith/expand-template /etc/httpd/admin-conf/httpd.conf
# /sbin/e-smith/expand-template /etc/httpd/conf/httpd.conf
# /usr/local/bin/svc -h /service/httpd-admin
# /usr/local/bin/svc -h /service/httpd-e-smith

# #this has moved ?fixme? 
# DBS=`find /home/e-smith/db/navigation -type f -name "navigation.*"`
# for db in $DBS ; do
#   /sbin/e-smith/db $db delete userpanelaccess
# done
#fi

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
