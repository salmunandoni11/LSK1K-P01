#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def loop_with_list() -> None:
    """
    Looping dengan list berisi string 'a', 'b', 'c'.
    """
    chars = ["a", "b", "c"]               # <-- inisialisasi tiga string
    print("=== Looping menggunakan list literal ===")
    for i, ch in enumerate(chars, start=1):
        # i : nomor urut (1‑based)
        # ch: karakter (tipe str dengan panjang 1)
        print(f"{i}. karakter = '{ch}'")


def loop_with_chr_range() -> None:
    """
    Looping dengan menghasilkan huruf a‑c secara dinamis
    menggunakan chr() + range().
    """
    start_ord = ord('a')                  # 97
    end_ord   = ord('c')                  # 99   (inklusif)
    print("\n=== Looping menggunakan chr() + range() ===")
    for i, code in enumerate(range(start_ord, end_ord + 1), start=1):
        ch = chr(code)                    # ubah kode Unicode -> karakter
        print(f"{i}. karakter = '{ch}' (Unicode: {code})")


def main() -> None:
    loop_with_list()
    loop_with_chr_range()


if __name__ == "__main__":
    main()
