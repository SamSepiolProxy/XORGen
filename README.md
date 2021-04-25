# XORGen
A python3 script to apply xor cipher encryption to a file's contents.

If you have issues with extra symbols after XOR encoding it might be due to the encoding of your file, it may need chaning to utf-16 etc.
If so adjust line 15 to fit your needs:
open(filename,'r',encoding='utf16') as f:

Example:
python xor.py -i test.txt -k mykeyname
