##############################################################################################################################################################
##Problem: So in this problem we are given two lists and in each list speed of a cyclist is given. We have match the two lists in such a way that we get the 
##         maximum or minimum number out of both lists. 
##Solution: The solution is that in case we wanted max numbers we sorted one array in ascending and other in descending. So that when we match them we get the
##          max number and also during matching our second pair is the smallest of the array. In this way our largest numbers are saved. For example during our
##          sorting of red and blue we get [2,....] and [7,....]. So when we match them our highest is 7 and also the 2 is smallest.
##############################################################################################################################################################
def checkSpeed(red_shirt_bicycle,blue_shirt_bicycle,a):
    speed_list = []
    if(a == "MAX"):
        red_shirt_bicycle.sort()
        blue_shirt_bicycle.sort(reverse=True)
    elif(a == "MIN"):
        red_shirt_bicycle.sort()
        blue_shirt_bicycle.sort()
    
    for ind,val in enumerate(red_shirt_bicycle):
        speed_val = max(red_shirt_bicycle[ind],blue_shirt_bicycle[ind])
        speed_list.append(speed_val)
    print(speed_list)

red_shirt_bicycle = [5,5,3,9,2]
blue_shirt_bicycle = [3,6,7,2,1]
a = "MIN"

checkSpeed(red_shirt_bicycle,blue_shirt_bicycle,a)


##############################################################################################################################################################
##Time Comlexity: The time complexity is nlogn from sorting, n for iterating through a list, n for checking the max. So it is O(nlogn)
##Space Complexity: The space complexity is O(n) as we are saving a new list by name of speed_list
#############################################################################################################################################################
