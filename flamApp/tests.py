from django.db.models.fields import files
from django.test import TestCase
from .models import ImagePro
from django.core.files import File
from PIL import Image
# Create your tests here.


class ImageTestCase(TestCase):

    def setUp(self):
        self.img = ""
        # test to check whether the image is saved or not
        self.img1 = ImagePro.objects.create(image = File(file=b"./media/testing/test1.jpg"))

        # test to check rotatation of image work or not
        self.img2 = ImagePro.objects.create(image = File(file=b"./media/testing/test2.jpg"), rotate_by=10)

        # # test to check flipping of image work or not
        self.img3 = ImagePro.objects.create(image = File(file=b"./media/testing/test3.jpg"),flip_to="flip left right")

        # # test to check color transformation work or not
        self.img4 = ImagePro.objects.create(image = File(file=b"./media/testing/test4.jpg"),color_transform="l")

    def test_image_exist_or_not(self):
        self.assertEqual(self.img1.pk, 1)

    def test_image_rotate(self):
        self.assertEqual(self.img2.rotate_by, 10)

    def test_image_flip(self):
        self.assertEqual(self.img3.flip_to, "flip left right")

    def test_image_color_transform(self):
        self.assertEqual(self.img4.color_transform, "l")