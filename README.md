# ZADANIA TEORETYCZNE

### 1. Jaki argument odpowiada za połączenie TCP?
**a)** AF\_INET  
**b)** AF\_INET6  
**c)** SOCK\_DGRAM  
**d)** SOCK\_STREAM

### 2. Chcąc wysłać obiekt x = [1, 2, 3] użyjemy komendy:
**a)** conn.sendall(str.encode(x))  
**b)** conn.sendall(pickle.dumps(x))

### 3. Mając obiekt client = socket.socket(socket.AF\_INET, socket.SOCK\_STREAM), napisz, jaką komendą połączysz się z serwerem o adresie 192.168.2.1 na porcie 5525.

### 4. Napisz jaki wynik zwraca funkcja atan2 i dlaczego dodajemy do niego wartość 180°. 

### 5. Do czego służy funkcja blit?
**a)** tworzy kopię grafiki i uzyskuje z niej kwadrat  
**b)** służy do rysowania jednych obiektów Surface na drugich 
**c)** obraca grafikę o podany kąt
**d)** wypełnia całe okno danym kolorem

# ZADANIA PRAKTYCZNE

## ZADANIE 1
Otwórz plik ZADANKO\_1.py i postępuj zgodnie z instrukcjami. Twoim zadaniem jest napisanie prostego przykładowego serwera.  
**Pobierz do jednego foldera wszystkie zadania z części połączeniowej.**

## ZADANIE 2
Otwórz plik ZADANKO\_2.py i postępuj zgodnie z instrukcjami. W tym zadaniu tworzysz prostą aplikację kliencką. Po wykonaniu wszystkich instrukcji przeklej całość do pliku ZADANKO\_2.2.py, a następnie uruchom kolejno ZADANKO\_1.py , ZADANKO\_2.py i ZADANKO\_2.2.py.  
**Miej na uwadze, że dla uproszczenia serwera każdy kolejny użytkownik przyjmuje kolejny indeks, a komunikacja przewidziana jest dla dwóch pierwszych użytkowników. Przy każdym teście restartuj serwer!**

## ZADANIE 3
Otwórz plik ZADANKO\_3.py i postępuj zgodnie z instrukcjami. Twoim zadaniem jest napisanie bardzo prostej aplikacji, korzystając z moduły pygame.
