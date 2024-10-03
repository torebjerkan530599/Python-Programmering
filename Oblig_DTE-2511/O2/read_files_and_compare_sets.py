from pathlib import Path

file_name_1 = input('Enter a filename:')
file_name_2 = input('Enter a filename:')
try:
    txt_file_1 = open(Path(__file__).parent / file_name_1)
    txt_file_2 = open(Path(__file__).parent / file_name_2)
    s1 = set(txt_file_1.read().split())
    s2 = set(txt_file_2.read().split())
    txt_file_1.close()
    txt_file_2.close()

    print(f'Antall unike ord: {len(s1.union(s2))}') # s1 | s2
    print(f'Alle unike ord i begge filer : {", ".join(s1.union(s2))}')
    print(f'Alle unike ord som forekommer både i første og andre fil: {", ".join(s1 & s2)}') # s1.intersection(s2)
    print(f'Alle unike ord som forekommer i første fil, men ikke i andre: {", ".join(s1 - s2)}') # s1.difference(s2)
    print(f'Alle unike ord som forekommer i andre fil, men ikke i første: {", ".join(s2 - s1)}') # s2.difference(s1)
    print(f'Unike ord i enten første eller andre fil: {", ".join(s1 ^ s2)}') # s1.symmetric_difference(s2)
except FileNotFoundError as ex:
        print(f'file was not found or incorrect filename')

