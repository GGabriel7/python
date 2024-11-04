def maior(*num):
    mai = 0
    for c in num:
        print(c, end =' ')
        if c > mai:
            mai = c

    print(f' / foram informados {len(num)} números.\nO maior é {mai}.')

maior(1, 6, 2, 3, 7, 0)
maior(7, 4, 0)
maior(1, 2)
maior(6)
maior()
