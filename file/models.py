from django.db import models
from django.conf import settings
import os


import io
from PIL import Image
import pytesseract
from wand.image import Image as wi

# Create your models here.


class Text(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="files"
    )
    file = models.FileField(upload_to="pdf/%Y/%m/")
    content = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return os.path.basename(self.file.name)

    pytesseract.pytesseract.tesseract_cmd = (
        "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    )

    def save(self, *args, **kwargs):
        pdfFile = wi(file=self.file, resolution=300)
        image = pdfFile.convert("jpeg")

        imageBlobs = []

        for img in image.sequence:
            imgPage = wi(image=img)
            imageBlobs.append(imgPage.make_blob("jpeg"))

        extract = []

        for imgBlob in imageBlobs:
            image = Image.open(io.BytesIO(imgBlob))
            text = pytesseract.image_to_string(image, lang="eng")
            extract.append(text)

        self.content = extract[0]
        super(Text, self).save(*args, **kwargs)
