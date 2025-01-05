from django.shortcuts import render,redirect
from .models import Investment
from django.db.models import Sum

def home(request):# this define a function named storehome that take platforms one parameter to get the request
    #investment = Investment.objects.all()
    return render(request,'home.html',{})


def funding(request):
    if request.method == 'POST':
        member_name = request.POST['member_name']
        member_cpm = request.POST['member_cpm']
        investment_amount = request.POST['investment_amount']

        # Create a new investment record
        Investment.objects.create(
            member_name=member_name,
            member_cpm=member_cpm,
            investment_amount=investment_amount
        )
        return redirect('funding')
    
    #retive all investment record from the data base
    member_list = Investment.objects.all()
    
    #calculate the total investment amount
    total_investment = sum(Investment.objects.all().values_list('investment_amount', flat=True))
    #calculate the sum of investment field for all recodes
    
    #render the funding with the data list of investment and total investment amount
    return render(request, 'funding.html',{
        'member_list': member_list,
        'total_investment': total_investment,
    })

def member_info(request, member_name):
    member_investment = Investment.objects.filter(member_name=member_name)
    member_total = Investment.objects.filter(member_name=member_name).aggregate(total=Sum('investment_amount'))['total']
    
    return render( request,'member_info.html',
        {
            'member_investment':member_investment,
            'member_total':member_total,
        }
    )
    
    

