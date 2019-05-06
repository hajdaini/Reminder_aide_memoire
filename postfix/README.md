# postfix config

## Local install

run the script and change the ${YOUR_HOSTNAME} ${YOUR_DOMAIN} only if : 

- If you send mail to only localhost, set myhostname = localhost and mydomain = localdomain.

- If you send mail to your domain, set your hostname to myhostname and your domain to mydomain. 
  This hostname and domain must be known with multiple machine (common /etc/hosts or DNS server).  
  Both mail sender machine and receiver machine needs this Postfix setting.
  
then test your email :

```shell
echo "ceci est un test" | mail -s "Test" ajdaini.hatim@gmail.com
```

Open your email provided and **verify your spams** 

## Send mail to internet via Gmail

You need the previous Postfix setting. The myhostname and mydomain can be localhost setting or your domain setting.

Append the following to /etc/postfix.main.cf.

```shell
$ cat <<EOF | sudo tee -a /etc/postfix/main.cf
relayhost = [smtp.gmail.com]:587
smtp_sasl_auth_enable = yes
smtp_sasl_password_maps = hash:/etc/postfix/sasl_passwd
smtp_sasl_security_options = noanonymous
smtp_sasl_mechanism_filter = plain
smtp_use_tls = yes
EOF
```

Create /etc/postfix/sasl_passwd. Please set your Gmail address to GMAIL_ADDR and your Gmail password to GMAIL_PASSWD.

```shell
$ echo "[smtp.gmail.com]:587 ${GMAIL_ADDR}:${GMAIL_PASSWD}" | \
sudo tee /etc/postfix/sasl_passwd
$ sudo chmod 600 /etc/postfix/sasl_passwd
$ sudo postmap hash:/etc/postfix/sasl_passwd
```

Restart Postfix :

```shell
$ sudo systemctl restart postfix
```

Gmail will return authentication error :

```diff
- postfix/smtp ... SASL authentication failed; server smtp.gmail.com...
```

The 2-step verification and application password is better ["Allow less secure apps: ON"](https://myaccount.google.com/lesssecureapps)

If Gmail returns authenticaion error again, you need ["Allow access to your Google account"](https://accounts.google.com/DisplayUnlockCaptcha).

And then you can send mail to internet via Gmail. Mail's from address is your Gmail address.

```shell
postfix/smtp ... to=<yourgmail@gmail.com>,relay=smtp.gmail.com ...
```
