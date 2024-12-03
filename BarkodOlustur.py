#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from datetime import datetime

class OtomotivBarkodSistemi:
    def __init__(self):
        self.markalar = {
            'Volkswagen': '02',
            'Opel': '04',
            'Fiat': '06',
            'Peugeot': '08',
            'Toyota': '10',
            'Honda': '12',
            'Nissan': '14',
            'Mazda': '16',
            'Mitsubishi': '18',
            'Subaru': '20',
            'Suzuki': '22',
            'Isuzu': '24',
            'Hyundai': '26',
            'Kia': '28',
            'SsangYong': '30',
            'Ford': '32',
            'Renault': '34'
        }

        self.modeller = {
            'Volkswagen': {
                'Golf': '02', 'Polo': '04', 'Passat': '06', 'Jetta': '08', 'Arteon': '10',
                'Tiguan': '12', 'T-Roc': '14', 'T-Cross': '16', 'ID.3': '18', 'ID.4': '20',
                'ID.5': '22', 'ID.7': '24', 'Atlas': '26', 'Taos': '28', 'Nivus': '30',
                'Virtus': '32', 'Touareg': '34', 'Caddy': '36', 'Transporter': '38',
                'Crafter': '40', 'Amarok': '42', 'Scirocco': '44', 'Beetle': '46',
                'CC': '48', 'Sharan': '50', 'Touran': '52'
            },
            'Opel': {
                'Corsa': '02', 'Astra': '04', 'Insignia': '06', 'Crossland': '08',
                'Grandland': '10', 'Mokka': '12', 'Combo': '14', 'Vivaro': '16',
                'Movano': '18', 'Zafira': '20', 'Vectra': '22', 'Meriva': '24',
                'Adam': '26', 'Karl': '28', 'Cascada': '30', 'Antara': '32',
                'Agila': '34', 'Ampera': '36', 'GT': '38'
            },
            'Fiat': {
                '500': '02', 'Panda': '04', 'Tipo': '06', '500X': '08', '500L': '10',
                'Cronos': '12', 'Pulse': '14', 'Strada': '16', 'Toro': '18', 'Ducato': '20',
                'Doblo': '22', 'Fiorino': '24', 'Fullback': '26', 'Scudo': '28', 'Talento': '30',
                'Linea': '32', 'Albea': '34', 'Palio': '36', 'Siena': '38', 'Egea': '40',
                'Egea Cross': '42', 'Bravo': '44', 'Punto': '46', 'Grande Punto': '48',
                'Uno': '50', 'Pratico': '52', 'Qubo': '54'
            },
            'Peugeot': {
                '108': '02', '208': '04', '2008': '06', '308': '08', '3008': '10',
                '408': '12', '508': '14', '5008': '16', 'Rifter': '18', 'Partner': '20',
                'Expert': '22', 'Boxer': '24', 'Landtrek': '26', 'Traveller': '28',
                'Bipper': '30', 'iOn': '32', 'RCZ': '34', '206': '36', '207': '38',
                '307': '40', '407': '42', '607': '44', '807': '46', '1007': '48',
                '4007': '50', '4008': '52'
            },
            'Toyota': {
                'Yaris': '02', 'Corolla': '04', 'Camry': '06', 'RAV4': '08', 'C-HR': '10',
                'Highlander': '12', 'Land Cruiser': '14', 'Hilux': '16', 'Proace': '18',
                'Aygo': '20', 'Prius': '22', 'Crown': '24', 'bZ4X': '26', 'Mirai': '28',
                'GR86': '30', 'Supra': '32', 'Avalon': '34', 'Sienna': '36', 'Venza': '38',
                'Sequoia': '40', 'Tundra': '42', 'Matrix': '44', 'Verso': '46', 'Avensis': '48',
                'Celica': '50', 'MR2': '52', 'Previa': '54', 'Urban Cruiser': '56'
            },
            'Honda': {
                'Civic': '02', 'Accord': '04', 'CR-V': '06', 'HR-V': '08', 'Jazz/Fit': '10',
                'e': '12', 'ZR-V': '14', 'NSX': '16', 'City': '18', 'Ridgeline': '20',
                'Pilot': '22', 'Passport': '24', 'Insight': '26', 'Legend': '28',
                'Odyssey': '30', 'Element': '32', 'Fit Shuttle': '34', 'Freed': '36',
                'Stepwgn': '38', 'Crosstour': '40', 'S2000': '42', 'Beat': '44',
                'Acty': '46', 'Vamos': '48', 'N-Box': '50', 'N-One': '52', 'N-WGN': '54',
                'Shuttle': '56', 'Airwave': '58', 'Mobilio': '60', 'Brio': '62',
                'WR-V': '64', 'BR-V': '66', 'Vezel': '68', 'Clarity': '70'
            },
            'Nissan': {
                'Micra': '02', 'Leaf': '04', 'Juke': '06', 'Qashqai': '08', 'X-Trail': '10',
                'Ariya': '12', 'GT-R': '14', 'Z': '16', 'Serena': '18', 'Patrol': '20',
                'Navara': '22', 'Note': '24', 'Kicks': '26', 'Terra': '28', 'Pathfinder': '30',
                'Altima': '32', 'Maxima': '34', 'Murano': '36', 'Rogue': '38', 'Sentra': '40',
                'Versa': '42', 'Armada': '44', 'Frontier': '46', 'Titan': '48', '370Z': '50',
                'NV200': '52', 'NV3500': '54', 'Cube': '56', 'Juke Nismo': '58', 'Pulsar': '60'
            },
            'Mazda': {
                'Mazda2': '02', 'Mazda3': '04', 'Mazda6': '06', 'CX-3': '08', 'CX-30': '10',
                'CX-5': '12', 'CX-60': '14', 'CX-90': '16', 'MX-5': '18', 'MX-30': '20',
                'BT-50': '22', 'CX-7': '24', 'CX-8': '26', 'RX-8': '28', 'Bongo': '30'
            },
            'Mitsubishi': {
                'Space Star': '02', 'Eclipse Cross': '04', 'ASX': '06', 'Outlander': '08',
                'Pajero Sport': '10', 'L200/Triton': '12', 'eK': '14', 'Xpander': '16',
                'Delica': '18', 'Express': '20', 'Mirage': '22', 'Lancer': '24', 'Galant': '26'
            },
            'Subaru': {
                'Impreza': '02', 'Legacy': '04', 'Outback': '06', 'Forester': '08',
                'XV/Crosstrek': '10', 'BRZ': '12', 'Ascent': '14', 'WRX': '16',
                'Levorg': '18', 'Solterra': '20', 'Baja': '22', 'Tribeca': '24', 'Justy': '26'
            },
            'Suzuki': {
                'Swift': '02', 'Baleno': '04', 'Ignis': '06', 'S-Cross': '08', 'Vitara': '10',
                'Jimny': '12', 'Across': '14', 'Swace': '16', 'Alto': '18', 'Hustler': '20',
                'Wagon R': '22', 'Splash': '24', 'Celerio': '26', 'Kizashi': '28', 'SX4': '30'
            },
            'Isuzu': {
                'D-Max': '02', 'MU-X': '04', 'N-Series': '06', 'F-Series': '08',
                'C&E Series': '10', 'H Series': '12', 'ELF': '14', 'Forward': '16',
                'Giga': '18', 'Reward': '20', 'Trooper': '22', 'Rodeo': '24', 'Axiom': '26'
            },
            'Hyundai': {
                'i10': '02', 'i20': '04', 'i30': '06', 'Bayon': '08', 'Kona': '10',
                'Tucson': '12', 'Santa Fe': '14', 'Ioniq 5': '16', 'Ioniq 6': '18',
                'Staria': '20', 'H-1': '22', 'Porter': '24', 'Elantra': '26',
                'Accent': '28', 'Palisade': '30', 'Venue': '32', 'Genesis': '34',
                'Azera': '36', 'Verna': '38', 'Getz': '40', 'Matrix': '42'
            },
            'Kia': {
                'Picanto': '02', 'Rio': '04', 'Ceed': '06', 'XCeed': '08', 'Niro': '10',
                'Sportage': '12', 'Sorento': '14', 'EV6': '16', 'EV9': '18', 'Stonic': '20',
                'Soul': '22', 'Carnival': '24', 'K3': '26', 'K5': '28', 'K8': '30',
                'K9': '32', 'Seltos': '34', 'Telluride': '36', 'Bongo': '38', 'Optima': '40',
                'Stinger': '42', 'Cerato': '44', 'Mohave': '46', 'Carens': '48'
            },
            'SsangYong': {
                'Tivoli': '02', 'Korando': '04', 'Torres': '06', 'Rexton': '08',
                'Musso': '10', 'Rodius': '12', 'Actyon': '14', 'Kyron': '16',
                'Chairman': '18', 'Korando Sports': '20'
            },
            'Ford': {
                'Fiesta': '02', 'Focus': '04', 'Puma': '06', 'Kuga': '08', 'Explorer': '10',
                'Mustang': '12', 'Ranger': '14', 'Transit': '16', 'Transit Custom': '18',
                'Transit Connect': '20', 'Transit Courier': '22', 'F-150': '24',
                'Bronco': '26', 'Maverick': '28', 'Edge': '30', 'Escape': '32',
                'Expedition': '34'
            },
            'Renault': {
                'Clio': '02', 'Captur': '04', 'Austral': '06', 'Megane E-Tech': '08',
                'Arkana': '10', 'Espace': '12', 'Trafic': '14', 'Master': '16',
                'Kangoo': '18', 'Express': '20', 'Twingo': '22', 'ZOE': '24',
                'Kiger': '26', 'Triber': '28', 'Duster': '30', 'Megane': '32',
                'Megane Sedan': '34', 'Fluence': '36', 'Symbol': '38', 'Latitude': '40',
                'Kadjar': '42', 'Scenic': '44', 'Grand Scenic': '46', 'Taliant': '48',
                'Talisman': '50', 'Koleos': '52', 'Laguna': '54', 'Safrane': '56'
            }
        }

        self.ana_gruplar = {
            'ÖN-ARKA TAKIM VE SÜSPANSİYONLARI': '02',
            'MOTOR MEKANİK PARÇALARI': '04',
            'V KAYIŞ GERGİ VE RULMANLARI': '06',
            'FREN SİSTEMİ PARÇALARI': '08',
            'SOĞUTMA SİSTEMİ PARÇALARI': '10',
            'ELEKTRİK VE ELEKTRONİK PARÇALAR': '12',
            'YAKIT SİSTEMİ PARÇALARI': '14',
            'ŞANZIMAN VE AKTARMA ORGANLARI': '16',
            'DİREKSİYON SİSTEMİ PARÇALARI': '18',
            'EGZOZ SİSTEMİ PARÇALARI': '20',
            'KAROSERİ VE DIŞ AKSAMI': '22'
        }

        self.alt_gruplar = {
            # ÖN-ARKA TAKIM VE SÜSPANSİYONLARI
            'Ön Amortisör': '02',
            'Arka Amortisör': '04',
            'Ön Salıncak': '06',
            'Arka Salıncak': '08',
            'Ön Z Rot': '10',
            'Arka Z Rot': '12',
            'Ön Viraj Demiri': '14',
            'Arka Viraj Demiri': '16',
            'Ön Yay': '18',
            'Arka Yay': '20',
            'Ön Aks Taşıyıcı': '22',
            'Arka Aks Taşıyıcı': '24',
            'Ön Tekerlek Rulmanı': '26',
            'Arka Tekerlek Rulmanı': '28',
            'Motor Takozu': '30',
            'Şanzıman Takozu': '32',

            # MOTOR MEKANİK PARÇALARI
            'Motor Bloğu': '34',
            'Silindir Kapağı': '36',
            'Emme Subapı': '38',
            'Egzoz Subapı': '40',
            'Emme Subap Yatağı': '42',
            'Egzoz Subap Yatağı': '44',
            'Krank Mili': '46',
            'Standart Piston': '48',
            'Oversize Piston': '50',
            'Volan': '52',
            'Eksantrik Mili': '54',
            'Silindir Contası': '56',
            'Yağ Pompası': '58',
            'Supap İtici Mekanizması': '60',
            'Distribütör': '62',

            # V KAYIŞ GERGİ VE RULMANLARI
            'V Kayışı': '64',
            'Triger Kayışı': '66',
            'Triger Gergi Rulmanı': '68',
            'Alternatör Kayış Gergi': '70',
            'Alternatör Rulmanı': '72',
            'Klima Kompresörü Rulmanı': '74',
            'Krank Kasnağı': '76',

            # FREN SİSTEMİ PARÇALARI
            'Ön Fren Balatası': '78',
            'Arka Fren Balatası': '80',
            'Ön Fren Diski': '82',
            'Arka Fren Diski': '84',
            'Ön Fren Kaliperi': '86',
            'Arka Fren Kaliperi': '88',
            'Ana Fren Silindiri': '90',
            'Fren Merkezi': '92',
            'Ön Fren Hortumu': '94',
            'Arka Fren Hortumu': '96',
            'ABS Sensörü': '98',
            'El Fren Teli': '100',
            'El Fren Kolu': '102',

            # SOĞUTMA SİSTEMİ PARÇALARI
            'Radyatör': '104',
            'Mekanik Su Pompası': '106',
            'Elektrikli Su Pompası': '108',
            'Termostat': '110',
            'Fan Motoru': '112',
            'Üst Soğutma Hortumu': '114',
            'Alt Soğutma Hortumu': '116',
            'Genleşme Kabı': '118',
            'Radyatör Kapağı': '120',

            # ELEKTRİK VE ELEKTRONİK PARÇALAR
            'Akü': '122',
            'Alternatör': '124',
            'Marş Motoru': '126',
            'Sigorta Kutusu': '128',
            'MAP Sensörü': '130',
            'MAF Sensörü': '132',
            'Oksijen Sensörü': '134',
            'Hız Sensörü': '136',
            'ECU': '138',
            'Ateşleme Bobini': '140',
            'Ön Far': '142',
            'Arka Far': '144',
            'Sinyal Lambası': '146',
            'Sis Farı': '148',

            # YAKIT SİSTEMİ PARÇALARI
            'Yakıt Pompası': '150',
            'Dizel Enjektör': '152',
            'Benzinli Enjektör': '154',
            'Yakıt Deposu': '156',
            'Yakıt Filtresi': '158',
            'Yakıt Giriş Borusu': '160',
            'Yakıt Çıkış Borusu': '162',
            'Gaz Kelebeği': '164',

            # ŞANZIMAN VE AKTARMA ORGANLARI
            'Şanzıman Kutusu': '166',
            'Debriyaj Baskı': '168',
            'Debriyaj Disk': '170',
            'Debriyaj Rulmanı': '172',
            'Şaft': '174',
            'Diferansiyel': '176',
            'Şanzıman Yağ Filtresi': '178',
            'Tork Konvertörü': '180',

            # DİREKSİYON SİSTEMİ PARÇALARI
            'Direksiyon Kutusu': '182',
            'Elektrikli Direksiyon Pompası': '184',
            'Mekanik Direksiyon Pompası': '186',
            'Ön Direksiyon Rotu': '188',
            'Arka Direksiyon Rotu': '190',
            'Direksiyon Mafsalı': '192',
            'Hidrolik Yağ Deposu': '194',

            # EGZOZ SİSTEMİ PARÇALARI
            'Egzoz Manifoldu': '196',
            'Egzoz Borusu': '198',
            'Katalitik Konvertör': '200',
            'Susturucu': '202',
            'Lambda Sensörü': '204',

            # KAROSERİ VE DIŞ AKSAMI
            'Ön Tampon': '206',
            'Arka Tampon': '208',
            'Kaput': '210',
            'Ön Çamurluk': '212',
            'Arka Çamurluk': '214',
            'Ön Kapı': '216',
            'Arka Kapı': '218',
            'İç Dikiz Aynası': '220',
            'Dış Ayna': '222',
            'Ön Cam': '224',
            'Arka Cam': '226',
            'Yan Cam': '228'
        }

    def barkod_olustur(self, marka, model, ana_grup, alt_grup):
        return f"PP-{self.markalar.get(marka, '00')}{self.modeller.get(marka, {}).get(model, '00')}-{self.ana_gruplar.get(ana_grup, '00')}{self.alt_gruplar.get(alt_grup, '00')}"

    def excel_kaydet(self):
        data = []
        for marka in self.markalar:
            for model in self.modeller.get(marka, {}):
                for ana_grup in self.ana_gruplar:
                    for alt_grup in self.alt_gruplar:
                        barkod = self.barkod_olustur(marka, model, ana_grup, alt_grup)
                        data.append({
                            'Barkod': barkod,
                            'Marka': marka,
                            'Model': model,
                            'Ana Grup': ana_grup,
                            'Alt Grup': alt_grup,
                            'Marka Kodu': self.markalar.get(marka),
                            'Model Kodu': self.modeller.get(marka, {}).get(model),
                            'Ana Grup Kodu': self.ana_gruplar.get(ana_grup),
                            'Alt Grup Kodu': self.alt_gruplar.get(alt_grup)
                        })
        
        df = pd.DataFrame(data)
        
        # Tarih ve saat bilgisini al
        simdi = datetime.now().strftime("%Y%m%d_%H%M%S")
        dosya_adi = f"C:\\OtomotivBarkodSistemi_{simdi}.xlsx"
        
        # Excel'e kaydet
        df.to_excel(dosya_adi, index=False, engine='openpyxl')
        print(f"Barkod sistemi başarıyla kaydedildi: {dosya_adi}")

sistem = OtomotivBarkodSistemi()

if __name__ == "__main__":
    # Excel dosyasını oluştur
    sistem.excel_kaydet()
    print("Program tamamlandı.")
