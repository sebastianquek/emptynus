from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('interval', hours=24)
def timed_job():
    print('This job is run every 24 hours.')

sched.start()