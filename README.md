# projekt-programowanie-Greski266860
projekt-programowanie-Greski266860 created by GitHub Classroom
## Amatorskie obserwacje astronomiczne zazwyczaj są prowadzone przez wiele godzin jednej nocy. Ogólnym zamysłem programu jest umożliwienie zaplanowania w łatwy sposób kilkudniowej sesji obserwacyjnej, w której na każdy dzień tygodnia przedstawi propozycje obserwacyjne w mniejszym przedziale czasowym niż pojedyncza sesja jednego dnia, co pozwoli uzyskać więcej czasu wolnego na inne czynności, np. na sen. Program ma za zadanie wspierać planowanie obserwacji astronomicznych poprzez analizę danych pobranych z serwisu meteorologicznego, mapy zanieczyszczenia światłem oraz bazy danych obiektów na nocnym niebie. Dodatkowo program będzie uwzględniał parametry sprzętu obserwacyjnego, co pozwoli na sporządzenie listy obiektów preferowanych do obserwacji przy danej konfiguracji. Obecnie rozpatrywana jest postać programu jako aplikacja webowa napisana w Pythonie 3 (Django). Projekt zakłada użycie darmowego API od serwisów meteoblue.com oraz openstreetmap.org. 
Program będzie podzielony na 5 stref (historii użytkownika):
-	Pogodowa – służąca określeniu pozycji na mapie użytkownika i uzyskaniu na jej podstawie danych pogodowych na ok. 7 dni, m.in.: zachmurzenia, opadów, temperatury w nocy.
-	Określająca zanieczyszczenie światłem – służąca określeniu pozycji na mapie użytkownika i pokazaniu zanieczyszczenia światłem w danym miejscu i okolicy na podręcznej mapie.
-	Sprzętowa – służąca określeniu parametrów sprzętu użytkownika, co pozwoli wyeliminować z pracy programu obiekty astronomiczne, które będą niemożliwe lub bardzo trudne do zauważenia oraz pokaże ich spodziewany wygląd w okularze.
-	Biblioteczna – posiadająca bazę danych obiektów astronomicznych oraz ich szczegółowe dane dotyczące widoczności danego dnia w danej lokalizacji, zdjęcia oraz podstawowe informacje na ich temat. 
-	Planu obserwacji – łącząca poprzednie strefy, na podstawie danych wprowadzonych przez użytkownika pokazuje ona możliwe do obserwacji obiekty na niebie w danych dniach z małym zachmurzeniem, dzieląc je na 1-3 godzinne strefy godzinowe, które zostaną przydzielone na dane dni. 

# UWAGA
## w folderze mysite zawarte są pliki z oficjalnego poradnika django, a pliki programu autorskiego w astrosupport
