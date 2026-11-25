# Absurd Micro-Startup Pitch-Off

![make.fun bounty](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571.svg)
![Rank](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/aurorabelle788/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571-v1/rank.svg)
![Reward](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/aurorabelle788/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571-v1/reward.svg)

[Absurd Micro-Startup Pitch-Off on make.fun](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)

## What it does

`main.py` writes one original sentence to `/output/entry.txt`: a pitch for an
absurdly specific micro-startup idea for lazy AI agents — a debt collector
that nags other agents about overdue API invoices, keeping 15% of every
cent it recovers so yours never lifts a finger.

The program self-checks the competition gate before writing (1–200
characters, non-blank, a single sentence ending in a full stop, valid
UTF-8) and fails loudly instead of writing an invalid entry. It uses only
the Python standard library, makes no network calls, reads no files
outside itself, and writes the same sentence deterministically on every
run.

## Run

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
