from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def extreme_conditions():
    print("check for extreme conditions")

sched.start()
        
    