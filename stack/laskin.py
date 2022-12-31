"""
Yksinkertainen Python-kielinen laskin-moduuli
"""

class Laskin():
    """
    Luokka, joka toteuttaa yksinkertaiset laskutoimitukset

    ...

    Attributes
    ----------
        luku_1 : int
            käyttäjän syöttämä lukuarvo
        luku_2 : int
            käyttäjän syöttämä lukuarvo

    Methods
    -------
        yhteenlasku(luku_1, luku_2)
            Palauttaa syötteiden luku_1 ja luku_2 summan
        vahennyslasku(luku_1, luku_2)
            Palauttaa syötteiden luku_1 ja luku_2 erotuksen
        kertolasku(luku_1, luku_2)
            Palauttaa syötteiden luku_1 ja luku_2 tulon
        jakolasku(luku_1, luku_2)
            Palauttaa syötteiden luku_1 ja luku_2 osamäärän
    """

    def __init__(self):
        """
        Laskin-luokan konstruktori

        Parameters
        ----------
            None
        Examples:
            >>> laskin = Laskin()
            >>> type(laskin) is Laskin
            True
        """


    def yhteenlasku(self, luku_1: int, luku_2: int) -> int:
        """
        Tämä metodi laskee luvut yhteen
        Args:
            luku_1 (int): kokonaisluku
            luku_2 (int): kokonaisluku
        Returns:
            summa: kokonaislukujen luku_1 ja luku_2 summa
        Examples:
            >>> laskin = Laskin()
            >>> laskin.yhteenlasku(2, 5)
            7
            7
        """
        print(luku_1+luku_2)
        return luku_1+luku_2

    def vahennyslasku(self, luku_1: int, luku_2: int) -> int:
        """
        Tämä metodi palauttaa kahden kokonaisluvun erotuksen
        Args:
            luku_1 (int): kokonaisluku
            luku_2 (int): kokonaisluku
        Returns:
            erotus: kokonaislukujen luku_1 ja luku_2 erotus
        Examples:
            >>> laskin = Laskin()
            >>> laskin.vahennyslasku(5, 2)
            3
            3
        """
        print(luku_1-luku_2)
        return luku_1-luku_2

    def kertolasku(self, luku_1: int, luku_2: int) -> int:
        """
        Tämä metodi palauttaa kahden kokonaisluvun tulon
        Args:
            luku_1 (int): kokonaisluku
            luku_2 (int): kokonaisluku
        Returns:
            tulo: kokonaislukujen luku_1 ja luku_2 tulo
        Examples:
            >>> laskin = Laskin()
            >>> laskin.kertolasku(2, 5)
            10
            10
        """
        print(luku_1*luku_2)
        return luku_1*luku_2

    def jakolasku(self, luku_1: int, luku_2: int) -> float:
        """
        Tämä metodi jakaa kokonaisluvun toisella kokonaisluvulla.
        Args:
            luku_1 (int): kokonaisluku
            luku_2 (int): kokonaisluku
        Returns:
            osamäärä (float): kokonaislukujen luku_1 ja luku_2 osamäärä
            virhe (ZeroDivisionError): jos luku_2 on nolla
        Examples:
            >>> laskin = Laskin()
            >>> laskin.jakolasku(10, 2)
            5.0
            5.0
            >>> laskin = Laskin()
            >>> laskin.jakolasku(10, 0)
            Virhe: 0 ei voi olla jakaja
            <class 'ZeroDivisionError'>
        """
        try:
            print(float(luku_1/luku_2))
            return float(luku_1/luku_2)
        except ZeroDivisionError:
            print("Virhe: 0 ei voi olla jakaja")
            return ZeroDivisionError

if __name__ == "__main__":
    import doctest
    doctest.testmod()
