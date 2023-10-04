def selectionSort(self, arr,n):
        for m in range(len(arr)):
            minindex=m
            for n in range(m+1,len(arr)):
                if arr[n]<arr[minindex]:
                    minindex=n
            arr[m],arr[minindex]=arr[minindex],arr[m]
