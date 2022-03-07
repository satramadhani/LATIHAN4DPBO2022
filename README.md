# LATIHAN4DPBO2022
Latihan Praktikum 04 - Desain dan Pemrograman Berorientasi Objek

### Saya [Muhammad Satria Ramadhani - 2005128] mengerjakan evaluasi [Latihan Praktikum 04] dalam mata kuliah [Desain dan Pemrograman Berorientasi Objek] untuk keberkahan-Nya, maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.

## Desain Program

![Design](https://user-images.githubusercontent.com/72297396/157062140-91c88d93-1291-4419-81c1-5cf6a42bea4f.png)

Dalam implementasi program, terdapat dua kategori kelas, yang masing-masing berisi tiga kelas:
- Vehicle, Ship, Airplane
- Person, Job, Driver

Untuk kategori "Vehicle", desain program menggunakan **Hierarchical Inheritance** karena baik Ship maupun Airplane merupakan bentuk turunan dari kendaraan ("*Ship and Airplane **is a** vehicle*"). Sementara itu, kategori "Person" menggunakan **Multiple Inheritance**. Hal ini dikarenakan Driver bisa berbentuk Person, tetapi juga berbentuk Job sehingga perlu mewarisi kedua sifatnya ("*Driver **is a** Person and a Job*").

## Hasil Program

Data Ship

![Ship](https://user-images.githubusercontent.com/72297396/157063225-52af7ca9-35b5-49fa-8243-bb77fa99fa43.png)

Data Airplane

![Airplane](https://user-images.githubusercontent.com/72297396/157063245-1e88d85e-ed3b-4296-9330-9fd5c566a1df.png)

Data Driver

![Driver](https://user-images.githubusercontent.com/72297396/157063276-e850b632-b55f-4a3a-adb2-e62a6b8e7820.png)
