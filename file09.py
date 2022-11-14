def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """

# Read data from file
    x=0
    list=[]
    m=0
    while m<len(data):
        if data[m].isdigit():
            list.append(int(data[m]))
        m+=1
    for i in list:
        if i<x:
            x=i
    return x


f=open('txt_file/data08.txt').read()
data=f
print(main(data))