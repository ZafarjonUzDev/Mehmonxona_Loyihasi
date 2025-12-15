# Konsolga Asoslangan Mehmonxona Boshqaruv Tizimi 

## Asosiy Maqsad

Ushbu mini-loyihaning asosiy maqsadi — **Python** lug‘atlari (dictionaries) va funksional logikadan foydalangan holda real vaqt rejimida (in-memory) ishlaydigan **Mehmonxona Xonalarini Boshqarish Tizimining (HMS - Hotel Management System)** mustahkam prototipini yaratish.

Loyihaning diqqat markazi **toza mantiq (clean logic)** va **tezkor ishlash (performance)**ga qaratilgan.

## Muhim Texnik Qismlar

Loyihaning kodi bitta faylda jamlangan bo'lishiga qaramay, u quyidagi muhim jihatlarni o'z ichiga oladi:

* **Ma'lumotlar Tuzilmasini Optimallashtirish:** Mehmonlar va xonalar holatini samarali boshqarish uchun Pythonning **Lug'at (Dictionary)** ma'lumotlar tuzilmasidan foydalanilgan.
* **Xatolar Bilan Ishlash (Error Handling):** Buyruqlarni kiritishda va xona tanlashda noto'g'ri qiymatlar kiritilishining oldini olish uchun mantiqiy tekshiruvlar (Validation) joriy etilgan.

## Dasturni Ishga Tushirish

Tizimni mahalliy kompyuteringizda ishga tushirish uchun:

1.  Repozitoriyani klonlash:
    ```bash
    git clone [https://github.com/ZafarjonUzDev/Mehmonxona_Loyihasi.git](https://github.com/ZafarjonUzDev/Mehmonxona_Loyihasi.git)
    ```
2.  Loyiha papkasiga o'ting va dasturni ishga tushiring:
    ```bash
    python Mehmonxona_dasturi.py
    ```

## Kelajakdagi Kengayish Salohiyati (Scalability)

Loyihaning mavjud tuzilmasi kelgusida yanada yirik tizimga aylantirish uchun mukammal asos bo'lib xizmat qiladi:

* **Tizimni Modullash (Refactoring):** Lug'at strukturasini **`Mehmon`** va **`Xona`** kabi alohida OOP klasslariga aylantirish.
* **Doimiy Saqlash (Persistence):** Ma'lumotlarni xotirada emas, balki **SQLite** kabi haqiqiy ma'lumotlar bazasida saqlashga o'tish.
