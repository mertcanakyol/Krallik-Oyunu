#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import sys

class Kingdom:
    def __init__(self, name, is_player_controlled):
        self.name = name

        if is_player_controlled:
            self.population = 2000
            self.gold = 5000
            self.army = 1000
            self.food = 2000
            self.happiness = 80
        else:
            self.population = random.randint(800, 3000)
            self.gold = random.randint(3000, 8000)
            self.army = random.randint(400, 1500)
            self.food = random.randint(1500, 2500)
            self.happiness = random.randint(60, 100)

    def train_soldiers(self):
        if self.gold >= 500 and self.food >= 200:
            self.army += 50
            self.gold -= 500
            self.food -= 200
            self.happiness += 5
            print(f"⚔️ 50 asker eğitildi! Mevcut asker sayısı: {self.army} - Savaşa hazır!")
        else:
            print("❌ Yeterli kaynak yok! (500 altın ve 200 yemek gerekiyor)")

    def battle(self, enemy, kingdoms):
        print(f"\n⚔️ {enemy.name} krallığına savaş açıldı! Düşman asker sayısı: {enemy.army}")

        if self.army >= enemy.army:
            print(f"🏆 Zafer! {enemy.name} Krallığını yendik!")
            self.army -= random.randint(50, 200)
            self.happiness -= 20

            captured_gold = enemy.gold // 4
            captured_food = enemy.food // 4

            self.gold += captured_gold
            self.food += captured_food

            enemy.army = 0
            enemy.gold = 0
            enemy.food = 0
            kingdoms.remove(enemy)

            print(f"💀 {enemy.name} Krallığı çöktü! Artık bir tehdit değil.")
            print(f"💰 Krallığın altının %50’sini ele geçirdik! Kazandığımız altın: {captured_gold}")
            print(f"🍽️ Krallığın yemek stoklarının %25’ini ele geçirdik! Kazandığımız yemek: {captured_food}")

            additional_rebellion_risk = random.randint(5, 15)
            self.happiness -= additional_rebellion_risk
            print(f"⚠️ Savaş sonrası halk huzursuz! İsyan riski %{additional_rebellion_risk} arttı.")

            if len(kingdoms) == 0:
                print("\n🎉🎊 Tebrikler! Artık tüm toprakların tek hükümdarısın! 🎊🎉")
                print("👑 Krallığın gücü ile tüm dünyayı fethettin ve halkın seni büyük bir kahraman olarak selamlıyor!")
                print("🔥 Krallığın, Altınşehir, sonsuza kadar hüküm sürecek!")
                print("🏰 Artık tahtta mutlak bir lider olarak oturuyorsun! 🎯")
                sys.exit()

            self.check_rebellion()
        else:
            print("💀 Savaşı kaybettik! Halk panik içinde!")
            self.happiness = 0
            self.check_rebellion()

    def check_rebellion(self):
        rebellion_risk = 100 - self.happiness
        print(f"⚠️ Halkın isyan riski: %{rebellion_risk}")

        if rebellion_risk >= 75:
            print("💥 Halk isyan etti! Krallığın çöktü, oyun sona erdi.")

            print("\n🔄 Tekrar oynamak için 'Q' tuşuna basın veya çıkmak için herhangi bir tuşa basın.")
            restart_choice = input()

            if restart_choice.lower() == "q":
                print("\n🌀 Oyun yeniden başlatılıyor...\n")
                main()
            else:
                sys.exit()
        else:
            print("✅ İsyan riski yüksek ama henüz isyan çıkmadı. Dikkatli yönetmelisin!")

    def show_status(self):
        print(f"\n🏰 {self.name} Krallığı Durumu:")
        print(f"👥 Nüfus: {self.population}")
        print(f"💰 Altın: {self.gold}")
        print(f"⚔️ Ordu: {self.army}")
        print(f"🍽️ Yemek: {self.food}")
        print(f"😊 Mutluluk: {self.happiness}")

def main():
    player_name = input("👑 Kendi krallığını kur! Krallığının adını gir: ").strip()
    if not player_name:
        player_name = "Adsız Krallık"
    player_kingdom = Kingdom(player_name, True)

    kingdoms = [
        Kingdom("Batanya", False),
        Kingdom("İmparatorluk", False),
        Kingdom("Aseray", False),
        Kingdom("Kuzait", False),
        Kingdom("Vlandıya", False)
    ]

    while True:
        print("\n📜 Krallık Yönetimi")
        print("1️⃣ Kendi Krallık Durumunu Görüntüle")
        print("2️⃣ Asker Eğit (Altın ve Yemek Harcar)")
        print("3️⃣ Krallık Seçerek Savaş Başlat")
        print("4️⃣ Genel Krallık Sıralaması")
        print("5️⃣ Çıkış")
        choice = input("👉 Seçiminizi girin: ")

        if choice == "1":
            player_kingdom.show_status()

        elif choice == "2":
            player_kingdom.train_soldiers()

        elif choice == "3":
            print("\n⚔️ Hangi krallığa saldırmak istiyorsun?")
            for i, k in enumerate(kingdoms):
                print(f"{i + 1}. {k.name}")
            try:
                kingdom_choice = int(input("👉 Seçiminizi girin: "))
                if 1 <= kingdom_choice <= len(kingdoms):
                    player_kingdom.battle(kingdoms[kingdom_choice - 1], kingdoms)
                else:
                    print("❌ Geçersiz seçim!")
            except ValueError:
                print("❌ Sayı girmen gerekiyor!")

        elif choice == "4":
            all_kingdoms = kingdoms + [player_kingdom]
            sorted_kingdoms = sorted(all_kingdoms, key=lambda k: k.gold + k.army, reverse=True)

            print("\n🏆 Genel Krallık Sıralaması:")
            for k in sorted_kingdoms:
                print(f"{k.name} - {k.gold} altın, {k.army} asker")

        elif choice == "5":
            print("🏰 Krallık yönetimi sonlandırılıyor...")
            break

        else:
            print("❌ Geçersiz seçim!")

if __name__ == "__main__":
    main()


# In[ ]:




