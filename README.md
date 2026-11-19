# software-uninstall-leftover-finder

Find leftover files of software that is no longer installed: installed.csv lists the software still on the machine, leftovers.csv lists scanned leftover files, folders or registry entries attributed to a program name — a leftover counts only when its program is not in installed.csv, items for still-installed software are skipped, and leftovers are grouped by program, most items first.

Sample input is included (sample-installed.csv and sample-leftovers.csv).

## How to run

```sh
python3 main.py sample-installed.csv sample-leftovers.csv
```

## Example output

```
OldApp: 3 leftover item(s) - program not installed
  C:/ProgramData/OldApp/config.ini
  C:/Users/Public/OldApp/cache.dat
  HKLM/Software/OldApp
Video Editor: 1 leftover item(s) - program not installed
  C:/ProgramData/Video Editor/settings.xml
4 leftover item(s) from 2 uninstalled program(s); 1 item(s) skipped (program still installed).
```

Standard library only. Run the tests with `python3 -m unittest discover`.
