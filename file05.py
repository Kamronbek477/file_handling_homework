def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    x=0
    y=0
    i=0
    while i<len(data):
        if data[i].isdigit():
            x+=1
        else:
            y+=1
        
    return [x,y]

f=open('txt_file/data05.txt').read()
data=f
print(main(data))

# Read data from file