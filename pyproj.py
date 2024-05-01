import time
def counterTimer(duration):
    while duration>=0:
        mins,sec=divmod(duration,60)#quotient and remainder
        timer=f"{mins:02d}:{sec:02d}"
        print(f"\nTime left:{timer}",end='',flush=True)
        time.sleep(1)
        duration-=1
        print("\nTime up!!")

def main():
    try:
        duration=int(input("Enter the duration in seconds"))
        if duration<0:
            raise ValueError("Duration must be non negative integer")
        counterTimer(duration)
    except ValueError as V:
        print(f"Error: {V}")
if __name__=="__main__":
    main()
