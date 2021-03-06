from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect, HttpResponse
from ecommerce.forms import UserForm, AffiliateForm,AffiliateForm2
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string
from .models import Account_aff

def ecommerce_home(request):
	context={
	 	"title":"Welcome"
	 	}
	# if request.user.is_authenticated():
	# 	context={
	# 	"title":"Welcome"
	# 	}
	# else:
	# 	context={
	# 	"title":"Fuck off"
	# 	}
	return render(request,"index.html",context)

def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == "POST":
    	#return "hi"
    	#print 'hi'
    	# return render_to_response(
     #        'registration.html',
     #        {'registered': registered,'d':request.method},context)
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
    # Render the template depending on the context.
    return render_to_response(
            'register.html',
            {'user_form': user_form,'registered': registered,'d':request.method},
            context)

'''login_Waala'''


def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']
        print username,password
        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)
        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            print 'hi'
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/ecommerce/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Pickonn account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('login.html', {}, context)


''' logout waala'''
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/ecommerce/')

def user_order(request):
    context = {
        'title':'My Orders',
    }
    return render(request,'orders.html',context)

def product_detail(request):
    context={
        'title':'prod',
    }
    return render(request,'products.html',context)

def affiliate(request):
    context = RequestContext(request)
    if request.method == 'POST':
        aff_id = request.POST['aff_id']
        password = request.POST['password']
        print aff_id,password
        b = Account_aff.objects.filter(affliate_id=aff_id)
        username =  b[0]
        user = authenticate(username=username, password=password)
        if user:
            print 'hi'
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/ecommerce/')
            else:
                return HttpResponse("Your Pickonn account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render_to_response('index_aff.html', {'title':'Affiliate'}, context)


def aff_register(request):
    context = RequestContext(request)
    registered = False
    if request.method == "POST":
        aff_form = AffiliateForm(data=request.POST)
        aff_form2 =AffiliateForm2(data=request.POST)
        print aff_form2
        # If the two forms are valid...
        if aff_form.is_valid() and aff_form2.is_valid():
            print 'ff'
            # Save the user's form data to the database.
            aff = aff_form.save()
            
            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user 0bject.
            password = get_random_string(length=15)
            AFF_ID = get_random_string(length=10).upper()

            aff.set_password(password)
            aff.save()
            aff2 = aff_form2.save(commit=False)
            aff2.user = aff
            aff2.affliate_id = AFF_ID
            aff2.save()
            # Update our variable to tell the template registration was successful.
            registered = True
        else:
            print aff_form2.errors
            error = ''
            if(aff_form.errors):
                for key in aff_form.errors:
                    error = error+aff_form.errors[key]+'\n'
            elif(aff_form2.errors):
                for key in aff_form2.errors:
                    error = error+aff_form2.errors[key]+'\n'
            return render_to_response('aff_register.html',{'error':error},context)
        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
    else:
        #print password
        aff_form = AffiliateForm()
        aff_form2 = AffiliateForm2()
    return render_to_response('aff_register.html',{'aff_form': aff_form,'aff_form2':aff_form2,'registered':registered},context)