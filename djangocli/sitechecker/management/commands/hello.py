from django.core.management.base import BaseCommand, CommandError
#from polls.models import Question as Poll

class Command(BaseCommand):
    help = 'Test command that says hello'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str)
# Optional args       parser.add_argument('--name', type=str)

    def handle(self, *args, **options):
        print('Hello')
        self.stdout.write(self.style.SUCCESS('Hello, %s.' % options['name']))
        self.stdout.write(self.style.ERROR('Thank you, %s.' % options['name']))
#       self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))
