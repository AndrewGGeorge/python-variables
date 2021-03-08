'''
Variable Assignment
'''

# add 'Andrew' to the variable 'name'
#name= "Andrew"
#print(name)

#==================

#assign same value to multiple variables on the same line
#a = b = c = 'cat'
#print(a)
#print(b)
#print(c)

#===================

#reuse variable names, the last assignment is printed
#colour = 'red'
#colour = 'blue'

#print(colour)

#==================

#legal names
#firstname = 'john'
#first_name = 'john'
#_firs_tname = 'john'
#firstName = 'john'
#firstname2 = 'john'
#FIRSTNAME = 'john'

#illegal names
#2firstname = 'john'
#first-name = 'john'
#first name = 'john'

#==================

'''
Reserved Keywords
'''
#help("Keywords")
# use this to find out the kewords you cant use, example below 
#from ="London"
#print(from)

#==================

# variable types
#var = "hello world"
#print(type(var))

#var = 23
#print(type(var))

'''
Object identity
'''
score = 400
identity = id(score)
print(identity)

#==================

# score variable is saved into the pb by reference

#score = 400 
#pb = score
#print(id(score))
#print(id(pb))