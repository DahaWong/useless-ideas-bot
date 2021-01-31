from config import update_info
from telegram.ext import Updater
from handlers.register import register
import utils.job as job
from utils.post_idea import IdeaPoster
 
updater = Updater(**update_info)
dispatcher = updater.dispatcher
register(dispatcher)

poster = IdeaPoster()
job_queue = updater.job_queue
job.run(job_queue, poster)

updater.start_polling()
updater.idle()