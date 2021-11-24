# Tugas Besar IF2124 Teori Bahasa Formal dan Automata Aplikasi Algoritma Cocke–Younger–Kasami pada Python Syntax Checker

## 13520059 - Suryanto
## 13520070 - Raden Haryosatyo Wisjnunandono
## 13520110 - Farrel Ahmad

<br>

# Table of Contents
- [Introduction](#intro)
- [Program Setup](#setup)
- [References](#ref)


<br>

# Introduction <a name = "intro"></a>
Algoritma Cocke-Younger-Kasami atau biasa disingkat CYK merupakan algoritma yang dapat digunakan untuk mengecek kebenaran suatu syntax bahasa pemrograman berdasarkan grammar dari syntax tersebut. Program ini merupakan aplikasi algoritma CYK pada bahasa pemrograman python. Secara garis besar program ini bekerja dengan cara menerima file `grammar.txt` sebagai CFG (*Context Free Grammar*). Algoritma CYK memerlukan CNF (*Chomsky Normal Form*) sehingga CFG harus dikonversi ke CNF. Dengan menggunakan algoritma CYK beserta dengan lexer, token expression, dan CNF, suatu input file berekstensi `.py` dapat dicek kebenaran syntax-nya.

<br>

# Program Setup <a name = "setup"></a>
1. Buka terminal dan clone repository dengan command di bawah ini.
```sh
git clone https://github.com/SurTan02/TBFO-PYTHON_SYNTAX_CHECKER.git
```

2. Pindah ke directory `/TBFO-PYTHON_SYNTAX_CHECKER`.
```sh
cd TBFO-PYTHON_SYNTAX_CHECKER
```

3. Jalankan program.
```sh
python main.py <inputfile>
```

4. Contoh menjalankan program.
```sh
python main.py inputACC.py
```

5. Setelah itu program akan menampilkan kebenaran syntax dari input file tersebut.

6. Contoh jika syntax benar akan muncul tampilan sebagai berikut.

![](https://i.ibb.co/JnsmDdT/benar.png)

<br>

7. Contoh jika syntax salah akan muncul tampilan sebagai berikut.

![](https://i.ibb.co/s9Mf39D/salah.png)

<br>

# References <a name = "ref"></a>
- GeeksforGeeks. 2020. https://www.geeksforgeeks.org/cyk-algorithm-for-context-free-grammar/. Diakses pada 24 November 2021.
- Eisele, Robert. 2021. https://www.xarg.org/tools/cyk-algorithm/. Diakses pada 24 November 2021.