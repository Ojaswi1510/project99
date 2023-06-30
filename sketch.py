def Countingletters():
    f=input("enter the file name")
    file=open(f,'r')
    countOfwords=0
    for f in file:
        words=f.split()
        countOfwords=countOfwords+len(words)
    print(countOfwords)
Countingletters()
