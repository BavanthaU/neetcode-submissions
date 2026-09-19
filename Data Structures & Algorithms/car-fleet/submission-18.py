class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_len =  len(position)
        if pos_len<2:
            return pos_len
        combined = sorted([[x,y] for x, y in zip(position, speed)])
        time = [(target-x)/y for x,y in combined]
        car_fleets=0
        streak = False
        slow_car_time = 0 
        for i in range(pos_len):
            if i < pos_len-1:
                close_car = time.pop()
                slow_car_time = max(close_car, slow_car_time)
                if time[-1] <= slow_car_time:
                    if not streak:
                        car_fleets+=1
                        streak = True
                else:
                    if not streak:
                        car_fleets+=1
                    streak = False
                    
            else:
                if not streak:
                    car_fleets+=1

        return car_fleets
        