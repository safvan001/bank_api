import csv
from django.core.management.base import BaseCommand
from bank.models import Bank, Branch

class Command(BaseCommand):
    help = 'Imports bank branches from a CSV file'

    def handle(self, *args, **kwargs):
        csv_file_path = r'C:\Users\User\Documents\bank_branches.csv'

        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Get or create the bank by bank_id and bank_name
                bank, created = Bank.objects.get_or_create(id=row['bank_id'], defaults={'name': row['bank_name']})

                # Create the branch entry
                Branch.objects.create(
                    ifsc=row['ifsc'],
                    bank=bank,
                    branch=row['branch'],
                    address=row['address'],
                    city=row['city'],
                    district=row['district'],
                    state=row['state']
                )
        
        self.stdout.write(self.style.SUCCESS('Successfully imported branches from CSV'))
