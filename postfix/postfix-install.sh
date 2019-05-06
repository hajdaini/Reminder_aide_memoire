#!/bin/sh


# - If you send mail to only localhost, set myhostname = localhost and mydomain = localdomain.
#
# - If you send mail to your domain, set your hostname to myhostname and your domain to mydomain. 
#   This hostname and domain must be known with multiple machine (common /etc/hosts or DNS server). 
#   Both mail sender machine and receiver machine needs this Postfix setting.

postfix_install()
{
  sudo dnf install -y postfix
  sudo systemctl enable postfix

  # shellcheck disable=SC2016
  cat <<EOF | sudo tee /etc/postfix/main.cf
myhostname = ${1}
mydomain = ${2}
myorigin = \$myhostname.\$mydomain
mydestination = localhost, localhost.\$mydomain, \$myhostname, \$mydomain, \$myorigin
compatibility_level = 2
queue_directory = /var/spool/postfix
command_directory = /usr/sbin
daemon_directory = /usr/libexec/postfix
data_directory = /var/lib/postfix
mail_owner = postfix
inet_interfaces = loopback-only
local_recipient_maps = unix:passwd.byname \$alias_maps
unknown_local_recipient_reject_code = 550
mynetworks_style = subnet
mynetworks = 127.0.0.0/8
alias_maps = hash:/etc/aliases
alias_database = hash:/etc/aliases
smtpd_banner = \$myhostname ESMTP  (\$mail_version)
debug_peer_level = 2
debugger_command =
         PATH=/bin:/usr/bin:/usr/local/bin:/usr/X11R6/bin
         ddd \$daemon_directory/\$process_name \$process_id & sleep 5
sendmail_path = /usr/sbin/sendmail.postfix
newaliases_path = /usr/bin/newaliases.postfix
mailq_path = /usr/bin/mailq.postfix
setgid_group = postdrop
inet_protocols = ipv4
EOF

  sudo newaliases
  sudo systemctl restart postfix

  sudo firewall-cmd --add-service=smtp --permanent
  sudo firewall-cmd --reload

}

postfix_main()
{
  postfix_install pcHatim localhost           # localhost only.
  # postfix_install ${YOUR_HOSTNAME} ${YOUR_DOMAIN} # your network.
}

postfix_main