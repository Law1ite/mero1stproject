grade={'ram':'A+','hari':'A'} #(dictionary)
result=list(grade.values())
step2=result.count('A+')
print(step2)

user_input='ilove python python'
result=user_input.count('python')
print(result)

#replace method
user_input = 'i love python pythor programming'
updated_input = user_input.replace('python', 'java')
print(updated_input)

user_input = 'ram'
result=(user_input.maketrans('rm', 'RM'))
print(user_input.translate(result))


#skivalue of alphabate
print(ord('A'))

full_name='  Laxmi  prasad  devkota  '
print(full_name.rstrip().replace(" ","_"))



input='I love south indian movies'.title()
step1=input.split()
print(''.join(step1[::-1]))


email='laxman.kc123@gmail.com'
s1=email.split('@')[0]
s2 = s1.replace('.','')
print(s2)