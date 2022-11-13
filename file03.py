def main(data:str):
    """
    The data is from the file. Return the numbers as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    
# Read data from file
    list = []
    i=0
    while i<len(data):
        if data[i].isdigit():
            list.append(data[i])
        i+=1
    return list

f = open('txt_file/data03.txt').read()
data = f
print(main(data))
