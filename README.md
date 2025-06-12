# how_to_get_to
The goal of the algorithm is to determine which public transport lines (e.g. bus, tram, metro) a user should take in order to travel from a starting point to a destination point within a city.

# run command

```bash
    touch temp.txt && python utils/temp.py > temp.txt && tail -n +3 temp.txt > temp_cleaned.txt && mv temp_cleaned.txt temp.txt && python run.py < temp.txt
```

# tests

```bash
    echo "Test #1:" &&
    awk '$0 != "[TIMEOUT]"' results/result_1.txt > temp && mv temp results/result_1.txt &&
    echo "Avarage:" &&
    cat results/result_1.txt | cut -d" " -f3 | awk 'BEGIN{sum = 0; count=0} {sum = sum + $0; count = count + 1} END{print sum/count}' &&
    echo "Mean:" &&
    cat results/result_1.txt | cut -d" " -f3 | sort -n | awk 'BEGIN{count=0} {count = count + 1; if(count == 25) print $0}' &&
    echo "Best:" &&
    cat results/result_1.txt | cut -d" " -f3 | sort -n | head -1 &&
    echo "Least:" &&
    cat results/result_1.txt | cut -d" " -f3 | sort -n | tail -1
```

```bash
    echo "Test #2:" &&
    awk '$0 != "[TIMEOUT]"' results/result_2.txt > temp && mv temp results/result_2.txt &&
    echo "Avarage:" &&
    cat results/result_2.txt | cut -d" " -f3 | awk 'BEGIN{sum = 0; count=0} {sum = sum + $0; count = count + 1} END{print sum/count}' &&
    echo "Mean:" &&
    cat results/result_2.txt | cut -d" " -f3 | sort -n | awk 'BEGIN{count=0} {count = count + 1; if(count == 25) print $0}' &&
    echo "Best:" &&
    cat results/result_2.txt | cut -d" " -f3 | sort -n | head -1 &&
    echo "Least:" &&
    cat results/result_2.txt | cut -d" " -f3 | sort -n | tail -1
```

```bash
    echo "Test #3:" &&
    awk '$0 != "[TIMEOUT]"' results/result_3.txt > temp && mv temp results/result_3.txt &&
    echo "Avarage:" &&
    cat results/result_3.txt | cut -d" " -f3 | awk 'BEGIN{sum = 0; count=0} {sum = sum + $0; count = count + 1} END{print sum/count}' &&
    echo "Mean:" &&
    cat results/result_3.txt | cut -d" " -f3 | sort -n | awk 'BEGIN{count=0} {count = count + 1; if(count == 25) print $0}' &&
    echo "Best:" &&
    cat results/result_3.txt | cut -d" " -f3 | sort -n | head -1 &&
    echo "Least:" &&
    cat results/result_3.txt | cut -d" " -f3 | sort -n | tail -1
```

```bash
    echo "Test #4:" &&
    awk '$0 != "[TIMEOUT]"' results/result_4.txt > temp && mv temp results/result_4.txt &&
    echo "Avarage:" &&
    cat results/result_4.txt | cut -d" " -f3 | awk 'BEGIN{sum = 0; count=0} {sum = sum + $0; count = count + 1} END{print sum/count}' &&
    echo "Mean:" &&
    cat results/result_4.txt | cut -d" " -f3 | sort -n | awk 'BEGIN{count=0} {count = count + 1; if(count == 25) print $0}' &&
    echo "Best:" &&
    cat results/result_4.txt | cut -d" " -f3 | sort -n | head -1 &&
    echo "Least:" &&
    cat results/result_4.txt | cut -d" " -f3 | sort -n | tail -1
```

```bash
    echo "Test #5:" &&
    awk '$0 != "[TIMEOUT]"' results/result_5.txt > temp && mv temp results/result_5.txt &&
    echo "Avarage:" &&
    cat results/result_5.txt | cut -d" " -f3 | awk 'BEGIN{sum = 0; count=0} {sum = sum + $0; count = count + 1} END{print sum/count}' &&
    echo "Mean:" &&
    cat results/result_5.txt | cut -d" " -f3 | sort -n | awk 'BEGIN{count=0} {count = count + 1; if(count == 25) print $0}' &&
    echo "Best:" &&
    cat results/result_5.txt | cut -d" " -f3 | sort -n | head -1 &&
    echo "Least:" &&
    cat results/result_5.txt | cut -d" " -f3 | sort -n | tail -1
```

```bash
    echo "Test #6:" &&
    awk '$0 != "[TIMEOUT]"' results/result_6.txt > temp && mv temp results/result_6.txt &&
    echo "Avarage:" &&
    cat results/result_6.txt | cut -d" " -f3 | awk 'BEGIN{sum = 0; count=0} {sum = sum + $0; count = count + 1} END{print sum/count}' &&
    echo "Mean:" &&
    cat results/result_6.txt | cut -d" " -f3 | sort -n | awk 'BEGIN{count=0} {count = count + 1; if(count == 25) print $0}' &&
    echo "Best:" &&
    cat results/result_6.txt | cut -d" " -f3 | sort -n | head -1 &&
    echo "Least:" &&
    cat results/result_6.txt | cut -d" " -f3 | sort -n | tail -1
```

### 📊 Wyniki testów

Testy były wykonywane na 6 różnych trasach różnych odległości, 50 powtórzeń każdego testu

| Test # | Average   | Mean | Best | Least |
|--------|-----------|------|------|-------|
| 1      | 268       | 268  | 268  | 268   |
| 2      | 290.76    | 288  | 288  | 294   |
| 3      | 193.46    | 180  | 145  | 433   |
| 4      | 365.34    | 368  | 361  | 375   |
| 5      | 238.449   | 231  | 211  | 336   |
| 6      | 445.105   | —    | 395  | 507   |

### Wnioski

#### Trasa I:

- Za każdym razem została znaleziona najlepsza trasa.

#### Trasa II:

- Mała różnica między best a least jest oznaką tego, że algorytm dobrze sobie radzi na tych danych.

#### Trasa III:

- Duża różnica mięðzy best a least oznacza, że trasa była trudna i algorytm dał się złapać.
- Mean jest wyraźnie mniejsze od avarage, więc algorytm zazwyczaj radzi sobie dobrze, średnią zawyżają wyniki odstające.
- Mean jest sporo większe od best, więc najlepszy wynik był rzadszy, a częściej trafiały się gorsze.

#### Trasa IV:

- Mała różnica między best a least jest oznaką tego, że algorytm dobrze sobie radzi na tych danych.

#### Trasa V:

- Mała różnica między avarage, mean i best, oraz odstający least. Oznacza to że radzi sobie prawie zawsze dobrze, ale czasem występują odstająco mocno wyniki.

#### Trasa VI:

- Różnica 25% między best a least, więc całkiem nieźle.
- Avarage mniej więcej po środku, więc najpewniej można założyć rozkład normalny wyników.
- Brak mean oznacza dużą ilość timeoutów, więc trasa była trudna do znalezienia.
- Na podstawie poprzednich wniosków, trudno było znaleźć trase, ale jak już została znaleziona, to była całkiem niezła

### Wnioski końcowe:

- Algorytm radzi sobie dobrze na większości tras.
- Zazwyczaj znajduje bardzo dobre wyniki.
- W testach z większą wariancją wyników (np. Trasa III), mediana daje lepsze odzwierciedlenie typowego zachowania algorytmu niż średnia arytmetyczna.
- Jeżeli trasa ma dużo przesiadek mogą wystąpić problemy, ale nadal sobie radzi.
- Dla niektórych tras pojawia się sporo timeout, ponieważ algorytm nie jest w stanie znaleźć żadnej trasy przez narzuconą limit czasowy.