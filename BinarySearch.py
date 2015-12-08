
mList = [5, 8, 9, 3, 11, 22, 19, 27, 0, -2, 60, 7, 98, 99, 56];
mList = sorted(mList);
print(mList);

#binary search
def binarySearch(mList, high, low, target):
        mid = 0;
        while low <= high:
                mid = (high + low) // 2;
                if mList[mid] == target:
                        return mid;
                elif mList[mid] > target:
                        high = mid - 1;
                elif mList[mid] < target:
                        low = mid + 1;
        return -1;

while 1:
        target = int(input("Please input your target number?\n"));
        location = binarySearch(mList, len(mList) - 1, 0, target);
        if(location == -1):
                print("Not found!\n");
        else:
                print("Yes, find it! It is at ", location, "\n");
        ask = input("Please press 'q' to quit, other key to continue!\n...");
        if(ask == 'q'):
                break;
                
