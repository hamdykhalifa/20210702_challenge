def n_sum(n):
    sum = 0
    for number in n:
        sum += number

    return sum


def get_n(array, i):
    if(i == 0):
        return array[0:2]

    elif(i == len(array)-1):
        return array[i-1:i+1]

    else:
        return array[i-1:i+2]


def solution(array):
    add_counter = 0

    for i, x in enumerate(array):
        sum = n_sum(get_n(array, i))

        if(sum < 0):
            add_counter += abs(sum)

            if(i != len(array)-1):
                array[i+1] += abs(sum)
            else:
                array[i] += abs(sum)

    return add_counter


env = [-2, 1, -3, 1]
print(solution(env))
