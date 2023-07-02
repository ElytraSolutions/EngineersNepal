from .models import Category, Author
from datetime import date
import nepali_datetime 

# context processor to send context data to base.html

def message_processor(request):
    categories=Category.objects.all()
    dateeng=date.today()
    datenep=nepali_datetime.date.today()
    dateeng=dateeng.strftime("%d %B %Y")
    d1=datenep.strftime("%K-%n-%D (%k %N %G)")
    if request.user.is_authenticated:
        current_user=Author.objects.get(user=request.user)
        return {'categories':categories, 'dateeng':dateeng, 'datenep':d1,'current_user':current_user}
    else:
        return {'categories':categories, 'dateeng':dateeng, 'datenep':d1}
        