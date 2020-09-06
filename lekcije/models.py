from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from lekcije.video_id import embed_video
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


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
                ("Obrazovanje za ordživi razvoj", "Obrazovanje za ordživi razvoj"),
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
                ("Obrazovanje za ordživi razvoj", "Obrazovanje za ordživi razvoj"),
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


class Ucenik(models.Model):

    STRANI_PREDMETI = (
        ("Engleski jezik", "Engleski jezik"),
        ("Nemački jezik", "Nemački jezik"),
        ("Francuski jezik", "Francuski jezik"),
    )
    JEZIK = (
        ("Srpski jezik ", "Srpski jezik "),
        ("Bosanski jezik ", "Bosanski jezik "),)
    SMER = (
        ("Prirodno matematički smer",  "Prirodno matematički smer"),
        ("Društveno jezički smer", "Društveno jezički smer"),
        ("Opšti smer",  "Opšti smer"),
        ("IT-smer",
         "IT-smer"),
        ("Odeljenje za  učenike nadarene za sport",
         "Odeljenje za  učenike nadarene za sport"),
    )
    IZBORNI_PROGRAMI = (
        ("Jezik medija i kultura", "Jezik medija i kultura"),
        ("Primenjene nauke", "Primenjene nauke"),
        ("Umetnost i dizajn", "Umetnost i dizajn"),
        ("Zdravlje i sport", "Zdravlje i sport"),
    )
    IZBORNI_PREDMETI = (
        ("Islamska veronauka", "Islamska veronauka"),
        ("Pravoslavna veronauka", "Pravoslavna veronauka"),
        ("Građansko vaspitanje", "Građansko vaspitanje"),)
    ODELJENJE = (
        ("I-1", "I-1"),
        ("I-2", "I-2"),
        ("I-3", "I-3"),
        ("I-4", "I-4"),
        ("I-5", "I-5"),
        ("I-6", "I-6"),
        ("I-7", "I-7"),
        ("I-8", "I-8"),
        ("I-9", "I-9"),
        ("I-10", "I-10"),
        ("I-11", "I-11"),
        ("I-12", "I-12"),
    )
    ime = models.CharField(max_length=300)
    prezime = models.CharField(max_length=300)
    maticni_broj = models.BigIntegerField()
    smer = models.CharField(choices=SMER, max_length=40)
    jezik_na_kojem_se_odvija_nastava = models.CharField(choices=JEZIK,
                                                        max_length=40
                                                        )
    prvi_strani_jezik = models.CharField(choices=STRANI_PREDMETI,
                                         max_length=40
                                         )
    drugi_strani_jezik = models.CharField(choices=STRANI_PREDMETI,
                                          max_length=40
                                          )
    izborni_predmet = models.CharField(choices=IZBORNI_PREDMETI,
                                       max_length=40
                                       )
    prvi_izborni_program = models.CharField(choices=IZBORNI_PROGRAMI,
                                            max_length=300, blank=True, null=True)
    drugi_izborni_program = models.CharField(choices=IZBORNI_PROGRAMI,
                                             max_length=300, blank=True, null=True)

    odeljenje = models.CharField(choices=ODELJENJE,
                                 max_length=300, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Prijava ucenika za prvi razred"

    def __str__(self):
        return f'{self.ime}--{self.prezime}:{self.maticni_broj}-{self.jezik_na_kojem_se_odvija_nastava}-{self.prvi_strani_jezik}-{self.drugi_strani_jezik}-{self.prvi_izborni_program}-{self.drugi_izborni_program}'

    def clean(self):
        if self.prvi_strani_jezik == self.drugi_strani_jezik:
            raise ValidationError(
                _('Prvi i drugi strani jezik moraju biti različiti'))
        if self.prvi_izborni_program or self.drugi_izborni_program:
            if self.prvi_izborni_program == self.drugi_izborni_program:
                raise ValidationError(
                    _('Prvi i drugi izborni programi moraju biti različiti'))


class IzborNastave(models.Model):
    ODELJENJE = (
        ("I-1", "I-1"),
        ("I-2", "I-2"),
        ("I-3", "I-3"),
        ("I-4", "I-4"),
        ("I-5", "I-5"),
        ("I-6", "I-6"),
        ("I-7", "I-7"),
        ("I-8", "I-8"),
        ("I-9", "I-9"),
        ("I-10", "I-10"),
        ("I-11", "I-11"),
        ("I-12", "I-12"),
        ("II-1", "II-1"),
        ("II-2", "II-2"),
        ("II-3", "II-3"),
        ("II-4", "II-4"),
        ("II-5", "II-5"),
        ("II-6", "II-6"),
        ("II-7", "II-7"),
        ("II-8", "II-8"),
        ("II-9", "II-9"),
        ("II-10", "II-10"),
        ("II-11", "II-11"),
        ("III-1", "III-1"),
        ("III-2", "III-2"),
        ("III-3", "III-3"),
        ("III-4", "III-4"),
        ("III-5", "III-5"),
        ("III-6", "III-6"),
        ("III-7", "III-7"),
        ("III-8", "III-8"),
        ("III-9", "III-9"),
        ("III-10", "III-10"),
        ("III-11", "III-11"),
        ("IV-1", "IV-1"),
        ("IV-2", "IV-2"),
        ("IV-3", "IV-3"),
        ("IV-4", "IV-4"),
        ("IV-5", "IV-5"),
        ("IV-6", "IV-6"),
        ("IV-7", "IV-7"),
        ("IV-8", "IV-8"),
        ("IV-9", "IV-9"),
        ("IV-10", "IV-10"),
    )

    ime_prezime_ucenika = models.CharField(max_length=300)
    odeljenje = models.CharField(choices=ODELJENJE,
                                 max_length=30)
    izbor = models.CharField(max_length=30)
    ime_prezime_roditelja = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = 'Izbor nastave učenika'

    def __str__(self):
        return f'{self.izbor}-{self.ime_prezime_ucenika}'

    def clean(self):
        if not self.izbor:
            raise ValidationError(
                _('Molim Vas odaberite "Da" ili "Ne" '))
