# 미세먼지 농도 ( Particulate Matter )

dust = int(input('PM > '))

if dust < 0:
    print('Wrong PM input!')
elif dust <= 30:
    print('좋음')
elif dust <= 80:
    print('보통')
elif dust <= 150:
    print('나쁨')
else:
    print('매우나쁨')