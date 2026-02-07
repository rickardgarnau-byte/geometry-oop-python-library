# Lab 2 - Geometri och OOP

Ett Python-projekt där jag byggt geometriska former med Objektorienterad Programmering (OOP). Fokus låg på arv, inkapsling och att få klasserna att funka smidigt ihop.

## Vad Går Projektet Ut På?

Målet var att bygga ett gäng klasser för geometriska former. Hela projektet innehåller:

  * En **abstrakt basklass** `Shape` som samlar all gemensam logik (som position och flytt-metoder).
  * Klasserna `Circle` och `Rectangle` som ärver från `Shape`.
  * Properties (`@property`) för att beräkna `area` och `perimeter` på ett snyggt sätt.
  * **Operator overloading** (t.ex. `==` och `<`) för att kunna jämföra former med varandra.
  * Felhantering så att man inte kan skapa former med negativa mått eller text-strängar.
  * En `utils.py`-fil för att återanvända valideringskod (vi gillar **DRY**-principen\!).

### Bonusfunktioner

Jag implementerade även alla bonusuppgifter:

  * 3D-formerna `Cube` och `Sphere` (dessa ärver *inte* från `Shape` då 2D/3D-logik skiljer sig).
  * En `Shape2DPlotter`-klass som ritar upp 2D-formerna i en graf med `matplotlib`.
  * Enhetstester med `pytest` för att verifiera 3D-klasserna.

## Min UML-plan

Här är ritningen jag började med för 2D-klasserna. Planen var att ha `Shape` som en abstrakt förälder som `Circle` och `Rectangle` ärver ifrån. All gemensam kod (som `x`, `y` och `translate`) hamnar i `Shape`.
![UML Klassdiagram](Uml_lab2.png)

## Klass-struktur

### Shape (Abstrakt Basklass)

  * **Attribut**: `x`, `y` (position).
  * **Abstrakta Properties**: `area`, `perimeter` (dessa *måste* implementeras av alla barnklasser).
  * **Metoder**:
      * `translate(dx, dy)` - Flyttar formen.
      * Jämförelse-operatorer (`==`, `<`, `>`, `<=`, `>=`).
      * `__repr__()` & `__str__()` för att skriva ut objektet snyggt.

### Rectangle

  * **Extra attribut**: `width`, `height`.
  * **Properties**:
      * `area` - Räknar ut `width * height`.
      * `perimeter` - Räknar ut `2 * (width + height)`.
      * `is_square` - Kollar om bredd och höjd är lika.
  * **Validering**: Ser till att `width` och `height` är positiva tal.

### Circle

  * **Extra attribut**: `radius`.
  * **Properties**:
      * `area` - Räknar ut $\pi \times \text{radie}^2$.
      * `perimeter` - Räknar ut $2\pi \times \text{radie}$.
      * `is_unit_circle` - Kollar om radien är 1 och centrum är i (0,0).
  * **Validering**: Ser till att `radius` är ett positivt tal.

## Exempel på Användning

Här är hur man kan använda 2D-klasserna:

```python
from circle import Circle
from rectangle import Rectangle

# Skapa former
circle1 = Circle(x=0, y=0, radius=1)  # enhetscirkel
rectangle = Rectangle(x=0, y=0, width=5, height=3)

# Jämför former (baserat på area)
print(circle1 == rectangle)  # False

# Flytta former
circle1.translate(5, 3)
print(f"Ny position: ({circle1.x}, {circle1.y})") # Ny position: (5.0, 3.0)

# Kolla properties
print(f"Cirkelns area: {circle1.area:.2f}") # Cirkelns area: 3.14
print(f"Är rektangeln en kvadrat? {rectangle.is_square}") # Är rektangeln en kvadrat? False
```

### Felhantering

Koden kraschar (på ett bra sätt) om man försöker mata in felaktiga värden, tack vare valideringen i mina **setters**:

```python
try:
    # Försöker skapa en cirkel med negativ radie
    circle = Circle(radius=-5)
except ValueError as e:
    print(e)  # "The radius cannot be negative"

try:
    # Försöker skapa en rektangel med text
    rectangle = Rectangle(width="fem", height=3)
except TypeError as e:
    print(e)  # "must be a number"
```

## Bonus: Visualisering med Plotter

Jag byggde en `Shape2DPlotter`-klass för att rita upp formerna:

```python
from shape2dplotter import Shape2DPlotter
from circle import Circle
from rectangle import Rectangle

# Skapa en plotter
plotter = Shape2DPlotter(title="Mina Fina Former")

# Skapa och lägg till former
plotter.add_shape(Circle(x=5, y=5, radius=4))
plotter.add_shape(Rectangle(x=0, y=0, width=3, height=6))
plotter.add_shape(Rectangle(x=-8, y=2, width=2, height=2)) # En kvadrat

# Visa grafen
plotter.show_plot()
```

## Mina Designval

  * **Arv (Inheritance)**: Jag använde en abstrakt basklass (`Shape`) för att tvinga alla 2D-former att ha en `area` och `perimeter`. Det blir som ett "kontrakt" som barnklasserna måste följa.
  * **Valideringsstrategi**: All validering (kolla typ, kolla negativa tal) sker i **setters** (t.ex. `@radius.setter`). Det gör att koden är säker oavsett om jag sätter värdet i `__init__` eller ändrar det senare (t.ex. `c1.radius = -5`).
  * **Jämförelselogik**: Former jämförs först på sin `area`. Om arean är lika, kollar jag på `perimeter` som en "tie-breaker".
  * **Decimaltal (Floats)**: Jag använder `math.isclose()` istället för `==` när jag kollar floats (t.ex. i `is_square`). Det är för att undvika de klassiska avrundningsfelen som kan ske med decimaltal.

## Källor och Resurser

### Lärresurser

  * **Python ABC Module**: [Python Official Documentation](https://docs.python.org/3/library/abc.html) - För att förstå abstrakta klasser.
  * **Property Decorators**: [Real Python - Python Property](https://realpython.com/python-property/) - Grym guide till `@property`.
  * **pytest `raises`**: [Pytest Documentation](https://www.google.com/search?q=https://docs.pytest.org/en/7.1.x/how-to/assert.html%23assertions-about-expected-exceptions) - För att testa att koden kastar fel som den ska.


## Övriga källor:
  https://www.w3resource.com/python-exercises/oop/python-oop-exercise-4.php 
  https://medium.com/%40edmundlhs1104/python-oop-geometric-shapes-program-94ce4163fdbe 
  https://docs.python.org/3/reference/datamodel.html 
  https://github.com/AllenDowney/ThinkPython2/tree/master/code 
  https://www.geeksforgeeks.org/python/python-program-to-get-the-class-name-of-an-instance/ 
  https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax 
  https://github.com/AIgineerAB/
  https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html
  https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html
  https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html


### AI-Användning (LLM)

Jag använde en AI (typ ChatGPT/Claude) som ett bollplank under projektet. Jag bad den om:

  * Feedback på min kodstruktur och om jag följde Python-konventioner.
  * Hjälp att felsöka problem likt: varför min validering inte funkade i `__init__` (svaret var att anropa `self.x` (settern) istället för `self._x` (attributet))
  * Tips på hur man skriver bra `docstrings` och en tydlig README.
  * Hjälp med shape2dplotter framförallt

All kärnlogik har jag skrivit själv, men AIn var en bra "code reviewer" att studsa idéer mot.

## Hur man testar

De flesta 2D-filerna (`circle.py`, `rectangle.py`) har egna test-block under `if __name__ == "__main__":` som man kan köra direkt:

```bash
pytest
```

<<<<<<< HEAD
För 3D-klasserna finns det riktiga enhetstester. Kör dem från terminalen i projektmappen med:

```bash
pytest
```

Du bör se att alla tester passerar\!

## Projektstruktur

```
lab_2_geometry_oop/
├── README.md
├── Uml_lab2.png
│
├── shape.py          # Abstrakt basklass (2D)
├── rectangle.py      # Rektangel-klassen (2D)
├── circle.py         # Cirkel-klassen (2D)
├── utils.py          # Hjälpfunktion (validate_number)
│
├── shape2dplotter.py # Bonus: Plotter-klassen (2D)
│
├── cube.py           # Bonus: Kub-klassen (3D)
├── sphere.py         # Bonus: Sfär-klassen (3D)
│
├── test_cube.py      # Bonus: Pytest för Kub
└── test_sphere.py    # Bonus: Pytest för Sfär
```

## Student

Rickard Garnau
=======
