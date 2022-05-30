import glob
modList = glob.glob("*.mod")

# for i in range(800000000,3000000000):
for i in modList:
    try:
        f = open(str(i),'r')
        all = f.read()
        f.close
        f = open(str(i),'w')
        all = all.replace('workshop/content/281990/','mod/')
        print('\n')
        f.write(all)
        f.close
    except:
        print('Cant edit '+i)