import sys

try:
    f = open('courses.txt')
except:
    print('file does not exist')
    sys.exit(0)

courses = {}
data = f.readlines()

for line in data:
    tmp = line.split(',')
    print(tmp)
    try:
        tmp[1] = int(tmp[1])
        courses[tmp[0]] = tmp[1]
    except:pass
f.close()

#Q7a
try:
    cname = input('enter course name: ')
    print(f'count for course {cname} is {courses[cname.capitalize()]}')
except:
    print('Course name does not exist')

#Q7b
choice = input('Want to add course?[y,n] ')
if choice.lower() == 'y':
    name = input('Enter course name: ')
    count = int(input('Enter count: '))
    courses[name.capitalize()] = count
    try:
        f = open('courses.txt','a')
        f.write(name+', '+str(count)+' \n')
        f.close()
    except:
        print('file does not exist')
        sys.exit(0)
else :
        sys.exit(0)
