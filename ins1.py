def mer(file_path):
    # Read input from text file
    with open(file_path, 'r') as file:
        # First line contains the first array
        A = list(map(int, file.readline().strip().split()))
        # Second line contains the second array
        B = list(map(int, file.readline().strip().split()))
    
    # Merge procedure
    result = []
    i = j = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            result.append(A[i])
            i += 1
        else:
            result.append(B[j])
            j += 1
    
    # Append remaining elements
    result.extend(A[i:])
    result.extend(B[j:])
    
    # Optional: write output to file
    with open('output.txt', 'w') as outfile:
        outfile.write(' '.join(map(str, result)))
    
    return result

print(mer('mer.txt'))