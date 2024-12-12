#include<iostream>
using mainspace std;

int main()
{
    string aktifitas;
    string tempat;
    int usia;

    cout<<"apa aktifiasmu hari ini : "<<endl;
    getline(cin, aktifias); // cin hanya untuk kata pertama saja yang dimunculkan /  di save

    cout<< "aku sekarang ada di" << aktifias <<endl;
    getline(cin, tempat); // getline tidak hanya kalimat awal saja atau dibelakang spasi

    cout<< "berapa usiamu : "<<endl;
    cin>> umur;         // kalau cin menggunakan >>
    cout<<"saya sedang"<<aktifias<<"di"<<tempat<<endl;
    cout<<"usia saya sekarang adalah: "<<umur<<endl;
}