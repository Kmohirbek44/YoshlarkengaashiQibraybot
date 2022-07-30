from aiogram import types
from items.calc_distance import choose_shortest
from items.callback import bobcallback
from keybord import locations_buttons,default
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, CallbackQuery, fields

from keybord.Boblar import inline_kb1
from keybord.locations_buttons import keyboardstart
from loader import dp, bot







@dp.message_handler(text="Qonun_bo'yicha_ma'lumotlar")
async def Qonun(message:Message):
    print('111111111111111111111111111111111')
    await message.answer(text="Qoraqalpog‘iston Respublikasi, viloyatlar va Toshkent shahri, shuningdek, tuman (shahar)lardagi “Yoshlar daftari” jamg‘armalari to‘g‘risida"
                         ,reply_markup=inline_kb1)



@dp.callback_query_handler(bobcallback.filter(number="Umumiy qoidalar"))

async def birinchibob(call:CallbackQuery):
    print('11111111111111111')
    await call.answer()
    await call.message.answer(' 1-bob. Umumiy qoidalar\n'
                              '1. Ushbu Nizom Qoraqalpog‘iston Respublikasi, viloyatlar va Toshkent shahridagi “Yoshlar daftari” jamg‘armalari (keyingi o‘rinlarda — hududiy “Yoshlar daftari” jamg‘armasi), shuningdek, tuman (shahar)lardagi “Yoshlar daftari” jamg‘armalarini (keyingi o‘rinlarda — tuman (shahar) “Yoshlar daftari” jamg‘armasi) tashkil etish, ularning mablag‘larini shakllantirish va ushbu mablag‘lardan '
                              'foydalanish tartibini belgilaydi.\n'
                              '2. Hududiy “Yoshlar daftari” jamg‘armasi mablag‘lari tegishlicha Qoraqalpog‘iston Respublikasi Jo‘qorg‘i Kengesi, xalq deputatlari viloyatlar va Toshkent shahar Kengashlari qaroriga, shuningdek, tuman (shahar) “Yoshlar daftari” jamg‘armasi xalq deputatlari tuman (shahar) Kengashlari qaroriga muvofiq belgilangan tartibda shakllantiriladi.\n'
                              '3. Hududiy va tuman (shahar) “Yoshlar daftari” jamg‘armasi yuridik shaxs hisoblanmaydi.\n'
                              '4.Hududiy “Yoshlar daftari” jamg‘armasining mablag‘lari tegishlicha Qoraqalpog‘iston Respublikasi, viloyatlar va Toshkent shahar g‘aznachilik boshqarmalarida, shuningdek, tuman (shahar) “Yoshlar daftari” jamg‘armasining mablag‘lari tuman (shahar) g‘aznachilik bo‘limlarida alohida ochilgan shaxsiy g‘azna hisobvaraqlarida yig‘iladi.',reply_markup=inline_kb1)
@dp.callback_query_handler(bobcallback.filter(number="yoshlar"))
async def yoshlar(call:CallbackQuery):

    await call.answer(cache_time=20)
    text="""O‘zbekiston Respublikasi Prezidentining “Mahallalarda yoshlar bilan ishlash tizimini tubdan takomillashtirish chora-tadbirlari to‘g‘risida” 2022-yil 19-yanvardagi PQ-92-son va “Zakovat” intellektual o‘yinini aholi o‘rtasida ommaviy-ma’rifiy harakatga aylantirish va boshqa intellektual o‘yinlarni rivojlantirishga oid chora-tadbirlar to‘g‘risida” 2022-yil 20-yanvardagi PQ-96-son qarorlariga muvofiq ijtimoiy himoyaga muhtoj, ishsiz va ijtimoiy faol bo‘lmagan yoshlar bilan “Yoshlar daftari”ni yuritish orqali ishlash tizimini yanada takomillashtirish, ularni har tomonlama qo‘llab-quvvatlash, shuningdek, oliy ta’lim tashkilotlari talabalari o‘rtasida intellektual sog‘lom raqobatni shakllantirish, talaba va yoshlarning bilim va salohiyatini yanada oshirish hamda ularni rag‘batlantirish maqsadida Vazirlar Mahkamasi qaror qiladi:
        1. “Yoshlar daftari”ga kiritilgan yoshlarning ijtimoiy-iqtisodiy muammolarini hal etish maqsadida tuman va shaharlarda “Yoshlar daftari”ga kiritilgan yoshlarni qo‘llab-quvvatlash jamg‘armalari (keyingi o‘rinlarda — tuman (shahar) “Yoshlar daftari” jamg‘armasi) tashkil etilganligi ma’lumot uchun qabul qilinsin.
        2. Qoraqalpog‘iston Respublikasi Vazirlar Kengashi, viloyatlar va Toshkent shahar hokimliklari hamda Yoshlar ishlari agentligining Qoraqalpog‘iston Respublikasi, viloyatlar va Toshkent shahrida “Yoshlar daftari”ga kiritilgan yoshlarni qo‘llab-quvvatlash jamg‘armalarini (keyingi o‘rinlarda — hududiy “Yoshlar daftari” jamg‘armasi) tashkil etish hamda ushbu jamg‘armalar mablag‘larini quyidagi manbalar hisobidan shakllantirish to‘g‘risidagi taklifi ma’qullansin:
        Qoraqalpog‘iston Respublikasi respublika budjeti, viloyatlar va Toshkent shahar mahalliy budjetlarining prognozi orttirib bajarilgan qismining kamida 15 foizi miqdorida har chorakda ajratiladigan mablag‘lar;
        jismoniy va yuridik shaxslarning homiylik mablag‘lari hamda qonunchilik hujjatlarida taqiqlanmagan boshqa manbalar.
        3. Qoraqalpog‘iston Respublikasi Vazirlar Kengashi Raisi, viloyatlar va Toshkent shahar, shuningdek, tuman (shahar) hokimlari ushbu qarorda nazarda tutilgan manbalar hisobidan hududiy va tuman (shahar) “Yoshlar daftari” jamg‘armalari mablag‘larini o‘z vaqtida va to‘liq shakllantirishga shaxsan mas’ul hisoblanishi belgilab qo‘yilsin.
        4. Quyidagilarni nazarda tutuvchi:
        Qoraqalpog‘iston Respublikasi, viloyatlar va Toshkent shahri, shuningdek, tuman (shahar)lardagi “Yoshlar daftari” jamg‘armalari to‘g‘risidagi nizom 1-ilovaga muvofiq:
        yuridik shaxs bo‘lmagan hududiy va tuman (shahar) “Yoshlar daftari” jamg‘armasini tashkil etish tartibi;
        hududiy va tuman (shahar) “Yoshlar daftari” jamg‘armasi mablag‘larini shakllantirish tartibi;
        hududiy va tuman (shahar) “Yoshlar daftari” jamg‘armasi mablag‘larini boshqarish va ulardan foydalanish;
        Yoshlar ishlari agentligining hududiy boshqarmalarini hududiy “Yoshlar daftari” jamg‘armasining, Yoshlar ishlari agentligining tuman (shahar) bo‘limlarini tuman (shahar) “Yoshlar daftari” jamg‘armasining ishchi organi etib belgilash;
        “Yoshlar daftari”ni yuritish orqali yoshlar muammolarini tizimli ravishda hal etish va ularni ijtimoiy qo‘llab-quvvatlash tartibi to‘g‘risidagi nizom 2-ilovaga muvofiq tasdiqlansin:
        “Yoshlar daftari”ga kiritilgan va moddiy ahvoli og‘ir yoshlarga bir martalik moddiy yordam ko‘rsatish;
        “Yoshlar daftari”ga kiritilgan yoshlarga ularning davlat va nodavlat ta’lim tashkilotlarida avtomototransport vositalari haydovchilarini tayyorlash o‘quv kursi xarajatlarini qoplash uchun subsidiya ajratish;
        “Yoshlar daftari”ga kiritilgan yoshlarning muammolarini tizimli ravishda hal etish va ularni ijtimoiy qo‘llab-quvvatlash, ijtimoiy-iqtisodiy, psixologik himoyaga muhtoj hamda iqtidorli va faol yoshlarga ko‘maklashish;
        “Yoshlar daftari”ga kiritilgan yoshlarni kasb-hunarga o‘rgatish orqali ularning bandligini ta’minlash, tadbirkorlik loyihalari va tashabbuslarini qo‘llab-quvvatlash;
        yoshlarning iste’dodlarini qo‘llab-quvvatlash, besh muhim tashabbus doirasidagi tadbirlarni moliyalashtirish hamda amaliy yordamlar to‘liq ko‘rsatish orqali yoshlarni “Yoshlar daftari”dan chiqarish tartibi.
        5. Belgilansinki:
        hududiy va tuman (shahar) “Yoshlar daftari” jamg‘armalarining daromadlar va xarajatlar parametrlarini, ularning ijrosi to‘g‘risidagi hisobotlarni, ish rejalarini tasdiqlash hamda mablag‘larini shakllantirish va ulardan foydalanish bilan bog‘liq boshqa vakolatlar tegishlicha Qoraqalpog‘iston Respublikasi, viloyatlar va Toshkent shahar, shuningdek, tuman (shahar)lardagi “Yoshlar daftari” jamg‘armalari Vasiylik kengashlari tomonidan amalga oshiriladi;
        Qoraqalpog‘iston Respublikasi Vazirlar Kengashi Raisi, viloyatlar va Toshkent shahar hokimlari — tegishli hududiy “Yoshlar daftari” jamg‘armasi, tuman (shahar) hokimlari — tegishli tuman (shahar) “Yoshlar daftari” jamg‘armasi Vasiylik kengashi raisi hisoblanadi;
        hududiy va tuman (shahar) “Yoshlar daftari” jamg‘armalari Vasiylik kengashlari a’zolarining faoliyati jamoatchilik asosida tashkil etiladi."""
    for x in range(0, len(text), 4096):
         await call.message.answer(text[x:x + 4096])


@dp.callback_query_handler(bobcallback.filter(number="laridan"))
async def Shakllantirish(call:CallbackQuery):

    await call.answer(cache_time=20)
    text="""2-bob. Hududiy va tuman (shahar) “Yoshlar daftari” jamg‘armalari mablag‘larini shakllantirish manbalari
4. Hududiy “Yoshlar daftari” jamg‘armasi quyidagi manbalar hisobidan shakllantiriladi:
Qoraqalpog‘iston Respublikasi respublika budjeti, viloyatlar va Toshkent shahar mahalliy budjetlari prognozining orttirib bajarilgan qismining kamida 15 foizi miqdorida har chorakda ajratiladigan mablag‘lar;
xorijiy (xalqaro) moliya institutlari va boshqa xorijiy donorlarning texnik ko‘mak mablag‘lari va grantlari;
jismoniy va yuridik shaxslarning homiylik mablag‘lari hamda qonunchilik hujjatlari bilan taqiqlanmagan boshqa manbalar.
Bunda Qoraqalpog‘iston Respublikasi Vazirlar Kengashi, viloyatlar va Toshkent shahar hokimliklari tegishlicha Qoraqalpog‘iston Respublikasi respublika budjeti, viloyatlar va Toshkent shahar mahalliy budjetlari prognozining orttirib bajarilgan qismining kamida 15 foizi miqdoridagi mablag‘lar har chorakda, birinchi navbatda, tegishli hududning qo‘shimcha manbalari nisbatan kam miqdorda shakllangan tuman (shahar) “Yoshlar daftari” jamg‘armalariga o‘tkazib borish yuzasidan takliflarni Qoraqalpog‘iston Respublikasi Jo‘qorg‘i Kengesiga, viloyatlar va Toshkent shahar xalq deputatlari Kengashlariga kiritib borsin.
5. Tuman (shahar) “Yoshlar daftari” jamg‘armasi quyidagi manbalar hisobidan shakllantiriladi:
hududiy “Yoshlar daftari” jamg‘armasidan ajratmalar;
tumanlar (shaharlar) mahalliy budjetlari prognozining orttirib bajarilgan qismining kamida 15 foizi miqdorida har chorakda ajratiladigan mablag‘lar;
O‘zbekiston Respublikasi Prezidentining “Sud hujjatlari va boshqa organlar hujjatlarini ijro etish tizimini yanada takomillashtirish chora-tadbirlari to‘g‘risida” 2020-yil 24-noyabrdagi PF-6118-son Farmonining 12-bandida belgilangan tushumlarning mazkur Farmonga 3-ilovaga muvofiq miqdordagi mablag‘lar;
xorijiy (xalqaro) moliya institutlari va boshqa xorijiy donorlarning texnik ko‘mak mablag‘lari va grantlari;
jismoniy va yuridik shaxslarning homiylik mablag‘lari hamda qonunchilik hujjatlari bilan taqiqlanmagan boshqa manbalar.
6. Qoraqalpog‘iston Respublikasi Vazirlar Kengashi Raisi, viloyatlar va Toshkent shahar, shuningdek, tuman (shahar) hokimlari ushbu Nizomning 4-bandida nazarda tutilgan manbalar hisobidan hududiy va tuman (shahar) “Yoshlar daftari” jamg‘armalari mablag‘larini o‘z vaqtida va to‘liq shakllantirishga shaxsan mas’ul hisoblanadi."""
    for x in range(0, len(text), 4096):
         await call.message.answer(text[x:x + 4096])



@dp.callback_query_handler(bobcallback.filter(number="mablag"))
async def mablag(call:CallbackQuery):

    await call.answer(cache_time=20)
    text="""3-bob. Hududiy va tuman (shahar) “Yoshlar daftari” jamg‘armalari mablag‘laridan foydalanish
7. Hududiy “Yoshlar daftari” jamg‘armasi mablag‘lari:
tegishli hududning qo‘shimcha manbalari nisbatan kam miqdorda shakllangan tuman (shahar) “Yoshlar daftari” jamg‘armalariga;
Yoshlar ishlari agentligi direktori tomonidan tasdiqlangan kalendar rejada belgilangan mahalla, sektor, tuman (shahar) va hudud darajasidagi loyihalar, yoshlar festivallari, forumlar, tanlovlar va boshqa madaniy-ma’rifiy tadbirlarni moliyalashtirishga;
mahallalarda yoshlarning bo‘sh vaqtini mazmunli tashkil etish uchun qo‘shimcha sharoitlar yaratishga mo‘ljallangan yengil turdagi kichik kutubxonalar va sport obyektlarini barpo etish hamda ularni zamonaviy jihozlashga;
mahallalardagi yoshlar yetakchilari uchun ajratilgan xizmat xonalarini moddiy-texnik jihozlar (mebel, planshet, kompyuter to‘plami, aloqa, internet va boshqalar) bilan ta’minlashga;
qonunchilik hujjatlari bilan belgilangan boshqa xarajatlarni qoplashga yo‘naltiriladi.
8. Tuman (shahar) “Yoshlar daftari” jamg‘armasi mablag‘lari:
“Yoshlar daftari”ga kiritilgan va moddiy ahvoli og‘ir yoshlarga bazaviy hisoblash miqdorining (keyingi o‘rinlarda — BHM) 4 baravarigacha miqdorda bir martalik moddiy yordam ko‘rsatishga;
“Yoshlar daftari”ga kiritilgan yoshlarni tadbirkorlik va kasb-hunarga o‘qitish uchun sarflangan xarajatlarning 75 foizigacha qismini, biroq bir oygacha, bir oydan ikki oygacha, ikki oydan ortiq muddatli o‘quv kurslari uchun tegishlicha BHMning 4, 8, 12 baravaridan ko‘p bo‘lmagan miqdordagi qismini qoplashga;
“Yoshlar daftari”ga kiritilgan yoshlarga ularning davlat va nodavlat ta’lim tashkilotlarida avtomototransport vositalari haydovchilarini tayyorlash o‘quv kursi xarajatlarini qoplash uchun BHMning 4 baravarigacha miqdorda subsidiya ajratishga;
“Yoshlar daftari”ga kiritilgan, dehqonchilik va tomorqa xo‘jaligini yuritish bilan shug‘ullanayotgan yoshlarga urug‘lik va ko‘chatlar sotib olish uchun BHMning 8 baravarigacha miqdorda subsidiya ajratishga;
“Yoshlar daftari”ga kiritilgan yoshlarga tadbirkorlik faoliyati hamda o‘zini o‘zi band qilish maqsadida noturar joyning 12 oygacha ijara xarajatlarini ko‘pi bilan bir yilda 30 foiz, biroq BHMning 25 baravarigacha miqdorda qoplashga;
“Yoshlar daftari”ga kiritilgan yoshlarga tadbirkorlik faoliyatini boshlash va o‘zini o‘zi band qilish uchun zarur bo‘lgan asbob-uskunalar va mehnat qurollarini xarid qilishga BHMning 40 baravarigacha miqdorda subsidiya ajratishga;
mamlakatimizdagi professional va oliy ta’lim muassasalarida ta’lim olayotgan, “Temir daftar”ga kiritilgan oilalar farzandlarining, shuningdek, “Yoshlar daftariga” kiritilgan yoshlarning to‘lov-kontrakt summasining 50 foizigacha, ammo BHMning 50 baravaridan oshmagan miqdorda to‘lab berishga;
yoshlarga zamonaviy kasblarni egallashi, axborot texnologiyalarini o‘rganishi va ularni xorijiy tillarga o‘qitish bo‘yicha olti oygacha muddatli o‘quv kurslar uchun har oyda BHMning 4 baravarigacha miqdorda subsidiya ajratishga;
ijtimoiy himoyaga muhtoj iqtidorli yoshlarning ilm-fan, sport, san’at va madaniyat yo‘nalishlaridagi olti oygacha muddatli o‘quv kurslari uchun har oyda BHMning 1 baravarigacha miqdorda subsidiya ajratishga;
“Temir daftar” va “Ayollar daftari”ga kiritilgan oilalarning farzandlari hamda “Yoshlar daftari”ga kiritilgan ijtimoiy himoyaga muhtoj yoshlarning fuqarolik pasporti (biometrik pasport) olish badalini qoplab berish;
ijtimoiy himoyaga muhtoj iqtidorli yoshlarning ilm-fan, sport, san’at va madaniyat yo‘nalishlaridagi olimpiada, tanlov va musobaqalarning mahalliy bosqichlarida qatnashish xarajatlari uchun BHMning 4 baravarigacha hamda xalqaro bosqichlarida qatnashish xarajatlari uchun BHMning 40 baravarigacha miqdorda subsidiya ajratishga;
“Temir daftar” va “Ayollar daftari”ga kiritilgan oilalarning farzandlari hamda “Yoshlar daftari”ga kiritilgan yosh oilalarning o‘quvchi farzandlari uchun bir kalendar yilida bir marotaba maktab formasi hamda o‘quv qurollari uchun xarajatlarini qoplash;
“Temir daftar” va “Ayollar daftari”ga kiritilgan oilalarning farzandlari hamda “Yoshlar daftari”ga kiritilgan ijtimoiy himoyaga muhtoj yoshlar hamda tengdoshlari orasida namuna ko‘rsatgan faol yoshlarning mamlakatimiz bo‘ylab turizm obyektlariga sayohatlari uchun mehmonxona va yo‘l xarajatlarini qoplab berish;
yoshlarga ta’lim, madaniyat va san’at, sport, axborot texnologiyalar sohasiga va fanlarni o‘qitishga ixtisoslashgan ta’lim tashkilotlarining uch oy muddatgacha noturar joy ijara xarajatlari uchun BHMning 50 baravarigacha miqdorda subsidiya ajratishga;
moddiy ahvoli og‘ir bo‘lgan 30 yoshdan oshmagan bemor fuqarolarga mamlakatda yoki xorijiy davlatlarda davolanish bilan bog‘liq xarajatlarni qoplash uchun BHMning 50 baravaridan oshmagan miqdorda subsidiya ajratishga;
psixologik maslahatga muhtoj yoshlarga ixtisoslashgan nodavlat notijorat tashkilotlari hamda nodavlat ta’lim tashkilotlari tomonidan pulli psixologik xizmat ko‘rsatilishi bilan bog‘liq xarajatlarni qoplashga;
ijtimoiy himoyaga muhtoj yoshlarning safarbarlik chaqiruvi rezervidagi xizmatni o‘tash badalini to‘liq miqdorda qoplash uchun subsidiya ajratishga;
yoshlarga yangi turmush qurayotganda, o‘z xonadonida qo‘shimcha uy-joy qurish uchun 33 million so‘mgacha garovsiz kredit ajratishga kafillik berishga;
ijtimoiy himoyaga muhtoj yosh oilalarga har oyda BHMning 3 baravaridan oshmagan miqdorda 12 oygacha turar joy ijarasi uchun subsidiya ajratishga;
Yoshlar ishlari agentligi direktori tomonidan tasdiqlangan kalendar rejada belgilangan mahalla, sektor va tuman (shahar) darajasidagi loyihalar, yoshlar festivallari, forumlar, tanlovlar va boshqa madaniy-ma’rifiy tadbirlarni moliyalashtirishga;
mahalladagi yoshlar yetakchisining tuman (shahar) Vasiylik kengashiga kiritgan iltimosnomasiga binoan Kengash raisi Yoshlar ishlari agentligining hududiy boshqarmasiga “Yoshlar daftari”ga kiritilgan yoshlarning muammolarini “Yoshlar daftari” jamg‘armasi mablag‘lari hisobidan yetarli darajada hal qilinganligi to‘g‘risida axborot beradi. Mazkur axborot asosida Yoshlar ishlari agentligining hududiy boshqarmasi tavsiyasi bilan tuman (shahar) jamg‘armasidagi mavjud mablag‘lar hisobidan mahallalarda yoshlarning bo‘sh vaqtini mazmunli tashkil etish uchun qo‘shimcha sharoitlar yaratishga mo‘ljallangan yengil turdagi kichik kutubxonalar va sport obyektlarini barpo etish hamda ularni zamonaviy jihozlashga mablag‘ yo‘naltirish;
qonunchilik hujjatlari bilan belgilangan boshqa xarajatlarni qoplashga yo‘naltiriladi.
9. Hududiy va tuman (shahar) “Yoshlar daftari” jamg‘armalarining mablag‘lari ushbu Nizomning 7 va 8-bandlarida nazarda tutilmagan maqsadlarga yo‘naltirilishiga, shuningdek, “Yoshlar daftari”ga kiritilgan yoshlarga aynan bir turdagi subsidiya yoki ijtimoiy yordam (bir martalik moddiy yordam bundan mustasno) boshqa manbalar va jamg‘armalar tomonidan ko‘rsatilganda taqdim etilishiga yo‘l qo‘yilmaydi.
10. O‘zbekiston Respublikasi Yoshlar ishlari agentligining Yoshlarga oid davlat siyosatini qo‘llab-quvvatlash jamg‘armasi hisobidan, zarur hollarda, ushbu Nizomning 7 va 8-bandlarida nazarda tutilgan maqsadlar uchun mablag‘lar ajratilishi mumkin.
11. Hududiy va tuman (shahar) “Yoshlar daftari” jamg‘armalari mablag‘larini shakllantirish, boshqarish va ulardan foydalanish maqsadida ushbu Nizomga 1 va 2-ilovalarga muvofiq tarkibda Vasiylik kengashi (keyingi o‘rinlarda — Vasiylik kengashi) tuziladi.
Vasiylik kengashi tarkibi Qoraqalpog‘iston Respublikasi Jo‘qorg‘i Kengesi, xalq deputatlari viloyatlar va Toshkent shahar Kengashlari, shuningdek, xalq deputatlari tuman (shahar) Kengashlari qaroriga muvofiq tasdiqlanadi.
Vasiylik kengashi raisi va a’zolari “Yoshlar daftari” jamg‘armasini boshqarish bo‘yicha faoliyatini jamoatchilik asosida amalga oshiradi.
Vasiylik kengashi raisi “Yoshlar daftari” jamg‘armasi mablag‘larini boshqaruvchi hisoblanadi.
12. Yoshlar ishlari agentligining hududiy boshqarmalari hududiy “Yoshlar daftari” jamg‘armasining, Yoshlar ishlari agentligining tuman (shahar) bo‘limlari tuman (shahar) “Yoshlar daftari” jamg‘armasining ishchi organi hisoblanadi.
13. “Yoshlar daftari” jamg‘armalari mablag‘lari sarflash Vasiylik kengashi qarori asosida sarflanadi.
Vasiylik kengashi yig‘ilishlari har oyda kamida ikki marta — oyning 15-sanasigacha va oxirgi sanasigacha o‘tkaziladi.
14. Vasiylik kengashi raisi Vasiylik kengashi yig‘ilishlariga raislik qiladi.
15. Vasiylik kengashlari qarorlari Vasiylik kengashi yig‘ilishi bayoni bilan rasmiylashtiriladi.
16. Vasiylik kengashi:
“Yoshlar daftari” jamg‘armasiga umumiy rahbarlik qiladi va uning faoliyatini nazorat qiladi;
“Yoshlar daftari” jamg‘armasining daromad va xarajatlari yillik parametrlarini, ularning ijrosi to‘g‘risidagi yillik hisobotlarni, shuningdek, “Yoshlar daftari” jamg‘armasiga yuklangan vazifalarning bajarilishi to‘g‘risidagi hisobotlarni tasdiqlaydi;
“Yoshlar daftari” jamg‘armasining yillik ish rejasi va dasturlarini tasdiqlaydi;
“Yoshlar daftari” jamg‘armasi mablag‘laridan foydalanishda shaffoflikni ta’minlaydi;
“Yoshlar daftari” jamg‘armasi mablag‘lari hisobidan alohida tadbirlarni moliyalashtirish tartibini belgilaydi;
“Yoshlar daftari” jamg‘armasiga homiylik xayriyalari, shuningdek, xalqaro tashkilotlarning texnik ko‘mak mablag‘lari va grantlarini jalb qilishga ko‘maklashadi;
“Yoshlar daftari” jamg‘armasiga yuklatilgan vazifalarni Vasiylik kengashi a’zolari o‘rtasida taqsimlaydi;
“Yoshlar daftari” jamg‘armasi faoliyatiga taalluqli masalalarni ko‘rib chiqadi va ular bo‘yicha qarorlar qabul qiladi;
“Yoshlar daftari” jamg‘armasi mablag‘larini shakllantirish va ulardan foydalanish bilan bog‘liq boshqa vakolatlarni amalga oshiradi;
“Yoshlar daftari” jamg‘armasi faoliyatiga aloqador boshqa masalalarni ko‘rib chiqadi va ular bo‘yicha qarorlar qabul qiladi.
17. “Yoshlar daftari” jamg‘armasining ishchi organi:
“Yoshlar daftari” jamg‘armasining yillik ish rejasi va dasturlarini ishlab chiqadi;
Vasiylik kengashi yig‘ilishi kun tartibiga kiritiladigan masalalarni tayyorlaydi, yig‘ilish bayonnomasini yuritadi va rasmiylashtiradi;
Vasiylik kengashi a’zolariga Vasiylik kengashi yig‘ilishining vaqti va o‘tkaziladigan joyi to‘g‘risida xabar beradi;
davlat tomonidan beriladigan ijtimoiy ko‘mak va ko‘rsatiladigan moddiy yordam to‘g‘risidagi ma’lumotlarni “Yoshlar daftari”ga kiritilgan yoshlarning yakka tartibdagi anketasida qayd etib boradi;
“Yoshlar daftari”ga kiritilgan yoshlarning murojaatlari bilan ishlaydi va ko‘rib chiqish uchun Vasiylik kengashiga taqdim etadi;
Vasiylik kengashi tomonidan qabul qilingan qaror to‘g‘risida murojaat etuvchiga xabar yuboradi.
Vasiylik kengashi qarori bilan ishchi organga qo‘shimcha vazifalar ham yuklanishi mumkin."""
    for x in range(0, len(text), 4096):
         await call.message.answer(text[x:x + 4096])


@dp.callback_query_handler(bobcallback.filter(number="hisob"))
async def hisob(call:CallbackQuery):

    await call.answer(cache_time=20)
    text="""4-bob. Hududiy va tuman (shahar) “Yoshlar daftari” jamg‘armalari mablag‘laridan foydalanish bo‘yicha hisob va hisobot
18. Hududiy va tuman (shahar) “Yoshlar daftari” jamg‘armalari mablag‘laridan foydalanish bo‘yicha hisob va hisobotlar tegishlicha Qoraqalpog‘iston Respublikasi Vazirlar Kengashi, viloyatlar, Toshkent shahar, tuman (shahar) hokimliklari hisobot bo‘limlari tomonidan har oyning 5-sanasiga qadar xarajatlar to‘g‘risida, Qoraqalpog‘iston Respublikasi Moliya vazirligi, viloyatlar va Toshkent shahar moliya boshqarmalari hamda tuman (shahar) moliya bo‘limlari mahalliy budjetning orttirilgan qismi miqdori to‘g‘risida Yoshlar ishlari agentligiga ma’lumot berib boradi.
19. Qoraqalpog‘iston Respublikasi, viloyatlar, Toshkent shahar hamda tuman (shahar) moliya organlari tomonidan budjet ijrosi hisobotini shakllantirish davrida tegishlicha “Yoshlar daftari” jamg‘armasi hisoboti ham qabul qilinadi.
20. Vasiylik kengashi raisi har chorakda “Yoshlar daftari” jamg‘armasi daromadlari va xarajatlari ijrosi to‘g‘risida tegishliligi bo‘yicha Qoraqalpog‘iston Respublikasi Jo‘qorg‘i Kengesi, xalq deputatlari viloyatlar, Toshkent shahar, tuman (shahar) Kengashlariga hisobot beradi."""
    for x in range(0, len(text), 4096):
         await call.message.answer(text[x:x + 4096])


@dp.callback_query_handler(bobcallback.filter(number="qoidalar"))
async def qoidalar(call:CallbackQuery):

    await call.answer(cache_time=20)
    text="""5-bob. Yakunlovchi qoidalar
21. Hududiy va tuman (shahar) “Yoshlar daftari” jamg‘armalarining joriy yilda foydalanilmay qolgan mablag‘lari keyingi yilga o‘tadi hamda Qoraqalpog‘iston Respublikasi respublika budjeti, viloyatlar va Toshkent shahar, shuningdek, tuman (shahar) mahalliy budjetiga olib qo‘yilmaydi.
22. O‘zbekiston Respublikasi Moliya vazirligi huzurida Davlat moliyaviy nazorati inspeksiyasining hududiy boshqarmalari mazkur Nizom doirasida tuman (shahar)larda amalga oshiriladigan ishlar uchun ajratilgan mablag‘lar samarali va maqsadli ishlatilishi bo‘yicha nazorat o‘rnatadi.
23. Mazkur Nizom talablarining buzilishida aybdor shaxslar qonunchilik hujjatlarida belgilangan tartibda javob beradilar."""
    for x in range(0, len(text), 4096):
         await call.message.answer(text[x:x + 4096])

@dp.callback_query_handler(bobcallback.filter(number="namunaviy"))
async def qoidalar(call:CallbackQuery):

    await call.answer(cache_time=20)
    text="""Qoraqalpog‘iston Respublikasi, viloyatlar va Toshkent shahridagi “Yoshlar daftari” jamg‘armasi vasiylik kengashining NAMUNAVIY TARKIBI

Lavozimiga ko‘ra

—

Qoraqalpog‘iston Respublikasi Vazirlar Kengashi Raisi, viloyatlar va Toshkent shahar hokimlari, Vasiylik kengashi raisi

2.

Lavozimiga ko‘ra

—

Qoraqalpog‘iston Respublikasi Vazirlar Kengashi Raisi, viloyatlar va Toshkent shahar hokimining yoshlar siyosati, ijtimoiy rivojlantirish va ma’naviy-ma’rifiy ishlar bo‘yicha o‘rinbosarlari, Vasiylik kengashi raisi o‘rinbosari

3.

Lavozimiga ko‘ra

—

Qoraqalpog‘iston Respublikasi, viloyatlar va Toshkent shahar prokurorlari (kelishuv asosida)

4.

Lavozimiga ko‘ra

—

Qoraqalpog‘iston Respublikasi ichki ishlar vaziri, Toshkent shahar, Toshkent viloyati ichki ishlar bosh boshqarmalari va viloyatlar ichki ishlar boshqarmalari boshliqlari

5.

Lavozimiga ko‘ra

—

Qoraqalpog‘iston Respublikasi bandlik va mehnat munosabatlari vaziri, viloyatlar va Toshkent shahar bandlik bosh boshqarmalari boshliqlari

6.

Lavozimiga ko‘ra

—

Qoraqalpog‘iston Respublikasi sog‘liqni saqlash vaziri, Toshkent shahar sog‘liqni saqlash bosh boshqarmasi, viloyatlar sog‘liqni saqlash boshqarmalari boshliqlari

7.

Lavozimiga ko‘ra

—

Qoraqalpog‘iston Respublikasi sportni rivojlantirish vaziri, viloyatlar va Toshkent shahar sportni rivojlantirish bosh boshqarmalari boshliqlari

8.

Lavozimiga ko‘ra

—

Qoraqalpog‘iston Respublikasi madaniyat vazirligi, Toshkent shahar madaniyat bosh boshqarmasi, viloyatlar madaniyat boshqarmalari boshliqlari

9.

Lavozimiga ko‘ra

—

Qoraqalpog‘iston Respublikasi, viloyatlar va Toshkent shahar davlat soliq boshqarmalari boshliqlari

10.

Lavozimiga ko‘ra

—

Qoraqalpog‘iston Respublikasi moliya vaziri, viloyatlar va Toshkent shahar moliya boshqarmalari boshliqlari

11.

Lavozimiga ko‘ra

—

Mahallabay ishlash va tadbirkorlikni rivojlantirish agentligining Qoraqalpog‘iston Respublikasi, viloyatlar va Toshkent shahar boshqarmalari boshliqlari

12.

Lavozimiga ko‘ra

—

Yoshlar ishlari agentligining Qoraqalpog‘iston Respublikasi, viloyatlar va Toshkent shahar boshqarmasi boshliqlari, Vasiylik kengashi kotibi"""
    for x in range(0, len(text), 4096):
         await call.message.answer(text[x:x + 4096])


@dp.callback_query_handler(bobcallback.filter(number="vasiylik"))
async def qoidalar(call:CallbackQuery):

    await call.answer(cache_time=20)
    text="""
    Tuman (shahar)lardagi “Yoshlar daftari” jamg‘armasi vasiylik kengashining NAMUNAVIY TARKIBI\n

Lavozimiga ko‘ra

—

tuman (shahar) hokimlari, Vasiylik kengashi raisi

2.

Lavozimiga ko‘ra

—

tuman (shahar) hokimining yoshlar siyosati, ijtimoiy rivojlantirish va ma’naviy-ma’rifiy ishlar bo‘yicha o‘rinbosarlari, Vasiylik kengashi raisi o‘rinbosari

3.

Lavozimiga ko‘ra

—

tuman (shahar) hokimining moliya-iqtisodiyot va kambag‘allikni qisqartirish masalalari bo‘yicha birinchi o‘rinbosarlari

4.

Lavozimiga ko‘ra

—

tuman (shahar) prokurorlari (kelishuv asosida)

5.

Lavozimiga ko‘ra

—

tuman (shahar) ichki ishlar boshqarmalari (bo‘limlari) boshliqlari

6.

Lavozimiga ko‘ra

—

tuman (shahar) aholi bandligiga ko‘maklashish markazlari boshliqlari

7.

Lavozimiga ko‘ra

—

tuman (shahar) tibbiyot birlashmalari boshliqlari

8.

Lavozimiga ko‘ra

—

tuman (shahar) sportni rivojlantirish bo‘limlari boshliqlari

9.

Lavozimiga ko‘ra

—

tuman (shahar) madaniyat bo‘limlari boshliqlari

10.

Lavozimiga ko‘ra

—

tuman (shahar) davlat soliq inspeksiyalari boshliqlari

11.

Lavozimiga ko‘ra

—

tuman (shahar) moliya bo‘limi boshliqlari

12.

Lavozimiga ko‘ra

—

Mahallabay ishlash va tadbirkorlikni rivojlantirish agentligining tuman (shahar) markazlari boshliqlari

13.

Lavozimiga ko‘ra

—

Yoshlar ishlari agentligining tuman (shahar) bo‘limi boshliqlari, Vasiylik kengashi kotibi"""
    for x in range(0, len(text), 4096):
         await call.message.answer(text[x:x + 4096])


@dp.callback_query_handler(bobcallback.filter(number="1_2 bob"))
async def bir(call:CallbackQuery):

    await call.answer(cache_time=20)
    text="""1-bob. Umumiy qoidalar\n. Mazkur Nizom “Yoshlar daftari”ni yuritish orqali yoshlar muammolarini tizimli ravishda hal etish va ularni ijtimoiy qo‘llab-quvvatlash tartibini belgilaydi.
2. Ushbu Nizomda quyidagi asosiy tushunchalar qo‘llaniladi:
ariza beruvchi — “Yoshlar daftari”ga kirish yoki “Yoshlar daftari” jamg‘armasi mablag‘lari hisobidan qo‘llab-quvvatlash bo‘yicha mazkur Nizomga muvofiq murojaat qilgan o‘n to‘rt yoshga to‘lgan va o‘ttiz yoshdan oshmagan (o‘ttiz bir yoshga to‘lmagan) O‘zbekiston Respublikasi fuqarosi yoki ularning vakili (o‘n olti yoshga to‘lmagan shaxs nomidan murojaat qilgan uning qonuniy vakili) hamda fuqaroligi bo‘lmagan shaxs;
Vasiylik kengashi — “Yoshlar daftari” jamg‘armasi mablag‘larini shakllantirish, boshqarish va ulardan foydalanish maqsadida qonunchilik hujjatlarida belgilangan tartibda manfaatdor tashkilotlar rahbarlari va mas’ul xodimlaridan iborat tarkibda tuziladigan kollegial organ;
“Yoshlar daftari” — ijtimoiy, iqtisodiy, huquqiy, psixologik va boshqa turdagi qo‘llab-quvvatlashga, bilim va kasb o‘rganishga ehtiyoji va ishtiyoqi bo‘lgan yoshlarning muammolarini aniqlash, bartaraf etish va nazorat qilib borish tizimi;
“Yoshlar daftari” elektron platformasi (elektron platforma) — yoshlarga tegishli bo‘lgan ma’lumotlarni jamlash, tahlil qilish, qayta ishlash tizimini yaratish hamda tegishli vazirliklar va idoralar bilan raqamli ma’lumotlar almashuvini tashkil etish, yoshlarning murojaatlari bilan tizimli ishlash yuzasidan chora-tadbirlar samaradorligi monitoringini olib borish imkonini beruvchi maxsus elektron platforma;
“Yoshlar daftari” jamg‘armasi — “Yoshlar daftari”ga kiritilgan yoshlarni ijtimoiy qo‘llab-quvvatlash va ularning tashabbuslarini rag‘batlantirish maqsadida belgilangan tartibda Qoraqalpog‘iston Respublikasi, viloyatlar va Toshkent shahri, shuningdek, tuman (shahar)larda tashkil etilgan jamg‘arma;
“Yoshlar daftari” jamg‘armasining ishchi organi — Qoraqalpog‘iston Respublikasi, viloyatlar va Toshkent shahri Yoshlar ishlari agentligining hududiy boshqarmalari hamda tuman (shahar) Yoshlar ishlari agentligi bo‘limlari;
ishsiz yoshlar — haq to‘lanadigan ishga yoki ish haqi (mehnat daromadi) keltiradigan mashg‘ulotga ega bo‘lmagan, ish qidirayotgan va ish taklif etilsa, unga kirishishga tayyor bo‘lgan yoxud kasbga tayyorlashdan, qayta tayyorlashdan o‘tishga yoki malakasini oshirishga tayyor bo‘lgan, ishga joylashishda ko‘mak olish uchun mahalliy mehnat organlariga murojaat qilgan va ushbu organlar tomonidan ish qidirayotgan shaxslar sifatida ro‘yxatga olingan mehnatga layoqatli yoshlar (bundan ta’lim tashkilotlarida tahsil olayotganlar mustasno);
nodavlat kasb-hunarga o‘qitish tashkilotlari — yoshlarni kasb-hunar, tadbirkorlik, ta’lim, fan, madaniyat va san’at, sport, axborot texnologiyalar va xorijiy tillarga o‘qitish vakolatiga ega bo‘lgan nodavlat notijorat tashkilotlar, shu jumladan, nodavlat ta’lim tashkilotlari;
sektorlar — Qoraqalpog‘iston Respublikasi, viloyatlar, tumanlar, shaharlar hududlarini tegishlicha Qoraqalpog‘iston Respublikasi Vazirlar Kengashi Raisi, viloyatlar va Toshkent shahar, tumanlar (shaharlar) hokimlari, prokuratura, ichki ishlar va davlat soliq xizmati hududiy organlari rahbarlari boshchilik qiladigan tumanlar (shaharlar) va hududlarni kompleks ijtimoiy-iqtisodiy rivojlantirish bo‘yicha tegishli mahalliy davlat hokimiyati organining kollegial ishchi tuzilmasi;
yoshlar yetakchisi — O‘zbekiston Respublikasi Prezidentining “Mahallalarda yoshlar bilan ishlash tizimini tubdan takomillashtirish chora-tadbirlari to‘g‘risida” 2022-yil 19-yanvardagi PQ-92-son qarori bilan har bir mahallada joriy etilgan mahallalardagi yoshlar yetakchisi;
xotin-qizlar faoli — O‘zbekiston Respublikasi Prezidentining “Oila va xotin-qizlar bilan ishlash, mahalla va nuroniylarni qo‘llab-quvvatlash tizimini takomillashtirish chora-tadbirlari to‘g‘risida” 2022-yil 1-martdagi PF-81-son Farmoni bilan har bir mahallada joriy etilgan xotin-qizlar faoli;
hokim yordamchisi — O‘zbekiston Respublikasi Prezidentining “Mahallada tadbirkorlikni rivojlantirish, aholi bandligini ta’minlash va kambag‘allikni qisqartirish masalalari bo‘yicha hokim yordamchilari faoliyatini tashkil etish chora-tadbirlari to‘g‘risida” 2021-yil 3-dekabrdagi PQ-31-son qarori bilan har bir mahallada tashkil etilgan mahallada tadbirkorlikni rivojlantirish, aholi bandligini ta’minlash va kambag‘allikni qisqartirish masalalari bo‘yicha tuman (shahar) hokimining yordamchisi.
kalendar reja — yoshlarning intellektual salohiyatini yuksaltirish, ularni bo‘sh vaqtini mazmunli tashkil etish va huquqiy savodxonligini oshirish, shuningdek, besh muhim tashabbus doirasidagi mahalla, sektor, tuman (shahar) va hududiy tadbirlarni moliyalashtirish uchun “Yoshlar daftari” elektron platformasi orqali shakllantiriladigan hamda Yoshlar ishlari agentligi tomonidan tasdiqlanadigan yil yoki yarim yilga mo‘ljallangan reja.
Kalendar rejada aks etmagan biroq hududning o‘ziga xosligidan kelib chiqib, mahalla, sektor, tuman(shahar) bosqichlarini o‘zida aks ettirgan tadbirlarni moliyalashtirish Yoshlar ishlari agentligining hududiy boshqarmasi bilan kelishilgandan so‘ng “Yoshlar daftari” jamg‘armasi mablag‘lari hisobidan amalga oshirilishi mumkin.
Davlat va xo‘jalik boshqaruv organlari, mahalliy davlat hokimiyati organlari tomonidan mahallada yoshlar siyosati sohasida tashkil etiladigan loyiha, tanlov va tadbirlarini moliyalashtirish Yoshlar ishlari agentligi bilan kelishgan holda belgilangan tartibda kalendar rejaga kiritilgandan so‘ng hududiy va tuman (shahar) “Yoshlar daftari” jamg‘armasi mablag‘lari hisobidan moliyalashtiriladi.
3. “Yoshlar daftari”ga kiritilgan yoshlarni ijtimoiy qo‘llab-quvvatlash bo‘yicha chora-tadbirlar ushbu Nizomga muvofiq hamda tegishli qonunchilik hujjatlarida belgilangan tartibda amalga oshiriladi.
“Yoshlar daftari”ni yuritish orqali yoshlar muammolarini tizimli ravishda hal etish va ularni ijtimoiy qo‘llab-quvvatlash mazkur Nizomning 1-ilovasidagi ro‘yxatda keltirilgan subsidiya, kompensatsiya va moddiy yordamlarni berish orqali amalga oshiriladi."""
    for x in range(0, len(text), 4096):
         await call.message.answer(text[x:x + 4096])

@dp.callback_query_handler(bobcallback.filter(number="shakllantirish"))
async def ikki(call:CallbackQuery):
    print('1111')
    await call.answer(cache_time=20)
    text="""2-bob. “Yoshlar daftari”ni shakllantirish
    4. “Yoshlar daftari”ga doimiy yoki vaqtincha yashash joyi bo‘yicha o‘n to‘rt yoshga to‘lgan va o‘ttiz yoshdan oshmagan (o‘ttiz bir yoshga to‘lmagan) quyidagi toifadagi:
oila a’zosi “Temir daftar”, “Ayollar daftari” yoki “Ijtimoiy himoya yagona reyestri”ga kiritilgan;
ijtimoiy himoyaga muhtoj bo‘lgan;
boquvchisini yo‘qotgan, yetim yoki ota-ona qaramog‘idan mahrum bo‘lgan;
o‘ziga nisbatan vasiylik yoki homiylik belgilangan;
o‘zgalar parvarishiga muhtoj bo‘lgan ishga layoqatsiz;
I yoki II guruh nogironligi bo‘lgan;
farzandida I yoki II guruh nogironligi bo‘lgan;
jismoniy va (yoki) ruhiy rivojlanishida nuqsonlari bo‘lgan;
ota-onasidan birida I yoki II guruh nogironligi bo‘lgan, ikkinchisi esa ish faoliyatini to‘xtatgan holda bemorga qarashga majbur bo‘lgan yoxud ota-onasining har ikkisida I yoki II guruh nogironligi bo‘lgan;
yuzaga kelgan holatlar sababli og‘ir turmush sharoitida qolgan;
zo‘ravonlik va ekspluatatsiya, tabiiy ofatlar, halokatlar, yong‘inlar va boshqa favqulodda vaziyatlar oqibatida hayotiga, sog‘lig‘iga, mulkiga zarar yetgan;
“Mehribonlik” uyi, Bolalar shaharchasi yoki oilaviy bolalar uyida tarbiyalangan;
haq to‘lanadigan ishga yoki ish haqi (mehnat daromadi) keltiradigan mashg‘ulotga ega bo‘lmagan;
davolanishga muhtoj bo‘lgan bemor yoshlar;
jazoni ijro etish muassasalaridan qaytgan;
muayyan yashash joyiga ega bo‘lmagan;
psixologik maslahatga muhtoj;
nikohi qayd etilganiga uch yildan oshmagan yosh oila;
dehqonchilik yoki tomorqa xo‘jaligini yuritayotgan;
yosh tadbirkor yoki o‘zini o‘zi band qilgan shaxs sifatida soliq xizmati organlarida ro‘yxatdan o‘tgan yoshlar kiritiladi.
5. “Yoshlar daftari”ga yoshlar yashab turgan joyi bo‘yicha kiritiladi. Bunda yoshlarning yashab turgan joyi bo‘yicha hisobda turmasligi ularni “Yoshlar daftari”ga kiritishni rad etish uchun asos hisoblanmaydi.
Ushbu Nizomning 4-bandida keltirilgan toifadagi ariza beruvchilar elektron platforma orqali:
ariza beruvchining bevosita o‘zi tomonidan elektron platformaga tegishli ma’lumotlarni kiritish;
ariza beruvchi tomonidan Yoshlar ishlari agentligining “1093” qisqa raqamli Call-markaziga murojaat qilish;
yoshlar yetakchisining ko‘magida elektron platformaga ariza beruvchining tegishli ma’lumotlarini kiritish yo‘li bilan “Yoshlar daftari”ga kiritiladi.
6. Ariza beruvchi yashab turgan mahalladagi yoshlar yetakchisi uning “Yoshlar daftari”ga kiritish haqidagi murojaatini uch kun muddatda o‘rganib chiqadi va ariza beruvchining “Yoshlar daftari”ga kiritilishini tasdiqlaydi yoki rad etadi.
Ariza beruvchining ushbu murojaati asosida uning ma’lumotlari tegishli integratsiya qilingan ma’lumotlar bazalari orqali tasdiqlangan hollarda ariza beruvchi “Yoshlar daftari”ga avtomatik tarzda kiritiladi va bunda yoshlar yetakchisining tasdiqlashi talab etilmaydi.
7. Ariza beruvchiga “Yoshlar daftari”ga kiritilganligi yoki kiritish rad etilganligi haqida asoslangan xabar, shu jumladan, SMS-xabarnoma yuboriladi.
8. Ariza beruvchi “Yoshlar daftari”ga kiritilganda tizim tomonidan avtomatik tarzda ariza beruvchi ushbu Nizomga muvofiq olmoqchi bo‘lgan yordam turini olish haqidagi ariza uning nomidan shakllantiriladi va ushbu yordam turini berish yoki bermaslik yuzasidan tavsiya berish uchun ariza beruvchining yashab turgan joyidagi mahallaning yoshlar yetakchisiga yo‘naltiriladi, ushbu Nizomning 3-bobi 2, 4, 5, 6, 10, 13-paragraflarida belgilangan subsidiya va yordam turlari bundan mustasno."""
    for x in range(0, len(text), 4096):
         await call.message.answer(text[x:x + 4096])

@dp.callback_query_handler(text="uch")
async def uch(call:CallbackQuery):

    await call.answer(cache_time=20)
    text="""3-bob. “Yoshlar daftari”ga kiritilgan yoshlarning muammolarini tizimli ravishda hal etish va ularni ijtimoiy qo‘llab-quvvatlash
1-§. “Yoshlar daftari”ga kiritilgan moddiy ahvoli og‘ir yoshlarga bir martalik moddiy yordam ko‘rsatish tartibi
9. “Yoshlar daftari”ga kiritilgan moddiy ahvoli og‘ir yoshlarga bir martalik moddiy yordam ushbu Nizomga 2-ilovada keltirilgan sxemaga muvofiq har bir individual holatda ariza beruvchining hayotiy vaziyati murakkabligini, uning ijtimoiy himoyaga muhtoj ekanligini inobatga olgan holda bazaviy hisoblash miqdorining (keyingi o‘rinlarda — BHM) 4 baravarigacha miqdorda to‘lab beriladi.
10. Ariza beruvchi bir martalik moddiy yordam ajratishni so‘rab mahalladagi yoshlar yetakchisiga ariza beradi.
11. Mahalladagi yoshlar yetakchisi uch ish kuni ichida ariza beruvchining ijtimoiy toifasi va holatini o‘rganadi hamda moddiy yordam ajratish haqidagi tavsiyanoma yoki rad etish to‘g‘risida xabarnomani Vasiylik kengashiga yuboradi.
12. Mahalladagi yoshlar yetakchisining moddiy yordam ajratish haqidagi ijobiy tavsiyasi asosida Vasiylik kengashi qarori qabul qilinib, yetti ish kuni ichida tuman (shahar)lar hokimliklariga yuboriladi.
Vasiylik kengashi qarori asosida tuman (shahar)lar hokimliklari “Yoshlar daftari” jamg‘armasi mablag‘lari hisobidan zarur mablag‘larni uch ish kuni ichida Xalq bankining tegishli bo‘limi (filiali)ga o‘tkazadi.
13. Xalq bankining tegishli bo‘limi (filiali) tomonidan bir martalik moddiy yordam to‘lovlarini uch ish kuni ichida ariza beruvchiga naqd yoki naqd pulsiz shaklda to‘lab beradi.
Oyning oxirgi ish kunida qaydnomalar yopiladi, tayinlangan, biroq o‘z vaqtida talab qilib olinmagan moddiy yordam, uni oluvchining nomidagi maxsus depozit hisob raqamiga o‘tkaziladi va oluvchining birinchi talabiga ko‘ra to‘lanadi.
Shuningdek, oyning 27-kuniga qadar to‘lanmagan moddiy yordamga yo‘naltirilgan mablag‘lar har oyning oxirida tegishli hisob raqamlarga qaytariladi. Qaydnomaning bir nusxasi Yoshlar ishlari agentligining tuman (shahar) bo‘limiga taqdim etiladi.
Ariza beruvchi tomonidan talab qilib olinmagan moddiy yordam mablag‘larini qonunchilikda belgilangan tartibda “Yoshlar daftari” jamg‘armasi hisob raqamiga qaytarish choralari ko‘riladi.
“Yoshlar daftari” jamg‘armasining ishchi organi muhtoj yoshlarga to‘langan bir martalik moddiy yordam to‘g‘risidagi ma’lumotlar qaydnoma nusxasi taqdim etilgan kundan boshlab uch kun muddatda elektron platformadagi yoshlarning individual so‘rovnomasiga kiritilishini ta’minlaydi.
Bunda Xalq bankining tegishli axborot tizimidagi ma’lumotlar bo‘yicha elektron platforma bilan o‘zaro axborot almashinuvi tizimi joriy etilgandan so‘ng elektron qaydnoma nusxasini taqdim etish hamda yoshlarning individual so‘rovnomasiga kiritish talab etilmaydi.
14. Shaxsga bir martalik moddiy yordam berilishi uni “Yoshlar daftari”dan chiqarishga asos bo‘lmaydi.
15. Moddiy yordam shaxsga bir kalendar yil davomida bir marotaba beriladi.
2-§. “Yoshlar daftari”ga kiritilgan yoshlarni tadbirkorlikka va kasb-hunarga o‘qitish kurslari xarajatlarini qoplash tartibi
16. “Yoshlar daftari”ga kiritilgan yoshlarni tadbirkorlikka va kasb-hunarga o‘qitish uchun sarflangan xarajatlarning 75 foizigacha qismi hokim yordamchisining ijobiy tavsiyasi asosida “Yoshlar daftari” jamg‘armasi mablag‘lari hisobidan ushbu Nizomga 3-ilovadagi sxemaga muvofiq o‘qitish xizmatini ko‘rsatgan nodavlat ta’lim tashkiloti yoki kasb-hunarga o‘qitish markaziga qoplab beriladi.
Bunda yoshlarni tadbirkorlikka va kasb-hunarga o‘qitish uchun sarflangan xarajatlarning 75 foizigacha qismi, biroq bir oygacha, bir oydan ikki oygacha, ikki oydan ortiq muddatli o‘quv kurslari uchun tegishlicha BHMning 4, 8, 12 baravaridan ko‘p bo‘lmagan qismi qoplab beriladi.
O‘quv kurslari xarajatlarining qolgan qismi ariza beruvchi tomonidan nodavlat ta’lim tashkilotiga to‘lab beriladi.
17. Tadbirkorlikka yoki kasb-hunarga o‘qish istagida bo‘lgan ariza beruvchi o‘qitish kurslari xarajatlarini qoplashni so‘rab Vasiylik kengashiga o‘zi va ta’lim tashkiloti o‘rtasida tuzilgan shartnoma nusxasini taqdim etadi.
Shartnomada ta’lim tashkilotining nomi, STIR, o‘quv kursi yoki o‘qitiladigan kasb-hunar nomi, o‘quv kursining bir oylik to‘lovi miqdori va umumiy muddati ko‘rsatilgan bo‘lishi lozim.
Taqdim etilgan hujjatlardagi ma’lumotlarning to‘g‘riligi va haqqoniyligi uchun ariza beruvchi javobgar hisoblanadi.
Ushbu bandda nazarda tutilgan hujjatlar taqdim etilgandan so‘ng Vasiylik kengashi uch ish kuni ichida murojaatni unga ilova qilingan hujjatlar bilan birga ariza beruvchi yashab kelayotgan mahalladagi hokim yordamchisiga ko‘rib chiqish uchun yuboradi.
Hokim yordamchisi besh ish kuni ichida o‘qish xarajatlarini qoplash haqidagi tavsiyanoma yoki rad etish haqidagi xabarnomani Vasiylik kengashiga yuboradi. Bunda subsidiya ajratishni rad etish haqidagi xabarnoma yuborilganda rad etish sabablari asoslanishi talab etiladi.
Agar hokim yordamchisi murojaatni unga kelib tushgan paytdan boshlab besh ish kuni ichida ko‘rib chiqmasa yoki o‘qish xarajatlarini qoplashni asossiz rad etish haqida xabarnoma bersa, ariza beruvchining murojaati ushbu Nizom talablariga muvofiq bo‘lganda Vasiylik kengashi uning murojaatini qanoatlantirish huquqiga ega bo‘ladi.
Murojaatni o‘rganish natijalari bo‘yicha Vasiylik kengashi tomonidan o‘qish xarajatlarini qoplash haqida qaror qabul qilingandan so‘ng uch ish kuni ichida o‘quv kursi uchun belgilangan mablag‘lar ariza beruvchining o‘qiganligini tasdiqlovchi hisob-faktura va dalolatnomaga asosan ta’lim tashkilotining hisob raqamiga o‘tkazib boriladi.
18. Hokim yordamchisi ariza beruvchi haqiqatda o‘quv kursida o‘qiyotganligini har oyda kamida bir marta monitoring asosida o‘rganadi.
O‘rganish jarayonida ariza beruvchi o‘quv kursida o‘qimayotganligi aniqlangan taqdirda, hokim yordamchisining taqdimnomasiga asosan o‘quv kursi xarajatlarini qoplash to‘xtatiladi.
3-§. “Yoshlar daftari”ga kiritilgan yoshlarning davlat va nodavlat ta’lim tashkilotlarida avtomototransport vositalari haydovchilarini tayyorlash o‘quv kursi xarajatlarini qoplash uchun subsidiya ajratish tartibi
19. “Yoshlar daftari”ga kiritilgan ijtimoiy himoyaga muhtoj yoshlarning davlat va nodavlat ta’lim tashkilotlarida avtomototransport vositalari haydovchilarini tayyorlash o‘quv kursining xarajatlarini qoplash uchun BHMning 4 baravarigacha miqdorda yoshlar yetakchisining ijobiy tavsiyasi asosida “Yoshlar daftari” jamg‘armasi mablag‘lari hisobidan ushbu Nizomga 4-ilovada keltirilgan sxemaga muvofiq o‘qitish xizmatini ko‘rsatgan davlat va nodavlat ta’lim tashkilotiga subsidiya ajratiladi.
O‘qish xarajatlarining qolgan qismi ariza beruvchi tomonidan ta’lim tashkilotiga to‘lab beriladi.
20. Avtomototransport vositalari haydovchilarini tayyorlash o‘quv kursida o‘qish istagida bo‘lgan ariza beruvchi o‘qitish kurslari xarajatlari uchun subsidiya ajratishni so‘rab Vasiylik kengashiga o‘zi va ta’lim tashkiloti o‘rtasida tuzilgan shartnoma nusxasini taqdim etadi.
Shartnomada ta’lim tashkilotining nomi, STIR, o‘qitiladigan toifa nomi, o‘quv kursining bir oylik to‘lovi miqdori va umumiy muddati ko‘rsatilgan bo‘lishi lozim.
Taqdim etilgan hujjatlardagi ma’lumotlarning to‘g‘riligi va haqqoniyligi uchun ariza beruvchi javobgar hisoblanadi.
Ushbu bandda nazarda tutilgan hujjatlar taqdim etilgandan so‘ng Vasiylik kengashi uch ish kuni ichida murojaatni unga ilova qilingan hujjatlar bilan birga ariza beruvchi yashab kelayotgan mahalladagi yoshlar yetakchisiga ko‘rib chiqish uchun yuboradi.
Mahalladagi yoshlar yetakchisi besh ish kuni ichida murojaatni ko‘rib chiqadi va o‘qish xarajatlarini qoplash haqidagi tavsiyanoma yoki rad etish to‘g‘risidagi xabarnomani Vasiylik kengashiga yuboradi. Bunda subsidiya ajratishni rad etish to‘g‘risida xabarnoma yuborilganda rad etish sabablari asoslanishi talab etiladi.
Agar mahalladagi yoshlar yetakchisi murojaatni unga tushgan paytdan boshlab besh ish kuni ichida ko‘rib chiqmasa yoki o‘qish xarajatlarini qoplashni asossiz rad etish haqida xabarnoma bersa, ariza beruvchining murojaati ushbu paragraf talablariga muvofiq bo‘lganda Vasiylik kengashi uning murojaatini qanoatlantirish huquqiga ega bo‘ladi.
21. Murojaatni o‘rganish natijalari bo‘yicha Vasiylik kengashi tomonidan o‘qish xarajatlarini qoplash haqida qaror qabul qilingandan so‘ng uch ish kuni ichida o‘quv kursi uchun belgilangan mablag‘lar ariza beruvchining o‘qiganligini tasdiqlovchi hisob-faktura va dalolatnomaga asosan ta’lim tashkilotining hisob raqamiga o‘tkazib boriladi.
22. Mahalladagi yoshlar yetakchisi ariza beruvchining haqiqatda o‘quv kursida o‘qiyotganligini har oyda kamida bir marta monitoring qilib boradi.
O‘rganish jarayonida ariza beruvchi o‘quv kursida o‘qimayotganligi aniqlangan taqdirda, yoshlar yetakchisining taqdimnomasiga asosan o‘quv kursi xarajatlarini qoplash to‘xtatiladi va to‘langan summa belgilangan tartibda undiriladi.
4-§. “Yoshlar daftari”ga kiritilgan dehqonchilik va tomorqa xo‘jaligini yuritish bilan shug‘ullanayotgan yoshlarga urug‘lik va ko‘chatlar xarid qilish uchun subsidiya ajratish tartibi
23. Tomorqa yer egasi bo‘lgan yoki dehqonchilik bilan shug‘ullanish uchun, shu jumladan, yangi o‘zlashtirilgan, lalmi, foydalanilmayotgan yer maydonlarida 0,1 gektardan 1 gektargacha yer maydoni ajratib berilgan yoshlarga urug‘lik va ko‘chatlar xarid qilish uchun BHMning 8 baravarigacha miqdorda hokim yordamchisining ijobiy tavsiyasi asosida “Yoshlar daftari” jamg‘armasi mablag‘lari hisobidan ushbu Nizomga 5-ilovada keltirilgan sxemaga muvofiq subsidiya ajratiladi.
Subsidiya ajratish uchun ariza beruvchi Vasiylik kengashiga quyidagi hujjatlarni taqdim etadi:
ariza beruvchining egaligida yoki foydalanishida bo‘lgan erga nisbatan huquqini tasdiqlovchi hujjat (ijara shartnomasi va boshqalar);
urug‘lik va ko‘chatlarni xarid qilish bo‘yicha yetkazib beruvchi tashkilot bilan tuzilgan shartnoma nusxasi. Shartnomada yetkazib beruvchining nomi, STIR, xarid qilinadigan mahsulot nomi, to‘lov summasi ko‘rsatilishi lozim.
Taqdim etilgan hujjatlardagi ma’lumotlarning to‘g‘riligi va haqqoniyligi uchun ariza beruvchi javobgar hisoblanadi.
Ushbu bandda nazarda tutilgan hujjatlar taqdim etilgandan so‘ng Vasiylik kengashi uch ish kuni ichida murojaatni unga ilova qilingan hujjatlar bilan birga ariza beruvchi faoliyat yuritib kelayotgan mahalladagi hokim yordamchisiga ko‘rib chiqish uchun yuboradi.
24. Hokim yordamchisi yoshlar yetakchisi va tegishli soha mutaxassislari bilan birgalikda “Yoshlar daftari”ga kiritilgan ariza beruvchining murojaati tushgan kundan boshlab besh ish kuni ichida joyiga chiqqan holda ariza beruvchining tomorqa erida yoki dehqonchilik bilan shug‘ullanish uchun ajratilgan ekin maydonida urug‘lik va ko‘chatlar ekish uchun mavjud sharoitni o‘rganadi.
Hokim yordamchisi o‘rganish natijalariga ko‘ra, ariza beruvchining tomorqa eriga yoki dehqonchilik bilan shug‘ullanish uchun ajratilgan ekin maydonida urug‘lik va ko‘chatlar xarid qilish uchun subsidiya ajratish haqidagi tavsiyanoma yoki rad qilish to‘g‘risidagi xabarnomani Vasiylik kengashiga kiritadi. Bunda subsidiya ajratishni rad etish haqida xabarnoma yuborilganda rad etish sabablari asoslanishi talab etiladi.
Agar hokim yordamchisi murojaatni unga tushgan paytdan boshlab besh kuni ichida ko‘rib chiqmasa yoki subsidiya ajratishni asossiz rad etish haqida xabarnoma bersa, ariza beruvchining murojaati ushbu paragraf talablariga muvofiq bo‘lganda Vasiylik kengashi uning murojaatini qanoatlantirish huquqiga ega bo‘ladi.
25. Vasiylik kengashining qaroriga asosan uch ish kuni ichida “Yoshlar daftari” jamg‘armasi mablag‘lari hisobidan subsidiya yetkazib beruvchi tashkilotning hisob raqamiga o‘tkaziladi.
5-§. “Yoshlar daftari”ga kiritilgan yoshlarga tadbirkorlik faoliyati va o‘zini o‘zi band qilish uchun noturar joyning ijara xarajatlarini qoplash tartibi
26. “Yoshlar daftari”ga kiritilgan yosh tadbirkor yoki o‘zini o‘zi band qilgan shaxs sifatida soliq xizmati organlarida ro‘yxatdan o‘tgan yosh fuqaroga faoliyatini amalga oshirayotgan noturar joyning 12 oygacha ijara xarajatlarining bir yilda 30 foizi, biroq BHMning 25 baravarigacha bo‘lgan qismi hokim yordamchisining ijobiy tavsiyasi asosida “Yoshlar daftari” jamg‘armasi mablag‘lari hisobidan ushbu Nizomga 6-ilovada keltirilgan sxemaga muvofiq ijaraga beruvchi tashkilotga qoplab beriladi.
27. Noturar joyning ijara xarajatlarini qoplash uchun ariza beruvchi Vasiylik kengashiga quyidagi hujjatlarni taqdim etadi:
tadbirkorlik subyekti guvohnomasi nusxasi yoki o‘zini o‘zi band qilgan sifatida ro‘yxatdan o‘tganlikni tasdiqlovchi matritsali shtrix kodli (QR-kod) ma’lumotnoma;
ijara shartnomasining soliq organlarida hisobga qo‘yilganligi haqidagi bildirishnoma;
ijara shartnomasi nusxasi. Bunda ijara shartnomasida ijaraga beruvchining nomi, STIR, ijara muddati, ijaraning bir oylik va umumiy to‘lovi miqdori ko‘rsatilishi lozim.
Taqdim etilgan hujjatlardagi ma’lumotlarning to‘g‘riligi va haqqoniyligi uchun ariza beruvchi javobgar hisoblanadi.
Ushbu bandda nazarda tutilgan hujjatlar taqdim etilgandan so‘ng Vasiylik kengashi uch ish kuni ichida murojaatni ilova qilingan hujjatlar bilan birga ariza beruvchi faoliyat yuritib kelayotgan mahalladagi hokim yordamchisiga ko‘rib chiqish uchun yuboradi.
Hokim yordamchisi besh ish kuni ichida ijara xarajatlarini qoplash haqidagi tavsiyanomani yoki rad etish haqida xabarnomani Vasiylik kengashiga yuboradi. Bunda, ijara xarajatlarini qoplashni rad etish haqida xabarnoma yuborilganda rad etish sabablari asoslantirishi talab etiladi.
Agar hokim yordamchisi murojaatni unga tushgan paytdan boshlab besh ish kuni ichida ko‘rib chiqmasa yoki subsidiya ajratishni asossiz rad etish haqida xabarnoma bersa, ariza beruvchining murojaati ushbu paragraf talablariga muvofiq bo‘lganda Vasiylik kengashi uning murojaatini qanoatlantirish huquqiga ega bo‘ladi.
28. Murojaatni o‘rganish natijalari bo‘yicha Vasiylik kengashi tomonidan ijara xarajatlarini qoplash haqida qaror qabul qilinganda ariza beruvchi bino va inshootdan foydalanayotganligi to‘g‘risida ijaraga beruvchi bilan har oy yakuni bo‘yicha tuziladigan va keyingi oyning 5-kunigacha taqdim etiladigan hisob-faktura va dalolatnomaga asosan Vasiylik kengashi bino va inshootning ijara haqi uchun to‘lovni uch ish kuni ichida ijaraga beruvchining hisob raqamiga o‘tkazadi.
29. Hokim yordamchisi ijaraga olingan bino va inshootning ijaraga oluvchi tomonidan haqiqatda foydalanilayotganligini har oyda kamida bir marta monitoring asosida o‘rganadi.
O‘rganish jarayonida ijaraga oluvchi tomonidan ijaraga olingan bino va inshootdan foydalanilmayotganligi aniqlangan taqdirda, hokim yordamchisining taqdimnomasiga asosan ijara to‘lovi uchun subsidiya berish to‘xtatiladi.
6-§. “Yoshlar daftari”ga kiritilgan yoshlarga tadbirkorlik faoliyatini boshlash va o‘zini o‘zi band qilishga zarur bo‘lgan asbob-uskunalar yoki mehnat qurollarini xarid qilishga subsidiya ajratish tartibi
30. Tadbirkorlik yoki o‘zini o‘zi band qilish faoliyatini boshlamoqchi bo‘lgan yoshlarga asbob-uskuna yoki mehnat qurollari (motokultivator, o‘t o‘rish o‘roq mashinasi, perforator, payvandlash apparati, o‘simliklarga ishlov berish qurilmasi, duradgorlik, chilangarlik uskunasi, qurilish uskunasi, kompyuter jamlanmasi va boshqalar)ni xarid qilish uchun BHMning 40 baravarigacha miqdorda hokim yordamchisining ijobiy tavsiyasi asosida “Yoshlar daftari” jamg‘armasi mablag‘lari hisobidan ushbu Nizomga 7-ilovada keltirilgan sxemaga muvofiq subsidiya ajratiladi.
31. Asbob-uskuna yoki mehnat qurollari uchun subsidiya ajratish uchun ariza beruvchi Vasiylik kengashiga unga zarur bo‘lgan asbob-uskuna yoki mehnat qurollarining turi, miqdori, tovarning markasi, taxminiy xarid narxi to‘g‘risidagi ma’lumotlarni taqdim etadi.
Taqdim etilgan hujjatlardagi ma’lumotlarning to‘g‘riligi va haqqoniyligi uchun ariza beruvchi javobgar hisoblanadi.
Ushbu bandda nazarda tutilgan hujjatlar taqdim etilgandan so‘ng Vasiylik kengashi uch ish kuni ichida murojaatni unga ilova qilingan hujjatlar bilan birga ariza beruvchi yashab kelayotgan mahalladagi hokim yordamchisiga ko‘rib chiqish uchun yuboradi.
Hokim yordamchisi besh ish kuni ichida asbob-uskuna yoki mehnat qurollari uchun subsidiya ajratish haqidagi tavsiyani yoki rad etish to‘g‘risidagi xabarnomani Vasiylik kengashiga yuboradi. Bunda, subsidiya ajratishni rad etish haqida xabarnoma yuborilganda rad etish sabablari asoslanishi talab etiladi.
Agar hokim yordamchisi murojaatni unga tushgan paytdan boshlab besh ish kuni ichida ko‘rib chiqmasa yoki subsidiya ajratishni asossiz rad etish haqida xabarnoma bersa, ariza beruvchining murojaati ushbu paragraf talablariga muvofiq bo‘lganda Vasiylik kengashi uning murojaatini qanoatlantirish huquqiga ega bo‘ladi.
32. Murojaatni o‘rganish natijalari bo‘yicha Vasiylik kengashi tomonidan subsidiya ajratish haqida qaror qabul qilinganda asbob-uskuna yoki mehnat qurollarini yetkazib beruvchi tashkilot davlat xaridlarining elektron tizimi orqali besh ish kuni ichida aniqlanadi, asbob-uskuna yoki mehnat quroli yetkazib beruvchi tashkilot tomonidan taqdim etilgandan so‘ng Vasiylik kengashining ishchi organi va ariza beruvchi o‘rtasida tuziladigan dalolatnoma asosida ariza beruvchiga uch ish kuni ichida topshiriladi.
33. Ariza beruvchiga ajratilgan subsidiya asosida xarid qilingan asbob-uskuna yoki mehnat qurollaridan samarali foydalanilayotganligi, uning texnik holati sozligi kafolat muddati davomida hokim yordamchisi tomonidan o‘rganiladi.
34. O‘rganish davomida asbob-uskuna yoki mehnat qurollaridan ish faoliyatida foydalanilmaganligi aniqlangan taqdirda, Vasiylik kengashi tomonidan ariza beruvchidan subsidiya asosida berilgan asbob-uskuna yoki mehnat qurollarini qaytarish choralari ko‘riladi.
7-§. “Yoshlar daftari”ga kiritilgan yoshlarga professional va oliy ta’lim tashkilotlari o‘quvchi-talabalarining ta’lim to‘lov-kontrakt summasining bir qismini to‘lab berish tartibi
35. Respublikamizdagi professional ta’lim tashkilotlarida ta’lim olayotgan, shuningdek, O‘zbekiston Respublikasida faoliyat ko‘rsatayotgan barcha oliy ta’lim tashkilotlarida (davlat, nodavlat oliy ta’lim tashkilotlari, O‘zbekiston Respublikasi hududidagi xorijiy oliy ta’lim tashkilotlari va xorijiy oliy ta’lim tashkilotlarining filiallarida) bakalavriatning kunduzgi, sirtqi va kechki shaklida, magistraturaning kunduzgi yo‘nalishida ta’lim olayotgan o‘quvchi-talabalarga to‘lov-kontrakt asosida o‘qish bo‘yicha yillik xarajatlarining bir qismi qoplab beriladi.
Ushbu xarajatlarni to‘lab berish yoshlar yetakchisining ijobiy tavsiyasi asosida “Yoshlar daftari” jamg‘armasi mablag‘lari hisobidan to‘lov-kontrakt summasining 50 foizigacha, biroq BHMning 50 baravaridan oshmagan miqdorda ushbu Nizomga 8-ilovada keltirilgan sxemaga muvofiq amalga oshiriladi (ikkinchi va undan keyingi mutaxassislik, qo‘shma ta’lim dasturlari bo‘yicha, tabaqalashtirilgan to‘lov-kontrakt asosida ta’lim olayotganlar bundan mustasno).
36. O‘quvchi-talabalar to‘lov-kontrakt xarajatlarining bir qismini to‘lab berishni so‘rab Vasiylik kengashiga to‘lov-kontrakt asosida o‘qish haqida belgilangan tartibda rasmiylashtirilgan shartnoma (kontrakt) nusxasini taqdim etishi lozim.
Kontraktda o‘qishning belgilangan muddati va bir yil uchun to‘lov miqdori ko‘rsatilgan bo‘lishi talab etiladi.
Taqdim etilgan hujjatlardagi ma’lumotlarning to‘g‘riligi va haqqoniyligi uchun ariza beruvchi javobgar hisoblanadi.
Hujjatlar taqdim etilgandan so‘ng Vasiylik kengashi uch ish kuni ichida murojaatni unga ilova qilingan hujjatlar bilan birga ariza beruvchi yashab kelayotgan mahalladagi yoshlar yetakchisiga ko‘rib chiqish uchun yuboradi.
Mahalladagi yoshlar yetakchisi besh ish kuni ichida to‘lov-kontrakt xarajatlarini qoplash haqidagi tavsiyanoma yoki rad etish to‘g‘risidagi xabarnomani Vasiylik kengashiga yuboradi. Bunda to‘lov-kontrakt xarajatlarini qoplashni rad etish haqida xabarnoma yuborilganda rad etish sabablari asoslanishi talab etiladi.
Agar mahalladagi yoshlar yetakchisi murojaatni unga tushgan paytdan boshlab besh ish kuni ichida ko‘rib chiqmasa yoki subsidiya ajratishni asossiz rad etish haqida xabarnoma bersa, ariza beruvchining murojaati ushbu paragraf talablariga muvofiq bo‘lganda Vasiylik kengashi uning murojaatini qanoatlantirish huquqiga ega bo‘ladi.
37. Murojaatni o‘rganish natijalari bo‘yicha Vasiylik kengashi tomonidan to‘lov-kontrakt xarajatlarini qoplash haqida qaror qabul qilingandan so‘ng uch ish kuni ichida belgilangan miqdordagi to‘lov-kontrakt mablag‘lari professional ta’lim yoki oliy ta’lim tashkilotining hisob raqamiga o‘tkazib beriladi.
8-§. “Yoshlar daftari”ga kiritilgan yoshlarga zamonaviy kasblarni egallashi, axborot texnologiyalarini o‘rganishi va ularni xorijiy tillarga o‘qitish bo‘yicha o‘quv kurslarida o‘qish xarajatlarini qoplash uchun subsidiya ajratish tartibi
38. Yoshlarga zamonaviy kasblarni egallashi, axborot texnologiyalarni o‘rganishi va ularni xorijiy tillarga o‘qitish bo‘yicha olti oygacha muddatli o‘quv kurslari uchun har oyda BHMning 4 baravarigacha miqdorda yoshlar yetakchisining ijobiy tavsiyasi asosida “Yoshlar daftari” jamg‘armasi mablag‘lari hisobidan ushbu Nizomga 9-ilovada keltirilgan sxemaga muvofiq subsidiya ajratiladi.
Bunda ariza beruvchiga “1+1” tamoyili asosida bir vaqtning o‘zida zamonaviy kasb yoki axborot texnologiyalar o‘quv kursi bilan birgalikda xorijiy til o‘quv kursida o‘qish xarajatlari uchun ham subsidiya ajratilishi mumkin.
Mazkur bandda nazarda tutilgan xarajatlarni qoplash uchun Yoshlar ishlari agentligining Yoshlarga oid davlat siyosatini qo‘llab-quvvatlash jamg‘armasi hisobidan ham qonunchilik hujjatlarida belgilangan tartibda subsidiya ajratilishi mumkin.
39. Ariza beruvchi subsidiya ajratishni so‘rab Vasiylik kengashiga o‘zi va nodavlat ta’lim tashkiloti o‘rtasida tuzilgan shartnoma nusxasini taqdim etadi.
Shartnomada nodavlat ta’lim tashkilotining nomi, STIR, o‘qitiladigan zamonaviy kasb, xorijiy til turi yoki axborot texnologiyalar yo‘nalishi, o‘quv kursining bir oylik to‘lovi miqdori va umumiy muddati ko‘rsatilgan bo‘lishi lozim.
Taqdim etilgan hujjatlardagi ma’lumotlarning to‘g‘riligi va haqqoniyligi uchun ariza beruvchi javobgar hisoblanadi.
Hujjatlar taqdim etilgandan so‘ng Vasiylik kengashi uch ish kuni ichida murojaatni unga ilova qilingan hujjatlar bilan birga ariza beruvchi yashab kelayotgan mahalladagi yoshlar yetakchisiga ko‘rib chiqish uchun yuboradi.
Mahalladagi yoshlar yetakchisi besh ish kuni ichida subsidiya ajratish haqidagi tavsiyanoma yoki rad etish to‘g‘risidagi xabarnomani Vasiylik kengashiga yuboradi. Bunda, subsidiya ajratishni rad etish haqida xabarnoma yuborilganda rad etish sabablari asoslanishi talab etiladi.
Agar mahalladagi yoshlar yetakchisi murojaatni unga tushgan paytdan boshlab besh ish kuni ichida ko‘rib chiqmasa yoki subsidiya ajratishni asossiz rad etish haqida xabarnoma bersa, ariza beruvchining murojaati ushbu paragraf talablariga muvofiq bo‘lganda Vasiylik kengashi uning murojaatini qanoatlantirish huquqiga ega bo‘ladi.
40. Murojaatni o‘rganish natijalari bo‘yicha Vasiylik kengashi tomonidan subsidiya ajratish haqida qaror qabul qilingandan so‘ng uch ish kuni ichida o‘quv kursi uchun belgilangan mablag‘lar ariza beruvchining o‘qiganligini tasdiqlovchi hisob-faktura va dalolatnomaga asosan nodavlat ta’lim tashkilotining hisob raqamiga o‘tkazib boriladi.
41. Mahalladagi yoshlar yetakchisi ariza beruvchi tomonidan haqiqatda o‘quv kursida o‘qiyotganligini har oyda kamida bir marta monitoring asosida o‘rganadi.
O‘rganish jarayonida ariza beruvchi tomonidan o‘quv kursida o‘qimayotganligi aniqlangan taqdirda, yoshlar yetakchisining taqdimnomasiga asosan o‘quv kursi uchun subsidiya berish to‘xtatiladi.
9-§. “Yoshlar daftari”ga kiritilgan ijtimoiy himoyaga muhtoj iqtidorli yoshlarning ilm-fan, sport, san’at va madaniyat yo‘nalishlaridagi o‘quv kurslari uchun subsidiya ajratish tartibi
42. Yoshlarning ilm-fan, sport, san’at va madaniyat yo‘nalishlaridagi olti oygacha muddatli o‘quv kurslari uchun har oyda BHMning bir baravarigacha miqdorda mahalladagi yoshlar yetakchisining ijobiy tavsiyasi asosida “Yoshlar daftari” jamg‘armasi mablag‘lari hisobidan ushbu Nizomga 10-ilovada keltirilgan sxemaga muvofiq subsidiya ajratiladi.
Mazkur paragrafda nazarda tutilgan xarajatlarni qoplash uchun Yoshlar ishlari agentligining Yoshlarga oid davlat siyosatini qo‘llab-quvvatlash jamg‘armasi hisobidan ham qonunchilik hujjatlarida belgilangan tartibda subsidiya ajratilishi mumkin.
43. Ariza beruvchi o‘quv kursida o‘qish uchun subsidiya ajratishni so‘rab Vasiylik kengashiga o‘zi va nodavlat ta’lim tashkiloti o‘rtasida tuzilgan shartnoma nusxasini taqdim etadi.
Shartnomada nodavlat ta’lim tashkilotining nomi, STIR, o‘qitiladigan ta’lim turi, o‘quv kursining bir oylik to‘lovi miqdori va umumiy muddati ko‘rsatilgan bo‘lishi lozim.
Taqdim etilgan hujjatlardagi ma’lumotlarning to‘g‘riligi va haqqoniyligi uchun ariza beruvchi javobgar hisoblanadi.
Ushbu bandda nazarda tutilgan hujjatlar taqdim etilgandan so‘ng Vasiylik kengashi uch ish kuni ichida murojaatni unga ilova qilingan hujjatlar bilan birga ariza beruvchi yashab kelayotgan mahalladagi yoshlar yetakchisiga ko‘rib chiqish uchun yuboradi.
Mahalladagi yoshlar yetakchisi besh ish kuni ichida subsidiya ajratish haqidagi tavsiyanoma yoki rad etish to‘g‘risidagi xabarnomani Vasiylik kengashiga yuboradi. Bunda, subsidiya ajratishni rad etish haqida xabarnoma yuborilganda rad etish sabablari asoslantirilishi talab etiladi.
Agar mahalladagi yoshlar yetakchisi murojaatni unga tushgan paytdan boshlab besh ish kuni ichida ko‘rib chiqmasa yoki subsidiya ajratishni asossiz rad etish haqida xabarnoma bersa, ariza beruvchining murojaati ushbu paragraf talablariga muvofiq bo‘lganda Vasiylik kengashi uning murojaatini qanoatlantirish huquqiga ega bo‘ladi.
44. Murojaatni o‘rganish natijalari bo‘yicha Vasiylik kengashi tomonidan subsidiya ajratish haqida qaror qabul qilingandan so‘ng uch ish kuni ichida o‘quv kursi uchun belgilangan mablag‘lar ariza beruvchining o‘qiganligini tasdiqlovchi hisob-faktura va dalolatnomaga asosan nodavlat ta’lim tashkilotining hisob raqamiga o‘tkazib boriladi.
45. Mahalladagi yoshlar yetakchisi ariza beruvchi haqiqatda o‘quv kursida o‘qiyotganligi to‘g‘risida har oyda kamida bir marta monitoring asosida o‘rganadi.
O‘rganish jarayonida ariza beruvchi tomonidan o‘quv kursida o‘qimayotganligi aniqlangan taqdirda, yoshlar yetakchisining taqdimnomasiga asosan o‘quv kursi uchun subsidiya berish to‘xtatiladi.
10-§. “Yoshlar daftari”ga kiritilgan yoshlarning ilm-fan, sport, san’at va madaniyat yo‘nalishlaridagi olimpiada, tanlov va musobaqalarda qatnashish xarajatlari uchun subsidiya ajratish tartibi
46. Yoshlarning ilm-fan, sport, san’at va madaniyat yo‘nalishlaridagi olimpiada, tanlov va musobaqalarning mahalliy bosqichlarida qatnashish uchun ishtirokchilarning yashash va transport xarajatlarini qoplash uchun BHMning 4 baravarigacha hamda ushbu olimpiada, tanlov va musobaqalarning xalqaro bosqichlarida qatnashish xarajatlari (ishtirokchilarning yashash va transport xarajatlari) uchun BHMning 40 baravarigacha miqdorda “Yoshlar daftari” jamg‘armasi mablag‘lari hisobidan ushbu Nizomga 11-ilovada keltirilgan sxemaga muvofiq subsidiya ajratiladi.
Mazkur paragrafda nazarda tutilgan xarajatlarni qoplash uchun Yoshlar ishlari agentligining Yoshlarga oid davlat siyosatini qo‘llab-quvvatlash jamg‘armasi hisobidan ham qonunchilik hujjatlarida belgilangan tartibda subsidiya ajratilishi mumkin.
47. Olimpiada, tanlov va musobaqalarning mahalliy va xalqaro bosqichlarida qatnashish xarajatlari uchun subsidiya ajratishni so‘rab ariza beruvchi Vasiylik kengashiga olimpiada, tanlov va musobaqalarda ishtirok etish huquqini tasdiqlovchi hujjatlarni (sportni rivojlantirish bo‘limi, madaniyat bo‘limi, xalq ta’limi bo‘limi yoki tegishli sport federatsiyalarining Vasiylik kengashi nomiga rasmiy xati va boshqalar) taqdim etadi.
Taqdim etilgan hujjatlardagi ma’lumotlarning to‘g‘riligi va haqqoniyligi uchun ariza beruvchi javobgar hisoblanadi.
Bunda ushbu subsidiyani berish uchun mahalladagi yoshlar yetakchisining tavsiyasi talab etilmaydi.
Vasiylik kengashi talabgorning arizasini uch ish kuni ichida o‘rganib chiqib qaror qabul qiladi.
48. Vasiylik kengashi qaroriga asosan ariza beruvchining transport (temiryo‘l, avia hamda viloyatlararo va shaharlararo qatnovchi avtobus) xarajatlari:
havo transportida — iqtisodiy klass tarifi bo‘yicha;
temir yo‘l transportida — 2-klass tarifi bo‘yicha qoplash uchun chipta realizatsiya qiluvchi tashkilotlarning hisob raqamiga o‘tkazib beriladi.
49. Olimpiada, tanlov va musobaqa davomidagi yashash xarajatlari vazirliklar, idoralar, korxonalar va tashkilotlar xodimlari O‘zbekiston Respublikasi tashqarisiga xizmat safariga yuborilganda xizmat safari xarajatlari uchun mablag‘lar berish tartibi to‘g‘risidagi nizomga (2015-yil 19-noyabr, ro‘yxat raqami 2730) 1-ilovada belgilangan summalarda (transport xarajatlarini qo‘shganda ushbu Nizomning 46-bandida belgilangan miqdordan oshmagan holda) qoplanadi.
Vasiylik kengashi tomonidan uch ish kuni ichida zarur chora-tadbirlar belgilanadi va mablag‘lar o‘tkazib beriladi.
11-§. “Yoshlar daftari”ga kiritilgan yoshlarga ta’lim, madaniyat va san’at, sport, axborot texnologiyalar sohasiga va fanlarni o‘qitishga ixtisoslashgan nodavlat ta’lim tashkilotining noturar joy ijara xarajatlarini qoplash tartibi
50. Yoshlarga ta’lim, madaniyat va san’at, sport, axborot texnologiyalar sohasiga va fanlarni o‘qitishga ixtisoslashgan nodavlat ta’lim tashkilotining uch oy muddatgacha noturar joy ijara xarajatlari uchun BHMning 50 baravarigacha miqdorda mahalladagi yoshlar yetakchisining ijobiy tavsiyasi asosida “Yoshlar daftari” jamg‘armasi mablag‘lari hisobidan ushbu Nizomga 12-ilovada keltirilgan sxemaga muvofiq ijaraga beruvchi tashkilotga qoplab beriladi.
Bunda nodavlat ta’lim tashkilotida o‘qiyotgan jami fuqarolarning eng kamida beshdan bir qismi “Yoshlar daftari”ga kiritilgan yoshlar bo‘lsa, o‘quv markaziga ushbu imkoniyatdan foydalanishga yo‘l qo‘yiladi.
Mazkur paragrafda nazarda tutilgan xarajatlarni qoplash uchun Yoshlar ishlari agentligining Yoshlarga oid davlat siyosatini qo‘llab-quvvatlash jamg‘armasi hisobidan ham qonunchilik hujjatlarida belgilangan tartibda subsidiya ajratilishi mumkin.
51. Noturar joyning ijara xarajatlarini qoplash uchun nodavlat ta’lim tashkiloti nomidan ish yuritish vakolatiga ega shaxs — ariza beruvchi Vasiylik kengashiga quyidagi hujjatlarni taqdim etadi:
tadbirkorlik subyekti guvohnomasi nusxasi;
ijara shartnomasining soliq organlarida hisobga qo‘yilganligi haqidagi bildirishnoma;
ijara shartnomasi nusxasi. Bunda, ijara shartnomasida ijaraga beruvchining nomi, STIR, ijaraning bir oylik to‘lovi miqdori ko‘rsatilishi lozim;
nodavlat ta’lim tashkilotida ta’lim olayotgan o‘quvchilarning umumiy soni va “Yoshlar daftari”ga kiritilgan yoshlar soni to‘g‘risida ma’lumot.
Taqdim etilgan hujjatlardagi ma’lumotlarning to‘g‘riligi va haqqoniyligi uchun ariza beruvchi javobgar hisoblanadi.
Ushbu bandda nazarda tutilgan hujjatlar taqdim etilgandan so‘ng Vasiylik kengashi uch ish kuni ichida murojaatni ilova qilingan hujjatlar bilan birga ariza beruvchi faoliyat yuritib kelayotgan mahalladagi yoshlar yetakchisiga ko‘rib chiqish uchun yuboradi.
Mahalladagi yoshlar yetakchisi besh ish kuni ichida ijara xarajatlarini qoplash haqidagi tavsiyanomani yoki rad etish to‘g‘risidagi xabarnomani Vasiylik kengashiga yuboradi. Bunda ijara xarajatlarini qoplashni rad etish haqida xabarnoma yuborilganda rad etish sabablari asoslanishi talab etiladi.
Agar mahalladagi yoshlar yetakchisi murojaatni unga kelib tushgan paytdan boshlab besh ish kuni ichida ko‘rib chiqmasa yoki ijara xarajatlarini qoplashni asossiz rad etish haqida xabarnoma bersa, ariza beruvchining murojaati ushbu paragraf talablariga muvofiq bo‘lganda Vasiylik kengashi uning murojaatini qanoatlantirish huquqiga ega bo‘ladi.
52. Murojaatni o‘rganish natijalari bo‘yicha Vasiylik kengashi tomonidan ijara xarajatlarini qoplash haqida qaror qabul qilingandan so‘ng ariza beruvchi bino va inshootdan foydalanayotganligi to‘g‘risida ijaraga beruvchi bilan har oy yakuni bo‘yicha tuziladigan va keyingi oyning 5-kunigacha taqdim etiladigan hisob-fakturaga va dalolatnomaga asosan Vasiylik kengashi bino va inshootning ijara haqi uchun to‘lovni uch ish kuni ichida ijaraga beruvchining hisob raqamiga o‘tkazadi.
53. Mahalladagi yoshlar yetakchisi ijaraga olingan bino va inshootning ijaraga oluvchi tomonidan haqiqatda foydalanilayotganligini har oy mobaynida kamida bir marta monitoring asosida o‘rganadi.
O‘rganish jarayonida ijaraga oluvchi tomonidan ijaraga olingan bino va inshootdan foydalanilmayotganligi aniqlangan taqdirda, yoshlar yetakchisining taqdimnomasiga asosan ijara to‘lovi uchun subsidiya berish to‘xtatiladi.
12-§. “Yoshlar daftari”ga kiritilgan bemor yoshlarga davolanish xarajatlari uchun subsidiya ajratish tartibi
54. “Yoshlar daftari”ga kiritilgan bemor yoshlarga mamlakatda yoki xorijiy davlatlarda davolanish bilan bog‘liq xarajatlarni qoplash uchun yoshlar yetakchisining ijobiy tavsiyasi asosida BHMning 50 baravaridan oshmagan miqdorda “Yoshlar daftari” jamg‘armasi mablag‘lari hisobidan ushbu Nizomga 13-ilovada keltirilgan sxemaga muvofiq subsidiya ajratiladi.
55. Ariza beruvchi subsidiya ajratishni so‘rab murojaat qilganda mahalladagi yoshlar yetakchisi uch ish kuni ichida hududiy birlamchi tibbiy-sanitariya muassasasidan shifokor jalb qilishga ko‘maklashadi va ariza beruvchining sog‘lig‘i holati baholanadi.
O‘rganish natijasida ariza beruvchiga tibbiy yordam ko‘rsatish zarurati aniqlanganda, ariza beruvchining sog‘lig‘i holatiga qarab belgilangan tartibda davolash uchun tegishli birlamchi, viloyat yoki respublika darajasidagi tibbiyot muassasasiga yo‘naltiriladi.
56. O‘zbekiston Respublikasining Davlat budjeti mablag‘lari hisobidan tibbiy yordam ko‘rsatiladigan imtiyozli toifaga kiradigan (ariza beruvchining ushbu toifaga kirishi yoki kirmasligi tibbiyot muassasasi xulosasiga ko‘ra aniqlanadi), viloyat yoki respublika darajasida davolanishi lozim deb topilgan “Yoshlar daftari”ga kiritilgan yoshlar davolanish uchun belgilangan tartibda elektron navbatga qo‘yilishi ta’minlanadi.
Ushbu toifaga kirmaydigan, birlamchi tibbiy-sanitariya muassasasi tomonidan viloyat, respublika darajasida yoki xorijiy davlatda davolanishi lozim deb topilgan “Yoshlar daftari”ga kiritilgan yoshlarning davolanishi yoki jarrohlik amaliyotidan o‘tishi bilan bog‘liq xarajatlar uchun mahalladagi yoshlar yetakchisining tavsiyasiga asosan “Yoshlar daftari” jamg‘armasi mablag‘lari hisobidan subsidiya ajratiladi.
57. Ariza beruvchi shifokor ko‘rigidan o‘tgandan so‘ng mahalladagi yoshlar yetakchisi uch ish kuni ichida subsidiya ajratish haqidagi tavsiyanomani yoki rad etish haqidagi xabarnomani Vasiylik kengashiga yuboradi. Bunda subsidiya ajratishni rad etish haqida xabarnoma yuborilganda rad etish sabablari asoslanishi talab etiladi.
Agar mahalladagi yoshlar yetakchisi murojaat unga tushgan paytdan boshlab uch ish kuni ichida ariza beruvchining sog‘lig‘ini baholash uchun shifokor jalb qilishga ko‘maklashmasa yoki subsidiya ajratishni asossiz rad etish haqida xabarnoma bersa, ariza beruvchining murojaati ushbu paragraf talablariga muvofiq bo‘lganda Vasiylik kengashi uning murojaatini qanoatlantirish huquqiga ega bo‘ladi.
58. Nogironlik belgilari aniq namoyon bo‘lgan yoshlar belgilangan tartibda ko‘rikdan o‘tish uchun Tibbiy-mehnat ekspert komissiyalariga yuboriladi.
13-§. “Yoshlar daftari”ga kiritilgan psixologik maslahatga muhtoj yoshlarga pullik psixologik xizmat ko‘rsatilishi bilan bog‘liq xarajatlarni qoplash tartibi
59. Psixologik maslahatga muhtoj yoshlarga ixtisoslashgan nodavlat notijorat tashkilotlar hamda nodavlat ta’lim tashkilotlari tomonidan pullik psixologik xizmat ko‘rsatilishi bilan bog‘liq xarajatlarni qoplash uchun mahalladagi yoshlar yetakchisining ijobiy tavsiyasi asosida BHMning 4 baravaridan oshmagan miqdorda “Yoshlar daftari” jamg‘armasi mablag‘lari hisobidan ushbu Nizomga 14-ilovada keltirilgan sxemaga muvofiq subsidiya ajratiladi.
Psixologik maslahatga muhtoj yoshlarga Yoshlarga ijtimoiy-psixologik xizmat ko‘rsatish respublika markazi, Ayollarni reabilitatsiya qilish va moslashtirish bo‘yicha respublika, hududiy va tumanlararo namunali markazlari, Odam savdosi jabrdiydalariga yordam berish bo‘yicha respublika reabilitatsiya markazi, Respublika ijtimoiy moslashuv markazi, ta’lim muassasalari va xususiy tashkilotlarning malakali psixologlari tomonidan psixologik maslahatlar beriladi.
60. Ariza beruvchi pullik psixologik xizmat ko‘rsatilishi bilan bog‘liq xarajatlarni qoplashni so‘rab mahalladagi yoshlar yetakchisiga ariza beradi.
Yoshlar yetakchisi uch ish kuni ichida ariza beruvchining ijtimoiy toifasi va holatini o‘rganib, Vasiylik kengashiga quyidagi hujjatlar bilan tavsiyanoma taqdim etadi:
psixolog tomonidan berilgan ariza beruvchining psixologik yordamga muhtojligi to‘g‘risidagi xulosa;
psixologik yordam ko‘rsatish xizmatini ko‘rsatuvchi tashkilot va ariza beruvchi o‘rtasida tuzilgan shartnoma nusxasi. Shartnomada tashkilotning nomi, STIR, ko‘rsatiladigan xizmat summasi ko‘rsatilgan bo‘lishi lozim.
Taqdim etilgan hujjatlardagi ma’lumotlarning to‘g‘riligi va haqqoniyligi uchun ariza beruvchi javobgar hisoblanadi.
61. Murojaatni o‘rganish natijalari bo‘yicha uch ish kuni ichida Vasiylik kengashi subsidiya ajratish haqida qaror qabul qiladi.
Mazkur qaror asosida tuman (shahar) hokimliklari tomonidan uch ish kuni ichida psixologik xizmat ko‘rsatish bilan bog‘liq xarajatlar psixologik yordam ko‘rsatish xizmatini ko‘rsatuvchi tashkilotning bank hisob raqamiga o‘tkaziladi.
14-§. “Yoshlar daftari”ga kiritilgan yoshlarning safarbarlik chaqiruvi rezervidagi xizmatni o‘tash badalini to‘liq miqdorda qoplash uchun subsidiya ajratish tartibi
62. Yoshlarning safarbarlik chaqiruvi rezervidagi xizmatni o‘tash badalini to‘liq qoplash uchun mahalladagi yoshlar yetakchisining tavsiyasi asosida “Yoshlar daftari” jamg‘armasi mablag‘lari hisobidan ushbu Nizomga 15-ilovada keltirilgan sxemaga muvofiq subsidiya ajratiladi.
63. Ariza beruvchi subsidiya ajratishni so‘rab o‘zi va tuman (shahar) mudofaa ishlari bo‘limi o‘rtasida tuzilgan “Safarbarlik chaqiruvi rezervi mablag‘lari” maxsus hisob raqamiga badal o‘tkazish tartibi to‘g‘risida shartnoma nusxasini taqdim etadi.
Shartnoma nusxasi taqdim etilgandan so‘ng Vasiylik kengashi uch ish kuni ichida murojaatni unga ilova qilingan hujjatlar bilan birga ariza beruvchi yashab kelayotgan mahalladagi yoshlar yetakchisiga yuboradi.
Mahalladagi yoshlar yetakchisi besh ish kuni ichida subsidiya ajratish haqidagi tavsiyanomani yoki rad etish to‘g‘risidagi xabarnomani Vasiylik kengashiga yuboradi. Bunda subsidiya ajratishni rad etish haqida xabarnoma yuborilganda rad etish sabablari asoslanishi talab etiladi.
Agar mahalladagi yoshlar yetakchisi murojaatni unga tushgan paytdan boshlab besh ish kuni ichida ko‘rib chiqmasa yoki subsidiya ajratishni asossiz rad etish haqida xabarnoma bersa, ariza beruvchining murojaati ushbu paragraf talablariga muvofiq bo‘lganda Vasiylik kengashi uning murojaatini qanoatlantirish huquqiga ega bo‘ladi.
64. Murojaatni o‘rganish natijalari bo‘yicha uch ish kuni ichida Vasiylik kengashining subsidiya ajratish haqidagi qarori qabul qilinadi.
Qaror asosida tuman (shahar) hokimliklari uch ish kuni ichida tuman (shahar) mudofaa ishlari bo‘limining Xalq bankidagi tegishli tuman (shahar) filialida 29896 “Boshqa majburiyatlar” tranzit hisob raqamiga safarbarlik chaqiruvi rezervi xizmatchisining familiyasi, ismi, otasining ismi va to‘lov maqsadini ko‘rsatgan holda subsidiyani o‘tkazib beradi.
15-§. Yoshlarga yangi turmush qurayotganida o‘z xonadonida qo‘shimcha uy-joy qurish uchun garovsiz kredit ajratish uchun kafillik berish tartibi
65. “Yoshlar daftari”ga kiritilgan, nikohi qayd etilganiga 3 yildan oshmagan yoshlarga yakka tartibdagi o‘z xonadonida qo‘shimcha uy-joy qurish uchun 33 mln so‘mgacha garovsiz kredit ajratishda “Yoshlar daftari” jamg‘armasining kafilligi ushbu Nizomga 16-ilovada keltirilgan sxemaga muvofiq beriladi.
66. Ariza beruvchi kafillik ajratishni so‘rab tijorat bankining Vasiylik kengashi nomiga yuborilgan ariza beruvchi tomonidan qo‘shimcha uy-joy qurish uchun garovsiz kredit ajratish uchun kafillik berish haqidagi xatini taqdim etadi.
Vasiylik kengashi uch ish kuni ichida murojaatni unga ilova qilingan hujjatlar bilan birga ariza beruvchi yashab kelayotgan mahalladagi yoshlar yetakchisiga yuboradi.
Mahalladagi yoshlar yetakchisi besh ish kuni ichida kafillik berish yoki rad etish haqida xabarnomani Vasiylik kengashiga yuboradi. Bunda kafillik berishni rad etish haqida xabarnoma yuborilganda rad etish sabablari asoslanishi talab etiladi.
Agar mahalladagi yoshlar yetakchisi murojaatni unga tushgan paytdan boshlab besh ish kuni ichida ko‘rib chiqmasa yoki kafillik berishni asossiz rad etish haqida xabarnoma bersa, Vasiylik kengashi ariza beruvchining ijtimoiy himoyaga muhtojligini hamda uning murojaati ushbu paragraf talablariga muvofiqligini o‘rgangan holda uning murojaatini qanoatlantirish huquqiga ega bo‘ladi.
67. Murojaatni o‘rganish natijalariga ko‘ra, Vasiylik kengashi qaroriga asosan uch ish kuni ichida ariza beruvchiga kafillik berilishi mumkin.
16-§. “Yoshlar daftari”ga kiritilgan ijtimoiy himoyaga muhtoj yosh oilalarga turar joy ijarasi uchun subsidiya ajratish tartibi
68. Ijtimoiy himoyaga muhtoj yosh oilalarga 12 oygacha turar joy uchun ijara kompensatsiyasi har oyda BHMning 3 baravaridan oshmagan miqdorda “Yoshlar daftari” jamg‘armasi mablag‘lari hisobidan ushbu Nizomga 17-ilovada keltirilgan sxemaga muvofiq subsidiya ajratiladi.
Bunda er-xotinning har ikkisi o‘ttiz yoshdan oshmagan (o‘ttiz bir yoshga to‘lmagan) bo‘lishi, mulk huquqi asosida turar joyi bo‘lmagan, ilgari maqsadli dasturlar doirasida imtiyozli ipoteka kreditlari orqali kvartira yoki yakka tartibdagi uy-joylar bilan ta’minlanmagan, ipoteka kreditlari bo‘yicha subsidiyalar yoki uy-joylar ta’minoti bilan bog‘liq boshqa imtiyozlardan foydalanmagan hamda har ikkisi yoki biri “Yoshlar daftari”ga kiritilgan bo‘lishi talab etiladi.
69. Ariza beruvchi subsidiya ajratishni so‘rab Vasiylik kengashiga quyidagi hujjatlarni taqdim etadi:
turar joy ijara shartnomasi nusxasi. Bunda ijara shartnomasida ijaraga beruvchining ismi va familiyasi, JShShIR, bank plastik kartasining rekvizitlari, ijara muddati, ijaraning bir oylik to‘lovi miqdori ko‘rsatilishi lozim;
ijara shartnomasining soliq organlarida hisobga qo‘yilganligi haqidagi bildirishnoma.
Taqdim etilgan hujjatlardagi ma’lumotlarning to‘g‘riligi va haqqoniyligi uchun ariza beruvchi javobgar hisoblanadi.
Hujjatlar taqdim etilgandan so‘ng Vasiylik kengashi uch ish kuni ichida murojaatni ilova qilingan hujjatlar bilan birga ariza beruvchi yashab kelayotgan mahalladagi yoshlar yetakchisiga yuboradi.
Mahalladagi yoshlar yetakchisi besh ish kuni ichida subsidiya ajratish haqidagi tavsiyanomani yoki rad etish to‘g‘risidagi xabarnomani Vasiylik kengashiga yuboradi. Bunda, subsidiya ajratishni rad etish haqida xabarnoma yuborilganda rad etish sabablari asoslanishi talab etiladi.
Agar mahalladagi yoshlar yetakchisi murojaatni unga tushgan paytdan boshlab besh ish kuni ichida ko‘rib chiqmasa yoki subsidiya ajratishni asossiz rad etish haqida xabarnoma bersa, Vasiylik kengashi ariza beruvchining ijtimoiy himoyaga muhtojligini hamda uning murojaati ushbu paragraf talablariga muvofiqligini o‘rgangan holda uning murojaatini qanoatlantirish huquqiga ega bo‘ladi.
70. Murojaatni o‘rganish natijalari bo‘yicha Vasiylik kengashi tomonidan ijara xarajatlarini qoplash uchun subsidiya ajratish haqida qaror qabul qilinganda Vasiylik kengashi har oyning 5-kunigacha ijara xarajatlari uchun subsidiyaning oylik to‘lovlarini ijaraga beruvchining bank plastik kartasiga o‘tkazadi.
71. Mahalladagi yoshlar yetakchisi ijaraga oluvchi tomonidan haqiqatda ijaraga olingan turar joyda yashayotganini har oy mobaynida kamida bir marta monitoring asosida o‘rganadi.
O‘rganish jarayonida ijaraga oluvchi ijaraga olingan turar joyda yashamayotganligi aniqlangan taqdirda, yoshlar yetakchisining taqdimnomasiga asosan ijara to‘lovi uchun subsidiya berish to‘xtatiladi.
17-§. Yoshlarning intellektual salohiyatini yuksaltirish, ularning bo‘sh vaqtini mazmunli tashkil etish va huquqiy savodxonligini oshirish, shuningdek, besh muhim tashabbus doirasidagi tadbirlarni moliyalashtirish
72. Kalendar rejada belgilangan loyiha, tanlov va tadbirlarni mahalla, sektor, tuman (shahar) va hudud darajasida tashkil etish va o‘tkazish bilan bog‘liq xarajatlar “Yoshlar daftari” jamg‘armasi mablag‘lari hisobidan ushbu Nizomga 18-ilovada keltirilgan sxemaga muvofiq moliyalashtiriladi.
har bir mahalla darajasidagi tadbirlarga bir kalendar oy uchun — BHMning 10 baravarigacha mablag‘ ajratiladi. Kalendar rejaga kiritilmagan tadbirlar “Yoshlar daftari” jamg‘armasi mablag‘laridan moliyalashtirilishiga yo‘l qo‘yilmaydi.
Kalendar rejaga kiritilgan loyiha, tanlov va tadbirlarni sektor va tuman (shahar) bosqichlarini moliyalashtirish Yoshlar ishlari agentligining tuman (shahar) bo‘limlari tomonidan asosli hisob-kitob qilingan holda Vasiylik kengashiga yuboriladi. Vasiylik kengashi murojaatga asosan qaror qabul qiladi va tadbirlarni moliyalashtirish choralarini ko‘radi.
Hududda o‘tkaziladigan respublika va hudud darajasidagi tadbirlar hududiy “Yoshlar daftari” jamg‘armasi mablag‘lari hisobidan moliyalashtiriladi.
73. Mahalla darajasidagi tadbirlarni tashkil etish uchun mahalladagi yoshlar yetakchisi Kalendar rejadan kelib chiqib, Yoshlar ishlari agentligining tuman (shahar) bo‘limlariga choraklik loyiha, tanlov va tadbirlar soni va turi xususidagi ma’lumotlarni taqdim etadi.
Yoshlar ishlari agentligining tuman (shahar) bo‘limlari besh ish kuni ichida mahallalar bo‘yicha choraklik loyiha, tanlov va tadbirlar soni va turi to‘g‘risidagi ma’lumotlarni kalendar rejaga muvofiqligini tekshiradi va ajratiladigan tovar moddiy boyliklar turi va soni to‘g‘risidagi ma’lumotlarni tuman (shahar) “Yoshlar daftari” jamg‘armasi Vasiylik kengashiga yuboradi.
74. Tuman (shahar) “Yoshlar daftari” jamg‘armasi Vasiylik kengashi mahallalar bo‘yicha rejadagi tovar moddiy boyliklarni xarid qilish to‘g‘risida qaror qabul qiladi.
Vasiylik kengashi qarori asosida tovar moddiy boyliklar “Yoshlar daftari” jamg‘armasi mablag‘lari hisobidan qonunchilikda belgilangan tartibda xarid qilinadi.
75. Vasiylik kengashi tovar moddiy boyliklar xarid qilingandan so‘ng uch ish kuni ichida Yoshlar ishlari agentligining tuman (shahar) bo‘limlariga yetkazilishini ta’minlaydi.
Yoshlar ishlari agentligining tuman (shahar) bo‘limlari ikki ish kuni ichida tovar moddiy boyliklarni mahallalar bo‘yicha taqsimlab, mahalladagi yoshlar yetakchilariga tarqatadi.
Mahalladagi yoshlar yetakchisi tovar moddiy boyliklarni yoshlarga tarqatish bo‘yicha, topshirish, qabul qilish dalolatnomasini rasmiylashtiradi va qonunchilikda belgilangan tartibda Yoshlar ishlari agentligining tuman (shahar) bo‘limlariga hisobot topshiradi.
76. Kalendar rejada belgilangan loyiha, tanlov va tadbirlarni sektor, tuman (shahar) bosqichlarini o‘tkazish uchun Yoshlar ishlari agentligining tuman (shahar) bo‘limlari Vasiylik kengashiga choraklik tadbirlar rejasini taqdim etadi va xalq deputatlari tuman (shahar) Kengashiga ko‘rib chiqish uchun kiritadi.
Tadbirlar rejasi xalq deputatlari tuman (shahar) Kengashi tomonidan tasdiqlangandan so‘ng tadbirlarni o‘tkazish uchun Vasiylik kengashining qaroriga muvofiq “Yoshlar daftari” jamg‘armasidan mablag‘lar ajratiladi va qonunchilikda belgilangan tartibda tadbirlarga ajratiladigan tovar moddiy boyliklarni xarid qiladi.
Vasiylik kengashi tovar moddiy boyliklar xarid qilingandan so‘ng uch ish kuni ichida Yoshlar ishlari agentligining tuman (shahar) bo‘limlariga yetkazilishini ta’minlaydi.
Yoshlar ishlari agentligining tuman (shahar) bo‘limlari tovar moddiy boyliklarni topshirish, qabul qilish dalolatnomasini rasmiylashtiradi va qonunchilikda belgilangan tartibda Vasiylik kengashiga hisobot topshiradi.
Vasiylik kengashi har chorak yakuni bo‘yicha o‘tkazilgan tadbirlar bo‘yicha xalq deputatlari tuman (shahar) Kengashiga hisobot taqdim etadi.
77. Kalendar rejaga kiritilmagan tadbirlarni tashkil etishga mahalladagi yoshlar yetakchisini jalb etishga yo‘l qo‘yilmaydi.
18-§. “Yoshlar daftari”ga kiritilgan yoshlarning ish bilan bandligini ta’minlash
78. “Yoshlar daftari”ga kiritilgan ishsiz yoshlarning bandligiga quyidagi yo‘nalishlarda ko‘maklashiladi:
sektorlar rahbarlari tuman (shahar) hokimlarining iqtisodiyot va tadbirkorlik masalalari bo‘yicha birinchi o‘rinbosarlari, mahallabay ishlash va tadbirkorlikni rivojlantirish markazlari, aholi bandligiga ko‘maklashish markazlari, Savdo-sanoat palatasining tuman (shahar) tadbirkorlikka ko‘maklashish markazlari tomonidan “Ishga marhamat” monomarkazlari, davlat va nodavlat kasb-hunarga o‘qitish markazlari, mahalla aholisini kasb-hunarga o‘qitish maskanlarida kasb-hunarga va tadbirkorlikka o‘qitishni tashkil etish, tadbirkorlikka jalb etish, o‘zini o‘zi mustaqil ravishda band qilishni rivojlantirishga doir faoliyatni tashkil etish orqali bandlikka ko‘maklashish;
sektorlar rahbarlari tuman (shahar) hokimlarining investitsiyalar va tashqi savdo masalalari bo‘yicha o‘rinbosarlari, tuman (shahar) investitsiya bo‘limlari, mahallabay ishlash va tadbirkorlikni rivojlantirish markazlari, Aholi bandligiga ko‘maklashish markazlari, tijorat banklari hamkorligida tarmoq va hududiy investitsiya dasturlariga kiritilgan loyihalarda yoshlar uchun yaratilayotgan yangi ish o‘rinlariga ishga joylashtirish;
sektorlar rahbarlari tuman (shahar) mahallabay ishlash va tadbirkorlikni rivojlantirish markazlari hamda aholi bandligiga ko‘maklashish markazlari bilan birgalikda mavjud vakansiya va zaxira (kvota) ish o‘rinlariga ishga joylashtirish hamda haq to‘lanadigan jamoat ishlariga jalb qilish;
sektorlar rahbarlari tuman (shahar) hokimlarining qishloq va suv xo‘jaligi masalalari bo‘yicha o‘rinbosarlari, tuman (shahar) mahallabay ishlash va tadbirkorlikni rivojlantirish markazlari bilan birgalikda fermer va dehqon ho‘jaliklari, qishloq xo‘jaligi kooperativlariga jalb qilish, shuningdek, dehqonchilik bilan shug‘ullanish uchun yangi o‘zlashtirilgan, lalmi, foydalanilmayotgan yer maydonlarini 0,10 gektardan 1 gektargacha belgilangan tartibda ochiq elektron tanlov orqali 10 yilga ijaraga yer berish;
sektorlar rahbarlari tuman (shahar) mahallabay ishlash va tadbirkorlikni rivojlantirish markazlari, tuman (shahar) hokimlarining sanoatni rivojlantirish, kapital qurilish, kommunikatsiyalar va kommunal xo‘jalik masalalari bo‘yicha o‘rinbosarlari, qurilish bo‘limlari bilan birgalikda hududdagi qurilish ishlariga jalb qilish;
tuman (shahar) mahallabay ishlash va tadbirkorlikni rivojlantirish markazlari, Yoshlar ishlari agentligi hamda Aholi bandligiga ko‘maklashish markazlari bilan birgalikda yoshlar bandligiga ko‘maklashish, tadbirkorlikni rivojlantirish hamda yoshlarni ishga qabul qilgan ish beruvchilarni rag‘batlantirish maqsadida subsidiyalar ajratishga ko‘maklashish.
Ushbu bandda ko‘rsatilgan yo‘nalishlar qonunchilik hujjatlarida belgilangan tartibda amalga oshiriladi.
19-§. “Yoshlar daftari”ga kiritilgan yoshlarni tadbirkorlikka jalb qilish
79. “Yoshlar daftari”ga kiritilgan yoshlarga tadbirkorlik faoliyatini yo‘lga qo‘yishda ko‘maklashish quyidagi yo‘nalishlarda amalga oshiriladi:
a) Savdo-sanoat palatasi va “Yoshlar — kelajagimiz” jamg‘armasi tomonidan:
48 soatlik (haftalik) o‘quv dasturi asosida o‘quv kurslarida tadbirkorlikka bepul o‘qitiladi;
o‘quv kurslarini muvaffaqiyatli bitirib, sertifikatga ega bitiruvchilarning o‘zini o‘zi daromadli mehnat bilan band qilish yoki ularning doimiy mehnat bilan bandligini ta’minlashga (ish o‘rinlari yaratishga) qaratilgan loyihalarini tuzish va amalga oshirishga ko‘maklashadi;
b) “Mikrokreditbank” ATB, “Agrobank” ATB va AT “Xalq banki”ning tuman (shahar) filiallari orqali tadbirkorlikni yo‘lga qo‘yish va rivojlantirish uchun O‘zbekiston Respublikasi Davlat budjeti mablag‘lari hisobidan kreditlar ajratiladi.
“Mikrokreditbank” ATB “Yoshlar daftari”ga kiritilgan yoshlarni tadbirkorlikka jalb qilish, ularga kredit olishda ko‘maklashish, bu masalada respublikada ajratilgan kreditlarning statistik hisobotini yuritish va kredit ajratilgandan so‘ng ularning tadbirkorligini rivojlantirish uchun doimiy qo‘llab-quvvatlash borasidagi amaliy ishlarni muvofiqlashtirishga mas’ul hisoblanadi.
80. Kreditlar “Yoshlar daftari”ga kiritilgan va tadbirkorlik bilan shug‘ullanish istagida bo‘lgan yoshlarning tadbirkorligini yo‘lga qo‘yish va rivojlantirishga yo‘naltiriladi.
Bunda:
tadbirkorlik tashabbusiga ega jismoniy shaxslarga, shu jumladan, yoshlarga o‘z biznesini tashkil etish uchun 33 million so‘mgacha bo‘lgan miqdordagi kreditlar garovsiz;
kichik tadbirkorlik subyektlariga uchinchi shaxs kafilligi, sug‘urta polislari, kredit hisobiga sotib olinayotgan mol-mulk garovi, Tadbirkorlik faoliyatini qo‘llab-quvvatlash davlat jamg‘armasining kafilligi va qonun hujjatlarida nazarda tutilgan boshqa ta’minot turlari asosida 225 million so‘mgacha miqdorda kreditlar ajratiladi.
Kreditlarni ilgari olingan kreditlar yoki har qanday boshqa qarzlarni qaytarishga, shaxsiy ehtiyoj uchun avtotransport sotib olishga, ma’muriy xarajatlarni to‘lashga, jumladan, avtotransport vositasining ta’minoti, mebel, aloqa xizmatlari to‘lovi va uyali telefon sotib olishga hamda qonunchilik hujjatlari va Markaziy bankning qoidalariga ko‘ra taqiqlangan faoliyatlarga ajratishga yo‘l qo‘yilmaydi.
Kreditlar hokim yordamchilarining tavsiyalari asosida 14 foizlik stavkada:
oilaviy tadbirkorlik, daromad topishga qaratilgan muayyan mehnat faoliyati bilan shug‘ullanish istagini bildirgan yoshlarga — 3 oydan 6 oygacha bo‘lgan imtiyozli davr bilan 3 yilgacha muddatga;
chorvachilik (chetdan keltirilgan naslli qo‘y va echki), baliqchilik va parrandachilik (tuxum yo‘nalishi) uchun — 1 yilgacha bo‘lgan imtiyozli davr bilan 3 yilgacha muddatga;
bog‘dorchilik, uzumchilik va limonchilikni tashkil etish, issiqxona, qishloq xo‘jaligi texnikasi va asbob-uskunalarni xarid qilish uchun — 3 yilgacha bo‘lgan imtiyozli davr bilan 7 yilgacha muddatga ajratiladi.
81. Kreditlar qarz oluvchining ssuda hisob raqamidan kredit shartnomasida belgilangan maqsadlar uchun tegishli tashkilotlarning bankdagi hisob raqamiga pul o‘tkazish yo‘li bilan ajratiladi.
“Yoshlar daftari”ga kiritilgan va o‘zini o‘zi band qiladigan yoshlarga ayrim turdagi faoliyatni amalga oshirish (kasanachilik, hunarmandchilik, issiqxona qurish va shu kabilar uchun zarur xomashyo, ehtiyot qism hamda qurilish mollarini sotib olish) maqsadida 5 million so‘mgacha miqdorda kredit mablag‘lari naqd pulda berilishi mumkin.
Kreditlar “Mikrokreditbank” ATB, “Agrobank” ATB va AT “Xalq banki”ning tuman (shahar) filiallari tomonidan “Yoshlar daftari”da hisobda turgan yoshlarning qat’iy navbatma-navbat murojaat qilishi asosida Oilaviy tadbirkorlikni rivojlantirish dasturlarining yagona platformasi orqali ajratiladi.
82. “Yoshlar daftari”ga kiritilgan, biroq kredit olishni rad qilgan yoshlarning doimiy bandligini ta’minlash maqsadida tadbirkorlik subyektlarining “Yoshlar daftari”ga kiritilgan yoshlarni ish bilan bandligini ta’minlashga qaratilgan loyihalariga Oilaviy tadbirkorlikni rivojlantirish davlat dasturi doirasidagi resurslar hisobidan yillik 14 foizlik stavkada imtiyozli kreditlar ajratilishi mumkin.
Bunda kichik tadbirkorlik subyektlari tomonidan “Yoshlar daftari”ga kiritilgan yoshlarni doimiy ish bilan ta’minlash sharti bilan samaradorligi yuqori va barqaror ish o‘rinlari yaratishga qaratilgan loyihalariga Oilaviy tadbirkorlikni rivojlantirish davlat dasturi doirasidagi resurslar hisobidan 225 million so‘mdan ortiq, biroq 1 milliard so‘mdan ko‘p bo‘lmagan miqdorda belgilangan tartib asosida kredit ajratilishi mumkin.
Kredit summasining aniq miqdori tadbirkor tomonidan ish bilan ta’minlanadigan har bir yosh uchun 33 million so‘mgacha miqdorda mutanosib ravishda belgilanadi.
83. Savdo-sanoat palatasi, “Yoshlar — kelajagimiz” jamg‘armasining hududiy bo‘linmalari joylarda tadbirkorlik faoliyatini yo‘lga qo‘yish istagini bildirgan yoshlarning tadbirkorlik ko‘nikmalarini oshirish va biznes loyihalarini tuzishga ko‘maklashadi.
20-§. “Yoshlar daftari”ga kiritilgan yoshlarning xorijda xavfsiz, tartibli va qonuniy mehnat migratsiyasini tashkil etish
84. Yoshlarning xorijda xavfsiz, tartibli va qonuniy mehnat migratsiyasini tashkil etish O‘zbekiston Respublikasi Prezidentining “Xavfsiz, tartibli va qonuniy mehnat migratsiyasi tizimini joriy qilish chora-tadbirlari to‘g‘risida” 2020-yil 15-sentabrdagi PQ-4829-son qarori asosida Bandlik va mehnat munosabatlari vazirligi tomonidan quyidagi tartibda amalga oshiriladi:
uyushtirilgan mehnat migratsiyasi yo‘li bilan xorijga chiqib ketayotgan yoshlar ishga yuborilishidan oldin davlat va nodavlat ta’lim tashkilotlarida, xususan hududlardagi “Ishga marhamat” monomarkazlari, kasb-hunarga o‘qitish markazlari, qisqa muddatli kasb-hunarga o‘qitish kurslari, mahalla aholisini kasb-hunarga o‘qitish maskanlarida kasb-hunarga o‘qitiladi (xorijiy ish beruvchining malaka talablariga javob beradigan shaxslar bundan mustasno);
uyushtirilgan mehnat migratsiyasi yo‘li bilan chet elda mehnat faoliyatini amalga oshirayotgan yoshlarning haq-huquqlarini ta’minlashga va ko‘maklashishga qaratilgan chora-tadbirlar amalga oshiriladi;
Mehnat migratsiyasidan qaytib kelgan yoshlarni reintegratsiya qilish, shu jumladan ularning bandligini ta’minlash, kasbiy malakasini oshirish va tadbirkorlik tashabbuslarini rag‘batlantirish hamda qonun hujjatlariga muvofiq boshqa choralar-tadbirlar ko‘riladi."""
    for x in range(0, len(text), 4096):
         await call.message.answer(text[x:x + 4096])


@dp.callback_query_handler(bobcallback.filter(number="tort"))
async def tort(call:CallbackQuery):

    await call.answer(cache_time=20)
    text="""4-bob. Yordam turlarini berish tartibi
85. Tegishli ijobiy tavsiya asosida “Yoshlar daftari” jamg‘armasi mablag‘lari hisobidan yoshlarga beriladigan yordamlar bo‘yicha murojaatlar Vasiylik kengashining ishchi organiga elektron platforma orqali yuboriladi.
86. Vasiylik kengashiga kiritilgan murojaatlar Vasiylik kengashi yig‘ilishlarida ko‘rib chiqiladi.
Vasiylik kengashi yig‘ilishlari har oyda kamida ikki marta — oyning 15-kunigacha va oxirgi kunigacha o‘tkaziladi.
87. Vasiylik kengashining ishchi organi ikki kun muddatda Vasiylik kengashi yig‘ilishi kun tartibiga kiritiladigan masalalarni tayyorlaydi, bu haqida Vasiylik kengashi a’zolariga yig‘ilish vaqti va o‘tkaziladigan joyi to‘g‘risida xabar beradi.
Ko‘riladigan masalalar bo‘yicha qarorlar ochiq ovoz berish orqali ko‘pchilik ovoz bilan qabul qilinadi. Vasiylik kengashining har bir a’zosi, shu jumladan, rais ham bitta ovozga ega bo‘ladi.
88. Vasiylik kengashi ishchi organi Vasiylik kengashi yig‘ilishlari bayonnomasini yuritadi va rasmiylashtiradi.
Bunda yig‘ilish bayonnomasi besh kun muddatda Vasiylik kengashi a’zolari bilan kelishilgan holda Vasiylik kengashi raisi tomonidan imzolanadi.
89. Sektorlar rahbarlari tegishli mahallalar bo‘yicha “Yoshlar daftari”ga kiritilgan yoshlarning muammolarini bartaraf etishga qaratilgan “Yoshlar dasturi”ni tasdiqlaydi va ijrosini ta’minlash uchun mas’ul davlat organlari va tashkilotlariga yuboradi.
“Yoshlar dasturi” ijrosi uchun mas’ul etib belgilangan sektorlar rahbarlari, Vasiylik kengashi raisi, mas’ul davlat organlari va tashkilotlar rahbarlari yoshlarning muammolari bartaraf etilganligi bo‘yicha har chorakda kamida bir marotaba xalq deputatlari tuman (shahar) Kengashlariga hisobot beradi."""
    for x in range(0, len(text), 4096):
         await call.message.answer(text[x:x + 4096])

@dp.callback_query_handler(bobcallback.filter(number="besh"))
async def tort(call:CallbackQuery):

    await call.answer(cache_time=20)
    text="""5-bob. “Yoshlar daftari”dan chiqarish tartibi\n90. Yoshlar quyidagi hollarda “Yoshlar daftari”dan chiqariladi:
ushbu Nizomning 3-bobida belgilangan tegishli toifa bo‘yicha belgilangan amaliy yordamlar to‘liq ko‘rsatilganda (bir martalik moddiy yordam ko‘rsatilganligi bundan mustasno);
bandligi ta’minlangan yoki doimiy daromad manbaiga ega bo‘lganda;
to‘liq davlat ta’minotiga olinganda;
o‘z arizasiga ko‘ra;
“Yoshlar daftari”ga noqonuniy kiritilganligi aniqlanganda;
boshqa davlatlarga ishlash yoki doimiy yashash uchun chiqib ketganda;
sudning ozodlikdan mahrum etishni nazarda tutuvchi hukmi qonuniy kuchga kirganda;
vafot etgan taqdirda yoki sud qarori asosida bedarak yo‘qolgan deb topilganda.
“Yoshlar daftari”ga kiritilgan yoshlarning “Yoshlar dasturi”ga kiritilgan masalalari to‘liq hal etilgunga qadar ularni “Yoshlar daftari”dan chiqarishga yo‘l qo‘yilmaydi.
Ish beruvchi tomonidan jismoniy shaxslardan olinadigan daromad solig‘i yoki ijtimoiy soliq to‘lovi hisoblanganda hamda ushbu ma’lumotlar O‘zbekiston Respublikasi Davlat soliq qo‘mitasining markazlashtirilgan axborot bazasida va Yagona milliy mehnat tizimida aks etgan taqdirda, ish bilan bandligi ta’minlangan deb hisoblanadi hamda “Yoshlar daftari”dan chiqarish uchun asos bo‘ladi.
Doimiy va vaqtincha yashash uchun respublikaning boshqa hududiga ko‘chib o‘tganda, doimiy yashash va vaqtincha turar joyi bo‘yicha ro‘yxatga olingan kundan boshlab o‘n besh kundan kechiktirmasdan “Yoshlar daftari”ga tegishli o‘zgartirishlar kiritiladi.
91. Yoshlar yetakchilari mazkur Nizomning 90-bandida ko‘rsatilgan holatlarga asosan yoshlarni “Yoshlar daftari”dan chiqarish bo‘yicha Yoshlar ishlari agentligining tuman (shahar) bo‘limlariga elektron platforma orqali tavsiya beradi.
Yoshlar ishlari agentligining tuman (shahar) bo‘limlari yoshlar yetakchilari tomonidan “Yoshlar daftari”dan chiqarish tavsiya etilayotgan yoshlarni besh ish kuni ichida mazkur Nizomning 90-bandida ko‘rsatilgan holatlar bo‘yicha o‘rganib, haqiqatda chiqarish yoki rad etishni elektron platformada belgilaydi.
“Yoshlar daftari”ga kiritilgan yoshlar Nizomning 90-bandida ko‘rsatilgan holatlardan boshqa sabablar bilan “Yoshlar daftari”dan chiqarilgan taqdirda, amaliy yordam berish uchun “Yoshlar daftari”ga qayta kiritiladi.
92. “Yoshlar daftari”dan chiqarilayotgan yoshlar bir kun ichida bu haqida xabardor qilinadi."""
    for x in range(0, len(text), 4096):
         await call.message.answer(text[x:x + 4096])

@dp.callback_query_handler(bobcallback.filter(number="olti"))
async def tort(call:CallbackQuery):

    await call.answer(cache_time=20)
    text="""6-bob. Yakunlovchi qoidalar\n93. Ushbu Nizomga muvofiq “Yoshlar daftari” jamg‘armasi mablag‘lari hisobidan ko‘rsatiladigan ko‘mak ariza beruvchilarning arizalariga asosan ularning ehtiyoji va xohish-istaklarini o‘rganish natijalariga asosan tegishliligi bo‘yicha yoshlar yetakchisi va hokim yordamchisi tavsiyasiga ko‘ra Vasiylik kengashi qaroriga muvofiq amalga oshiriladi.
Vasiylik kengashi tomonidan ariza va unga ilova qilingan tegishli hujjatlar ko‘rib chiqilib, natijasi bo‘yicha “Yoshlar daftari” jamg‘armasi mablag‘lari hisobidan ko‘mak berish yoki rad etish to‘g‘risida asoslangan qaror qabul qilinadi.
“Yoshlar daftari” jamg‘armasi mablag‘lari hisobidan ko‘mak berish asoslangan holda rad etilgan taqdirda, Vasiylik kengashining tegishli qarori qabul qilingan kundan boshlab uch ish kuni ichida bu haqida ariza beruvchiga xabarnoma yuboriladi.
94. Yoshlarning ehtiyojlari va xohish-istaklarini o‘rganish natijalari bo‘yicha xalq deputatlari tuman (shahar) Kengashlari qaroriga asosan qonunchilik hujjatlariga zid bo‘lmagan boshqa yo‘nalishlar bo‘yicha ham yoshlarga moddiy va ijtimoiy yordam berilishi mumkin.
95. Sektorlar rahbarlari, tuman (shahar) hokimining yoshlar siyosati, ijtimoiy rivojlantirish va ma’naviy-ma’rifiy ishlar bo‘yicha o‘rinbosarlari elektron platformada “Yoshlar daftari”ni yuritish bilan bog‘liq masalalar to‘liq aks ettirib borilishini ta’minlaydi hamda unga ma’lumotlarni kiritish va chiqarish, ularning haqqoniyligi bo‘yicha shaxsan javobgar hisoblanadi.
“Yoshlar daftari”ga kiritilgan yoshlar bo‘yicha amalga oshirilayotgan ishlar to‘g‘risida barcha hisobotlar elektron platformada shakllantiriladi.
96. “Yoshlar daftari”ga kiritilgan yoshlarni qo‘llab-quvvatlash bo‘yicha ishlarni muvofiqlashtirish:
mahalla darajasida — tuman (shahar) sektorlari rahbarlari, tuman (shahar) hokimining yoshlar siyosati, ijtimoiy rivojlantirish va ma’naviy-ma’rifiy ishlar bo‘yicha o‘rinbosarlari, Yoshlar ishlari agentligining tuman (shahar) bo‘limlari boshliqlari;
tuman (shahar) darajasida — viloyat sektorlari rahbarlari, Qoraqalpog‘iston Respublikasi Vazirlar Kengashi Raisi, viloyatlar va Toshkent shahar hokimining yoshlar siyosati, ijtimoiy rivojlantirish va ma’naviy-ma’rifiy ishlar bo‘yicha o‘rinbosarlari, Yoshlar ishlari agentligining hududiy boshqarmalari boshliqlari;
viloyat darajasida — Yoshlar ishlari agentligi, sektorlar, tegishli vazirliklar va idoralar;
respublika darajasida — Mahallalarda yoshlar bilan ishlash masalalarini muvofiqlashtirish bo‘yicha respublika komissiyasi tomonidan amalga oshiriladi.
97. Yoshlar yetakchilari tomonidan “Yoshlar daftari”ga kiritilgan har bir yoshlarning aniqlangan muammolari bartaraf etilganligi haqidagi hisobotlar elektron platformaga kiritib boriladi.
98. Yoshlar ishlari agentligi elektron platformaga ma’lumotlarning kiritilishi yuzasidan monitoring yuritadi.
99. “Yoshlar daftari”ga kiritilgan yoshlarning muammolarini bartaraf etishga qaratilgan “Yoshlar dasturi”ning ijrosi har chorakda kamida bir marta xalq deputatlari tuman (shahar) kengashida muhokama qilinadi.
Kengash sessiyalarida muammolarni hal qilishga mas’ul bo‘lgan sektorlar va tashkilot rahbarlarining hisobotlari eshitib boriladi.
100. Yoshlar ishlari agentligi “Yoshlar daftari”ga yuritilishi bo‘yicha amalga oshirilgan ishlar haqida hududiy bo‘linmalardan olingan ma’lumotlarni tegishli vazirlik, idora va tashkilotlar hamda mahalliy hokimliklar bilan har oy yakuni bilan tahlil qiladi.
Respublika darajasida hal etilishi lozim bo‘lgan muammolarni hududlar bo‘yicha bartaraf etish maqsadida Mahallalarda yoshlar bilan ishlash masalalarini muvofiqlashtirish bo‘yicha respublika komissiyasiga axborot kiritib boriladi.
101. Qoraqalpog‘iston Respublikasi Vazirlar Kengashi, viloyatlar va Toshkent shahar hokimliklari, tegishli vazirliklar va idoralar har oy yakuni bo‘yicha keyingi oyning 5-kuniga qadar “Yoshlar dasturi” ijrosi bo‘yicha ma’lumotlarni Yoshlar ishlari agentligiga taqdim etadi.
102. “Yoshlar dasturi” va “Yoshlar daftari” yuritilishi bo‘yicha mutasaddi bo‘lgan vazirliklar, idoralar va mahalliy hokimliklarning barcha darajadagi rahbarlarining hisobdorligini Mahallalarda yoshlar bilan ishlash masalalarini muvofiqlashtirish bo‘yicha respublika komissiyasi hamda Vazirlar Mahkamasining Rayosat majlisida ko‘rib chiqish uchun har chorak yakunida “Yoshlar daftari” yuritilishi bo‘yicha tahliliy ma’lumotlar Yoshlar ishlari agentligi tomonidan belgilangan tartibda O‘zbekiston Respublikasi Prezidenti Administratsiyasi hamda Vazirlar Mahkamasiga kiritib boriladi.
103. Mahallalarda yoshlar bilan ishlash masalalarini muvofiqlashtirish bo‘yicha respublika komissiyasi kamchilikka yo‘l qo‘ygan mas’ul tashkilotlar rahbarlariga baho beradi, choralar ko‘radi, kamchiliklarni bartaraf etish bo‘yicha tegishli “yo‘l xaritalari” ishlab chiqilishi va ijroga yo‘naltirilishini ta’minlaydi.
"""
    for x in range(0, len(text), 4096):
         await call.message.answer(text[x:x + 4096])

@dp.callback_query_handler(bobcallback.filter(number="uchikki"))
async def tort(call:CallbackQuery):

    await call.answer(cache_time=20)
    text="""3-bob. Hududiy va tuman (shahar) “Yoshlar daftari” jamg‘armalari mablag‘laridan foydalanish
7. Hududiy “Yoshlar daftari” jamg‘armasi mablag‘lari:
tegishli hududning qo‘shimcha manbalari nisbatan kam miqdorda shakllangan tuman (shahar) “Yoshlar daftari” jamg‘armalariga;
Yoshlar ishlari agentligi direktori tomonidan tasdiqlangan kalendar rejada belgilangan mahalla, sektor, tuman (shahar) va hudud darajasidagi loyihalar, yoshlar festivallari, forumlar, tanlovlar va boshqa madaniy-ma’rifiy tadbirlarni moliyalashtirishga;
mahallalarda yoshlarning bo‘sh vaqtini mazmunli tashkil etish uchun qo‘shimcha sharoitlar yaratishga mo‘ljallangan yengil turdagi kichik kutubxonalar va sport obyektlarini barpo etish hamda ularni zamonaviy jihozlashga;
mahallalardagi yoshlar yetakchilari uchun ajratilgan xizmat xonalarini moddiy-texnik jihozlar (mebel, planshet, kompyuter to‘plami, aloqa, internet va boshqalar) bilan ta’minlashga;
qonunchilik hujjatlari bilan belgilangan boshqa xarajatlarni qoplashga yo‘naltiriladi.
8. Tuman (shahar) “Yoshlar daftari” jamg‘armasi mablag‘lari:
“Yoshlar daftari”ga kiritilgan va moddiy ahvoli og‘ir yoshlarga bazaviy hisoblash miqdorining (keyingi o‘rinlarda — BHM) 4 baravarigacha miqdorda bir martalik moddiy yordam ko‘rsatishga;
“Yoshlar daftari”ga kiritilgan yoshlarni tadbirkorlik va kasb-hunarga o‘qitish uchun sarflangan xarajatlarning 75 foizigacha qismini, biroq bir oygacha, bir oydan ikki oygacha, ikki oydan ortiq muddatli o‘quv kurslari uchun tegishlicha BHMning 4, 8, 12 baravaridan ko‘p bo‘lmagan miqdordagi qismini qoplashga;
“Yoshlar daftari”ga kiritilgan yoshlarga ularning davlat va nodavlat ta’lim tashkilotlarida avtomototransport vositalari haydovchilarini tayyorlash o‘quv kursi xarajatlarini qoplash uchun BHMning 4 baravarigacha miqdorda subsidiya ajratishga;
“Yoshlar daftari”ga kiritilgan, dehqonchilik va tomorqa xo‘jaligini yuritish bilan shug‘ullanayotgan yoshlarga urug‘lik va ko‘chatlar sotib olish uchun BHMning 8 baravarigacha miqdorda subsidiya ajratishga;
“Yoshlar daftari”ga kiritilgan yoshlarga tadbirkorlik faoliyati hamda o‘zini o‘zi band qilish maqsadida noturar joyning 12 oygacha ijara xarajatlarini ko‘pi bilan bir yilda 30 foiz, biroq BHMning 25 baravarigacha miqdorda qoplashga;
“Yoshlar daftari”ga kiritilgan yoshlarga tadbirkorlik faoliyatini boshlash va o‘zini o‘zi band qilish uchun zarur bo‘lgan asbob-uskunalar va mehnat qurollarini xarid qilishga BHMning 40 baravarigacha miqdorda subsidiya ajratishga;
mamlakatimizdagi professional va oliy ta’lim muassasalarida ta’lim olayotgan, “Temir daftar”ga kiritilgan oilalar farzandlarining, shuningdek, “Yoshlar daftariga” kiritilgan yoshlarning to‘lov-kontrakt summasining 50 foizigacha, ammo BHMning 50 baravaridan oshmagan miqdorda to‘lab berishga;
yoshlarga zamonaviy kasblarni egallashi, axborot texnologiyalarini o‘rganishi va ularni xorijiy tillarga o‘qitish bo‘yicha olti oygacha muddatli o‘quv kurslar uchun har oyda BHMning 4 baravarigacha miqdorda subsidiya ajratishga;
ijtimoiy himoyaga muhtoj iqtidorli yoshlarning ilm-fan, sport, san’at va madaniyat yo‘nalishlaridagi olti oygacha muddatli o‘quv kurslari uchun har oyda BHMning 1 baravarigacha miqdorda subsidiya ajratishga;
“Temir daftar” va “Ayollar daftari”ga kiritilgan oilalarning farzandlari hamda “Yoshlar daftari”ga kiritilgan ijtimoiy himoyaga muhtoj yoshlarning fuqarolik pasporti (biometrik pasport) olish badalini qoplab berish;
ijtimoiy himoyaga muhtoj iqtidorli yoshlarning ilm-fan, sport, san’at va madaniyat yo‘nalishlaridagi olimpiada, tanlov va musobaqalarning mahalliy bosqichlarida qatnashish xarajatlari uchun BHMning 4 baravarigacha hamda xalqaro bosqichlarida qatnashish xarajatlari uchun BHMning 40 baravarigacha miqdorda subsidiya ajratishga;
“Temir daftar” va “Ayollar daftari”ga kiritilgan oilalarning farzandlari hamda “Yoshlar daftari”ga kiritilgan yosh oilalarning o‘quvchi farzandlari uchun bir kalendar yilida bir marotaba maktab formasi hamda o‘quv qurollari uchun xarajatlarini qoplash;
“Temir daftar” va “Ayollar daftari”ga kiritilgan oilalarning farzandlari hamda “Yoshlar daftari”ga kiritilgan ijtimoiy himoyaga muhtoj yoshlar hamda tengdoshlari orasida namuna ko‘rsatgan faol yoshlarning mamlakatimiz bo‘ylab turizm obyektlariga sayohatlari uchun mehmonxona va yo‘l xarajatlarini qoplab berish;
yoshlarga ta’lim, madaniyat va san’at, sport, axborot texnologiyalar sohasiga va fanlarni o‘qitishga ixtisoslashgan ta’lim tashkilotlarining uch oy muddatgacha noturar joy ijara xarajatlari uchun BHMning 50 baravarigacha miqdorda subsidiya ajratishga;
moddiy ahvoli og‘ir bo‘lgan 30 yoshdan oshmagan bemor fuqarolarga mamlakatda yoki xorijiy davlatlarda davolanish bilan bog‘liq xarajatlarni qoplash uchun BHMning 50 baravaridan oshmagan miqdorda subsidiya ajratishga;
psixologik maslahatga muhtoj yoshlarga ixtisoslashgan nodavlat notijorat tashkilotlari hamda nodavlat ta’lim tashkilotlari tomonidan pulli psixologik xizmat ko‘rsatilishi bilan bog‘liq xarajatlarni qoplashga;
ijtimoiy himoyaga muhtoj yoshlarning safarbarlik chaqiruvi rezervidagi xizmatni o‘tash badalini to‘liq miqdorda qoplash uchun subsidiya ajratishga;
yoshlarga yangi turmush qurayotganda, o‘z xonadonida qo‘shimcha uy-joy qurish uchun 33 million so‘mgacha garovsiz kredit ajratishga kafillik berishga;
ijtimoiy himoyaga muhtoj yosh oilalarga har oyda BHMning 3 baravaridan oshmagan miqdorda 12 oygacha turar joy ijarasi uchun subsidiya ajratishga;
Yoshlar ishlari agentligi direktori tomonidan tasdiqlangan kalendar rejada belgilangan mahalla, sektor va tuman (shahar) darajasidagi loyihalar, yoshlar festivallari, forumlar, tanlovlar va boshqa madaniy-ma’rifiy tadbirlarni moliyalashtirishga;
mahalladagi yoshlar yetakchisining tuman (shahar) Vasiylik kengashiga kiritgan iltimosnomasiga binoan Kengash raisi Yoshlar ishlari agentligining hududiy boshqarmasiga “Yoshlar daftari”ga kiritilgan yoshlarning muammolarini “Yoshlar daftari” jamg‘armasi mablag‘lari hisobidan yetarli darajada hal qilinganligi to‘g‘risida axborot beradi. Mazkur axborot asosida Yoshlar ishlari agentligining hududiy boshqarmasi tavsiyasi bilan tuman (shahar) jamg‘armasidagi mavjud mablag‘lar hisobidan mahallalarda yoshlarning bo‘sh vaqtini mazmunli tashkil etish uchun qo‘shimcha sharoitlar yaratishga mo‘ljallangan yengil turdagi kichik kutubxonalar va sport obyektlarini barpo etish hamda ularni zamonaviy jihozlashga mablag‘ yo‘naltirish;
qonunchilik hujjatlari bilan belgilangan boshqa xarajatlarni qoplashga yo‘naltiriladi.
9. Hududiy va tuman (shahar) “Yoshlar daftari” jamg‘armalarining mablag‘lari ushbu Nizomning 7 va 8-bandlarida nazarda tutilmagan maqsadlarga yo‘naltirilishiga, shuningdek, “Yoshlar daftari”ga kiritilgan yoshlarga aynan bir turdagi subsidiya yoki ijtimoiy yordam (bir martalik moddiy yordam bundan mustasno) boshqa manbalar va jamg‘armalar tomonidan ko‘rsatilganda taqdim etilishiga yo‘l qo‘yilmaydi.
10. O‘zbekiston Respublikasi Yoshlar ishlari agentligining Yoshlarga oid davlat siyosatini qo‘llab-quvvatlash jamg‘armasi hisobidan, zarur hollarda, ushbu Nizomning 7 va 8-bandlarida nazarda tutilgan maqsadlar uchun mablag‘lar ajratilishi mumkin.
11. Hududiy va tuman (shahar) “Yoshlar daftari” jamg‘armalari mablag‘larini shakllantirish, boshqarish va ulardan foydalanish maqsadida ushbu Nizomga 1 va 2-ilovalarga muvofiq tarkibda Vasiylik kengashi (keyingi o‘rinlarda — Vasiylik kengashi) tuziladi.
Vasiylik kengashi tarkibi Qoraqalpog‘iston Respublikasi Jo‘qorg‘i Kengesi, xalq deputatlari viloyatlar va Toshkent shahar Kengashlari, shuningdek, xalq deputatlari tuman (shahar) Kengashlari qaroriga muvofiq tasdiqlanadi.
Vasiylik kengashi raisi va a’zolari “Yoshlar daftari” jamg‘armasini boshqarish bo‘yicha faoliyatini jamoatchilik asosida amalga oshiradi.
Vasiylik kengashi raisi “Yoshlar daftari” jamg‘armasi mablag‘larini boshqaruvchi hisoblanadi.
12. Yoshlar ishlari agentligining hududiy boshqarmalari hududiy “Yoshlar daftari” jamg‘armasining, Yoshlar ishlari agentligining tuman (shahar) bo‘limlari tuman (shahar) “Yoshlar daftari” jamg‘armasining ishchi organi hisoblanadi.
13. “Yoshlar daftari” jamg‘armalari mablag‘lari sarflash Vasiylik kengashi qarori asosida sarflanadi.
Vasiylik kengashi yig‘ilishlari har oyda kamida ikki marta — oyning 15-sanasigacha va oxirgi sanasigacha o‘tkaziladi.
14. Vasiylik kengashi raisi Vasiylik kengashi yig‘ilishlariga raislik qiladi.
15. Vasiylik kengashlari qarorlari Vasiylik kengashi yig‘ilishi bayoni bilan rasmiylashtiriladi.
16. Vasiylik kengashi:
“Yoshlar daftari” jamg‘armasiga umumiy rahbarlik qiladi va uning faoliyatini nazorat qiladi;
“Yoshlar daftari” jamg‘armasining daromad va xarajatlari yillik parametrlarini, ularning ijrosi to‘g‘risidagi yillik hisobotlarni, shuningdek, “Yoshlar daftari” jamg‘armasiga yuklangan vazifalarning bajarilishi to‘g‘risidagi hisobotlarni tasdiqlaydi;
“Yoshlar daftari” jamg‘armasining yillik ish rejasi va dasturlarini tasdiqlaydi;
“Yoshlar daftari” jamg‘armasi mablag‘laridan foydalanishda shaffoflikni ta’minlaydi;
“Yoshlar daftari” jamg‘armasi mablag‘lari hisobidan alohida tadbirlarni moliyalashtirish tartibini belgilaydi;
“Yoshlar daftari” jamg‘armasiga homiylik xayriyalari, shuningdek, xalqaro tashkilotlarning texnik ko‘mak mablag‘lari va grantlarini jalb qilishga ko‘maklashadi;
“Yoshlar daftari” jamg‘armasiga yuklatilgan vazifalarni Vasiylik kengashi a’zolari o‘rtasida taqsimlaydi;
“Yoshlar daftari” jamg‘armasi faoliyatiga taalluqli masalalarni ko‘rib chiqadi va ular bo‘yicha qarorlar qabul qiladi;
“Yoshlar daftari” jamg‘armasi mablag‘larini shakllantirish va ulardan foydalanish bilan bog‘liq boshqa vakolatlarni amalga oshiradi;
“Yoshlar daftari” jamg‘armasi faoliyatiga aloqador boshqa masalalarni ko‘rib chiqadi va ular bo‘yicha qarorlar qabul qiladi.
17. “Yoshlar daftari” jamg‘armasining ishchi organi:
“Yoshlar daftari” jamg‘armasining yillik ish rejasi va dasturlarini ishlab chiqadi;
Vasiylik kengashi yig‘ilishi kun tartibiga kiritiladigan masalalarni tayyorlaydi, yig‘ilish bayonnomasini yuritadi va rasmiylashtiradi;
Vasiylik kengashi a’zolariga Vasiylik kengashi yig‘ilishining vaqti va o‘tkaziladigan joyi to‘g‘risida xabar beradi;
davlat tomonidan beriladigan ijtimoiy ko‘mak va ko‘rsatiladigan moddiy yordam to‘g‘risidagi ma’lumotlarni “Yoshlar daftari”ga kiritilgan yoshlarning yakka tartibdagi anketasida qayd etib boradi;
“Yoshlar daftari”ga kiritilgan yoshlarning murojaatlari bilan ishlaydi va ko‘rib chiqish uchun Vasiylik kengashiga taqdim etadi;
Vasiylik kengashi tomonidan qabul qilingan qaror to‘g‘risida murojaat etuvchiga xabar yuboradi.
Vasiylik kengashi qarori bilan ishchi organga qo‘shimcha vazifalar ham yuklanishi mumkin.
"""
    for x in range(0, len(text), 4096):
         await call.message.answer(text[x:x + 4096])


@dp.callback_query_handler(bobcallback.filter(number="mavzu"))
async def tort(call:CallbackQuery):

    await call.answer(cache_time=20)
    await call.message.answer(text="Bu bo'lim 6 ta bobdan iborat bu boblar bilan bizda tanishingiz mumkin")