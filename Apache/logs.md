Get top 20 most visited url :

```shell
cat <apache_log_path> | cut -d " " -f 7 | sort | uniq -c | sort -nr | head -n 20
```

Get top 10 IP :

```shell
cat <apache_log_path>  | cut -d " " -f 1 | sort | uniq -c | sort -nr | head -n 10
```
