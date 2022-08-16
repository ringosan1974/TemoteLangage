import sys

args = sys.argv

f = open(args[1], mode='w')
f.write(args[2].replace('>', 'てもて\n').replace('<', 'てもてっ\n').replace('+', 'てもて〜\n').replace('-', 'てもてー\n').replace('.', 'てもて！\n').replace(',', 'てもて？\n').replace('[', 'あっぷっ\n').replace(']', 'ぷぇ！\n'))
f.close()
