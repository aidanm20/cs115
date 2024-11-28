original = [[1, 2, 3], [4, 5, 6]]

# Shallow copy using slicing
shallow = original[:]

# Modify an element in the nested list
shallow[0][0] = 99

print("Original:", original)  # The original list is affected
print("Shallow:", shallow) 
original = [[1, 2, 3], [4, 5, 6]]

# Function to create a deep copy
def deep_copy(obj):
    if isinstance(obj, list):  # Handle lists
        return [deep_copy(item) for item in obj]
    elif isinstance(obj, dict):  # Handle dictionaries
        return {key: deep_copy(value) for key, value in obj.items()}
    else:  # Handle other types (e.g., integers, strings)
        return obj

# Deep copy the original
deep = deep_copy(original)

# Modify an element in the nested list
deep[0][0] = 99

print("Original:", original)  # The original list remains unchanged
print("Deep:", deep)


def read_preferences(filename):
    dic = {}
    with open(filename, 'r') as file:
        for line in file:
            [username, singers] = line.strip().split(":")
            singersList = singers.strip().split(",")
      
            dic[username.rstrip()] = singersList
    return dic

userInfo = read_preferences("C:\Users\aidan\OneDrive\Desktop\cs115\nov22\recsys.txt")
for user in userInfo.keys():
    print(user,userInfo[user])
















