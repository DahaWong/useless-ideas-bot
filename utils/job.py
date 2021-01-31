import datetime

def run(job_queue, poster):
  morning = datetime.time(7,51)# AM 7:15
  job_queue.run_daily(poster.post, time=morning)
