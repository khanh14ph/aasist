with open("/home4/khanhnd/aasist/submission2.txt", "r") as f:
    with open("/home4/khanhnd/aasist/submission.txt", "w") as f1:
        lst=f.readlines()
        for i in lst:
            i=i.strip()
            a,b,c=i.split("\t")
            c=float(c)
            if c>0.5:
                c=1
            if c<0.5:
                c=0
            f1.write(f"{a}\t{b}\t{str(c)}\n")