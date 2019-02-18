## git-enc


### Synopsis
``` git-enc.py encrypt [-k password] path1 [path2 ...] ```
``` git-enc.py decrypt [-k password] path1 [path2 ...] ```


### Abstract
use this tool to easily encrypt/decrypt credential files for github repository or any kind of public storage.


### .gitencrypt
A `.gitencrypt` must exist on a git repository where files to be encrypted/decrypted are categorized into multi-layed groups. E.g.:
```
---
group1:
  sub-group1:
    original file1 : encrypted file1
    original file2 : encrypted file2

cert:
  server1:
    ./dir1/foo.pem : ./dir1/foo.pem.aes
    ./dir1/bar.pem : ./dir1/bar.pem.aes
  server2:
    ./dir2/foo.pem : ./dir2/foo.pem.aes
    ./dir2/bar.pem : ./dir2/bar.pem.aes

db:
  aaa:
    ./db/aa/shadow : ./john.doe
```

It's at your own risk not to push confidential files onto remote public repository.


### Run git-enc
```bash
$ git-enc.py encrypt -k passw@rd cert.server1 db
$ git-enc.py decrypt -k passw@rd cert.server1 db
```

### Example

```bash
$ cat testfile
name: jinsung choi
bank: kookmin 101-775-081254
social security number: M9812354
address: Seoul city hall 2F
email: jinchoiseoul@gmail.com
```

```bash
group:
  testfile: testfile.aes
```

```bash
$ git-enc.py encrypt -k passw@rd group
```

```bash
$ git-enc.py decrypt group
```

```bash
$ cat testfile.aes
Salted__/^O ^YVí^_4Å^C^FÉ$ÂcæéVä±N^?<9b>}zÐ^BÚ.^T0<8a>^\y^Etºp^UÞ<82>&§ø<92>g<80>¬<80>ªêK®<98>Þ<8e>ý^^}
ûnôÆóÅU<8a>þ{Þ<91>Ís^E<9b>o^RÂï^Wÿ×\E|<ª^P<95>ÆÒ^Nê<9f>ßx¯<8c><9e>ö<84><87>½3Ä^[^RÈSÄ<8b>»E'O~Ãd^Aùû¯<8f>È,ßkÌ^X<98>^[+:Q ^Pñc:º,;^MtTñÝ©g>ï
```
