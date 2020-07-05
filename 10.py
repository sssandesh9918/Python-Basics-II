#CamelCased to snake_cased and to kebab_case_too
def camel_to_snake(string,seperator):
    str=''
    stri=''
    str=str+string[0].lower()
    stri=stri+string[0].lower()
    for i in range(1,len(string)):
        if string[i].isupper():
            str=str+'_'
            stri=stri+seperator
            str=str+string[i].lower()
            stri=stri+string[i].lower()
        else:
            str=str+string[i]
            stri=stri+string[i]
    return str,stri
string='ThisIsCamelCased'
seperator='-'
print(camel_to_snake(string,seperator))
