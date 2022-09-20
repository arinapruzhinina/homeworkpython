def task_12_09(str_1):
    word_list=str_1.split()
    big_str=0
    for pod_str in word_list:
        big_letter = sum(map(str.isupper,pod_str))
        small_letter= sum(map(str.islower,pod_str))
        if big_letter > small_letter:
            big_str+=1
    return '{0}%'.format(big_str/len(word_list)*100)
        
print(task_12_09('ABc dbE FRl Ama'))