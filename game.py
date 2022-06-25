while(True):
    try:
        inp = int(input("what is the level?: "))
    except:
        print("must be a number")
        continue

    if inp < 1:
        print("must be positive integer!")
    else:
        break
   


print(inp)