from django.urls import path
import learn.views
urlpatterns = [
    path('',learn.views.index,name = 'index1'),
    path('index1',learn.views.index,name = 'index1'),
    path('course',learn.views.course_single,name = 'course'),
    path('news',learn.views.news,name = 'news'),
    path('about',learn.views.about,name = 'about'),
    path('registration',learn.views.registration,name='registration'),
    path('sec_reg',learn.views.sec_reg,name='sec_reg'),
    path('admin_reg',learn.views.admin_reg,name='admin_reg'),
    path('teacher_reg',learn.views.teacher_reg,name='teacher_reg'),
    path('student_reg',learn.views.student_reg,name='student_reg'),
    path('login',learn.views.login,name='login'),
    path('adminhome',learn.views.adminhome,name='adminhome'),
    path('add_blog', learn.views.add_blog, name='add_blog'),
    path('view_blog', learn.views.view_blog, name='view_blog'),
    path('contact', learn.views.contact, name='contact'),
    path('admin', learn.views.admin, name='admin'),
    path('update_prof', learn.views.update_prof, name='update_prof'),
    path('adm_prof', learn.views.adm_prof, name='adm_prof'),
    path('del_admin/<id>', learn.views.del_admin, name='del_admin'),
    path('edit_admin', learn.views.edit_admin, name='edit_admin'),
    path('bnb', learn.views.bnb, name='bnb'),
    path('blogs_admin', learn.views.blogs_admin, name='blogs_admin'),
    path('blog_approves/<id>', learn.views.blog_approves, name='blog_approves'),
    path('blog_rejects/<id>', learn.views.blog_rejects, name='blog_rejects'),
    path('blog_delete/<id>', learn.views.blog_delete, name='blog_delete'),
    path('upload_cert',learn.views.upload_cert, name= 'upload_cert'),
    path('del_cer',learn.views.delete_cert, name= 'del_cer'),
    path('about_content',learn.views.about_content, name= 'about_content'),
    path('block',learn.views.block, name= 'block'),
    path('feedbak',learn.views.feedbak, name= 'feedbak'),
    path('pass_req',learn.views.pass_req, name= 'pass_req'),
    path('sub_ad',learn.views.subject_ad, name= 'sub_ad'),
    path('message',learn.views.member_messages, name= 'message'),
    path('guest_message',learn.views.guest_messages, name= 'guest_message'),
    path('chapter_ad', learn.views.chapter_ad, name='chapter_ad'),
    path('cont_ad', learn.views.cont_ad, name='cont_ad'),
    path('logout', learn.views.logout, name='logout'),
    path('block', learn.views.block, name='block'),
    path('blocks/<id>', learn.views.blocks, name='blocks'),
    path('blocks1/<id>', learn.views.blocks, name='blocks1'),
    path('allows/<id>', learn.views.allows, name='allows'),
    path('allows1/<id>', learn.views.allows1, name='allows1'),
    path('teacher_prof', learn.views.teacher_prof, name='teacher_prof'),
    path('student_progress', learn.views.student_progress, name='student_progress'),
    path('change_password', learn.views.change_password, name='change_password'),
    path('subject', learn.views.subject, name='subject'),
    path('chapter', learn.views.chapter, name='chapter'),
    path('chapter_content', learn.views.chapter_content, name='chapter_content'),
    path('Student_booked_details', learn.views.Student_booked_details, name='Student_booked_details'),
    path('teacher_messages', learn.views.teacher_messages, name='teacher_messages'),
    path('attendence', learn.views.attendence, name='attendence'),
    path('scedule_test', learn.views.scedule_test, name='scedule_test'),
    path('delete_scedule_test', learn.views.delete_scedule_test, name='delete_scedule_test'),
    path('results', learn.views.results, name='results'),
    path('logout', learn.views.logout, name='logout'),
    path('tupdate_prof', learn.views.tupdate_prof, name='tupdate_prof'),



]