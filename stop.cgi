#!/usr/bin/perl
# Stop the tomcat daemon from running

require './tomcat-lib.pl';
&ReadParse();
&error_setup($text{'stop_err'});
$err = &stop_tomcat();
&error($err) if ($err);
&webmin_log("stop");
&redirect("");

