from .models import Category, Author, Post, advertisement
from datetime import date
import nepali_datetime 


# context processor to send context data to base.html

def message_processor(request):
    development=Category.objects.filter(priority=2)
    posters=Post.objects.filter(approved=True).order_by('-timestamp')[:5]
    news=Category.objects.get(priority=8)
    cappa=Category.objects.all().exclude(priority__in=[2,3]).order_by('priority')[0:2]
    # cappa=Category.objects.all()
    # cappa=cappa.objects.exclude(priority=[2,3])
    engsug=Category.objects.get(priority=6)
    engedu=Category.objects.get(priority=3)
    dateeng=date.today()
    datenep=nepali_datetime.date.today()
    homepagetop = advertisement.objects.get(title='homepagetop')
    newsside=advertisement.objects.get(title='newspageside')
    dateeng=dateeng.strftime("%d %B %Y")
    d1=datenep.strftime("%K-%n-%D (%G)")
    
    newspagemobile = advertisement.objects.get(title='newspagemobile')
    
    
   
    if request.user.is_authenticated:
        current_user=Author.objects.get(user=request.user)
        return {'aalu':cappa, 'dateeng':dateeng, 'datenep':d1,'current_user':current_user,'development':development,'engsug':engsug,'scroller':posters,'newer':news,'homepagetop':homepagetop,'newsside':newsside,'engedu':engedu, 'newspagemobile':newspagemobile }
    else:
        return {'aalu':cappa, 'dateeng':dateeng, 'datenep':d1,'development':development,'engsug':engsug,'scroller':posters,'newer':news,'homepagetop':homepagetop,'newsside':newsside,'engedu':engedu, 'newspagemobile':newspagemobile}
        