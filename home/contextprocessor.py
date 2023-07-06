from .models import Category, Author
from datetime import date
import nepali_datetime 

# context processor to send context data to base.html

def message_processor(request):
    development=Category.objects.filter(priority=2)
    cappa=Category.objects.all().exclude(priority=2).order_by('priority')[0:3]
    engsug=Category.objects.get(priority=6)
    dateeng=date.today()
    datenep=nepali_datetime.date.today()
    dateeng=dateeng.strftime("%d %B %Y")
    d1=datenep.strftime("%K-%n-%D (%k %N %G)")
    if request.user.is_authenticated:
        current_user=Author.objects.get(user=request.user)
        return {'aalu':cappa, 'dateeng':dateeng, 'datenep':d1,'current_user':current_user,'development':development,'engsug':engsug,}
    else:
        return {'aalu':cappa, 'dateeng':dateeng, 'datenep':d1,'development':development,'engsug':engsug,}
        