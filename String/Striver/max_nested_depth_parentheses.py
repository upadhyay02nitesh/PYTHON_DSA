


def nested_max_depth(s):
    cur_depth=0
    max_depth=0
    for char in s:
        if char=="(":
            cur_depth+=1
            # print("cur",cur_depth)
            if cur_depth>max_depth:
                max_depth=cur_depth
        elif char==")":
            cur_depth-=1
    return max_depth


    
if __name__=="__main__":
    s=input("Enter String : ")
    print(nested_max_depth(s))