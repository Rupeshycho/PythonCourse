course='python for Beginners'
print(len(course))
print(course.upper())
print(course.lower())
print(f'The B is found at index: {course.find('B')}')
print(course.replace('Beginners','Absolute Beginners'))

replaced=course.replace('p','j')
print(replaced)

course2="python course"
rep=course2.replace('python',"Java")
print(rep)

#"str" in variable d
print('python' in course )
print('Java' in rep)

module="python for beginners"
print(len(module))
print(module.upper())
print(module.lower())
print(module.title())
print(module.find('f'))
print(module.replace("python", "Java"))
print(module.find('b'))

print(f'b is found at index: {module.find('b')} ')
print('b' in course) #true -> b in beginners at index: 12