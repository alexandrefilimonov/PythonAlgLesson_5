#2.Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив, элементы которого это цифры числа. 
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. 
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: для решения задачи попробуйте применить какую-нибудь коллекцию из модуля collections

from collections import defaultdict

s1 = str(input( "Enter first number in hex: " ))
s2 = str(input( "Enter second number in hex: " ))

arr1 = list(s1)
len1 = len(arr1)
arr2 = list(s2)
len2 = len(arr2)
lmax = max(len1,len2)
i = lmax
s_sum = 0
s_mult = 0
i_16th=0
one_in_memory_sum = 0
one_in_memory_mult = 0
while  (i>=0) :
    if (len1>0 or len2>0) :
        if (len1>0 and len2>0) :
            i_digit = int(arr1[len1-1],16) + int(arr2[len2-1],16)
            i_digit2 = int(arr1[len1-1],16) * int(arr2[len2-1],16)			
        elif (len1>0 and len2<=0) :
            i_digit = int(arr1[len1-1],16) 
            i_digit2 = int(arr1[len1-1],16) 
        elif (len2>0 and len1<=0) :
            i_digit = int(arr2[len2-1],16)
            i_digit2 = int(arr2[len2-1],16)			
			
        i_digit_s=i_digit+one_in_memory_sum
        #print("i_digit_s",i_digit_s)
        if (i_digit_s >15) :
            i_digit_s=i_digit_s-16
            one_in_memory_sum=1
            s_sum+=(i_digit_s*16**i_16th)
        else :
            one_in_memory_sum=0
            s_sum+=(i_digit_s*16**i_16th)

        i_digit_m=i_digit2+one_in_memory_mult
        #print("i_digit_m",i_digit_m)
		
        if (i_digit_m >15) :
            one_in_memory_mult=0
            while(not(i_digit_m<=15)) :
                i_digit_m=i_digit_m-16
                one_in_memory_mult+=1
            #print("M:",i_digit,one_in_memory_mult,i_digit_m)
            s_mult+=(i_digit_m*16**i_16th)
            #print("S_M:",s_mult)
        else :
            one_in_memory_mult=0
            s_mult+=(i_digit_m*16**i_16th)
		
        #print("Sum",s_sum)
        #print("Mult",s_mult,(i_digit_m*16**i_16th),i_digit_m,one_in_memory_mult)
        i_16th+=1
    i-=1
    len1-=1
    len2-=1
s3 = hex(s_sum)
s4 = hex(s_mult)

arr3 = list(s3)
arr4 = list(s4)
print("Hex Sum",arr3[2:])
print("Hex Multiplication",arr4[2:])	



