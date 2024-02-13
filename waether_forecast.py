import requests
from bs4 import BeautifulSoup as bs
import sys

class ObHavoMalumotiTopilmadi(Exception):
    if sys.version_info >= (3, 10):
        xatolik: str

class ObHavoMalumotu:
    def __init__(self, hudud):
        self.hudud: str = hudud

    def olish(self):
        try:
            res = requests.get(f"https://obhavo.uz/{self.hudud}")
            soup = bs(res.content, 'html.parser')
            response = soup.select(".current-forecast")[0].text.replace("\n", " ")
            return response
        except:
            if self.hudud == "yordam":
                return "\tagar toshkent ob-havosini chiqarmoqchi bo'lsangiz shu koddan foydalaning Ob_Havo('tashkent').malumot()\n\tagar andijon ob-havosini chiqarmoqchi bo'lsangiz shu koddan foydalaning Ob_Havo('andijan').malumot()\n\tagar buxoro ob-havosini chiqarmoqchi bo'lsangiz shu koddan foydalaning Ob_Havo('bukhara').malumot()\n\tagar guliston hududini ob-havosini chiqarmoqchi bo'lsangiz shu koddan foydalaning Ob_Havo('gulistan').malumot()\n\tagar jizzax ob-havosini chiqarmoqchi bo'lsangiz shu koddan foydalaning Ob_Havo('jizzakh').malumot()\n\tagar zarafshon ob-havosini chiqarmoqchi bo'lsangiz shu koddan foydalaning Ob_Havo('zarafshan').malumot()\n\tagar qarshi ob-havosini chiqarmoqchi bo'lsangiz shu koddan foydalaning Ob_Havo('karshi').malumot()\n\tagar navoiy ob-havosini chiqarmoqchi bo'lsangiz shu koddan foydalaning Ob_Havo('navoi').malumot()\n\tagar namangan ob-havosini chiqarmoqchi bo'lsangiz shu koddan foydalaning Ob_Havo('namangan').malumot()\n\tagar nukus ob-havosini chiqarmoqchi bo'lsangiz shu koddan foydalaning Ob_Havo('nukus').malumot()\n\tagar samarqand ob-havosini chiqarmoqchi bo'lsangiz shu koddan foydalaning Ob_Havo('samarkand').malumot()\n\tagar termiz ob-havosini chiqarmoqchi bo'lsangiz shu koddan foydalaning Ob_Havo('termez').malumot()\n\tagar urganch ob-havosini chiqarmoqchi bo'lsangiz shu koddam foydalaning Ob_Havo('urgench').malumot()\n\tagar farg'ona ob-havosini chiqarmoqchi bo'lsangiz shu koddan foydalaning Ob_Havo('ferghana').malumot()\n\tagar xiva ob-havosini chiqarmoqchi bo'lsangiz shu koddan foydalaning Ob_Havo('khiva').malumot()\n\tagar qarshi ob-havosini chiqarmoqchi bo'lsangiz shu koddan foydalaning Ob_Havo('karshi').malumot()"
            else:
                raise ObHavoMalumotiTopilmadi("bunday hudud topilmadi, to'g'ri yozganingizni tekshiring yoki Ob_Havo('yordam').malumot() funksiyasidan foydalaning")
            

print(ObHavoMalumotu("dwaf").olish())