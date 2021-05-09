#  jail has a number of prisoners and a number of treats to pass out to them. Their jailer decides the fairest way to divide the treats is to seat the prisoners around a circular table in sequentially numbered chairs. A chair number will be drawn from a hat. Beginning with the prisoner in that chair, one candy will be handed to each prisoner sequentially around the table until all have been distributed.

# The jailer is playing a little joke, though. The last piece of candy looks like all the others, but it tastes awful. Determine the chair number occupied by the prisoner who will receive that candy.


def saveThePrisoner(n, m, s):


    # find the remainder of m and n
    # write down the remainder
    # add the (remainder - 1) to the s    

    # return the answer

    remainder = m % n

    if(remainder == 0):
        answer = n
    else:
        answer = s + (remainder - 1)

    return answer

for _ in range(1,10**9):
    print(f"{saveThePrisoner(5,_,1)} {_}" )

