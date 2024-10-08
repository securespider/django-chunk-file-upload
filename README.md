# Django Chunk File Upload

Django Chunk File Upload is an alternative utility that helps you easily edit Django's chunked, drag and drop file uploads.

<img src="https://i.ibb.co/9y2SgmS/f-P5-Or-Gkxk0-Ynj00ct-G.webp" alt="f-P5-Or-Gkxk0-Ynj00ct-G">

Features
----------
- Multiple file uploads.
- Drag and Drop UI.
- MD5 checksum file.
- Chunked uploads: optimizing large file transfers.
- Prevent uploading existing files with MD5 checksum.
- Easy to use any models.
- Image optimizer, resizer, auto convert to webp (supported webp, png, jpg, jpeg).
- Permissions.


Quickstart
----------

Install Django Chunk File Upload:
```shell
pip install git+https://github.com/thewebscraping/django-chunk-file-upload.git
```


Add it to your `settings.py`:

```python
INSTALLED_APPS = [
    'django_chunk_file_upload',
]
```

Add it to your `urls.py`:


```python
from django.urls import path, include

urlpatterns = [
    path("file-manager/", include("django_chunk_file_upload.urls")),
]
```

Run Demo

Demo URL: http://127.0.0.1:8000/file-manager/uploads/
```shell
cd examples
python manage.py migrate
python manage.py runserver
```

Change default config: `settings.py`

```python
DJANGO_CHUNK_FILE_UPLOAD = {
    "chunk_size": 1024 * 1024 * 2,  # # custom chunk size upload (default: 2MB).
    "upload_to": "custom_folder/%Y/%m/%d",  # custom upload folder.
    "is_metadata_storage": True,  # save file metadata,
    "remove_file_on_update": True,
    "optimize": True,
    "js": (
        "https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.1/jquery.min.js",
        "https://cdnjs.cloudflare.com/ajax/libs/spark-md5/3.0.2/spark-md5.min.js",
        "https://cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/toastr.min.js",
    ),  # use cdn.
    "css": (
        "custom.css"
     ),  # custom css path.
    "image_optimizer": {
        "quality": 82,
        "compress_level": 9,
        "max_width": 1024,
        "max_height": 720,
        "to_webp": True,  # focus convert image to webp type.
    },
    "permission_classes": ("django_chunk_file_upload.permissions.AllowAny",)  # default: IsAuthenticated
}

```

Custom Your Models
----------

models.py

```python
from django.db import models
from django_chunk_file_upload.models import FileManagerMixin


class Tag(models.Model):
    name = models.CharField(max_length=255)


class YourModel(FileManagerMixin):
    tags = models.ManyToManyField(Tag)
    custom_field = models.CharField(max_length=255)

```

forms.py

```python
from django_chunk_file_upload.forms import ChunkedUploadFileForm
from .models import YourModel


class YourForm(ChunkedUploadFileForm):
    class Meta:
        model = YourModel
        fields = "__all__"
```

views.py

Accepted methods: GET, POST, DELETE (UPDATE, PUT does not work with FormData).
```python
from django_chunk_file_upload.views import ChunkedUploadView
from django_chunk_file_upload.typed import File
from django_chunk_file_upload.permissions import IsAuthenticated
from .forms import YourForm


class CustomChunkedUploadView(ChunkedUploadView):
    form_class = YourForm
    permission_classes = (IsAuthenticated,)

    # file_class = File  # file class
    # file_status = app_settings.status  # default: PENDING (Used when using background task, you can change it to COMPLETED.)
    # optimize = True  # default: True
    # remove_file_on_update = True  # update image on admin page.
    # chunk_size = 1024 * 1024 * 2  # custom chunk size upload (default: 2MB).
    # upload_to = "custom_folder/%Y/%m/%d"  # custom upload folder.
    # template_name = "custom_template.html"  # custom template

    # # Run background task like celery when upload is complete
    # def background_task(self, instance):
    #     pass
```

custom_template.html
```html
<form action="."
      method="post"
      id="chunk-upload-form">
    {{ form.media }}
    {{ form }}
</form>
```

urls.py

```pyhon
from django.urls import path

from .views import CustomChunkedUploadView

urlpatterns = [
    path("uploads/", CustomChunkedUploadView.as_view(), name="custom-uploads"),
]
```

### Permissions
```python
from django_chunk_file_upload.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsSuperUser
```

### File Handlers
```python
from django_chunk_file_upload.typed import (
    ArchiveFile,
    AudioFile,
    BinaryFile,
    DocumentFile,
    File,
    FontFile,
    HyperTextFile,
    ImageFile,
    JSONFile,
    MicrosoftExcelFile,
    MicrosoftPowerPointFile,
    MicrosoftWordFile,
    SeparatedFile,
    XMLFile,
)
```

This package is under development, only supports create view. There are also no features related to image optimization. Use at your own risk.
