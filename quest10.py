'''big_list = [[1,2,3], [5,8,9], [4,3,77,521,31,311]]
counter1 = 0
while counter1 < len(big_list):
    small_list_length = len(big_list[counter1])
    counter2 = 0
    while counter2 < small_list_length:
        print (big_list[counter1][counter2])
        counter2 = counter2 + 1
    counter1 = counter1 + 1
    print ('-----')'''

marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]] 
i=0
while i<len(marks):
    s_m_l=len(marks[i])
    j=0
    while j<s_m_l:
        # print(marks[i][j])
        m=max(marks[i][j])
        print(m)
        j+=1
    i+=1