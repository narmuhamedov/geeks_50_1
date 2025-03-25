from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest

child_club = "Детский клуб"
teenager_club = "Подростковый клуб"
adult_club = "Взрослый клуб"


####
class AgeClubMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/register/' and request.method == 'POST':
            age = int(request.POST.get('age'))
            if age < 7:
                return HttpResponseBadRequest('Ваш возраст должен быть больше 7')
            elif age >= 7 and age < 12:
                request.club = child_club
            elif age >= 12 and age < 18:
                request.club = teenager_club
            elif age >= 18 and age < 45:
                request.club = adult_club
            else:
                return  HttpResponseBadRequest('Ваш возраст слишком высокий извините!')

        elif request.path == '/register/' and request.method == 'GET':
            setattr(request, 'club', "Клуб не определен")