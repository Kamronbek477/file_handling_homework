def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    
    list=[]
    
    
    for i in data.split('\n'):
        list.append(len(i))
    return list

        

f=open('txt_file/data05.txt').read()
data=f
print(main(data))


# Read data from file