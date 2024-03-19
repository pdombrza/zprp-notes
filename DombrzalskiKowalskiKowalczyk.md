# Zaawansowane Programowanie w Pythonie

Jakub Kowalczyk,  <br>
Paweł Dombrzalski, <br>
Piotr Kowalski


### Planowana funkcjonalność programu:
Implementacja internetowej platformy konkursowej do rejestracji zgłoszeń uczestników, które zawierają prace artystyczne. Aplikacja webowa umożliwi właścicielom fundacji "Bo Warto" powiadomienie odbiorców z bazy mailingowej o nowym konkursie, zarządzanie trwającymi konkursami, weryfikację formularzy zgłoszeniowych, ocenę prac i generowanie statystyk. System ma być dostępny po przekierowaniu z zakładki istniejącej już  [strony fundacji](https://www.fundacjabowarto.pl/). Celem pracy podczas projektu na ZPRP jest naprawienie istniejących problemów, przykładając szczególną uwagę do poprawienia jakości kodu oraz dodanie nowych funkcjonalności do stworzenia kompletnej aplikacji webowej wymaganej przez klienta i możliwej do wdrożenia.
[Obecny stan repozytorium](https://gitlab.com/filipeckijan/contest-platform)

### Szczegółowy zakres funkcjonalności:
* Dostosowanie projektu do wszystkich wymagań przedmiotu - 12factor.net, logowanie, cache, kolejki, testy automatyczne, OpenAPI
* Nowe funkcjonalności zlecone przez Panią Prezes: automatyczne generowanie i przydzielanie / wysyłka mailowa dyplomów uznania dla wszystkich uczestników konkursów oraz moduł generowania statystyk konkursów i potencjalne ułatwienia integracji z kanałami na social mediach
* Naprawa istotnej części systemu oceny prac - obecnie każdy juror modyfikuje tę samą instancję oceny. Należy odróżnić indywidualne oceny, wyświetlać średnią z nich, dodać możliwość uwag tekstowych zamiast samych kryteriów liczbowych oraz potencjalne oznaczanie prac jako faworytów / wstępnie odrzuconych.
* Naprawa importu danych szkół (posiadanych przez fundację) z pliku csv
* Rozbudowanie profilu użytkownika - dotychczas wyświetla jedynie imię, nazwisko i mail
* Rozróżnianie stanów konkursów - aktywny, w trakcie oceny, zakończony
* Wysyłka newslettera o konkursie dla filtrowanych grup odbiorców - teraz można wysłać jedynie do wszystkich użytkowników bazy
* Uzupełnienie operacji CRUD w wielu miejscach np. teraz lista użytkowników jest jedynie do wglądu dla administratora - nie da się usuwać kont ani edytować o nich informacji; nie ma możliwości edycji informacji o konkursie w czasie jego trwania; nie ma możliwości korekty błędów w zgłoszeniach przez administratora poprzez edytowanie go; brak opcji dodania nowych szkół do bazy;
* Poprawa User Experience, np. wymagane wyrażenie zgody na newsletter, pole tekstowe na uwagi w zgłoszeniu, mailowe potwierdzenie poprawnego zgłoszenia, sprawdzanie poprawności danych w zgłoszeniu konkursowym, powiadomienia o konkursach, które wkrótce się kończą, potencjalnie inne opcje logowania np. przez konto Google
* Poprawa jakości kodu


### Harmonogram projektu

|Tydzień |   Data	|   Praca nad    |
|---	|---	|  --- |
| 4. | 11 - 17 marca    | Stworzenie design proposal  	|
|5. |18 - 24 marca   	| Zapoznanie się z istniejącym kodem przez nowych członków zespołu; początek pracy nad dostosowaniem projektu do wszystkich wymagań przedmiotu; nauka narzędzi pracy  	|
|6. |25 - 31 marca   	| Dostosowanie projektu do wszystkich wymagań przedmiotu - 12factor.net, logowanie, cache, kolejki, testy automatyczne, OpenAPI, skrypty  	|
|7. |1 - 7 kwietnia   	|  Refaktoring kodu, naprawa systemu oceniania i importu csv 	|
| 8. |8 - 14 kwietnia  	| Refaktoring kodu c.d.; dodanie nowych funkcjonalności segregacji prac i ocen pisemnych do modułu oceniania prac; rozbudowanie profilu użytkownika; rozróżnianie stanów konkursów  	|
|9. |15 - 21 kwietnia   	| Przerwa - czas na naukę do kolokwiów  	|
| 10. |22 - 28 kwietnia  	|Nowe funkcjonalności zlecone przez Panią Prezes: automatyczne generowanie i przydzielanie / wysyłka mailowa dyplomów uznania dla wszystkich uczestników konkursów oraz moduł generowania statystyk konkursów i potencjalne ułatwienia integracji z kanałami na social mediach  	|
|11. |29 kwietnia - 5 maja   	| Ewentualne kontynuowanie pracy nad nowymi funkcjonalnościami, uzupełnienie kompletności wymaganych operacji CRUD  	|
|12. |6 - 12 maja   	| Testy, poprawa newslettera  	|
|13. |13 - 19 maja   	|   Poprawa User Experience, np. wymagane wyrażenie zgody a newsletter, pole tekstowe na uwagi w zgłoszeniu, mailowe potwierdzenie poprawnego zgłoszenia, sprawdzanie poprawności danych w zgłoszeniu konkursowym, powiadomienia o konkursach, które wkrótce się kończą, Skupienie uwagi na testowaniu potencjalnie inne opcje logowania np. przez konto Google; Planowane oddanie projektu
|   14-17.	|   20 maja- 14 czerwca	| Ewentualna poprawa projektu


### Stack technologiczny:
* backend - Python Django,
* frontend - React + Vite,
* baza danych - PostgreSQL,
* testy automatyczne - Selenium,
* testy jednostkowe - Unittest,
* konteneryzacja - Docker,
* skrypty - shell

### Bibliografia:
* Django Documentation: https://docs.djangoproject.com/en/5.0/
* Django Tutorial: https://www.youtube.com/watch?v=rHux0gMZ3Eg&t=1699s&pp=ygUPZGphbmdvIHR1dG9ya
WFs
* Django course: https://www.youtube.com/watch?v=PtQiiknWUcI&pp=ygUPZGphbmdvIHR1dG9yaWFs
* React Documentation: https://react.dev/
* React Tutorial: https://www.youtube.com/watch?v=SqcY0GlETPk&t=366s&pp=ygUOUmVhY3QgdHV0b3JpY
Ww%3D
* MUI: https://mui.com/
* Unittest Documentation: https://docs.python.org/3/library/unittest.html
* Selenium Documentation: https://selenium-python.readthedocs.io/