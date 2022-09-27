print('eps')
# for raw_left in ['symbol', '(base)']:
for raw_left in ['left']:
    for asterix in ['*', ' ']:
        for alt in ['|', ' ']:
            # for raw_right in ['eps', '(base)', 'symbol']:
            for raw_right in ['right']:
                print(raw_left, asterix, alt, raw_right, sep='')