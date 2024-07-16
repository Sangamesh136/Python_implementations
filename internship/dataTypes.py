a=10;
# integer data type
#  to know the datatype type() method is used
print(type(a));

c=1+2j
# here c is a complex data type of form x+yj where x is a real part and y is an imaginary part
print(type(c))
print(c);

# list
# list are mutable
d=[1,2,2.5,'a',"Name"]
print(type(d));
print(d);
# to print individual element of the list 
print(d[0]);

'''
 to insert any new element in the list, follow the syntax:
  listName.insert(index,element);
'''
d.insert(5,"HelloEveryOne");
print(d);

# tuple
# tuple is immutable
month=("jan","feb","march","april");
print(month);

# for string
e="name";
print(type(e));
print(e);

# for multiline comment we use '''...... ''' within the veriable
f= ''' Name: Sangamesh
       Age: 20
   '''
print(f);