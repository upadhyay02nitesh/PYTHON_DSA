def largest_odd(s):
    for i in range(len(s)-1,-1,-1):
        if int(s[i])%2!=0:
            return s[0:i+1]
    return ""


if __name__=="__main__":
    s=input("Enter the String : ")

    print(largest_odd(s))