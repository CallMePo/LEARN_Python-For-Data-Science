with open("sesayang.txt", 'a+') as nyu:
    print("Initial Location: {}".format(nyu.tell()))

    data=nyu.read()
    if (not data):
        print("Nothing")
    else:
        print(data)
    print("Location after read: {}".format(nyu.tell()))

with open("sesayang.txt", 'r+') as nyunyu:
    data=nyunyu.readlines()
    nyunyu.seek(0,0)

    nyunyu.write("dimi"+"\n")
    nyunyu.write("azaleaaaaa"+"\n")
    nyunyu.truncate()
    nyunyu.seek(0,0)
    print(nyunyu.read())