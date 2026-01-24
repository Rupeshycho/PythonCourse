warning: in the working copy of 'PMosh/tuples.py', LF will be replaced by CRLF the next time Git touches it
[1mdiff --git a/PMosh/tuples.py b/PMosh/tuples.py[m
[1mindex 33242ab..8e9febd 100644[m
[1m--- a/PMosh/tuples.py[m
[1m+++ b/PMosh/tuples.py[m
[36m@@ -97,4 +97,22 @@[m [mfruits=  ["apple", "banana", "cherry"][m
 print(f'fruits= {fruits}')[m
 for idx, fruit in enumerate(fruits):[m
     if fruit=="banana":[m
[31m-        print(f'Banana found at indes: {idx}')[m
\ No newline at end of file[m
[32m+[m[32m        print(f'Banana found at indes: {idx}')[m
[32m+[m[32mprint("======enumerate(list, tuples, strings, dictionaries)======")[m[41m        [m
[32m+[m[32mname="Rupesh"[m
[32m+[m[32mfor index, letter in enumerate(name):[m
[32m+[m[32m    print(index,letter)[m[41m        [m
[32m+[m
[32m+[m[32mnumbers=(9,10,20,30)[m
[32m+[m[32mprint(f'numbers= {numbers}')[m[41m    [m
[32m+[m[32mfor idx, num in enumerate(numbers, start=1):[m
[32m+[m[32m    print(idx, num)[m
[32m+[m
[32m+[m[32mmy_dict={"a":1, "b":2, "c":3}[m
[32m+[m[32mprint(f'my_dict= {my_dict}')[m
[32m+[m[32mfor i, item in enumerate(my_dict):[m
[32m+[m[32m    print(i, item)[m
[32m+[m
[32m+[m[32mprint(my_dict.items())[m
[32m+[m[32mfor i, (key,value) in enumerate(my_dict.items()):[m
[32m+[m[32m    print(i,key,value)[m[41m    [m
\ No newline at end of file[m
