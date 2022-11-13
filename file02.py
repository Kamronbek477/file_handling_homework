def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """

# Read data from file

    x=[]
    for i in data.split(','):
        x.append(int(i))
    return x
f = open('txt_file/data02.txt').read()
data=f
print(len(data))