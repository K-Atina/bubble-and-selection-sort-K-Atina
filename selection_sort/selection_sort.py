def selection_sort(arr):
    def selection_sort(arr):
        for i in range(len(arr)-1):
            #We will assume the minimum element is the first element
            min_index = i
            #Comparing the minimum elemet with the rest of the elements
            for j in range(i+1 , len(arr)):
                #We check if current element is less than the element we marked as the minimum
                if arr[j] < arr[min_index]:
                    #If true, value is reassigned 
                    min_index = j
                # Swapping the elements
                temp = arr[i]
                arr[i] = arr[min_index]
                arr[min_index]= temp
        return arr

