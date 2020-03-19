import inspect
import re
import json


################################################
###   Serialization to JSON

TAB = '\t'
NEWLINE = '\n'
COMMA = ','
LEVEL = 0
OUTPUT=""
file= ''

#create a bool that is true add comma if not then nothing

def addComma(bool):
    if bool==True:
        return ','
    else:
        return ''

def putInQuotes(string):
    return '\"'+string+'\"'

def to_json_str(string, obj, level, comma):
    item = obj.__dict__[string].replace("\\",r"\\")
    item = item.replace('"',r'\"')
    file.write(NEWLINE+TAB*(level+1)+putInQuotes(string) +': '+putInQuotes(item)+addComma(comma))
    print(TAB*(level+1)+putInQuotes(string) +': '+putInQuotes(item)+addComma(comma))

def to_json_float(string, obj, level, comma):
    file.write(NEWLINE+TAB*(level+1)+putInQuotes(string)+': '+str(obj.__dict__[string])+addComma(comma))
    print(TAB*(level+1)+putInQuotes(string)+': '+str(obj.__dict__[string])+addComma(comma))

def to_json_bool(string, obj, level, comma):
    #return output+TAB*(level+1)+putInQuotes(string)+': '+str(obj.__dict__[string]).lower()+COMMA+NEWLINE
    file.write(NEWLINE+TAB*(level+1)+putInQuotes(string)+': '+str(obj.__dict__[string]).lower()+addComma(comma))
    print(TAB*(level+1)+putInQuotes(string)+': '+str(obj.__dict__[string]).lower()+addComma(comma))

def to_json_int(string, obj, level, comma):
    #return output+TAB*(level+1)+putInQuotes(string)+': '+str(obj.__dict__[string])+COMMA+NEWLINE
    file.write(NEWLINE+TAB*(level+1)+putInQuotes(string)+': '+str(obj.__dict__[string])+addComma(comma))
    print(TAB*(level+1)+putInQuotes(string)+': '+str(obj.__dict__[string])+addComma(comma))

def to_json_obj(item, obj, level, comma):
    # print(obj)
    # print(obj.__class__.__qualname__.lower())
    # print(item)
    # output = output + TAB*(level+1) + putInQuotes(str(item))+': {'+NEWLINE
    file.write(NEWLINE+TAB*(level+1) + putInQuotes(str(item))+': {')
    print(TAB*(level+1) + putInQuotes(str(item))+': {')
    #output= output+ to_json(obj.__dict__[item], level=level+1)
    to_json(obj.__dict__[item], level=level+1)
    if level- LEVEL<0:
        file.write(NEWLINE+TAB*(level+1)+'}'+addComma(comma))
        print(TAB*(level+1)+'}'+addComma(comma)) 
    #return output

functions= {
    'str': to_json_str,
    'float': to_json_float,
    'bool': to_json_bool,
    'int': to_json_int,
}

def add_objects_to_functions(obj):
    count=0
    for item in obj.__dict__:
        count+=1
        if obj.__dict__[item].__class__.__qualname__.lower() not in functions:
            functions[obj.__dict__[item].__class__.__qualname__.lower()]=to_json_obj
    


def to_json(obj, level=0):
    '''Serializes the given object to JSON, printing to the console as it goes.'''
    global LEVEL
    global file
    if level==0:
        add_objects_to_functions(obj)
        #OUTPUT="{"+NEWLINE
        file=open("output.json",'w+')
        file.write('{')
        print('{')
    count1=0
    count2=0
    comma=True
    # if level-LEVEL>0:
    #     print(TAB*(level)+'}'+addComma(True)) 
    if level- LEVEL<0:
        file.write(NEWLINE+TAB*(level)+'}'+addComma(False))
        print(TAB*(level)+'}'+addComma(False)) 
        OUTPUT=OUTPUT+NEWLINE+TAB*(level)+'}'+addComma(False)
    for item in obj.__dict__:
        count1+=1
    for item in obj.__dict__:
        count2+=1
        if count1==count2:
            comma=False
        if obj.__dict__[item] is None or obj.__dict__[item]=='nil' or obj.__dict__[item]=='null':
            #OUTPUT=OUTPUT+TAB*(level+1)+putInQuotes(item)+ ': null'
            file.write(NEWLINE+TAB*(level+1)+putInQuotes(item)+ ': null'+addComma(comma))
            print(TAB*(level+1)+putInQuotes(item)+ ': null'+addComma(comma))
        else:
            functions[obj.__dict__[item].__class__.__qualname__.lower()](item,obj, level, comma)
    if level==0:
        file.write(NEWLINE+TAB*(level)+'}')
        print(TAB*(level)+'}')
        file.close()
    LEVEL=level
    return ''

