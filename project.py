
def get_friends_data():
    friends_data = {}
    while True:
        name = input("Enter the name of the person (or 'stop' to finish): ").strip()
        if name.lower() == 'stop':
            break
        friends = input(f"Enter the friends of {name}, separated by commas: ").strip().split(',')
        friends_data[name] = set(friend.strip() for friend in friends)
    return friends_data


def find_common_friends(person1, person2, friends_dict):
    if person1 not in friends_dict or person2 not in friends_dict:
        return "One or both people are not in the friends data."
    
    common_friends = friends_dict[person1].intersection(friends_dict[person2])
    
    return common_friends if common_friends else "No common friends."


def main():
    friends_data = get_friends_data()
    
    person1 = input("Enter the first person's name: ").strip()
    person2 = input("Enter the second person's name: ").strip()
    
    common_friends = find_common_friends(person1, person2, friends_data)
    print(f"Common friends of {person1} and {person2}: {common_friends}")

if __name__ == "__main__":
    main()
