def bubble_sort(unsorted_list):
    def bubble_sort(unsorted_list):
    #To access each element in the list,
        for i in range(len(unsorted_list)):
            #To comapare the current element with its next element.
            for j in range(0, len(unsorted_list) - i -1):
                #If the current element is greater than the next element...
                if unsorted_list[j] > unsorted_list[j+1]:
                    # Swapping the elements
                    temp = unsorted_list[j]
                    unsorted_list[j] = unsorted_list[j+1]
                    unsorted_list[j+1] = temp
    return unsorted_list
