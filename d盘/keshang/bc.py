count = int(input())
for i in range(count):
    in1 = int(input())
    in2 = input().split()
    in3 = input().split()
    in2_list = [int(x) for x in in2]
    in3_list = [int(x) for x in in3]

    in22_list = sorted(list(set(in2_list)))
    in33_list = sorted(list(set(in3_list)))


    str0 ='={,'
    for i1 in  in22_list:
        str0+=str(i1)+'=0'+','
    str0+='}'

    dict1 ={}
    for i2 in range(in1):
        in2_list_i = in2_list[i2]
        in3_list_i = in3_list[i2]
        if in3_list_i not  in dict1:
            dict1[in3_list_i]={}
        if in2_list_i not in dict1[in3_list_i]:
            dict1[in3_list_i][in2_list_i]=1
        else:
            dict1[in3_list_i][in2_list_i]+=1

    for k,v in dict1.items():
        s=str0
        for k1, v1 in v.items():
            s0 = ','+str(k1)+'=0'
            sn = ','+str(k1)+'='+str(v1)+','
            s = s.replace(s0,sn)
        s = s.replace('{,','{').replace(',}','}')
        s = str(k)+s
        print(s)





