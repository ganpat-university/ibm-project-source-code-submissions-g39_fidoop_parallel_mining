from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.shortcuts import redirect, reverse
from user_profile.forms import UserProfileModelForm, UserDetailModelForm


# Create your views here.


class UserProfileView(TemplateView, LoginRequiredMixin):
    template_name = "user_profile/profile.html"

    def post(self, request, *args, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['user_profile_form'] = user_profile_form = UserProfileModelForm(request.POST, request.FILES,
                                                                                instance=request.user.user_profile)
        context['user_detail_form'] = user_detail_form = UserDetailModelForm(request.POST,
                                                                             instance=request.user)
        if user_profile_form.is_valid() and user_detail_form.is_valid():
            user_profile_form.save()
            user_detail_form.save()
            return redirect(reverse('profile'))
        else:
            print(user_profile_form.errors, "++++++")

        return render(request, self.template_name, context=context)

    def get(self, request, *args, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['user_profile_form'] = UserProfileModelForm(instance=request.user.user_profile)
        context['user_detail_form'] = UserDetailModelForm(instance=request.user)
        return render(request, self.template_name, context=context)


class UserStatusView(TemplateView, LoginRequiredMixin):
    template_name = "user_profile/status.html" 

class UserUploadView(FormView, LoginRequiredMixin):
    template_name = "dashboard/dashboard_with_pivot.html"
    form_class = UserProfileModelForm
    success_url = '/accounts/profile/'

    def form_valid(self, form):
        form.save()
        return super(UserUploadView, self).form_valid(form) 

# 

class UserUploadSuccessView(TemplateView, LoginRequiredMixin):
    # print(">>>>>>hiii")
    # open upload_success.html
    template_name = "user_profile/upload_success.html"
    # save the file to the media folder
    # return the file data to template
    
    def get(self, request, *args, **kwargs):
        #print("1",request)
        return render(request, self.template_name)
    def post(self, request, *args, **kwargs):
        # fetch the uploaded file
        # save it to the media folder
        # return the file data to template
        return render(request, self.template_name)
    def get_context_data(self, **kwargs):
        context = super(UserUploadSuccessView, self).get_context_data(**kwargs)
        return context
    
# create dashborad view 
# create pivot data view

class DashboardView(TemplateView, LoginRequiredMixin):
    template_name = "user_profile/dashboard_with_pivot.html"

