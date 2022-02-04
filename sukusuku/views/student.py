from django.shortcuts import render
from django.http import HttpResponse
from ..models import User, Role
from import_export import resources
from django.views.decorators.csrf import csrf_exempt
import json
import tablib
import pandas as pd

# Create your views here.


def find(request):  # メールアドレスで検索を行いJsonファイルでuser情報を表示する。
    data = list(User.objects.filter(roleid_id='student').values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    return HttpResponse(json_str)


def find2(request):  # 学籍番号で検索を行いJsonファイルでuser情報を表示する。
    userid = request.GET['userid']
    data = list(User.objects.filter(userid=userid).values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    return HttpResponse(json_str)


def create(request):  # メールアドレスで検索を行いJsonファイルでuser情報を表示する。
    mail = request.GET['mail']
    userid = request.GET['userid']
    role = request.GET['roleid_id']
    username = request.GET['username']
    roletemp = Role.objects.get(roleid=role)
    users = User(userid=userid, mail=mail, roleid=roletemp, username=username)
    users.save()

    data = list(User.objects.all().values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    return HttpResponse(json_str)


def delete(request):
    userid = request.GET['userid']
    user = User.objects.get(userid=userid)
    user.delete()

    data = list(User.objects.all().values())
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    return HttpResponse(json_str)


@csrf_exempt
def useradd(request):
    if request.method == 'POST':
        headers = ('userid', 'mail', 'roleid', 'username')
        data = []
        df = pd.read_excel(request.body, sheet_name='Tablib Dataset',)
        for i in range(len(df)):
            data.append([df.iat[i, 0], df.iat[i, 1],
                        df.iat[i, 2], df.iat[i, 3]])
        user_resource = resources.modelresource_factory(
            model=User, resource_class=UserResource)()
        dataset = tablib.Dataset(*data, headers=headers)
        user_resource.import_data(dataset)

        data = list(User.objects.all().values())
        json_str = json.dumps(data, ensure_ascii=False, indent=2)
        return HttpResponse(json_str)


class UserResource(resources.ModelResource):
    class Meta:
        model = User
        import_id_fields = ["userid"]
