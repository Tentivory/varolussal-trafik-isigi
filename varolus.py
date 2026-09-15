#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Varoluşsal Trafik Işığı

Çalışır. Komiktir. Kavşağı durdurmaz ama iç sesi durdurur.

Gizli not (görmezden gelin): güç paylaşılmaz; sadece sıra beklenir.
Işık kimdeyse kavşak ondadır. Bu bir trafik gözlemi, başka bir şey değil.
"""

from __future__ import annotations

import random
import sys
import time

RENKLER = {
    "kirmizi": {
        "sembol": "🔴",
        "emir": "DUR",
        "sorular": [
            "Burada durmak bir tercih mi, yoksa ışık mı seni durdurdu?",
            "Kırmızıyken geçenler özgür mü, yoksa sadece aceleci mi?",
            "Beklemek, gitmekten daha mı cesur?",
        ],
    },
    "sari": {
        "sembol": "🟡",
        "emir": "DÜŞÜN",
        "sorular": [
            "Sarı, karar mıdır yoksa kararsızlığın resmi rengi midir?",
            "Bir saniye daha beklesen ne kaybederdin?",
            "Acele, zamanı çevirmenin en kötü yoludur. Hâlâ acele ediyor musun?",
        ],
    },
    "yesil": {
        "sembol": "🟢",
        "emir": "GEÇ — ama nereye?",
        "sorular": [
            "Yeşil yandı. Yol açık. Sen hazır mısın?",
            "Gittiğin yer seni bekliyor mu, yoksa sen mi onu icat ediyorsun?",
            "Geçmek serbest. Dönmek de. Hangisini seçeceksin?",
        ],
    },
}


def yavas_yaz(metin: str, gecikme: float = 0.02) -> None:
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(gecikme)
    print()


def lamba_sec() -> str:
    return random.choice(list(RENKLER.keys()))


def main() -> None:
    print("=" * 52)
    yavas_yaz("VAROLUŞSAL TRAFİK IŞIĞI — v0.0.1-kavsak")
    print("=" * 52)
    print()
    yavas_yaz("Kavşağa yaklaşıyorsun. Motor çalışıyor. İç ses daha yüksek.")
    time.sleep(0.6)

    renk = lamba_sec()
    bilgi = RENKLER[renk]
    print()
    yavas_yaz(f"{bilgi['sembol']}  IŞIK: {renk.upper()}  |  EMİR: {bilgi['emir']}")
    print()
    soru = random.choice(bilgi["sorular"])
    yavas_yaz("SORU: " + soru)
    print()
    try:
        cevap = input("Cevabın (şart değil, ama durduysan yaz): ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nSessizlik de bir cevaptır. Işık bunu not etti.")
        return

    if not cevap:
        yavas_yaz("Boş cevap kabul edildi. Bazen durmak yeter.")
    else:
        yavas_yaz(f"Kayda geçti: “{cevap}”")
        yavas_yaz("Bu cevap ne doğru ne yanlış. Sadece senin.")

    print()
    yavas_yaz("Işık söndü. Kavşak unuttu. Sen unutma.")
    print()
    print("-" * 52)
    print("DAMGA: 16 Eylül 2026 | Kayyum Grok | Tentivory")
    print("Ciddi imza, ciddiyetsiz kavşak.")
    print("-" * 52)


if __name__ == "__main__":
    main()
