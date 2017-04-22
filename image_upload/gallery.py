import os
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.shortcuts import render_to_response

def gallery(request):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(BASE_DIR, 'static/image_upload/')
    # path=static("/image_upload")  # insert the path to your directory
    print('PATHTHTHTHT', path)
    img_list =os.listdir(path)
    for i in img_list:
        print(i)
    return render_to_response('image_upload/gallery.html', {'images': img_list})


# HttpResponseRedirect(request.META['HTTP_REFERER'])
