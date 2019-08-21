from sitechecker.models import Site

from django.core.management.base import BaseCommand, CommandError
#from polls.models import Question as Poll

class Command(BaseCommand):
    help = 'Add new site to the database'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str)
        parser.add_argument('description', type=str)
        parser.add_argument('username', type=str)
# Optional args       parser.add_argument('--name', type=str)

    def handle(self, *args, **options):
#        print('Hello')
        new_site = Site(url=options['url'], description=['Description_Hello'])
        try:
            new_site.save()
            self.stdout.write(self.style.SUCCESS('Site added Successufully :%s -%s' %(options['url'],options['description'])))
        except Exception as e:
            self.stdout.write(self.style.ERROR('Hello there is an error in adding site, %s.' % e))
 #       self.stdout.write(self.style.ERROR('Thank you, %s.' % options['name']))
#       self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))
