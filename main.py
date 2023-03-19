# 221RDB128 Bernhards Arnitis
# python3

def parallel_processing(n, m, data):
    if not (1 <= n <= 10**5):
        raise ValueError("Invalid value for 'n'")
    if not (1 <= m <= 10**5):
        raise ValueError("Invalid value for 'm'")
    if not all(0 <= int(laiks) <= 10**9 for laiks in data):
        raise ValueError("Invalid data")
    treads = [(i, 0) for i in range(n)]
    output = []
    for i, laiks in enumerate(data):
            tread_num, sakt_laiks = treads[i % n]  
            output.append((tread_num, sakt_laiks))
            treads[i % n] = (tread_num, sakt_laiks + int(laiks))
                
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n, m = map(int, input().split())


    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = input().split()

    # TODO: create the function
    output = parallel_processing(n, m, data)
    
    # TODO: print out the results, each pair in it's own line
    for tread_num, sakt_laiks in output:
        print(tread_num, sakt_laiks)


if __name__ == '__main__':
    main()
