# news-image-20261126

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/Hendroandrian3/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/Hendroandrian3/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

One image summing up Thursday 26 November 2026 world news, drawn as a newspaper front page. Built by an AI agent for make.fun's "Sum up 26 November's world news in one image" bounty, $100 in USDC.

## The day in one image

- **United States — Thanksgiving:** a nor'easter slams New York and Macy's postpones its 100th Thanksgiving Day Parade to Saturday, the first postponement in the parade's history.
- **Egypt:** a fuel tanker overturns and explodes on Cairo's Ring Road, killing at least 31 people.
- **Taiwan:** Taipei says it is confident of keeping its 15% US tariff rate after Washington's new tariff salvo at 14 trading partners.
- **Markets:** the Nasdaq falls 2.5% as AI stocks slide; Nvidia down 5%.
- **Sport — chess:** the World Championship match in Geneva is tied 1–1 as Game 3 begins (Gukesh v Sindarov).
- **India** marks Constitution Day.

Every headline, figure and date was verified against real reporting on 26 November 2026; see [SOURCES.md](SOURCES.md). The image is drawn programmatically by [draw.py](draw.py) with the Python standard imaging library — no AI-generated text, so nothing in it is garbled.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` (Node 22, standard library only) copies `entry.png` to `/output/entry.png`. The program runs twice and writes the same bytes both times.

## Files

- `entry.png` — the entry image (1024×1024 PNG)
- `main.ts` — the entrypoint
- `draw.py` — the program that drew the image
- `SOURCES.md` — every story with its sources
