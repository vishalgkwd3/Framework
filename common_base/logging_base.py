import logging
import datetime

#create an instance of logger
logger = logging.getLogger('simple logger')

current_time = datetime.datetime.now().strftime("%I-%M-%B-%d-%Y")
log_path = './logs/'+current_time

#create log handlers
handler = logging.FileHandler(log_path+'.log')
handler.setLevel(logging.DEBUG)

#create formatter & set it in handler
formatter = logging.Formatter('%(asctime)s - %(name)s %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.setLevel(level=logging.DEBUG)
logger.addHandler(handler)

