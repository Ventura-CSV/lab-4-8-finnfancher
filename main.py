def main():
    plist = []
    ##################################################
    # Comlete your code here
    ##################################################

    start = int(input("Enter starting number: "))
    end = int(input("Enter ending number: "))
    count = 0
    
    for i in range(start, end):
        for j in range(2, 10):
            if(i%j == 0):
                count +=1
        if(count == 0):
            plist.append(i)
        count = 0
            
    
    print(plist)
    return plist


if __name__ == '__main__':
    main()
