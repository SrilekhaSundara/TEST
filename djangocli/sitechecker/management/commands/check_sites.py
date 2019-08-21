# Perform a HTTP GET Request to check if the site is up and returns a 200 OK message


from django.core.management.base import BaseCommand, CommandError
import requests
from django.utils import timezone
from django.utils.datetime_safe import datetime

from sitechecker.models import Site, Check


#from polls.models import Question as Poll

def get_url_list():
#    Site.objects.all()
    return Site.objects.all()
#    return['https://verygoodrecipes.com/andhra','https:/zomato.com']
#    pass
class Command(BaseCommand):
    help = 'Checks all the sites are running'


    def handle(self, *args, **options):
        print('Hello')
        self.stdout.write("[*] Checking all the Sites are running...")
        for site in Site.objects.all():
            response=requests.get(site.url,all_redirects=True)
            #TO DO MULTI THREADING
            self.stdout.write("Response: for %s: %s " % (site.url,response.status_code))
            site.last_response_code=str(response.status_code)
            site.last_time_checked = timezone.now()
            site.save()
#            new_check_entry.save()
            try:
                site.save()
            except Exception as e:
                self.stdout.write(self.style.ERROR('Hello there is an error in updating site_check, %s- %s.' % (e,site)))
            try:
                new_check_entry=Check(site=site,response_code=str(response.status_code))
                new_check_entry.save()

#               self.style.SUCCESS('Site added Successufully :%s -%s' % (options['url'], options['description']))
            except Exception as e:
                self.stdout.write(self.style.ERROR('Hello there is an error in adding site_check, %s- %s.' % (e, new_check_entry)))

        # Perform http rewuests
#        for site_url  in get_url_list():
#            response=requests.head(site_url)
            #Redirects

 #       self.stdout.write(self.style.SUCCESS('Hello, %s.' % options['name']))
 #       self.stdout.write(self.style.ERROR('Thank you, %s.' % options['name']))
        # Update the data base records and the last response and the timestamp

