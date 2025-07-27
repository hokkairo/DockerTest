from django.shortcuts import render
from .forms import TestForm  # 追加
from .models import Employee # 追加
from .forms import Employee # 追加
from django.shortcuts import redirect # 追加
from .forms import EmployeeAdd # 追加

# Create your views here.

def index(request):
    my_dict = {
        'insert_something':"views.pyのinsert_somethingの部分です。",
        'name':'Bob',
        'test_titles': ['title 1', 'title 2', 'title 3'],
        'form': TestForm(),  # 追加
        'insert_forms': '初期値',  # 追加
    }
    # 追加 -----
    if (request.method == 'POST'):
        my_dict['insert_forms'] = '文字列:' + request.POST['text'] + '\n整数型:' + request.POST['num']
        my_dict['form'] = TestForm(request.POST)
    # 追加 -----

    return render(request, 'index.html', my_dict)


# 追加 -----
def info(request):
    infodata = Employee.objects.all()
    header = ['ID','名前','メール','性別','部署','社歴','作成日']
    my_dict2 = {
        'title': 'テスト',
        'employees': infodata,
        'header':header
    }
    return render(request, 'webtestapp/info.html',my_dict2)

# 追加 -----
def create(request):
    message = ''  # 初期表示ではカラ
    if (request.method == 'POST'):
        form = EmployeeAdd(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='/info')
        else:
            message = '再入力して下さい'
    modelform_dict = {
        'title':'modelformテスト',
        'form': EmployeeAdd(),
        'message': message, # エラーメッセージ
    }
    return render(request, 'webtestapp/create.html', modelform_dict)

def update(request, num):
    message = ''
    employee_obj = Employee.objects.get(id=num)
    if (request.method == 'POST'):
        employee = EmployeeAdd(request.POST, instance=employee_obj)
        if employee.is_valid():
            employee.save()
            return redirect(to='/info')
        else:
            message = '再入力して下さい'
    update_dict = {
        'title': '登録情報更新画面',
        'id': num,
        'form': EmployeeAdd(instance=employee_obj),
        'message': message,
    }
    return render(request, 'webtestapp/update.html', update_dict)

def delete(request, num):
    header = ['ID','名前','メール','性別','部署','社歴','作成日']
    message = ''
    employee_obj = Employee.objects.get(id=num)
    if (request.method == 'POST'):
        employee_obj.delete()
        return redirect(to='/info')
    delete_dict = {
        'title': '削除画面',
        'header': header,
        'id': num,
        'employee': employee_obj,
        'message': message,
    }
    return render(request, 'webtestapp/delete.html', delete_dict)


