import datetime

def log_fish(fish_data):
    try:
        log = open("diary.txt", "a+")
    except:
        pass
    fishName = fish_data.type
    fishWeight = fish_data.weight
    fishSize = fish_data.size
    timestamp = datetime.datetime.now()

    logString = f"Timestamp: {timestamp}\nFish: {fishName}\nSize: {fishSize} inches\nWeight: {fishWeight} lbs\n----------------------------------\n"

    log.write(logString)

    log.close()
    