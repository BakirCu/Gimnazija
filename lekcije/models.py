from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from lekcije.video_id import embed_video


class Lekcije(models.Model):
    PREDMETI = (("Matematika", "Matematika"),
                ("Fizika", "Fizika"),
                ("Srpski jezik i književnost", "Srpski jezik i književnost"),
                ("Srpski kao nematernji jezik", "Srpski kao nematernji"),
                ("Bosanski jezik i književnost", "Bosanski jezik i književnost"),
                ("Engleski jezik", "Engleski jezik"),
                ("Nemački jezik", "Nemački jezik"),
                ("Francuski jezik", "Francuski jezik"),
                ("Latinski jezik", "Latinski jezik"),
                ("Istorija", "Istorija"),
                ("Geografija", "Geografija"),
                ("Biologija", "Biologija"),
                ("Hemija", "Hemija"),
                ("Računarstvo i informatika", "Računarstvo i informatika"),
                ("Muzička kultura", "Muzička kultura"),
                ("Likovna kultura", "Likovna kultura"),
                ("Fizičko vaspitanje", "Fizičko vaspitanje"),
                ("Građansko vaspitanje", "Građansko vaspitanje"),
                ("Islamska veronauka", "Islamska veronauka"),
                ("Pravoslavna veronauka", "Pravoslavna veronauka"),
                ("Jezik medija i kultura", "Jezik medija i kultura"),
                ("Primenjene nauke", "Primenjene nauke"),
                ("Umetnost i dizajn", "Umetnost i dizajn"),
                ("Zdravlje i sport", "Zdravlje i sport"),
                ("Psihologija", "Psihologija"),
                ("Filozofija", "Filozofija"),
                ("Sociologija", "Sociologija"),
                ("Ustav i prava građana", "Ustav i prava građana"),
                )

    GODINE = (("Prva godina", "Prva godina"),
              ("Druga godina", "Druga godina"),
              ("Treća godina", "Treća godina"),
              ("Četvrta godina", "Četvrta godina"), )
    naslov = models.CharField(max_length=300)
    fajl = models.FileField(upload_to='lekcije', validators=[
                            FileExtensionValidator(['pdf', 'doc', 'docx', 'ppt', 'pptx', 'jpg'])])
    predmet = models.CharField(choices=PREDMETI, max_length=40)
    godina = models.CharField(choices=GODINE, max_length=40)
    autor = models.CharField(max_length=40)
    vreme_posta = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.predmet} : {self.autor} - {self.naslov}'

    class Meta:
        ordering = ['predmet', 'autor']
        verbose_name_plural = "Započni lekciju(ili dodaj sliku)"


class Video(models.Model):
    PREDMETI = (("Matematika", "Matematika"),
                ("Fizika", "Fizika"),
                ("Srpski jezik i književnost", "Srpski jezik i književnost"),
                ("Srpski kao nematernji jezik", "Srpski kao nematernji"),
                ("Bosanski jezik i književnost", "Bosanski jezik i književnost"),
                ("Engleski jezik", "Engleski jezik"),
                ("Nemački jezik", "Nemački jezik"),
                ("Francuski jezik", "Francuski jezik"),
                ("Latinski jezik", "Latinski jezik"),
                ("Istorija", "Istorija"),
                ("Geografija", "Geografija"),
                ("Biologija", "Biologija"),
                ("Hemija", "Hemija"),
                ("Računarstvo i informatika", "Računarstvo i informatika"),
                ("Muzička kultura", "Muzička kultura"),
                ("Likovna kultura", "Likovna kultura"),
                ("Fizičko vaspitanje", "Fizičko vaspitanje"),
                ("Građansko vaspitanje", "Građansko vaspitanje"),
                ("Islamska veronauka", "Islamska veronauka"),
                ("Pravoslavna veronauka", "Pravoslavna veronauka"),
                ("Jezik medija i kultura", "Jezik medija i kultura"),
                ("Primenjene nauke", "Primenjene nauke"),
                ("Umetnost i dizajn", "Umetnost i dizajn"),
                ("Zdravlje i sport", "Zdravlje i sport"),
                ("Psihologija", "Psihologija"),
                ("Filozofija", "Filozofija"),
                ("Sociologija", "Sociologija"),
                ("Ustav i prava građana", "Ustav i prava građana"),
                )

    GODINE = (("Prva godina", "Prva godina"),
              ("Druga godina", "Druga godina"),
              ("Treća godina", "Treća godina"),
              ("Četvrta godina", "Četvrta godina"), )
    naslov = models.CharField(max_length=300)
    nalepi_Youtube_link = models.CharField(max_length=100)
    predmet = models.CharField(choices=PREDMETI, max_length=40)
    godina = models.CharField(choices=GODINE, max_length=40)
    autor = models.CharField(max_length=40)
    vreme_posta = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.nalepi_Youtube_link = embed_video(str(self.nalepi_Youtube_link))
        return super(Video, self).save(*args, **kwargs)

    def clean(self):
        embed_video(str(self.nalepi_Youtube_link))

    def __str__(self):
        return f'{self.autor} - {self.naslov}'

    class Meta:
        ordering = ['autor']
        verbose_name_plural = "Dodaj video(ako želiš)"
