from apscheduler.schedulers.background import BackgroundScheduler

from sample_function import message_print, job_print
if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(message_print, trigger='interval', seconds=2, coalesce=True, max_instances=1)
    #                어떤 function을 어떤 trigger 방식으로 2초마다  instance는 무조건 1개라는 의미(다른 function을 동시에 시작하게 될 경우를 대비)
    # interval = 바로 동작시킨다
    scheduler.add_job(job_print, trigger='interval', seconds=2, coalesce=True, max_instances=1)
    
    scheduler.start()
    pass

    # 무한루프에 넣어둬야 계속 정상적으로 동작함(무한루프 = 응답 지속 계속 기다림.)
    while True:
        pass