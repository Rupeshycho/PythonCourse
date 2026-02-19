

def check_for_line2():
    word = input("Find a word: ").strip().lower()
    line_no = 1
    total_count = 0

    try:
        with open("practice.txt", "r") as f:
            for line in f:
                line_lower = line.lower()

                if word in line_lower:
                    # Find all positions in the line
                    start = 0
                    while True:
                        index = line_lower.find(word, start)
                        if index == -1:
                            break
                        
                        print(f'Found "{word}" in line {line_no} at position {index}')
                        total_count += 1
                        start = index + 1

                line_no += 1

        if total_count == 0:
            print("-1 : That's wrong bro! Word not found.")
        else:
            print(f"\nTotal occurrences: {total_count}")

    except FileNotFoundError:
        print("File not found. Make sure practice.txt exists.")


check_for_line2()

# numbers=[1,23,45,67,89,88,76,54,32,21]
count=0
with open("numbers.txt","r+") as f:
    data=f.read()
    # f.write(','.join(map(str,numbers)))
    # print("numbers= ",data)
    print(data)
    
    nums=data.split(",")
    for val in nums: # print(nums)
        if(int(val)%2==0):
            count+=1
print(count)
    
    
    # num=""
    # for i in range(len(data)):
    #     if(data[i]==","):
    #         print(int(num))
    #         num = ""
    #     else:
    #         num+=data[i]    
    