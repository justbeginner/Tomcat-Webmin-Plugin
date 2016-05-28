# Tomcat Webmin Plugin 1.0.1 BETA


1. Install the module from Webmin configuration.
	1.1 Archive module
		tar -cvzf tomcat.wbm.gz tomcat/
	1.2 Upload from Webmin->Webmin Modules

Notes:
	Arch
		- Install tomcat packages manually
			pacman --noconfirm -S tomcat8 tomcat-native
	SuSe
		- Install tomcat packages manually
			zypper -n install tomcat tomcat-webapps tomcat-admin-webapps
	Slackware
		- Install Tomcat using one of our scripts!
