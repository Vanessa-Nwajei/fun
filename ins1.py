def ins(input_file):
     with open(input_file, 'r') as f:
        # First line is the number of elements
        n = int(f.readline().strip())
        # Second line contains the array elements
        A= list(map(int, f.readline().split()))
        swaps = 0
        for i in range(1,len(A)):
            k = i
            while k > 0 and A[k]<A[k-1]:
                A[k], A[k-1] = A[k-1], A[k]
                k -= 1
                swaps +=1
        return swaps
     

print(ins('rosalind_ins.txt'))