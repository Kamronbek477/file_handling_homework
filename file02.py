def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """

# Read data from file
    x=0
    for i in data:
        x+=1
    return x
    
    
f = open('txt_file/data02.txt').read()
data=f
    
print(main((data)))