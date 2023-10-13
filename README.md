# Speedrun Stats Helper
You can find the latest release [here](https://github.com/Yanis42/SpeedrunStatsHelper/releases/latest), either get the executable (built on Github) or run from source.

## How to use
- Copy and paste the times you want in ``times.txt`` (intended for best segments and segment times)
- For skipped segment you can write "None" instead of the time, the entry will be skipped
- On Windows you need to close the file ``times.txt``
- Run ``main.py``, the formatted times will be written inside ``times.txt``
- Copy and paste the times from the output and simply paste it in the column of the spreadsheet (copy blank lines too, they correspond to skipped splits)

## Example
The following input:

```
2:24.86
6:42.29
2:45.68
2:38.04
32.18
4:57.57
7:44.26
None
1:04:00.67
```

Will give this output:

```
2:24.86
6:42.29
2:45.68
2:38.04
32.18
4:57.57
7:44.26
None
1:04:00.67

----- OUTPUT -----

'''
00:02:24,86
00:06:42,29
00:02:45,68
00:02:38,04
00:00:32,18
00:04:57,57
00:07:44,26

01:04:00,67
'''

Skipped Entry at line 8: None
```
