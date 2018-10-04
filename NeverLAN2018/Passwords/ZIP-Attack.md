## ZIP Attack (100) 

```
We intercepted this encrypted zip.
And we noticed it had a file inside that we have previously seen. 
Will that help you crack it open?
```
***
1) Examine the compressed file 
```groovy
$ zipinfo encrypted.zip 
Archive:  encrypted.zip   186312 bytes   3 files
drwxr-xr-x  3.0 unx        0 bx stor XX-XX-18 x:x supersecretstuff/
-rw-r--r--  3.0 unx       34 TX stor XX-XX-18 x:x supersecretstuff/flag.txt
-rw-r--r--  3.0 unx   220680 BX defX XX-XX-18 x:x supersecretstuff/sw-iphone-wallpaper-first-order.jpg
3 files, 220714 bytes uncompressed, 185662 bytes compressed:  15.9%
```

2) Now with the help of **[pkcrack](https://www.unix-ag.uni-kl.de/~conrad/krypto/pkcrack.html)**
```ruby

 $> pkcrack -C encrypted-ZIP -c ciphertextname -P plaintext-ZIP -p plaintextname -d decrypted_file -a

encrypted-ZIP
is the name (and path) of the encrypted ZIP-archive
ciphertextname
is the name of the file in the archive, for which you have the plaintext
plaintext-ZIP
is the name (and path) of the ZIP-archive containing the compressed plaintext 
plaintextname
is the name of the file in the archive containing the known plaintext
decrypted_file
is the name of a file to which the decrypted archive will be written
```

3) Crafting..

 **`./pkcrack-1.2.2/src/pkcrack -C encrypted.zip -c supersecretstuff/sw-iphone-wallpaper-first-order.jpg -p sw-iphone-wallpaper-first-order.jpg -P known-file.zip -d decrypted.zip`**
```groovy

Files read. Starting stage 1 on Mon x x x 2018
Generating 1st generation of possible key2_185639 values...done.
Found 4194304 possible key2-values.
Now we're trying to reduce these...
                          :
Finished on Mon x x x 2018
$ unzip decrypted.zip
Archive:  decrypted.zip
   creating: supersecretstuff/
 extracting: supersecretstuff/flag.txt  
  inflating: supersecretstuff/sw-iphone-wallpaper-first-order.jpg  

$ cat supersecretstuff/flag.txt
```

**`flag{plaintext-attacks-are-cool!}`**
