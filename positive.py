def positive(n):
    positive = []  
    for num in n:  
        if num > 0:  
            positive_numbers.append(num)  
    print("Output:", positive_numbers)  

if __name__ == "__main__":
    list1 = [12, -7, 5, 64, -14] 
    print("Input:", list1, end=" ") 
    print_positive_numbers(list1)  

    list2 = [12, 14, -95, 3]  
    print("Input:", list2, end=" ")  
    print_positive_numbers(list2)  
