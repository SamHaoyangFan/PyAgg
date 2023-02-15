import logging

from django.conf import settings
from django.core.management.base import BaseCommand

import feedparser
from dateutil import parser
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution

from news.models import Post

logger = logging.getLogger(__name__)

def save_new_posts(feed):
    feed_title = feed.channel.title
    feed_image = feed.channel.image['href']


    for item in feed.entries:
        if not Post.objects.filter(link=item.link).exists():
            post = Post(
                title=item.title,
                description=item.description,
                pubdate=parser.parse(item.published),
                link=item.link,
                image=feed_image,
            )
            post.save()

def fetch_first_posts():
    #Please parse RSS feed for the news address
    _feed = feedparser.parse("")
    save_new_posts(_feed)

def fetch_second_posts():
    _feed = feedparser.parse("")
    save_new_posts(_feed)

def delete_old_job_executions(max_age=604_800):
    DjangoJobExecution.objects.delete_old_job_executions(max_age)

class Command(BaseCommand):
    help = "Runs apscheduler."
    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            fetch_first_posts,
            trigger="interval",
            minutes=2,
            id="The First News",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job: The first news feed.")

        scheduler.add_job(
            fetch_second_posts,
            trigger="interval",
            minutes=2,
            id="The Second News",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job: The second news feed.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),
            id="Delete Old Job Executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added weekly job: Delete Old Job Executions.")
        
        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")
