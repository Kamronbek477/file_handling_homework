def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    i=0
    sum=0
    while i<len(data):
        if data[i].isdigit():
            sum+=int(data[i])
        i+=1
    return sum

f=open('txt_file/data07.txt').read()
data=f
print(main(data))


# Read data from file