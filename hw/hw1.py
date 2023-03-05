def sec2time(s):
    # m = s // 60
    # s = s % 60
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    return f'{d}:{h:02}:{m:02}:{s:02}'

time = sec2time(120)
print(time)
