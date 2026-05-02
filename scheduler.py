from apscheduler.schedulers.blocking import BlockingScheduler
import batch_prediction 

scheduler = BlockingScheduler()

scheduler.add_job(batch_prediction.main, 'interval', minutes=5)

scheduler.start()