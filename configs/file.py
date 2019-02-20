f=open("helo.txt")
try:
    for line in f:
        print line,
finally:
    f.close()


