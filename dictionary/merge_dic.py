# Merge two dictionaries into one
dic ={
    input("enter key1 : ") : input("enter value1 : "),
    input("enter key2 : ") : input("enter value2 : "), 
}
dic2 = {
    input("enter key1 : ") : input("enter value1 : "),
    input("enter key2 : ") : input("enter value2 : "), 
}
dic.update(dic2)

print(dic)
