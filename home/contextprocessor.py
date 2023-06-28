from .models import Category
from datetime import date
import nepali_datetime 

# context processor to send context data to base.html

def message_processor(request):
    categories=Category.objects.all()
    dateeng=date.today()
    datenep=nepali_datetime.date.today()
    dateeng=dateeng.strftime("%d %B %Y")
    d1=datenep.strftime("%K-%n-%D (%k %N %G)")
    return {'categories':categories, 'dateeng':dateeng, 'datenep':d1,}