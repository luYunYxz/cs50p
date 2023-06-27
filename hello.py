# Ask user for their name

'''
this is the test many lines comments
'''
name = input("what is your name?")
name = name.strip()
name = name.title()
first, second = name.split()
# print(*objects,seq=' ',end='\n'); 当传入多个参数的俄时候,以空格分割符,以\n作为结尾
print(f"hello, \"my friend\" {name}" ,  end="")

print(f"the first name = {first}")

print(f"the second = {second}")