import random
from collections import defaultdict

class RockPaperScissorsAI:
    """AI yang bisa belajar dari pola pemain"""
    
    def __init__(self):
        self.choices = ['batu', 'gunting', 'kertas']
        self.player_history = []
        self.win_count = 0
        self.loss_count = 0
        self.draw_count = 0
        self.move_predictions = defaultdict(lambda: {'batu': 0, 'gunting': 0, 'kertas': 0})
        self.last_player_move = None
        self.learning_rate = 0.7  # Probabilitas AI menggunakan strategi learned
    
    def get_winning_move(self, player_choice):
        """Mengembalikan move yang mengalahkan pilihan pemain"""
        winning_moves = {
            'batu': 'kertas',      # Kertas mengalahkan batu
            'gunting': 'batu',     # Batu mengalahkan gunting
            'kertas': 'gunting'    # Gunting mengalahkan kertas
        }
        return winning_moves[player_choice]
    
    def learn_from_player(self, player_choice):
        """AI belajar dari pilihan pemain sebelumnya"""
        if self.last_player_move is not None:
            # Track pola: setelah move X, pemain cenderung memilih apa?
            self.move_predictions[self.last_player_move][player_choice] += 1
    
    def predict_next_move(self):
        """Prediksi move pemain berdasarkan riwayat"""
        if self.last_player_move is None or len(self.player_history) < 2:
            return random.choice(self.choices)
        
        # Ambil statistik move yang paling sering setelah last_player_move
        predictions = self.move_predictions[self.last_player_move]
        most_likely_move = max(predictions.items(), key=lambda x: x[1])
        
        return most_likely_move[0]
    
    def choose_move(self):
        """AI memilih gerakan untuk melawan pemain"""
        if len(self.player_history) < 2:
            # Di awal game, random
            return random.choice(self.choices)
        
        # Gunakan pembelajaran dengan probabilitas
        if random.random() < self.learning_rate:
            # Coba mengalahkan prediksi pemain
            predicted_move = self.predict_next_move()
            counter_move = self.get_winning_move(predicted_move)
            return counter_move
        else:
            # Random sebagai variasi
            return random.choice(self.choices)
    
    def record_result(self, player_choice, ai_choice):
        """Mencatat hasil permainan untuk pembelajaran"""
        self.learn_from_player(player_choice)
        self.player_history.append(player_choice)
        self.last_player_move = player_choice
        
        # Tentukan pemenang dan update statistik
        result = self.determine_winner(player_choice, ai_choice)
        if result == 'pemain':
            self.loss_count += 1
        elif result == 'ai':
            self.win_count += 1
        else:
            self.draw_count += 1
        
        return result
    
    def determine_winner(self, player_choice, ai_choice):
        """Menentukan pemenang"""
        if player_choice == ai_choice:
            return 'seri'
        
        winning_conditions = {
            ('batu', 'gunting'): 'pemain',      # Batu mengalahkan gunting
            ('gunting', 'kertas'): 'pemain',    # Gunting mengalahkan kertas
            ('kertas', 'batu'): 'pemain',       # Kertas mengalahkan batu
            ('batu', 'kertas'): 'ai',
            ('gunting', 'batu'): 'ai',
            ('kertas', 'gunting'): 'ai'
        }
        
        return winning_conditions.get((player_choice, ai_choice), 'seri')
    
    def show_ai_stats(self):
        """Menampilkan statistik pembelajaran AI"""
        print(f"\n📊 Statistik AI:")
        print(f"   Menang: {self.win_count} | Kalah: {self.loss_count} | Seri: {self.draw_count}")
        
        if self.player_history:
            print(f"   Total pertandingan: {len(self.player_history)}")
            win_rate = (self.win_count / len(self.player_history)) * 100
            print(f"   Win rate AI: {win_rate:.1f}%")


class RockPaperScissorsGame:
    """Game Batu Gunting Kertas dengan AI yang belajar"""
    
    def __init__(self):
        self.ai = RockPaperScissorsAI()
        self.player_wins = 0
        self.ai_wins = 0
        self.draws = 0
        self.total_rounds = 0
    
    def display_welcome(self):
        """Menampilkan pesan sambutan"""
        print("=" * 60)
        print("🎮 SELAMAT DATANG DI GAME BATU GUNTING KERTAS! 🎮")
        print("=" * 60)
        print("\n🤖 Anda bermain melawan AI yang BISA BELAJAR!")
        print("\n📋 Aturan:")
        print("   • Batu mengalahkan Gunting")
        print("   • Gunting mengalahkan Kertas")
        print("   • Kertas mengalahkan Batu")
        print("\n💡 Strategi AI:")
        print("   ✓ Mencatat pola pilihan Anda")
        print("   ✓ Memprediksi gerakan Anda berikutnya")
        print("   ✓ Mencoba mengalahkan prediksi tersebut")
        print("\n" + "=" * 60)
    
    def get_player_input(self):
        """Mendapatkan input dari pemain"""
        while True:
            print("\n🎯 Pilih gerakan Anda:")
            print("   1. Batu")
            print("   2. Gunting")
            print("   3. Kertas")
            print("   0. Keluar dari game")
            
            choice = input("\nMasukkan pilihan (0-3): ").strip()
            
            if choice == '0':
                return None
            elif choice == '1':
                return 'batu'
            elif choice == '2':
                return 'gunting'
            elif choice == '3':
                return 'kertas'
            else:
                print("❌ Input tidak valid! Coba lagi.")
    
    def display_round(self, round_num, player_choice, ai_choice, result):
        """Menampilkan hasil putaran"""
        print(f"\n{'='*60}")
        print(f"🎯 PUTARAN {round_num}")
        print(f"{'='*60}")
        
        # Emoji untuk setiap pilihan
        emojis = {
            'batu': '✊',
            'gunting': '✌️',
            'kertas': '✋'
        }
        
        print(f"\n🧑 Pemain  : {emojis[player_choice]} {player_choice.upper()}")
        print(f"🤖 AI     : {emojis[ai_choice]} {ai_choice.upper()}")
        
        # Tampilkan hasil
        if result == 'seri':
            print(f"\n🤝 HASIL: SERI!")
            self.draws += 1
        elif result == 'pemain':
            print(f"\n🎉 HASIL: PEMAIN MENANG! 🎉")
            self.player_wins += 1
        else:
            print(f"\n😔 HASIL: AI MENANG")
            self.ai_wins += 1
        
        self.total_rounds += 1
        self.display_score()
    
    def display_score(self):
        """Menampilkan skor saat ini"""
        print(f"\n📈 SKOR: Pemain {self.player_wins} - {self.ai_wins} AI | Seri: {self.draws}")
    
    def display_final_stats(self):
        """Menampilkan statistik akhir game"""
        print(f"\n\n{'='*60}")
        print(f"📊 STATISTIK AKHIR GAME")
        print(f"{'='*60}")
        
        print(f"\n🏆 Skor Akhir:")
        print(f"   Pemain  : {self.player_wins} 🧑")
        print(f"   AI      : {self.ai_wins} 🤖")
        print(f"   Seri    : {self.draws} 🤝")
        print(f"   Total   : {self.total_rounds} putaran")
        
        if self.player_wins > self.ai_wins:
            print(f"\n🎖️  PEMENANG KESELURUHAN: PEMAIN! 🎖️")
        elif self.ai_wins > self.player_wins:
            print(f"\n🤖 PEMENANG KESELURUHAN: AI! 🤖")
        else:
            print(f"\n🤝 PEMENANG KESELURUHAN: SERI! 🤝")
        
        # Statistik AI
        self.ai.show_ai_stats()
        
        print(f"\n{'='*60}\n")
    
    def play(self):
        """Menjalankan game"""
        self.display_welcome()
        
        while True:
            # Dapatkan pilihan pemain
            player_choice = self.get_player_input()
            
            if player_choice is None:
                print("\n👋 Terima kasih telah bermain!")
                self.display_final_stats()
                break
            
            # AI memilih berdasarkan pembelajaran
            ai_choice = self.ai.choose_move()
            
            # Tentukan pemenang dan catat
            result = self.ai.record_result(player_choice, ai_choice)
            
            # Tampilkan hasil
            self.display_round(self.total_rounds, player_choice, ai_choice, result)
            
            # Tampilkan info pembelajaran AI
            if self.total_rounds > 2:
                print(f"\n🧠 AI Insight: AI sudah belajar dari {len(self.ai.player_history)} gerakan Anda!")


def main():
    """Main function untuk menjalankan game"""
    game = RockPaperScissorsGame()
    game.play()


if __name__ == "__main__":
    main()
