if __name__ == '__main__':
    N = int(input())
    result = []
    for _ in range(N):
        command = str(input())
        command_list = command.split(" ")
        if command_list[0] == 'insert':
            result.insert(int(command_list[1]), int(command_list[2]))
        elif command_list[0] == 'append':
            result.append(int(command_list[1]))
        elif command_list[0] == 'remove':
            result.remove(int(command_list[1]))
        elif command_list[0] == 'sort':
            result = sorted(result)
        elif command_list[0] == 'pop':
            result.pop()
        elif command_list[0] == 'reverse':
            result.reverse()
        else:
            print(result)
